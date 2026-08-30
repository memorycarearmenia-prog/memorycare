# 02 — Visual Design Lead: visual language for MemoryCare

Site + client portal. English. Version 1, 30.08.2026.

Type note that must appear on every mock and every exported page:
**Cabin is used as a free substitute for Gill Sans (commercial Monotype). It is not the brand text face.**

---

## A. UI

### A.0 The visual concept

MemoryCare is a company that keeps records of care, so the page is built like a
record, not like a brochure. The whole system rests on one structural idea —
**paper laid on stone** — and one structural device — **the verification rail**.
Nude is the ground: warm, mineral, slightly dusty, the colour of the site itself.
Ivory is paper: every document, report, form and tariff card is a sheet placed on
that ground, separated only by a hairline, the way a sheet of paper is separated
from a stone table. Every element that carries proof — a report, a visit, a
guarantee, a price — carries a narrow right-hand rail of flat factual metadata set
in tabular small caps: date, plot, cemetery, coordinates, time on site. That rail
is the thing a generic wellness template does not have and cannot fake; it is the
visible form of "we sell proof, not cleaning". The brand's own vocabulary supplies
the marks, and each one has exactly one job: the **five-petal forget-me-not** is
the list bullet and the point marker on the plot diagram, never wallpaper; the
**woven medallion** is the section divider, drawn once as a single-stroke interlaced
band in Olive and used four times on the home page, never more; **Olive hairlines**
rule the page the way a plot boundary rules a cemetery — horizontal, thin,
absolute. Layout is asymmetric and flush left throughout, with Gloock set very
large against generous left margin and short measure. There is no centred hero, no
rounded card with an accent rail, no gradient, no shadow anywhere in the system.
The page is quiet, ruled, and factual, and its warmth comes entirely from the Nude
ground and the size of the type — which is exactly the register in which a person
at 1 a.m. in Glendale decides to trust a company with their mother's grave.

---

### A.1 Type system

**Display — Gloock Regular** (Google Fonts, 400 only).
**Text — Cabin** 400 / 500 / 600 / 700 (Google Fonts) — *substitute for Gill Sans.*

#### Solving the single-weight constraint

Gloock cannot make hierarchy by weight, so hierarchy is made by five other means,
and Gloock's job is deliberately narrowed:

1. **Gloock is rationed.** It appears in exactly five slots: H1, H2, H3 (desktop
   only), price numerals, and the single pull-quote per page. Everything else —
   H4 and below, all UI, all labels, all data — is Cabin, which has four weights
   and carries the fine-grained hierarchy.
2. **Size steps are large.** Between adjacent Gloock levels the ratio is never
   below 1.35, so two Gloock levels can never be confused at a glance.
3. **Measure differentiates.** H1 is set to a 16–22 character line; H2 to 28–34;
   H3 to a full 44. Line length reads as rank before size does.
4. **Colour differentiates.** Gloock is Anthracite on light and Nude on dark.
   A single **Deep Olive** word inside an H1 or H2 is the only permitted emphasis
   inside display type — no italic (Gloock has none), no all-caps, no bold fake.
5. **Optical floor.** Gloock is high-contrast and its hairlines break up under
   24px. **Gloock is never set below 24px, ever, in any medium, including PDF
   reports.** Below 24px the role is handed to Cabin 600. This is why mobile H3 is
   Cabin, not Gloock (see scale).

Never synthesise a bold or an italic of Gloock. Never letterspace Gloock positive.
Never set Gloock in all caps.

#### Scale — 1440 (desktop)

| Token | Face / weight | Size / line-height | Tracking | Use |
|---|---|---|---|---|
| `display` | Gloock 400 | 76 / 82 (1.08) | −0.02em | Hero H1 only |
| `h1` | Gloock 400 | 60 / 66 (1.10) | −0.015em | Page titles |
| `h2` | Gloock 400 | 44 / 50 (1.14) | −0.01em | Section heads |
| `h3` | Gloock 400 | 30 / 38 (1.27) | −0.005em | Sub-sections, card titles |
| `h4` | Cabin 600 | 20 / 28 (1.40) | 0 | In-card and in-report headings |
| `price-xl` | Gloock 400 | 56 / 58 | −0.01em, tabular | Calculator total |
| `price` | Gloock 400 | 40 / 44 | −0.01em, tabular | Tariff card price |
| `quote` | Gloock 400 | 34 / 46 (1.35) | −0.005em | One pull-quote per page max |
| `body-l` | Cabin 400 | 19 / 30 (1.58) | 0 | Hero standfirst, section standfirst |
| `body` | Cabin 400 | 17 / 27 (1.59) | 0 | Default paragraph |
| `body-s` | Cabin 400 | 15 / 23 (1.53) | 0 | Card body, legal pages |
| `caption` | Cabin 500 | 13 / 18 | +0.01em | Image captions, helper text |
| `eyebrow` | Cabin 600 UC | 12 / 16 | +0.14em | Section eyebrows, badges, card labels |
| `rail` | Cabin 500 UC | 12 / 20 | +0.08em, tabular | Verification rail, report metadata |
| `button` | Cabin 600 | 16 / 16 | +0.02em | All button labels |
| `nav` | Cabin 500 | 15 / 20 | +0.01em | Header nav, footer links |
| `legal` | Cabin 400 | 14 / 24 | 0 | Footer legal, disclaimers |

