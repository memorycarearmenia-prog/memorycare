# ACCESSIBILITY

Method, so the numbers can be reproduced or disputed:

- **axe-core 4.10.2**, injected into each rendered page and run with the tag set
  `wcag2a, wcag2aa, wcag21a, wcag21aa, best-practice`, across **6 routes × 3 locales = 18 pages**,
  at 1440×900, after a full scroll pass so lazy content had rendered. Raw results:
  `measurements.json` → `<route>__<locale>.axe`.
- **Contrast measured on rendered output, not on token pairs.** Two methods, both reported:
  for text on a solid colour, the ratio is computed from the element's own resolved colour and the
  first opaque background painted behind it; for text on a photograph, the element itself is
  screenshotted and the ratio computed from the glyph pixels against the background pixels of that
  same image. The second method exists because the first cannot see an image and silently returns
  white — it produced two false failures on the English home page during this audit, which is why
  the pixel method was added rather than the computed-style result being reported.
- **Keyboard walk** by pressing Tab, never by clicking, with a capture at each of the first four
  stops.
- **Type and hit areas measured at 360**, from the rendered layout, including invisible padding
  (`getBoundingClientRect`).

---

## 1 · axe violations, all 18 pages

| Rule | Impact | Nodes (sum over 18 pages) | Pages affected | Example target |
|---|---|---|---|---|
| `image-alt` | critical | 198 | 18 | `a[href=""] > img[src$="logo.png"]`, `.back-to-top`, `.n5 > img[src$="03.jpg"]` |
| `region` | moderate | 142 | 18 | `#ms_clouds`, `.numbers_wrap`, `body > a[href="javascript:void(0)"]` |
| `link-name` | serious | 126 | 18 | `.logo > a[href=""]`, `li:nth-child(1) > a[href="#"][target="_blank"]` |
| `aria-prohibited-attr` | serious | 18 | 3 (home ×3 locales) | `.stars-display[aria-label="Rating"]` |
| `meta-viewport` | critical | 18 | 18 | `meta[name="viewport"]` — zoom disabled |
| `landmark-one-main` | moderate | 17 | 17 | `html` |
| `page-has-heading-one` | moderate | 17 | 17 | `html` |
| `document-title` | serious | 9 | 9 | login, register, reset — all three locales |
| `color-contrast` | serious | 3 | 3 | `.nothing` on the 404 panel |
| `frame-title` | serious | 3 | 3 | the Google Maps `iframe` on the contact page |
| `button-name` | critical | 2 | 1 | `.nav-left`, `.nav-right` — the carousel controls |

Nothing here is locale-specific except `aria-prohibited-attr`, which only appears where the reviews
carousel appears. The Armenian, Russian and English builds fail identically.

Lighthouse's own accessibility category, mobile profile: **81** on the home page in all three
locales, **69** on contact, **67** on login.

## 2 · Contrast

### Measured on solid backgrounds (computed styles, reliable)

| Where | Foreground on background | Size | Ratio | Required | Verdict |
|---|---|---|---|---|---|
| `.ctry`, testimonial country line, home | `rgb(204,204,204)` on `rgb(248,248,248)` | 12px | **1.51** | 4.5 | fail |
| `.nothing`, the 404 panel message | `rgb(187,187,187)` on `rgb(255,255,255)` | 16px | **1.92** | 4.5 | fail |
| Package card titles, cards 1, 2, 4 | white on `rgb(90,92,95)` | 19px | 6.74 | 4.5 | pass |
| Package card title, card 3 | white on the olive header | 19px | 5.29 | 4.5 | pass |
| Footer headings (`Հասցե`, `Адрес`, `Address`) | white on the footer grey | 18.72px | 7.03 | 3.0 | pass |
| Footer body and links | white on the footer grey | 14–16px | 6.5–7.03 | 4.5 | pass |
| Primary buttons (`Իմանալ ավելին`, `Заказать`, `Order`) | white on olive | 15px | 5.14–5.43 | 4.5 | pass |

### Measured on photographs (element screenshot, pixel-based)

| Where | Size | Median ratio | Ratio over the brightest tenth of the background | Required | Verdict |
|---|---|---|---|---|---|
| English carousel caption, above the footer | 18px | **3.20** | 2.36 | 4.5 | **fail** |
| English carousel heading, same slide | 65px bold | 3.02 | 2.36 | 3.0 | marginal — passes on average, fails over the bright part of the image |

Both sit on an unscrimmed photograph inside a carousel, so the ratio moves as slides change. The
Armenian and Russian versions of that carousel use different images and did not fail.

