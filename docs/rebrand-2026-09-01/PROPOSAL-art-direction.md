# PROPOSAL — Art direction

Slot: art director. Written 2026-09-01 against `BRIEF.md` (31.08 brandbook),
`docs/site-audit-2026-08-31/FINDINGS.md`, brandbook pages 2–4,
`assets/brand/logo-v6/README.md`, and the ten contact sheets in
`docs/site-audit-2026-08-31/sheets/`.

**Note on evidence.** `docs/site-audit-2026-08-31/screens/` (the 242 individual
PNGs) is **not present in this working copy** — `README.md` lists it, the
directory does not exist. I reviewed the ten contact sheets instead, which
carry the same frames at reduced size: `fold-home.png` (home, am/ru/en ×
360/768/1024/1440/1920), `fold-login.png`, `fold-register.png`,
`fold-contact.png`, `fold-history.png`, `fold-reset.png`, `states-forms.png`,
`states-menu.png`, `states-focus-slider.png`, `spot-1440.png`. That covers home
at 360 and 1440 in all three locales and every form route, which is what was
asked. Anything below that I could not read at contact-sheet scale is marked as
such rather than guessed.

**Note on file location.** `BRIEF.md` lives at
`docs/site-audit-2026-08-31/docs/rebrand-2026-09-01/BRIEF.md`. I was told to
deliver to `docs/rebrand-2026-09-01/PROPOSAL-art-direction.md`, so that is where
this is. If the lead is collecting proposals next to the brief, this file needs
moving; I have not created a second copy.

---

## 0. What is actually wrong, in one paragraph

