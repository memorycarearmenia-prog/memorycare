# Build the MemoryCare design system — from the given inputs only

You are building a production design system for MemoryCare, a Yerevan
service that cares for family memorial plots and delivers photo, video and
GPS-verified visit reports.

**Everything you need is given below or in the archive that accompanies
this prompt. Nothing else is permitted.** Your job is to turn decided
inputs into a rigorous, buildable system — not to design a brand. The
brand is finished. The palette is finished. The type is finished. The
pricing is finished.

> **The single rule that governs this whole task: if a value is not in the
> inputs, you may not introduce it.** Not a shade, not a size, not a
> weight, not a component, not a state, not a breakpoint. Where the inputs
> are silent and you genuinely need a value to proceed, you **derive it
> from a given value by a stated rule, and you write the rule down** — or
> you mark it `[NOT GIVEN]` and stop. You never fill a gap with taste.

---

## 1. The inputs

### 1.1 Colour — five brand values, from the brandbook of 31.08.2026

| Token | Hex |
|---|---|
| Dark Olive | `#212212` |
| Olive | `#7C8654` |
| Nude | `#EFE5D5` |
| Ivory white | `#F3F0E9` |
| Sky blue | `#A4D6E8` |

**Sky blue is contested and you must not resolve it.** The brandbook's
colour page prints `#D4ECF9`; every delivered vector, PNG, JPG and PDF
paints `#A4D6E8`, and the book's own logo page renders `#A4D6E8`. Use
`#A4D6E8`, and architect the system so that changing it is **one token in
one file**, verifiable by a grep for the literal. Do not average them, do
not pick a third, do not ask which is "better".

### 1.2 Two interface values that are not in the brandbook

| Token | Hex | Why it exists |
|---|---|---|
| Deep Olive | `#575E3B` | On light grounds the body text is Dark Olive and Olive fails as text, so no brandbook colour can mark a link apart from ordinary text. Measures 5.49 on Nude, 6.01 on Ivory. |
| Error | `#8C3A2E` | Validation only. 6.10 on Nude, 6.69 on Ivory. |

**These two, and no others.** If you find yourself needing a third, that is
a signal you have designed a component the site does not need.

### 1.3 Measured contrast — these are facts, not preferences

| Pair | Ratio | |
|---|---|---|
| Dark Olive on Nude | 12.93 | pass |
| Dark Olive on Ivory | 14.17 | pass |
| Nude on Dark Olive | 12.93 | pass |
| Ivory on Dark Olive | 14.17 | pass |
| Sky blue on Dark Olive | 10.26 | pass |
| Deep Olive on Nude / Ivory | 5.49 / 6.01 | pass |
| Error on Nude / Ivory | 6.10 / 6.69 | pass |
| **Olive on Nude / Ivory / Dark Olive** | **3.12 / 3.42 / 4.14** | **fails as text** |
| **Sky blue on Nude / Ivory** | **1.26 / 1.38** | **invisible** |
| **Deep Olive on Dark Olive** | **2.36** | **never** |
| **Error on Dark Olive** | **2.12** | **invisible** |

Four structural rules follow, and they are not negotiable:

1. **Olive never carries text and never receives text.** Fills, petals,
   rules, dividers, decorative panels only.
2. **Sky blue is a dark-ground colour.** On light grounds it may only be a
   tint fill — a panel, a chip ground, the seal disc — never type.
3. **The consultation form may never sit inside a dark band**, because the
   error colour is invisible there.
4. **Nude is the page ground; Ivory is the objects that sit on it** —
   cards, the report sheet, inputs, the header bar. They differ by 1.10 in
   contrast, so the eye cannot tell them apart and the token name must.

### 1.4 Type

Display **Ghea Mariam**. Text **Montserrat**. Armenian text **Montserrat
Arm**, which is a **separate family, not a subset** — the stack must name
it explicitly. Self-host all three.

The ramp is decided. Sixteen roles, desktop only:

| Role | Face / weight | Size / line-height | Tracking |
|---|---|---|---|
| `display` | Ghea Mariam 400 | 72 / 78 | −0.015em |
| `h1` | Ghea Mariam 400 | 56 / 62 | −0.012em |
| `h2` | Ghea Mariam 400 | 40 / 48 | −0.008em |
| `h3` | Ghea Mariam 400 | 28 / 36 | −0.004em |
| `h4` | Montserrat 600 | 20 / 28 | 0 |
| `price-xl` | Ghea Mariam 400 | 60 / 64 | −0.01em, tabular |
| `price` | Ghea Mariam 400 | 44 / 48 | −0.01em, tabular |
| `body-lg` | Montserrat 400 | 19 / 30 | 0 |
| `body` | Montserrat 400 | 17 / 28 | 0 |
| `small` | Montserrat 400 | 15 / 24 | 0 |
| `caption` | Montserrat 500 | 14 / 20 | +0.01em |
| `rail` | Montserrat 500 | 14 / 20 | +0.06em, tabular |
| `eyebrow` | Montserrat 600 uppercase | 14 / 18 | +0.14em |
| `button` | Montserrat 600 | 16 / 20 | +0.02em |
| `nav` | Montserrat 500 | 16 / 24 | +0.01em |
| `legal` | Montserrat 400 | 15 / 24 | 0 |

**Do not add a seventeenth role.** If a piece of UI seems to need one, it
is using the wrong existing one.

Floors: body never below 16px; no informational text below 14px anywhere;
uppercase chips, badges and eyebrows never below 14px; every input 16px.
Tabular lining figures everywhere a number can change. Opacity is banned
for text — secondary text is a token.

### 1.5 The ֏ problem — given to you unsolved, and you must not pretend otherwise

**֏ (U+058F) is in neither Ghea Mariam nor Montserrat.** Verified directly
against Source Serif 4, Montserrat, Noto Sans and Noto Serif: absent from
all four. The browser therefore falls back silently to whatever system
face has it, which is why the live site renders the dram sign at a
visibly different weight and size from the digits beside it — on the most
important string the site prints.

Your system must handle this structurally: **the sign is its own element
with its own font stack, scoped `unicode-range: U+058F` and nothing else**,
so a missing glyph degrades for that one character instead of dragging an
Armenian face onto the English page or breaking a price.

**A face that actually contains the glyph has not been sourced.** Do not
name one you have not verified. Mark it `[NOT GIVEN — someone must source
a face containing U+058F whose weight matches Montserrat]`.

### 1.6 The mark

Two open hands in Nude cradling a five-petal forget-me-not in Olive, its
centre a woven interlaced medallion in Sky blue. The wordmark is
**single-colour Olive**. The tagline is Sky blue, uppercase, wide
tracking, **no full stop**.

Three facts about the delivered artwork you must design around:

- The medallion is **29 filled paths with no stroke attribute** — the
  interlace was drawn as filled outlines, not centrelines. `stroke-dasharray`
  cannot draw it.
- It **still reads at 48px** and closes up below that. 48px is the floor.
- **Clear-space, minimum-size and misuse rules do not exist** in the
  brandbook. Do not invent them. Mark them `[NOT GIVEN]`.

### 1.7 Scope

**Desktop web only.** Owner's decision. No mobile breakpoints, no mobile
ramp, no mobile components. The page must not break in a narrow window,
but there is no mobile design and you must not produce one.

Three languages: **ARM / ENG / RUS**. Armenian and Russian run 15–30%
longer than English, and a hard character budget is a ceiling in **every**
language, not an English budget with an allowance bolted on.

### 1.8 What the system is for

The site sells five products — an inspection, a single visit, two annual
subscriptions and a non-standard one priced by a calculator with two
sliders. It shows a sample visit report. It takes a consultation request.
It has a client portal with family sub-accounts. It needs About, a tariffs
page, legal restrictions, a privacy policy, a refund policy and
service-delivery terms.

**Build components for that, and for nothing else.**

---

## 2. What you must not invent

Read this list twice. Every item on it has been a real failure in this
project.

- **No new colours.** Not a hover shade you liked, not a "neutral grey",
  not a success green, not a warning amber. There is one error colour and
  no siblings. If you need a hover state, derive it from a given value by
  a stated rule — lightness only, hue and saturation held — and write the
  rule and the resulting measured ratio.
- **No new type sizes, weights or families.** Sixteen roles.
- **No dark theme.** Two bands on the page flip to the dark ground. That
  is two sections, not a theme, and it does not imply a dark mode for
  forms, tables or the portal.