#### Scale — 375 (mobile, primary channel)

| Token | Face / weight | Size / line-height | Tracking |
|---|---|---|---|
| `display` | Gloock 400 | 40 / 44 (1.10) | −0.015em |
| `h1` | Gloock 400 | 34 / 39 (1.15) | −0.01em |
| `h2` | Gloock 400 | 28 / 34 (1.21) | −0.005em |
| `h3` | **Cabin 600** | 21 / 28 | 0 | *(below the 24px Gloock floor)* |
| `h4` | Cabin 600 | 18 / 26 | 0 |
| `price-xl` | Gloock 400 | 40 / 44 | −0.01em, tabular |
| `price` | Gloock 400 | 32 / 36 | −0.01em, tabular |
| `quote` | Gloock 400 | 26 / 36 | 0 |
| `body-l` | Cabin 400 | 17 / 27 | 0 |
| `body` | Cabin 400 | 16 / 26 | 0 |
| `body-s` | Cabin 400 | 15 / 23 | 0 |
| `caption` | Cabin 500 | 13 / 19 | +0.01em |
| `eyebrow` | Cabin 600 UC | 11 / 15 | +0.14em |
| `rail` | Cabin 500 UC | 11 / 18 | +0.08em, tabular |
| `button` | Cabin 600 | 16 / 16 | +0.02em |
| `nav` | Cabin 500 | 16 / 24 | +0.01em |

**Body text never goes below 15px anywhere on the site or in the portal.** The
audience is 40–60 and reading on a phone at night. 13px is permitted only for
captions and helper text, never for a sentence that carries meaning.

**Measure.** Body 62–70 characters desktop, 34–42 mobile. Display 16–22 characters
per line. Report body 58–64 characters — a report is read, not scanned.

**Numerals.** Tabular lining figures everywhere a number can change: prices, the
calculator, coordinates, dates, visit counts. Proportional only inside running
prose. Prices always carry both forms — `160,000 ֏ AMD` — per the bank requirement;
`AMD` in `caption` after the symbol, never as a superscript.

**Armenian and Russian.** Gloock has no Armenian coverage and Cabin's Cyrillic is
adequate but its Armenian is absent. The English site is designed so that the
display face is a **single swappable token**; nothing in the layout depends on
Gloock's specific proportions except the character budgets in section C, which
carry 20% headroom for Armenian. Localisation must not begin until a display face
with Armenian coverage is confirmed. Flagged as blocking.

---

### A.2 Colour application

#### The Nude / Ivory decision — write this down

The two lights differ by 1.1 in contrast, so they can only be told apart by
**consistent role**, never by eye. The rule, once, for the whole system:

> **Nude `#EFE5D5` is the ground. Ivory `#F3F0E9` is the paper.**

- **Nude** — page background, light section bands, input fills when the input sits
  on an Ivory band, table zebra on Ivory, the footer's Nude button.
- **Ivory** — every discrete object placed on the ground: cards, tariff cards, the
  report sheet, the calculator panel, modals, the header bar, input fills when the
  input sits on a Nude band, and **all light text on Anthracite**.
- **Ivory never sits on Ivory.** If a card would land on an Ivory band, the card
  loses its fill and is defined by hairlines alone.
- **An Ivory object on a Nude ground always carries a 1px hairline.** Without it the
  1.1 difference reads as a printing error.

Full-bleed Ivory bands are used for *document* moments — the sample report, the
calculator, the legal pages — so the whole band reads as a sheet.

#### Anthracite

Dark ground and body text. Used as a band exactly **three times** on the home page —
hero, Family Circle, and the closing CTA which runs into the footer. Any more and
the page tips into the funeral register we are forbidden. Anthracite is a warm
graphite, not black; it must never be pushed to `#000` and never used as a border
around a photograph.

Opacity ladder on light grounds (composited, so no new tokens):
Anthracite 100% body · 70% secondary text (7.1:1, passes) · 45% decorative only,
never text · 12% hairlines · 8% table rules.
On dark grounds: Ivory 100% · Ivory 80% secondary (7.9:1) · Ivory 40% borders ·
Ivory 16% hairlines. **60% is the floor for any Ivory text on Anthracite.**

#### Olive `#7C8654` — decoration only, and only these five jobs

