# SYSTEM — how a page is built from this

Five files. Three you link, two you never edit by hand.

```
assets/
  tokens.source.json     ← the ONLY file anyone edits for a value
  build-tokens.py        ← emits the two below, in one pass
  tokens.css             ← GENERATED. link 1st
  tokens.json            ← GENERATED. for Figma, the report PDF, anything not CSS
  base.css               ← link 2nd
  components.css         ← link 3rd
  CONTRAST.md            ← computed, not asserted
  SYSTEM.md              ← this
  fonts/                 ← woff2 + FONTS.md
  tools/check-contrast.py
  tools/check-tokens.sh      ← the single entry point; runs the other two
  tools/check-dark-forms.py
```

```html
<link rel="stylesheet" href="/assets/tokens.css">
<link rel="stylesheet" href="/assets/base.css">
<link rel="stylesheet" href="/assets/components.css">
```

**Load order is not a preference.** `tokens.css` declares the cascade-layer
order in its first statement — `@layer mc.reset, mc.tokens, mc.base,
mc.components, mc.utilities;` — and a later `@layer` statement cannot reorder
layers that already exist. If `base.css` loads first, the order is wrong for the
rest of the page's life and nothing visibly breaks until it does.

---

## 1. How a page is assembled

```html
<!doctype html>
<html lang="hy">          <!-- hy | en | ru. :lang(hy) is what swaps the font -->
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- NOT user-scalable=no. The live build ships that on all 36 pages. -->
  <link rel="alternate" hreflang="hy" href="…"> …
  <link rel="canonical" href="…">
</head>
<body>
  <a class="mc-skip-link" href="#main">…</a>

  <header class="mc-header">
    <div class="mc-page mc-header__inner"> … <nav class="mc-nav"> … </nav>
      <nav class="mc-lang"> … </nav> </div>
  </header>

  <main id="main" tabindex="-1">
    <section class="mc-section">
      <div class="mc-page"> <h1>…</h1> </div>      <!-- exactly one h1 -->
    </section>

    <section class="mc-section band--dark">        <!-- one of the two -->
      <div class="mc-page"> … </div>
    </section>
  </main>

  <footer class="mc-footer"><div class="mc-page mc-footer__grid"> … </div></footer>
</body>
</html>
```

Three structural facts:

- **`.mc-page` is the only thing that sets horizontal padding.** It uses
  `--mc-gutter`, which is `clamp(20px, 4vw, 64px)`. A section that sets its own
  `padding-inline` is how a document ends up 452px wide inside a 360px viewport.
- **`.mc-section` is the only thing that sets vertical rhythm**, from
  `--mc-section-gap`.
- **One `h1` per page.** All 36 measured pages currently have none, and axe's
  `page-has-heading-one` and `landmark-one-main` fire on every one of them.

### Layout

**Use the layout utilities, not another component's grid.** They live in
`base.css`, in the `mc.utilities` layer, and they carry no colour and no
meaning — only grid, flex and the space scale.

| | For |
|---|---|
| `.mc-grid` | the workhorse auto-fit grid. `--mc-grid-min` (default 17rem) and `--mc-grid-gap` are per-instance knobs; `--tight` / `--wide` / `--2` / `--3` / `--4` are presets |
| `.mc-split` | two unequal columns that become one below 60rem. `--mc-split-fraction`, `--wide-start`, `--wide-end` |
| `.mc-cluster` | a row of things that wraps: buttons, chips, meta, marks |
| `.mc-media` | a fixed-size thing beside text that flows: a portrait, an icon, a document |
| `.mc-steps` | a numbered sequence. A real `<ol>`; `--horizontal` lays it across above 60rem |
| `.mc-panel` | the neutral container (this one is in `components.css` §25) — Ivory on Nude, a hairline, padding, no meaning. `--quiet`, `--flush`, `--marked` |

These exist because two engineers had to build five layouts out of components
meant for other things — a dashboard grid out of `.mc-tariffs`, an honesty
statement out of `.mc-verify`, a founders block out of `.mc-family__row`. That
is a system failure, not an engineer's mistake: the neutral tools did not
exist. If you find yourself reaching for a component's grid because it happens
to be the right shape, that is the signal to ask for a utility instead.

Every per-instance knob is **declared** in its own rule rather than left to a
`var()` fallback, because §9 of the lint fails on a token nothing defines — and
it is right to: an undeclared knob and a typo look identical.

### The dark band