**Note on the olive.** The project's own brandbook records that Olive `#7C8654` gives 3.42 against
Ivory and 3.12 against Nude, below the 4.5 threshold, and that "no text is legible on Olive". The
olive rendered on this build measures darker than `#7C8654` and the white button labels clear 4.5.
Either the build is not using the official brand olive, or the brandbook value has moved. Worth
resolving before the brand palette is applied properly, but it is not a failure as built.

## 3 · Keyboard walk

Captured: `home__am__1440__focus-visible-tab1.png` … `tab4.png`.

**The first stop is an unlabelled control.** Tab 1 lands on `<a href="javascript:void(0)">` wrapping
`<img class="back-to-top">` with no `alt` — the first thing a keyboard user meets has no name and no
purpose at the top of a page. There is no skip link.

**Focus enters submenus that are not visible.** `nav li.has-children ul` computes to
`opacity: 0; pointer-events: none` but stays `display: block` and `visibility: visible`, so its links
remain in the tab order. On the Armenian home page the tab sequence runs
`Գլխավոր → Մեր մասին → Պատմություն → Առաքելություն → Արժեքներ → Նորություններ → Լուրեր → …`:
five of the first eleven stops are invisible, and three of them lead to 404 panels. The focus
indicator moves to a place the user cannot see. This is WCAG 2.4.3 Focus Order and 2.4.7
Focus Visible together, and it is also why the measured "out of visual order" count is 3 of 37 —
the submenu items sit below the bar they belong to.

**Focus is visible on links, invisible in fields.** Navigation links take a faint outline
(`tab1`–`tab4`). Text inputs take nothing at all: `contact__am__1440__form-empty.png` and
`contact__am__1440__form-focus-first-field.png` are byte-identical at 92,651 bytes, and the Russian
and English pairs likewise. A keyboard user filling the contact form cannot tell which field is
active.

**Nothing traps focus**, because there is nothing to trap it in: the mobile menu is the only
overlay, and it does not move focus into itself when opened or restore it when closed. Opening the
menu at 360 and pressing Tab continues from wherever focus already was, behind the panel.

**Five dead links in the footer.** `<a href="#" target="_blank"><img src="/img/icons/sh-fb.svg"></a>`
and four more — no `alt`, no `aria-label`, no destination. They are focusable, unnamed, and do
nothing.

## 4 · Type floors, measured at 360

| Rule from the brief | Measured | Verdict |
|---|---|---|
| Nothing under 13px | `.ctry` at **12px** (one string, the testimonial country) | fail, one element |
| Informational text 14px or more | 24 elements at 13px | borderline pass |
| Body 16px on mobile | **225 elements at 15px, 132 at 14px** | fail — the body of the site sits one to two steps below the floor |

With zoom disabled (FINDINGS #7) this cannot be worked around by the reader.

## 5 · Hit areas, measured at 360, including padding

| Control | Measured | Required |
|---|---|---|
| `.menu-toggle` (hamburger) | **28 × 27** | 44 × 44 |
| `ՀԱՅ` | **33.2 × 22.5** | 44 × 44 |
| `РУС` | **28.7 × 22.5** | 44 × 44 |
| `ENG` | **32.3 × 22.5** | 44 × 44 |
| `.swiper-button-prev` / `-next` | **27 × 44** | 44 × 44 |
| `.sp.btn` — the package order button | 205.2 × **30.9** | 44 tall |
| Footer phone link | 129.3 × **16** | 44 tall |
| Footer e-mail link | 155.8 × **16** | 44 tall |
| "Forgot your password?" | 147.5 × **19.5** | 44 tall |
| "Don't have an account? Register…" | 270 × 39 (Russian, wraps to two lines) | 44 tall |
| The broken floating button | **40 × 40** | 44 × 44 |

The three language links are the worst case: 22.5px tall, side by side, a few pixels apart, and they
are the control a diaspora visitor reaches for first.

## 6 · What was not tested

- **No screen reader was run.** The findings above are structural (missing names, missing landmarks,
  wrong `lang`) and are what a screen reader would stumble on, but the experience itself was not
  heard. Someone should walk the header, the package cards and the contact form with NVDA or
  VoiceOver.
- **Only Chromium 141 was used.** Armenian text shaping differs between engines; Safari and Firefox
  were not checked.
- **Reduced-motion preference was set for capture** but the site's response to it was not evaluated
  separately. The Vanta cloud background animates continuously and is not gated on
  `prefers-reduced-motion`; that is worth a check with the preference honoured rather than forced.
- **Zoom to 200% and 400% reflow** (WCAG 1.4.10) was not measured, because zoom is disabled at the
  viewport level, which fails 1.4.4 before reflow becomes testable.