1. Structural hairline rules between content groups (1px, 100% opacity).
2. The woven-medallion divider band between major sections.
3. The five-petal bullet glyph in feature lists and the point marker on the plot diagram.
4. The tagline in the footer, small caps, no full stop.
5. Focus rings and the outline of the plot-diagram frame (non-text UI: Olive on Nude
   is 3.12 and on Ivory 3.42 — both clear the 3:1 threshold for UI components).

Olive never carries text, never fills a button, never sits behind a label, never
becomes a badge fill, never becomes a hover state. Olive on Anthracite (3.08) is
permitted only as a 1px decorative rule, never as a glyph a user must read.

#### Deep Olive `#575E3B` — interface only

Primary button fill on light, links, accent word inside a heading, slider fill,
badge outline and badge text, active nav underline, the small-caps product name on
a tariff card. **Never on Anthracite** (1.75). Never in the logo, never in the
brandbook, never in a printed report header.

#### Section rhythm down the home page

| # | Section | Ground | Note |
|---|---|---|---|
| — | Header | Ivory | Bar; hairline appears on scroll only |
| 1 | Hero — the report and its GPS proof | **Anthracite** | Ivory report sheet on dark reads as paper under a lamp |
| 2 | What this is, in three lines | Nude | Woven divider above |
| 3 | Sample report — the product | **Ivory, full bleed** | The whole band is the sheet |
| 4 | How it works — 3 steps | Nude | |
| 5 | Family Circle | **Anthracite** | Second dark band; our only true differentiator gets the weight |
| 6 | Products — Inspection apart, three cards | Nude | Cards Ivory; Optimal inverted to Anthracite |
| 7 | Plot calculator | **Ivory, full bleed** | Result panel Anthracite |
| 8 | MemoryCare Guarantees | Nude | Woven divider above |
| 9 | Method, equipment, verification | Ivory | |
| 10 | Free consultation | **Anthracite** | Form fields Ivory |
| — | Footer | Anthracite | Continuous with 10, separated by a 1px Olive rule |

Dark at positions 1, 5, 10 — opening, differentiator, close. Light everywhere
between. The eye gets three anchors and eight breaths.

---

### A.3 Space, grid, radii, borders, shadows

**Spacing scale (4px base).** 4 · 8 · 12 · 16 · 24 · 32 · 40 · 48 · 64 · 80 · 96 ·
128 · 160. Nothing off-scale. Optical exceptions require a written note in the file.

**Section padding.** Desktop light band 128 top / 128 bottom; dark band 144 / 144
(dark grounds need more air or they close in). Mobile 72 / 72, dark 80 / 80.

**Grid — 1440.** Page margin 120. Content max 1200. 12 columns, 24px gutter,
column 74px. The signature split is asymmetric: **main column = cols 1–8 (622px),
verification rail = cols 10–12 (222px)**, col 9 empty. Editorial body text sits in
cols 1–7. Full-bleed bands break the margin; content inside them returns to the grid.

**Grid — 375.** Margin 20. 4 columns, 16px gutter. The verification rail collapses
to a horizontal ruled strip beneath its content: two rows of label/value pairs
separated by a 1px Anthracite-12% rule, `rail` type, values right-aligned.

**Breakpoints.** 375 · 600 · 900 · 1200 · 1440. Real design at 375 and 1440;
600 and 900 are reflow only.

**Corner radii.** `0` for bands, photographs, the report sheet, dividers and the
plot diagram. `2px` for buttons, inputs, cards, badges, modals. `999px` only for
the slider thumb and the five-petal bullet's optical circle. Nothing else is round.
No 8px/12px/16px "friendly" radii — they are the wellness-template tell.

**Borders.** One hairline weight: **1px**. Three values only —
`Anthracite 12%` (object edges on light), `Ivory 16%` (object edges on dark),
`Olive 100%` (structural rules and the plot-diagram frame). A 2px border exists in
exactly one place: input error state. No 3px, no 4px, no accent rails on card edges.

**Shadows — none.** There is not one shadow in the system. Elevation is expressed
by a change of ground plus a hairline. Two managed consequences:
- Modals and the mobile sheet separate from the page with an **Anthracite 60% scrim**,
  not a shadow.
- The mobile sticky CTA bar sits on solid Ivory with a 1px Anthracite-12% top rule,
  and above it a 24px Nude→transparent gradient scrim so content does not appear
  to be sliced. That gradient is the only gradient permitted anywhere.

---

### A.4 Component visual specs

#### Buttons

Heights: 52 desktop / 48 mobile (both clear the 44px touch minimum). Radius 2.
Horizontal padding 28 / 24. Label `button`. Icons are 16px, optical-aligned, gap 10.
Full-width only inside a mobile card or the sticky bar.

**Primary, light ground** — fill Deep Olive, label Ivory (6.01).
- Hover: a 1px Ivory rule draws in from the left under the label over 160ms; the
  button gains a 1px Olive outline at 3px offset.