Two sections flip, and only two. Add `band--dark` to the section element. Every
semantic token is redeclared inside it; components need no dark variants beyond
the short block at the end of `components.css`.

`band--light` exists for the opposite case: a light island **inside** a dark
band. It is needed because custom properties inherit — without it the island
would keep the dark scope's `--mc-text-link` (Sky) and render links at 1.26 on a
pale ground. Nest a light region and you must say so.

**A form that can show a validation error may never be inside `band--dark`.**
See §5, rule 3.

### Widths

Design target is 1440. The page must reflow correctly to 360 with no horizontal
scroll — that is a defect fix, not a mobile design, and there is no second type
ramp and no mobile-only component. What carries it:

- one fluid ramp: every size is `clamp()` between the 360 and 1440 ends, computed
  by the generator from the `min`/`max` pair in `tokens.source.json`;
- `grid-template-columns: repeat(auto-fit, minmax(min(17rem, 100%), 1fr))` — the
  inner `min()` is what stops a track from being wider than its container at
  360, which plain `minmax(17rem, 1fr)` does not;
- container queries on the two components whose layout depends on their own
  width rather than the page's: the tariff card and the report sheet;
- tables get `--stack` (rows become labelled blocks below 48rem) or `--scroll`
  (the table scrolls inside its own focusable region, never the document);
- the nav panel is absolutely positioned only above 60rem;
- `overflow-x: clip` on `html` as a backstop, not as the fix.

---

## 2. Naming

`--mc-<layer><-role><-variant>` for tokens, `.mc-<block>__<element>--<modifier>`
for classes, `--_<name>` for a component's private properties (the button's
`--_bg` / `--_fg` / `--_bd`).

**Three layers, and the boundary is enforceable.**

| Layer | Looks like | Who may use it |
|---|---|---|
| Primitive | `--mc-color-olive`, `--mc-space-6`, `--mc-ink-a56` | `tokens.css` only |
| Semantic | `--mc-surface-object`, `--mc-text-accent`, `--mc-decor-olive-rule` | everything |
| Component | `--_bg` inside `.mc-btn` | that component |

A component that names `--mc-color-*` has reached past the semantic layer, and
`check-tokens.sh` §6 says so.

**Names are chosen so that misuse is a sentence that reads wrong.**

- `--mc-decor-olive-fill` — the namespace is *defined* as **paint that never has
  a foreground**. `color: var(--mc-decor-olive-fill)` is visibly the wrong verb
  before any tool sees it.
- `--mc-text-accent-on-dark` — carries its scope in its name, and exists only in
  that scope.
- `--mc-text-muted` is documented as *disabled labels only*; the thing you want
  for dim-but-readable information is `--mc-text-secondary`. Muted is 3.55;
  secondary is 5.67.
- The guard tokens are whole sentences:
  `--mc-__ERROR-RED-IS-INVISIBLE-ON-DARK-OLIVE-2-POINT-1-2--MOVE-THIS-FORM-OUT-OF-THE-BAND`.

---

## 3. The type ramp

Sixteen roles: `display h1 h2 h3 h4 price-xl price body-lg body small caption
rail eyebrow button nav legal`. There is no seventeenth, and adding one is a
decision that goes back to the design lead, not a line of CSS.

Each role is four custom properties plus family and case:
`--mc-type-<role>-{size,leading,tracking,weight,family,case}`. Apply them as
longhands. **Never use the `font` shorthand:** it resets
`font-variant-numeric` to `normal`, which would silently undo every tabular-
figure rule in the system, and its `var()`-with-slash parsing is the one thing
here that would have depended on a browser behaving well.

Elements carry their role by default (`h1`…`h4`, `small`, `figcaption`, `body`).
Everything else uses the class: `.mc-eyebrow`, `.mc-price`, `.mc-legal`.

Floors, all met: body never below 16px (`body` is 16→17), no informational text
below 14px (`caption`, `rail`, `eyebrow` sit at exactly 14 and do not shrink),
inputs 16px (the `button` role, which is also what stops iOS zooming a focused
field), tabular figures wherever a number can change.

A price slot must be able to hold a phrase — Հատուկ խնամք is priced
"calculator / consultation". `.mc-tariff__price` has a fixed minimum height so
the card row does not step, and `.mc-tariff__price--phrase` borrows the `h3`
role rather than inventing one.

### Fonts, and what is not settled

`fonts/FONTS.md` has the evidence; the short version, read from each `cmap`:

| | Latin | Cyrillic | Armenian | ֏ U+058F |
|---|---|---|---|---|
| GHEA Mariam (827 glyphs) | yes | yes | yes | **yes** |
| Montserrat var (1312) | yes | yes | **no** | **no** |
| Noto Sans Armenian var (430) | yes | no | yes | yes |
| `mc-dram.woff2` (684 bytes) | — | — | — | **yes** |

- **A price needs no fallback at all.** `price` and `price-xl` are set in GHEA
  Mariam, which carries ֏ natively.
- **֏ inside a Montserrat run does.** `MC Dram` is GHEA Mariam subset to U+058F
  and nothing else, loaded with `unicode-range: U+058F`, so the download and the
  substitution are confined to one character: if it 404s, one glyph degrades and
  the price survives.
- **`Montserrat Arm` does not exist.** The brandbook names it; the Google Fonts
  API has no such family. Noto Sans Armenian is a **documented stand-in**, said
  so in the `@font-face` comment and in the token description, and it is not a
  proportional match. → question out to Mariam. When she answers, one
  `@font-face` and one token value change and nothing else does.
- WOFF2 conversion is a build step. It has been run; the command is in the
  header of `base.css` for the day a source is replaced.

---

## 4. Components — the contract

Every component in `components.css` is numbered and commented in place. What
matters at the system level:

**Nothing requires JavaScript.** The nav submenu opens on `:focus-within` as
well as `:hover`, so there is a keyboard path — the live build has hover only,
on every submenu, on every page. The accordion is `<details>`/`<summary>`. The
modal is `<dialog open>` server-rendered, or `:target`. The toast is rendered
after a redirect and dismissed by a link, never by a timer. The calculator is a
`<form method="get">` that round-trips: two range inputs, each paired with a
number input showing the same value, and the arithmetic printed in full above
the total, so nobody has to trust it and nobody has to guess where a thumb is.
Script may enhance any of these; nothing may depend on it.

**State comes from the real attribute.** `[aria-current]`, `[aria-expanded]`,
`[aria-invalid]`, `[aria-busy]`, `[disabled]`, `:checked`, `[open]`. Styling and
accessibility information therefore cannot disagree — which is a different
guarantee from "we remembered to add ARIA".

**No state is signalled by colour alone.** Hover thickens an underline. The
recommended tariff gets a rule as well as a tint. A visited season on the year
rail gets a taller mark *and* a dot. An invalid field gets a thicker border,
`aria-invalid`, and a message with a glyph.

**`:has()` is used twice and nothing depends on it.** The plot picker and the
chip get their state from a native `:checked` sibling rule first; `:has()` only
adds the surrounding card treatment. A browser without it shows a checked radio
and a bolder, underlined label.

**The cancellation dialog, precisely.** Two mechanisms, and they are not equal:

- `<dialog open>`, server-rendered — **the target.** `::backdrop` is free,
  focus is contained, Escape closes it, and the top layer means no z-index
  argument. Use this wherever a server renders the page.
- `:target` — **a degraded preview of that one component**, for the static
  build where nothing renders. The backdrop now works: `.mc-scrim` is hidden by
  default and revealed by `.mc-modal:target + .mc-scrim`, so the scrim must
  follow the modal in the DOM for the sibling combinator to reach it. Paint
  order is unaffected — both are positioned and z-index decides (scrim 900,
  modal 1000). Making the scrim an `<a href="#">` with an `.mc-sr-only` label
  gives click-outside-to-close and a real keyboard path to the same action.

  What `:target` still does **not** give you, and cannot without script:
  **focus is not moved into the dialog, focus is not trapped, and Escape does
  not close it.** The Back button closes it, which is not the same affordance.
  Treat the static build's dialog as a screenshot of the real one. This is the
  only component in the system where the static build is not the real thing,
  and it is called out here so nobody ships `:target` to production believing
  it is equivalent.

