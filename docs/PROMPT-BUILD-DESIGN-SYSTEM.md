# Build the MemoryCare design system as a real component library

You are a senior design-systems engineer. You are given a design package as
input and you will produce a working, installable, documented React component
library that implements it exactly. Not a prototype, not a sketch — a package a
product team ships against.

Read this entire brief before writing any code.

---

## 1. What you are given

A folder `MemoryCare-design-v1.0/` containing:

```
START-HERE.md                     read this first
01-specification/
  LEAD-REVIEW.md                  verification protocol — HIGHEST authority
  DECISIONS.md, DECISIONS-2.md    owner rulings — binding
  FINAL-UX.md                     structure, screens, states, flows
  FINAL-UI.md                     visual system, type, grid, layouts
  FINAL-CONTENT.md                every user-facing string, with keys
  FINAL-SYSTEM.md                 tokens, tokens.json, CSS, 52 component specs
  BRIEF.md                        background (contains two known errors)
  working/                        the reasoning history; NOT authoritative
02-brand/
  brandbook/                      the designer's brandbook PDF
  logo/svg|png|pdf + .ai          9 SVG lock-ups, 9 PNG, 3 PDF, AI source
  BRAND-NOTES.md                  palette, measured contrast, open items
03-briefs/                        scope and task documents
04-site-audit/                    the site being replaced; context only
```

### Precedence — settles every conflict, no exceptions

1. `LEAD-REVIEW.md`
2. `DECISIONS.md`, then `DECISIONS-2.md`
3. `FINAL-SYSTEM.md` for tokens and component behaviour ·
   `FINAL-UI.md` for visual treatment · `FINAL-UX.md` for structure and states ·
   `FINAL-CONTENT.md` for strings
4. `BRIEF.md` last — `LEAD-REVIEW.md` §4 corrects two errors in it

`working/` never wins an argument. It exists to explain *why*.

If two sources of equal rank disagree, do not choose silently: implement
nothing for that item, and record it in `OPEN-QUESTIONS.md` with both readings
and your recommendation.

---

## 1b. You are not starting from zero — read this first

A working design system already exists and ships inside the delivered
prototype, at `existing-ds/`. It was built from this same specification by
another team and independently reviewed. **Start from it. Do not rewrite it.**

What it already gets right, verified:

- Three real token layers with the rule enforced: `tokens/primitive.css`
  (the only place a literal appears), `tokens/semantic.css`,
  `tokens/component.css`, plus `tokens/scopes.css` and `tokens/fonts.css`.
- The dark scope is a **class**, `.mc-on-dark`, not a media query — with the
  reason written in the file: a visitor's OS setting must never repaint a page
  containing photographs of a grave in colours nobody checked.
- Deep Olive is remapped to Nude inside that scope, so the 1.75 pair cannot
  occur by construction.
- Radii exactly `0 · 2 · 8 · 9999`. One functional colour. No success or
  warning token anywhere.
- `--mc-tariff-badge-reserve:46px` — the badge-reserve rule implemented.
- `--mc-rail-width-lg:222px` — the verification rail on the specified grid.
- A `.mc-hit-44` helper that carries a comment explaining why all four insets
  must not be set, because that bug was already hit once.
- Five stylesheets — `base`, `controls`, `product`, `chrome`, `feedback` —
  covering roughly fifty components.

**Six defects you must fix in it**, each already located:

1. `tokens/primitive.css:71` — the display font stack
   `"MC Dram","Gloock",Georgia,serif` has **no Armenian face**, so every
   Armenian heading falls back to a generic serif. The text stack is correct;
   copy its approach.
2. `styles/product.css:56` — `.mc-calculator__surcharges` puts
   `--mc-text-secondary` on `--mc-surface-sunken`: `#606161` on `#E4D8C4`
   measures **4.41** and fails. Check `.mc-report__block--recommend`
   (`product.css:100`) for the same pair.
3. `styles/controls.css:160` — `.mc-segmented__item{min-height:36px}`. The
   language switcher is below the 44px minimum and does not use the system's
   own `.mc-hit-44`.
4. `tokens/scopes.css:9` — `--mc-surface-raised-hover:#52565A` is a literal hex
   outside the primitive layer and a grey that exists in no palette.
5. `tokens/semantic.css:129` — `--mc-layout-band-dark:112px` at the 900px
   breakpoint is off the declared spacing scale.
6. `tokens/fonts.css` — fonts load by `@import` from the Google CDN. The
   specification requires self-hosted subset woff2 with no third-party
   requests, and that is a bank condition.

Your job is to take that system from a stylesheet bundle to an installable,
typed, tested, documented package — and to fix those six things on the way.