- Focus-visible: 2px Olive ring at 2px offset, plus 1px Ivory inner ring so the
  ring reads on both light grounds.
- Active: fill at 92% opacity (composites onto the ground — no new colour token).
- Loading: label stays, a 14px Ivory five-petal glyph rotates at the left, 900ms
  linear. It is the only permitted loop in the system.
- Disabled: **avoid.** Buttons stay enabled and validation is inline. Where a
  disabled state is unavoidable, fill Deep Olive 32%, label Anthracite 55%, cursor
  default, `aria-disabled`.

**Primary, dark ground** — fill Nude, label Anthracite (9.61). Same state logic,
hover rule in Anthracite, focus ring Olive.

**Secondary, light** — transparent, 1px Anthracite border, Anthracite label.
Hover: border → Olive, fill → Ivory. Focus as above.

**Secondary, dark** — transparent, 1px Ivory 40% border, Ivory label.
Hover: border → Ivory 100%.

**Text link / tertiary** — Deep Olive on light, Ivory on dark. Underline 1px at
0.14em offset, `text-decoration-skip-ink: auto`. Hover: underline 2px. On dark the
underline may be Olive (decorative, 3.08 against Anthracite — permitted as a rule,
never as the text itself).

There is no ghost button, no icon-only primary, and no button larger than 52px.

#### Inputs

Height 56 / 52. Radius 2. 1px Anthracite 20% border. Fill is always the *other*
light: Nude fill on an Ivory band, Ivory fill on a Nude band, Ivory fill on
Anthracite. Text `body` Anthracite, 16px minimum on mobile (prevents iOS zoom).

- **Label above, always.** `eyebrow`, Anthracite 70%. Placeholders are never used
  as labels; where a placeholder exists it is a format example only
  (`+1 818 555 0134`) at Anthracite 60%.
- Helper text `caption` Anthracite 70%, 8px below.
- Focus: border → Deep Olive, plus 2px Olive ring at 2px offset.
- Filled: border Anthracite 30%.
- **Error:** border 2px Anthracite, a 4px Anthracite bar on the left edge, a filled
  4px Anthracite dot before the message, message in Cabin 600 14 Anthracite.
  *See the open item in section B — we have no functional red and this needs an
  owner decision.*
- Phone field: country selector on the left inside the field, separated by a 1px
  Anthracite 20% rule, flag omitted (no flags anywhere — a diaspora audience does
  not need to be told which country it lives in). International format accepted.
- Textarea min-height 120, same styling.
- Checkbox 20×20, radius 2, 1px Anthracite border, checked = Deep Olive fill with
  an Ivory tick. Radio 20×20 circle, checked = 1px Deep Olive ring with an 8px
  Deep Olive core.

#### Cards

Ivory on Nude, 1px Anthracite 12%, radius 2, padding 32 desktop / 20 mobile, no
shadow, no hover lift. Hover on a linked card: border → Olive, title underline
draws. Structure top to bottom: eyebrow → title → body → hairline → footer row.

#### Tariff cards

**Inspection is set apart by form, not by decoration.** It is not a card. It is a
full-width horizontal band above the row, on the Nude ground, bounded by a 1px
Olive rule top and bottom, with nothing else: left, `eyebrow` "ONE-OFF · NO
SUBSCRIPTION" then h3 "Inspection" and a one-line description; right, `price`
`20,000 ֏ AMD` and a secondary button. Because it has no fill, it cannot be read as
a fourth member of the row.

**The row** — three Ivory cards, cols 1–4 / 5–8 / 9–12, gap 24.
Anatomy: product name (`eyebrow`, Deep Olive) · price (`price`, Anthracite) with
`֏ AMD / year` in `caption` at Anthracite 70% on the following line · 1px Olive rule ·
the visit line in `h4` ("4 full visits — one per season") · feature list, each item
led by a 6px Olive five-petal glyph at 0.6em from the baseline, `body-s`, 12px row
gap · a 1px Anthracite 12% rule · primary button, full width of the card.

**Optimal is marked as leading by inversion, not by a badge.** The Optimal card is
the only one on an Anthracite ground, its text Ivory, its price Nude, its rule
Olive, its button Nude-fill / Anthracite-label. It is 24px taller than its
neighbours and its top edge rises 24px above the row. Its lead label sits at the
top of the card: a 10px Olive woven-medallion glyph followed by "MOST CHOSEN" in
`eyebrow`, **Nude** (never Olive — Olive on Anthracite is 3.08). No ribbon, no
corner flag, no coloured fill, and the word "bestseller" appears nowhere in any
language.

**Special** is a ruled row beneath the whole block: 1px Olive rule, then one line —
"Larger plot, more monuments, several family plots — priced by the calculator.
Entry is always through Inspection." with a Deep Olive text link.

Never the phrase "light visit", "preventive visit", or "monthly". Every card says
**full visit**.

#### Calculator

