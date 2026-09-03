#!/usr/bin/env python3
"""Render every built page to PNG, in the audit's naming, and verify each file.

Screenshots are not drawn by hand. They fall out of the real implementation —
the only way 26 routes x 3 locales can be covered honestly, and it means a
screenshot cannot drift from the code it depicts.

Two things this script refuses to do quietly:
  * capture over file:// — the pages use root-relative asset paths, correct for
    production, which resolve to the filesystem root under file:// and render
    every page unstyled. An unstyled page still passes a size-and-variance
    check, so 780 worthless captures would look like a clean run. It serves
    over HTTP and asserts the stylesheets are reachable before shooting.
  * treat a width mismatch as a capture fault — on a full-page capture it means
    the SITE scrolls sideways. That distinction found a real bug in the 02.09
    audit, so it is reported as a site defect, not silently re-shot.
"""
import functools, http.server, json, os, socketserver, struct, sys, threading
from pathlib import Path
from multiprocessing import Pool

os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
from playwright.sync_api import sync_playwright
from PIL import Image, ImageStat

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'site'
OUT  = ROOT / 'render' / 'screens'
PORT = 8899
BASE = f'http://127.0.0.1:{PORT}'
WIDTHS  = [360, 1024, 1280, 1440, 1920]
FOLD    = {360: 640, 1024: 768, 1280: 800, 1440: 900, 1920: 1080}
LOCALES = ['am', 'ru', 'en']

ROUTES = {
    'index.html': 'home', 'how-it-works.html': 'how-it-works',
    'prices.html': 'prices', 'sample-report.html': 'sample-report',
    'contact.html': 'contact', '404.html': 'notfound-tpl',
    'about.html': 'about', 'history.html': 'nav-history',
    'mission.html': 'nav-mission', 'values.html': 'nav-values',
    'legal/restrictions.html': 'legal-restrictions',
    'legal/privacy.html': 'legal-privacy', 'legal/cookies.html': 'legal-cookies',
    'legal/refunds.html': 'legal-refunds', 'legal/terms.html': 'legal-terms',
    'legal/security.html': 'legal-security',
    'account/index.html': 'acct-dashboard', 'account/plots.html': 'acct-objects',
    'account/plot-new.html': 'acct-plot-new', 'account/order.html': 'acct-order',
    'account/packages.html': 'acct-packages', 'account/payments.html': 'acct-payments',
    'account/profile.html': 'acct-profile', 'account/login.html': 'login',
    'account/register.html': 'register', 'account/reset.html': 'reset',
}

# Three account pages carry both of their states in one file: one rendered
# live, the other parked in an inert <template>. The parked one is real,
# reviewed markup that no default capture can ever show — the plots and
# payments tables would be absent from the whole archive. These captures
# reveal it: drop the live block, inline the template, shoot again.
ALT_STATE = {'acct-objects': 'populated', 'acct-payments': 'populated',
             'acct-packages': 'empty'}

REVEAL_JS = """(want) => {
  const tpl = document.querySelector('template[data-state="' + want + '"]');
  if (!tpl) return false;
  const live = tpl.previousElementSibling &&
               tpl.previousElementSibling.closest('.mc-empty, .mc-table-region');
  if (live) live.remove();
  tpl.replaceWith(tpl.content.cloneNode(true));
  return true;
}"""


