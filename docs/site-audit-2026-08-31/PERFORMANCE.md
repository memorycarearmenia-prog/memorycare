# PERFORMANCE

## How these numbers were produced, and what they are worth

Two sources, deliberately kept apart:

**Lighthouse 12 (mobile profile) was run against a byte-exact local mirror of the site**, not
against `mc.makyan.com`. The sandbox this audit ran in is blocked from that origin by network
policy. The mirror was taken from the live site through the browser: every one of the 48 documents
and all 51 same-origin and third-party assets, unmodified except for rewriting absolute URLs to
local paths.

What that means for the numbers below:

- **Byte weights, request counts, asset dimensions and unused-code estimates are real.** They come
  from the same files the live site serves.
- **The scores and the timings are optimistic and should not be quoted.** `server-response-time`
  reads 0 ms because a local static server answered. Lighthouse's simulated throttling still applies
  to transfer, but there is no real network in front of it. The performance scores of 94–100 below
  are what this page weight would achieve *if the server were instant and the network were the
  simulated one*. They are recorded for completeness, not as a claim about the live site.
- **Live timings were measured separately**, from the user's own browser against the real origin.

To get real Lighthouse numbers, someone on a machine that can reach the origin should run:

```
npx lighthouse https://mc.makyan.com/am/page/home/ --form-factor=mobile \
  --throttling-method=devtools --output=html --output-path=./lh-home-am.html
```

## Live measurements against the real origin

Taken in Chrome against `https://mc.makyan.com`, Yerevan, on a desktop connection:

| Metric | Value |
|---|---|
| TTFB, `/am/page/home/` | 85 ms |
| DOMContentLoaded | 1,504 ms |
| Load event | 1,544 ms |
| HTML document, `/am/page/home/` | 23 KB |
| HTML document, `/en/page/home/` | 24 KB |
| HTML document, `/am/contact/` | 6 KB |
| Same-origin assets on the home page | **3,746 KB over 29 requests** |
| Third-party files on the home page | 5 (four CDNs plus Google Fonts) |

The server itself is quick. The weight is the problem.

## Lighthouse, mobile profile, against the mirror

| Route | Perf | A11y | Best practices | SEO | FCP | LCP | TBT | CLS | Total bytes |
|---|---|---|---|---|---|---|---|---|---|
| `/am/page/home/` | 94 | 81 | 96 | 75 | 671 ms | 2,058 ms | 273 ms | 0.000 | **4,661 KiB** |
| `/ru/page/home/` | 97 | 81 | 96 | 75 | 670 ms | 2,006 ms | 151 ms | 0.000 | 4,660 KiB |
| `/en/page/home/` | 98 | 81 | 96 | 67 | 671 ms | 2,075 ms | 135 ms | 0.000 | **5,730 KiB** |
| `/am/contact/` | 100 | 69 | 96 | 75 | 631 ms | 1,041 ms | 0 ms | 0.000 | 800 KiB |
| `/am/account/login/` | 100 | 67 | 96 | 58 | 631 ms | 1,061 ms | 0 ms | 0.000 | 800 KiB |

CLS is genuinely 0.000 — the layout does not shift. That is the one thing this build does well.

## Where the weight goes

### Home page, Armenian — the eight heaviest requests

| Size | Asset | Comment |
|---|---|---|
| **2,327 KB** | `/uploads/files/video/v.mp4` | An `autoplay` video rendered into a 558 × 464 box. `preload="metadata"`, but it autoplays, so it downloads. Half the page. |
| **601 KB** | `three.js` r134 | Loaded solely so `vanta.clouds` can paint the decorative sky behind the hero. |
| **276 KB** | `/img/logo.png` | A **500 × 500 PNG displayed at 60 × 60** in the header. On every page of the site, including the 404 panel. |
| 221 KB | `/uploads/images/other/03.jpg` | 800 × 600 JPEG |
| 192 KB | `/uploads/images/ba/01/before.webp` | before/after slider |
| 151 KB | `swiper-bundle.min.js` | |
| 143 KB | `/uploads/images/other/04.jpg` | |
| 133 KB | `/uploads/images/ba/01/after.webp` | |

