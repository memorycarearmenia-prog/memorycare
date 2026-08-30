# MemoryCare — Final UI Specification

**Author:** Visual Design Lead · **Date:** 30.08.2026 · **Language:** English
**Status:** binding. This document supersedes `01`–`05` and `r2-01`–`r2-05`.
**Above it, in this order:** `DECISIONS.md`, `DECISIONS-2.md`, `BRIEF.md`.
Where a round-one or round-two document disagrees with a line below, this
document wins; where this document disagrees with the two `DECISIONS` files,
they win.

*Cabin is used as a free substitute for Gill Sans (commercial Monotype,
unlicensed for web). It is not the brand text face. This sentence is repeated in
`FONTS.md`, in `tokens.json` `$description`, as a comment in the generated CSS,
on Figma page `01 · Foundations`, and in the footer of every exported spec.*

---

## 1. The visual concept

MemoryCare keeps records of care, so the interface is built like a record and
not like a brochure: **paper laid on stone**. Nude is the ground — warm,
mineral, slightly dusty, the colour of the site itself — and Ivory is paper:
every report, form, card, calculator panel and header bar is a discrete sheet
placed on that ground and separated from it only by a hairline, the way a sheet
of paper is separated from a stone table. Every element that carries proof —
a report, a visit, a guarantee, a price — carries the **verification rail**, a
narrow band of flat tabular metadata (date, cemetery, plot, crew, coordinates,
time on site) that a generic wellness template does not have and cannot fake;
it is the visible form of "we sell proof, not cleaning". The brand's own
vocabulary supplies the marks and each has exactly one job: the five-petal
forget-me-not is the list bullet and the point marker on the plot diagram, never
wallpaper; the woven medallion is the section divider, drawn once and used at
most four times on a page; Olive hairlines rule the page the way a plot boundary
rules a cemetery — horizontal, thin, absolute. Layout is asymmetric and flush
left, Gloock set very large against a generous left margin and a short measure,
Anthracite reserved for exactly two full-bleed bands per page so that darkness
stays an anchor and never becomes a funeral. There is no centred hero, no
gradient except one 24px scrim, no shadow except on overlays, no rounded
accent-railed card, no photograph of a person's grief. The page is quiet, ruled
and factual, and its warmth comes entirely from the Nude ground and the size of
the type — which is the register in which a person at 1 a.m. in Glendale decides
to trust a company with their mother's grave.

---

## 2. Surface rules

Six colours. Nothing else is ever added.

| Token (L1) | Value | Name |
|---|---|---|
| `--mc-color-olive-500` | `#7C8654` | Olive |
| `--mc-color-olive-700` | `#575E3B` | Deep Olive |
| `--mc-color-nude-500` | `#EFE5D5` | Nude |
| `--mc-color-ivory-500` | `#F3F0E9` | Ivory white |
| `--mc-color-anthracite-500` | `#33373C` | Anthracite |
| `--mc-color-feedback-error` | `#8C3A2E` | Error (the sixth and last colour) |

Derived values that are **not** new hues and are the only derivations permitted:

| Token | Value | Note |
|---|---|---|
| `--mc-text-secondary` | `#606161` | A solid token, never an opacity. 4.98 on Nude, 5.46 on Ivory. |
| `--mc-border-default` | `rgba(51,55,60,0.12)` | Object edge on light |
| `--mc-border-strong` | `rgba(51,55,60,0.20)` | Input rest border |
| `--mc-border-on-dark` | `rgba(243,240,233,0.40)` | Object edge on Anthracite |
| `--mc-rule-on-dark` | `rgba(243,240,233,0.16)` | Hairline on Anthracite |
| `--mc-surface-scrim` | `rgba(51,55,60,0.60)` | Overlay scrim |
| `--mc-surface-feedback-error-subtle` | `rgba(140,58,46,0.10)` | An alpha, never a second hex |

**No token in this system may end in `-success` or `-warning`.** `lint:tokens`
rejects both suffixes outright. There is no green, no amber, no `danger` name,
no `Button--danger`, no `Toast--success`. Success and attention are carried by a
word, a glyph and a rule weight.

### 2.1 Which ground is Nude

Nude `#EFE5D5` is **the ground**, and only the ground:

- the page background of every marketing page and every portal screen;
- every full-bleed light `<section>` — a full-bleed section is Nude or it is
  Anthracite, never Ivory;
- the fill of an input that sits on an Ivory surface;
- the zebra row of a table drawn on Ivory;
- the fill of a primary button on an Anthracite band (label Anthracite, 9.61);
- the fill of the plot-diagram frame in `GpsVerification`;
- text on Anthracite, interchangeably with Ivory — see 2.3.

### 2.2 Which ground is Ivory

Ivory `#F3F0E9` is **paper** — a discrete object placed on the ground, never a
page or a band:

- cards, tariff cards, the report sheet, the calculator panel, guarantee panels,
  modals, drawers, bottom sheets, toasts, menus;
- the header bar and the mobile action bar (both are sheets, both carry a
  permanent hairline);
- the fill of an input that sits on a Nude ground or on an Anthracite band;
- all light text on Anthracite where the text is a heading or body — see 2.3.

Two absolute rules, both machine-checked by `stylelint-mc-contrast`:

1. **Ivory is never a page background and never a full-bleed band.** The
   "document moment" full-bleed Ivory band proposed in round one is deleted; the
   sample report and the calculator are Ivory *objects* on the Nude ground,
   which states the paper-on-stone idea more purely and survives an automated
   check. Header and action bar are the two declared exceptions, and they are
   bars, not bands.
2. **Ivory never sits directly on Ivory.** A card that would land on an Ivory
   surface loses its fill and is defined by a 1px `--mc-border-default` alone.
3. **An Ivory object on Nude always carries a 1px `--mc-border-default`.**
   Without it the 1.1 tonal step reads as a printing error.

Nude and Ivory are told apart only by consistent role. Write it on the wall:
**Nude is the ground, Ivory is the paper.**

### 2.3 Where Anthracite bands appear, and how many

Anthracite `#33373C` is a warm graphite. It is never pushed to `#000` and never
used as a border around a photograph.

**Exactly two full-bleed Anthracite bands per marketing page, no exceptions.**
On Home they are: **Family Circle** (our only true differentiator gets the
weight) and the **closing CTA band, which runs continuously into the footer**,
separated from it by a 1px Olive rule. The hero is **Nude**: a dark hero spends
the page's scarcest asset on the first screen where the brief's tone rule is
strictest, costs 8–16px of fold, and forces a second header variant. Inner pages
carry the same two: the page's own differentiator band (or none) and the closing
CTA→footer. Portal screens carry **zero** Anthracite bands — the portal is a
working surface, not a sales page.

On Anthracite: headings and body in Ivory or Nude (10.53 / 9.61 — both pass at
any size); secondary text in Ivory only, as the solid token
`rgba(243,240,233,0.80)` composited ≈ 8.3; primary button = Nude fill with an
Anthracite label; secondary button = 1px `--mc-border-on-dark` with an Ivory
label; the footer tagline is **Nude**, never Olive.

**The request form may never sit on an Anthracite band.** The error red on
Anthracite is 1.57 — it fails text and the 3:1 non-text floor, so a form there
cannot show a validation error at all. The closing CTA band therefore carries a
heading, a support line and buttons only; the form itself lives on Nude
(`/consultation/`, the modal on an Ivory sheet, and the in-page form sections).
This is a structural rule, not a preference.

### 2.4 Where Olive appears

Olive `#7C8654` **never carries text and never has text placed on it.** Ivory on
Olive is 3.42, Anthracite on Olive is 3.08; nothing is legible on an Olive fill
at any size. This is the palette's single most likely production mistake — two
independent reviewers reached for it — so it is blocked in the linter, not in
prose. Olive has exactly five jobs:

1. Structural hairline rules between content groups — 1px, 100% opacity, never
   an opacity variant (Olive at 20% over Nude is a 1.05 step; it is invisible).
2. The woven-medallion section divider, at most four times per page.
3. The five-petal bullet glyph in feature lists, and the point marker on the
   plot diagram.
4. The tagline, in print, in the logo lock-ups and in the OG image only.
5. Focus rings and the frame of the plot diagram — non-text UI, where 3.12 on
   Nude and 3.42 on Ivory clear the 3:1 threshold. On Anthracite, Olive is
   permitted only as a 1px decorative rule (3.08 ≥ 3:1), never as a glyph a user
   must read.

Olive never fills a button, never sits behind a label, never becomes a badge
fill, never becomes a hover state, and never becomes wallpaper.

### 2.5 Where Deep Olive appears

Deep Olive `#575E3B` is **interface only**. It exists because Olive fails
contrast everywhere. It never enters the logo, the brandbook or a printed report
header.

- Primary button fill on light grounds (label Ivory, 6.01).
- Links and accent text on light (5.49 on Nude, 6.01 on Ivory).
- A single accent word inside an H1 or H2 — the only permitted emphasis inside
  display type.
- Badge fill for the leading tariff, with an Ivory label.
- Slider fill and thumb, checkbox and radio checked state.
- Active nav underline, the "Care" half of the live-text header wordmark.
- The product name in small caps at the head of a tariff card.
- The `Cancel subscription` text link and every other calm destructive action.

**Deep Olive is never used on Anthracite** — 1.75, it disappears. No component
may reference `--mc-color-olive-700` directly; all accent colour goes through
`--mc-text-accent` / `--mc-border-accent` / `--mc-surface-accent-strong`, which
the `.mc-on-dark` band scope rewrites to Nude. The linter rejects a raw
`olive-700` reference outside the semantic layer.

### 2.6 Where the error red appears — the complete list

`--mc-color-feedback-error` `#8C3A2E` is a terracotta in the palette's own
family: warm, earthed, low saturation. It appears in **three places and nowhere
else**:

1. **Field validation.** A 2px inset border on the field (inset, so the field
   does not change height), a 16px error glyph, and the message beneath in
   `--mc-text-feedback-error` at 14px. The required-field marker in the label is
   the same colour. Colour is never the only signal: glyph plus sentence carry
   it.
2. **The form-level failure summary after submit** — the same component at the
   top of the form, `role="alert"`.
3. **Payment failure.** An inline panel on `--mc-surface-feedback-error-subtle`
   with a 2px `--mc-border-feedback-error` inline-start rule and the heading in
   the error colour. Not a modal, not a toast: a failed payment is a screen. A
   missed error here is an unfinished payment.

**Where it is forbidden — this list matters more than the first.**

- **Never on an Anthracite ground** (1.57). If a validation error must ever
  surface on dark, it is Nude text plus a 2px Nude inline-start rule plus the
  word "error" spelled out — no colour at all. In practice this never happens,
  because forms do not sit on dark bands.
- **Never on a report screen, a guest view or the report PDF.** A red mark
  beside a photograph of a grave is the worst thing this system could do.
- **Never as a button fill.** There is no error button. Cancelling a
  subscription is a calm Deep Olive text link.
- **Never as a status for "Visit moved" or "Could not reach the plot".** Those
  are reports of a visit that happened, with GPS proof that the crew was there —
  not faults. Neutral outline badge, glyph and word.
- **Never in the calculator ceiling state.** Passing 100 m² is a normal outcome
  and a route to Inspection.
- **Never on 404 or 500.**
- **Never as a countdown, a scarcity marker, or anything attached to the 60-day
  credit window.**
- **Never a border around a photograph, never a fill behind body text, never a
  toast rule.** There is no error toast; errors are inline or a screen.
- Never in a bad-news status screen, an expired link, an expired invitation, a
  failed report load, a session timeout, or a cancellation flow.

It appears at most twice in a session, always at 2px or as 14px type, never as a
fill larger than a chip, always on a warm light ground it was mixed to sit on,
and it is structurally incapable of appearing near a photograph. It is the only
colour in the system whose prohibition list is longer than its permission list,
which is what makes it read as part of the palette rather than a framework
default.

---

## 3. Type system

**Display: Gloock Regular** (Google Fonts, 400, one weight).
**Text: Cabin** 400 / 500 / 600 / 700 — *substitute for Gill Sans.*
Both self-hosted as subset woff2 (Russia, and the bank dislikes third-party
requests). ≤180 KB per locale.