Ivory full-bleed band. Two columns at 1440: controls cols 1–7, result panel cols
9–12 sticky at 96px from the top. Stacked at 375, result panel pinned to the
bottom of the viewport as a 96px bar while the sliders are in view.

- Slider track 2px, Anthracite 20%. Filled portion 2px Deep Olive. Thumb 20px
  circle, Deep Olive, 2px Ivory inner ring; focus adds a 2px Olive ring at 3px
  offset. Track hit-area 44px tall and invisible.
- Above each slider: the label in `eyebrow` on the left, the current value in
  Gloock `h3` tabular on the right ("24 m²", "3 monuments").
- Beneath each slider a paired **numeric stepper + text field**, because a slider
  alone is unusable for a 58-year-old on a phone and unusable by keyboard.
- Tick marks at the thresholds (16 m², 2 monuments) as 1px Olive verticals with a
  `caption` label "included".
- **Result panel** — Anthracite. `eyebrow` "OPTIMAL, PER YEAR" in Ivory 80%; total
  in `price-xl` Nude, tabular; then a transparent breakdown, one row per line,
  `body-s` Ivory 80%, values right-aligned, 1px Ivory 16% rules between:
  `Base 160,000` / `+8 m² above 16 × 10,000 = 80,000` / `+1 monument above 2 × 30,000`.
  A toggle switches the panel between Optimal and Maximum. Then a Nude primary
  button and a `caption` line "Price shown before any conversation. The same for
  every client." — the single most valuable sentence in the block.
- Past 100 m² / 10 monuments the panel replaces the total with a short message and
  a button routing to Inspection. No error styling — this is a normal outcome.
- **Numbers change instantly. No count-up animation.** A price that rolls like a
  slot machine is exactly the wrong register.

#### Report card and the sample report

The report is drawn as a physical document, not a dashboard.

- Sheet: Ivory, max-width 720 desktop / full-bleed-minus-20 mobile, radius 0, 1px
  Anthracite 12%, padding 40 / 20. On the Anthracite hero it needs no shadow — the
  ground change does the work.
- **Sheet header strip:** left, the mono mark at 20px plus "Visit report" in
  `eyebrow`; right, the verification rail — `Date · Cemetery · Plot · Crew` as
  label/value pairs in `rail`, values Anthracite, labels Anthracite 70%. 1px Olive
  rule below the strip, full sheet width.
- **Block order is fixed** (brief §8): (1) calm confirmation — `h3` "The visit took
  place", then date, plot, status badge; (2) the GPS verification element; (3) what
  was done — a short list with five-petal bullets; (4) photographs; (5) the crew's
  written note; (6) next visit date. Prices never appear on a report, in any view.
- **Status badge:** height 24, radius 2, padding 0 10, 1px Deep Olive outline,
  `eyebrow` in Deep Olive, preceded by an 8px glyph. No fill. On dark: 1px Ivory
  40% outline, Ivory label. States are distinguished by **glyph and outline weight**
  — Completed (filled medallion, 1px), Postponed (open ring, 1px), Rescheduled
  (open ring, 2px). *This is a compromise; see the open item in section B.*

#### The GPS verification element

Not a map screenshot and not a red pin — a map tile is someone else's brand and a
red pin is a delivery app.

A **plot diagram**: a 1:1 frame, 120px desktop / 96px mobile, 1px Olive border,
radius 0, Nude fill. Inside, three concentric 1px Olive circles at 20% opacity
(a bearing rose), a 1px Olive cross-hair at 30%, and at the true offset position a
solid **Olive five-petal glyph, 14px** — the plot itself. Beneath the frame, in
`rail` tabular: `40.1872° N, 44.5453° E`, then in `caption` Anthracite 70%:
"Coordinates recorded on site · 14:22 · 12 Sept 2026". To the right of the frame,
the "GPS VERIFIED" badge and one `body-s` line: "The device recorded its position
at your plot, not at the gate."

The same element, at 96px, is the trust anchor in the hero and appears once more
in "Method and verification". Three uses total. It is never animated and never
becomes a decorative pattern.

#### Before / after presentation

Side-by-side as the opening image reads as a cleaning-product advertisement.
So the report shows them **in sequence, vertically**:

1. `eyebrow` "CONDITION ON ARRIVAL" left, timestamp in `rail` right, 1px Anthracite
   12% rule between label and image, image full sheet width at **4:3**.
2. 32px gap. `eyebrow` "AFTER THE VISIT", timestamp, image at **4:3**.
3. Further down, and only there, an optional compact **2-up comparison** at **4:5**
   each with a 1px gutter of Nude showing between, headed "Compare".

No drag-slider handle, no wipe, no 50/50 curtain, no arrows between the two, no
"BEFORE"/"AFTER" burned into the image. Labels are typographic and sit outside the
frame.

#### Family Circle

