# PROPOSAL — Design system

**Design Systems Engineer · 01.09.2026**
**Scope:** tokens, components, responsive architecture, accessibility, performance, CSS architecture.
**Supersedes for its own scope:** `docs/design-package-v1/FINAL-SYSTEM.md` (v1.0, 30.08.2026).
Everything in §0.2 of that file — *"Igor never picks a colour, a radius, a duration, a gap or a
string"* — is carried forward. Its values are not: the palette it is built on was retired on
31.08.2026 and the type pair with it.

> **Revision 2 · 01.09.2026 — what changed after the lead's correction.** The first draft was written
> before `BRIEF.md` existed at this path and while the pricing table was still the stale `CLAUDE.md`
> one. Four things changed, all of them substantive:
>
> 1. **§0 B** — the pricing question is closed, not open. The 26.08 owner line-up is now stated and
>    is the one the system is specified against.
> 2. **§3.9 `TariffCard` is rebuilt: five variants, not four**, a `PriceSlot` sub-component that can
>    hold a phrase instead of a number, and **no visit-kind breakdown in the anatomy at all** — the
>    light/heavy split is rejected, every visit is a full visit, and the card carries one count.
> 3. **§3.9a `PriceCalculator`** is now a specified component with its published formula, its two
>    sliders, its ceilings and its shown-arithmetic rule. It was a line in the inventory; it is an
>    owner decision, so it is a spec.
> 4. **§4.3 and §4.6** — the ֏ stack is re-specified against the corrected language rule. One script
>    per locale is about **words, not symbols**: ֏ (U+058F) renders in all three locales, and the
>    isolated one-codepoint slice is what makes that possible without dragging an Armenian face onto
>    the English page. The exact ranges are now written out per family.
>
> The 242 audit screenshots at `docs/site-audit-2026-08-31/screens/`, which were missing when this
> was started, are consistent with every finding cited below; nothing here changed because of them.

---

## 0. Before anything: the facts this is built on, and the two still open

Precedence, and every value in this document traces to one of these:

```
1  docs/rebrand-2026-09-01/BRIEF.md          the approved brief, as corrected 01.09
2  docs/TARIFF-REDESIGN-2026-08-26.md        the owner's pricing decision — supersedes CLAUDE.md
3  assets/brand/logo-v6/README.md            values read out of the vectors, not sampled
4  docs/design-package-v1/DECISIONS-2.md + LEAD-REVIEW.md   owner + lead rulings
5  docs/site-audit-2026-08-31/{FINDINGS,ACCESSIBILITY,PERFORMANCE}.md   measured
6  docs/design-package-v1/FINAL-SYSTEM.md    prior art; its values are retired
```

**`CLAUDE.md`'s brand section is accurate on the palette and stale on the pricing** — it was never
updated after 26.08. Where the two disagree, the 26.08 decision wins, and someone should fix
`CLAUDE.md` at source before a fourth specialist trips over it.

**Every contrast ratio in this document I recomputed myself from the hexes**, sRGB relative
luminance, WCAG 2.x formula. Where my number differs from a number in an existing file I say so.
Where I invented a colour (secondary text, border-strong, the dark raised ground) I give the hex and
its measured ratio, and it is a *working value* the designer may overrule — the token architecture
in §1 makes each of them a one-line change.

Two things remain unresolved and the team must close them. Neither blocks this specification,
because each is isolated behind exactly one token. The third row is recorded as closed, because three
specialists have now tripped over it:

| # | Unresolved | My working decision | The one line that changes if it resolves the other way |
|---|---|---|---|
| **A** | **Sky blue is `#D4ECF9` in the brandbook's colour page and `#A4D6E8` in every delivered vector, PNG, JPG and PDF, including the brandbook's own logo page.** The book contradicts itself. | **`#A4D6E8`** — it is what the artwork physically contains; building the interface on `#D4ECF9` puts two blues side by side the moment an eyebrow sits next to the logo. Both clear WCAG on the dark ground (10.26 / 13.18) and both are invisible on Nude (1.26 / 1.02), so this is not an accessibility question. | `--mc-color-sky-500` in `tokens.json`. See §1.6 for how I made this — including the logo artwork — a genuine one-token swap. |
| **B** | ~~Pricing~~ — **closed.** `CLAUDE.md`'s "Pricing — locked" table is stale: the owner re-decided the entire line-up on **26.08.2026** (`docs/TARIFF-REDESIGN-2026-08-26.md` §8 names that table as outdated), and the 31.08 audit independently treats the 26.08 line-up as expected. Later owner decision wins. | **Five products**: Զննում 20,000 · Էքսպրես 65,000 · Օպտիմալ 160,000/yr (4 full visits) · Մաքսիմում 200,000/yr (6 full visits) · Հատուկ խնամք priced by calculator. **All visits are full visits** — the light/heavy split is rejected. No discounted repeat Express. §3.9 and §3.9a are specified against this. | Prices still live in `content/products.json`, not in any component, and `qa/prices.spec.ts` asserts every rendered price traces to it. The line-up has moved three times in three weeks; the component must not need re-specifying when it moves again. |
| **C** | **Glyph coverage of Ghea Mariam and Montserrat Arm** — Latin/Cyrillic/Armenian, and ֏ (U+058F) in either. No outbound network in this session. | §4 ships a stack that renders correctly whichever way each claim resolves, and a CI test that turns each claim into a build failure rather than a memory. | `--mc-type-price-font` and, in the worst case, one `@font-face` block. |

---

## 1. Tokens — three layers

### 1.0 The rules, unchanged from prior art

1. A component stylesheet references **Layer 3 only**.
2. Layer 3 references **Layer 2 only**. Layer 2 references **Layer 1 only**.
3. Layer 1 is the only place a literal hex, px, ms, cubic-bezier or font name appears.
4. Skipping a layer is never allowed. If a component needs a primitive, the semantic token is
   missing — add it.
5. `grep -rE "#[0-9a-fA-F]{3,8}" src/` returns zero. So does
   `grep -rE "var\(--mc-color-" src/` — **Layer 1 is unreachable from components by name**, which is
   the mechanism that makes §2 work.

Naming grammar (carried from FINAL-SYSTEM §1.2, one addition):

```
mc . <category> . <role> [. <variant>] [. <state>] [. <scale-step>]
```

Names describe role, never appearance (`--mc-text-accent`, never `--mc-text-olive`). Names never
encode a measurement (`--mc-size-5`, never `--mc-space-20px`). Logical properties only. Scale steps
numeric. No abbreviation except `bg`, `fg`, `min`, `max`. **New:** a token whose value is only valid
in one scope carries that scope in its name — every token that resolves to Sky blue ends in
`-on-dark`. §2 explains why.

**Forbidden token substrings, build fails on any of them:** `danger`, `success`, `warning`
(owner-banned family, `DECISIONS.md §2`), `gold`, `navy`, `lilac`, `blue`, `mut`, `dim`,
`anthracite` (the colour no longer exists; the word appearing in a diff means someone pasted from a
retired file), `gill`, `gloock`, `cabin`, `jakarta`.

### 1.1 Layer 1 · Primitive · colour

The five brandbook colours, one error, one working interface value, and the ramps derived from
them. **Every ratio in the "measured" column I computed; the four marked ◆ match the brandbook's
own table exactly, which is the cross-check that my arithmetic is right.**

| Token | Value | Origin | Measured |
|---|---|---|---|
| `--mc-color-dark-olive-500` | `#212212` | brandbook | ◆ 12.93 on Nude · 14.17 on Ivory |
| `--mc-color-dark-olive-400` | `#2F3021` | **derived** — the raised dark ground | Ivory on it 11.79 · Nude 10.76 · Sky 8.53 |
| `--mc-color-dark-olive-600` | `#171808` | **derived** — sunken dark, scrim base | Ivory on it 15.6 |
| `--mc-color-olive-500` | `#7C8654` | brandbook | ◆ 3.12 on Nude · 3.42 on Ivory · 4.14 on Dark Olive — **fails as text everywhere** |
| `--mc-color-olive-700` | `#575E3B` | **Deep Olive, working value**, owner-adopted 29.08 | 5.49 on Nude · 6.01 on Ivory · Ivory on it 6.01 · **2.36 on Dark Olive** |
| `--mc-color-olive-800` | `#4E5535` | derived, link hover | 6.30 on Nude · 6.90 on Ivory |
| `--mc-color-olive-900` | `#474D30` | derived, link active | 7.10 on Nude · 7.78 on Ivory |
| `--mc-color-olive-neutral-600` | `#5C5C50` | **derived, new** — warm secondary text | 5.43 on Nude · 5.95 on Ivory |
| `--mc-color-olive-neutral-500` | `#737060` | **derived, new** — border-strong | 3.99 on Nude · 4.38 on Ivory — clears 1.4.11's 3:1 with margin |
| `--mc-color-nude-500` | `#EFE5D5` | brandbook | the page ground |
| `--mc-color-nude-400` | `#F2EADD` | derived, hover of a Nude fill | — |
| `--mc-color-nude-600` | `#E4D8C4` | derived, sunken | Dark Olive on it 11.46 |
| `--mc-color-ivory-500` | `#F3F0E9` | brandbook | the object ground |
| `--mc-color-ivory-400` | `#E9E5DC` | derived, pressed state of an Ivory fill | — |
| `--mc-color-sky-500` | **`#A4D6E8`** | delivered artwork — **contested, see §0 A** | 10.26 on Dark Olive · **1.26 on Nude, 1.38 on Ivory — invisible** |
| `--mc-color-feedback-error-500` | `#8C3A2E` | prior art, unchanged | 6.10 on Nude · 6.69 on Ivory · **2.12 on Dark Olive — invisible** |
| `--mc-color-white` | `#FFFFFF` | — | permitted only as the report-print ground |

Alpha ramps — all derived from Dark Olive or Ivory, never from black or white:

| Token | Value | Composited | Use |
|---|---|---|---|
| `--mc-alpha-dark-08` | `rgb(33 34 18 / .08)` | `#DFD5C5` on Nude | hairline on a light card |
| `--mc-alpha-dark-12` | `rgb(33 34 18 / .12)` | `#D6CEBE` | disabled fill |
| `--mc-alpha-dark-16` | `rgb(33 34 18 / .16)` | `#CEC6B6` | divider |
| `--mc-alpha-dark-60` | `rgb(33 34 18 / .60)` | `#737060` | **border-strong is this composite, declared solid** — see §1.7 |
| `--mc-alpha-dark-72` | `rgb(33 34 18 / .72)` | — | scrim |
| `--mc-alpha-ivory-12 / -24 / -45` | `rgb(243 240 233 / …)` | on Dark Olive: 1.41 / 2.07 / **3.99** | dark-scope hairline, divider, input border |
| `--mc-alpha-olive-16` | `rgb(124 134 84 / .16)` | `#E1DAC6` on Nude | decorative wash only |
| `--mc-alpha-deepolive-08 / -16` | `rgb(87 94 59 / …)` | — | secondary-button hover/active, focus halo |
| `--mc-alpha-error-08` | `rgb(140 58 46 / .08)` | `#E7D7C8` on Nude | error panel ground — error text on it **5.42** |

**Opacity is banned for text, system-wide, at every layer.** Prior art proved the trap: Anthracite
at 70% over Nude measures 4.28 and fails. Every "N% of the text colour" in any earlier document is
replaced by a solid token here. The alpha ramp above is for *fills and borders only*, and every
composited result is listed so no one has to guess.

### 1.2 Layer 2 · Semantic · colour

Two scopes only: the default (light) scope on `:root`, and `.mc-on-dark`, applied with a **class,
never a media query**. MemoryCare has no OS dark mode: a visitor's system setting must never repaint
a page carrying photographs of a grave in colours nobody checked. `prefers-color-scheme` appears
nowhere in this codebase, and `color-scheme: light` is declared on `:root`.

| Semantic token | Light scope | `.mc-on-dark` | Ratio that justifies it |
|---|---|---|---|
| `--mc-surface-ground` | nude-500 | dark-olive-500 | the page |
| `--mc-surface-object` | ivory-500 | dark-olive-400 | cards, the report sheet, inputs, the header bar |
| `--mc-surface-sunken` | nude-600 | dark-olive-600 | wells, table zebra, disabled input |
| `--mc-surface-float` | nude-500 | dark-olive-400 | **the opposite light of the band beneath** — a menu never opens Ivory on Ivory |
| `--mc-surface-inverse` | dark-olive-500 | nude-500 | the band that flips |
| `--mc-surface-accent-strong` | dark-olive-500 | nude-500 | primary button fill |
| `--mc-decor-olive-fill` | olive-500 | olive-500 | **§2** |
| `--mc-decor-olive-rule` | olive-500 | olive-500 | **§2** |
| `--mc-decor-sky-tint-on-dark` | — | sky-500 | **§2** |
| `--mc-text-primary` | dark-olive-500 | nude-500 | 12.93 both ways |
| `--mc-text-secondary` | olive-neutral-600 | ivory-500 | 5.43 · 14.17 — ≥14px only |
| `--mc-text-accent` | olive-700 | nude-500 | 5.49 · 12.93 — **Deep Olive is 2.36 on the dark ground, so the scope rewrites it** |
| `--mc-text-link` | olive-700 | nude-500 | as above |
| `--mc-text-link-hover` | olive-800 | ivory-500 | 6.30 · 14.17 |
| `--mc-text-on-accent` | ivory-500 | dark-olive-500 | **14.17 · 12.93** |
| `--mc-text-eyebrow-on-dark` | *unset* | sky-500 | 10.26. **Unset in the light scope on purpose** — §2 |
| `--mc-text-feedback-error` | error-500 | *unset* | 6.10. **Unset on dark on purpose** — §2 |
| `--mc-border-subtle` | alpha-dark-08 | alpha-ivory-12 | decorative only, never a control |
| `--mc-border-default` | alpha-dark-16 | alpha-ivory-24 | card hairline; decorative |
| `--mc-border-strong` | olive-neutral-500 `#737060` | alpha-ivory-45 | **3.99 / 3.99** — every input, checkbox, radio, slider track |
| `--mc-border-accent` | olive-700 | nude-500 | selected, leading tariff |
| `--mc-border-focus` | olive-700 | nude-500 | 5.49 / 12.93 — comfortably over 1.4.11's 3:1 |
| `--mc-border-feedback-error` | error-500 | *unset* | 6.10 |