### 3.1 Solving the single-weight constraint

Gloock cannot make hierarchy by weight, so hierarchy is made by five other means
and Gloock's job is deliberately narrowed:

1. **Gloock is rationed to five slots:** H1, H2, H3 (desktop only), price
   numerals, and one pull-quote per page. Everything else — H4 and below, all
   UI, all labels, all data — is Cabin, which has four weights and carries the
   fine-grained hierarchy.
2. **Size steps are large.** Between adjacent Gloock levels the ratio is never
   below 1.35, so two Gloock levels can never be confused at a glance.
3. **Measure differentiates.** H1 is set to a 16–22 character line, H2 to 28–34,
   H3 to a full 44. Line length reads as rank before size does.
4. **Colour differentiates.** Gloock is Anthracite on light, Nude on dark. One
   Deep Olive word inside an H1 or H2 is the only permitted emphasis inside
   display type.
5. **Optical floor: Gloock is never set below 24px, in any medium, including
   PDF.** Its hairlines break up. Below 24px the role is handed to Cabin 600 —
   which is why mobile H3 is Cabin.

Never synthesise a bold or an italic of Gloock, never letterspace it positive,
never set it in all caps.

### 3.2 Scale at 1440

| Token | Face / weight | Size / line-height | Tracking | Use |
|---|---|---|---|---|
| `display` | Gloock 400 | 76 / 82 (1.08) | −0.02em | Hero H1 only |
| `h1` | Gloock 400 | 60 / 66 (1.10) | −0.015em | Page titles |
| `h2` | Gloock 400 | 44 / 50 (1.14) | −0.01em | Section heads |
| `h3` | Gloock 400 | 30 / 38 (1.27) | −0.005em | Sub-sections, card titles |
| `h4` | Cabin 600 | 20 / 28 (1.40) | 0 | In-card and in-report headings |
| `price-xl` | Gloock 400 | 56 / 58 | −0.01em, tabular | Calculator total |
| `price` | Gloock 400 | 40 / 44 | −0.01em, tabular | Tariff card price |
| `quote` | Gloock 400 | 34 / 46 (1.35) | −0.005em | One pull-quote per page |
| `body-lg` | Cabin 400 | 19 / 30 (1.58) | 0 | Standfirsts, report body, legal, About |
| `body` | Cabin 400 | 17 / 27 (1.59) | 0 | Default paragraph |
| `body-sm` | Cabin 400 | 15 / 23 (1.53) | 0 | Card body, dense lists |
| `caption` | Cabin 500 | 14 / 20 | +0.01em | Image captions, helper text |
| `rail` | Cabin 500 | 14 / 20 | +0.06em, tabular | **Verification rail, report metadata** |
| `overline` | Cabin 600 UC | 13 / 18 | +0.14em | Section eyebrows, badges, card labels |
| `button` | Cabin 600 | 16 / 20 | +0.02em | All button labels |
| `nav` | Cabin 500 | 15 / 20 | +0.01em | Header nav, footer links |
| `legal` | Cabin 400 | 15 / 26 | 0 | Footer legal, disclaimers |

### 3.3 Scale at 360

| Token | Face / weight | Size / line-height | Tracking |
|---|---|---|---|
| `display` | Gloock 400 | 32 / 38 (1.19) | −0.015em |
| `h1` | Gloock 400 | 30 / 36 (1.20) | −0.01em |
| `h2` | Gloock 400 | 26 / 32 (1.23) | −0.005em |
| `h3` | **Cabin 600** | 20 / 28 | 0 *(below the 24px Gloock floor)* |
| `h4` | Cabin 600 | 18 / 26 | 0 |
| `price-xl` | Gloock 400 | 40 / 44 | −0.01em, tabular |
| `price` | Gloock 400 | 32 / 36 | −0.01em, tabular |
| `quote` | Gloock 400 | 26 / 36 | 0 |
| `body-lg` | Cabin 400 | 17 / 27 | 0 |
| `body` | Cabin 400 | 16 / 26 | 0 |
| `body-sm` | Cabin 400 | 15 / 23 | 0 |
| `caption` | Cabin 500 | 14 / 20 | +0.01em |
| `rail` | Cabin 500 | 14 / 20 | +0.06em, tabular |
| `overline` | Cabin 600 UC | 13 / 18 | +0.14em |
| `button` | Cabin 600 | 16 / 20 | +0.02em |
| `nav` | Cabin 500 | 16 / 24 | +0.01em |
| `legal` | Cabin 400 | 15 / 26 | 0 |

`display` at 360 is 32px because the fold arithmetic in 9.1 requires it; it
rises through `clamp()` to 76 at 1440. `body` is `clamp(1rem, …, 1.0625rem)` —
16 → 17, which satisfies the reading floor and the iOS-no-zoom rule at once.

### 3.4 Floors and prohibitions

- **Informational floor: 14px.** Anything that carries meaning in a sentence —
  captions, helper text, the verification rail, legal small print — is 14px or
  larger. 13px exists only for `overline`, a decorative uppercase tracked label.
  Nothing in the product, in any medium, is below 13px. **The 11–12px rail
  proposed in round one is retired**: it carried the actual proof (date,
  cemetery, plot, crew, coordinates) for an audience of 40–60 reading on a phone
  at night.
- **Body never below 15px anywhere**; 16px minimum for body on mobile.
- **Every input is 16px** — below 16 iOS zooms on focus.
- `--mc-text-secondary` (`#606161`) is restricted to **≥15px**. It is never
  applied to `caption` or `rail`; those are Anthracite or, on dark, Ivory.
- **Opacity is banned for text system-wide.** "Anthracite at 70%" resolves to
  4.28 on Nude and fails. Use the token.
- Uppercase is banned in Armenian (`:lang(hy)` branch on `overline` and `rail`):
  Armenian caps read as shouting. Values are never uppercase in any script.
- Tabular lining figures everywhere a number can change: prices, calculator,
  coordinates, dates, visit counts. Proportional only inside running prose.
- **Measure:** body 62–70 characters at 1440, 34–42 at 360; display 16–22 per
  line; report body 58–64 — a report is read, not scanned.

### 3.5 The ֏ glyph fallback rule

Gloock is Latin/Latin-ext and **does not contain ֏ (U+058F)**. Whether Cabin
contains it is unverified and cannot be verified in this session. The rule below
is correct whichever way that resolves, and it satisfies `DECISIONS.md §5`.

1. **The numeral may be Gloock. `֏ AMD` is always the text face**, at `caption`
   size, and never baseline-aligned against a display numeral. On a tariff card
   the amount is `price` and `֏ AMD / year` sits on the following line in
   `caption`. Both forms are always printed — the symbol **and** the letters
   `AMD` — which is a bank requirement and which also means a total glyph
   failure still leaves the price legible.
2. **Every currency glyph is emitted in its own element** by the price
   formatter, bound to its own family:

```html
160,000 <span class="mc-currency">֏</span> AMD
```
```css
.mc-currency { font-family: var(--mc-font-currency); }
--mc-font-currency: "Noto Sans Armenian", "Noto Sans", "Cabin", system-ui, sans-serif;
```

`"MC Dram"` may be declared instead as a single-codepoint face:
`@font-face { font-family:"MC Dram"; src:url("/fonts/noto-sans-armenian-400.woff2") format("woff2"); unicode-range:U+058F; font-display:swap; }`
placed first in both `--mc-font-display` and `--mc-font-text`. Either form is
acceptable; the second is preferred because it fixes Gloock as well.

3. **Every `@font-face` declares an explicit `unicode-range`**, so a missing
   glyph falls to the next family and never renders as tofu. Every stack
   terminates in `system-ui` and a generic family.
4. **`qa/glyphs.spec.ts` turns the unverified claims into build failures**:
   U+058F present in the currency family; U+0531–U+058A and U+FB13–FB17 in the
   `hy` stack; U+0400–U+04FF in the `ru` stack; digits plus tabular figures in
   whichever family sets prices. A locale does not ship until its assertion
   passes.
5. If the display face proves to lack tabular figures, `--mc-type-price` falls
   back to the text face at 600 — one token change, no component edits.
6. **Localisation of the display face.** The target is one face covering Latin,
   Cyrillic and Armenian; choosing it is the designer's and the owner's call and
   it does not block the English build. Until it exists, `hy` and `ru` headings
   fall to the **text face at 600**, never to a second serif — a heading in the
   text face reads as a deliberate system, a heading in a different serif reads
   as a broken font. Three display faces are refused. `font-display: optional`
   on display type in `hy`/`ru`, with `size-adjust` / `ascent-override` on the
   fallback declaration, so the 0.05 CLS budget holds.

### 3.6 Character limits per slot

English is the source. Localisation headroom: **hy +25%, ru +15%**. Every limit
is a grapheme count enforced by `content-limits.json` and `qa/strings.spec.ts`.
Overflow **wraps**; it never ellipsises a badge or a button.

| Slot | EN | hy | ru | Note |
|---|---|---|---|---|
| `hero.h1` | **≤48** | 58 | 55 | Hard. Derived from the fold table in 9.1: a third line costs the CTA. Canonical string: `You will see exactly what was done, and when.` (44) |
| `hero.standfirst` | ≤105 | 130 | 120 | Three lines at 360 |
| `hero.eyebrow` | ≤42 | 52 | 48 | Carries the dementia-care disambiguation |
| `page.h1` | ≤52 | 64 | 60 | |
| `section.h2` | ≤56 | 70 | 64 | |
| `section.h3` | ≤48 | 60 | 55 | |
| `overline` | ≤28 | 34 | 32 | Sentence case in hy |
| `body.paragraph` | ≤420 | 520 | 480 | Per paragraph |
| `button.label` | **≤22** | 27 | 25 | Buttons must survive two lines, label centred |
| `nav.item` | ≤16 | 20 | 18 | |
| `tariff.name` | ≤12 | 16 | 14 | |
| `tariff.description` | ≤74 | 92 | 85 | |
| `tariff.feature` | ≤48 | 60 | 55 | |
| `badge.label` | ≤18 | 22 | 20 | `Our recommendation` = 18. Wraps to two lines in hy/ru — **never an ellipsis** |
| `rail.label` | ≤12 | 15 | 14 | |
| `rail.value` | ≤18 | 22 | 20 | |
| `caption` | ≤80 | 100 | 92 | |
| `placeholder.caption` | ≤64 | 80 | 74 | |
| `guarantee.title` | ≤30 | 38 | 34 | |
| `guarantee.body` | ≤110 | 138 | 126 | |
| `form.label` | ≤24 | 30 | 28 | |
| `form.helper` | ≤90 | 112 | 104 | |
| `form.error` | ≤90 | 112 | 104 | Split into two sentences rather than truncate |
| `report.status` | ≤24 | 30 | 28 | `Could not reach the plot` = 24 |
| `report.crewNote` | 120–320 | 150–400 | 138–368 | Wrap, no clamp |
| `report.recommendation.item` | ≤72 | 90 | 83 | |
| `credit.rule.bullet` | ≤120 | 150 | 138 | |
| `link.tertiary` | ≤46 | 58 | 53 | May wrap to three lines; declared |
| `role.name` | ≤18 | 22 | 20 | |
| `role.description` | ≤90 | 112 | 104 | |
| `faq.question` | ≤72 | 90 | 83 | |
| `faq.answer` | ≤420 | 520 | 480 | |
| `toast` | ≤48 | 60 | 55 | |
| `email.subject` | 30–52 | 38–65 | 35–60 | |
| `email.preheader` | ≤90 | 112 | 104 | |
| `push.title` | ≤40 | 50 | 46 | |
| `push.body` | ≤90 | 112 | 104 | |
| `meta.title` | ≤60 | 60 | 60 | Hard SERP limit, not a translation budget |
| `meta.description` | ≤155 | 155 | 155 | Same |
| `legal.paragraph` | ≤600 | 750 | 690 | |

---

## 4. Grid, spacing, radii, borders, shadow, motion

### 4.1 Breakpoints and grid