## 2. What you are building

An npm package `@memorycare/ui`.

```
package.json          name, version 0.1.0, exports map, sideEffects for CSS
src/
  tokens/             the token source of truth (see §4)
  components/         one folder per component (see §7)
  styles/             base stylesheet, resets, font faces
  index.ts            the public barrel
dist/                 built ESM + CJS + .d.ts + compiled CSS
.storybook/           Storybook 8 config
docs/                 authored guidance (see §10)
```

**Stack, non-negotiable:** React 18, TypeScript strict, Vite library mode,
Storybook 8, vanilla CSS with custom properties. No CSS-in-JS runtime, no
Tailwind, no component framework underneath. The system must be usable from a
plain HTML page with a `<link>` and from a React app with an import.

**Why plain CSS:** the client portal is being built by an external developer on
a stack we do not control. A stylesheet plus custom properties is the only
contract that survives that.

---

## 3. Hard rules — violating any of these is a failed deliverable

These come from measured verification in `LEAD-REVIEW.md`, not from taste.

1. **Olive `#7C8654` never carries text and never receives text.** Measured:
   3.12 on Nude, 3.42 on Ivory, 3.08 on Anthracite, 3.42 for Ivory on Olive.
   It is a decorative fill only — petals, rules, dividers, panels, the tagline.
2. **Deep Olive `#575E3B` is the only interactive colour on light grounds.**
   Links, accent text, primary button fill. Measured 5.49 on Nude, 6.01 on
   Ivory, 6.01 for Ivory on it.
3. **Deep Olive is never used on Anthracite** — 1.75. On a dark ground the
   primary button is Nude fill with an Anthracite label (9.61).
4. **Exactly one functional colour exists: error `#8C3A2E`.** There is no
   success token and no warning token. Name it so a sibling cannot be added:
   `--mc-color-feedback-error` with no `-success` / `-warning`. Success and
   warning are expressed with words, glyphs and rule weight.
5. **Error red is never placed on Anthracite** — 1.57, invisible. Consequence:
   **a form may never sit inside a dark band.** Enforce this in the layout
   primitives, not in a comment.
6. **No text below 13px anywhere, in any locale, in any medium.** 13px exists
   only for `overline`. Informational floor 14px. Body 16px minimum on mobile.
7. **Hit areas are at least 44×44**, including invisible padding. Write a test
   that fails otherwise.
8. **Every spacing value is on the scale**
   `4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 72 · 80 · 96 · 128 · 144 · 160`.
   Nothing off-scale. Enforce with a lint rule.
9. **Radii: `0` · `2px` · `8px` (overlays only) · `9999px`.** No other value.
10. **No shadows** except a single overlay elevation for modals, drawers and
    the lightbox.
11. **Cards in a row are always equal height**, the row fixed to its tallest
    child, and a card's action is pushed to its foot by a growing spacer — never
    by hand-tuned padding.
12. **A card without a badge reserves the badge's height**, so titles across a
    row align. The reserve is badge height plus the gap that follows it.

---

## 4. Tokens

`FINAL-SYSTEM.md` contains a complete `tokens.json` and the matching CSS custom
properties. **Use them verbatim.** Do not re-derive, do not rename, do not
"improve" the naming.

Three layers, enforced structurally:

- **primitive** — raw values. The only layer where a literal hex, px or ms
  appears.
- **semantic** — references primitives only.
- **component** — references semantic only.

A component consumes layer three and nothing else. Write a test that fails if a
component stylesheet contains a literal colour or a literal spacing value.

Pipeline: `tokens/tokens.json` → Style Dictionary → `dist/mc-tokens.css`,
`.scss`, `tailwind.tokens.js`, `tokens.d.ts`.

The TypeScript output must make illegal states unrepresentable. `FINAL-SYSTEM.md`
specifies typed unions so that `"monthly"` and `"light visit"` cannot be
expressed — reproduce that intent.

### The values, for cross-checking your import

| Token | Value |
|---|---|
| Olive | `#7C8654` |
| Nude | `#EFE5D5` |
| Ivory white | `#F3F0E9` |
| Anthracite | `#33373C` |
| Deep Olive | `#575E3B` |
| Error | `#8C3A2E` |
| Secondary text | `#606161` |
| Hairline | `#D8D0BC` |

Nude is the page ground. Ivory is objects — cards, sheets, forms, bars. They
differ by only 1.1 in contrast, so the distinction is a rule, not a judgement:
**Nude below, Ivory above.**

---

## 5. Typography

- **Display: Gloock Regular.** Google Fonts, free, **single weight only.** The
  hierarchy is built from size, measure, colour and tracking — never weight.
  Gloock appears in at most five slots and never below 24px.