- **No mobile.** See §1.7.
- **No component without a page that uses it.** No carousel — the existing
  one produced six audit findings, costs 151 KB and does not advance. No
  testimonial card, no star rating, no counter, no partner strip, no badge
  ribbon. Not even as an "empty state for later".
- **No asserted contrast.** Every ratio in your output is computed from the
  hex values by you and shown. If you write a number you did not compute,
  the deliverable is void.
- **No invented content.** No customer counts, no years in business, no
  placeholder testimonials. The company has zero paying customers.
- **No prices** other than those in the inputs, and no price you cannot
  cite.
- **No filling a `[NOT GIVEN]`.** Six things are genuinely undecided:
  the Sky blue value, a font containing ֏, clear-space and minimum-size
  rules, the favicon crops, the liability figure behind the damage
  guarantee, and the price of the optional flowers/candle item. Each stays
  marked. A system that quietly resolves them is worse than one that
  reports them, because the resolution will be wrong and invisible.

---

## 3. What to build

### 3.1 Tokens, three layers

**Primitive → semantic → component.** Primitives are the raw values.
Semantics say what a thing is for. Components consume semantics only.

Name the semantics so that misuse is a word that is obviously wrong to
type. Two examples of the standard expected:

- Olive lives in a `decor` namespace **defined as "paint that never has a
  foreground"**, so setting `color` on `--decor-olive-fill` reads as an
  error before it renders as one.
- Sky blue as **type** and Sky blue as a **fill** are different tokens.
  The type token is defined only in the dark scope; on light it is
  undefined, so misuse fails to a readable state rather than to 1.26.

Cover: colour, type, space, radius, border, elevation, motion duration and
easing, and z-index. Emit **CSS custom properties and a machine-readable
token file generated from the same source**, so they cannot drift.

### 3.2 Components

Every one with its variants, its states — `default · hover · focus-visible
· active · disabled · loading · error · empty` — and its anatomy.

At minimum, because the site needs them: the tariff card with a variant
whose price slot holds a phrase rather than a number; the price calculator
with two sliders that shows its arithmetic rather than asserting a result;
the report sheet; the verification rail; the language switcher; the header
and its navigation; form fields, buttons, badges, chips; the accordion;
the toast; the modal; and the family-member row.

For each, state **which page uses it**. A component with no page is
deleted.

### 3.3 Proof, not claims

Deliver a contrast table you computed, covering **every text-on-background
pair the system actually produces** — not the pairs that are convenient.
Include the failures and say where they are structurally prevented.

Deliver a keyboard path for every interaction, including any that is
hover-only today.

Deliver a performance budget with numbers you are willing to be held to.

### 3.4 Enforcement

A design system that relies on people remembering the rules has already
failed. Specify the checks that make each structural rule mechanical:
a lint rule, a CI grep, a type-level constraint, a token name that cannot
be misused. For each of the four colour rules in §1.3, say exactly what
catches a violation and at what point — authoring, build, or review.

---

## 4. Deliverables

1. `tokens.css` and a generated token file, from one source.
2. A component specification, one section each, with anatomy, variants,
   states, and the page that uses it.
3. A computed contrast table covering every real pair.
4. The font strategy: stacks per locale, loading, subsetting, fallback
   metrics, and the isolated `unicode-range: U+058F` slice.
5. The enforcement plan of §3.4.
6. **`NOT-GIVEN.md`** — every input that was missing, what you did instead,
   and who must decide. This file is a deliverable, not an apology.
7. A runnable page that demonstrates the system on real components, using
   only tokens.

---

## 5. How this will be judged

In order. Failing an earlier test means the later ones are not considered.

1. **Did you invent anything?** One introduced colour, size or component
   fails the whole deliverable. This is the point of the exercise.
2. **Is every number computed?** Spot-checked. An asserted ratio fails.
3. **Are the four colour rules mechanically enforced**, or merely written
   down?
4. **Can Sky blue be changed in one place?** Grep for the literal. More
   than one hit fails.
5. **Is every `[NOT GIVEN]` still marked?** A quietly filled gap fails.
6. **Does every component name a page that uses it?**
7. **Does the runnable page use only tokens?** A hard-coded hex fails.

---

## 6. If an input contradicts another input

Say so, quote both, and stop on that point. Do not resolve it by
preference and do not average. In this project every silent reconciliation
has later turned out to be wrong, and each one cost a full round of work
to undo.