| Name | Min | Columns | Gutter | Margin | Notes |
|---|---|---|---|---|---|
| `base` | **360** | 4 | 16 | 20 | **QA floor.** Design frames may be drawn at 375, but 360 is the gate. |
| `sm` | 600 | 8 | 24 | 40 | Tariff cards go 2-up |
| `md` | 900 | 8 | 24 | 40 | Nav expands; drawer retires |
| `lg` | 1200 | 12 | 24 | auto, content max 1200 | The verification rail becomes a right column |
| `xl` | 1440 | 12 | 32 | auto | More air, no new layout |

Media queries are `min-width` only. Figma layout modes: **360 / 900 / 1440**.

**The signature split at `lg`+:** main column `cols 1–8` (622px at 1440), the
verification rail `cols 10–12` (222px), column 9 deliberately empty. Editorial
body sits in `cols 1–7`. Full-bleed bands break the margin; content inside them
returns to the grid.

### 4.2 Spacing

4px base: **4 · 8 · 12 · 16 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 128 · 160.**
Nothing off-scale; an optical exception requires a written note in the spec file.

| Where | 360 | 1440 |
|---|---|---|
| Section padding, light band | 72 / 72 | 128 / 128 |
| Section padding, Anthracite band | 80 / 80 | 144 / 144 |
| Card padding | 20 | 32 |
| Report sheet padding | 20 | 40 |
| Between blocks inside a section | 24 | 40 |
| Page bottom padding where the action bar can appear | 88 | — |

### 4.3 Radii

**`0 · 4 · 8 · full`. The unused steps are deleted from `tokens.json`** — an
unused token gets used.

| Token | Value | Applies to |
|---|---|---|
| `--mc-radius-0` | `0` | bands, photographs, the report sheet, dividers, the plot diagram, the verification rail, tables |
| `--mc-radius-sm` | `2px` | buttons, inputs, cards, tariff cards, badges, chips, toasts, menus |
| `--mc-radius-md` | `8px` | modals, drawers, bottom sheets, the lightbox frame — overlays only |
| `--mc-radius-full` | `9999px` | slider thumb, petal bullet, avatar disc |

2px was too austere at a 48px button on a phone; 10/14px is a consumer app.
There are no "friendly" 12/16px radii anywhere.

### 4.4 Borders

**One hairline weight: 1px.** Four values only —
`--mc-border-default` (Anthracite 12%, object edges on light),
`--mc-border-strong` (Anthracite 20%, input rest),
`--mc-border-on-dark` (Ivory 40%, object edges on dark),
Olive 100% (structural rules and the plot-diagram frame).

2px exists in exactly three places: the input error border, the Deep Olive
border on the leading tariff card, and the focus ring. There is no 3px, no 4px,
and no accent rail on a card edge. Olive is never used at an opacity.

### 4.5 Shadows

**One shadow token in the entire system.**

```
--mc-elevation-overlay: 0 16px 40px rgba(51,55,60,0.16);
```

Permitted on: modal, drawer, bottom sheet, lightbox, toast. Nowhere else. There
is no shadow on any card, tariff card, report sheet, input, badge, band, header
or button, and there is no hover lift. Elevation on the page is expressed as a
**change of ground plus a hairline**; shadow is the SaaS-template tell and this
brand's entire visual argument is paper on stone.

Consequences that must be specified rather than assumed:

- Overlays additionally take `--mc-surface-scrim` (Anthracite 60%). Without a
  scrim an Ivory modal on a Nude page is invisible.
- **Floating layers take the opposite light of the surface beneath them.**
  `--mc-surface-float` resolves to Ivory over a Nude ground and to Nude over an
  Ivory surface (via a `.mc-on-ivory` scope), plus a 1px `--mc-border-strong`
  outline. This is what stops a `Combobox` menu being Ivory on Ivory.
- A toast that must appear over an Anthracite band takes the inverse raised
  surface with a Nude label.
- The mobile action bar sits on solid Ivory with a 1px `--mc-border-default` top
  rule, and above it a 24px Nude→transparent gradient scrim so content does not
  appear sliced. **That gradient is the only gradient permitted anywhere.**

### 4.6 Motion

Motion confirms; it never entertains. Total budget on a marketing page: **six
behaviours.**

| Where | What | Duration / curve |
|---|---|---|
| Header | Bottom hairline is permanent; no scroll transition | — |
| Section entrance | opacity 0→1 with translateY 8→0, once, staggered 60ms, max 3 items per section | 320ms `cubic-bezier(.2,.7,.2,1)` |
| Buttons and links | Underline draws from the inline start | 160ms `ease-out` |
| Slider | Fill and thumb track the input | 120ms linear |
| Accordion | height + opacity | 240ms `cubic-bezier(.2,.7,.2,1)` |
| Report images | Fade in on decode, no skeleton shimmer | 200ms linear |
| Overlays | Scrim fade 160ms; sheet translateY 240ms same curve | |

**Forbidden, explicitly:** count-up or rolling numerals anywhere, the calculator
total included — the number snaps, the track fill follows the drag, and
`aria-live="polite"` announces on release; parallax of any kind; auto-advancing
carousels; hover-zoom or Ken Burns on a photograph of a plot; scroll-jacking or
pinned sequences; a rotating, spinning or "blooming" mark — the brand mark never
rotates, so the five-petal loading spinner proposed in round one is withdrawn
and loading is a 2px Deep Olive arc or a fading opacity pulse on the label;
falling petals; typewriter text; a before/after wipe, curtain or drag-slider;
any transition on the Family Circle avatars; and **any animation whatsoever on
the sample report photographs, on a status screen, or on a guest report view.**

`prefers-reduced-motion: reduce` removes every entrance animation and every
transform and reduces everything to opacity at ≤100ms. It is tested, not
assumed: a meaningful share of a 40–60 audience has it on.

---

## 5. Components — visual specification, every state

Radius `sm` = 2px unless stated. All targets ≥44×44 including invisible hit
area. Focus is always `2px Olive ring at 2px offset plus a 1px Ivory inner
ring`, so it reads on both light grounds; on Anthracite the ring is Nude.

### 5.1 Button

Heights 52 at `lg`+, 48 below. Padding 28 / 24 horizontal. Label `button`. Icons
16px, optical-aligned, gap 10. Full-width only inside a mobile card, the mobile
action bar, or a form. There is no ghost button, no icon-only primary, no button
taller than 52, and **no error/destructive button variant**.
Buttons must survive **two lines** with the label centred (Armenian at +25%).

| Variant | Rest | Hover | Focus-visible | Active | Loading | Disabled |
|---|---|---|---|---|---|---|
| **Primary, light** | Deep Olive fill, Ivory label (6.01) | fill → `#4A5033` (Deep Olive stepped down; 7.6 with Ivory); a 1px Ivory rule draws in under the label | standard ring | fill at 92% composited | label stays, 2px Deep Olive arc at the inline start, 900ms linear | avoid — validation is inline. Where unavoidable: Deep Olive 32%, Anthracite label, `aria-disabled`, cursor default |
| **Primary, dark band** | Nude fill, Anthracite label (9.61) | fill → Ivory; hover rule in Anthracite | Nude ring | 92% | Anthracite arc | as above, inverted |
| **Secondary, light** | transparent, **1px Deep Olive border, Deep Olive label** | border 2px Deep Olive, fill → Ivory | standard ring | fill Ivory, border stays | inline arc | 40% opacity |
| **Secondary, dark** | transparent, 1px `border-on-dark`, Ivory label | border → Ivory 100% | Nude ring | — | — | 40% |
| **Tertiary / text link** | Deep Olive on light, Ivory on dark; underline 1px at 0.14em offset, `text-decoration-skip-ink: auto` | underline 2px | ring around the text box | — | — | — |

A secondary button never takes an Anthracite outline — next to a Deep Olive fill
it reads as disabled. 1.5px does not exist in this system.

### 5.2 Input, and the whole form family

Height 56 at `lg`+, 52 below. Radius `sm`. 1px `--mc-border-strong`. Fill is
always the *other* light: Ivory on a Nude ground, Nude on an Ivory surface,
Ivory on Anthracite. Text `body`, Anthracite, 16px minimum.

- **Label above, always**, in `overline`, Anthracite. Placeholders are never
  labels; where one exists it is a format example (`+1 818 555 0134`) in
  `--mc-text-secondary`.
- Helper `caption`, `--mc-text-secondary`, 8px below.

| State | Treatment |
|---|---|
| Rest | 1px `border-strong` |
| Hover | border → Anthracite 30% |
| Focus | border → Deep Olive, plus the standard ring |
| Filled | border Anthracite 30% |
| **Error** | **2px inset `--mc-border-feedback-error`**, a 16px error glyph inline-start of the message, message in `--mc-text-feedback-error` at 14px below the field. Field height does not change. Required marker in the label is the same colour. |
| Read-only | Nude fill, no border, value in Anthracite |
| Disabled | 40% opacity, `aria-disabled` |

There is no success state and no green tick — a completed field is simply
filled.

**Textarea** min-height 120, same styling, no resize handle below `md`.
**Checkbox** 20×20, radius `sm`, 1px Anthracite border; checked = Deep Olive
fill with an Ivory tick; focus ring as standard; error = 2px error border.
**Radio** 20×20 circle; checked = 1px Deep Olive ring with an 8px Deep Olive
core.
**`CountrySelect`** — dial code plus ISO as **text** (`+374 AM`), never a flag
alone (no flags anywhere: a diaspora audience does not need to be told which
country it lives in). Searchable in three scripts. Default guessed by IP,
always visibly overridable, never re-guessed after an override. Sits inside the
phone field, separated by a 1px `border-strong` vertical.
**`Combobox`** (cemetery or city) — free text with suggestions; free entry is
always accepted. The menu is a floating layer (4.5).
**`NumberField`** — paired with every slider. 48 tall, 96 wide, stepper buttons
44×44, tabular figures. A slider alone is unusable for a 58-year-old and
unusable by keyboard.
**`FileUpload`** (guarantee re-visit) — up to 3 photos, 10 MB each, **HEIC
accepted**. States: idle / uploading (determinate 2px Deep Olive bar) / complete
(filename + remove) / too large / wrong type. The last two use the error
treatment.

### 5.3 Card

Ivory on Nude, 1px `border-default`, radius `sm`, padding 32 / 20, **no shadow,
no hover lift**. Structure top to bottom: `overline` → title → body → hairline →
footer row. Hover on a linked card: border → Olive, title underline draws. The
whole card is one stretched link; there is never a second interactive element
inside a card that is itself a link.

### 5.4 `PricingBand` and `TariffCard`

**Two bands. This is the settled structure and it amends the brief's phrase
"the three annual subscriptions" — there are two.**

```
Band A · One-off services       Inspection 20,000 ֏ AMD   ·   Express 65,000 ֏ AMD
        → credit rule, four bullets, stated once directly beneath this band
Band B · Annual subscriptions   Optimal 160,000 ֏ AMD / year   ·   Maximum 200,000 ֏ AMD / year
Special                          one ruled line beneath the calculator. No card, no price.
```

`PricingBand` — a labelled group: `overline` band heading, 1px Olive rule below
it, then the cards. `--one-off` and `--annual`. Layout **1-up below 600, 2-up
from 600. There is no 3-up grid and there is no fifth card.**

`TariffCard` — Ivory on Nude, 1px `border-default`, radius `sm`, padding 32 / 20.
Height is `auto`, equalised by `display:grid; align-items:stretch` on the band
with `min-height:0` on the card. **There is no fixed `min-height`** — a fixed
minimum either wastes 120px in English or overflows in Armenian.

Anatomy, top to bottom:
1. badge slot (leading card only);
2. product name in `overline`, Deep Olive, with the Armenian original in
   `caption` beneath on the Armenian site only;
3. price in `price`, Anthracite, tabular; `֏ AMD` or `֏ AMD / year` in `caption`
   on the following line, `--mc-text-secondary`;
4. 1px Olive rule;
5. the visit line in `h4` — "Four full visits, one each season";
6. feature list, each item led by a 6px Olive five-petal glyph 0.6em above the
   baseline, `body-sm`, 12px row gap, max 5 items;
