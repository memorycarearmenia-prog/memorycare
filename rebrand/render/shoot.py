#!/usr/bin/env python3
"""Render every built page to PNG, in the audit's naming, and verify each file.

Screenshots are not drawn by hand. They fall out of the real implementation,
which is the only way 22 routes x 3 locales can be covered honestly — and it
means a screenshot cannot drift from the code it depicts.

Naming matches docs/site-audit-2026-09-02/screens/ exactly, so before and
after sort side by side in a directory listing.
"""
import json, os, struct, subprocess, sys, threading, functools, http.server, socketserver
from pathlib import Path

ROOT   = Path('/home/user/memorycare/rebrand')
SITE   = ROOT / 'site'
OUT    = ROOT / 'render' / 'screens'
CHROME = '/opt/pw-browsers/chromium'
PORT   = 8791
BASE   = f'http://127.0.0.1:{PORT}'

# The pages use root-relative asset paths — correct for production, and they
# resolve to the filesystem root under file://, which silently renders every
# page unstyled. Serve over HTTP so what is captured is what ships.
def serve(directory, port):
    handler = functools.partial(http.server.SimpleHTTPRequestHandler,
                                directory=str(directory))
    class Quiet(socketserver.TCPServer):
        allow_reuse_address = True
    httpd = Quiet(('127.0.0.1', port), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd
WIDTHS = [360, 1024, 1280, 1440, 1920]
FOLD   = {360: 640, 1024: 768, 1280: 800, 1440: 900, 1920: 1080}
LOCALES = ['am', 'ru', 'en']

# file path -> route name used in the audit, so the pairs line up
ROUTES = {
    'index.html':                 'home',
    'how-it-works.html':          'how-it-works',
    'prices.html':                'prices',
    'sample-report.html':         'sample-report',
    'contact.html':               'contact',
    '404.html':                   'notfound-tpl',
    'about.html':                 'about',
    'history.html':               'nav-history',
    'mission.html':               'nav-mission',
    'values.html':                'nav-values',
    'legal/restrictions.html':    'legal-restrictions',
    'legal/privacy.html':         'legal-privacy',
    'legal/cookies.html':         'legal-cookies',
    'legal/refunds.html':         'legal-refunds',
    'legal/terms.html':           'legal-terms',
    'legal/security.html':        'legal-security',
    'account/index.html':         'acct-dashboard',
    'account/plots.html':         'acct-objects',
    'account/plot-new.html':      'acct-plot-new',
    'account/order.html':         'acct-order',
    'account/packages.html':      'acct-packages',
    'account/payments.html':      'acct-payments',
    'account/profile.html':       'acct-profile',
    'account/login.html':         'login',
    'account/register.html':      'register',
    'account/reset.html':         'reset',
}

def png_size(p):
    with open(p, 'rb') as f:
        head = f.read(24)
    if head[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    return struct.unpack('>II', head[16:24])

def stddev(p):
    """Per-channel standard deviation. A blank or single-colour capture fails
    this, which is the failure that otherwise passes for a real file."""
    try:
        from PIL import Image, ImageStat
        return round(max(ImageStat.Stat(Image.open(p).convert('RGB')).stddev), 2)
    except Exception:
        return None

def shoot(url, dest, width, height, full):
    args = [CHROME, '--headless', '--disable-gpu', '--no-sandbox',
            '--hide-scrollbars', '--force-device-scale-factor=1',
            '--font-render-hinting=none', '--virtual-time-budget=4000',
            f'--window-size={width},{height}',
            f'--screenshot={dest}']
    if full:
        args.insert(-1, '--screenshot-full-page' if False else '--hide-scrollbars')
    args.append(url)
    r = subprocess.run(args, capture_output=True, text=True, timeout=180)
    return r.returncode == 0 and os.path.exists(dest)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    httpd = serve(SITE, PORT)
    # Fail loudly rather than capture 780 unstyled pages.
    import urllib.request
    for probe in ('/assets/tokens.css', '/assets/base.css', '/assets/components.css'):
        with urllib.request.urlopen(BASE + probe, timeout=10) as r:
            assert r.status == 200 and int(r.headers.get('content-length', 0)) > 1000, probe
    print('stylesheets reachable — capturing against HTTP, not file://')
    log, manifest, missing = [], {}, []

    for rel, route in ROUTES.items():
        for loc in LOCALES:
            src = SITE / loc / rel
            if not src.exists():
                missing.append(f'{loc}/{rel}')
                continue
            url = f'{BASE}/{loc}/{rel}'
            for w in WIDTHS:
                for state, h in (('default-fold', FOLD[w]), ('default-full', 20000)):
                    name = f'{route}__{loc}__{w}__{state}.png'
                    dest = OUT / name
                    ok = shoot(url, str(dest), w, h, state.endswith('full'))
                    if not ok:
                        log.append({'file': name, 'ok': False, 'reason': 'capture failed'})
                        continue
                    dim = png_size(dest)
                    sd  = stddev(dest)
                    b   = os.path.getsize(dest)
                    entry = {
                        'file': name, 'bytes': b,
                        'w': dim[0] if dim else 0, 'h': dim[1] if dim else 0,
                        'stddev': sd,
                        'bytesOk':  b > 2000,
                        'varianceOk': (sd or 0) > 3.0,
                        'widthOk':  bool(dim) and dim[0] == w,
                    }
                    entry['ok'] = all([entry['bytesOk'], entry['varianceOk'], entry['widthOk']])
                    log.append(entry)
                    manifest.setdefault(route, {}).setdefault(loc, {}).setdefault(str(w), {})[state] = name

    (ROOT / 'render' / 'capture-log.json').write_text(
        json.dumps({'captured': log, 'missingPages': missing}, indent=2, ensure_ascii=False))
    (ROOT / 'render' / 'manifest.json').write_text(
        json.dumps({'routes': manifest, 'widths': WIDTHS, 'locales': LOCALES}, indent=2, ensure_ascii=False))

    total = len(log)
    bad   = [e for e in log if not e.get('ok')]
    print(f'captured        : {total}')
    print(f'failed checks   : {len(bad)}')
    print(f'pages missing   : {len(missing)}')
    for e in bad[:12]:
        print('   ', e['file'], {k: v for k, v in e.items()
              if k in ('bytesOk','varianceOk','widthOk','w','bytes','stddev','reason')})
    if missing[:8]:
        print('   not built yet:', missing[:8])
    # A width mismatch on a full capture is the site scrolling sideways,
    # not a bad screenshot. That distinction caught a real bug in the audit.
    wrong_w = [e for e in log if e.get('widthOk') is False]
    if wrong_w:
        print(f'\nHORIZONTAL SCROLL — {len(wrong_w)} captures wider than their viewport:')
        for e in wrong_w[:10]:
            print(f"    {e['file']}  {e['w']}px in a viewport of {e['file'].split('__')[2]}px")

if __name__ == '__main__':
    main()