### 1.3 The closed contrast list

**A foreground/background pair not in this table does not exist in the system.**
`stylelint-mc-contrast` fails the build on any `color` / `background-color` pair outside it.

#### Permitted

| # | Foreground | Background | Ratio | For |
|---|---|---|---|---|
| 1 | text-primary `#212212` | surface-ground `#EFE5D5` | **12.93** | all text |
| 2 | text-primary | surface-object `#F3F0E9` | **14.17** | all text |
| 3 | text-primary | surface-sunken `#E4D8C4` | **11.46** | all text |
| 4 | text-primary | error panel ground `#E7D7C8` | **11.48** | all text |
| 5 | text-secondary `#5C5C50` | surface-ground | **5.43** | text ≥14px only |
| 6 | text-secondary | surface-object | **5.95** | text ≥14px only |
| 7 | text-accent `#575E3B` | surface-ground | **5.49** | all text, links, icons |
| 8 | text-accent | surface-object | **6.01** | all text |
| 9 | link-hover `#4E5535` | ground / object | **6.30 / 6.90** | all text |
| 10 | text-on-accent `#F3F0E9` | accent-strong `#212212` | **14.17** | primary button label, leading badge |
| 11 | text-feedback-error | surface-ground / object | **6.10 / 6.69** | error text, glyph, border |
| 12 | text-feedback-error | error panel ground `#E7D7C8` | **5.42** | error panel body |
| 13 | text-primary (`#EFE5D5` in scope) | surface-ground on dark `#212212` | **12.93** | all text on the dark band |
| 14 | ivory | dark surface-object `#2F3021` | **11.79** | all text on a dark card |
| 15 | nude | dark surface-object | **10.76** | all text on a dark card |
| 16 | text-eyebrow-on-dark `#A4D6E8` | dark ground | **10.26** | eyebrows, rail labels, accent lines on dark |
| 17 | text-eyebrow-on-dark | dark object `#2F3021` | **8.53** | same, on a dark card |
| 18 | dark-olive | nude fill (dark-scope primary button) | **12.93** | that button |
| 19 | border-strong `#737060` | ground / object | **3.99 / 4.38** | non-text 1.4.11 |
| 20 | border-focus `#575E3B` | ground / object | **5.49 / 6.01** | focus ring, 1.4.11 |

#### Forbidden, with the reason each is the mistake *this* palette invites

| Foreground | Background | Ratio | Ruling |
|---|---|---|---|
| **anything** | Olive `#7C8654` | ≤ 4.14 | **No label on Olive, ever.** Dark Olive on Olive is 4.14 — it clears AA-large and *only* AA-large, which is exactly why the wordmark works in the lock-up and why someone will reach for it as a button. A button label is not large text. Blocked in code. |
| Olive | Nude / Ivory / Sky | 3.12 / 3.42 / 2.48 | **Olive never carries text at any size.** There is no "16px as a graphic element" exemption: the large-text exemption starts at 24px regular, and 3.12 also fails the 3:1 non-text floor. |
| Olive | Dark Olive | **4.14** | The one place Olive is legible — and still below 4.5. Permitted for the **wordmark artwork only**, which is a logo and exempt (1.4.3 excludes logotypes). Never for live text. |
| Sky blue | Nude / Ivory | **1.26 / 1.38** | Invisible. Sky is a dark-ground colour and a light-ground *tint fill*, never type on light. |
| Deep Olive | Dark Olive | **2.36** | Never. The scope rewrite makes this unreachable. |
| Error `#8C3A2E` | Dark Olive | **2.12** | Never — fails text *and* the 3:1 non-text floor. **Consequence: no form may sit on a dark band anywhere in the product.** §2 enforces it. |
| any text | any alpha of a text colour | — | Opacity banned for text. |
| Ivory | Ivory | 1.0 | A floating layer never opens on its own light; `--mc-surface-float` takes the opposite. |
| text-secondary | anything, < 14px | — | 5.43 has a 20% margin; below 14px that margin is a rendering difference, not a design one. |

### 1.4 Layer 1 · size, radius, border, shadow, motion, z, breakpoints

**Space.** 4px base, expressed in `rem` so browser zoom and the reader's text-size setting work.
`--mc-size-<n>` where the value is `n × 4px`. Closed set:
`0 · 1 · 2 · 3 · 4 · 5 · 6 · 8 · 10 · 12 · 16 · 20 · 24 · 30 · 40 · 50`
→ `0 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 120 · 160 · 200`.
Plus one exception, `--mc-size-hair: 2px`, for the only 2px gap in the system (the badge inset).

| Use | Value |
|---|---|
| icon ↔ label inside a control | `size-2` |
| label ↔ field, field ↔ help | `size-2` |
| between form rows | `size-5` |
| card padding | `size-5` base · `size-6` `sm`+ · `size-8` feature cards |
| between cards in a band | `size-4` base · `size-6` `sm`+ |
| between blocks in a section | `size-6` base · `size-8` `md`+ |
| between sections | `--mc-layout-section-block: clamp(3rem, 2rem + 5vw, 7.5rem)` |
| page block-end padding wherever `MobileActionBar` can appear | `size-22` (88px) |
| clear space between adjacent targets | ≥ `size-2` |

**Radius** — lead-ruled 29.08, carried forward, with one bug fixed.

| Token | Value | Applies to |
|---|---|---|
| `--mc-radius-0` | `0` | photographs, the report sheet, bands, rules, the verification rail, tables, the plot diagram |
| `--mc-radius-sm` | `2px` | buttons, inputs, cards, tariff cards, badges, chips, toasts, menus |
| `--mc-radius-overlay` | `8px` | modals, drawers, bottom sheets, the lightbox — **and nothing else** |
| `--mc-radius-full` | `9999px` | slider thumb, avatar disc, petal bullet |

> **Override of prior art.** `FINAL-SYSTEM §5.3` deletes `--mc-radius-md` from the token file, and
> then `§3` sets `--mc-modal-radius: var(--mc-radius-md)`. That is an undefined variable: every
> modal in that system would have rendered with `border-radius:` invalid, i.e. square, silently.
> The 8px overlay value the lead ruled is real and now has a name of its own.

**Border.** `--mc-border-0: 0` · `-1: 1px` · `-2: 2px` · `-3: 3px`. There is no 1.5px. 1px at rest,
2px when selected or in error, 3px only for a panel's inline-start rule.

**Elevation.** One shadow in the system, tinted with Dark Olive, never black:

```css
--mc-elevation-overlay:
  0 2px 4px -1px rgb(33 34 18 / .12),
  0 12px 32px -4px rgb(33 34 18 / .18);
```

Referenced by exactly five components: `Modal`, `Drawer`, `BottomSheet`, `Lightbox`, `Toast`.
No card shadow, no hover lift, no header shadow. **Elevation on a light ground is a ground change
plus a hairline, not a shadow** — Nude and Ivory differ by 1.10 in contrast, so without the 1px rule
the step reads as a printing error. `backdrop-filter` appears nowhere: it costs a compositor layer
on the old Android that is our QA floor and buys nothing over a solid bar.

**Motion.**

| Token | Value |
|---|---|
| `--mc-duration-instant` | `80ms` |
| `--mc-duration-fast` | `140ms` |
| `--mc-duration-base` | `220ms` |
| `--mc-duration-slow` | `320ms` |
| `--mc-ease-standard` | `cubic-bezier(.2, 0, 0, 1)` |
| `--mc-ease-decelerate` | `cubic-bezier(0, 0, .2, 1)` |
| `--mc-ease-accelerate` | `cubic-bezier(.4, 0, 1, 1)` |
| `--mc-ease-linear` | `linear` |
| `--mc-motion-distance-sm` | `8px` |
| `--mc-motion-distance-md` | `16px` |

Semantic: `--mc-motion-hover: var(--mc-duration-fast) var(--mc-ease-standard)` ·
`--mc-motion-enter: var(--mc-duration-base) var(--mc-ease-decelerate)` ·
`--mc-motion-exit: var(--mc-duration-fast) var(--mc-ease-accelerate)` ·
`--mc-motion-expand: var(--mc-duration-base) var(--mc-ease-standard)`.

**No spring physics anywhere. Only `opacity` and `transform` are ever animated** — animating
`height`, `width`, `top` or `box-shadow` is a build failure, because it is also an INP failure.
(The accordion is the one exception and it uses `grid-template-rows: 0fr → 1fr`, which the compositor
handles without a layout thrash per frame; see §3.16.)

**z-index** — a closed ladder, no other value exists:

| Token | Value | Layer |
|---|---|---|
| `--mc-z-base` | `0` | page content |
| `--mc-z-raised` | `1` | a card's stretched-link `::after` |
| `--mc-z-sticky` | `100` | sticky table header, sticky section label |
| `--mc-z-header` | `200` | site header |
| `--mc-z-actionbar` | `300` | `MobileActionBar`, report share bar |
| `--mc-z-popover` | `400` | select menu, combobox, tooltip |
| `--mc-z-scrim` | `500` | modal / drawer scrim |
| `--mc-z-overlay` | `600` | modal, drawer, bottom sheet, lightbox |
| `--mc-z-toast` | `700` | toast region |
| `--mc-z-skiplink` | `800` | the skip link, above everything, always |