On the Anthracite band. Members are shown as a horizontal row of 48px circles —
Nude fill, initials in Cabin 600 16 Anthracite (9.61), 1px Ivory 40% ring, −12px
overlap. The owner's circle carries a 1px Olive outer ring at 3px offset. No
photographs of people, no stock avatars. Permission differences are shown as a
small ruled table beneath, `rail` for column heads, a filled 6px Olive square for
"can" and an empty 6px 1px-Ivory-40% square for "cannot" — plus a text column, so
the meaning never depends on the glyph alone.

---

### A.5 Photography and placeholder art direction

**Ratios — fixed, no exceptions.**

| Use | Ratio | Export |
|---|---|---|
| Report photograph, full width | 4:3 | 1600×1200 |
| Comparison pair | 4:5 | 1000×1250 |
| Section illustrative image | 3:2 | 1800×1200 |
| Crew / equipment portrait | 1:1 | 1000×1000 |
| Hero background (if ever used) | 16:9 | 2400×1350 |
| OG / link preview | 1.91:1 | 1200×630 |

**Treatment rules.**
- Radius 0. No border. **No black border under any circumstance.** No shadow, no
  vignette, no duotone, no olive wash, no grain, no film emulation, no HDR.
- Natural exposure, neutral white balance, mild contrast. Overcast or open shade
  preferred; hard midday sun makes stone look like a monument catalogue.
- Framing: the plot occupies the lower two-thirds, sky or path above. Camera at
  standing eye height, level. Never a low heroic angle, never a drone shot directly
  over a grave (drone footage is for context and access routes only).
- **Neighbouring plots' names and inscriptions must be out of frame or out of
  focus.** The subject's own inscription is shown only with the client's consent.
- Crew appear working, hands and equipment in frame, never posed, never smiling to
  camera, never in a "team photo". Faces of mourners never appear.
- No flowers arranged for the photograph, no candles, no crosses composed as
  graphic elements, no black-and-white conversion.
- The before and after frame must be **identical** — same position, same focal
  length, same height. This is the whole evidentiary point; the crew gets a marked
  standing position for it.

**Placeholders (until the September shoot).**
A placeholder is a Nude rectangle at the exact final ratio, 1px Olive border, and:
- a single Olive five-petal glyph at 8% opacity, 240px, bleeding off the
  bottom-right corner, rotated 0° (never a repeating pattern);
- in the lower-left, in `caption` Anthracite 70%, four facts on two lines:

```
PLACEHOLDER · 4:3 · 1600×1200
"Condition on arrival — Tokhmakh, section 12" · September shoot
```

No "image coming soon", no camera icon, no grey box, no `lorem`. Every placeholder
names its ratio, its pixel size, its subject and its source. A placeholder that
does not name all four is not shippable.

**Link preview, hard rule.** The OG image is generated, never a photograph:
Anthracite ground, mono light mark at 96px, "Visit report" in `h3` Ivory, and the
date in `rail` Ivory 80%. Nothing else. A photograph of a burial must never appear
in a WhatsApp or Viber preview.

---

### A.6 The header problem — no horizontal lock-up

The primary lock-up is vertical and every SVG sits in a 1080×1080 artboard with
large asymmetric padding. Squeezing the vertical lock-up into a 72px bar would make
the mark tiny and the tagline illegible, and scaling the padded artboard would make
the logo appear to float off-centre.

**Proposal: construct a horizontal lock-up from the existing parts, and specify it.**
We do not draw anything new; we define a relationship between two supplied assets.

1. **Deliver two tightly-bounded exports** (a design-team task, not a developer
   guess): `mc-mark.svg` and `mc-wordmark.svg`, each trimmed to its own ink
   bounding box with zero padding. The 1080×1080 files are never referenced by the
   site. Provide mono-dark, mono-light and colour variants of each.
2. **The header lock-up** = mark + wordmark, side by side.
   - Mark height **32px** desktop / **28px** mobile.
   - Vertical alignment: the mark's optical centre aligns to the wordmark's
     **cap height centre**, not to its bounding box. Expect a 1–2px optical nudge;
     record it in the spec.
   - Gap between mark and wordmark = **0.5 × mark height** (16px / 14px).
   - Wordmark cap height 18px desktop, ~148px wide; 16px mobile, ~130px wide.
   - Clear space around the whole lock-up = **0.75 × mark height** on all sides.
3. **Colour in the header.** The header ground is Ivory, and the colour mark's
   hands are Ivory — they would vanish. So the header uses the **mono-dark**
   variants of both parts, in Anthracite. The two-colour wordmark ("Memory" Ivory /
   "Care" Olive) is used only on Anthracite: the footer and the OG image. Note that
   in the two-colour version "Care" in Olive on Anthracite is 3.08 — acceptable for
   a logo (large forms, not body text) but it is the reason the header does not use it.
4. **The tagline never appears in the header.** It appears exactly once per page, in
   the footer, under the vertical primary lock-up, Olive small caps, `eyebrow`
   tracking, **no full stop**: `HONORING MEMORY, CARING FOR LOVED ONES`.