7. one-off cards only: the credit line, `caption` — "Credited toward an annual
   subscription signed within 60 days";
8. 1px `border-default`;
9. CTA, full card width.

**Prices in Band A are set at the same type size as Band B.** Shrinking a price
is what makes a product read as cheap, and Express is a real product at 65,000,
not a lead-in.

**Marking the leading tariff.** Per `DECISIONS-2 §5` the label is
**`Our recommendation`**, never "Most chosen" — with zero customers, "most
chosen" is a behavioural claim we cannot support and it belongs to the same
class as "trusted by N families". The word "bestseller" exists nowhere, in any
language, in any file. Optimal is marked by three consistent signals:

- a **2px Deep Olive border** on the card (Maximum keeps the 1px hairline);
- a badge above the product name: **Deep Olive fill, Ivory label (6.01)**,
  `overline`, radius `sm`, height 24, padding 0 10;
- it is the **only** card in the band with a `primary` CTA; Maximum's CTA is
  `secondary`.

**An Olive fill carrying any label is forbidden system-wide** (3.08 / 3.42) and
is blocked in the linter. There is no inversion of the Optimal card: with two
cards in the band an inversion reads as a light/dark opposition rather than a
hierarchy, it collides with the two-Anthracite-band budget, and it would give
the leading product the only button on the page that is not a Deep Olive fill.

`Special` is a single ruled line beneath the calculator: 1px Olive rule, then one
sentence and a Deep Olive text link routing to Inspection. A priceless card in a
price comparison re-opens the exact fear the calculator exists to close.

### 5.5 `Badge` and `StatusBadge`

Height 24, radius `sm`, padding 0 10, `overline`.

| Variant | Treatment | Used for |
|---|---|---|
| `accent` | Deep Olive fill, Ivory label (6.01) | `Our recommendation`, `GPS confirmed` |
| `accent-soft` | transparent, 1px Deep Olive border, Deep Olive label | `One-off · not a subscription`, `Subscription active` |
| `neutral` | transparent, 1px `border-default`, Anthracite label | `Scheduled`, `Being prepared`, `Visit moved`, `Could not reach the plot`, `Repeat visit requested` |
| `inverse` | transparent, 1px `border-on-dark`, Ivory label | the same, on an Anthracite band |

Every status badge carries **its word and an 8px glyph**; outline weight alone is
invisible to this audience and colour is never the only carrier. There is no
error badge and no coloured status fill. Statuses: `completed · scheduled ·
preparing · rescheduled (Visit moved) · no-access (Could not reach the plot) ·
revisit-requested (Repeat visit requested)`.

### 5.6 `VerificationRail` — the signature device

`rail` type: **Cabin 500, 14 / 20, +0.06em, tabular, sentence case in Armenian.**
Labels in `--mc-text-secondary`, values in Anthracite. Radius 0. Never below
14px, in any medium, including PDF.

| Width | Form |
|---|---|
| `lg`+ | Right column, `cols 10–12` (222px), flush to the top of the content it annotates, label above value, 16px row gap, 1px `border-default` between rows |
| `base`–`md` | A horizontal ruled strip **beneath** its content: two rows of label/value pairs, 1px `border-default` between rows, labels at the inline start, values at the inline end |

Fields: `Date · Cemetery · Sector · Plot · Crew · Arrived · Left · Coordinates`.
**Every field has a defined empty form.** A missing value renders `Pending`, in
`--mc-text-secondary`, never a blank cell — if the platform cannot supply a
field the layout must not collapse. These fields are an API requirement and are
raised with the developer now, not at integration.

### 5.7 `GpsVerification`

Not a map screenshot and not a red pin: a map tile is someone else's brand, it
carries an attribution licence and a third-party request from a page full of
grave photographs, and a red pin is a delivery app.

- **Plot diagram** — a 1:1 frame, 120px at `md`+, 96px below, 1px Olive border,
  radius 0, Nude fill. Inside: three concentric 1px Olive circles at 20% (a
  bearing rose), a 1px Olive cross-hair at 30%, and at the true offset a solid
  **Olive five-petal glyph at 14px** — the plot itself.
- Beneath the frame, coordinates in `rail`: `40.1872° N, 44.5453° E`; then a
  `caption`: `Coordinates recorded on site · 14:22 · 12 September 2026`.
- To the side, `Badge--accent` reading `GPS confirmed`, and one `body-sm` line:
  "The device recorded its position at your plot, not at the gate."
- **`Show on map`** is a tertiary text link that opens the visitor's own map app
  by `geo:` / Apple Maps URL. **We serve no tiles, ever**, and there is no
  lightbox map crop.
- States: `recorded` · `pending` ("Coordinates pending upload" — never an empty
  cell) · `not-recorded`.
- It is never animated and never becomes a decorative pattern. Three uses on
  Home: the hero report preview, the method block, and nowhere else.

### 5.8 `ReportSheet` — the product

Ivory sheet, radius **0**, 1px `border-default`, max-width 720 at `lg`+,
full-bleed minus 20 at `base`, padding 40 / 20, no shadow. The ground change
does the work.

**Canonical block order — binding on every document, the portal, the guest view
and the PDF:**

| # | Block | Guest sees |
|---|---|---|
| 1 | **Masthead** — mono mark 20px, `Visit report` in `overline`, plot identity, cemetery; 1px Olive rule beneath, full sheet width | yes |
| 2 | **Confirmation** — `h3` "The visit took place", the date as the largest element, `Visit completed` badge, arrival and departure times, **and the `GpsVerification` block at the foot of the block — its own block, never a chip** | yes |
| 3 | **Work performed** — ticked list, petal bullets, max 8, first 4 plus "Show all" at `base` | yes |
| 4 | **Photographs** — group `On arrival`, then group `After the work` | yes |
| 5 | **Video** — one 20–40s clip, poster frame, muted, inline, never autoplay | yes |
| 6 | **The crew's note** — 120–320 characters, the one first-person voice in the product | yes |
| 7 | **Work we would recommend, with prices** — Owner and Family manager only, on a changed ground with a full-width rule above; **removed server-side for everyone else, not hidden** | **no** |
| 8 | **Documents** — report PDF | yes |
| 9 | **Actions** — Share · Order additional work · Request a repeat visit | text link only |
| 10 | **Next visit** — date | **no** |

The report opens on a calm confirmation, not on an image. **Photographs run
chronologically: `On arrival` first, then `After the work`,** each group headed
in `overline` with the timestamp in `rail` at the inline end and a 1px
`border-default` between label and image. Leading with the after-shot is the
advertising register the brief forbids; a report that opens on the clean stone
with no reference frame is a marketing image, not a record. **No drag-slider, no
wipe, no 50/50 curtain, no arrows between the frames, no "BEFORE"/"AFTER" burned
into the image.** Labels are typographic and sit outside the frame. An optional
2-up `ComparePair` may appear further down, headed `Compare`, never as the
opening image.