- **Text: Cabin.** This is a **substitute** for Gill Sans, which the brandbook
  specifies but which is a commercial Monotype face that cannot be licensed for
  the web here. Label it as a substitute in the docs, in the token comment, and
  in the README. If a Gill Sans licence is later purchased, swapping the family
  must be a one-token change.

### Two verified facts you must design around

**The dram sign `֏` (U+058F) is absent from Gloock, Cabin, Noto Sans and Noto
Serif.** Verified by rendering — the glyph does not fall back, it disappears.
Therefore the currency symbol is **its own element with its own font stack**:

```html
<span class="mc-price">160,000 <span class="mc-price__symbol">֏</span></span>
```

and `.mc-price__symbol` carries a `font-family` that resolves it, with `AMD` as
the accessible text alternative. Ship a subset face for U+058F if no system
font is reliable. Every price must also be renderable as `160,000 AMD` — the
word form is the default for surfaces where the glyph cannot be guaranteed.

**Armenian must be handled but cannot be proofed in Figma.** Neither brand face
covers Armenian. Provide a documented fallback stack for `:lang(hy)` and verify
Armenian layouts in a browser. Armenian strings are in `FINAL-CONTENT.md`.

Armenian sets taller and wider than Latin. Every component that holds a string
must be laid out against the **longest** locale, not English. Provide a
Storybook decorator that switches locale so every story can be checked in
`hy`, `ru` and `en`.

---

## 6. Layout primitives

Breakpoints `360 · 600 · 900 · 1200 · 1440`. **360 is the QA floor** — the
audience is mobile-first and 40–60 years old.

Section padding, from `FINAL-UI.md` §4.2 with the adjacency rule from
`LEAD-REVIEW.md` §8:

| | 360 | 1440 |
|---|---|---|
| Light band | 72 / 72 | 128 / 128 |
| Anthracite band | 80 / 80 | 144 / 144 |
| Card padding | 20 | 32 |
| Report sheet padding | 20 | 40 |

**The adjacency rule:** a light section following another light section opens at
`0` and relies on the section above. A light section that is first after the
header, or that follows a dark band, opens at its full value. Dark bands always
carry their full padding on both edges. Implement this in a `<Section>`
primitive that knows its neighbour — do not leave it to whoever composes pages.

Build these primitives before any component: `Section` (ground-aware, enforces
rule 5 above), `Stack`, `Row` (equal-height mode), `Grid`, `Sheet`,
`VisuallyHidden`.

---

## 7. Components

`FINAL-SYSTEM.md` specifies 52 components with every state and measurement.
Implement all of them. Build in this order, because each tier unblocks the next:

**Tier 1 — foundations.** Section, Stack, Row, Grid, Sheet, Rule, Button
(primary / secondary / on-dark, three sizes, four states), Link, Icon,
VisuallyHidden.

**Tier 2 — forms.** Input, Textarea, Select, Checkbox, Radio, Switch, Field
(label + help + error), FormError, ConsentCheckbox, PhoneInput with
international format.

**Tier 3 — the product.** VerificationRail, GpsBlock, ReportSheet,
BeforeAfter (two stacked frames, never a slider, never a side-by-side pair —
that reads as cleaning-product advertising), PhotoPlaceholder, Badge, Chip,
TariffCard, PriceDisplay, PlotCalculator, GuaranteeCard, MemberCard,
PermissionMatrix.

**Tier 4 — states and shells.** EmptyState, LoadingState, ErrorState,
PostponedVisitNotice, NoAccessNotice, Toast, Modal, Drawer, Lightbox, Header,
Footer, LanguageSwitcher, StickyActionBar.

Each component folder:

```
ComponentName/
  ComponentName.tsx
  ComponentName.css          component-layer tokens only
  ComponentName.stories.tsx  every state, every locale
  ComponentName.test.tsx     behaviour + the a11y gates
  index.ts
```

Every component ships: full keyboard operation, a visible focus ring,
`prefers-reduced-motion` respected, and correct semantics before any ARIA
attribute is reached for.

---

## 8. Content rules that constrain the components

From `DECISIONS.md`, `DECISIONS-2.md` and `FINAL-CONTENT.md`. These are not
copy suggestions — they change component APIs.

- **Nothing is invented.** No testimonials, no counts, no "trusted by N
  families", no years in business. The company has zero paying customers. Do
  not build a `Testimonial` component; do not put a rating prop on anything.
- **Never render a QR code or a memorial-page link.** That product does not
  exist. There is no component for it.