**The narrow-width nav is a real trade, and there are two answers.** Below
60rem `.mc-nav` becomes a full-width ladder. For a four-item menu that is
correct. For the twelve-item public menu and the account sidebar it is not: a
sighted touch user scrolls past twelve rows before reaching the `h1`, and the
skip link — the right mitigation, and it stays — only helps the keyboard and
screen-reader user who thinks to use it. `.mc-nav--collapsible` puts the ladder
behind a `<details>` disclosure: keyboard-operable, `[open]` is real state, no
script. Above 60rem the toggle is hidden and the list is revealed regardless of
`[open]`, by overriding the UA rule that hides a closed `<details>`'s children —
handled both ways, `display:none` on children and `::details-content`. The
degradation if an engine ever hid it a third way is that the desktop menu
appears behind the toggle: visible, operable, inconvenient, not broken. There
is no scriptless way to force `[open]` at a breakpoint, so that is the trade.
**Use the plain nav for short menus and the collapsible one for the two long
ones.**

**Two components are flagged off.** `.mc-testimonial` and `.mc-partners` are
`display: none` unless `[data-flag="on"]`, which nothing sets. The markup
survives — the owner's rule 1 removes no functionality — but the content does
not: six slides all named `Անուն Ազգանուն`, photographs of real people presented
as customers of a company that has none, and an empty partners strip. Under
Ameriabank §4.9.2 advertising must comply with the law, which is what makes that
a legal exposure and not a taste question. They are deliberately styled to the
minimum. Polishing them would be work spent on something that must not ship
until there is a real customer and a real partner to name.

**The statistics band survives, repurposed.** `.mc-figures` was four invented
numbers (150,000 customers, 55+ services, 250,000+ graves, 15 years). It now
carries the published visit protocol, where every figure is a real quantity with
a real label: **8 photographs · 4 angles · 2 videos · 1 GPS point.** A figure
with `data-source="none"` is outlined in the error colour and does not ship.

**The payment-marks strip is the single palette exception**, and it is not an
exception in CSS. Ameriabank §4.10 requires the schemes' colour marks; those are
their trademarks and must appear in their own colours. They appear inside
`<img>`. No hex enters this stylesheet for them.

---

## 5. Enforcement — the four structural colour rules

The rules are the brief's. What follows is, for each, the exact thing that
catches a violation and the moment it does.

Three lines of defence, in the order they fire:

| | Where | What it costs |
|---|---|---|
| **A. In the token** | the value itself makes the mistake impossible | free, always on |
| **B. In the lint** | `tools/check-tokens.sh`, pre-commit and CI | seconds |
| **C. In the render** | a visible dashed outline in the screenshot pass | a human looking |

### Rule 1 — Olive never carries text and never receives text

- **A.** There is no token that produces it. Olive reaches the semantic layer
  only as `--mc-decor-olive-fill` and `--mc-decor-olive-rule`, in a namespace
  documented as *paint that never has a foreground*. No `--mc-text-*` and no
  `--mc-surface-*` resolves to Olive in either scope.
- **B.** `check-tokens.sh` §3 fails any `color:` whose value contains
  `--mc-decor-`, and any direct `color: var(--mc-color-olive)`. One whitelisted
  exception, `li::marker`, which accepts no other property and is a graphic at
  3.12/3.42.
- **When.** A. at author time — the sentence reads wrong. B. at commit.
- **The 4.14 case.** Olive on Dark Olive clears AA-large and fails AA. The
  system draws the line at the token rather than at a font size, because a token
  cannot be resized by accident. The wordmark is art; a paragraph is not.

### Rule 2 — Sky blue is a dark-ground colour; on light it is a tint fill only

- **A.** `--mc-text-accent-on-dark` is defined **only** in `.band--dark`. In
  `:root` and in `.band--light` it points at a custom property that does not
  exist, so the `var()` is invalid at computed-value time and `color` falls back
  to the inherited Dark Olive. The failure mode is legible dark text plus a
  guard name in DevTools naming the fix. Sky on light remains available as
  `--mc-decor-sky-tint`, a fill; Dark Olive on it is 10.26.
- **B.** `check-tokens.sh` §4 flags `color: var(--mc-color-sky)` outside
  `.band--dark` — the route in that bypasses the semantic layer.
- **When.** A. in the browser, instantly and harmlessly. B. at commit.

### Rule 3 — no form showing validation errors may sit in a dark band

This is the one that had a hole in it, and it is worth being explicit about why.
The previous token pass wrote *"Deliberately NOT defined here"* in `.band--dark`
and left the space empty. **Custom properties inherit**, so the `:root` value was
still visible to every descendant and an error message in a dark band would have
rendered at 2.12. A comment is not a mechanism.

- **A.** `.band--dark` redeclares `--mc-text-error`, `--mc-border-error` and
  `--mc-surface-error-wash` as guards. `color` → inherited Nude (12.93),
  `border-color` → `currentColor`, `background-color` → `transparent`. The
  message is readable and visibly wrong.