The build is not off-brand at the margins — it has no brand in it. The hero is
an animated Vanta cloud sky behind a translucent glass card (`fold-home.png`,
every locale, every width): sky, clouds, soft blue, ascending light. That is
the single most literal afterlife cliché available, arrived at by accident, and
it is the first two seconds a visitor gets. The header carries a **superseded
circular mandala mark**, not the 31.08 hands-and-forget-me-not (`fold-login.png`,
`spot-1440.png` footer crops). Buttons are an Olive fill with a white label —
Ivory on Olive measures 3.42, so the primary action on the site fails contrast
by construction. Inputs are underlines with no labels and no visible focus
(`states-forms.png`; FINDINGS #10, #24). The footer is a cool neutral grey with
no relationship to any brand colour. At 1440 and 1920 the pages are a small
centred card in a field of dead white (`fold-login.png`, `spot-1440.png` — the
1920 column is almost entirely empty), and four routes render a 404 panel whose
own message measures 1.92 (#38). There is nothing here to adjust. The visual
language is replaced wholesale.

---

## 1. The visual language

### 1.1 The idea, stated once

**Paper laid on stone.** Nude `#EFE5D5` is the ground — warm, mineral, dusty,
the colour of the site itself. Ivory `#F3F0E9` is paper: every report, card,
form, sheet and bar is a discrete object placed on that ground and separated
from it by a 1px hairline, the way a sheet of paper is separated from a stone
table. Nude and Ivory differ by 1.10 in contrast, which is a deliberate
near-miss: the two grounds are told apart by *role and hairline*, never by
brightness. Write it on the wall — **Nude is the ground, Ivory is the paper.**

This concept is inherited from `docs/design-package-v1/FINAL-UI.md` §1 and I am
keeping it: it is the strongest idea in that document and the brandbook change
does not touch it. What the brandbook does change is the dark, the display face
and the arrival of a fifth colour with no assigned job. Sections 1.2–1.4 and 3
below are my revisions.

### 1.2 The three marks, and exactly one job each

The mark decomposes into three elements. Each gets one job in the interface and
is forbidden everywhere else. This is the whole extension system; there is no
fourth motif and no pattern library.

**The woven medallion → the seal of verification.**
The interlaced open line-work at the flower's centre is the only element in the
identity that reads as *a record made and closed*. It becomes the site's
verification seal, and it appears in exactly four places:

1. On the **report sheet masthead**, 44px, top inline-end — drawn as Olive
   1.5px open line-work on a Sky blue `#A4D6E8` tint disc. (Olive line on Sky
   blue is 3.18 — non-text graphic, clears the 3:1 floor. Sky blue as a *tint
   fill on light* is the one thing the brief permits it to do on Nude/Ivory,
   and this is where I spend it.)
2. As the **section divider** on marketing pages — 28px wide, Olive 1px
   line-work, centred on a full-width Olive hairline, **at most three per
   page**. A fourth occurrence is a lint error.
3. As the **favicon and app icon** — the medallion alone, cropped square, Sky
   blue line-work on Dark Olive at 16/32/180/512. The `logo-v6/README.md`
   correctly flags that no favicon crop exists in the brandbook; this is the
   crop, and it is the one asset I am asking Mariam for.
4. As the **loading indicator**, drawn not spun — see §1.5.

**The five-petal forget-me-not → the bullet and the point marker.**
One petal, single glyph, Olive fill, 8px on light grounds, used as: the list
bullet in every feature list and in the report's "work performed" list; and the
plot marker on the GPS diagram, where it sits at 12px over a Sky blue tint
field. Nothing else. **No petal pattern, no petal rain, no watermark petal, no
five-petal cluster used as ornament, no rotation, no bloom.** A petal used as
decoration cheapens the same petal used as a data point four sections later,
and the plot marker is a data point.

**The open hands → a layout rule, never a drawing.**
The hands are never redrawn, never extracted, never used as an icon, never
animated. Their gesture becomes the **cradle rule**, which is the most
consequential thing in this document:

> **No photograph of a plot, a monument or a report ever bleeds to the edge of
> the viewport.** Every such image sits inside a frame with visible Nude ground
> on all four sides — minimum 20px at 360, 48px at 1440 — and inside a
> container that is itself inset from the page margin.

Full-bleed photography of a grave is the register of advertising and of news;
an inset frame with ground around it is the register of something being held
and shown to you. This is contestable — full-bleed is the modern default and
the reference sites use it — and I am overruling it deliberately: airbnb.com
full-bleeds a room because it is selling the room. We are not selling the grave.
The frame is what stops the page reading as a listing.

### 1.3 The rule field

The only permitted background texture in the entire system is **Olive 1px
hairlines at 100% opacity**. They rule the page the way a plot boundary rules a
cemetery: horizontal, thin, absolute. Olive at an opacity over Nude is a 1.05
step — invisible — so opacity variants of the rule are banned outright.

Permitted rule positions: between content groups inside a section; under the
report masthead; between the metadata rail rows; under the header bar; between
the closing CTA band and the footer. That is the list.

**Backgrounds are flat colour. Full stop.** No gradient anywhere except a single
24px Nude→transparent scrim above the mobile action bar. No mesh, no noise, no
texture image, no paper grain, no `vanta.clouds`, no `three.js`. Deleting the
Vanta + three.js pair also removes two unpinned CDN dependencies (FINDINGS #32)
and roughly a megabyte from a 4.8 MB page (#31) — the art direction and the
performance budget want the same thing here, which is how you know it is right.

### 1.4 Empty states, error states, zero states

These are where a brand like this usually collapses into a stock illustration.
They do not get one.

| State | Composition |
|---|---|
| No reports yet | Ivory sheet, 1px border, the medallion at 44px in Olive line-work at the top, `h4`, one sentence of body, one Deep Olive text link. No image, no illustration. |
| Report preparing | The finished sheet with blocks 1–3 present and the photograph slot as an Ivory rectangle at the exact final ratio, 1px Olive border, one line of `caption` inside. The report never appears as a spinner. |
| 404 / 500 | Nude ground, `h1`, one sentence, three Deep Olive links to real destinations. Text is Dark Olive at 12.93 — this alone fixes FINDINGS #38, where the current message runs at 1.92. **Never a "404" numeral as a graphic**, which is what ships today on four live routes. |
| Photograph failed to load | Ivory rectangle, exact ratio, 1px Olive border, `caption` sentence. **Never a black box** — a black rectangle where a photograph of someone's mother's grave should be is the worst frame this system can produce. |
| Form submitted | Inline Ivory panel on the Nude ground with a 2px Deep Olive inline-start rule, `h4` plus one sentence naming the promise ("We call or write within one business day"). Not a toast, not a modal, not a checkmark animation. |

### 1.5 Loading

**The mark never spins.** A rotating logo is the one motion that turns a memorial
brand into a startup. Loading is the medallion **drawn**: an SVG
`stroke-dashoffset` sweep of the interlace path, 1.5px Deep Olive on light /
Sky blue on dark, 900ms, `cubic-bezier(.4,0,.2,1)`, playing once and then
holding at full stroke with a 1200ms opacity pulse 1 → 0.55 → 1 while the wait
continues. Under `prefers-reduced-motion: reduce` the path renders complete
immediately and only the opacity pulse remains, at 0.85 → 1.

It reads as a seal being made rather than a wheel being turned, and it is
recognisably ours at 24px, which a generic arc is not.

---

## 2. Typographic scale

Display **Ghea Mariam** (one weight, 400). Text **Montserrat** 400/500/600/700,
with Armenian in **Montserrat Arm** named explicitly in the stack — it is a
separate family, not a subset. Both faces cover Latin, Cyrillic and Armenian
(brandbook page 4 shows Aa / Аа / Աա for both), which retires the whole
"Armenian headings fall back to the text face" problem in the previous spec.
Self-host both as subset woff2; ≤180 KB per locale.

```css
--mc-font-display: "MC Dram", "Ghea Mariam", "Noto Serif Armenian", Georgia, serif;
--mc-font-text:    "MC Dram", "Montserrat", "Montserrat Arm", "Noto Sans Armenian", system-ui, sans-serif;
--mc-font-currency:"MC Dram", "Noto Sans Armenian", "Montserrat Arm", system-ui, sans-serif;
```

`MC Dram` is a single-codepoint `@font-face` (`unicode-range: U+058F`) loaded
first in all three stacks. Neither Ghea Mariam nor Montserrat is verified to
carry ֏, and this makes that question stop mattering: the dram sign resolves
from one known-good face and a total failure degrades one glyph, not a price.
**Every price prints the symbol and the letters — `180,000 ֏ AMD`** — which is
both a bank requirement and the reason a missing glyph is survivable. This also
fixes FINDINGS #21, where `֏` renders from an unstyled system fallback,
visibly smaller and lighter than the digits next to it.

### 2.1 Two hard rules on Ghea Mariam

1. **Optical floor 24px, every medium including PDF.** Below that its hairline
   joins break up. Any slot that would fall below 24px is handed to Montserrat
   600 — which is why mobile `h3` is a sans.
2. **Ghea Mariam is rationed to five slots**: `display`, `h1`, `h2`, `h3`
   (desktop only), `price`. Never in a button, never in a badge, never in the
   nav, never in a table, never uppercase, never letterspaced positive, never
   synthetically bolded or italicised.

Hierarchy is not made by weight in the display face — it is made by size steps
never smaller than 1.30 between adjacent Ghea levels, and by measure: `display`
is set to a 16–22 character line, `h2` to 28–34, `h3` to a full 44. Line length
reads as rank before size does.

### 2.2 Scale at ≥1200 (desktop)

| Token | Face / weight | Size / line-height | Tracking | Use |
|---|---|---|---|---|
| `display` | Ghea Mariam 400 | 72 / 78 (1.083) | −0.015em | Hero H1, once per page |
| `h1` | Ghea Mariam 400 | 56 / 62 (1.107) | −0.012em | Page titles |
| `h2` | Ghea Mariam 400 | 40 / 48 (1.20) | −0.008em | Section heads |
| `h3` | Ghea Mariam 400 | 28 / 36 (1.286) | −0.004em | Sub-sections, card titles |
| `h4` | Montserrat 600 | 20 / 28 (1.40) | 0 | In-card, in-report headings |
| `price-xl` | Ghea Mariam 400 | 60 / 64 | −0.01em, tabular | Report/calculator total |
| `price` | Ghea Mariam 400 | 44 / 48 | −0.01em, tabular | Tariff card amount |
| `body-lg` | Montserrat 400 | 19 / 30 (1.58) | 0 | Standfirst, report body, legal |
| `body` | Montserrat 400 | 17 / 28 (1.65) | 0 | Default paragraph |
| `small` | Montserrat 400 | 15 / 24 (1.60) | 0 | Card body, dense lists |
| `caption` | Montserrat 500 | 14 / 20 | +0.01em | Image captions, helper text |
| `rail` | Montserrat 500 | 14 / 20 | +0.06em, tabular | Verification rail, report metadata |
| `eyebrow` | Montserrat 600 UC | 14 / 18 | +0.14em | Section eyebrows, badges, chips |
| `button` | Montserrat 600 | 16 / 20 | +0.02em | All button labels |
| `nav` | Montserrat 500 | 16 / 24 | +0.01em | Header nav, footer links |
| `legal` | Montserrat 400 | 15 / 24 | 0 | Footer legal, disclaimers |

### 2.3 Scale at 360 (mobile)

| Token | Face / weight | Size / line-height | Tracking |
|---|---|---|---|
| `display` | Ghea Mariam 400 | 34 / 40 (1.176) | −0.010em |
| `h1` | Ghea Mariam 400 | 30 / 38 (1.267) | −0.008em |
| `h2` | Ghea Mariam 400 | 26 / 34 (1.308) | −0.004em |
| `h3` | **Montserrat 600** | 20 / 28 | 0 — below the 24px Ghea floor |
| `h4` | Montserrat 600 | 18 / 26 | 0 |
| `price-xl` | Ghea Mariam 400 | 40 / 44 | −0.01em, tabular |
| `price` | Ghea Mariam 400 | 32 / 36 | −0.01em, tabular |
| `body-lg` | Montserrat 400 | 17 / 28 | 0 |
| `body` | Montserrat 400 | 16 / 26 (1.625) | 0 |
| `small` | Montserrat 400 | 15 / 23 | 0 |
| `caption` | Montserrat 500 | 14 / 20 | +0.01em |
| `rail` | Montserrat 500 | 14 / 20 | +0.06em, tabular |
| `eyebrow` | Montserrat 600 UC | 14 / 18 | +0.14em |
| `button` | Montserrat 600 | 16 / 20 | +0.02em |
| `nav` | Montserrat 500 | 16 / 24 | +0.01em |
| `legal` | Montserrat 400 | 15 / 24 | 0 |

Intermediate widths interpolate with `clamp()` between the two tables; there are
no third and fourth typographic scales. `body` is
`clamp(1rem, 0.94rem + 0.28vw, 1.0625rem)` — 16 → 17.

### 2.4 Floors and prohibitions

- **Body is never below 16px on mobile** and never below 15px anywhere. The
  current build runs 225 elements at 15px, 132 at 14px and one at 12px
  (FINDINGS #26) with pinch-zoom disabled (#7). Both go.
- **Uppercase chips, badges and eyebrows are never below 14px.** This is why
  `eyebrow` is 14/18 and not the 13px the previous spec used — the brief sets
  the floor at 14 and the brief wins.
- **Every input is 16px.** Below 16, iOS zooms on focus.
- **No informational text below 14px, in any medium, ever.** The verification
  rail carries the actual proof — date, cemetery, plot, crew, coordinates — for
  a 40–60 audience reading on a phone at night. It is 14px minimum.
- **Opacity is banned for text.** Dark Olive at 70% over Nude resolves to about
  6.3 and passes, but it stops being auditable the moment a background changes.
  Secondary text is a token, `--mc-text-secondary: #5A5A50` (6.02 on Nude, 6.60
  on Ivory), restricted to ≥15px.
- Tabular lining figures everywhere a number can change: prices, coordinates,
  dates, times, visit counts. Proportional only inside running prose.
- Measure: body 62–70 characters at 1440, 34–42 at 360; display 16–22 per line;
  **report body 58–64** — a report is read, not scanned.
- `pinch-to-zoom stays enabled.` No `maximum-scale`, no `user-scalable=no`.

### 2.5 Armenian and Russian run long — how the scale absorbs it

Budget: **hy +30%, ru +15%** over English. Four mechanisms, applied in this
order:

1. **Copy budgets before type tricks.** Every slot has a grapheme cap enforced
   at build. The load-bearing ones: `hero.display` EN ≤48 / hy ≤62 / ru ≤55;
   `h2` EN ≤56 / hy ≤72 / ru ≤64; `button.label` EN ≤22 / hy ≤28 / ru ≤25;
   `badge.label` EN ≤18 / hy ≤23 / ru ≤20; `tariff.name` EN ≤12 / hy ≤16 /
   ru ≤14; `nav.item` EN ≤16 / hy ≤21 / ru ≤18. `Օպտիմալ խնամք` is 14, so the
   tariff name budget is set by Armenian, not English.
2. **A per-locale step down on display type only.**
   `:lang(hy)` multiplies `display`/`h1`/`h2` by **0.88**; `:lang(ru)` by
   **0.94**. Body, caption, rail and eyebrow are **never** scaled down — the
   floors in 2.4 are absolute and a long language does not get smaller reading
   text.
3. **Per-locale tracking and leading.** Armenian gets **tracking 0 minimum,
   never negative** — Ghea Mariam's Armenian has deep descenders (ղ, ք, ը) and
   negative tracking collides them — and **+0.04 on every line-height ratio**.
   Russian display gets a floor of −0.008em. Armenian eyebrows are
   `text-transform: none` with tracking +0.08em: Armenian caps read as
   shouting and the script has no true small-caps tradition. Russian eyebrows
   stay uppercase at +0.10em (Cyrillic caps need less than Latin).
4. **Components tolerate two lines, always.** Buttons are `min-height: 48px`
   with a centred label allowed to wrap to two lines; badges wrap; nav items
   wrap. **Nothing ellipsises.** `Our recommendation` is 18 characters in
   English and wraps in Armenian — that is a designed state, not an overflow.

**Test gate:** every component ships a 360 screenshot in all three locales with
the longest permitted string in every slot. A component that has only been seen
in English is not finished.

---

## 3. Colour application

### 3.1 Tokens

| Token | Value | Role |
|---|---|---|
| `--mc-dark-olive` | `#212212` | The dark ground. Bands, footer. |
| `--mc-olive` | `#7C8654` | Rules, petals, medallion line-work, decorative fills. **Never text, never behind text.** |
| `--mc-nude` | `#EFE5D5` | Page ground. Primary button fill on dark. Text on dark. |
| `--mc-ivory` | `#F3F0E9` | Paper objects. Labels on dark fills. |
| `--mc-sky` | `#A4D6E8` | Dark-ground accent. Tint fill on light. |
| `--mc-deep-olive` | `#575E3B` | Links, accents, secondary button, focus on light. Interface only. |
| `--mc-error` | `#8C3A2E` | Validation only, light grounds only. |
| `--mc-text-secondary` | `#5A5A50` | Derived. ≥15px only. |

`--mc-sky` is **one token, referenced nowhere directly** — every use goes
through `--mc-accent-on-dark`, `--mc-surface-tint`, `--mc-focus-on-dark`. If
Mariam rules for `#D4ECF9` it is one line. (`logo-v6/README.md` documents the
conflict; the artwork says `#A4D6E8` and the artwork is what will sit next to
the interface.)

### 3.2 The four structural rules, and what I do with the fifth colour

1. **Olive never carries text and never receives text.** Rules, petals,
   medallion line-work, the plot-diagram frame, focus on non-text UI. It never
   fills a button — which is exactly what today's build does, at 3.42, on the
   primary action of every page (`states-forms.png`, `fold-login.png`).
2. **Sky blue is a dark-ground colour.** On Dark Olive it measures 10.26 and
   carries type beautifully. On Nude it is 1.26 — invisible — where it may only
   be a **tint fill**, and I permit exactly two: the medallion seal disc on the
   report masthead, and the GPS plot-diagram field. Nothing else on light.
3. **The consultation form never sits inside a dark band.** The error colour is
   2.12 on Dark Olive; a form there cannot show a validation error at all. The
   closing CTA band carries a heading, a support line and buttons; the form
   itself is an Ivory sheet on the Nude ground immediately above or below it.
   Structural, not aesthetic.
4. **Nude is the ground, Ivory is the paper.** An Ivory object on Nude always
   carries a 1px `rgba(33,34,18,0.14)` border — without it the 1.10 step reads
   as a printing error. Ivory never sits directly on Ivory (a card landing on
   an Ivory surface loses its fill and is defined by its border alone). Ivory is
   never a full-bleed band; header and mobile action bar are bars, not bands,
   and are the two declared exceptions.

**Sky blue's assignment — my call.** The brandbook delivers it and does not say
what it is for beyond the tagline. I give it one meaning: **Sky blue means
verified.** Every proof signal that appears on a dark ground is Sky blue — the
`GPS confirmed` chip, the eyebrow on the Family Circle and CTA bands, the
timestamp rail on dark, the focus ring on dark. On light grounds verification is
carried by the Olive-on-Sky-tint seal and by typography, not by the blue itself.
One meaning, two grounds, no drift. The alternative — treating it as a generic
"accent" — would put it on light grounds within a week, where it is invisible.

**What is never used again:** `#33373C` Anthracite, `#5E6A3A`, `#6B7075`,
`#FAFAF7`, the 27.08 sampled set, the site's current cool grey footer
(`spot-1440.png`), any green other than the three olives, any red other than
`#8C3A2E`, and pure `#000` or `#FFF` anywhere including photographs and the PDF.

### 3.3 Buttons and focus — the contrast fixes stated as tokens

| Context | Primary | Secondary | Tertiary |
|---|---|---|---|
| Light ground (Nude / Ivory) | Dark Olive fill, Ivory label — **14.17** | 1px Deep Olive border, Deep Olive label — **5.49 / 6.01** | Deep Olive text, 1px underline drawn from the inline start |
| Dark ground (Dark Olive) | Nude fill, Dark Olive label — **12.93** | 1px `rgba(243,240,233,0.40)`, Ivory label | Sky blue text, underlined — **10.26** |

Focus ring, always visible, never removed: on light, **2px Deep Olive at 2px
offset plus a 1px Ivory inner ring** so it reads on both light grounds; on dark,
**2px Sky blue at 2px offset**. Today's forms have no focus state at all — the
empty and focused captures are byte-identical (FINDINGS #24).

### 3.4 The rhythm of the home page, band by band

Two dark bands per marketing page. Not three, not one.

| # | Band | Ground | Objects | Accent | Approx. height, 1440 |
|---|---|---|---|---|---|
| 0 | Header bar | Ivory, 1px bottom hairline `rgba(33,34,18,0.14)` | — | Deep Olive active underline | 72 |
| 1 | **Hero** | **Nude** | Ivory `ReportPreview` object, inset per the cradle rule | Deep Olive CTA fill is Dark Olive; eyebrow Deep Olive | 640–720 |
| 2 | How it works — 4 steps | Nude | no cards; four columns divided by Olive hairlines | Olive petal bullets | 420 |
| 3 | **The report** | Nude | the full **Ivory report sheet**, 720 wide, the heaviest object on the page | Sky-tint seal, Olive rules | 900–1040 |
| 4 | Tariffs | Nude | four Ivory cards; Inspection separated by a full-width Olive rule and set as a wide single-column card, not a fourth column | Deep Olive `Our recommendation` badge on Optimal | 760 |
| 5 | **Family Circle** | **Dark Olive** | Ivory-bordered role panels, no fills | **Sky blue** eyebrow and role labels; Nude body | 560 |
| 6 | Trust — verification, regularity, transparency | Nude | three Ivory panels | Olive medallion divider above | 480 |
| 7 | **Consultation form** | **Nude** (rule 3) | Ivory form sheet | Deep Olive labels, error `#8C3A2E` | 620 |
| 8 | **Closing CTA → footer, continuous** | **Dark Olive** | none | Sky blue eyebrow; 1px Olive rule between CTA and footer | 340 + 380 |

Dark bands total ≈ 1,280px of roughly 6,000 — **21%**. Cap it at 25%. Dark Olive
`#212212` is materially heavier than the Anthracite it replaces (12.93 vs 9.61
against Nude); at 40% of the page it stops being an anchor and becomes a
funeral, which the brief explicitly forbids. Dark bands therefore also take
**more vertical padding than light ones** (§5) so the weight reads as
deliberate space rather than a slab.

**The hero is Nude, and I will argue for that.** A dark hero spends the page's
scarcest asset on the one screen where the tone rule is strictest, costs 8–16px
of fold to a second header variant, and — for an audience opening the site at
1 a.m. in Glendale — is the exact frame that says "funeral home". Warmth here
comes from the Nude ground and the size of the type, not from darkness.

---

## 4. Photography art direction

### 4.1 Two classes of image, two ratios, no others

| Use | Ratio | Export | Shot by |
|---|---|---|---|
| Report photograph | **4:3** | 1600 × 1200 | crew, phone, portrait-held device turned landscape |
| Marketing / section image | **3:2** | 1800 × 1200 | professional, September shoot |
| Crew or equipment portrait | 1:1 | 1000 × 1000 | professional |
| Report video | 16:9 | 1920 × 1080 | crew |
| OG / link preview | 1.91:1 | 1200 × 630 | **generated, never a photograph** |

4:3 for the plot because a plot needs vertical extent — headstone, base, kerb,
ground — and because it is what a phone gives without cropping. 1:1 is right for
a crew portrait and wrong for a plot. There is no 4:5 comparison crop: a
comparison is two 4:3 frames, stacked at 360 and 2-up at ≥900.

### 4.2 Framing

- Camera at **standing eye height, level**. Never a low heroic angle. Never a
  drone frame directly above a grave — drone is for access routes and cemetery
  context only, and never in the report.
- The plot occupies the **lower two-thirds**; path, wall or sky above. The
  **monument base and the ground line are always in frame** — a monument cropped
  at the base floats, and a floating headstone is a stock photograph.
- **Before and after are the same frame**: marked standing position, fixed
  tripod height, fixed focal length, same time of day where possible. This is
  the evidentiary point of the entire product. A crew that moves two metres
  between frames has destroyed the proof, so the standing position is an
  operational artefact of the September shoot, not a preference.
- **The client's own inscription is legible by default** — it is the proof we
  cleaned *their* plot. **Every neighbouring plot's name and inscription is out
  of frame or out of focus, without exception.** Whether the deceased's name is
  *displayed* in the report is a separate, off-by-default consent setting.
- Crew appear working — hands, brush, water, gloves. Never posed, never smiling
  to camera, never a line-up team photo. **No mourner's face ever appears.**
- No flowers arranged for the camera, no candles, no crosses composed as
  graphic elements, no wilting-flower metaphor, no rain, no sunset, no
  silhouette, no light shaft, no clouds. (The build currently opens on clouds
  and on a stock nurse with a stethoscope — FINDINGS #30.)

### 4.3 Grade

Numbers, not adjectives. Applied identically to report and marketing images so
a crew phone frame and a professional frame sit on the same page without a
visible seam.

- **White balance 5,200–5,600 K.** Warm enough to sit on Nude; not golden.
- **Overcast or open shade.** Hard midday sun turns granite into a monument
  catalogue and blows the inscription.
- **Stone renders at 55–70% luminance.** Under-exposed stone reads as neglect,
  which is the opposite of the message.
- **Black point lifted to 10–14 / 255. Nothing goes to pure black.** A true
  black in an image adjacent to a `#212212` band punches a hole in the page.
- **Highlights held below 245 / 255.** No clipped sky.
- **Saturation −5 to 0. No duotone, no olive wash, no split-tone, no
  black-and-white, no grain, no film emulation, no HDR, no vignette.** The
  grade's job is to be invisible; a graded photograph of a grave is a photograph
  someone has interpreted, and interpretation is the one thing this product must
  not do.
- Contrast: a gentle S, no more than ±8 on the mid-tones.

### 4.4 Presentation, crop and caption — the part that keeps it dignified

- **Radius 0. No border. No shadow. Never a black border.** Ground plus hairline
  does the work everywhere else and does it here.
- **No text is ever set over a photograph. No scrim, no overlay, no gradient, no
  "BEFORE"/"AFTER" burned into the frame.** Every label is typographic and sits
  **outside** the frame: `overline` label above, `rail` timestamp at the inline
  end, `caption` sentence below in `--mc-text-secondary`. This single rule
  eliminates the class of defect the audit found at 3.20 and 2.36 (FINDINGS
  #12) — if there is no text on the image, the ratio cannot fail.
- **Chronological order, always: `On arrival` first, then `After the work`.**
  Leading with the clean stone is the advertising register the brief forbids,
  and a report that opens on the after-shot with no reference frame is a
  marketing image, not a record. **No drag-slider, no wipe, no curtain, no
  arrows between frames** — the audit already flags that the design package
  forbids the before/after slider, and the build ships one anyway.
- **No hover-zoom, no Ken Burns, no parallax, no autoplay** on any image of a
  plot. Tap opens a lightbox at full size; that is the only interaction.
- Captions carry facts, not feelings: `Tokhmakh, section 12 · on arrival ·
  14:05 Yerevan`. Two timezones on report timestamps when the viewer's locale
  differs from Asia/Yerevan — `14:05 Yerevan · 03:05 your time`. That single
  line is the most diaspora-specific thing on the site and costs nothing.

### 4.5 There are no real photographs yet — and placeholders must not look like placeholders

The honest answer and the good-looking answer conflict here, and the resolution
is to stop trying to fake a photograph.

**Rule: the site ships zero images that pretend to be photographs of a plot.**
No stock cemetery imagery, no AI-generated grave, no grey box, no "image coming
soon", no camera glyph, no blurred stand-in. Every one of those either lies or
looks broken, and a stock photograph of someone else's grave on a page selling
care of *your* grave is a specific, avoidable insult.

Three substitutes, in order of preference:

1. **The marketing hero carries no photograph at all.** It carries the
   `ReportPreview` — a real, built, translatable HTML object (§6). It is
   finished, not pending; it demonstrates the product better than any
   photograph could; and it is sharp at every DPR and weighs under 15 KB. This
   is the strongest argument for the hero I have: the thing we are selling is a
   *document*, so show the document.
2. **Where a frame is structurally required** — the report sheet's photograph
   slots, the how-it-works steps — use a **commissioned plate**: a flat
   line-work drawing at the exact final ratio, Olive 1.5px lines on Nude, in
   the same open-line vocabulary as the medallion. A plot with a headstone, a
   kerb and a path; no figures, no faces, no sky. It reads as a deliberate
   illustration, not a missing asset, because it plainly is not trying to be a
   photograph. Caption beneath in `caption`: `Illustration. Photographs from
   the September visits replace this.` One sentence, no apology.
3. **Internal-only stubs** (staging, Storybook, QA) are the honest labelled
   rectangle — Nude, 1px Olive, exact ratio, and four facts in `caption`:
   `PLACEHOLDER · 4:3 · 1600×1200 · "arrival, Tokhmakh s.12" · September shoot`.
   These are gated behind an environment flag and **cannot render in
   production**; a build that emits one fails CI. The previous spec put these on
   the live site; I am overruling that. It is admirably honest and it looks
   unfinished, and "unfinished" is a claim about our reliability that we cannot
   afford to make on a page asking for 180,000 ֏.

File names are stable so the September shoot is a `1.x` asset swap with zero
component changes: `plot-4x3-arrival.{svg|jpg}`, `plot-4x3-after.*`,
`section-3x2-*.*`, `crew-1x1-*.*`, `report-16x9-*.*`.

---

## 5. Grid, spacing and density

### 5.1 Breakpoints and grid

`min-width` queries only. Design frames at **360 / 900 / 1440**; 360 is the QA
gate, not 375.

| Name | Min | Cols | Gutter | Margin | Content max | Notes |
|---|---|---|---|---|---|---|
| `base` | **360** | 4 | 16 | 20 | — | The primary channel |
| `sm` | 600 | 8 | 24 | 32 | 720 | Tariff cards go 2-up |
| `md` | 900 | 8 | 24 | 40 | 840 | Nav expands, drawer retires, `h3` returns to Ghea Mariam |
| `lg` | 1200 | 12 | 24 | 48 | 1128 | Verification rail becomes a right-hand column |
| `xl` | 1440 | 12 | 32 | auto | 1240 | More air, **no new layout** |

**One breakpoint set, shared by CSS and JavaScript.** The current build's menu
script switches on `window.innerWidth <= 1300` while the CSS switches elsewhere,
producing a dead zone between 1024 and 1300 where the mobile menu is live with
no way to open it (FINDINGS #28). Breakpoints are exported from one token file
and read by both.

Text measure is capped independently of the grid: **`--mc-measure: 68ch`** on
body copy, 44ch on `h3`, 22ch on `display`. At 1920 the page does **not** grow
past 1240 — it gains margin. What it must never do is what it does today, which
is leave a 400px card marooned in a white field (`fold-login.png`, 1920 column).

**The signature split at `lg`+:** main column cols 1–8, the verification rail
cols 10–12, **column 9 deliberately empty**. That empty column is the page's
most expensive gesture and the reason it reads as editorial rather than as a
template.

### 5.2 Spacing scale

4px base, thirteen steps, nothing off-scale:
**4 · 8 · 12 · 16 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 128 · 160.**
An optical exception requires a written note in the token file.

### 5.3 Section padding (top / bottom)

| | 360 | 600 | 900 | 1200 | 1440 |
|---|---|---|---|---|---|
| Light band | 72 | 88 | 104 | 120 | **128** |
| **Dark band** | 80 | 96 | 112 | 136 | **144** |
| Between blocks in a section | 24 | 32 | 32 | 40 | 40 |
| Card padding | 20 | 24 | 28 | 32 | 32 |
| Report sheet padding | 20 | 28 | 32 | 40 | 40 |
| Page bottom, where the mobile action bar can appear | 88 | — | — | — | — |

Dark bands get 16px more than light ones at every width. A dark band with light
padding reads as a slab; with generous padding it reads as a held breath.

### 5.4 Where the page is generous, and where it is deliberately tight

**Generous** — hero (128/160 at 1440, `display` on a 22ch measure with a hard
left margin and nothing at all on the right), the section above the report
sheet, the closing CTA. These are the three places a visitor decides whether
this is a serious company.

**Tight, on purpose** — three zones, and they are tight because density is the
signal:

1. **The verification rail.** 8px vertical rhythm, `rail` at 14/20, 1px Olive
   hairline between rows, label and value on one line at ≥900. Flat tabular
   metadata packed close is what a record looks like and what a brochure cannot
   fake.
2. **The tariff feature list.** 24px rows, 8px petal-to-text gap, no dividers.
   Four cards must be scannable side by side in one eye movement.
3. **The report's metadata block and the footer's legal group.** 20/24 rhythm,
   `legal` at 15/24. Legal information that is spaced out looks apologetic.

Everything else sits at 24–40. The contrast between the 160px hero and the 8px
rail is the page's whole rhythm.

### 5.5 Density floors

- **Touch targets 48 × 48 minimum**, including invisible padding, at every
  width. Today: hamburger 28 × 27, language links 33 × 22.5, order button
  205 × 31 (FINDINGS #25). The three language links are the single most
  important control for a diaspora visitor and the hardest to hit on the site.
- The **language switcher is present in every state at every width**, including
  inside the open mobile menu, where it currently vanishes (#27). At 360 it is
  three 48px-tall rows at the top of the drawer, `nav` 16/24, active state a
  2px Deep Olive inline-start rule — **not** three 22px links crammed into a
  header row.
- 24px minimum between adjacent interactive elements.

---

## 6. The report sheet

This is the product. Everything else on the site exists to get someone to look
at it. It should be the object a visitor screenshots and sends to their sister.

### 6.1 As an artefact

An **Ivory sheet on the Nude ground**. Radius 0. 1px `rgba(33,34,18,0.14)`
border. **No shadow** — the ground change and the hairline do the work, and a
drop shadow is the SaaS tell that would undo the entire paper-on-stone
argument in one property. Max-width **720** at `lg`+; full-bleed minus 20 at
360. Padding 40 desktop / 20 mobile. It is the only object on the home page
allowed to exceed 640px of vertical extent.

### 6.2 Block order — binding on the portal, the guest view and the PDF

| # | Block | Detail | Guest |
|---|---|---|---|
| 1 | **Masthead** | Monochrome-dark mark at 20px inline-start; `VISIT REPORT` in `eyebrow`; plot identity and cemetery in `h4`; the **medallion seal at 44px** inline-end, Olive line-work on a Sky-blue tint disc. 1px **Olive** rule beneath, full sheet width. | yes |
| 2 | **Confirmation** | `h3` "The visit took place". **The date is the largest element on the sheet** — `price-xl` in Ghea Mariam, 60/64 desktop, tabular. Arrival and departure times in `rail`, dual-timezone. `Visit completed` badge: 1px Deep Olive outline, Deep Olive label, no fill. | yes |
| 3 | **GPS verification** | Its own block, never a chip. Sky-blue tint field, 1px Olive frame, radius 0, the plot marked with a 12px Olive petal, coordinates in `rail` tabular beneath. | yes |
| 4 | **Work performed** | Ticked list, Olive petal bullets, max 8 items, first 4 plus "Show all" at 360. | yes |
| 5 | **Photographs** | Group `ON ARRIVAL`, then group `AFTER THE WORK`. `overline` label above each group, `rail` timestamp at the inline end, 1px hairline between label and frame. 4:3, radius 0, no border, no text on the image. | yes |
| 6 | **Video** | One 20–40s clip, poster frame, muted, inline, **never autoplay**. | yes |
| 7 | **The crew's note** | 120–320 characters, `body-lg` 19/30, the one first-person voice in the entire product. Set on a 58–64 character measure. Not italic, not a quote mark, not a signature graphic. | yes |
| 8 | **Recommended work, with prices** | Owner and Family manager only. Changed ground (Nude inset panel), full-width Olive rule above. **Removed server-side for everyone else — not hidden with CSS.** | **no** |
| 9 | **Documents** | The report PDF. | yes |
| 10 | **Actions** | Share · Order additional work · Request a repeat visit. | text link only |
| 11 | **Next visit** | Date, `rail`. | **no** |

**The report opens on a calm confirmation, not on an image.** Someone opening
this at 1 a.m. six thousand kilometres away needs to know it happened before
they need to see it.

### 6.3 States

`complete` · `preparing` ("The visit is done. The report is being prepared.")
· `media-partial` ("Some photographs are still uploading. The rest of the report
is complete.") · `failed` (a calm sentence and a phone number). **No red
anywhere on a report screen, in any state.** A red mark beside a photograph of a
grave is the worst thing this system could produce. "Could not reach the plot"
is a *report of a visit that happened*, with GPS proof that the crew was there —
neutral outline badge, glyph and word, never an error colour.

### 6.4 PDF

A4, identical block order, identical type scale down-stepped one size, Ivory
ground so it prints as the same object. **Never any price in any variant**, so
one file serves owner, member and guest. The tagline is set from the print
lock-up. `֏` follows §2. Past reports stay readable forever, including after
cancellation — read-only, no new visits, no upsell on those screens.

### 6.5 `ReportPreview` — the hero object

A distinct component, not a cropped sheet: masthead strip, the verification rail
as a horizontal strip, the `GPS confirmed` chip, one 4:3 slot and two
thumbnails. Built in HTML — sharp, translatable, fast, and **never a photograph
of a phone holding the report**. This is what the hero shows instead of a
photograph (§4.5).

### 6.6 Link preview — a hard rule

The OG image is **generated, never a photograph**: Dark Olive ground (a Nude
card renders near-blank in a dark WhatsApp thread), monochrome-light mark at
96px, `Visit report` in `h3` Ivory, the date in `rail` Sky blue. `og:title =
"Visit report — {date}"`. **No cemetery, no plot label, no name, no image of the
plot.** The page `<title>` is `Visit report — {date}` and nothing more: a plot
identity in a browser tab is visible over a shoulder and in every screen-share.
A shared report link is `noindex, nofollow`, token ≥128 bits, revocable from the
sheet that created it.

---

## 7. Iconography and illustration

### 7.1 Icon style

- **24px grid, 1.5px stroke, round caps, round joins, no fill, no corner
  radius below 2px.** Drawn on the same optical skeleton as the medallion's
  interlace, which is what makes them look like they came with the logo instead
  of from a package.
- Colour: Dark Olive on light, Nude on dark. **Never Olive** (3.12 on Nude —
  it clears the 3:1 non-text floor but sits at the very bottom of it, and an
  icon carrying meaning deserves better than the minimum). Sky blue for
  verification icons **on dark only**.
- A 20px variant exists at 1.25px stroke for inline use; nothing smaller.
- One set, hand-drawn to the brief, roughly 24 glyphs. No Font Awesome, no
  Material, no Feather-as-shipped.
- **Icons never carry meaning alone.** Every icon has a text label or an
  accessible name. Today 198 images have no alt text and 126 links have no
  discernible name (FINDINGS #11).

### 7.2 Illustration

One style only: **flat open line-work, Olive 1.5px on Nude, no fill, no shading,
no perspective, no colour beyond Olive and one Sky-blue tint field.** Subjects
are limited to: a plot, a path, a kerb, a headstone silhouette without
inscription, tools, a map field. Used only where §4.5 requires a plate.

### 7.3 Never, under any circumstances

Crosses · doves · angel wings · praying hands · candles · flames · urns ·
weeping willows · sunsets · light shafts through clouds · gothic or blackletter
lettering · RIP · script fonts · rotating or blooming marks · falling petals ·
a petal or medallion used as a repeating background pattern · isometric SaaS
illustration · 3D renders · glassmorphism (the current hero card) · drop shadows
on cards · gradient-filled icons · duotone · stock photography of any kind ·
illustrated people, faces, or families · emoji anywhere in the interface ·
five-star graphics · badge or ribbon shapes · counters and count-ups · progress
"trust" meters · animated numbers · a spinner made from the logo.

The current build contains six items from that list. That is the measure of the
distance.

---

## 8. Motion, briefly — because motion is part of the first two seconds

Total budget on a marketing page: **six behaviours.** Motion confirms, it never
entertains.

| Where | What | Duration / curve |
|---|---|---|
| Section entrance | opacity 0→1, translateY 8→0, once, stagger 60ms, max 3 items per section | 320ms `cubic-bezier(.2,.7,.2,1)` |
| Links and buttons | underline draws from the inline start | 160ms `ease-out` |
| Accordion | height + opacity | 240ms `cubic-bezier(.2,.7,.2,1)` |
| Overlays | scrim fade 160ms; sheet translateY 240ms, same curve | |
| Report images | fade in on decode, no skeleton shimmer | 200ms linear |
| Loading | the medallion draw (§1.5) | 900ms once, then a 1200ms opacity pulse |

**Forbidden:** parallax, scroll-jacking, pinned sequences, auto-advancing
carousels, count-up numerals, typewriter text, hover-lift on cards, Ken Burns or
hover-zoom on a photograph of a plot, before/after wipes, any animation
whatsoever on report photographs, on a status screen, or on a guest report view.

`prefers-reduced-motion: reduce` removes every transform and every entrance, and
reduces everything to opacity at ≤100ms. It is tested, not assumed — a
meaningful share of a 40–60 audience has it switched on.

---

## 9. What makes this specific, and not a nice minimal template

Six things, and I would defend the page on these alone:

1. **The verification rail.** Flat tabular metadata — date, cemetery, sector,
   plot, crew, coordinates, arrival, departure, time on site — set at 14/20
   with +0.06em tracking, occupying its own grid column at ≥1200. A wellness
   template does not have this and cannot fake it. It is the visible form of
   "we sell proof, not cleaning".
2. **The dual-timezone timestamp.** `14:05 Yerevan · 03:05 your time`. One line,
   written for someone who is asleep when the work happens. Nothing else on the
   site says "we know where you are" so quietly.
3. **The cradle rule.** No image of a grave ever touches the edge of the screen.
   Every reference site full-bleeds its photography; we hold ours in a frame.
   That is the hands, translated into layout, and it is the difference between
   showing someone their mother's grave and advertising it.
4. **No text ever set on a photograph.** Every label is typographic and outside
   the frame. It is a contrast fix, a dignity decision and a translation
   convenience at once — and it is why the audit's #12 cannot recur.
5. **Chronological, identical-frame before/after with no slider.** The framing
   discipline *is* the product; a drag-slider turns evidence into a toy.
6. **The seal, drawn not spun.** A memorial brand whose logo rotates in a
   loading state has told you what it thinks of itself.

## 10. What I need from others

- **Mariam:** rule on Sky blue (`#A4D6E8` vs `#D4ECF9`) and supply the medallion
  favicon crop at 16/32/180/512. Neither blocks build — one token, one asset.
- **Ghea Mariam licence and webfont files**, with the Armenian and Cyrillic
  subsets, plus confirmation of tabular figures. If tabular figures are absent,
  `price` falls to Montserrat 600 — one token, no component changes.
- **The September shoot brief as an operational document**: shot list per plot,
  marked standing position, tripod height, focal length, file-naming convention
  matching §4.5. Without the standing position the before/after pairs are
  worthless as evidence and the art direction above cannot be executed.