5. **Degradation rule: the wordmark survives, not the mark.** At the narrowest
   layouts, drop the mark and keep "MemoryCare" set as the wordmark. `MC` and
   "MEMORYCARE" are forbidden; the name must always be readable, in English, in the
   header, for a person who arrived from a Google result about dementia care.
6. **Header behaviour.** Height 72 desktop / 60 mobile. Ivory, sticky, no shadow;
   a 1px Anthracite 12% bottom rule fades in over 120ms after 8px of scroll.
   Desktop: lock-up left; 5 nav items centre-right in `nav`, active item carrying a
   1px Deep Olive underline at 6px offset; then the language switcher; then a
   Deep Olive primary button "Free consultation". Mobile: lock-up left, a 44px
   call-button (phone glyph, secondary style) and a 44px menu button right;
   the persistent primary CTA lives in the bottom sticky bar, not the header.
7. **Language switcher.** Three text items `ARM · ENG · RUS` separated by 1px Olive
   verticals, current item Anthracite 100%, others Anthracite 60% (6.3:1). Not a
   dropdown, not a globe icon, no flags — three characters-wide items are faster and
   unambiguous, and a diaspora visitor should see their language exists without a click.

---

### A.7 Motion

Motion is used to confirm, never to entertain. Total motion budget on the home
page: six behaviours.

| Where | What | Duration / curve |
|---|---|---|
| Header | Bottom hairline fades in on scroll | 120ms linear |
| Section entrance | opacity 0→1 with translateY 8px→0, once, staggered 60ms, max 3 items per section | 320ms `cubic-bezier(.2,.7,.2,1)` |
| Buttons / links | Underline draws from left | 160ms `ease-out` |
| Slider | Fill and thumb track the input | 120ms linear |
| Accordion (FAQ, legal, permission table) | height + opacity | 240ms `cubic-bezier(.2,.7,.2,1)` |
| Report images | Fade in on decode, no skeleton shimmer | 200ms linear |

**Forbidden, explicitly:** parallax of any kind; count-up or rolling numerals in
the calculator or anywhere else; auto-advancing carousels; hover-zoom or Ken Burns
on a photograph of a plot; scroll-jacking or pinned scroll sequences; a rotating or
"blooming" medallion; falling petals; typewriter text; a before/after wipe that
plays itself; any parallax or transition on the Family Circle avatars; and any
animation whatsoever on the sample report photographs, on a bad-news screen, or on
a guest report view. The only permitted loop in the entire system is the 14px
five-petal loading glyph.

`prefers-reduced-motion: reduce` — all entrance animations off, all transforms
removed, everything reduced to opacity at ≤100ms. This must be tested, not assumed;
a meaningful share of a 40–60 audience has it on.

---

## B. UX implications of the visual system

Only where the visual language constrains layout or behaviour.

1. **The verification rail needs data.** Every report and visit component reserves
   a 222px right column for date, cemetery, plot, crew and coordinates. If the
   platform cannot supply a field the layout must not collapse — specify a fallback
   row ("Coordinates pending upload") in Anthracite 70%, never an empty cell. The
   developer needs these fields in the API; raise it now, not at integration.

2. **The inverted Optimal card changes DOM order.** At 1440 Optimal is the middle
   card; at 375 it must be first. Source order should be Optimal → Express →
   Maximum with a desktop grid reorder, so the mobile reading order and the
   keyboard tab order agree without CSS trickery that breaks screen readers.

3. **Naming discrepancy to resolve.** The brief calls Inspection "apart from the
   three annual subscriptions", but only Optimal and Maximum are annual — Express
   is a one-off. My layout puts Express, Optimal and Maximum in the row and labels
   Express "ONE VISIT · NOT A SUBSCRIPTION" in its eyebrow. Strategy and copy must
   confirm this grouping, because it determines whether the row is three cards or two.

4. **No shadows means overlays need a scrim.** Every modal, mobile sheet, language
   menu and image lightbox separates with an Anthracite 60% scrim and a 1px hairline.
   Without the scrim an Ivory modal on a Nude page is invisible.

5. **The two lights force a nesting rule.** No Ivory surface inside an Ivory band.
   Cards inside the Ivory calculator and Ivory report bands are hairline-only, no
   fill. Anyone building components must know this or the pages will go flat.

6. **Sliders are not sufficient input.** Each calculator slider ships with a paired
   stepper and numeric field. Keyboard and older-phone users cannot be asked to drag
   a 20px thumb to an exact square metre.

7. **The sticky mobile CTA bar is 64px.** Every page needs 80px of bottom padding,
   and no fixed element may sit under it. On the report screen and on the guest
   report view the bar is **removed entirely** — no CTA appears beside a photograph
   of a grave.