- **C.** `components.css` §6 draws a dashed focus-coloured outline around any
  `.mc-form-error` or `.mc-field__error` inside `.band--dark`, so it is caught in
  the screenshot pass without anyone reading CSS.
- **B.** `tools/check-dark-forms.py` parses the HTML and maintains the open-
  element stack, so it fails **only** when validation markup is genuinely a
  descendant of an element carrying `band--dark`, with `band--light` cancelling
  it exactly as it does in the cascade. It hard-fails the build.
- **When.** A. at render. C. at screenshot. B. at commit.

  *This check was a whole-file substring grep in the first pass, and it was
  wrong.* It fired on any page containing both strings anywhere in any
  relationship, including inside a comment — an engineer tripped it on the home
  page and had to reword a comment that merely contained `mc-form-error`. A
  check that cries wolf gets muted, and a muted check is worse than none. The
  parser version has no false positives and can therefore be a hard failure
  rather than a warning, which is a stronger rule than the one it replaces.

### Rule 4 — Nude is the ground, Ivory is the objects on it

- **A.** `--mc-surface-ground` and `--mc-surface-object`. The two hexes are 1.10
  apart, so a swap produces no visible error at all — a card simply stops looking
  like a card. This is the rule most likely to rot quietly, which is why it is
  the one with the strictest lint.
- **B.** `check-tokens.sh` §6 rejects `var(--mc-color-nude)` and
  `var(--mc-color-ivory)` in `components.css` outside a short named whitelist
  (the payment-mark plate, the Sky-tint blocks, the family avatar — the places
  where the literal ground colour is the point).
- **When.** B. at commit. There is no render-time signal, and there cannot be:
  1.10 is invisible.

### And the rule under all four

**Rule 5 of the brief — only our brand colours; one stray hex fails the work.**
`check-tokens.sh` §2 rejects any hex, `rgb()`, `hsl()`, `oklch()` or `lab()` in
`base.css`, `components.css` or any page HTML. `tokens.source.json` is the only
file permitted to contain a hex, and `tokens.css` is generated from it.

This is why the derived colours in this pass are **alpha composites of brand
colours** rather than new hexes. The previous pass added ten values —
`#737060`, `#5A5A50`, `#2F3021`, `#171808`, `#4E5535`, `#474D30`, `#F2EADD`,
`#E4D8C4`, `#E9E5DC`, `#E7D7C8` — each defensible on its own and each, strictly,
a stray hex. Here every one of them is either gone or expressed as Dark Olive or
Ivory at an alpha, and the ratio is computed against the ground it is actually
painted on. §9 of the lint additionally fails on any `var(--mc-…)` that no file
defines, so a typo cannot become a silent transparent.

---

## 6. Running the checks

```
python3 build-tokens.py              # rebuild after editing tokens.source.json
python3 build-tokens.py --check      # CI: fails if a generated file was hand-edited
python3 tools/check-contrast.py      # the full table
python3 tools/check-contrast.py --assert
python3 tools/check-dark-forms.py --glob ..   # rule 3, tree-aware
sh tools/check-tokens.sh             # everything above, plus the structural rules
```

`check-tokens.sh` is the single entry point; it runs the other three first. Wire it
to `.git/hooks/pre-commit` and to CI. It exits non-zero on any violation and
prints the offending file and line.

---

## 7. What is not settled, and who owns it

| | Status | Owner |
|---|---|---|
| Sky blue `#A4D6E8` vs `#D4ECF9` | Working value is `#A4D6E8` — what all twelve delivered files paint. The brandbook's colour page disagrees with the brandbook's own logo page. Nothing in this system depends on which wins; `CLAUDE.md`'s contrast table does, and is wrong for the artwork (see CONTRAST.md §3). | Mariam |
| `Montserrat Arm` | Not a published family. Noto Sans Armenian is a stand-in, named as one. | Mariam |
| Deep Olive `#575E3B` and Error `#8C3A2E` | Not in the brandbook. Adopted by the owner and carried forward by the brief. There is no brandbook colour that can mark a link apart from body text on light — Olive fails at 3.12. | owner, recorded |
| The registered entity spelling | `Memory Care LLC` vs `MemoryCare LLC` — unresolved, and a bank blocker. It is a string, so it lives in `strings/<loc>.json`, not here. | Davit, with the certificate |