- **`Optimal` is marked "Our recommendation", never "Most chosen".** The badge
  prop must not accept a popularity claim.
- **One script per locale.** The English strings contain no Armenian and no
  Cyrillic; the Russian contain no Armenian. Product names are `Inspection`,
  `Express`, `Optimal`, `Maximum`, `Special` in English and their Russian
  equivalents in Russian — never a parenthetical in another alphabet. The owner
  reversed the earlier ruling on 31.08.2026; `DECISIONS-2` §5 carries the
  history. There must be no `armenian` prop on any component.
- **A report's guest view renders no prices, no plans and no upsell** — server
  side, not hidden with CSS. Model this as two distinct components or an
  explicit `audience` prop that gates rendering, so it cannot be defeated by a
  stylesheet.
- **A link preview for a report never carries a photograph of a burial.** The
  OG component takes mark, title and date only.
- **Forbidden words in any string the library ships:** `monthly`, `bestseller`,
  `light visit`, `preventive visit`, `discount`, `save`, `most chosen`,
  `deceased`, `the departed`, `remains`, `object`, `disposal`. No exclamation
  marks. No emoji. Add a lint rule over the strings.
- **Currency always shows `AMD` in words as well as the symbol.**
- **The deceased's name is off by default** in any component that could display
  it, and turning it off must also remove it from already-shared links.

---

## 9. Verification — the gates, all objectively checkable

Ship nothing that fails these. Automate every one.

1. **Contrast.** A test enumerates every text-on-surface pair the token set
   permits and asserts ≥ 4.5. The closed list of allowed pairs is in
   `FINAL-SYSTEM.md`; a pair outside it is a build failure, not a warning.
2. **No literals.** No component stylesheet contains a hex, an rgb, or an
   off-scale spacing value.
3. **Type floors.** No rendered text below 13px; nothing informational below
   14px; body ≥ 16px at 360.
4. **Hit areas.** Every interactive element ≥ 44×44 including padding.
5. **Locale.** Every story renders in `hy`, `ru` and `en` with no overflow and
   no horizontal scroll at 360.
6. **The dram glyph.** A test asserts the symbol element resolves to a face
   that contains U+058F, and that the `AMD` word form is always available.
7. **Axe.** Zero violations on every story.
8. **Visual regression.** Baselines at 360 and 1440 for every story.
9. **The build is consumable.** A scratch React app and a plain HTML page both
   import the built package and render correctly from `dist/` only.

Write `ACCEPTANCE.md` listing each gate with the command that proves it.

---

## 10. Documentation you must author

- **`README.md`** — install, the two consumption paths, the token contract, and
  the substitution note about Gill Sans.
- **`docs/conventions.md`** — written for an AI agent that will build screens
  with this library and will never read the source. Name the real class and
  token vocabulary, the provider or root wrapper if one exists, what breaks
  without it, and one idiomatic snippet. Every name you write must exist in the
  built artifacts — grep before you commit. A conventions file that names
  something which does not exist is worse than no file.
- **`docs/migration-from-figma.md`** — how a Figma frame maps to components.
- **`OPEN-QUESTIONS.md`** — every conflict you found and could not settle.

---

## 11. What you must not do

Do not redesign. Do not "modernise" the palette. Do not add a colour. Do not
introduce a gradient, a shadow beyond the one overlay, or a rounded-pill button.
Do not substitute a familiar component library for a specified component. Do not
soften or sharpen the two service promises — callback within one business day,
report within 48 hours — they appear identically in six places by decision. Do
not invent content to fill a story; use the strings in `FINAL-CONTENT.md`.

If you believe a specified decision is wrong, implement it as specified and put
your argument in `OPEN-QUESTIONS.md`.

---

## 12. Order of work

1. Read `START-HERE.md`, then `LEAD-REVIEW.md`, then the two decision files.
   Only then the four specifications.
2. Scaffold the package and the build. Prove `dist/` imports from a scratch app
   before writing a single component.
3. Tokens, all three layers, with the pipeline and the lint rules.
4. Fonts, including the dram-symbol element and the Armenian fallback stack.
5. Layout primitives.
6. Tier 1 → 4, each tier fully verified before the next begins.
7. Storybook, every state, every locale.
8. The gates in §9, automated.
9. Documentation.
10. `OPEN-QUESTIONS.md` and a written handover of what remains.

Work in small increments and verify continuously. A component that renders
wrong here renders wrong in every screen anyone builds with it.

---

## 13. When it is finished

The package is done when a developer who has never seen this repository can
install it, read `README.md` and `docs/conventions.md`, and build a correct
MemoryCare screen without asking a question.

That is the bar. Not "it compiles".