**Breakpoints.** Unchanged from the lead's ruling — one set, for CSS *and* script. The audit found a
site where `menu.js` gated on `innerWidth <= 1300` while the CSS switched somewhere else, producing
a live mobile menu between 1024 and 1300px with no way to open it (FINDINGS #28). That cannot recur
here because the breakpoints are generated from `tokens/breakpoints.json` into **both**
`@custom-media` rules for PostCSS **and** a `breakpoints.ts` consumed by any script that needs one.
A media query written by hand is a build failure.

| Name | Min width | Cols | Gutter | Margin | What changes |
|---|---|---|---|---|---|
| `base` | **360** | 4 | 16 | 20 | **QA floor and the arithmetic floor.** Every fold claim is computed at 360×640 |
| `sm` | 600 | 8 | 24 | 40 | tariff cards 2-up; one-off band 2-up |
| `md` | 900 | 8 | 24 | 40 | desktop nav; drawer gone; header 56 → 72 |
| `lg` | 1200 | 12 | 24 | container max 1200 | `VerificationRail` becomes a right column |
| `xl` | 1440 | 12 | 32 | container max 1200 | more air, **no new layout** |

Media queries are **min-width only**, with exactly two documented `max-width` exceptions: hiding the
desktop nav, and the calculator's stacked-slider layout. Container: `760px` narrow variant for legal
pages, About, report body copy and the crew note.

### 1.5 Layer 3 · component tokens

One group per component, `--mc-<component>-<part>-<prop>[-<state>]`. Every value is a Layer 2
reference. Extract:

```css
--mc-button-min-block-size: 48px;          /* 44px from lg — pointer, not touch */
--mc-button-padding-inline: var(--mc-size-6);
--mc-button-radius: var(--mc-radius-sm);
--mc-button-primary-bg: var(--mc-surface-accent-strong);
--mc-button-primary-bg-hover: var(--mc-color-dark-olive-400);   /* documented Layer-1 step */
--mc-button-primary-fg: var(--mc-text-on-accent);
--mc-button-secondary-border: var(--mc-border-accent);
--mc-button-secondary-fg: var(--mc-text-accent);
--mc-input-min-block-size: 48px;
--mc-input-bg: var(--mc-surface-object);
--mc-input-border: var(--mc-border-strong);
--mc-input-border-focus: var(--mc-border-focus);
--mc-input-border-error: var(--mc-border-feedback-error);
--mc-card-bg: var(--mc-surface-object);
--mc-card-border: var(--mc-border-default);
--mc-tariff-border-leading: var(--mc-border-accent);
--mc-tariff-badge-reserve: 46px;           /* lead-ruled, see §3.9 */
--mc-rail-inline-size-lg: 222px;
--mc-report-sheet-bg: var(--mc-surface-object);
--mc-report-sheet-radius: var(--mc-radius-0);
```

Exactly three Layer-1 references are permitted at Layer 3, all of them hover/active steps that have
no semantic meaning of their own: `dark-olive-400`, `olive-800`, `olive-900`. They are listed in the
linter's allowlist by name. Everything else routes through Layer 2.

### 1.6 The Sky-blue swap — how it is genuinely one token

`#A4D6E8` appears in this system in exactly **one** place, `--mc-color-sky-500` in `tokens.json`.
Four mechanisms keep it there:

1. **No component may reference it.** All Sky use routes through `--mc-text-eyebrow-on-dark`,
   `--mc-decor-sky-tint-on-dark` and `--mc-decor-sky-rule-on-dark`.
2. **The logo swaps too, which is the part that usually breaks.** The mark ships as **inline SVG**,
   not `<img>`, with the delivered `<style>` classes rewritten to
   `.cls-3 { fill: var(--mc-color-sky-500); }`, `.cls-1 { fill: var(--mc-decor-olive-fill); }`,
   `.cls-2 { fill: var(--mc-color-nude-500); }`. A palette change repaints the artwork on the next
   deploy with no re-export. The monochrome lock-ups stay as delivered files, because they contain
   no blue.
3. **The favicon and the OG image are generated, not drawn.** `npm run build:brand` rasterises the
   inline SVG at 16/32/180/512 and composites the OG card, reading the token file. They are build
   artefacts, not committed art. (This also closes the gap `logo-v6/README.md` records: the
   brandbook ships no favicon crop.)
4. **CI proves it.** `qa/sky.spec.ts`: `grep -riE "a4d6e8|d4ecf9" --exclude=tokens.json src/ public/`
   returns zero, and a rendered-DOM assertion that the medallion's computed `fill` equals the token.

If Mariam rules `#D4ECF9`, the change is one line and one re-export of the three colour lock-ups by
her; nothing in this repository is touched but that line. **The same architecture protects Deep
Olive `#575E3B`**, which is also a working value and also unratified.

### 1.7 Two overrides of prior art in the colour layer, stated plainly

- **`--mc-text-secondary` was `#606161`, a cool grey derived from Anthracite. It is now `#5C5C50`,
  5.43 on Nude.** Anthracite is retired; a cool grey next to a warm near-black olive reads as a
  second, dirtier text colour rather than as a quieter one. Prior value measured 4.98 — an 11%
  margin over 4.5. The new one has 21%.
- **`--mc-border-strong` was `--mc-alpha-anthracite-50`, which composites to 3.01 on Nude. It is now
  the solid `#737060`, 3.99.** This one matters: `border-strong` is the *input* border, and WCAG
  1.4.11 requires 3:1 for a control boundary. 3.01 passes by 0.01 — that is a rounding difference,
  not a design decision, and it fails outright the moment a card's Ivory ground sits under it at
  3.30. The solid token clears both grounds by a third.

---

## 2. Making the four structural rules unbreakable

The brief's four rules are not preferences; each one is a defect that a competent developer will
introduce anyway, because in every other design system he has used the token he reached for was
fine. So each rule gets a **name that is wrong to type**, a **scope that removes the value**, and a
**linter that fails the build**. Prose is the fourth line of defence, not the first.

### Rule 1 — Olive never carries text and never receives text

**The name.** There is no `--mc-surface-olive`, no `--mc-text-olive`, no `--mc-color-accent-olive`.
The only semantic tokens that resolve to `#7C8654` are:

```
--mc-decor-olive-fill
--mc-decor-olive-rule
--mc-decor-olive-petal
```

`decor` is defined once, in the token file's header comment and in the linter: **a `decor` value is
paint that never has a foreground.** `surface` means "things sit on this"; `decor` means "nothing
does". A developer writing `background: var(--mc-decor-olive-fill)` on an element that contains text
has typed a word that says he shouldn't.

**The lint.** `stylelint-mc-contrast` has one rule that is not about a pair: any selector that sets
`color` and whose computed background chain resolves to a `--mc-decor-*` token is an error, and any
`--mc-decor-*` token used on an element that is not `aria-hidden="true"`, a `<hr>`, an `<svg>` fill,
or a `::before`/`::after` is an error. The permitted-property list is closed:
`background-color` on decorative elements, `border-color`, `fill`, `stroke`.

**The test.** `qa/contrast.spec.ts` walks every rendered route in three locales at 360 and 1280,
finds every text node, resolves its painted background, and fails on any pair outside §1.3. That
catches the case the linter cannot see: an Olive panel introduced by a *parent* rule with text added
by a *child* rule in another file.

**The one exemption, written down so nobody widens it.** Olive on Dark Olive is 4.14 and the
wordmark uses it. Logotypes are exempt from 1.4.3. The exemption covers `svg` inside `.mc-logo` and
nothing else — asserted by selector in the linter.

### Rule 2 — Sky blue is dark-ground only

**The name.** Every token that can resolve to Sky and be *read* ends in `-on-dark`:
`--mc-text-eyebrow-on-dark`, `--mc-decor-sky-rule-on-dark`, `--mc-decor-sky-tint-on-dark`.
`color: var(--mc-text-eyebrow-on-dark)` inside a light section is a sentence that reads wrong.

**The scope.** In the light scope those tokens are **not defined at all**. Not "defined to something
safe" — undefined. A component that uses one outside `.mc-on-dark` renders with an invalid value and
the property is dropped: the eyebrow inherits `--mc-text-primary` and remains legible, and the
mistake is visible in review as *"the eyebrow isn't blue"* rather than invisible as *"the eyebrow
is 1.26"*. **Failing to the readable state, not to the branded one, is the whole design.**

**The exception that must exist.** Sky *is* usable on light as a tint fill — a chip ground, a panel,
the medallion — because a fill has no contrast requirement of its own. That is
`--mc-decor-sky-tint-on-dark`'s light-scope sibling `--mc-decor-sky-tint`, which is defined in both
scopes, is in the `decor` namespace (Rule 1's machinery therefore also applies: nothing sits on it
that isn't checked), and whose composited grounds are pre-measured: Sky at 18% over Nude is
`#E2E2D8`, text-primary on it **12.37**; at 18% over Ivory `#E5EBE9`, **13.36**. Those two
composites are in the permitted list; a third opacity is not.

### Rule 3 — the form never sits on dark

This is the most dangerous of the four, because it fails *silently and only when something goes
wrong*: the form works perfectly until a visitor mistypes a phone number, and then the error is
2.12 against its ground and simply is not there.

**The name.** The error tokens are `--mc-text-feedback-error` and `--mc-border-feedback-error`, and
in `.mc-on-dark` they are **unset**. An error state on a dark ground has no colour to paint with.

**The guard.** A live custom-property tripwire, so the failure is loud in development and impossible
in production:

```css
:root       { --mc-form-guard: var(--mc-surface-object); }
.mc-on-dark { --mc-form-guard: ;            /* deliberately empty — invalid at computed-value time */ }

.mc-field { background: var(--mc-form-guard, #FF00FF); }
```

An empty custom-property value makes `var()` fall back, so a field placed inside a dark band paints
magenta the first time anyone looks at it. It is not subtle and it is not meant to be.

**The lint.** `stylelint-mc-scope`: any selector containing `.mc-on-dark` that also matches a
descendant of the form component list (`Field`, `Input`, `Textarea`, `Select`, `Checkbox`, `Radio`,
`ConsultationForm`, `ErrorSummary`) is a build error. **The build fails, so the magenta never
ships** — it exists to catch the case where a section's scope class is added at runtime by a CMS
field, which the linter cannot see and the DOM test can.

**The test.** `qa/scope.spec.ts`: for every route, assert `document.querySelectorAll('.mc-on-dark
.mc-field').length === 0`, and assert every form's nearest scope ancestor is the light scope.

**And the design consequence, which is the actual point:** the consultation CTA band on the home
page cannot be the dark band. The dark band goes above or below it and the form sits on Nude. That
is a layout instruction to whoever designs the page, not a note in a token file, so it appears in
§5's per-component breakpoint table as well.

### Rule 4 — Nude is the ground, Ivory is the objects

Nude and Ivory differ by 1.10 in measured contrast. To the eye they are the same colour. Left as
`--mc-color-nude-500` and `--mc-color-ivory-500`, they will be used interchangeably within a month,
and the reason nobody will notice is that *nothing will look wrong* — the page will just quietly
stop having a figure/ground structure.

**The names carry the rule, not the pigment.** `--mc-surface-ground` and `--mc-surface-object`.
There is no `--mc-surface-nude` and no `--mc-surface-ivory` at Layer 2, and the primitives are
unreachable from components by the rule in §1.0.5. A developer choosing a card background sees one
token whose name says "this is an object".

**The hairline makes it visible.** Every object on a light ground carries a 1px `--mc-border-default`
rule. Without it the 1.10 step is a printing error; with it the step is a decision. This is why
`--mc-card-border` is not optional and there is no `Card--borderless`.

**The lint.** `background: var(--mc-surface-ground)` on anything that is not `<body>`, a `<section>`
or a band element is an error, and `--mc-surface-object` on `<body>` is an error. Both are single
selector rules.

**The test.** `qa/ground.spec.ts` asserts the computed background of `<body>` equals nude-500 on
every route in every locale, and that every `.mc-card`, `.mc-report-sheet` and `.mc-field` computes
to ivory-500 (or their dark-scope equivalents).

---

## 3. Component inventory

**Rules common to every component**, carried from prior art and extended:

1. **Five states or it is not done:** `default · loading · empty · error · success`. Where a state is
   genuinely impossible the spec says so in one sentence. A spec with no empty state is rejected.
2. Interactive states are a closed set: `default · hover · focus-visible · active · disabled ·
   loading · selected · error`. **`hover` never exists without a non-hover equivalent** — the audit
   found five hover-only affordances and one submenu reachable only by pointer.
3. No literal user-facing text in any component; copy comes from `content/strings.<locale>.json` by
   key. No numbers in copy; prices come from `content/products.json` as `{price}`.
4. Every icon-only control has an `aria-label` from the string file.
5. **Colour is never the only carrier of meaning.** Status is a glyph plus a word; the leading tariff
   is a border plus a worded badge; a form error is a border plus a glyph plus a sentence.
6. Every component survives the Storybook pseudo-locale (+30% length, accented) before acceptance,
   and is reviewed at 360 first.
7. No `transform` on a card or a button. No shadow outside the five overlay components.
8. **Buttons must survive two lines**, label centred, never ellipsised.

### The inventory

| # | Component | Variants | Notes |
|---|---|---|---|
| 1 | `Button` | primary · secondary · tertiary · icon | §3.1 |
| 2 | `Field` | text · email · tel · textarea · number | §3.2 — the wrapper that owns label, control, help, error |
| 3 | `Select` · `Combobox` | — | native `<select>` for ≤7 options; `Combobox` only for country |
| 4 | `Checkbox` · `Radio` · `RadioCard` | — | consent checkbox is a `Checkbox`, required |
| 5 | `SegmentedControl` | 2–4 segments | `LanguageSwitcher` is an instance — §3.5 |
| 6 | `Slider` | single | calculator only; **paired stepper buttons, WCAG 2.5.7** |
| 7 | `Stepper` | — | number entry without dragging |
| 8 | `FileUpload` | — | portal only |
| 9 | `Badge` | neutral · accent · status | §3.6 |
| 10 | `Chip` | static · removable · filter | §3.7 |
| 11 | `Card` | default · feature · linked | equal-height in a row, always |
| 12 | `TariffCard` | **five**: inspection · express · annual · annual-leading · special | §3.9 |
| 12a | `PriceSlot` | amount · phrase | §3.9 — the price line, which for Special holds words, not a number |
| 13 | `PricingBand` | one-off · annual · special | the row that owns equal-height and the badge reserve |
| 14 | `PriceCalculator` | — | **§3.9a** — two sliders + steppers, live result, arithmetic shown |
| 15 | `ReportSheet` | full · guest | §3.10 — the product |
| 16 | `ReportPreview` | — | the cropped hero object |
| 17 | `VerificationRail` | inline · column | §3.11 |
| 18 | `GpsVerification` | — | coordinates + `PlotDiagram` + map link. We serve no map tiles |
| 19 | `Gallery` | grid · lightbox | §3.14 — **not a carousel** |
| 20 | `ComparisonPair` | — | two stacked 4:3 frames, `On arrival` / `After the work`. No drag wipe |
| 21 | `VisitListRow` | — | portal list |
| 22 | `FamilyMemberRow` | owner · manager · member · guest | §3.18 |
| 23 | `PermissionMatrix` | — | the only table permitted below 600px, with a frozen column and a DL equivalent |
| 24 | `Accordion` | single · multi | §3.16 — the FAQ |
| 25 | `Tabs` | — | portal only; never for pricing |
| 26 | `Modal` · `Drawer` · `BottomSheet` | — | §3.15 |
| 27 | `Lightbox` | — | gallery only |
| 28 | `Toast` | neutral · error | §3.17 |
| 29 | `ErrorPanel` | inline · page | 3px inline-start rule + glyph + sentence |
| 30 | `ErrorSummary` | — | `role="alert"`, receives focus on failed submit, links to each field |
| 31 | `EmptyState` | — | ships with **no illustration prop and no icon prop** |
| 32 | `SiteHeader` | — | §3.3 |
| 33 | `MobileMenu` (Drawer instance) | — | §3.4 |
| 34 | `MobileActionBar` | — | `base`–`sm`; hides while a field has focus |
| 35 | `SiteFooter` | — | contacts on every page (bank requirement + WCAG 3.2.6) |
| 36 | `SkipLink` | — | first in DOM, `--mc-z-skiplink` |
| 37 | `Breadcrumb` | — | portal + legal pages |
| 38 | `Pagination` | — | portal visit history |
| 39 | `ProgressRail` | — | "what happens next" |
| 40 | `StepStrip` | — | checkout |
| 41 | `Divider` | rule · medallion | medallion at most 4× on the home page |
| 42 | `BulletPetal` | — | list bullet, the one place the petal is used as furniture |
| 43 | `PullQuote` | — | About only |
| 44 | `Tooltip` | — | definitions only; every tooltip's content is also present as visible text somewhere |
| 45 | `CookieBanner` | — | **does not exist.** No third-party analytics at launch, therefore nothing to consent to |
| 46 | `Carousel` | — | **does not exist.** §3.14 |

`Testimonial`, `StatCounter`, `PartnerLogoWall`, `ReviewStars` and `Countdown` are **not in the
inventory and must not be added** — each is a component whose only purpose is to display something
this company does not have. FINDINGS #1, #2 and #22 are all the same defect: a component existed, so
someone filled it.

### 3.1 Button

**Anatomy:** `[optional leading icon 20px] · label · [optional trailing icon]`, `gap: size-2`,
`padding-inline: size-6`, `min-block-size: 48px` (44 from `lg`), `radius-sm`, label `type.label`.

| Variant | Rest | Hover | Active | Focus-visible | Disabled | Loading |
|---|---|---|---|---|---|---|
| primary | Dark Olive fill, Ivory label (**14.17**) | fill `#2F3021` (Ivory on it 11.79) | fill `#171808` | inner Ivory ring at `-3px` + 4px `alpha-deepolive-16` halo | fill `alpha-dark-12`, label `text-disabled`, `aria-disabled`, cursor default | label stays, 2px 24px accent arc replaces the leading icon, `aria-busy`, width frozen |
| secondary | transparent, 1px `border-accent`, `text-accent` label | bg `alpha-deepolive-08` | bg `alpha-deepolive-16` | standard 2px ring, 2px offset | border `alpha-dark-16`, label `text-disabled` | as above |
| tertiary | `text-accent`, 1px underline at 0.12em offset | `link-hover`, underline thickens to 2px | `olive-900` | standard ring | `text-disabled`, no underline | not applicable — a tertiary link never performs work |
| icon | 44×44, `text-accent` glyph | `alpha-deepolive-08` disc | `alpha-deepolive-16` | standard ring | `text-disabled` | as primary |

On `.mc-on-dark` the scope rewrite gives: primary = Nude fill with a Dark Olive label (12.93);
secondary = 1px `alpha-ivory-45` border with a Nude label. **The component stylesheet is unchanged.**
That is the whole point of the scope: nobody writing a button needs to know Deep Olive is banned on
the dark ground.

Label ceiling: 22 ref / 30 hy / 28 ru graphemes, **wrap to two lines, button grows, never ellipsis**.

### 3.2 Field — the form primitive

**Anatomy, in DOM order:**

```
<div class="mc-field" data-state="…">
  <label for=ID>            visible, always, type.label, never a placeholder
  <p id=HELP>               optional, type.caption, before the control
  <input id=ID
         aria-describedby="HELP ERR"
         aria-invalid="true|false"
         autocomplete=…  inputmode=…  type=…>
  <p id=ERR role="alert">   glyph + sentence, type.caption, text-feedback-error
```

The audit found **zero labels on the entire site** and placeholder-only fields (FINDINGS #10), and
focus states so absent that the empty and focused screenshots were byte-identical (FINDINGS #24).
Both are structural here: the label is a required prop with no "hidden" option, and the focus ring
is applied by a global `*:focus-visible` rule that no component may unset.

| State | Border | Ground | Extra |
|---|---|---|---|
| default | 1px `border-strong` `#737060` (**3.99**) | `surface-object` | — |
| hover | 1px `text-secondary` `#5C5C50` (5.43) | — | — |
| focus-visible | 2px `border-focus` | — | plus the global 2px ring at 2px offset |
| error | 2px `border-feedback-error` | — | glyph + sentence + `aria-invalid` |
| disabled | 1px `alpha-dark-12` | `surface-sunken` | `aria-disabled`, never `disabled` on a field the user must fix |
| readonly | none | transparent | value in `text-primary` |
| loading | default | — | `aria-busy` on the fieldset, not the input |

**Validation timing is a system rule, not a developer choice:** never on keystroke; on blur only if
the field was already errored; on submit for everything. On failed submit, focus moves to
`ErrorSummary` (`role="alert"`), which lists each error as a link to its field.

**Typed inputs.** `email` → `type="email" inputmode="email" autocomplete="email"`.
Phone → `type="tel" inputmode="tel" autocomplete="tel"` with a `CountrySelect` on the inline-start;
accepts `+1 818 555 0134`, `+33 6 12 34 56 78`, `+374 93 154 108` and `093154108`; stores E.164;
**never rejects a paste** (WCAG 2.2 3.3.8). The audit found `type="text"` on both (FINDINGS #10).

**Error copy is a system constraint:** never `Oops`, `Something went wrong`, `Error`, `Invalid`,
`Failed`, `Required field`; never an emoji; never an exclamation mark. An error says what to do:
*"Enter a phone number we can reach you on, including the country code."*

**The form is never inside `.mc-on-dark`** — §2, Rule 3.

### 3.3 SiteHeader

**Anatomy:** skip link · logo (mark + live wordmark, never a cropped raster) · primary nav ·
`LanguageSwitcher` · phone link · primary CTA · menu button.
Height **56px** below `md`, **72px** from `md`. Ground `surface-object` (Ivory) inside
`.mc-on-ivory`, so floating layers under it take Nude and never open Ivory-on-Ivory.
**The 1px block-end rule is permanent at every width and every scroll position** — not
scroll-triggered, which removes a scroll listener from the critical path.

- Below `md`: logo · menu button (48×48). The CTA lives in `MobileActionBar`, not the header.
- From `md`: full nav, no drawer, no submenu that opens on hover alone.
- **No dropdown submenu at all.** The audit found five invisible-but-focusable submenu links, three
  of which led to 404s (ACCESSIBILITY §3). A nav item is a link to a page that exists.
- `aria-current="page"` on the active item; a 2px `border-accent` block-end rule renders it, so the
  state is not colour-only.

### 3.4 MobileMenu

A `Drawer` instance, inline-end, full-height, `surface-ground`, `radius-overlay` on the leading
corners only.

- Opens on click/tap of the menu button; `aria-expanded` on the button, `aria-controls` to the panel.
- **Focus moves into the panel on open and returns to the button on close.** Focus is trapped while
  open. Escape closes. Scrim click closes. `<body>` gets `overflow: hidden` with the scroll position
  preserved and restored.
- **The `LanguageSwitcher` is inside the panel, first, above the nav list** — FINDINGS #27: on the
  current site opening the menu hides the only way to change language, on the viewport where the menu
  *is* the navigation.
- Contacts (both phones as `tel:`, `info@memorycare.am` as `mailto:`) at the foot of the panel.
- Enter: `translateX(100% → 0)` over `--mc-motion-enter`; exit over `--mc-motion-exit`; scrim fades.
  Under reduced motion the translate distance is 0 and only the opacity remains.

### 3.5 LanguageSwitcher

A `SegmentedControl` with three segments: **`ՀԱՅ · ENG · РУС`**, each written in its own script,
never flags, never transliterations.

- Markup: a `<nav aria-label>` of three `<a>` elements, each pointing at the same document in the
  other locale, each carrying `hreflang` and `lang`. **They are links, not buttons** — a locale is a
  URL, and a shared link must never be silently redirected (FINDINGS #15, #17, #18).
- Active segment: `surface-accent-strong` fill + `text-on-accent` label (14.17) **plus
  `aria-current="true"`**. Inactive: `text-secondary` (5.43).
- **Each segment is ≥44×44 with its padding**, and ≥8px of clear space between them. The audit
  measured 33.2×22.5, 28.7×22.5 and 32.3×22.5 — the control a diaspora visitor reaches for first was
  the hardest to hit on the site (ACCESSIBILITY §5).
- The focus ring is never removed from a segment.

### 3.6 Badge

`min-block-size: 24px`, `padding-inline: size-3`, `radius-sm`, `type.rail` (14px — the informational
floor; the lead's polish pass found 12 and 13px badges and raised them all).

| Variant | Ground | Label | Use |
|---|---|---|---|
| neutral | `surface-sunken` | `text-primary` (11.46) | metadata |
| accent | `surface-accent-strong` Dark Olive | `text-on-accent` Ivory (**14.17**) | the leading tariff — `Our recommendation`, never `most chosen`, never `bestseller` |
| status | `surface-sunken` + a glyph | `text-primary` | visit status |

**There is no Olive-fill badge with a label, at any size** (3.42 / 4.14). There is no `warning` badge
and no `danger` badge — those names are banned; the states they described are `neutral` plus a word.
Label wraps to two lines, never ellipsis.

> Prior art put the accent badge on a **Deep Olive** fill with an Ivory label at 6.01. I moved it to
> **Dark Olive at 14.17**, matching the primary button's new fill. One fewer dependency on an
> unratified value, and the badge and the button now read as the same system.

### 3.7 Chip

`min-block-size: 32px` visual, **44×44 hit area via `.mc-hit-44`**, `radius-sm`, `type.body-sm`.
Variants: static (a fact — "4 visits a year"), removable (portal filters, with a 44×44 remove button
carrying its own `aria-label`), filter (`role="button" aria-pressed`).
Selected filter chip: `border-accent` 2px + `text-accent` — **plus a check glyph**, because a border
weight change alone is a colour-adjacent signal.
The chip is the one place `--mc-decor-sky-tint` is permitted on a light ground, as a ground for a
static informational chip: Sky at 18% over Ivory is `#E5EBE9`, text-primary on it **13.36**.

### 3.8 Card

`surface-object` + 1px `border-default` + `radius-sm` + `padding: size-5 / size-6 / size-8`.
**Cards in a row are equal height, always** (lead-ruled): the row is a grid, every child is
`display: flex; flex-direction: column`, and the action is pushed to the foot by a growing spacer —
never by hand-tuned padding, so the alignment survives a copy change and a locale change.
A linked card uses a stretched `::after` at `--mc-z-raised`; nested interactive elements inside one
are forbidden, and the linter checks for them.
No hover lift, no shadow, no `transform`. Hover is a `border-default → border-decorative` change.

### 3.9 TariffCard — five variants

`variant: "inspection" | "express" | "annual" | "special"` · `emphasis: "leading" | null` ·
`period: "year" | "one-off" | null` — **there is no `"month"`**.

**There is no visit-kind breakdown in this anatomy, and the prop that would carry one does not
exist.** The light-visit / heavy-visit distinction was rejected by the owner on 26.08 — *"все визиты
полноценные"*. The card carries a **single count of full visits** (`visitCount: number | null`) and
the words `light visit`, `heavy visit` and `preventive visit` are on the string denylist, so a
comparison table cannot reintroduce the split through copy either. This is the one place where
removing a prop is the specification: if the card *could* express two kinds of visit, some future
pricing page will.

**Anatomy, in DOM order:**

```
badge slot            reserved 46px whether or not a badge is present
product name          type.heading-2 · ceiling 14 ref / 20 hy / 18 ru · overflow none
one-line description  type.body-sm · clamp 2 lines
PriceSlot             see below — the only part that varies structurally between the five
period                type.caption — "a year" | "one-off" | absent
visit count           type.body — "4 full visits, one in each season" · one number, from products.json
inclusion list        BulletPetal items · type.body · wrap, no clamp
spacer                flex: 1
button                primary on the leading card, secondary on the others
footnote slot         type.caption — credit rules, optional
```

**`PriceSlot`, the sub-component the fifth product forced into existence.**

| Variant | Renders | Type |
|---|---|---|
| `amount` | `.mc-price__amount` (tabular figures, display face) + `.mc-price__unit` `֏ AMD` beneath | `type.price` + `type.body` |
| `phrase` | one string from the string file — *"Priced after an inspection"* — **with no `֏`, no `AMD`, no digits and no currency element at all** | `type.heading-3`, `text-primary` |

The `phrase` variant is not a styling flag; it is a different element tree. The amount variant's
tabular-figure rule, its currency binding and its `{price}` placeholder are all absent, so there is
no path by which a Special card can render a number, a stray `֏`, or the string `0 ֏`. Both variants
occupy the same block-size (`min-block-size` = the amount variant's rendered height at that
breakpoint), so the five cards' inclusion lists still start on one line. **A `phrase` price is never
styled to look cheaper or lighter than an amount** — same weight, same colour, same slot: Special is
a product, not a fallback.

**The five cards on the page.**

| Card | Variant | Period | Badge | Band |
|---|---|---|---|---|
| Զննում / Inspection | `inspection` | one-off | — | `PricingBand--one-off`, above a `Divider--rule` |
| Էքսպրես / Express | `express` | one-off | — | `PricingBand--one-off` |
| Օպտիմալ / Optimal | `annual` | year | **`Our recommendation`** | `PricingBand--annual` |
| Մաքսիմում / Maximum | `annual` | year | — | `PricingBand--annual` |
| Հատուկ խնամք / Special | `special` | — | — | `PricingBand--special`, below the annual row, full width |

- **Inspection is set apart structurally, not decoratively** — it is a one-off, not a subscription,
  and it reads that way because it sits in a different band above a rule, with `period: "one-off"`.
  Express sits with it: both are one-off products, and grouping them is what makes the annual row
  legible as a subscription row.
- **Special sits below the annual row, full width, not as a fifth column.** It has no price to
  compare, so putting it in a price comparison row invites the reader to compare it. Its own band
  also carries the sentence the owner requires — Special always begins with a Զննում — as a
  `footnote`, and its button is secondary, labelled for a conversation, not a purchase.
- **The leading card is marked three ways:** a 2px `border-accent` instead of the 1px
  `border-default`, the accent `Badge`, and a primary button where the others are secondary. Never a
  fill, never a scale change, never a shadow. The badge reads **`Our recommendation`** (Armenian
  `առաջատար`) — never `most chosen`, never `bestseller`: the company has zero customers and those are
  claims about behaviour that has not happened. Both words are on the build-failing denylist.
- **Every amount renders both `֏` and `AMD`** — a bank requirement — split across two elements per
  §4.6 R2, with `֏` bound to `--mc-font-currency`.
- **No `line-through` on any price, ever** (build failure), and no `save` / `discount` / `offer` /
  `%` / `was` / `instead of` within 80 characters of a price. There is no discounted repeat Express:
  the price is always 65,000 ֏, the withdrawn 40,000 must not survive anywhere, and the denylist is
  what stops it reappearing as a struck-through "was".
- **Credit rules render as a `footnote` on the card that earns them**, from `products.json`, never as
  free copy: 60-day window; **one credit only** — either the Զննում or the Express, whichever is
  larger, never both; no credit between one-off products; Զննում credits only into an annual
  subscription, never into an Express.
- Breakpoints: one-off band 1-up below `sm`, 2-up from `sm`. Annual band 1-up below `sm`, 2-up from
  `sm`, one row from `md`. Special band full width at every size. Equal height applies within a band,
  never across bands — the two bands are different rows and aligning them would re-merge the
  distinction the layout exists to make.

### 3.9a PriceCalculator

An owner decision of 26.08, not an option: *"an open formula on the site, two sliders; the price is
the same for everyone and visible before anyone has to call."* It is the single most
brand-specific component in this system — a company that photographs graves for families abroad is
selling verifiability, and a published formula is verifiability applied to its own price.

**The formula, published on the page in words as well as computed:**

| Parameter | Standard, included | Added to an annual subscription | Added to a one-off Express |
|---|---|---|---|
| Area | up to **16 m²** | **+10,000 ֏ / year** per m² over 16 | **+2,500 ֏ / visit** per m² |
| Monuments | up to **2** | **+30,000 ֏ / year** each over 2 | **+7,500 ֏ / visit** each |

Slider ceilings: **100 m²** and **10 monuments**. Above either, the calculator stops computing and
routes to a consultation that begins with a Զննում. The surcharges are flat and identical for
Optimal and Maximum. The internal logic is worth showing the reader because it is the argument:
160,000 ÷ 16 m² = exactly 10,000 ֏ per m² per year — **an added metre costs exactly what an included
metre costs** — and the one-off surcharge is the annual one ÷ 4.

**Anatomy:**

```
overline + heading
tier control            SegmentedControl — Optimal | Maximum | Express (one-off)
area                    Slider (16→100 m², step 1) + Stepper + Field, all bound to one value
monuments               Slider (2→10, step 1)  + Stepper + Field, all bound to one value
result                  output — base + area surcharge + monument surcharge, each line shown
                        as arithmetic, then the total in a PriceSlot--amount
ceiling state           replaces the result when a slider is at its ceiling: one sentence
                        + a secondary button to the consultation
footnote                the flat-rate sentence, the 16 m² / 2 monument standard, "same price
                        for everyone, in Yerevan and in Los Angeles"
```

- **The arithmetic is shown, not asserted.** Four lines — base, area, monuments, total — each with
  its own operand. A single total is a number the reader must trust; four lines are a calculation the
  reader can check, which is the entire point of publishing the formula.
- **The total never animates and never counts up.** It replaces instantly. A rolling numeral on the
  price of caring for a family grave is the wrong register, and it is on the forbidden-motion list.
- **`aria-live="polite"` on the result region**, and the result is `<output for="area monuments">`.
- **Every slider is paired with a `Stepper` and a numeric `Field`** — three controls, one value.
  WCAG 2.2 2.5.7: dragging can never be the only way. Arrow keys step 1, PageUp/PageDown step 10,
  Home/End jump to the ceilings; the thumb has a 44×44 hit area and a focus ring that is never
  removed.
- **Handoff to the form is a contract, not a component:** URL state `?tier=&area=&monuments=`, mirrored
  into hidden fields on the consultation form, so nothing already given is asked again
  (WCAG 2.2 3.3.7).
- **The calculator and the refund table import the same arithmetic module**, asserted by the import
  graph. Two implementations of one formula is how a published price stops matching the invoice.
- States: `default` · `at-ceiling` · `loading` (impossible — the arithmetic is local and synchronous;
  stated) · `error` (impossible for the same reason; an out-of-range value clamps) · `empty`
  (the standard plot: both sliders at their included values and the result equal to the list price —
  which is the state it opens in, and it is the most persuasive one).
- Breakpoints: sliders stacked below `md` (one of the two documented `max-width` exceptions), two
  columns from `md` with the result on the inline-end, result sticky within the section at `lg`.
- **The calculator sits on Nude, never in a dark band** — it contains `Field`s, so §2 Rule 3 applies.

### 3.10 ReportSheet — the product

Ground `surface-object`, **`radius-0`**, 1px `border-default`, padding `size-5` / `size-10` at `md`+.
It is a document, so it has square corners; every other object in the system has 2px, and the
difference is the point.

**Block order is fixed and owner-ruled:** confirmation line → `VerificationRail` → `GpsVerification`
as its own block → photographs grouped `On arrival` before `After the work`, chronological → crew
note → recommendations → share bar. **The after-image is never the opening image**, and there is no
before/after wipe or drag slider anywhere (also WCAG 2.5.7).

States: `default` · `loading` (the rail's label/value pairs render, values as 1em-tall
`surface-sunken` blocks — **no shimmer**) · `empty` (impossible: a report exists or the route 404s —
stated) · `error` (`ErrorPanel`, page-level) · `guest` (see below).

**`variant: "guest"` is a server-side variant, not a CSS one.** It renders no price, no next-visit
date, no subscription name and no recommended-work figures, and that is asserted against the *server
response*, not the DOM. The route carries `X-Robots-Tag: noindex, nofollow`. `<title>` is
`Visit report — {date}` and nothing else; `og:description` contains no cemetery, no plot label and
no name. **The deceased's name is off by default** and turning it off removes the name from
previously issued links.

**No animation of any kind on the report sheet, on a bad-news screen, or on a guest view.**

### 3.11 VerificationRail

`type.rail` — **14px, owner-ruled, not 11 or 12.** It carries the proof: date, cemetery, sector,
plot, crew, coordinates. It was the least legible type in the previous system carrying the most
important content in the product.

Anatomy: a `<dl>` of label/value pairs, 1px `border-default` rules between rows, `radius-0`.
Labels `text-secondary`, uppercase in Latin and Cyrillic, **sentence case in Armenian** (`:lang(hy)`
branch — Armenian caps read as shouting). **Values are `text-primary`, never `text-secondary`, and
never uppercase in any script**: proof is primary text.

Breakpoints: below `lg` it is a full-width block above the photographs. From `lg` it becomes a
`222px` right column, sticky with `top: calc(var(--mc-layout-header-height) + var(--mc-size-4))`.
**DOM order does not change** — CSS reorders, so the reading order stays the reading order and no
`tabindex` is needed anywhere.

### 3.12 GpsVerification

Coordinates in `type.numeric` (tabular, so digits do not jitter) · `PlotDiagram` (our own vector
bearing rose, `radius-0`) · a map **link** that opens the coordinates in the visitor's own map app.
**We serve no map tiles**: a tile is a third party's brand on our proof, a third-party request on a
page the bank will review, and a cookie we would then have to disclose. The audit found an untitled,
unconsented Google Maps iframe on the contact page (FINDINGS #33); it does not come back.

### 3.13 Family-circle member row

**Anatomy:**

```
[avatar disc 40px, radius-full — initials in type.label on surface-sunken; never a photo]
name            type.body, text-primary
role Badge      neutral — Owner · Family manager · Family member · Guest
contact         type.caption, text-secondary — email or masked phone
[status]        "Invited 3 days ago" — type.caption, text-secondary
[menu button]   44×44 icon button, aria-label "Actions for {name}"
```

- Row `min-block-size: 64px`, 1px `border-default` block-end rule, `radius-0`, ground inherits.
- States: `active` · `invited` (pending — the name slot shows the email, the role badge is present,
  and the actions are *Resend invitation* / *Cancel invitation*) · `expired` · `removing` (loading,
  `aria-busy`) · `error` (an inline `ErrorPanel` beneath the row, not a toast) · `self` (the current
  viewer — the menu offers no *Remove*).
- **Empty state:** the family circle with one member is the normal first state, not an error. The
  empty state is a single sentence and one secondary button, no illustration.
- **No transition on the avatars.** No hover reveal of the action menu — the menu button is
  permanently visible, because the audit's single most repeated pattern was affordances that exist
  only for a pointer.
- Below `sm` the row wraps to two lines (name + badge / contact + menu) and keeps its 64px floor.

### 3.14 Carousel — there isn't one

**Decision: no carousel ships, on the marketing site or in the portal.** Reasons, in order of weight:

1. The one on the current site does not advance when its control is pressed (FINDINGS #23), its
   buttons have no accessible name (`button-name`, critical), its arrows measure 27×44, and its
   English captions sit unscrimmed on a photograph at **3.20** against a required 4.5 (FINDINGS #12).
   Every one of those is a normal carousel failure, not an unusual one.
2. It is the most expensive component on the page: Swiper is 151 KB, and the English slide set alone
   makes that page 1 MB heavier than the Armenian one (PERFORMANCE).
3. Auto-advance is already forbidden, and a carousel nobody advances is a stack of hidden content.

**What replaces it:**
- Marketing imagery → a static `Gallery` grid, 1-up below `sm`, 2-up at `sm`, 3-up at `md`, each
  image `3:2` at 1800×1200, `radius-0`, intrinsic `width`/`height` on every one.
- Report photographs → `Gallery` + `Lightbox`, `4:3` at 1600×1200, grouped and captioned.
- Before/after → `ComparisonPair`: two stacked 4:3 frames, identical framing, labelled
  `On arrival` / `After the work`. **No drag slider** — it is also a WCAG 2.2 2.5.7 dragging failure
  and it hides half the proof behind a gesture.
- Any text over a photograph → it doesn't. Captions sit **beneath** the frame on the page ground.
  There is no scrim token in this system because there is no text on an image.

### 3.15 Modal · Drawer · BottomSheet

One implementation, three presentations. `radius-overlay` (8px) — the only 8px in the system, because
an overlay is a different plane and may say so. `--mc-elevation-overlay`. Scrim `alpha-dark-72`.

`role="dialog" aria-modal="true"`, labelled by the title id. Focus moves in on open and returns to
the invoker on close. Focus is trapped. Escape closes. `<body>` locks with the scroll position
preserved. Scrim click closes **except** where the dialog holds unsaved input, where it prompts.
Modal max-inline-size 560px; below `sm` a modal becomes a `BottomSheet` with a 36×4 drag handle
**and a 44×44 close button**, because the handle is a dragging gesture and cannot be the only way out.

**Never used for:** errors (inline), success (a toast or an inline panel), marketing, or anything a
visitor did not ask for. There is no interstitial and no newsletter modal.

### 3.16 Accordion

The FAQ, the report's recommendation detail, and the legal pages' section navigation. Nowhere else —
an accordion is never used to hide something a visitor needs in order to buy.

`<button aria-expanded aria-controls>` inside an `<h3>`; panel `role="region"` labelled by the
button. `single` and `multi` variants; `single` is not a radio group and every panel can be closed.
Chevron rotates 180° over `--mc-motion-expand`; **the rotation is not the state** — `aria-expanded`
and a `border-accent` inline-start rule on the open item carry it.

Open/close animates `grid-template-rows: 0fr → 1fr` plus opacity — not `height`, which forces layout
every frame and is the standard way an accordion becomes an INP failure. Under reduced motion the
duration collapses to 1ms and the panel simply appears.

### 3.17 Toast

`radius-sm`, `surface-float`, 1px `border-strong`, `--mc-elevation-overlay`, max-inline-size 420px,
`--mc-z-toast`. Region is `role="status"` (`aria-live="polite"`); the error variant is `role="alert"`.
Two variants only: `neutral` and `error`. There is no success toast and no warning toast — a
completed payment, a sent invitation and a moved visit are all `neutral` plus a sentence.

**Toasts never carry information the user needs to keep.** A failed payment, a bounced invitation and
a cancelled visit are inline panels or screens. A toast is dismissible, has a 44×44 close button, and
is never the only place something is said. Auto-dismiss is 6s and is paused on hover, on focus, and
whenever `prefers-reduced-motion` is set.

### 3.18 Everything else, in one line each

`Select` — native below 8 options; the menu takes `surface-float`.
`Combobox` — country only; `role="combobox" aria-expanded aria-controls aria-activedescendant`.
`Checkbox` / `Radio` — 24×24 visual, 44×44 hit area, 2px `border-strong`, checked =
`surface-accent-strong` fill + Ivory glyph; the consent label **wraps freely** (Armenian consent copy
runs three lines on a phone).
`Slider` — 4px track `border-strong`, fill `surface-accent-strong`, 28×28 thumb with a 44×44 hit
area, **and a paired `Stepper`, always**, because a slider alone is a dragging-only control.
`ProgressRail` — `aria-current="step"`, dots + labels, never colour-only.
`EmptyState` — no illustration prop, no icon prop; a sentence and at most one action.
`SkipLink` — first focusable element on every page; the audit's first tab stop was an unlabelled
back-to-top image (ACCESSIBILITY §3).
`SiteFooter` — both founders' names and phones as `tel:`, `info@memorycare.am` as `mailto:`, the
legal address, `MemoryCare LLC`, the registration number, and links to the four legal pages, **in the
same place on every page** (bank requirement, and WCAG 2.2 3.2.6 Consistent Help).

---

## 4. Typography

### 4.1 What changed, and why it unblocks the build

The 31.08 brandbook retires Gloock and Gill Sans. That removes both of the blocking issues recorded
on 29.08 — there is no longer a commercial Monotype licence to buy, and both new faces are shown in
the book covering **Latin, Cyrillic and Armenian** (Aa / Аа / Աա).

> **Override of prior art.** `FINAL-SYSTEM §6.4 R4` rules that `hy` and `ru` headings fall back to
> the text face at 600 because the display face covers Latin only. **If the book is right, that rule
> is repealed** and Ghea Mariam sets headings in all three scripts. R4 survives as the *degraded
> path*, selected automatically by the CI test in §4.6 rather than by anyone's judgement — because
> "the brandbook shows a sample" is not the same as "the file we can license contains the range".

Faces: **Display — Ghea Mariam. Text — Montserrat, with Montserrat Arm as a separate family for
Armenian.** Montserrat Arm is a distinct family, not a subset of the Latin one: the stack must name
it explicitly.

### 4.2 The scale

| Role | Face | 360 → 1440 | `clamp()` | LH | Tracking | Weight |
|---|---|---|---|---|---|---|
| `display-1` | display | 32 → 56 | `clamp(2rem, 1.5rem + 2.222vw, 3.5rem)` | 1.08 | −0.01em | 400 |
| `display-2` | display | 28 → 44 | `clamp(1.75rem, 1.4167rem + 1.4815vw, 2.75rem)` | 1.12 | −0.005em | 400 |
| `heading-1` | display | 26 → 36 | `clamp(1.625rem, 1.4167rem + .926vw, 2.25rem)` | 1.18 | 0 | 400 |
| `heading-2` | display | 24 → 28 | `clamp(1.5rem, 1.4167rem + .37vw, 1.75rem)` | 1.24 | 0 | 400 |
| `heading-3` | **text** | 18 → 20 | `clamp(1.125rem, 1.0833rem + .185vw, 1.25rem)` | 1.35 | 0 | 600 |
| `body-lg` | text | 17 → 19 | `clamp(1.0625rem, 1.0208rem + .185vw, 1.1875rem)` | 1.6 | 0 | 400 |
| `body` | text | **16 → 17** | `clamp(1rem, .9792rem + .093vw, 1.0625rem)` | 1.6 | 0 | 400 |
| `body-sm` | text | 15 | `.9375rem` | 1.55 | 0 | 400 |
| `label` | text | 15 | `.9375rem` | 1.4 | 0.01em | 600 |
| `caption` | text | 14 | `.875rem` | 1.45 | 0.01em | 400 |
| `rail` | text | **14** | `.875rem` | 1.4 | 0.06em | 600 |
| `overline` | text | **13** | `.8125rem` | 1.3 | 0.12em | 600, uppercase |
| `price` | display | 28 → 40 | `clamp(1.75rem, 1.5rem + 1.111vw, 2.5rem)` | 1.0 | −0.01em | 400 |
| `numeric` | mono | 14 | `.875rem` | 1.5 | 0.02em | 400 |

**Every `clamp()` preferred term contains a `rem`.** A clamp expressed purely in `vw` does not
respond to the browser's text-size setting and fails WCAG 1.4.4; the `rem` component is what makes
these safe. Combined with removing `user-scalable=no` (FINDINGS #7), the reader gets both zoom paths
back.

**Floors, and why each is where it is.** 16px is the body and input floor — below 16, iOS zooms the
viewport on focus, and the audit measured 225 elements at 15px and 132 at 14px on a site whose
audience is 35–60. 14px is the informational floor: anything a reader must understand. 13px is the
absolute floor, permitted only for `overline` — decorative, uppercase, tracked, never data. Nothing
in the product, including the tagline and the PDF, is smaller than 13px. The audit found one 12px
string at 1.51 contrast, which is both the smallest and the least legible type on the site
(FINDINGS #39); the floor exists so that combination cannot recur.

### 4.3 Font stacks, per locale — and the ֏ slice, exactly

```css
--mc-font-display:
  "MC Dram", "Ghea Mariam", "Ghea Mariam Fallback", Georgia, "Times New Roman", serif;
--mc-font-text:
  "MC Dram", Montserrat, "Montserrat Arm", "Montserrat Fallback",
  system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
--mc-font-currency:
  "MC Dram", "Noto Sans Armenian", "Montserrat Arm", sans-serif;
--mc-font-mono:
  ui-monospace, "SF Mono", "Cascadia Mono", "Roboto Mono", Menlo, monospace;
```

**The declared ranges, per family. These are the specification, not an illustration.**

| Family | `unicode-range` | Loads on |
|---|---|---|
| `MC Dram` | **`U+058F`** — one codepoint, nothing else | **all three locales** |
| `Ghea Mariam` (Latin) | `U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+2000-206F, U+2122, U+2191, U+2193, U+2212` | en |
| `Ghea Mariam` (Cyrillic) | `U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116` | ru |
| `Ghea Mariam` (Armenian) | **`U+0531-058A, U+FB13-FB17`** — note the range **stops at U+058A** | hy |
| `Montserrat` (Latin) | `U+0000-00FF, U+0100-017F, U+2000-206F` | en, and the Latin runs inside hy/ru |
| `Montserrat` (Cyrillic) | `U+0400-04FF, U+0500-052F` | ru |
| `Montserrat Arm` | **`U+0531-058A, U+FB13-FB17`** — **stops at U+058A** | hy |

**The one-codepoint slice, and why the ranges above stop at U+058A.**

The corrected language rule is about **words, not symbols**: the English and Russian locales carry no
Armenian *words* — no product names in Armenian letters, no untranslated labels — but **֏ appears in
all three, because it is the sign for the currency the client is actually charged in.** ֏ is U+058F,
which sits in the Armenian Unicode block, so a naive reading of "one script per locale" would forbid
the character the same brief mandates. It does not, and the font architecture is what makes the
distinction real rather than rhetorical.

Three properties, and all three are needed together:

1. **`MC Dram` declares `unicode-range: U+058F` — a single codepoint.** A browser downloads a face
   only when the rendered text contains a codepoint inside its declared range. The English page
   contains exactly one such codepoint, `֏`, and only in price units, so `mc-dram.woff2` is fetched
   on `/en/` and `/ru/` **and nothing else Armenian is.** It is a one-glyph subset, ≤ 2 KB.
2. **The Armenian ranges of `Ghea Mariam` and `Montserrat Arm` deliberately stop at `U+058A`**, one
   codepoint short of the block's `U+058F`. If they ran to `U+058F`, an English page containing a
   price would fall inside `Montserrat Arm`'s range and **download the entire Armenian text face —
   26 KB of letterforms to draw one currency sign** — and, worse, the two families would both claim
   ֏ and which one won would depend on declaration order rather than on a decision. Truncating the
   range at U+058A makes `MC Dram` the only possible source of ֏ in every locale, deterministically.
   `U+058B–U+058E` are unassigned or unused symbols and losing them costs nothing.
3. **`MC Dram` is first in all three text-bearing stacks.** Family order only decides ties; since no
   other family in the stack declares U+058F after rule 2, there is no tie. It is first anyway, so
   that the intent is legible in the token file and so the arrangement survives someone adding a
   family later.

**Consequences worth stating.** On `/en/` the total Armenian-block cost is 2 KB and one glyph. On
`/hy/` the same 2 KB file serves the same glyph, and the Armenian text face never has to carry it —
so if Montserrat Arm turns out to lack ֏ (unverified, §4.6), **nothing changes, in any locale.** And
because `.mc-price__unit` is set in the text face while `.mc-currency` is set in
`--mc-font-currency`, the sign and the letters `AMD` sit side by side from two files without anyone
being able to see the seam — which is precisely the defect the audit measured on the live site, where
`֏` fell to a system face and rendered "visibly smaller and lighter than the digits beside it"
(FINDINGS #21).

**Every stack terminates in a generic family, and every `@font-face` declares an explicit
`unicode-range`**, so a codepoint outside a declared range is never requested from that file and a
missing glyph falls to the next family instead of rendering as tofu. No stack can dead-end.
`Montserrat` and `Montserrat Arm` are two families with disjoint ranges, so listing both costs
nothing on `/en/`.

### 4.4 Loading strategy

**Self-hosted, always. Zero requests to `fonts.googleapis.com` or `fonts.gstatic.com.`** Part of the
audience is in Russia, where Google Fonts is unreliable; the bank's review disliked third-party
requests; and the current site loads Plus Jakarta Sans across 200–800 in roman *and* italic, a face
that carries no Armenian at all, which is why the primary market's script currently renders in
whatever the device happens to have (PERFORMANCE).

**Weights shipped — six files, and no others exist:**

| Family | Weights | Ranges | Subset | Budget |
|---|---|---|---|---|
| Ghea Mariam | 400 | Latin + Latin-ext + punctuation; Cyrillic and Armenian **if §4.6 passes** | yes | ≤ 42 KB |
| Montserrat | 400, 600 | `U+0000-00FF, U+0100-017F, U+2000-206F` | yes | ≤ 30 KB each |
| Montserrat (Cyrillic) | 400, 600 | `U+0400-04FF, U+0500-052F` | yes | ≤ 22 KB each |
| Montserrat Arm | 400, 600 | `U+0530-058F, U+FB13-FB17` | yes | ≤ 26 KB each |
| MC Dram | 400 | `U+058F` **only** | one glyph | ≤ 2 KB |

No italics. No variable font — a variable Montserrat carrying three scripts is larger than the four
static subsets a single locale actually loads. `font-display: swap` everywhere.

**Preload exactly two files per locale** — the text 400 for that locale's script plus the display
400 — with `<link rel="preload" as="font" type="font/woff2" crossorigin>` emitted per-locale by the
build. Preloading more than two is a self-inflicted LCP regression, and preloading a font a locale
does not use is worse than not preloading at all.

**Per-locale font budget: 180 KB.** Asserted in CI (§4.6).

### 4.5 Fallback metrics — the CLS defence

`font-display: swap` without metric overrides is the standard way to spend a CLS budget. Every
fallback gets a metrics-matched alias, and the swap then shifts nothing:

```css
@font-face {
  font-family: "Montserrat Fallback";
  src: local("Arial"), local("Helvetica"), local("Liberation Sans");
  ascent-override: 84.94%;
  descent-override: 22.03%;
  line-gap-override: 0%;
  size-adjust: 113.93%;
}
```

**These four numbers are generated, not remembered.** `npm run build:fontmetrics` reads the shipped
`woff2` with `fontkit`, computes the overrides against the named local face, and writes them into
`mc-tokens.css`; CI fails if the committed values differ from the freshly computed ones. The block
above is the current output for Montserrat against Arial and is correct only for that pair. **Ghea
Mariam has no committed override yet** — nobody in this session has the file — and the build refuses
to emit a `@font-face` for the display face until the generator has produced one. That refusal is
deliberate: the alternative is shipping a guess and paying for it in CLS on the LCP element, which is
always the H1.

The fallback aliases are named in the stacks in position two, before the generic family.

### 4.6 The ֏, and the claims nobody has verified

The dram sign is the single point where this type system can break a legally required element: the
bank requires a real AMD price on the page. Three rules make that impossible.

**R1 — ֏ is bound to its own face, first in every stack, in every locale.**

```css
@font-face {
  font-family: "MC Dram";
  src: url("/fonts/mc-dram.woff2") format("woff2");   /* Noto Sans Armenian, subset to U+058F alone */
  font-weight: 400; font-style: normal; font-display: swap;
  unicode-range: U+058F;
}
```

Because the range is one codepoint, this affects nothing else — see §4.3 for why the Armenian text
faces stop at `U+058A` so that this is the *only* source of ֏ anywhere. If Montserrat Arm turns out
to carry ֏, the glyph still comes from `MC Dram` and nobody can tell. If it does not, prices still
render, in all three locales.

**R2 — the price is never one typeface's problem.** The **amount** may be set in the display face;
the **unit `֏ AMD` is always set in the text face**, at `type.body`, in its own element beneath the
amount. `AMD` is a bank requirement and is printed beside the symbol every time, so even a total
glyph failure leaves the price legible and legally sufficient.

```css
.mc-price__amount { font-family: var(--mc-type-price-font); font-variant-numeric: tabular-nums; }
.mc-price__unit   { font-family: var(--mc-font-text); font-size: var(--mc-type-body-size);
                    color: var(--mc-text-secondary); display: block; }
.mc-currency      { font-family: var(--mc-font-currency); }
```

The audit found the dram sign on the live site rendering from a system fallback, "visibly smaller and
lighter than the digits beside it" (FINDINGS #21). Binding it to a named face fixes exactly that.

**R3 — `qa/glyphs.spec.ts` turns every unverified claim into a build failure.** It runs `fontkit`
over the shipped `woff2` files and asserts, per locale:

- `U+058F` present in the family bound to `--mc-font-currency`;
- `U+0531–U+058A` and `U+FB13–FB17` present in the `hy` stack, **and no shipped face other than `MC Dram` declares `U+058F`** — asserted against the generated `@font-face` blocks, not only against the font files;
- `U+0400–U+04FF` present in the `ru` stack;
- digits present **and tabular figures available** in whichever family sets prices — if the display
  face has no tabular figures, `--mc-type-price-font` falls back to the text face at 600: one token
  change, no component edits;
- **`U+0531–U+058A` and `U+0400–U+04FF` in Ghea Mariam.** If either is absent, the build sets
  `--mc-type-heading-*-font` to the text face at 600 **for that locale only**, which is prior art's
  R4 reinstated automatically. A heading in the text face reads as a deliberate system; a heading in
  a second, mismatched serif reads as a broken font — and a mixed-script line, an Armenian name in an
  English sentence, happens constantly here;
- total shipped font weight ≤ 180 KB per locale.

**A locale does not ship until its assertion passes.** Nothing in this type spec depends on anyone's
recollection, including mine.

### 4.7 Script rules

- `overline` and `rail` **labels** are uppercase in Latin and Cyrillic and **sentence case in
  Armenian** — a `:lang(hy)` branch in the token file, not a developer judgement.
- **Rail and badge *values* are never uppercase in any script.**
- Headings `text-wrap: balance`; body `text-wrap: pretty`.
- `hyphens: auto` for `hy` and `ru`; **not** for `en` — hyphenation reads cheap in an editorial
  layout, and English does not need it at these measures.
- `font-variant-numeric: tabular-nums` on every price, date, coordinate, counter and calculator
  output.
- Measure: 66ch maximum on body copy, via the `760px` narrow container.
- Copy ceilings are enforced per locale (`hy` runs 15–25% and `ru` 10–20% longer than English for the
  same meaning); where a ceiling's overflow rule is `none`, the component has no ellipsis and no
  clamp and **breaks visibly on purpose**, so the copywriter fixes the string rather than the
  developer hiding it.

---

## 5. Responsive architecture

### 5.1 Container queries where the component decides, media queries where the page decides

This is the one place I add capability rather than restore it. Prior art is media-query-only, which
means a `TariffCard` behaves differently in the pricing grid and in the portal sidebar for no reason
other than the viewport width, and every component silently depends on where it was placed.

**The division of labour, and it is absolute:**

- **Media queries** own: the container width, page margins, the grid column count, header height,
  whether the mobile drawer exists, whether `MobileActionBar` exists, and section padding. These are
  properties of the *page*.
- **Container queries** own: whether a card is vertical or horizontal, whether a row wraps, whether
  a rail is inline or a column, how many gallery columns, whether a `FamilyMemberRow` is one line or
  two. These are properties of the *component in its slot*.

```css
.mc-pricing-band { container: mc-band / inline-size; }
.mc-card         { container: mc-card / inline-size; }
.mc-report       { container: mc-report / inline-size; }

@container mc-card (min-width: 30rem) { .mc-card { flex-direction: row; } }
```

Container-query size steps are a closed set, in `rem` so they respond to text size:
**`20rem · 30rem · 40rem · 56rem`**. A component may not invent a fifth.

**Baseline note, stated honestly:** container queries are supported in every browser the audit
touched, but the QA floor here is *old diaspora Android*. Every container query in this system is a
**progressive enhancement over a working single-column layout** — the un-queried state is the 360px
state, which is the state we design first anyway. No component's default rendering depends on
`@container` resolving.

### 5.2 Fluid type and space

Type: §4.2, every clamp with a `rem` in its preferred term.
Space: only the section rhythm is fluid — `--mc-layout-section-block: clamp(3rem, 2rem + 5vw, 7.5rem)`.
Everything inside a component steps on the 4px scale at breakpoints, because a fluid card padding
means no two screenshots ever match and the acceptance checklist stops being checkable.

**The section-adjacency rule, which the prior specification omitted and the lead had to discover
while building:** a light section following another light section opens at **0** and relies on the
section above's block-end padding. A light section that is first after the header, or that follows a
dark band, opens at its full padding. Dark bands always carry full padding on both edges, because
they must separate from what is on both sides. Applied literally without this rule, two adjacent
light sections produce 144px of dead space on mobile and 256px on desktop.

### 5.3 Logical properties, and what they are actually for here

All three locales are LTR. **I am not claiming logical properties buy us RTL support** — they do not,
because we will never ship Arabic or Hebrew, and pretending otherwise is how a system accumulates
machinery nobody needs.

They are mandatory for two real reasons: the padding and border scale is authored once instead of
twice, and `inline-size` / `block-size` make the equal-height card rule and the 44px hit-area rule
express what they mean. `padding-inline`, `margin-block`, `border-inline-start`, `inset-inline-end`,
`min-block-size` throughout; `stylelint` fails on `padding-left`, `margin-top`, `width`, `height`,
`left`, `right`, `top`, `bottom` outside the two documented exceptions (the focus-ring halo and the
`.mc-hit-44` pseudo-element).

### 5.4 Per-component breakpoint behaviour

| Component | `base` 360 | `sm` 600 | `md` 900 | `lg` 1200 | `xl` 1440 |
|---|---|---|---|---|---|
| `SiteHeader` | 56px; logo + menu button | = | **72px**; full nav, no drawer | = | = |
| `MobileMenu` | drawer, LanguageSwitcher first | = | **does not exist** | — | — |
| `MobileActionBar` | 64px + safe-area | = | **does not exist** | — | — |
| `LanguageSwitcher` | in the drawer, 44px segments | = | in the header utility slot | = | = |
| `PricingBand--annual` | 1-up | 2-up | one row, equal height | = | = |
| `PricingBand--one-off` | 1-up, above a rule | 2-up | 2-up, max-inline 760 | = | = |
| `PricingBand--special` | full width | = | = | = | = |
| `TariffCard` | full width, 46px badge reserve | = | = | = | = |
| `ReportSheet` | single column | = | padding `size-10` | rail becomes a right column | = |
| `VerificationRail` | block above the photos | = | = | **222px sticky right column** | = |
| `Gallery` | 1-up | 2-up | 3-up | = | = |
| `ComparisonPair` | stacked | stacked | side by side | = | = |
| `PriceCalculator` | stacked sliders + steppers (documented max-width exception) | = | 2 columns, result on the inline-end | sticky result | = |
| `FamilyMemberRow` | 2 lines, 64px floor | 1 line | = | = | = |
| `PermissionMatrix` | table with a frozen capability column + scroll-fade + a DL equivalent | = | full table | = | = |
| `ConsultationForm` | 1 column, **never inside a dark band at any width** | = | 2 columns for name/phone | = | = |
| `Footer` | stacked, contacts first | 2 columns | 4 columns | = | = |

**Non-negotiables.** Below `sm` everything is one column, including the gallery. No `<table>` renders
below `sm` except `PermissionMatrix`. `dvh`, never `vh`. Every image carries intrinsic
`width`/`height`. **Only one fixed bar may occupy the block-end at a time**, and both are suppressed
while any form field has focus, so nothing covers the keyboard. 200% zoom at 360px produces no
horizontal scroll on any route.

---

## 6. Accessibility — WCAG 2.2 AA, checked

Target: **WCAG 2.2 Level AA, zero axe serious/critical on every route × three locales × {360, 1280}
as a merge gate.** The current site returns 526 violation nodes across 11 rules on 18 pages, five of
them critical. That is the baseline this replaces.

### 6.1 Contrast — checked against the measured table, not asserted

Every colour pair in the system is in §1.3 with a computed ratio; a pair not in that table cannot be
written, because `stylelint-mc-contrast` fails the build on it. Three specific results are worth
stating because they are the ones a designer will push back on:

- **Body text is 12.93 on Nude and 14.17 on Ivory.** The new Dark Olive is a genuine improvement on
  the retired Anthracite (9.61) *and* it is warm rather than grey.
- **Olive fails every text pair** (3.12 / 3.42 / 4.14) and is fenced off structurally, §2 Rule 1.
- **Sky blue is invisible on light** (1.26 / 1.38) and is fenced off structurally, §2 Rule 2.

Non-text contrast (1.4.11, 3:1): input borders `#737060` at **3.99 / 4.38**; focus ring `#575E3B` at
**5.49 / 6.01**; on the dark ground, the ring is Nude at **12.93** and the input border is
`alpha-ivory-45` at **3.99**. Every one of these clears with margin; none of them is at 3.0-something.

### 6.2 Focus

- `:focus-visible` only, never `:focus`. 2px ring, 2px offset, `--mc-border-focus`, `radius-sm`.
- On a Dark Olive fill the ring inverts: inner Ivory at `-3px` offset plus a 4px
  `alpha-deepolive-16` halo, so it never vanishes into the button.
- Inside `.mc-on-dark` the ring is Nude.
- **The ring is never removed** — not on the language switcher, not on gallery thumbnails, not on
  slider handles, not on the map link. The audit's focused and unfocused screenshots of the contact
  form were byte-identical (FINDINGS #24); the ring here is a global rule no component may unset, and
  a `qa/focus.spec.ts` screenshot-diff asserts that focusing each control changes the pixels.
- Focus order follows the DOM. **No `tabindex` above 0 anywhere.** Where visual order differs from
  reading order — the rail at `lg`, the calculator result — the DOM is the reading order and CSS
  reorders.
- **Nothing invisible is focusable.** A collapsed panel is `hidden` or `display: none`, never
  `opacity: 0` with `visibility: visible`. That single pattern produced five phantom tab stops on the
  current site, three of which led to 404 panels.
- **2.4.11 Focus Not Obscured (Minimum), new in 2.2.** The sticky header and both fixed block-end
  bars can cover a focused control. Handled globally, not per-component:
  ```css
  :root { scroll-padding-block-start: calc(var(--mc-layout-header-height) + var(--mc-size-4));
          scroll-padding-block-end:   calc(var(--mc-actionbar-block-size) + var(--mc-size-4)); }
  ```
  and `qa/focus.spec.ts` tabs through every route asserting each focused element's rect is fully
  inside the unobscured viewport.

### 6.3 Target size

House rule **44×44** everywhere, via `.mc-hit-44` where the visual is smaller. WCAG 2.2's
2.5.8 (AA) only requires 24×24; we hold 44 because the audience is 35–60 on a phone and the audit
measured a 28×27 hamburger, 22.5px-tall language links and 16px-tall footer contact links.

```css
.mc-hit-44 { position: relative; }
.mc-hit-44::after {
  content: ""; position: absolute; top: 50%; inset-inline-start: 50%;
  inline-size: max(100%, 44px); block-size: max(100%, 44px);
  transform: translate(-50%, -50%);
}
```

> Carried from prior art **with its bug fixed already applied**: the earlier
> `inset: 50% 50% 50% 50%` version makes width and height inert, the box collapses to zero, and the
> 44×44 area silently does not exist. Worth restating because that failure is invisible in review.

Adjacent targets keep ≥8px clear space. Buttons and inputs are 48px tall on touch, 44px from `lg`.

### 6.4 Keyboard paths for everything that is hover-only today

| Today | Path here |
|---|---|
| nav submenu opens on hover | **no submenu exists**; every nav item is a link to a real page |
| carousel advanced only by pointer arrows | **no carousel exists**; the gallery is a grid, the lightbox is arrow-key and Escape operable |
| before/after drag slider | **replaced** by two stacked frames; no gesture at all (2.5.7) |
| row actions revealed on hover | the `FamilyMemberRow` menu button is permanently visible |
| calculator slider drag | slider **plus** a `Stepper`; arrow keys, Home/End, PageUp/PageDown all move the value (2.5.7) |
| bottom-sheet drag handle | plus a 44×44 close button and Escape |
| tooltip on hover | tooltip content also exists as visible text elsewhere; the trigger is focusable and Escape dismisses |
| logout on a `GET` link | **a `POST` form with a button.** FINDINGS #16: an automated link crawl signed the auditor out — any prefetcher, antivirus scanner or chat-app preview will do the same |

### 6.5 Forms

Visible `<label for>` on every control — no exceptions, no placeholder-as-label, no "visually hidden
label" escape hatch in the component API. `aria-describedby` chains help text and error.
`aria-invalid` when errored. On failed submit, an `ErrorSummary` with `role="alert"` receives focus
and links to each field. Correct `type`, `inputmode` and `autocomplete` on every field.
`role="alert"` on the inline error so it is announced when it appears.

WCAG 2.2's three new form-adjacent criteria, each answered:
- **3.3.7 Redundant Entry** — the calculator hands its state to the consultation form via
  `?tier=&area=&monuments=` and hidden fields; nothing already given is asked again.
- **3.3.8 Accessible Authentication (Minimum)** — no cognitive-function test, no puzzle CAPTCHA;
  **paste is never blocked** in any field, including password and any one-time code.
- **3.2.6 Consistent Help** — contacts appear in the same footer position on every page, which is
  also a bank requirement.

Consent: one checkbox, required, its own control, with a link to the privacy policy, recorded with
date and IP. The current registration form takes name, phone, email and a password with no consent,
no policy to point at and no confirmation field (FINDINGS #9).

### 6.6 Reduced motion

`prefers-reduced-motion: reduce` collapses all durations to 1ms and all translate distances to 0.
**It is not "animations off":** opacity cross-fades survive at 1ms and are simply instant; the
loading arc becomes a static arc plus its word. Because this system has no count-up, no auto-advance,
no parallax and no scroll-jacking, the reduced-motion path and the default path differ only in
duration — which is always the better outcome. The decorative animated sky on the current build
(three.js + Vanta, 601 KB) is not gated on the preference and does not survive to this system at all.

### 6.7 Language

- `<html lang="hy|en|ru">`, **correct per locale.** The audit found `lang="en"` on all 18 pages
  including every Armenian one, while `og:locale` on the same documents correctly said `hy_AM` — the
  value existed in the template and was not used (FINDINGS #6).
- **Locale codes in URLs are `hy`, `en`, `ru`.** `am` is Amharic. Every Armenian URL on the current
  site is labelled Amharic (FINDINGS #17). `/` redirects to a locale rather than serving one
  (FINDINGS #18).
- `lang` on any inline foreign-language fragment, and on each `LanguageSwitcher` link (`lang` +
  `hreflang`).
- Reciprocal `hreflang` alternates plus `x-default`, and a `canonical` on every page.
- `:lang(hy)` drives the sentence-case branch for overlines and rail labels, and `hyphens: auto` for
  `hy` and `ru`.
- Every locale is written in one script: no Armenian in the English build, no Armenian in the Russian
  build (owner-ruled 31.08).

### 6.8 The rest of the checklist

Landmarks — `header`, `nav`, `main`, `footer` on every page, exactly one `h1`, an unbroken heading
outline (the audit found `main: 0, footer: 0, h1: []` on all 18 pages). Meaningful `alt` on every
image; `alt=""` on decorative ones; **`alt` is a required prop with no default** — 198 images without
it is what a default gets you. Every link has a discernible name; no `href=""`, no `href="#"`, no
`javascript:void(0)`. Pinch-zoom enabled: the viewport meta carries `width=device-width,
initial-scale=1` **and nothing else**. `aria-label` never on a bare `div`. Every iframe has a
`title` — and there are no iframes.

---

## 7. Performance budget

The current home page weighs **4.66 MB** in Armenian and **5.73 MB** in English, over 29 same-origin
requests plus five third-party files, on a page whose entire text content is placeholder. A login
form with two fields ships 800 KB. Caching is defeated at source: the CSS and JS query strings are
`time()` at render, so a returning visitor never has a warm cache (FINDINGS #41). Those are the
numbers this budget replaces.

### 7.1 Field targets — p75, mobile, throttled 4G, at 360px, all three locales

| Metric | Budget | Fail |
|---|---|---|
| **LCP** | **≤ 2.0s** | > 2.5s |
| **INP** | **≤ 150ms** | > 200ms |
| **CLS** | **≤ 0.03** | > 0.05 |
| TTFB | ≤ 400ms | > 600ms |
| FCP | ≤ 1.4s | > 1.8s |

LCP is stricter than the 2.5s pass mark because the LCP element here is the H1 plus one hero image
and there is nothing on that page that justifies spending the margin. CLS is stricter than 0.05
because the current build achieves **0.000** — the one thing it does well — and a rebuild that gives
that away is a regression regardless of what else improves.

### 7.2 Byte budgets, per route, gzipped, first view

| | Home | Pricing | Sample report | Legal / About | Portal shell |
|---|---|---|---|---|---|
| HTML | 20 KB | 18 KB | 22 KB | 14 KB | 12 KB |
| CSS | **≤ 40 KB** total, ≤ 14 KB inlined critical | = | = | = | = |
| JS | **≤ 60 KB** | ≤ 45 KB | ≤ 45 KB | **≤ 10 KB** | ≤ 120 KB |
| Fonts | ≤ 180 KB / locale | = | = | = | = |
| Images | ≤ 450 KB | ≤ 200 KB | ≤ 600 KB | ≤ 100 KB | ≤ 150 KB |
| **Total first view** | **≤ 750 KB** | ≤ 500 KB | ≤ 900 KB | **≤ 320 KB** | ≤ 480 KB |

`npm run test:bundle` fails the build on any overage. The legal/About row is deliberately brutal:
those pages are text, and the reason the current login page weighs 800 KB is that four libraries none
of its two fields uses are loaded globally.

**JS is per-route, not global.** No library loads on a page that does not use it. The marketing site
needs no framework at all: it is HTML, one stylesheet, and roughly 6 KB of vanilla JS (drawer,
accordion, lightbox, form validation, calculator). If a framework is used for the portal, it does not
reach the marketing routes.

### 7.3 Images

| Use | Ratio | Delivered | Formats | Ceiling |
|---|---|---|---|---|
| Report photograph | **4:3** at 1600×1200 | 400 / 800 / 1200 / 1600 | AVIF → WebP → JPEG | 140 KB at 1600 |
| Marketing section image | **3:2** at 1800×1200 | 600 / 900 / 1200 / 1800 | same | 160 KB at 1800 |
| Crew / equipment portrait | 1:1 | 200 / 400 / 800 | same | 60 KB |
| OG / link preview | 1.91:1, 1200×630 | one | PNG (generated) | 120 KB |
| Logo, favicons | vector | inline SVG + generated PNGs | SVG | ≤ 6 KB inline |

Ratios are lead-ruled: a routine visit report is photographed by a crew member on a **phone**, whose
native still ratio is 4:3, so 4:3 is the no-crop ratio for the device that actually takes these
photographs. 3:2 is what the booked professional camera shoots, so marketing takes 3:2.

Rules: `<picture>` with AVIF and WebP sources and a JPEG fallback; `srcset` + `sizes` on every image;
intrinsic `width`/`height` on every image, no exceptions (this is the CLS budget); `loading="lazy"`
and `decoding="async"` on everything **except** the LCP image, which is eager with
`fetchpriority="high"` and is preloaded; `alt` required. Images fade in on decode over 200ms —
**no skeleton shimmer**. The audit found a 500×500 PNG logo displayed at 60×60, 276 KB, on every page
including the 404 panel; the logo here is inline SVG under 6 KB.

### 7.4 Caching and delivery

`Cache-Control: public, max-age=31536000, immutable` on every hashed asset; the hash is a **content
hash from the build**, never a timestamp. HTML gets `no-cache` with an ETag. Brotli, HTTP/2 or /3,
preconnect to nothing (there is nothing to preconnect to).

### 7.5 Forbidden outright

Each of these is in the current build; none survives.

- **jQuery** (94 KB), and especially `jquery-latest.min.js`, which the jQuery CDN froze in 2014.
- **three.js + Vanta** (601 KB) for a decorative animated sky that is indistinguishable from a static
  gradient at 360px and is not gated on reduced motion.
- **Swiper** (151 KB) — there is no carousel.
- **AOS**, and scroll-triggered animation libraries generally.
- **Magnific Popup** — loaded on all 48 documents, bound to four selectors that match nothing on any
  of them. It never runs.
- **Autoplay video.** The 2.3 MB `v.mp4` is half the home page. Video is behind a poster image and a
  play button, `preload="none"`.
- **Any unpinned CDN URL** (`@latest`, `-latest`), **any third-party script without SRI**, and any
  third-party origin for a brand asset. Six third-party origins on a page that will take card
  payments is a finding in its own right.
- **Google Fonts.** Self-hosted only.
- **Third-party analytics** at launch — owner-ruled — and therefore no cookie banner over the primary
  CTA.
- **Timestamp cache-busting.**
- **`backdrop-filter`**, and animating anything but `opacity` and `transform`.
- **Web fonts in more than two preloads per locale**, and italics (none are shipped).
- **Carousels, parallax, scroll-jacking, count-up numerals, skeleton shimmer, Ken Burns, hover-zoom,
  falling petals, a rotating medallion, typewriter text, spring physics.** Motion confirms; it never
  entertains. This product is opened to look at a photograph of a grave.

---

## 8. CSS architecture, and what a developer is handed

### 8.1 Cascade layers

```css
@layer mc.reset, mc.tokens, mc.base, mc.layout, mc.components, mc.utilities, mc.overrides;
```

Specificity stops being a weapon: a component rule never has to out-specify a utility, and
`mc.overrides` is empty in a healthy repository — a non-empty `mc.overrides` is the review signal
that something is missing a layer below. **No `!important` anywhere** except the reduced-motion
block, which must beat inline styles.

### 8.2 Naming

`mc-<block>__<element>--<modifier>`, one block per file, file named for the block. State is a data
attribute, never a class: `data-state="loading"`, `data-variant="annual"`, `data-emphasis="leading"`.
The reason is that state then has one representation in CSS, in the DOM inspector and in the test —
`[data-state="error"]` is greppable and `.is-error .has-error .error` is not.

ARIA carries state wherever ARIA has a word for it, and CSS reads *that*, so the two cannot diverge:

```css
.mc-accordion__trigger[aria-expanded="true"] .mc-accordion__chevron { rotate: 180deg; }
.mc-nav__link[aria-current="page"]                                   { border-block-end: 2px solid var(--mc-border-accent); }
```

If the style is wrong, the ARIA is wrong, and the screen-reader bug is visible to the eye.

### 8.3 How tokens reach the browser

```
tokens/tokens.json          W3C DTCG format — the only place a value is authored
   │  style-dictionary
   ├─► build/mc-tokens.css        :root + .mc-on-dark + .mc-on-ivory, wrapped in @layer mc.tokens
   ├─► build/mc-media.css         @custom-media --mc-sm … --mc-xl   (PostCSS)
   ├─► build/breakpoints.ts       the same five numbers, for any script that needs one
   └─► build/tokens.d.ts          the union type of every token name
```

`mc-tokens.css` is **generated, never edited** — a header comment says so and CI fails if the file
differs from a fresh build. It is imported exactly once, globally, as a real `<link>` in `<head>`
(not an `@import`, which serialises). No runtime theming, no CSS-in-JS, no JS reading or writing
custom properties — the palette must be identical in the HTML, the print stylesheet and the report
PDF, and a runtime layer breaks all three.

Everything a component uses is a Layer-3 custom property, so the only cascade a component
participates in is the one the token file defines.

### 8.4 What is handed over, so this cannot drift

```
tokens/     tokens.json · build/ · stylelint-mc-contrast/ · stylelint-mc-scope/
brand/      logo.svg (inline-ready, token fills) · FONTS.md · LOGO-USAGE.md · build:brand
components/ SPEC-<Name>.md ×46 — anatomy, variants, states, breakpoints, a11y notes, markup skeleton
content/    strings.{hy,en,ru}.json · products.json · content-limits.json
qa/         contrast · scope · ground · focus · glyphs · prices · strings · bundle · sky   (.spec.ts)
docs/       ACCEPTANCE-CHECKLIST.md · DEVELOPER-DECISIONS.md · OPEN-ITEMS.md
```

**Nine CI gates. Each fails the build; none is advisory.**

| Gate | Asserts |
|---|---|
| `lint:tokens` | layer discipline; no forbidden substring; no literal hex/px/ms in `src/`; no `var(--mc-color-*)` outside the token file |
| `stylelint-mc-contrast` | every colour pair is in §1.3; nothing sets `color` on a `--mc-decor-*` ground |
| `stylelint-mc-scope` | no form component inside `.mc-on-dark`; no `-on-dark` token used outside `.mc-on-dark` |
| `qa/contrast` | axe-core + a rendered-DOM pair walk, 3 locales × {360, 1280}, zero serious/critical |
| `qa/focus` | every control's focus changes pixels; no focused rect is obscured by a fixed bar; no `tabindex > 0`; no focusable invisible element |
| `qa/glyphs` | §4.6, per locale; ≤ 180 KB fonts per locale |
| `qa/strings` | denylist clean; every length ceiling met in all three locales |
| `qa/prices` | every rendered price traces to `products.json`; both `֏` and `AMD`; no `line-through` |
| `test:bundle` | §7.2 byte budgets per route |

**And the eleven things that are deliberately the developer's call** stay his: build tool, bundler,
template engine, directory layout inside `src/`, test runner, the portal's framework, the phone
parsing library, the image pipeline's implementation, the CI provider, the commit convention, and the
staging host. Everything else — every colour, radius, duration, gap and string — resolves from a
token or a content file. **If he needs a number that is not in `mc-tokens.css`, that is a defect in
this document, not a decision for him.**

---

## 9. Where I override `FINAL-SYSTEM.md`, in one list

| # | Prior art | Here | Why |
|---|---|---|---|
| 1 | Anthracite `#33373C` as the dark; `.mc-on-dark` built on it | **Dark Olive `#212212`**, plus derived 400/600 steps | Anthracite is retired. 12.93 on Nude against 9.61, and warm rather than cool grey |
| 2 | `--mc-text-secondary: #606161` (4.98) | **`#5C5C50`** (5.43 / 5.95) | A cool grey beside a warm near-black olive reads as a second, dirtier text colour |
| 3 | `--mc-border-strong` = alpha-50, composites to **3.01** on Nude, 3.30 on Ivory | **solid `#737060`**, 3.99 / 4.38 | It is the input border; 1.4.11 needs 3:1 and 3.01 passes by 0.01 |
| 4 | Accent badge = Deep Olive fill + Ivory label (6.01) | **Dark Olive fill + Ivory label (14.17)** | One fewer dependency on an unratified value; the badge and the button now match |
| 5 | Primary button = Deep Olive fill | **Dark Olive fill + Ivory label** | Same reason; also owner-recorded in `CLAUDE.md` |
| 6 | Gloock / Cabin (Gill Sans substitute), R4: no display face for `hy`/`ru` | **Ghea Mariam / Montserrat + Montserrat Arm**; R4 becomes the automatic degraded path | Both blocking issues — the Monotype licence and Armenian coverage — are removed by the 31.08 book |
| 7 | No Sky blue at all | A **fourth colour family**, dark-ground-only, with the swap architecture of §1.6 | It is new in the brandbook and it is contested |
| 8 | `--mc-modal-radius: var(--mc-radius-md)`, a token §5.3 deletes | **`--mc-radius-overlay: 8px`** | The prior file references an undefined variable; every modal would silently render square |
| 9 | Media queries only | **Container queries for component-internal layout**, media queries for the page | A card should not change shape because of the viewport when its slot did not change |
| 10 | `--mc-surface-page` / `--mc-surface-raised` | **`--mc-surface-ground` / `--mc-surface-object`** | The name has to carry the Nude/Ivory rule, because the eye cannot |
| 11 | Olive reachable as a semantic surface | **the `decor` namespace**, plus a lint on `color` over a decor ground | "Surface" invites a foreground; "decor" refuses one |
| 12 | "The form may never sit on a dark band" as prose + a stylelint rule | prose + lint + **an unset error token + the `--mc-form-guard` tripwire** | It is the one rule whose failure is invisible until a visitor makes a mistake |
| 13 | Font fallback metrics not specified | **generated by `build:fontmetrics`, CI-verified, and the display `@font-face` refuses to emit without them** | `font-display: swap` without overrides is how the CLS budget gets spent |
| 14 | Carousel not explicitly forbidden (auto-advance was) | **No carousel component exists** | Six separate audit findings, 151 KB, and it does not work today |
| 15 | Motion: "no transform on cards or buttons" | plus **only `opacity` and `transform` may be animated at all** | The accordion and the drawer are the INP risks, and both are fixable at spec time |
| 16 | `TariffCard`: two variants, price always a number | **five variants + a `PriceSlot--phrase`**, and no visit-kind prop at all | Special has no price, and a card that *can* express two kinds of visit will eventually be made to |
| 17 | Armenian faces declared `U+0530-058F`, overlapping `MC Dram`'s single codepoint | Armenian faces **stop at `U+058A`** | Otherwise an English page with one price pulls a 26 KB Armenian text face, and which family supplies ֏ depends on declaration order rather than on a decision |

Everything else in `FINAL-SYSTEM.md` that is not a colour or a typeface — the radius scale, the
photograph ratios, the equal-height card rule, the badge-height reserve, the breakpoints, the
44×44 rule, the forbidden-motion list, the vocabulary table, the content ceilings, the copy denylist,
the bank checklist — is carried forward unchanged and I recommend it be treated as still binding.