8. **Status colour is missing and it is a real gap.** We have no red, no amber and
   no green, and the brief forbids a sixth colour. My system distinguishes states by
   outline weight, glyph and wording. That works for three badge states; it will not
   comfortably carry the portal's bad-news screens (weather postponement, no access
   to the plot, failed payment, guarantee re-visit requested) or form errors. **Open
   item for the owner and the designer:** either approve two functional semantic
   colours used exclusively in system messaging and never in brand surfaces, or
   accept an all-typographic error language. I recommend the former, scoped tightly.

9. **Localisation headroom.** Armenian and Russian run 25–40% longer than English.
   Every fixed-height element (buttons, badges, tariff visit lines, nav items) must
   either wrap gracefully or has a character budget below. Nothing in the layout may
   depend on a heading fitting on exactly two lines.

10. **Focus visibility on both lights.** The Olive focus ring at 3.12/3.42 clears
    3:1 but not by much. Every focus ring carries a 1px Ivory or Anthracite inner
    ring so it survives on any ground. Do not let a developer replace it with a
    browser default.

11. **Photographs are large and this is a phone-first, sometimes-abroad audience.**
    4:3 at 1600px wide is the report standard, but delivery must be responsive
    (`srcset` at 480/800/1600) with AVIF/WebP and lazy loading below the fold. A
    report that takes fifteen seconds on a Yerevan-to-Los-Angeles connection is a
    broken product regardless of how it looks.

---

## C. Content implications — character budgets

These are the budgets my layouts impose in **English**. Armenian and Russian will
run longer, so the English budgets already carry roughly 20% headroom; treat the
number as the ceiling, not the target.

| Element | Budget (characters, incl. spaces) | Constraint |
|---|---|---|
| Hero H1 | **38–46**, hard max 52 | 2 lines at 1440 (18–23/line), 3 lines at 375 |
| Hero standfirst | **100–130** | 2 lines desktop, 4 mobile |
| Section eyebrow | **24** | one line at 375 |
| Section H2 | **34–44** | max 2 lines at both widths |
| Section standfirst | **140–180** | 2–3 lines |
| Card / step title (h3–h4) | **28** | one line desktop, two mobile |
| Card body | **90–120** | 3 lines at 375 |
| Tariff product name | **14** | Express / Optimal / Maximum / Inspection all fit |
| Tariff visit line | **34** | "4 full visits — one per season" = 30 |
| Tariff feature bullet | **48** | one line at 375 including the glyph |
| "Most chosen" label | **12** | |
| Primary button label | **14–22**, hard max 24 | Armenian +40% must still fit 52px height |
| Mobile sticky-bar button | **16** | "Free consultation" = 18 — trim to "Get a consultation"? no: use "Free consultation" and accept 2 chars over at 375 with tracking at 0 |
| Secondary button label | **20** | |
| Badge | **12** | "GPS VERIFIED" = 12 |
| Rail label / value | **12** / **18** | tabular, right-aligned |
| Guarantee title | **30** | |
| Guarantee body | **110** | |
| Report block heading | **24** | "The visit took place" = 20 |
| Report crew note | **220–320** | the only place a human voice is permitted |
| Calculator result caption | **90** | |
| Nav item | **16** | 5 items max at 1440 |
| Footer link | **22** | |
| Form label | **20** | |
| Form helper | **70** | |
| Error message | **80** | must fit 2 lines under a 56px field |
| Empty-state heading | **28** | |
| Empty-state body | **150** | |
| OG title | **60** | must contain the name and the category |
| Meta description | **150** | must pair "MemoryCare" with "grave care" and "Yerevan" — in English the phrase "memory care" belongs to dementia care, so the bare brand name in a title is a wasted result |
| Tagline | fixed | `HONORING MEMORY, CARING FOR LOVED ONES` — 38 chars, no full stop, footer only |

Two content rules that follow from the layout rather than from the brand:

- **The hero H1 has room for one idea.** At 40–46 characters it cannot carry both
  audiences' reasons. Lead with the outcome; the two reasons — distance and time —
  belong in the standfirst, which has 130 characters and can hold both without
  choosing one.
- **The report is the only surface where a first-person sentence is allowed** (the
  crew note). Everywhere else the voice is factual and third-person, because the
  page's whole visual argument is that these are records, not marketing.

---

## Open items I am handing on

1. Functional status colours for the portal — approve two, or accept an
   all-typographic error language (B.8).
2. A display face with Armenian coverage; Gloock has none. Localisation is blocked
   on this.
3. Tightly-bounded `mc-mark.svg` and `mc-wordmark.svg` exports; the 1080×1080 files
   must not be used on the site.
4. Whether the tariff row is three cards (Express, Optimal, Maximum) or two (B.3).
5. Legal address — placeholder, marked as such in the footer and listed for the developer.
6. Cabin must be labelled a Gill Sans substitute on every mock and in the built page's
   font-stack comment.