def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
    class Quiet(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
        def log_message(self, *a): pass
    httpd = Quiet(('127.0.0.1', PORT), h)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd

def verify(path, want_w):
    with open(path, 'rb') as f:
        head = f.read(24)
    if head[:8] != b'\x89PNG\r\n\x1a\n':
        return {'ok': False, 'reason': 'not a PNG'}
    w, h = struct.unpack('>II', head[16:24])
    b = os.path.getsize(path)
    sd = round(max(ImageStat.Stat(Image.open(path).convert('RGB')).stddev), 2)
    e = {'bytes': b, 'w': w, 'h': h, 'stddev': sd,
         'bytesOk': b > 2000, 'varianceOk': sd > 3.0, 'widthOk': w == want_w}
    e['ok'] = e['bytesOk'] and e['varianceOk'] and e['widthOk']
    return e

def shoot_one(job):
    rel, route, loc, w = job
    out = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium',
                                     args=['--no-sandbox', '--font-render-hinting=none',
                                           '--no-proxy-server', '--proxy-bypass-list=<-loopback>'])
        ctx = browser.new_context(viewport={'width': w, 'height': FOLD[w]},
                                  device_scale_factor=1, reduced_motion='reduce')
        pg = ctx.new_page()
        try:
            pg.goto(f'{BASE}/{loc}/{rel}', wait_until='networkidle', timeout=60000)
            pg.evaluate("document.fonts.ready")
            pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            pg.wait_for_timeout(150)
            pg.evaluate("window.scrollTo(0, 0)")
            pg.wait_for_timeout(100)
            for state, full in (('default-fold', False), ('default-full', True)):
                name = f'{route}__{loc}__{w}__{state}.png'
                dest = OUT / name
                pg.screenshot(path=str(dest), full_page=full)
                e = verify(dest, w); e['file'] = name
                out.append((route, loc, w, state, name, e))

            if route in ALT_STATE:
                want = ALT_STATE[route]
                assert pg.evaluate(REVEAL_JS, want), f'{route}: no template[{want}]'
                pg.wait_for_timeout(80)
                for state, full in ((f'state-{want}-fold', False),
                                    (f'state-{want}-full', True)):
                    name = f'{route}__{loc}__{w}__{state}.png'
                    dest = OUT / name
                    pg.screenshot(path=str(dest), full_page=full)
                    e = verify(dest, w); e['file'] = name
                    out.append((route, loc, w, state, name, e))
        finally:
            browser.close()
    return out

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    serve()
    import urllib.request
    # The environment routes HTTP through an egress proxy; a request to our own
    # loopback server would go out to it and come back 404. Bypass it explicitly
    # for both urllib and Chromium, or this assertion fails on a healthy server.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    for probe in ('/assets/tokens.css', '/assets/base.css', '/assets/components.css'):
        with opener.open(BASE + probe, timeout=10) as r:
            n = len(r.read())
            assert r.status == 200 and n > 1000, f'{probe} -> {r.status}, {n} bytes'
    print('stylesheets reachable — capturing over HTTP, not file://', flush=True)

    jobs = [(rel, route, loc, w)
            for rel, route in ROUTES.items() for loc in LOCALES for w in WIDTHS
            if (SITE / loc / rel).exists()]
    log, manifest = [], {}
    lock = threading.Lock()

    # Playwright's sync API is not thread-safe — a ThreadPoolExecutor over one
    # browser raises "cannot switch to a different thread". Parallelise with
    # PROCESSES, each owning its own Playwright instance; they all talk to the
    # one HTTP server running in this parent.
    with Pool(processes=5) as pool:
        for i, res in enumerate(pool.imap_unordered(shoot_one, jobs), 1):
            for route, loc, w, state, name, e in res:
                log.append(e)
                manifest.setdefault(route, {}).setdefault(loc, {}).setdefault(str(w), {})[state] = name
            if i % 20 == 0:
                print(f'  {i}/{len(jobs)} page-widths', flush=True)

    (ROOT/'render'/'capture-log.json').write_text(json.dumps({'captured': log}, indent=2))
    (ROOT/'render'/'manifest.json').write_text(json.dumps(
        {'routes': manifest, 'widths': WIDTHS, 'locales': LOCALES,
         'note': 'am is the URL segment; the language is hy'}, indent=2, ensure_ascii=False))

    bad = [e for e in log if not e['ok']]
    wide = [e for e in log if not e['widthOk']]
    print(f'\ncaptured        : {len(log)}')
    print(f'failed checks   : {len(bad)}')
    print(f'blank / uniform : {len([e for e in log if not e["varianceOk"]])}')
    print(f'under 2000 bytes: {len([e for e in log if not e["bytesOk"]])}')
    if wide:
        print(f'\nHORIZONTAL SCROLL — {len(wide)} captures wider than their viewport (a SITE defect):')
        for e in wide[:12]:
            print(f"    {e['file']}  {e['w']}px")
if __name__ == '__main__':
    main()