### Home page, English — why it is 1 MB heavier

The English carousel uses a different image set: `slider/05.webp` **545 KB**, `slider/02.webp`
268 KB, `slider/04.webp` 260 KB, none of which loads on the Armenian or Russian pages. The
English page is 5,730 KiB against 4,661 KiB — the same page, 23% heavier, because of the slide
images alone.

### Every page, including the empty ones

`/am/account/login/` — a form with two fields — ships **800 KiB**, of which 276 KB is the
oversized logo, 151 KB is Swiper, 94 KB is jQuery, 26 KB is AOS and 25 KB is BeerSlider. None of
those four libraries does anything on that page. The same is true of the 404 panel.

### Unused code

| Route | Unused JavaScript | Unused CSS |
|---|---|---|
| `/am/page/home/` | 500 KiB | 73 KiB |
| `/en/page/home/` | 497 KiB | 70 KiB |
| `/am/contact/` | 179 KiB | 88 KiB |

Magnific Popup (`js/popup.js` 20 KB + `css/popup.css` 7 KB) is loaded on every page and bound to
four selectors — `.igallery`, `.si`, `.popup-modal`, `.popup-youtube` — none of which matches any
element on any of the 48 documents. It never runs.

## Third-party origins

| Origin | What | Pinned |
|---|---|---|
| `code.jquery.com` | `jquery-latest.min.js`, 94 KB | **no** — and the jQuery CDN froze this filename in 2014, so it is not the latest release |
| `cdn.jsdelivr.net` | `vanta@latest/dist/vanta.clouds.min.js` | **no** — resolves at request time |
| `cdn.jsdelivr.net` | `swiper@11/swiper-bundle.min.{js,css}` | major version only |
| `cdnjs.cloudflare.com` | `three.js/r134/three.min.js`, 601 KB | yes |
| `fonts.googleapis.com` / `fonts.gstatic.com` | Plus Jakarta Sans, weights 200–800, both italics | — |
| `google.com/maps/embed` | contact page iframe | — |

No Subresource Integrity attribute on any of them. Six third-party origins on a page that will
eventually take card payments.

A note on the font: Plus Jakarta Sans is loaded across the full 200–800 range in both roman and
italic, and **it carries no Armenian glyphs**. Armenian text falls back to a system face — which is
why the price element resolves to `system-ui, -apple-system, "Helvetica Neue", Arial` rather than
the loaded family. The primary market's script is rendered by whatever the device happens to have.

## What would move the needle, in order

1. Remove or lazy-load the 2.3 MB autoplay video — 50% of the home page.
2. Replace the 500 × 500 logo PNG with a ~4 KB SVG — 276 KB off **every page on the site**.
3. Drop `three.js` + `vanta.clouds` (601 KB) unless the animated sky is a deliberate brand decision;
   a static gradient is indistinguishable at 360.
4. Load Swiper, AOS, BeerSlider and Magnific Popup only on pages that use them — 800 KiB → under
   200 KiB on the login, register, reset and 404 pages.
5. Serve the English slider images at the sizes they render.

Items 1–3 alone take the Armenian home page from 4.66 MB to roughly 1.5 MB.

## Not measured

- Real-network Lighthouse against the origin (command above).
- Response headers: compression, caching, HTTP version, TLS. `curl -sSI https://mc.makyan.com/am/page/home/`.
- Field data. The site has no analytics and no real users yet.
- Anything under authentication beyond the two account pages captured in the mirror.

## Addendum — caching is defeated at the source

The local CSS and JS are referenced with a query string that is `time()` at render, not a build
hash: two documents fetched seconds apart in the same mirror run carry `css/style.css?1788207401`
and `css/style.css?1788207403`. Every page view therefore re-downloads `style.css` (50 KB),
`aos.css` (26 KB), `init.js` (27 KB), `BeerSlider.js` (25 KB) and `popup.js` (20 KB), no matter how
many pages the visitor has already seen. Nothing above about page weight assumes a warm cache,
because on this build there is never a warm cache. Recorded as FINDINGS #41.
