#!/usr/bin/env python3
"""Extract a paint tree from a built page, for rebuilding it as Figma layers.

Screens in Figma are generated from the same DOM the screenshots are taken
from, so they cannot drift from the code. Only nodes that PAINT something are
kept -- a background, a border, or a run of text of their own. Everything else
is layout scaffolding that Figma does not need and that would bury the file in
empty frames.
"""
import functools, http.server, json, os, socketserver, sys, threading
from pathlib import Path

os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'site'
OUT  = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/tmp/layout')
WIDTH = 1440

JS = r"""() => {
  const px = v => Math.round(parseFloat(v) || 0);
  const rgba = s => {
    const m = (s || '').match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map(x => parseFloat(x));
    const a = p.length > 3 ? p[3] : 1;
    if (a === 0) return null;
    return {r: p[0]/255, g: p[1]/255, b: p[2]/255, a};
  };
  const SKIP = new Set(['SCRIPT','STYLE','TEMPLATE','HEAD','META','LINK','TITLE','BR','NOSCRIPT']);
  const out = [];
  const walk = (el, depth) => {
    if (SKIP.has(el.tagName)) return;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const r = el.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return;

    const bg = rgba(cs.backgroundColor);

    // Per side. A link's underline is border-block-end alone; taking the max
    // width and one colour would draw a box around every nav item.
    const side = (w, c) => { const n = px(w); const col = n ? rgba(c) : null;
                             return col ? {w: n, c: col} : null; };
    const bd = {
      t: side(cs.borderTopWidth, cs.borderTopColor),
      r: side(cs.borderRightWidth, cs.borderRightColor),
      b: side(cs.borderBottomWidth, cs.borderBottomColor),
      l: side(cs.borderLeftWidth, cs.borderLeftColor),
    };
    const anyBorder = bd.t || bd.r || bd.b || bd.l;
    const uniform = anyBorder && bd.t && bd.r && bd.b && bd.l &&
      bd.t.w === bd.r.w && bd.t.w === bd.b.w && bd.t.w === bd.l.w &&
      JSON.stringify(bd.t.c) === JSON.stringify(bd.b.c);

    // Visually-hidden text (the sr-only pattern) is a 1x1 clipped box: real
    // content for a screen reader, an invisible speck in a design file.
    const hidden = (r.width <= 2 && r.height <= 2) ||
                   (cs.clipPath && cs.clipPath.includes('inset(50%)'));
    const onPage = r.bottom + window.scrollY > 0;

    if ((bg || anyBorder) && !hidden && onPage) {
      out.push({
        tag: el.tagName, cls: (el.className || '').toString().slice(0, 60),
        x: Math.round(r.left + window.scrollX), y: Math.round(r.top + window.scrollY),
        w: Math.round(r.width), h: Math.round(r.height), text: null,
        bg, border: uniform ? {all: bd.t} : (anyBorder ? bd : null),
        radius: px(cs.borderTopLeftRadius),
        color: null, size: null, weight: null, lh: null, ls: null,
        upper: null, align: null, serif: null, depth
      });
    }

    // One entry PER RENDERED LINE of the text this element owns directly.
    // A range that wraps returns a union rect starting on its first line, so
    // an inline name followed by a wrapping role would be drawn on top of it.
    // Splitting by line rect and binary-searching the break offset gives each
    // line its own exact box, and makes every text node single-line.
    if (!hidden && onPage) {
      const serifFirst = /ghea|mariam/i.test(
        cs.fontFamily.split(',').map(f => f.trim().replace(/^["']|["']$/g, ''))
          .filter(f => f !== 'MC Dram')[0] || '');
      const lineCount = rg => Array.from(rg.getClientRects())
        .filter(r => r.width > 0.5 && r.height > 0.5).length;

      for (const node of el.childNodes) {
        if (node.nodeType !== 3) continue;
        if (!node.nodeValue.trim()) continue;
        const full = document.createRange();
        full.selectNodeContents(node);
        const rects = Array.from(full.getClientRects())
          .filter(r => r.width > 0.5 && r.height > 0.5);
        if (!rects.length) continue;

        const len = node.nodeValue.length;
        const lines = [];
        let start = 0;
        for (let i = 0; i < rects.length; i++) {
          if (i === rects.length - 1) { lines.push([rects[i], node.nodeValue.slice(start)]); break; }
          let lo = start + 1, hi = len, best = start + 1;
          while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            const probe = document.createRange();
            probe.setStart(node, start); probe.setEnd(node, mid);
            if (lineCount(probe) <= 1) { best = mid; lo = mid + 1; } else { hi = mid - 1; }
          }
          lines.push([rects[i], node.nodeValue.slice(start, best)]);
          start = best;
        }

        for (const [rr, raw] of lines) {
          const txt = raw.replace(/\s+/g, ' ').trim();
          if (!txt) continue;
          out.push({
            tag: el.tagName, cls: (el.className || '').toString().slice(0, 60),
            x: Math.round(rr.left + window.scrollX), y: Math.round(rr.top + window.scrollY),
            w: Math.ceil(rr.width), h: Math.ceil(rr.height),
            text: txt, bg: null, border: null, radius: 0,
            color: rgba(cs.color), size: Math.round(parseFloat(cs.fontSize)),
            weight: parseInt(cs.fontWeight) || 400,
            lh: Math.round(parseFloat(cs.lineHeight) || 0),
            ls: parseFloat(cs.letterSpacing) || 0,
            upper: cs.textTransform === 'uppercase',
            align: cs.textAlign, serif: serifFirst, depth
          });
        }
      }
    }

    for (const c of el.children) walk(c, depth + 1);
  };
  walk(document.body, 0);
  return {
    w: document.documentElement.clientWidth,
    h: Math.round(document.documentElement.scrollHeight),
    bg: rgba(getComputedStyle(document.body).backgroundColor),
    nodes: out
  };
}"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
    class Quiet(socketserver.ThreadingTCPServer):
        allow_reuse_address = True
    httpd = Quiet(('127.0.0.1', 0), h)
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()

    routes = json.loads((ROOT / 'render' / 'manifest.json').read_text())['routes']
    rel_of = {}
    for rel in sorted(p.relative_to(SITE / 'en').as_posix()
                      for p in (SITE / 'en').rglob('*.html')):
        rel_of[rel] = rel

    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium',
                               args=['--no-sandbox', '--no-proxy-server',
                                     '--proxy-bypass-list=<-loopback>'])
        ctx = b.new_context(viewport={'width': WIDTH, 'height': 900},
                            device_scale_factor=1, reduced_motion='reduce')
        pg = ctx.new_page()
        total = 0
        for rel in rel_of:
            pg.goto(f'http://127.0.0.1:{port}/en/{rel}', wait_until='networkidle', timeout=60000)
            pg.evaluate('document.fonts.ready')
            data = pg.evaluate(JS)
            data['route'] = rel
            name = rel.replace('/', '__').replace('.html', '')
            (OUT / f'{name}.json').write_text(json.dumps(data, ensure_ascii=False))
            total += len(data['nodes'])
            print(f'{rel:34} {len(data["nodes"]):5} nodes  {data["h"]:6}px', flush=True)
        b.close()
    print(f'\ntotal paint nodes: {total}')


if __name__ == '__main__':
    main()