States: `complete` · `preparing` ("The visit is done. The report is being
prepared.") · `media-partial` ("Some photographs are still uploading. The rest
of the report is complete.") · `failed` (calm sentence, phone number, no red).

**Report PDF:** A4, the same block order, **never any price in any variant**, so
one file serves owner, member and guest. The tagline is set from the print
asset. `֏` obeys 3.5. Past reports stay readable forever, including after
cancellation — read-only, no new visits, no upsell on those screens.

**`ReportPreview`** — the cropped Ivory object in the marketing hero. A distinct
component, not the sheet: masthead strip, verification rail as a horizontal
strip, `GPS confirmed` badge, one 4:3 image slot, two thumbnails. Built in HTML,
so it is sharp, translatable and fast, and it is **never a photograph of a
phone**.

**`VisitListRow`** — a third component, not the sheet: 72px minimum, whole row
tappable, date, status badge, one-line summary, chevron.

**Link preview, hard rule.** The OG image is generated, never a photograph:
**Anthracite** ground (a Nude card renders near-blank in a dark WhatsApp
thread), mono light mark at 96px, `Visit report` in `h3` Ivory, the date in
`rail`. `og:title = "Visit report — {date}"`;
`og:description = "A record of a MemoryCare visit. Photographs, video and GPS
confirmation."` — **no cemetery, no plot label, no name.** The page `<title>` is
`Visit report — {date}` and nothing else: a plot identity in a browser tab is
visible over a shoulder and in any screen-share. `/r/:shareToken` carries
`X-Robots-Tag: noindex, nofollow` and a `noindex` meta; the token is ≥128 bits;
the link is revocable from the sheet that creates it and dies on cancellation.

### 5.9 `PlotCalculator`

An Ivory panel on the Nude ground, radius `sm`, 1px `border-default`. Two
columns at `lg`: controls `cols 1–7`, result panel `cols 9–12`, sticky at 96px
from the top. Stacked at `base`, with the result **immediately below the two
sliders — not pinned to the viewport.**

- Slider track 2px, Anthracite 20%; filled portion 2px Deep Olive; thumb 20px
  disc, Deep Olive, 2px Ivory inner ring; focus adds the standard ring. Track
  hit area 44px tall and invisible.
- Above each slider: label in `overline` at the inline start, current value in
  `h3` tabular at the inline end (`24 m²`, `3 monuments`).
- Beneath each slider, the paired `NumberField`.
- Tick marks at the thresholds (16 m², 2 monuments) as 1px Olive verticals with
  a `caption` label `included`.
- **Result panel** — Ivory with a 1px Olive rule at the top (not Anthracite: it
  must be able to carry the error-free arithmetic and it sits inside a light
  region). `overline` `Optimal, per year`; total in `price-xl`, Anthracite,
  tabular; then the breakdown, one row per line, `body-sm`, values at the inline
  end, 1px `border-default` between:
  `Base 160,000` / `+8 m² above 16 × 10,000 = 80,000` /
  `+1 monument above 2 × 30,000 = 30,000`.
- **Optimal and Maximum are shown simultaneously**, plus a separate Express
  one-off row. There is no tier toggle and no segmented selector: a control that
  hides one of the two values defeats the "one variable, two values" structure.
- Two annual surcharge lines are permanently visible beneath the sliders; the
  Express surcharge line lives inside the Express row where it applies. Nothing
  goes behind an info icon.
- **Numbers change instantly. No count-up, ever** — not on drag, not on
  `pointerup`. Tabular figures prevent the jitter a count-up was compensating
  for. `aria-live="polite"` announces on release.
- Past 100 m² or 10 monuments the panel replaces the total with a short message
  and a button routing to Inspection. **No error styling** — this is a normal
  outcome.
- Beneath: `One price list — the same in Yerevan and in Los Angeles.` and
  `The price is on the page before you speak to anyone. It does not change
  depending on where you are calling from.`
- URL state `?tier=&area=&monuments=`; the configuration is carried into the
  consultation form as hidden fields and **echoed back in the confirmation**.
- **The calculator exists on `/pricing/` only.** Two live calculators double the
  maintenance of the one component whose arithmetic can embarrass us and split
  the analytics on the highest-value interaction on the site.

### 5.10 The 95,000 ֏ first-year figure

Required publicly by `DECISIONS.md §3`, in the calculator and on the pricing
page. It is the credit **mechanic**, never a discount.

Placement, and nowhere else: (a) the credit block beneath Band A on `/pricing/`;
(b) the calculator, **Express mode only**, as the third result row, recomputed
with surcharges; (c) the portal, after a one-off is paid, as a dated fact; (d)
the written quote sent after the consultation call.

**Not** in the hero, not on the Optimal card, not on the Express card's price
line, not in a badge, not in a meta description, not in the sticky bar, not in
the footer.

Six rules, all enforceable in `qa/prices.spec.ts`:

1. Always show the subtraction, never only the result:
   `160,000 − 65,000 = 95,000 ֏ AMD`.
2. Always name the mechanism in the same sentence — an amount already paid comes
   off.
3. **Always state the second year in the same sentence** — "and 160,000 ֏ AMD in
   each year after that". This is what converts 95,000 from a price into a
   one-time consequence.
4. Forbidden words near a price: `save`, `saving`, `discount`, `off` alone,
   `deal`, `offer`, `special`, `only`, `just`, `instead of`, `was/now`, `%`.
   Build failure.
5. No discount grammar: no strike-through on 160,000 anywhere ever, no colour on
   the 95,000, no larger type, no badge, no ribbon. It is set in the same type
   role as the sentence containing it.
6. Full currency form every time: `95,000 ֏ AMD`.

Load-bearing elsewhere: 160,000 is the only price on the Optimal card; the
calculator's default state is subscription mode showing 160,000; no screen shows
95,000 and 160,000 as two options of equal weight; the Express headline price
stays 65,000; the portal plan card shows `160,000 ֏ AMD / year · renews
{date}` from day one; **and the pro-rata refund is computed on the amount
actually paid, never the list price** (`DECISIONS-2 §1`).

### 5.11 `GuaranteesBlock`, `HonestyPanel`, `TeamBlock`

**`GuaranteesBlock`** — one component, four surfaces (Home, Pricing, its own
page, the portal visit list). Three items, each: title (`h4`), a number, and the
remedy in `body-sm`. Each item is led by a 6px Olive petal glyph. The panel is
Ivory on Nude with a 1px `border-default`; the panel is **never Olive-tinted
with text on it**. Below the three items, the honest-limits paragraph and links
to the four legal pages. Guarantees are our entire substitute for testimonials,
so they take the slot testimonials would have had: **immediately after How it
works, before the closing CTA**, on both Home and Pricing.

**`HonestyPanel`** — "We started in 2026. We have no reviews yet." Bordered
panel on Nude, **body size or one step above, never small print**: styling it as
a disclaimer inverts its job. Sits directly beneath the guarantees.

**`TeamBlock`** — two founders, name, role, `tel:` link, `wa.me` link, a 1:1
portrait placeholder. A published founder's mobile number outweighs any number
of anonymous reviews and costs nothing.

### 5.12 `Modal`, `Drawer`, `BottomSheet`, `Lightbox`, `Toast`

All are Ivory (or `--mc-surface-float`), radius `md` 8px, 1px `border-strong`,
`--mc-elevation-overlay`, over `--mc-surface-scrim`. The bottom sheet keeps a
36×4 drag handle. Focus is trapped; `Esc` closes; the trigger is restored on
close.

**`Lightbox`** — full-screen photograph, scrim, controls on a Nude chip so they
never sit directly on the image, pinch-zoom, counter in `rail`. No animation on
report photographs.

**`Toast`** — two variants only, `neutral` and `error`; there is no success
toast. Ivory, 1px `border-default`, radius `sm`, 4s, dismissible, `aria-live`.
Copy contract: "Link copied." A failed payment is never a toast.

### 5.13 Navigation components

**`LanguageSwitcher`** — three text items in **native script: `ՀԱՅ · ENG ·
РУС`**, separated by 1px Olive verticals; the current item Anthracite,
the others `--mc-text-secondary` (4.98 / 5.46). Not a dropdown, not a globe, no
flags. At `base`–`sm` it lives pinned at the bottom of the drawer, not in the
bar.

**`SegmentedControl`** — `aria-pressed`, 44×36 minimum with a 44×44 hit area,
1px `border-default`, selected segment = Ivory fill with a 2px Deep Olive
bottom rule.

**`StickyCtaBar`** (marketing, `base`–`md` only) — **64px + `env(safe-area-inset-bottom)`**,
Ivory, 1px `border-default` top rule, the 24px gradient scrim above it. A 44×44
call target plus one full-remaining-width primary button. Appears at
`scrollY > 320`. **Suppressed** on `/consultation/`, on the four legal pages, on
every report and guest route, **while any form field has focus**, and on
`/pricing/` while the calculator result is in the viewport — the calculator has
its own contextual CTA. **One fixed bar at the block-end, ever:** two would take
168px of a 640px viewport.

**`ReportShareBar`** — the report screen's own 48px sticky bar, **Share only**.

**`PortalTabBar`** — 56 + safe-area below `md`, four tabs: Plots · Visits ·
Family · Account. At `md`+ it becomes a 240px sidebar and the content column
scrolls.

**`Accordion`** — 240ms height+opacity, chevron rotates 180°, first item open on
FAQ, `aria-expanded`. Used by FAQ, legal ToC, "What each role can do".

**`Tooltip`** — tightly restricted to definitions only (GPS point, AMD, full
visit, pro rata). It may **never** carry a rule, a price or a surcharge.
Tap-to-open on touch, dismissible, never hover-only.

### 5.14 Feedback and empty components

**`ErrorPanel`** — three slots: what happened, whose fault it is, what to do,
plus an optional fourth line with the phone number. **The component has no
`icon` and no `illustration` prop at all**, so neither can be reached for under
deadline. Field-level errors keep the 16px glyph — colour is never the only
carrier, and roughly 8% of a male 40–60 audience is colour-deficient. Never, in
any language: `Oops`, `Something went wrong`, `Error`, `Invalid`, `Failed`,
`Required field`, any emoji, any exclamation mark.

**`EmptyState`** — heading, body, one action. **No illustration slot.**

**`ErrorPage` (404 / 500)** — calm heading, five real links, a phone number. No
joke, no illustration, no red.

**`ProgressRail`** — 4 dots, horizontal, labelled; `done` (Deep Olive fill) ·
`in-progress` (2px Deep Olive ring) · `pending` (1px `border-default`);
`aria-current="step"`; label ≤20 characters, wraps to two lines at 360.

**`RefundTable`** / **`DataTable`** — zebra rows (Nude on Ivory), 1px
`border-default` rules, tabular figures, radius 0. Column heads in `overline`.

**`PermissionMatrix`** — **the single permitted horizontally scrolling table**,
capability column frozen, a scroll-fade affordance, and a screen-reader
definition-list equivalent. It exists at `md`+ only. **At `base`–`sm` the public
Family Circle page shows four stacked role cards, each with a "can / cannot"
list** — a frozen-column scroll table at 360 is unusable for a 55-year-old.
"Can" is a filled 6px Olive square, "cannot" an empty 6px 1px-bordered square,
**plus a text column**, so meaning never depends on the glyph alone.

**`AvatarRow`** — 48px Nude discs, initials in Cabin 600 at 16 Anthracite
(9.61), 1px Ivory-40 ring, −12px overlap, the owner's disc carrying a 1px Olive
outer ring at 3px offset. **No photographs of people, no stock avatars.**

**`ShareSheet`** — one line explaining exactly what the recipient will see (the
owner needs to know she is not sending prices to her aunt), the link in a
read-only field with `Copy`, then WhatsApp, Viber, Email, a divider, and
**`Link is active · Revoke`** with the creation date and a confirm. Revocation
lives in the sheet that creates the link, never buried in settings.

**`RoleSelector`** — three radio **cards**, each with a one-line description,
never a dropdown: a dropdown hides the consequence of the choice. Plot-scope
checkboxes appear when there is more than one plot.

**`Stepper`** — "Step n of 4", back and next, and the escape at equal weight.

### 5.15 Brand furniture

**`BulletPetal`** — the five-petal glyph, 6px, Olive, 0.6em above the baseline.
**`Divider--medallion`** — the woven-medallion band, Olive, at most four times
per page. **`PullQuote`** — one per page maximum, display face.

**Three pieces of artwork are owed and do not exist yet:** the medallion divider
band, the petal bullet/loading glyph, and the 16px simplified mark (five petals
at the master's angles, a solid Olive centre disc, no hands, no weave). All are
derivable from the master; the designer draws or ratifies them. **Until they
land, the divider is a 1px Olive rule and the loading affordance is a 2px Deep
Olive arc.** Nothing ships blocked on them.

---

## 6. The header lock-up

The designer supplied nine SVGs, all `viewBox="0 0 1080 1080"`, all with large
asymmetric padding, and **no horizontal lock-up**. We construct one from her own
artwork at her own proportions, and swap the file when hers arrives.

### 6.1 Measured source geometry

| Asset | Content bbox (x, y, w, h) | Aspect |
|---|---|---|
| Mark | `112.7, 170.2, 854.7, 739.7` | 1.156 : 1 |
| Vertical lock-up | `112.9, 55.2, 854.7, 965.4` | 0.885 : 1 |
| Wordmark (word + tagline) | `130.5, 446.0, 819.0, 188.1` | 4.354 : 1 |
| Word line only | `168.0, 446.0, 744.0, 118.6` | 6.273 : 1 |
| Tagline only | `130.5, 604.1, 819.0, 30.0` | 27.3 : 1 |

Two facts make the construction legitimate rather than a crop: the wordmark file
is **97% empty space**, and the vertical lock-up reuses the mark and the wordmark
**at 1:1 scale with a 37.6-unit gap** — the designer's own relationship, turned
90°.

### 6.2 The constructed compact lock-up — `lockup-horizontal-mono.svg`

Mark at the inline start, word line only, no tagline (a 30-unit tagline is
illegible at header size).

- Word line unscaled: `744 × 118.6`.
- Mark height = **2.2 × word-line height = 260.9**; mark width
  = `260.9 × 1.1556 = 301.5`. This ratio makes the mark read as an icon beside
  the word rather than as a second focal point; the vertical lock-up's own 6.24×
  ratio is unusable horizontally.
- Gap = **0.55 × word-line height = 65.2** (the vertical lock-up's 37.6 against a
  739-tall mark is 0.32 of the wordmark block; 0.55 of the word-line height keeps
  the same optical looseness turned 90°).
- Canvas `301.5 + 65.2 + 744 = 1110.7 ≈ 1111` wide × `260.9 ≈ 261` tall.
  **`viewBox="0 0 1111 261"`, aspect 4.26 : 1.**
- The word is centred on the mark's vertical centre: `y = (260.9 − 118.6) / 2 =
  71.15`.

A tagline variant, `lockup-horizontal-tagline-mono.svg`, uses the full wordmark
block (`819 × 188.1`): mark height `1.55 × 188.1 = 291.6`, mark width `336.9`,
gap `60`, canvas `1216 × 292`, **aspect 4.16 : 1**, block centred at `y = 51.75`.
It is for the footer, letterhead, the invoice and print — never the header.

Production preparation is scripted in `brand/logo/prepare.mjs` so it is
reproducible when the designer sends corrected files: replace the square viewBox
with the measured bbox, drop `width`/`height` and add `preserveAspectRatio`,
replace `class="cls-N"` with `fill` attributes and `currentColor` in the mono
versions, add `role="img"` and a `<title>`, SVGO at `--precision=2 --multipass`,
then a pixel-diff gate at 512px. The nine originals are never edited and never
referenced by a layout.

### 6.3 How the header uses it

The header is an **Ivory bar** — it is a sheet, which is what the Nude/Ivory
rule says an object on the ground must be — with a **permanent 1px
`--mc-border-default` bottom rule at all widths**. The rule does not fade in on
scroll: a 1.1 tonal step without a rule reads as a printing error. No
`backdrop-filter` (three scripts, old Android, and it buys nothing over a solid
bar). Height **56 at `base`–`sm`, 72 at `md`+.**

| Width | Composition | Rendered size |
|---|---|---|
| ≥768 | `lockup-horizontal-mono.svg`, mono-dark (Anthracite via `currentColor`) | 36px tall, ≈153px wide |
| 480–767 | the same asset | 32px tall, ≈136px wide |
| <480 | `mark-mono.svg` + **live text** `MemoryCare` | mark 28px; word in the display face at **24px** |

Below 480 the drawn word is replaced by live text because it is selectable,
translatable, sharp at any DPR and needs no new asset. The live word is set at
**24px minimum — the Gloock optical floor** — with `Memory` in
`--mc-text-primary` and `Care` in **`--mc-text-accent` (Deep Olive)**. Never
Olive: at 24px Olive is 3.42 and unreadable. The floor applies to *live type
only*; the drawn wordmark inside the lock-up SVG is artwork and may render
smaller.

**Behaviour when space runs out — the degradation ladder, in order:**

1. Drop the tagline. It never appears in the header at any width, ever.
2. Drop the drawn word line; render the mark plus live `MemoryCare` at 24px.
3. Below 360, **drop the mark and keep the word.** The wordmark survives, not
   the mark: a visitor who arrived from an English search that returns dementia
   care must always be able to read the company's name. `MC`, `MEMORYCARE` and
   `Memory Care` are forbidden in every language and fail the build.

The mark inherits `color`, so one file serves both contexts: Anthracite in the
header, Nude in the Anthracite footer, where both halves of the word are Nude.

**Clear space** = `0.42 × total lock-up height` on all four sides, encoded as
`--mc-logo-clearspace: 0.42em` on the logo wrapper so nobody has to measure.

**Minimum sizes:** vertical lock-up 64px wide; horizontal compact 120px wide
(mark lands at 28px); horizontal with tagline 240px wide; mark at full detail
**24px** — at 16px the woven medallion collapses to a blur, which is why the
simplified mark exists for the favicon and the WhatsApp avatar.

**Forbidden uses**, each of which has already happened somewhere in this
project's history: the colour mark on a Nude ground (the Ivory hands vanish —
the colour mark goes on Anthracite or pure white only); any recolouring outside
the six values; rotation of the mark; outline or drop shadow; the mark inside a
circle or badge; **the mark used as the hero image** (the current site's
mistake); stretching to a non-native aspect; the tagline set with a full stop;
the tagline below 13px; `Memory Care`, `MEMORYCARE` or `MC`; and the 1080²
source files referenced directly in any layout.

**Header contents.** At `md`+: lock-up · five nav items (`Pricing · How it works
· Sample report · Family Circle · About`), the active item carrying a 1px Deep
Olive underline at 6px offset · `LanguageSwitcher` · `Sign in` (text link) ·
`Request a consultation` (primary). At `base`–`sm`: lock-up · 44×44 tap-to-call
· 44×44 menu; **no CTA button in the header** — it lives in the
`StickyCtaBar`, and the language switcher lives at the bottom of the drawer.
Removing the desktop button would cost requests from the local buyer on a laptop
in an open-plan office who will not phone from his desk.

---

## 7. Photography and placeholder art direction

### 7.1 Ratios — fixed, no exceptions

| Use | Ratio | Export |
|---|---|---|
| Report photograph, full width | **4:3** | 1600 × 1200 |
| Section illustrative image | 3:2 | 1800 × 1200 |
| Crew / equipment portrait | 1:1 | 1000 × 1000 |
| Video, report | 16:9 | 1920 × 1080 |
| Hero background, if ever used | 16:9 | 2400 × 1350 |
| OG / link preview | 1.91:1 | 1200 × 630 |

4:3 for the plot: a plot needs vertical extent and the phone is held in
portrait. 1:1 is correct for a crew portrait and **wrong for a plot**. The
separate 4:5 comparison crop is deleted — a comparison is two 4:3 frames, either
stacked or 2-up. This is the September shoot brief, and a re-shoot is not
available.

### 7.2 Treatment

- Radius 0. No border. **No black border under any circumstance.** No shadow, no
  vignette, no duotone, no olive wash, no grain, no film emulation, no HDR, no
  black-and-white conversion.
- Natural exposure, neutral white balance, mild contrast. Overcast or open shade
  preferred; hard midday sun makes stone look like a monument catalogue.
- Framing: the plot occupies the lower two-thirds, sky or path above. Camera at
  standing eye height, level. **Never a low heroic angle, never a drone shot
  directly over a grave** — drone footage is for context and access routes only.
- **The before and after frame must be identical** — same standing position,
  same focal length, same height. This is the whole evidentiary point, and the
  crew gets a marked standing position, a fixed tripod height and a fixed focal
  length for it.
- **The client's own monument inscription is legible by default** — it is the
  proof that we cleaned *their* grave. **Every neighbouring plot's name and
  inscription is out of frame or out of focus, without exception.** Whether the
  deceased's name is *displayed in the report* is a separate consent setting,
  **off by default** (`DECISIONS-2 §4`): a report shows cemetery, sector and
  plot; the name appears only if the client switches it on, the setting lives on
  the plot, is worded plainly, is reversible, and turning it off removes the name
  from previously issued links.
- Crew appear working, hands and equipment in frame; never posed, never smiling
  to camera, never a "team photo". **Faces of mourners never appear.**
- No flowers arranged for the photograph, no candles, no crosses composed as
  graphic elements.

The September shoot needs an operational artefact before it happens: a written
shot list per plot, the marked standing position, the tripod height and focal
length, and a file-naming convention matching the placeholder names.

### 7.3 Placeholders, until the September shoot

A placeholder is a **Nude rectangle at the exact final ratio**, 1px Olive
border, radius 0, containing:

- one Olive five-petal glyph at 8% opacity, 240px, bleeding off the bottom-right
  corner, unrotated — never a repeating pattern;
- at the lower left, in `caption` (`--mc-text-secondary`), four facts on two
  lines:

```
PLACEHOLDER · 4:3 · 1600×1200
"Condition on arrival — Tokhmakh, section 12" · September shoot
```

**Every placeholder names its ratio, its pixel size, its subject and its source.
A placeholder that does not name all four is not shippable.** No "image coming
soon", no camera icon, no grey box, no `lorem`, no stock photograph.

File names: `photo-4x3-plot-arrival.svg`, `photo-4x3-plot-after.svg`,
`photo-3x2-section.svg`, `portrait-1x1-crew.svg`, `video-16x9-report.svg`. When
the real photography lands it replaces these at identical names and identical
ratios — a `1.x` release with no component changes.

---

## 8. Content and claim rules that bind the visual work

- **Invent nothing.** No testimonials, no review counts, no "trusted by N
  families", no years in business, no client numbers. Zero paying customers. Use
  process trust: verified visits, GPS-tagged reports, named guarantees,
  described equipment and method.
- **No QR code and no digital memory page**, anywhere, in any language, not even
  as "coming soon". Year-2 scope; it does not exist.
- **No competitor is named on the site**, in any language, including in an FAQ
  answer. We describe the combination we offer — photo, video, GPS, portal,
  family circle — and never what anyone else lacks. Never claim that nobody does
  grave care with photo reports in Yerevan; that is false and checkable.
- In English, "memory care" is owned by the dementia-care industry. The hero
  eyebrow, the `<title>` and the meta description must disambiguate. Meta title,
  Home: `MemoryCare — grave care in Yerevan cemeteries` (45).
- Every visit is a **full visit**. Never "light", "preventive", "heavy",
  "standard" or "monthly". Never "bestseller", "most popular", "tier 1",
  "basic", "premium".
- Prices are always `160,000 ֏ AMD` — symbol **and** letters. Never `160k`,
  never `AMD 160,000`, never a bare symbol. Any FX figure is labelled
  approximate and never appears in a total.
- **Public service promises, identical in all six places they occur:** callback
  **within one business day**, business hours Yerevan time stated next to the
  promise so a client in Los Angeles can convert it; report **within 48 hours of
  the visit**. Nobody may soften or sharpen them locally.
- Product names in English: English first, Armenian in parentheses on first
  mention on the page — Inspection (Զննում), Express (Էքսպրես խնամք), Optimal
  (Օպտիմալ խնամք), Maximum (Մաքսիմում խնամք), Special (Հատուկ խնամք) —
  thereafter English only.
- **`MemoryCare LLC`**, one word, everywhere: footer, offer, invoices, receipts,
  legal pages, bank package, meta. `Memory Care`, `Memory-Care`, `MEMORYCARE`
  and `MC` fail the build.
- Primary CTA string, every instance including tariff cards and the sticky bar:
  **`Request a consultation`** (22). The form heading is `Request a free
  consultation` (27) — a heading, so the button budget does not apply. The
  support line under every instance: `No payment now. No account needed.` (34).
- No renewal, price, payment or upgrade string may be addressed to a **local
  contact** or a **family member**.
- **No auto-charge on renewal.** A renewal offer goes out 30 days before the
  client's own anniversary and the client acts. **A subscription year is 12
  months from the signing date**; seasons are a promise inside those twelve
  months, worded as "one visit in each season"; if no suitable winter weather
  window occurred, the visit is **added** to spring and four visits are
  guaranteed regardless.
- **No third-party analytics at launch**, therefore **no cookie consent
  banner** — nothing competes with the primary CTA for the bottom of a 640px
  screen. Server-side request counts only.

---

## 9. Page-by-page layout

Notation: **[F]** fixed, **[S]** scrolls. Fold budget at 360×640 is
`640 − 56 header ≈ 584px` of usable first paint after browser chrome; the
working figure used below is **500px**.

### 9.1 The fold arithmetic that fixes the H1 at 48 characters

| Element at 360 | Height |
|---|---|
| Overline 13/18 | 18 |
| gap | 12 |
| **H1, `display` 32/38, hard maximum 2 lines** | 76 |
| gap | 16 |
| Standfirst 16/26, 3 lines | 78 |
| gap | 16 |
| Verification strip, `rail` | 24 |
| gap | 16 |
| Primary CTA, 48 | 48 |
| gap | 16 |
| `ReportPreview`, deliberately cropped by the fold | 180 |
| **Total** | **500** |

A third H1 line costs 38px and pushes the report preview out of sight entirely.
**H1 hard maximum: 48 characters English, 58 hy, 55 ru.** One number,
everywhere. Canonical H1: `You will see exactly what was done, and when.` (44).
Standfirst: `Scheduled care for a family plot in Yerevan. Photographs, video and
a GPS point after every visit.` (98).

The `ReportPreview` is cropped on purpose so it invites the scroll, and **the
part that survives the crop is the metadata, not the image**: the masthead
strip, the verification rail (`Date · Cemetery · Plot`) and the `GPS confirmed`
badge. Proof is the coordinate and the date; a cropped photograph proves
nothing. Order at `base`–`sm` is eyebrow → H1 → standfirst → verification strip
→ CTA → report preview; the CTA is never below the card on a phone. At `lg` the
card moves alongside, `cols 8–12`.

### 9.2 Home — `/en/`

| # | Block | Ground | 360 | 1440 |
|---|---|---|---|---|
| — | Header **[F]** | Ivory bar | 56, lock-up · call · menu | 72, lock-up · 5 nav · lang · Sign in · CTA |
| 1 | **Hero / proof** | Nude | stacked per 9.1 | H1 `cols 1–7`, `ReportPreview` `cols 8–12`, verification rail inside the preview |
| 2 | **What this is** | Nude | one block: outcome first, then both reasons in one line of body text, neither ranked | `cols 1–8`, `h2` + `body-lg` |
| 3 | **Sample report** | Nude, Ivory sheet | the real `ReportSheet` at reduced height, edge-to-edge minus 20, then a text link | sheet `cols 1–8` max 720, rail `cols 10–12`, three annotations |
| 4 | **How it works** | Nude | `StepStrip`, 3 numbered steps stacked, 40px Olive line-icon each | 3-up, medallion divider above |
| 5 | **Guarantees + honesty** | Nude | `GuaranteesBlock` stacked, `HonestyPanel` directly beneath | 3-up, panel full width beneath |
| 6 | **Family Circle** | **Anthracite (band 1 of 2)** | `AvatarRow`, definition, 3 bullets, secondary button | `cols 1–6` text, `cols 7–12` avatars + role summary |
| 7 | **Pricing preview** | Nude | **four named products as four lines** with prices, then `See all products and the calculator →` | the same four lines, two columns |
| 8 | **Method and verification** | Nude | 2×2 grid of equipment/chemistry, then `GpsVerification` at 96px | 4-up, diagram at 120px `cols 9–12` |
| 9 | **Founders** | Nude | `TeamBlock`, two rows, `tel:` and `wa.me` at 44px each | 2-up with 1:1 portraits |
| 10 | **FAQ** | Nude | `Accordion`, 6 items, first open | `cols 1–8` |
| 11 | **Closing CTA** | **Anthracite (band 2 of 2)** | `h2` Ivory, support line, Nude-fill button, `tel:` link. **No form.** | centred `cols 3–10` |
| — | Footer **[S]** | Anthracite, continuous with 11, separated by a 1px Olive rule | stacked: lock-up → tagline in **Nude** small caps, no full stop → two names with phones as 44px rows → email → legal-address placeholder, visibly marked → four legal links → language switcher → `MemoryCare LLC, Yerevan, Armenia · © 2026` | four columns: Company · Services · Legal · Contact |
| — | `StickyCtaBar` **[F]** | Ivory | 64 + safe area, from `scrollY > 320` | not present |

Home carries the products as **four lines, not four cards**: duplicating the
card component would force us to duplicate the one-off/annual band split as
well, doubling the maintenance surface on the page that most needs to stay
short, and the local buyer reads four lines faster than four cards. Home carries
**no calculator**.

### 9.3 Pricing — `/en/pricing/`

1. **Page header** — `h1`, one line of standfirst, the coverage rule (up to
   16 m², up to 2 monuments), and `One price list — the same in Yerevan and in
   Los Angeles.`
2. **`PricingFork`** — two doors, stacked at `base`, 2-up from 600:
   `I want to know what it needs` → Inspection, and `I want it looked after` →
   the annual band. Heading `Two ways to start`. A fork beats a five-way
   comparison; the doors are never written in the reader's own voice about their
   own absence.
3. **Band A — One-off services.** `PricingBand--one-off`: Inspection 20,000,
   Express 65,000. 1-up at `base`, 2-up from 600. Each card carries the eyebrow
   `One-off · not a subscription` and the one-line credit note.
4. **The credit block** — `h3` `How a one-off payment is credited`, four bullets,
   always visible, never a tooltip, never a footnote, plus the worked
   arithmetic per 5.10 including "and 160,000 ֏ AMD in each year after that".
5. **Band B — Annual subscriptions.** `PricingBand--annual`: Optimal (2px Deep
   Olive border, `Our recommendation` badge, primary CTA) and Maximum
   (hairline, secondary CTA). 1-up at `base` with **Optimal first** — on mobile
   "centre" does not exist — 2-up from 600.
6. **`PlotCalculator`** — full width, per 5.9. The `StickyCtaBar` is suppressed
   while the result panel is in the viewport.
7. **Special** — one ruled line beneath the calculator with a Deep Olive text
   link, `Start with an Inspection`.
8. **`GuaranteesBlock` + `HonestyPanel`.**
9. **`PaymentRealityBlock`** — bank transfer available now, card payment when
   the bank enables it, **no date promised**.
10. **Pricing FAQ**, 5 items.
11. **Closing CTA band (Anthracite)** → footer.

### 9.4 How it works — `/en/how-it-works/`

Header → a 4-step vertical timeline at `base` with a 2px Olive rail down the
inline start at 20px, alternating sides at `lg` (Consultation → Subscription and
schedule → The visit → The report; number in Gloock, heading, 2–3 sentences, one
4:3 placeholder each) → **What a full visit includes**, 6–8 checked items, two
columns from `md` → **What we do not do**, at the same visual weight, 4 items,
linking to `/legal/limitations/` → **Weather and access**, the honest paragraph:
seasons, rain, locked sections, and that no visit is ever silently skipped →
report preview strip → closing CTA band → footer.

### 9.5 Sample report — `/en/sample-report/`

This page renders the **actual `ReportSheet`** with placeholder media inside the
marketing chrome. It must never be a picture of a report.

Short header → the component, full width minus 20 at `base`, max 720 centred at
`lg` with the verification rail in `cols 10–12` → **annotation layer**: callouts
to either side at `lg` explaining GPS verification, timestamping, video and
condition notes; at `base` the annotations become a numbered list **below** the
document, never overlaying it → **"How the link looks when you send it to
family"**: a rendered WhatsApp-style preview card demonstrating the OG rule —
mark, `Visit report`, date, no photograph → closing CTA band → footer.

### 9.6 Family Circle — `/en/family-circle/`

Header and a one-sentence definition → **How it works**, 3 steps → **the roles**:
four stacked role cards at `base`–`sm` with a can/cannot list each, the full
`PermissionMatrix` from `md` → **the Yerevan relative case**: the person who
meets the crew does not need an account → privacy note: who can see what, how to
remove someone, that removal is immediate → closing CTA → footer. One Anthracite
band on this page, on the roles section.

### 9.7 Guarantees — `/en/guarantees/`

`GuaranteesBlock` in full text, the honest-limits paragraph, `HonestyPanel`, and
links to the four legal pages. No dark band except the closing CTA.

### 9.8 About — `/en/about/`

Bank requirement and diaspora due diligence. What MemoryCare is (two paragraphs,
`body-lg`) → why it exists → the two founders with name, role, direct phone and
a 1:1 portrait slot → how we work: method, verification, equipment → the legal
entity block: `MemoryCare LLC`, registration-number placeholder, legal-address
placeholder, `info@memorycare.am`, both phones → the honest "we started in 2026"
line → closing CTA → footer. **No History, Mission, Values or News pages** —
those are the failure named in the brief.

### 9.9 Contacts — `/en/contacts/`

Two name cards with `tel:`, `wa.me` and role → email → **working hours in
Yerevan time with the UTC offset spelled out** → a short form (name, contact,
message) on Nude → the legal entity block → a map slot marked as a placeholder
pending the legal address.

### 9.10 Consultation — `/en/consultation/` and the modal

The same component in two containers; the modal is an Ivory sheet over the
scrim. **Never on an Anthracite band** (2.3, 2.6).

Fields, final: **Name** (required) · **Phone or email**, one field with
`CountrySelect`, international formats accepted (required) · **Cemetery or
city**, `Combobox` with free entry (required) · one disclosure link,
`Add a note or a family contact`, holding the optional textarea whose prompt
text is *"For example: the best hours to call you, or who else in the family we
should speak to"* · **consent checkbox**, required, one line with a link:
*"I agree to MemoryCare contacting me about this request."*

Preferred-contact-time chips are cut — we guess wrong more often than right and
we ask in the first ten seconds of the call. The Yerevan local-contact fields are
cut from the form and captured on the onboarding call; the **data model** still
carries three separate contact records per plot.

The consent checkbox stays (`DECISIONS-2 §5`): part of the audience is resident
in the EU, and the bank requires a demonstrable lawful basis. It is one line, not
a wall of text, and it is the only checkbox on the site.

At `base` the form is above the fold down to and including the first field. At
`lg` a right rail carries the three guarantees, `No payment now. No account
needed.` and both phone numbers. The confirmation states what happens, when,
in the visitor's own timezone, with the WhatsApp fallback and both numbers, and
echoes back the calculator configuration if one was carried in. Hidden fields:
`tier`, `area`, `monuments`.

### 9.11 Payment — `/en/pay/`

Two paths presented as equals, not as a primary and a broken one: **Bank
transfer (available now)** and **Card payment (opening soon — no date
promised)**. Transfer path: choose product → confirm plot parameters → generate
invoice → wire instructions on screen and as a PDF → "tell us when you have sent
it". `BankTransferPanel` and the invoice template carry `MemoryCare LLC`, the
legal-address placeholder, the AMD amount and the payment reference. A disabled
card button with no explanation reads as a broken site; labelling it honestly
reads as a young company, which is what we are.

### 9.12 Legal pages ×4

One template: `h1` → last-updated date → table of contents (a right column at
`lg`, an accordion at `base`) → body at 65–75 characters per line, `body-lg`,
line height 1.7 → contact block. Read by a bank officer and by a worried
55-year-old; both need it legible. Privacy · Refund (the pro-rata rule and its
worked example) · Terms · Service limitations.

---

## 10. Portal screens

Portal chrome: header **[F]** 56 with the mark, `PlotSwitcher` (only when more
than one plot) and an avatar menu; `PortalTabBar` **[F]** 56 + safe area below
`md`, becoming a 240px sidebar at `md`+. **No Anthracite band anywhere in the
portal.** No `StickyCtaBar`, no upsell on any screen showing a photograph.

### 10.1 First entry after payment — `/portal/`, zero visits

The most important screen in the product: the client has paid and there is
nothing to show. **It must not look empty; it must look scheduled.**

At 360, in order: (1) greeting, `h3`; (2) **status card**, Ivory on Nude, full
width — plot identity, `Subscription active` badge, **"First visit: 12–16
September"** as the largest text in the card, and one line naming who will come
and that the crew records GPS on arrival; (3) **`ProgressRail`** — four labelled
dots: Subscription active ✓ · Plot located · First visit · Report; (4) **what
happens next**, three rows with times, using the two public promises verbatim;
(5) two actions — `Add a family member` (primary, the action with the highest
retention value) and `See a sample report` (secondary); (6) support row with
Hayk's number, call and WhatsApp targets.

**Items 1, 2 and the top of 3 must be above the fold at 360.** If the client has
to scroll to learn when the first visit is, this screen has failed. At `md`+ the
status card takes `cols 1–8` and the progress rail runs beside it.

### 10.2 Dashboard — `/portal/`

Greeting → one `PlotCard` per plot (identity, cemetery, next visit, last-report
thumbnail on a **neutral crop**, plan name, whole card one stretched link, 88px
minimum) → `Add another plot` outline row → a notification strip when something
needs attention.

### 10.3 Visit list — `/portal/plots/:plotId/visits/`

Scheduled visits in a **separate group at the top** (Ivory rows, dashed Olive
inline-start rule) above completed visits (solid rows, Deep Olive rule). Each
`VisitListRow`: 72px, whole row tappable, date, status badge, one-line summary,
chevron. Filter chips at `md`+ only — at 360, filtering a list of at most nine
items a year is a needless control. `GuaranteesBlock` sits permanently at the
foot of this screen.

### 10.4 Report — `/portal/visits/:visitId/`

The `ReportSheet` of 5.8, full width minus 20 at `base`, max 720 centred at
`lg` with the verification rail in `cols 10–12`. `ReportShareBar` **[F]** 48px
at the block end, **Share only**. Photographs open in the `Lightbox` with
pinch-zoom.

### 10.5 Guest report — `/r/:shareToken/`

A short root path, deliberately: it is pasted into WhatsApp and read on a
five-inch screen by a 70-year-old aunt, and `memorycare.am/r/8fk2wq` is a link a
person can retype. Blocks 7-prices, 9-commercial and 10 are **removed
server-side, not hidden with CSS**. No plan name, no price, no renewal, no
sticky bar, no navigation into the marketing site, **no button of any kind**.

The foot of the page is one line saying what MemoryCare is, `{owner_first_name}
shared it with you`, and a `tel:` link. **The single permitted interactive
element is one tertiary text link:** `Something is not right with this report` →
three fields (name, phone, message) filing a guarantee re-visit and notifying
the owner. Support, never sales — a dead page forces the aunt in Yerevan to
phone her son abroad. The route bundle physically cannot import `TariffCard`,
`PlotCalculator`, `Badge--accent` or any `primary` button; `tertiary` is added
to its allowed set.

Expired or revoked: `This link is no longer active.` — the person who sent it
can share it again, nothing has been deleted, no sign-up prompt, no price.

### 10.6 Family Circle — `/portal/family/`

Roster rows: initials disc, name, role badge, `invited` vs `active`, plot scope.
The owner row is pinned first and cannot be removed. `Invite a family member`
primary. A collapsed `What each role can do` accordion holds the matrix (role
cards below `md`, table above).

`/portal/family/invite/`: name (optional) → phone or email → `RoleSelector`,
three radio cards → plot-scope checkboxes when more than one plot → optional
personal message, 200 characters → `Send invitation`. The confirmation states
exactly what the invitee will receive.

`/portal/invite/:token/`: brand block → "{Name} invited you to the Family Circle
for {plot}" → what this role can do → set a password **or** continue with a
magic link → accept.

Roles, user-facing: **Owner · Family manager · Family member · Guest**
(`owner | manager | member | guest`). Access is deliberately unequal — the whole
value is in the distinction. A Family manager sees every report and can request
extra work but **cannot approve a charge, cancel the subscription or change
payment details**.

### 10.7 Order a one-off service — `/portal/orders/new/`

Plot selector → services as cards with prices (Inspection, Express, and
additional works pre-selectable from the last report's recommendations) → date
preference: "as soon as possible" or a month picker → notes → price summary
**computed with the calculator's own arithmetic** → `Send request`. It is a
request, not a checkout: card acquiring is not live, and the button's helper line
says so.

### 10.8 Billing — `/portal/billing/`

Current plan card (name, price, plot parameters, period, **renewal date and the
renewal price visible from day one**) → payment method → invoice list with PDFs
→ `Change plan` → `Cancel subscription` as a **plain Deep Olive text link at the
bottom, never a red button**. Hiding cancellation is a dark pattern and a bank
violation; shouting it in red is equally wrong for this brand.

### 10.9 Cancellation with pro-rata refund — `/portal/billing/cancel/`

Four steps, one screen each, `Stepper` showing `Step n of 4`.

1. **Reason** — five radio options plus free text, all optional, `Skip` visible.
2. **What you will lose** — remaining visits with their scheduled dates, portal
   access end date, family members who lose access. No guilt copy, no "are you
   sure??". Past reports stay readable forever, and the screen says so.
3. **Your refund** — `RefundTable`, shown **as arithmetic, not as a single
   figure**, before the confirm step:

   ```
   refund = amount actually paid × (visits not performed ÷ visits total)
   rounded up to the nearest 100 ֏
   ```

   **The base is what the client actually paid, never the list price.** A client
   who paid 95,000 ֏ after an Express credit and has had 1 of 4 visits receives
   `95,000 × 3/4 = 71,250 → 71,300 ֏`. Computing from 160,000 would return
   120,000 and refund more than we took. The basis is **visits, not days** — the
   client can count visits himself, so the number is never disputed. There is
   **no cap**: the guarantee only sells if it is unconditional. Work already
   performed is already paid for and is never refunded.
4. **Confirm** — one button, with `Keep my subscription` at equal weight.

Success: a confirmation screen and email, a refund reference number, and a line
saying they can return without penalty. The flow must be completable without
phoning us; the bank requires that too.

### 10.10 Profile and notifications — `/portal/profile/notifications/`

A per-plot table of events × recipients with toggles, plus the **local contact**
block (name, phone, channel: SMS or WhatsApp) with an explicit third-party
consent checkbox: *"This person has agreed to receive messages from us."* The
day-before visit reminder is **opt-in** and can be directed to a different
person — the relative in Yerevan who will meet the crew. The plot's
`display_mode` setting (`family_name | full_name | none`, default `family_name`)
lives here.

### 10.11 Auth — `/portal/login/`, `/activate/:token/`, reset

Magic link **and** a password set during activation, both offered on the same
screen, with `Send it again` also offering WhatsApp delivery. A magic link that
lands in a corporate spam filter locks a client out days after paying 160,000 ֏
— the worst possible moment. The phone number stays on the login screen.

### 10.12 Status screens — `rescheduled`, `no-access`, `revisit`

These get the same design budget as a report, because we will meet them in week
one. **No red, no warning triangle, no error colour.** Neutral badge, the word,
an 8px glyph.

`no-access` keeps the full `GpsVerification` block — the crew went, and the
coordinates are the proof. Structure: status badge → heading naming plot and
date → confirmation with arrival time → GPS block with the helper line "This is
where the crew stood. It is how you know they went." → what we found, with a
photograph of the obstruction (**never a photograph of a neighbouring grave**) →
what happens now, with the return date → the line that this visit does not come
out of the subscription → two actions, `Call Hayk` and `Suggest a different
date`.

### 10.13 Every screen needs three more states

Empty, loading and error, on every screen. **An error on a screen showing a
photograph of a grave cannot say "Something went wrong 🙁".** Loading is a
skeleton of Nude blocks at the final geometry, never a shimmer, never a spinner
over a photograph. Errors use `ErrorPanel` and, on any report surface, render
with **no red at all** — the failure there is ours, not the client's, and it is
a sentence, not a validation.

### 10.14 Transactional email

Emails support none of this design system — no custom properties, no `clamp()`,
no reliable webfonts, no `:focus-visible`. **A separate one-column 600px
table-based template**, inline styles, literal hex values generated from the
tokens at build time, Georgia and Arial fallbacks for Gloock and Cabin, no
background images, and **never an embedded photograph** — a report notification
renders in an inbox preview pane at somebody's work. One Anthracite header bar,
text first, a link to the report. This is the artefact the diaspora client sees
before they ever reach the portal.

---

## 11. Contrast table — every pair specified in this document

Measured against the official palette with the WCAG 2.x relative-luminance
formula. **Every text pair below is ≥4.5.** No pair below 4.5 is used for text
anywhere in this specification.

### 11.1 Text pairs — all pass

| Foreground | Background | Ratio | Where |
|---|---|---|---|
| Anthracite `#33373C` | Nude `#EFE5D5` | **9.61** | body, headings, `rail` values, captions on the page ground |
| Anthracite | Ivory `#F3F0E9` | **10.53** | all text on cards, sheets, the header bar, inputs |
| Anthracite | white `#FFFFFF` | **11.98** | print, invoice, report PDF |
| Nude | Anthracite | **9.61** | text on the two dark bands; primary-button label on a Nude fill |
| Ivory | Anthracite | **10.53** | headings and body on dark bands; the footer tagline |
| `#606161` (`--mc-text-secondary`) | Nude | **4.98** | helper text, rail labels, placeholders — ≥15px only |
| `#606161` | Ivory | **5.46** | the same, on cards and sheets |
| Deep Olive `#575E3B` | Nude | **5.49** | links, accent words, secondary-button label on the ground |
| Deep Olive | Ivory | **6.01** | links and accent text on cards, sheets, the header |
| Ivory | Deep Olive | **6.01** | primary-button label; `Our recommendation` badge label; `GPS confirmed` badge |
| Nude | Deep Olive | **5.49** | button label where the ground forces Nude |
| white | Deep Olive | **6.84** | print and PDF only |
| Error `#8C3A2E` | Nude | **6.10** | validation message and glyph on the page ground |
| Error | Ivory | **6.69** | validation message inside a form card or modal |
| Error | `--mc-surface-feedback-error-subtle` over Nude | **≈5.6** | the payment-failure panel heading |
| Ivory | Error | **6.69** | permitted by contrast, but **no error fill exists** — recorded so nobody re-derives it |
| white | Error | **7.61** | print only |
| Anthracite | Nude disc (`AvatarRow` initials) | **9.61** | initials on a Nude disc with a 1px Ivory-40 ring |

### 11.2 Non-text pairs — 3:1 floor, decorative only

| Pair | Ratio | Verdict |
|---|---|---|
| Olive `#7C8654` on Nude | 3.12 | passes 3:1 — rules, frames, focus rings, petal glyphs only |
| Olive on Ivory | 3.42 | passes 3:1 — same uses only |
| Olive on Anthracite | 3.08 | passes 3:1 — 1px decorative rule only, never a glyph a user must read |
| Olive on white | 3.89 | print rules |

### 11.3 Forbidden pairs — recorded so they are never re-derived

| Pair | Ratio | Why it appears here |
|---|---|---|
| **Anthracite on Olive** | **3.08** | FAIL. Two independent reviewers proposed an Olive badge with an Anthracite label. Blocked in the linter. |
| **Ivory on Olive** | **3.42** | FAIL. Nothing is legible on an Olive fill at any size. |
| **Olive on Anthracite as text** | **3.08** | FAIL. The footer tagline is Nude, not Olive. |
| **Anthracite at 70% over Nude** (`≈#6B6B6A`) | **4.28** | FAIL. Opacity is banned for text; use `--mc-text-secondary`. |
| **Anthracite at 60% over Nude** | **3.31** | FAIL badly. The inactive language-switcher item uses `--mc-text-secondary`. |
| **Deep Olive on Anthracite** | **1.75** | Never. All accent colour goes through `--mc-text-accent`, which the dark scope rewrites to Nude. |
| **Error `#8C3A2E` on Anthracite** | **1.57** | Never — fails text *and* the 3:1 non-text floor. **This is why the request form may never sit on a dark band.** |
| Nude on Ivory | 1.10 | Not a contrast pair at all — they are told apart by role and by a hairline. |
| Olive on Deep Olive | 1.76 | Never adjacent. |

---

## 12. What I decided during convergence, and what still belongs to a person

### 12.1 Decisions I took as design lead, because the memos split and the work cannot wait

Each is reversible by the owner and each is in `OPEN-ITEMS.md`.

1. **Header height 56 / 72**, not 64 / 76. The fold is the scarcest resource and
   the 48-character H1 in 9.1 is computed against 56.
2. **Report photography is 4:3**, section 3:2, crew 1:1. Two of three memos
   converged on the 4:3 table; the separate 4:5 comparison crop is deleted.
3. **Photographs run chronologically — `On arrival` first.** The memos split 3–2
   for the after-shot leading. A report that opens on the clean stone with no
   reference frame is a marketing image, and the brand's whole argument is that
   these are records.
4. **Radius scale 0 · 4 · 8 · full.** 2px is too austere at a 48px button on a
   phone; 10/14px is a consumer app. 8px exists only on overlays.
5. **One shadow token, overlay only.** Absolute zero left drawers, sheets and
   lightboxes undefined against a 1.1 tonal step.
6. **Ivory is never a full-bleed band**, with the header bar and the action bar
   as the two declared exceptions. The whitelisted "document band" is dropped in
   favour of a rule a linter can enforce.
7. **The header lock-up is the constructed horizontal SVG** from the measured
   artwork at ≥480px, degrading to mark + live 24px text, then to the word
   alone. The 24px Gloock floor binds live type only, not the drawn wordmark.
8. **`rail` is 14px** at +0.06em, sentence case in Armenian; `overline` 13px is
   the only 13px role in the system.
9. **The calculator result panel is Ivory with an Olive top rule**, not
   Anthracite: it must be able to carry arithmetic and a ceiling message inside
   a light region, and no fixed bottom bar competes with the action bar.
10. **`GpsVerification` serves no map tiles.** `Show on map` is an outbound link
    to the visitor's own map app.
11. **`Our recommendation`**, per `DECISIONS-2 §5`, replaces "Most chosen"
    everywhere, including in `content-limits.json` and the string files.
12. **`Request a consultation` is the label in every context**, including tariff
    cards and the sticky bar. Two labels split recognition; 22 characters fits
    the budget in all three locales.

### 12.2 Still owned by a person, and blocking the named artefacts

| # | Item | Blocks | Owner |
|---|---|---|---|
| 1 | Legal address and registration number | footer, About, Contacts, the invoice, the bank package | Owner |
| 2 | Report SLA in hours (`{REPORT_SLA}`) beyond the 48-hour public promise | portal first entry, two emails | Operations |
| 3 | Confirmation that "within one business day" survives Fridays and Armenian public holidays | six surfaces | CEO |
| 4 | Credit guard: **once per plot** is the design-lead ruling; it needs writing into `products.json` and the Terms | the credit block, the platform | Owner |
| 5 | Armenian display names for Express, Optimal, Maximum, Special — only `Զննում` is confirmed | the Armenian build | Owner / localiser |
| 6 | A single display face covering Latin, Cyrillic and Armenian | `hy` and `ru` headings (they fall to Cabin 600 meanwhile) | Designer |
| 7 | Deep Olive ratified or replaced with the designer's own value | the interface palette | Designer |
| 8 | The medallion divider, the petal glyph, the 16px simplified mark | decorative only; fallbacks specified | Designer |
| 9 | Does Cabin contain ֏ | nothing — 3.5 is safe either way, but the test must run | Build |
| 10 | Legal read on the third-party consent for the Yerevan local contact | the notification matrix | Counsel |
| 11 | Whether a cancelled client keeps report PDFs after the portal — the design assumes **yes, forever, read-only** | the refund policy | Owner + counsel |
| 12 | The written quote PDF, the bank-transfer invoice template and the email template — three artefacts everyone named and nobody owns | the whole post-request path | Design system |

### 12.3 Closed by this document — do not re-open

The legal entity spelling (`MemoryCare LLC`); the credit window (60 days); one
error colour, errors only, no siblings; the 95,000 ֏ figure is public and framed
as the mechanic; two pricing bands and not three annual subscriptions; Special is
not a card; no Olive fill under any label; the form never on a dark band; no
count-up; no shadow except on overlays; no QR; no competitor named; no invented
proof.
