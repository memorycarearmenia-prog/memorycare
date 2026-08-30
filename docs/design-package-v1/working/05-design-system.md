# 05 — Design System & Handoff Package

**MemoryCare — site + client portal**
Author: Design System and Handoff Engineer
Version: 1.0 · 2026-08-30
Audience: Igor (external developer), the design lead, the owner
Language of all deliverables: English

---

## 0. The one-paragraph contract

Everything visual in MemoryCare is expressed as a token. Igor never picks a
colour, a radius, a duration or a gap. He picks a component, gives it a variant
and a state, and the system resolves the values. If he ever needs a number that
is not in `tokens/mc-tokens.css`, that is a bug in this document, not a decision
for him to make — he raises it in `OPEN-ITEMS.md` and we answer within one
working day. There are exactly eleven things that are deliberately his call;
they are listed in §12 and nowhere else.

---

# A. UI as a system

## A1. Naming convention

One grammar, used identically in JSON, CSS, Figma variables and component props.

```
mc . <layer> . <category> . <role> [. <variant>] [. <state>] [. <scale-step>]
```

| Rule | Why | Example |
|---|---|---|
| Prefix everything `mc` | The portal will embed third-party widgets (payment, maps). No collisions. | `--mc-color-olive-500` |
| Lower-kebab in CSS, lower-dot in JSON, `Title/Slash` in Figma | Three surfaces, one mental model | `--mc-surface-raised` ⇄ `mc.surface.raised` ⇄ `Surface/Raised` |
| **Names describe role, never appearance** | Copy is translated, colour is not. `--mc-text-green` breaks the day Olive changes; `--mc-text-accent` never does. | `--mc-text-accent`, not `--mc-text-olive` |
| **Names never encode a measurement** | `--mc-nav-width-240` becomes a lie in Armenian | `--mc-nav-item-padding-inline` |
| **Names never encode English copy** | `--mc-btn-learn-more` is untranslatable | `--mc-button-secondary-*` |
| Logical properties only: `inline-start/end`, `block-start/end` | Armenian and Russian set longer; a future Arabic-script or RTL market costs nothing | `padding-inline: var(--mc-space-5)` |
| Scale steps are numeric and open-ended: `100…900` for colour, `0…16` for space | The product grows; you can insert `250` without renaming anything | `--mc-color-anthracite-700` |
| States are a closed set: `default hover active focus disabled loading selected error` | Igor knows the full matrix before he starts | `--mc-button-primary-bg-hover` |
| No abbreviations except `bg`, `fg`, `min`, `max` | Two-person team, six months of memory | — |

**Forbidden token names** (they have all appeared in earlier repo work and must
not come back): `--gold`, `--gold2`, `--navy`, `--lilac`, `--blue`, `--mut`,
`--dim`. Any of these in a pull request is an automatic reject.

---

## A2. Three-layer token architecture

```
Layer 1  PRIMITIVE   mc.color.olive.500          raw value, no meaning, never used in a component
   │                 mc.size.4
   ▼
Layer 2  SEMANTIC    mc.surface.raised           the decision, theme-switchable
   │                 mc.text.accent
   ▼
Layer 3  COMPONENT   mc.button.primary.bg.hover  the contract with the markup
```

Rules, enforced in code review:

1. A component stylesheet may reference **Layer 3 only**.
2. A Layer 3 token may reference **Layer 2 only**.
3. A Layer 2 token may reference **Layer 1 only**.
4. Layer 1 is the only place a literal hex, px or ms appears.
5. Skipping a layer is allowed nowhere. If a component needs a primitive
   directly, the semantic token is missing — add it.

Why three layers here specifically: the palette has one unresolved value
(Deep Olive is a working value awaiting the designer), one unresolved type pair
(Gill Sans licence, Armenian coverage) and three languages. Each of those is a
single-line change at Layer 1 or 2 and zero changes at the component level.

---

### Layer 1 — primitives

#### Colour primitives

The five brand values are the only hues in the system. Everything else in this
table is an **alpha of a brand value or a documented mix of two brand values** —
the formula is printed next to each one so the designer can verify that no sixth
hue has been invented.

| Token | Value | Origin |
|---|---|---|
| `mc.color.olive.500` | `#7C8654` | Brandbook, Olive |
| `mc.color.olive.700` | `#575E3B` | Brandbook addendum, Deep Olive (working value) |
| `mc.color.olive.800` | `#4E5535` | Deep Olive × 0.90 toward black |
| `mc.color.olive.900` | `#474D30` | Deep Olive × 0.82 toward black |
| `mc.color.nude.500` | `#EFE5D5` | Brandbook, Nude |
| `mc.color.nude.400` | `#F2EADD` | Nude 80% + white 20% |
| `mc.color.nude.600` | `#E4D8C4` | Nude 92% + Anthracite 8% |
| `mc.color.ivory.500` | `#F3F0E9` | Brandbook, Ivory white |
| `mc.color.ivory.400` | `#F8F6F1` | Ivory 70% + white 30% |
| `mc.color.anthracite.500` | `#33373C` | Brandbook, Anthracite |
| `mc.color.anthracite.400` | `#4A4D51` | Anthracite 88% + Ivory 12% |
| `mc.color.anthracite.600` | `#292C30` | Anthracite × 0.80 toward black |
| `mc.color.anthracite.mix.760` | `#606161` | Anthracite 76% + Nude 24% |
| `mc.color.white` | `#FFFFFF` | — |
| `mc.color.danger.600` | `#8C3A2E` | **The only non-brand hue. See A3.5.** |
| `mc.color.danger.100` | `#F6E4E0` | danger.600 at 10% over Ivory |

Alpha primitives (these composite over any ground, which is why tints are alphas
and not new hexes):

| Token | Value |
|---|---|
| `mc.alpha.anthracite.08` | `rgba(51,55,60,0.08)` |
| `mc.alpha.anthracite.12` | `rgba(51,55,60,0.12)` |
| `mc.alpha.anthracite.20` | `rgba(51,55,60,0.20)` |
| `mc.alpha.anthracite.38` | `rgba(51,55,60,0.38)` |
| `mc.alpha.anthracite.60` | `rgba(51,55,60,0.60)` |
| `mc.alpha.ivory.12` | `rgba(243,240,233,0.12)` |
| `mc.alpha.ivory.24` | `rgba(243,240,233,0.24)` |
| `mc.alpha.ivory.40` | `rgba(243,240,233,0.40)` |
| `mc.alpha.olive.12` | `rgba(124,134,84,0.12)` |
| `mc.alpha.olive.24` | `rgba(124,134,84,0.24)` |
| `mc.alpha.deepolive.08` | `rgba(87,94,59,0.08)` |
| `mc.alpha.deepolive.16` | `rgba(87,94,59,0.16)` |

#### Size / space primitives

4 px base unit. `mc.size.N` where the value is `N × 4px`, expressed in rem
(root = 16px) so browser zoom and the 40–60 audience's text-size setting work.

| Token | rem | px |
|---|---|---|
| `mc.size.0` | 0 | 0 |
| `mc.size.0-5` | 0.125 | 2 |
| `mc.size.1` | 0.25 | 4 |
| `mc.size.2` | 0.5 | 8 |
| `mc.size.3` | 0.75 | 12 |
| `mc.size.4` | 1 | 16 |
| `mc.size.5` | 1.25 | 20 |
| `mc.size.6` | 1.5 | 24 |
| `mc.size.8` | 2 | 32 |
| `mc.size.10` | 2.5 | 40 |
| `mc.size.12` | 3 | 48 |
| `mc.size.16` | 4 | 64 |
| `mc.size.20` | 5 | 80 |
| `mc.size.24` | 6 | 96 |
| `mc.size.30` | 7.5 | 120 |
| `mc.size.40` | 10 | 160 |
| `mc.size.50` | 12.5 | 200 |

#### Radius primitives

| Token | Value |
|---|---|
| `mc.radius.0` | `0` |
| `mc.radius.xs` | `2px` |
| `mc.radius.sm` | `6px` |
| `mc.radius.md` | `10px` |
| `mc.radius.lg` | `14px` |
| `mc.radius.xl` | `20px` |
| `mc.radius.2xl` | `28px` |
| `mc.radius.full` | `9999px` |

Editorial-minimal, not consumer-app: buttons are `md` (10px), not pills. Pills
are reserved for badges and the language switcher, where the shape carries
meaning (a chip you can toggle).

#### Border-width, duration, easing, z-index primitives

| Token | Value |
|---|---|
| `mc.border.0 / 1 / 2 / 3` | `0 / 1px / 2px / 3px` |
| `mc.duration.instant` | `80ms` |
| `mc.duration.fast` | `140ms` |
| `mc.duration.base` | `220ms` |
| `mc.duration.slow` | `320ms` |
| `mc.duration.slower` | `480ms` |
| `mc.ease.standard` | `cubic-bezier(0.2, 0, 0, 1)` |
| `mc.ease.decelerate` | `cubic-bezier(0, 0, 0, 1)` |
| `mc.ease.accelerate` | `cubic-bezier(0.3, 0, 1, 1)` |
| `mc.ease.gentle` | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `mc.z.base` | `0` |
| `mc.z.sticky` | `100` |
| `mc.z.header` | `200` |
| `mc.z.dropdown` | `300` |
| `mc.z.overlay` | `400` |
| `mc.z.modal` | `410` |
| `mc.z.toast` | `500` |
| `mc.z.skiplink` | `600` |

No spring physics anywhere. This product is opened to look at a photograph of a
grave. Motion is a fade and a small translate, nothing bounces.

---

### Layer 2 — semantic

#### Surfaces — the Nude/Ivory question, settled

> **Nude below, Ivory above.**
> Nude `#EFE5D5` is the page ground. Ivory `#F3F0E9` is anything raised off it —
> cards, panels, sheets, inputs — and is the light text colour on Anthracite.
> Ivory is never a page background. Nude is never a card background.

This is the rule the brief asked to be written down. It is testable: any
full-bleed `<section>` is Nude; anything with a border-radius on a light ground
is Ivory.

| Token | Light theme | Dark section |
|---|---|---|
| `mc.surface.page` | `color.nude.500` | `color.anthracite.500` |
| `mc.surface.raised` | `color.ivory.500` | `color.anthracite.400` |
| `mc.surface.raised-hover` | `color.ivory.400` | `#52565A` (anthracite.400 +6% ivory) |
| `mc.surface.sunken` | `color.nude.600` | `color.anthracite.600` |
| `mc.surface.inverse` | `color.anthracite.500` | `color.nude.500` |
| `mc.surface.accent-wash` | `alpha.olive.12` | `alpha.olive.24` |
| `mc.surface.accent-solid` | `color.olive.500` | `color.olive.500` |
| `mc.surface.overlay-scrim` | `rgba(51,55,60,0.72)` | same |
| `mc.surface.media-placeholder` | `alpha.olive.24` over nude | — |
| `mc.surface.danger-subtle` | `color.danger.100` | — |

#### Text

| Token | Value | On page (Nude) | On raised (Ivory) |
|---|---|---|---|
| `mc.text.primary` | `color.anthracite.500` | **9.61** | **10.53** |
| `mc.text.secondary` | `color.anthracite.mix.760` `#606161` | **4.87** | **5.34** |
| `mc.text.accent` | `color.olive.700` `#575E3B` | **5.49** | **6.01** |
| `mc.text.link` | `color.olive.700` | 5.49 | 6.01 |
| `mc.text.link-hover` | `color.olive.800` `#4E5535` | 6.4 | 7.0 |
| `mc.text.on-accent` | `color.ivory.500` | on Deep Olive: **6.01** | — |
| `mc.text.inverse` | `color.nude.500` | on Anthracite: **9.61** | — |
| `mc.text.inverse-secondary` | `alpha.ivory.40`… | **not permitted for text** — see below |
| `mc.text.danger` | `color.danger.600` | **6.09** | 6.7 |
| `mc.text.disabled` | `alpha.anthracite.38` | 2.9 — **non-text use only** |

There is deliberately **no `mc.text.tertiary`**. Anything below 4.5 is not a
text token in this system. Secondary text on a dark ground is
`mc.text.inverse` at the same value as primary, differentiated by size and
letter-spacing, not by dropping contrast. Audience is 40–60, reading on a phone,
frequently outdoors.

`mc.text.disabled` fails contrast by design and is therefore **never the only
signal**: a disabled control also carries `aria-disabled`, a reduced-opacity
border, and no pointer cursor.

#### Borders

| Token | Value |
|---|---|
| `mc.border.subtle` | `alpha.anthracite.08` — hairlines inside a card |
| `mc.border.default` | `alpha.anthracite.20` — input rest, card outline |
| `mc.border.strong` | `alpha.anthracite.38` — input hover, selected card |
| `mc.border.accent` | `color.olive.700` |
| `mc.border.decorative` | `color.olive.500` — rules, dividers, ornament only |
| `mc.border.focus` | `color.olive.700` |
| `mc.border.focus-inverse` | `color.nude.500` |
| `mc.border.danger` | `color.danger.600` |
| `mc.border.inverse` | `alpha.ivory.24` |

`mc.border.decorative` is the **only** place Olive is allowed at Layer 2 next to
content, and it may never sit under text.

#### Elevation

Light-minimal brand: elevation is carried by a hairline first and a shadow
second. No shadow ever exceeds 8% opacity on a light ground.

| Token | Value |
|---|---|
| `mc.elevation.0` | `none` |
| `mc.elevation.1` | `0 1px 2px rgba(51,55,60,0.04), 0 0 0 1px rgba(51,55,60,0.06)` |
| `mc.elevation.2` | `0 2px 8px rgba(51,55,60,0.06), 0 0 0 1px rgba(51,55,60,0.06)` |
| `mc.elevation.3` | `0 8px 24px rgba(51,55,60,0.08), 0 0 0 1px rgba(51,55,60,0.06)` |
| `mc.elevation.4` | `0 20px 48px rgba(51,55,60,0.12)` — modals only |
| `mc.elevation.inverse-2` | `0 2px 8px rgba(0,0,0,0.24)` |

#### Typography semantics

Faces (see A3.4 for the licence/script reasoning):

| Token | Stack |
|---|---|
| `mc.font.display` | `"Gloock", "Noto Serif Armenian", "Playfair Display", Georgia, serif` |
| `mc.font.text` | `"Cabin", "Noto Sans Armenian", "Noto Sans", system-ui, -apple-system, "Segoe UI", sans-serif` |
| `mc.font.mono` | `ui-monospace, "SF Mono", "Roboto Mono", monospace` — GPS coordinates, invoice numbers, reference IDs only |

Display is Gloock **Regular 400 only**. There is no bold Gloock. Hierarchy in
display type is built from size, colour and space — never from weight.

Roles (`clamp()` values are the production values; the min is the 360px
rendering, the max the 1440px rendering):

| Token | Font | Size | Line height | Tracking | Weight |
|---|---|---|---|---|---|
| `mc.type.display-1` | display | `clamp(2.25rem, 1.4rem + 3.8vw, 4rem)` | 1.08 | `-0.01em` | 400 |
| `mc.type.display-2` | display | `clamp(1.875rem, 1.3rem + 2.6vw, 3rem)` | 1.12 | `-0.005em` | 400 |
| `mc.type.heading-1` | display | `clamp(1.625rem, 1.25rem + 1.6vw, 2.25rem)` | 1.18 | `0` | 400 |
| `mc.type.heading-2` | display | `clamp(1.375rem, 1.15rem + 0.9vw, 1.75rem)` | 1.24 | `0` | 400 |
| `mc.type.heading-3` | text | `1.125rem` | 1.35 | `0` | 600 |
| `mc.type.body-lg` | text | `1.125rem` | 1.6 | `0` | 400 |
| `mc.type.body` | text | `1rem` | 1.6 | `0` | 400 |
| `mc.type.body-sm` | text | `0.9375rem` | 1.55 | `0` | 400 |
| `mc.type.label` | text | `0.875rem` | 1.4 | `0.01em` | 600 |
| `mc.type.caption` | text | `0.8125rem` | 1.45 | `0.01em` | 400 |
| `mc.type.overline` | text | `0.75rem` | 1.3 | `0.14em` | 600, uppercase |
| `mc.type.price` | display | `clamp(1.75rem, 1.3rem + 1.9vw, 2.5rem)` | 1.0 | `-0.01em` | 400 |
| `mc.type.numeric` | mono | `0.875rem` | 1.5 | `0.02em` | 400 |

**Minimum body size on the site is 16px. Nothing below 13px exists in the
system at all**, including captions and legal text. Bank-required legal pages
use `mc.type.body-sm`, not fine print.

`mc.type.overline` is uppercase in Latin and Cyrillic. **It is set in sentence
case for Armenian** — Armenian uppercase is visually aggressive and reads as
shouting. This is a token-level branch, not a developer judgement:
`:lang(hy) .mc-overline { text-transform: none; letter-spacing: 0.08em; }`

#### Motion semantics

| Token | Value |
|---|---|
| `mc.motion.hover` | `var(--mc-duration-fast) var(--mc-ease-standard)` |
| `mc.motion.enter` | `var(--mc-duration-base) var(--mc-ease-decelerate)` |
| `mc.motion.exit` | `var(--mc-duration-fast) var(--mc-ease-accelerate)` |
| `mc.motion.expand` | `var(--mc-duration-slow) var(--mc-ease-standard)` |
| `mc.motion.page` | `var(--mc-duration-slower) var(--mc-ease-gentle)` |
| `mc.motion.distance-sm` | `4px` |
| `mc.motion.distance-md` | `8px` |
| `mc.motion.distance-lg` | `16px` |

#### Layout semantics

| Token | Value |
|---|---|
| `mc.layout.container-max` | `1200px` |
| `mc.layout.container-narrow` | `760px` — legal pages, About, report body text |
| `mc.layout.gutter` | `16px` → `24px` @md → `24px` @lg |
| `mc.layout.margin` | `16px` → `32px` @md → `48px` @lg |
| `mc.layout.section-block` | `clamp(3rem, 2rem + 5vw, 7.5rem)` — vertical rhythm between sections |
| `mc.layout.header-height` | `64px` mobile / `76px` @lg |
| `mc.layout.target-min` | `44px` |
| `mc.layout.focus-offset` | `2px` |
| `mc.layout.focus-width` | `2px` |

---

### Layer 3 — component tokens

Full list ships in `tokens/tokens.json`. The shape, using the button as the
worked example — every component follows it exactly:

```
mc.button.<variant>.<property>.<state>
variants:  primary | secondary | tertiary | danger | primary-inverse | secondary-inverse
props:     bg | fg | border | shadow | radius | padding-inline | padding-block | min-height | gap | font
states:    default | hover | active | focus | disabled | loading
```

Every component token resolves to a Layer 2 token. Extract:

| Component token | → Semantic |
|---|---|
| `mc.button.primary.bg.default` | `mc.surface.accent-strong` → `color.olive.700` |
| `mc.button.primary.bg.hover` | `color.olive.800` |
| `mc.button.primary.bg.active` | `color.olive.900` |
| `mc.button.primary.fg.default` | `mc.text.on-accent` → `color.ivory.500` |
| `mc.button.primary.bg.disabled` | `mc.alpha.anthracite.12` |
| `mc.button.primary.fg.disabled` | `mc.alpha.anthracite.38` |
| `mc.tariff-card.featured.border` | `mc.border.accent` |
| `mc.report-card.status-ok.icon` | `mc.text.accent` |

---

## A3. The written-out files

### A3.1 `tokens/tokens.json` — structure

W3C Design Tokens Community Group format (`$value` / `$type` / `$description`),
because Style Dictionary, Tokens Studio for Figma and Figma Variables all read
it. Three top-level groups matching the three layers. Aliases use
`{dot.path}` syntax.

```json
{
  "$schema": "https://tr.designtokens.org/format/",
  "$description": "MemoryCare design tokens v1.0 — 2026-08-30. Source of truth. Do not hand-edit generated CSS.",

  "primitive": {
    "$description": "Layer 1. Raw values. Never referenced by a component.",
    "color": {
      "olive":      { "500": { "$type": "color", "$value": "#7C8654", "$description": "Brandbook Olive. Decorative only — never carries text." },
                      "700": { "$type": "color", "$value": "#575E3B", "$description": "Deep Olive. WORKING VALUE pending designer confirmation. Interface only, not in the logo." },
                      "800": { "$type": "color", "$value": "#4E5535", "$description": "Deep Olive x0.90 toward black. Hover." },
                      "900": { "$type": "color", "$value": "#474D30", "$description": "Deep Olive x0.82 toward black. Active." } },
      "nude":       { "400": { "$type": "color", "$value": "#F2EADD" },
                      "500": { "$type": "color", "$value": "#EFE5D5", "$description": "Brandbook Nude. PAGE GROUND ONLY." },
                      "600": { "$type": "color", "$value": "#E4D8C4" } },
      "ivory":      { "400": { "$type": "color", "$value": "#F8F6F1" },
                      "500": { "$type": "color", "$value": "#F3F0E9", "$description": "Brandbook Ivory white. RAISED SURFACES + light text on dark." } },
      "anthracite": { "400": { "$type": "color", "$value": "#4A4D51" },
                      "500": { "$type": "color", "$value": "#33373C", "$description": "Brandbook Anthracite." },
                      "600": { "$type": "color", "$value": "#292C30" },
                      "mix760": { "$type": "color", "$value": "#606161", "$description": "Anthracite 76% + Nude 24%. Secondary text. 4.87 on Nude." } },
      "white":      { "$type": "color", "$value": "#FFFFFF" },
      "danger":     { "100": { "$type": "color", "$value": "#F6E4E0" },
                      "600": { "$type": "color", "$value": "#8C3A2E", "$description": "ONLY non-brand hue in the system. Form errors and destructive confirmation. Never in marketing surfaces." } }
    },
    "alpha": {
      "anthracite": { "08": { "$type": "color", "$value": "rgba(51,55,60,0.08)" },
                      "12": { "$type": "color", "$value": "rgba(51,55,60,0.12)" },
                      "20": { "$type": "color", "$value": "rgba(51,55,60,0.20)" },
                      "38": { "$type": "color", "$value": "rgba(51,55,60,0.38)" },
                      "60": { "$type": "color", "$value": "rgba(51,55,60,0.60)" } },
      "ivory":      { "12": { "$type": "color", "$value": "rgba(243,240,233,0.12)" },
                      "24": { "$type": "color", "$value": "rgba(243,240,233,0.24)" },
                      "40": { "$type": "color", "$value": "rgba(243,240,233,0.40)" } },
      "olive":      { "12": { "$type": "color", "$value": "rgba(124,134,84,0.12)" },
                      "24": { "$type": "color", "$value": "rgba(124,134,84,0.24)" } },
      "deepolive":  { "08": { "$type": "color", "$value": "rgba(87,94,59,0.08)" },
                      "16": { "$type": "color", "$value": "rgba(87,94,59,0.16)" } }
    },
    "size": {
      "0":   { "$type": "dimension", "$value": "0rem" },
      "0-5": { "$type": "dimension", "$value": "0.125rem" },
      "1":   { "$type": "dimension", "$value": "0.25rem" },
      "2":   { "$type": "dimension", "$value": "0.5rem" },
      "3":   { "$type": "dimension", "$value": "0.75rem" },
      "4":   { "$type": "dimension", "$value": "1rem" },
      "5":   { "$type": "dimension", "$value": "1.25rem" },
      "6":   { "$type": "dimension", "$value": "1.5rem" },
      "8":   { "$type": "dimension", "$value": "2rem" },
      "10":  { "$type": "dimension", "$value": "2.5rem" },
      "12":  { "$type": "dimension", "$value": "3rem" },
      "16":  { "$type": "dimension", "$value": "4rem" },
      "20":  { "$type": "dimension", "$value": "5rem" },
      "24":  { "$type": "dimension", "$value": "6rem" },
      "30":  { "$type": "dimension", "$value": "7.5rem" },
      "40":  { "$type": "dimension", "$value": "10rem" },
      "50":  { "$type": "dimension", "$value": "12.5rem" }
    },
    "radius":   { "0": {"$type":"dimension","$value":"0"},
                  "xs": {"$type":"dimension","$value":"2px"},
                  "sm": {"$type":"dimension","$value":"6px"},
                  "md": {"$type":"dimension","$value":"10px"},
                  "lg": {"$type":"dimension","$value":"14px"},
                  "xl": {"$type":"dimension","$value":"20px"},
                  "2xl":{"$type":"dimension","$value":"28px"},
                  "full":{"$type":"dimension","$value":"9999px"} },
    "border":   { "0":{"$type":"dimension","$value":"0"},
                  "1":{"$type":"dimension","$value":"1px"},
                  "2":{"$type":"dimension","$value":"2px"},
                  "3":{"$type":"dimension","$value":"3px"} },
    "duration": { "instant":{"$type":"duration","$value":"80ms"},
                  "fast":{"$type":"duration","$value":"140ms"},
                  "base":{"$type":"duration","$value":"220ms"},
                  "slow":{"$type":"duration","$value":"320ms"},
                  "slower":{"$type":"duration","$value":"480ms"} },
    "ease":     { "standard":{"$type":"cubicBezier","$value":[0.2,0,0,1]},
                  "decelerate":{"$type":"cubicBezier","$value":[0,0,0,1]},
                  "accelerate":{"$type":"cubicBezier","$value":[0.3,0,1,1]},
                  "gentle":{"$type":"cubicBezier","$value":[0.4,0,0.2,1]} },
    "z":        { "base":{"$type":"number","$value":0},
                  "sticky":{"$type":"number","$value":100},
                  "header":{"$type":"number","$value":200},
                  "dropdown":{"$type":"number","$value":300},
                  "overlay":{"$type":"number","$value":400},
                  "modal":{"$type":"number","$value":410},
                  "toast":{"$type":"number","$value":500},
                  "skiplink":{"$type":"number","$value":600} },
    "fontFamily": {
      "display": { "$type":"fontFamily", "$value":["Gloock","Noto Serif Armenian","Playfair Display","Georgia","serif"] },
      "text":    { "$type":"fontFamily", "$value":["Cabin","Noto Sans Armenian","Noto Sans","system-ui","-apple-system","Segoe UI","sans-serif"],
                   "$description":"Cabin is a SUBSTITUTE for Gill Sans, which is commercial Monotype and unlicensed for web. Label it as such in every document." },
      "mono":    { "$type":"fontFamily", "$value":["ui-monospace","SF Mono","Roboto Mono","monospace"] }
    },
    "fontWeight": { "regular":{"$type":"number","$value":400},
                    "medium":{"$type":"number","$value":500},
                    "semibold":{"$type":"number","$value":600},
                    "bold":{"$type":"number","$value":700} }
  },

  "semantic": {
    "$description": "Layer 2. The decisions. Theme-switchable.",
    "surface": {
      "page":            { "$type":"color", "$value":"{primitive.color.nude.500}" },
      "raised":          { "$type":"color", "$value":"{primitive.color.ivory.500}" },
      "raised-hover":    { "$type":"color", "$value":"{primitive.color.ivory.400}" },
      "sunken":          { "$type":"color", "$value":"{primitive.color.nude.600}" },
      "inverse":         { "$type":"color", "$value":"{primitive.color.anthracite.500}" },
      "inverse-raised":  { "$type":"color", "$value":"{primitive.color.anthracite.400}" },
      "accent-strong":   { "$type":"color", "$value":"{primitive.color.olive.700}" },
      "accent-solid":    { "$type":"color", "$value":"{primitive.color.olive.500}" },
      "accent-wash":     { "$type":"color", "$value":"{primitive.alpha.olive.12}" },
      "scrim":           { "$type":"color", "$value":"rgba(51,55,60,0.72)" },
      "danger-subtle":   { "$type":"color", "$value":"{primitive.color.danger.100}" },
      "media-placeholder": { "$type":"color", "$value":"{primitive.alpha.olive.24}" }
    },
    "text": {
      "primary":     { "$type":"color","$value":"{primitive.color.anthracite.500}",  "$description":"9.61 on page, 10.53 on raised" },
      "secondary":   { "$type":"color","$value":"{primitive.color.anthracite.mix760}","$description":"4.87 on page, 5.34 on raised" },
      "accent":      { "$type":"color","$value":"{primitive.color.olive.700}",       "$description":"5.49 on page, 6.01 on raised" },
      "link":        { "$type":"color","$value":"{primitive.color.olive.700}" },
      "link-hover":  { "$type":"color","$value":"{primitive.color.olive.800}" },
      "on-accent":   { "$type":"color","$value":"{primitive.color.ivory.500}",       "$description":"6.01 on accent-strong" },
      "inverse":     { "$type":"color","$value":"{primitive.color.nude.500}",        "$description":"9.61 on inverse" },
      "danger":      { "$type":"color","$value":"{primitive.color.danger.600}" },
      "disabled":    { "$type":"color","$value":"{primitive.alpha.anthracite.38}",   "$description":"FAILS CONTRAST BY DESIGN. Never the only signal." }
    },
    "border": {
      "subtle":        { "$type":"color","$value":"{primitive.alpha.anthracite.08}" },
      "default":       { "$type":"color","$value":"{primitive.alpha.anthracite.20}" },
      "strong":        { "$type":"color","$value":"{primitive.alpha.anthracite.38}" },
      "accent":        { "$type":"color","$value":"{primitive.color.olive.700}" },
      "decorative":    { "$type":"color","$value":"{primitive.color.olive.500}", "$description":"Ornament only. Never under text." },
      "focus":         { "$type":"color","$value":"{primitive.color.olive.700}" },
      "focus-inverse": { "$type":"color","$value":"{primitive.color.nude.500}" },
      "danger":        { "$type":"color","$value":"{primitive.color.danger.600}" },
      "inverse":       { "$type":"color","$value":"{primitive.alpha.ivory.24}" }
    },
    "elevation": {
      "1": { "$type":"shadow","$value":"0 1px 2px rgba(51,55,60,0.04), 0 0 0 1px rgba(51,55,60,0.06)" },
      "2": { "$type":"shadow","$value":"0 2px 8px rgba(51,55,60,0.06), 0 0 0 1px rgba(51,55,60,0.06)" },
      "3": { "$type":"shadow","$value":"0 8px 24px rgba(51,55,60,0.08), 0 0 0 1px rgba(51,55,60,0.06)" },
      "4": { "$type":"shadow","$value":"0 20px 48px rgba(51,55,60,0.12)" }
    },
    "layout": {
      "container-max":    { "$type":"dimension","$value":"1200px" },
      "container-narrow": { "$type":"dimension","$value":"760px" },
      "header-height":    { "$type":"dimension","$value":"64px" },
      "target-min":       { "$type":"dimension","$value":"44px" },
      "focus-width":      { "$type":"dimension","$value":"{primitive.border.2}" },
      "focus-offset":     { "$type":"dimension","$value":"{primitive.border.2}" }
    },
    "motion": {
      "hover":  { "$type":"transition","$value":{"duration":"{primitive.duration.fast}","timingFunction":"{primitive.ease.standard}"} },
      "enter":  { "$type":"transition","$value":{"duration":"{primitive.duration.base}","timingFunction":"{primitive.ease.decelerate}"} },
      "exit":   { "$type":"transition","$value":{"duration":"{primitive.duration.fast}","timingFunction":"{primitive.ease.accelerate}"} },
      "expand": { "$type":"transition","$value":{"duration":"{primitive.duration.slow}","timingFunction":"{primitive.ease.standard}"} }
    }
  },

  "component": {
    "$description": "Layer 3. The contract with the markup.",
    "button": {
      "primary": {
        "bg":     { "default":{"$type":"color","$value":"{semantic.surface.accent-strong}"},
                    "hover":  {"$type":"color","$value":"{primitive.color.olive.800}"},
                    "active": {"$type":"color","$value":"{primitive.color.olive.900}"},
                    "disabled":{"$type":"color","$value":"{primitive.alpha.anthracite.12}"} },
        "fg":     { "default":{"$type":"color","$value":"{semantic.text.on-accent}"},
                    "disabled":{"$type":"color","$value":"{semantic.text.disabled}"} },
        "radius": { "$type":"dimension","$value":"{primitive.radius.md}" },
        "min-height": { "$type":"dimension","$value":"48px" },
        "padding-inline": { "$type":"dimension","$value":"{primitive.size.6}" }
      }
    }
  }
}
```

Build: `style-dictionary build --config tokens/sd.config.js` emits
`mc-tokens.css`, `mc-tokens.scss`, `tailwind.tokens.js` and `tokens.d.ts`.
**Generated files are committed but never hand-edited**; a pre-commit hook
rebuilds and fails if the output drifts.

### A3.2 `tokens/mc-tokens.css` — the production file

```css
/* MemoryCare design tokens v1.0 — GENERATED from tokens/tokens.json. Do not edit. */

:root {
  /* ---------- Layer 1 · primitive · colour ---------- */
  --mc-color-olive-500: #7C8654;
  --mc-color-olive-700: #575E3B;
  --mc-color-olive-800: #4E5535;
  --mc-color-olive-900: #474D30;
  --mc-color-nude-400: #F2EADD;
  --mc-color-nude-500: #EFE5D5;
  --mc-color-nude-600: #E4D8C4;
  --mc-color-ivory-400: #F8F6F1;
  --mc-color-ivory-500: #F3F0E9;
  --mc-color-anthracite-400: #4A4D51;
  --mc-color-anthracite-500: #33373C;
  --mc-color-anthracite-600: #292C30;
  --mc-color-anthracite-mix760: #606161;
  --mc-color-white: #FFFFFF;
  --mc-color-danger-100: #F6E4E0;
  --mc-color-danger-600: #8C3A2E;

  --mc-alpha-anthracite-08: rgba(51,55,60,.08);
  --mc-alpha-anthracite-12: rgba(51,55,60,.12);
  --mc-alpha-anthracite-20: rgba(51,55,60,.20);
  --mc-alpha-anthracite-38: rgba(51,55,60,.38);
  --mc-alpha-anthracite-60: rgba(51,55,60,.60);
  --mc-alpha-ivory-12: rgba(243,240,233,.12);
  --mc-alpha-ivory-24: rgba(243,240,233,.24);
  --mc-alpha-ivory-40: rgba(243,240,233,.40);
  --mc-alpha-olive-12: rgba(124,134,84,.12);
  --mc-alpha-olive-24: rgba(124,134,84,.24);
  --mc-alpha-deepolive-08: rgba(87,94,59,.08);
  --mc-alpha-deepolive-16: rgba(87,94,59,.16);

  /* ---------- Layer 1 · primitive · size ---------- */
  --mc-size-0: 0rem;      --mc-size-0-5: .125rem; --mc-size-1: .25rem;
  --mc-size-2: .5rem;     --mc-size-3: .75rem;    --mc-size-4: 1rem;
  --mc-size-5: 1.25rem;   --mc-size-6: 1.5rem;    --mc-size-8: 2rem;
  --mc-size-10: 2.5rem;   --mc-size-12: 3rem;     --mc-size-16: 4rem;
  --mc-size-20: 5rem;     --mc-size-24: 6rem;     --mc-size-30: 7.5rem;
  --mc-size-40: 10rem;    --mc-size-50: 12.5rem;

  --mc-radius-0: 0;   --mc-radius-xs: 2px;  --mc-radius-sm: 6px;
  --mc-radius-md: 10px; --mc-radius-lg: 14px; --mc-radius-xl: 20px;
  --mc-radius-2xl: 28px; --mc-radius-full: 9999px;

  --mc-border-0: 0; --mc-border-1: 1px; --mc-border-2: 2px; --mc-border-3: 3px;

  --mc-duration-instant: 80ms; --mc-duration-fast: 140ms;
  --mc-duration-base: 220ms;   --mc-duration-slow: 320ms;
  --mc-duration-slower: 480ms;
  --mc-ease-standard:   cubic-bezier(.2,0,0,1);
  --mc-ease-decelerate: cubic-bezier(0,0,0,1);
  --mc-ease-accelerate: cubic-bezier(.3,0,1,1);
  --mc-ease-gentle:     cubic-bezier(.4,0,.2,1);

  --mc-z-base: 0; --mc-z-sticky: 100; --mc-z-header: 200; --mc-z-dropdown: 300;
  --mc-z-overlay: 400; --mc-z-modal: 410; --mc-z-toast: 500; --mc-z-skiplink: 600;

  --mc-font-display: "Gloock", "Noto Serif Armenian", "Playfair Display", Georgia, serif;
  --mc-font-text: "Cabin", "Noto Sans Armenian", "Noto Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mc-font-mono: ui-monospace, "SF Mono", "Roboto Mono", monospace;
  --mc-weight-regular: 400; --mc-weight-medium: 500;
  --mc-weight-semibold: 600; --mc-weight-bold: 700;

  /* ---------- Layer 2 · semantic ---------- */
  --mc-surface-page: var(--mc-color-nude-500);
  --mc-surface-raised: var(--mc-color-ivory-500);
  --mc-surface-raised-hover: var(--mc-color-ivory-400);
  --mc-surface-sunken: var(--mc-color-nude-600);
  --mc-surface-inverse: var(--mc-color-anthracite-500);
  --mc-surface-inverse-raised: var(--mc-color-anthracite-400);
  --mc-surface-accent-strong: var(--mc-color-olive-700);
  --mc-surface-accent-solid: var(--mc-color-olive-500);
  --mc-surface-accent-wash: var(--mc-alpha-olive-12);
  --mc-surface-scrim: rgba(51,55,60,.72);
  --mc-surface-danger-subtle: var(--mc-color-danger-100);
  --mc-surface-media-placeholder: var(--mc-alpha-olive-24);

  --mc-text-primary: var(--mc-color-anthracite-500);
  --mc-text-secondary: var(--mc-color-anthracite-mix760);
  --mc-text-accent: var(--mc-color-olive-700);
  --mc-text-link: var(--mc-color-olive-700);
  --mc-text-link-hover: var(--mc-color-olive-800);
  --mc-text-on-accent: var(--mc-color-ivory-500);
  --mc-text-inverse: var(--mc-color-nude-500);
  --mc-text-danger: var(--mc-color-danger-600);
  --mc-text-disabled: var(--mc-alpha-anthracite-38);

  --mc-border-subtle: var(--mc-alpha-anthracite-08);
  --mc-border-default: var(--mc-alpha-anthracite-20);
  --mc-border-strong: var(--mc-alpha-anthracite-38);
  --mc-border-accent: var(--mc-color-olive-700);
  --mc-border-decorative: var(--mc-color-olive-500);
  --mc-border-focus: var(--mc-color-olive-700);
  --mc-border-focus-inverse: var(--mc-color-nude-500);
  --mc-border-danger: var(--mc-color-danger-600);
  --mc-border-inverse: var(--mc-alpha-ivory-24);

  --mc-elevation-0: none;
  --mc-elevation-1: 0 1px 2px rgba(51,55,60,.04), 0 0 0 1px rgba(51,55,60,.06);
  --mc-elevation-2: 0 2px 8px rgba(51,55,60,.06), 0 0 0 1px rgba(51,55,60,.06);
  --mc-elevation-3: 0 8px 24px rgba(51,55,60,.08), 0 0 0 1px rgba(51,55,60,.06);
  --mc-elevation-4: 0 20px 48px rgba(51,55,60,.12);
  --mc-elevation-inverse-2: 0 2px 8px rgba(0,0,0,.24);

  --mc-layout-container-max: 1200px;
  --mc-layout-container-narrow: 760px;
  --mc-layout-header-height: 64px;
  --mc-layout-gutter: 16px;
  --mc-layout-margin: 16px;
  --mc-layout-section-block: clamp(3rem, 2rem + 5vw, 7.5rem);
  --mc-layout-target-min: 44px;
  --mc-focus-width: var(--mc-border-2);
  --mc-focus-offset: var(--mc-border-2);

  --mc-motion-hover: var(--mc-duration-fast) var(--mc-ease-standard);
  --mc-motion-enter: var(--mc-duration-base) var(--mc-ease-decelerate);
  --mc-motion-exit: var(--mc-duration-fast) var(--mc-ease-accelerate);
  --mc-motion-expand: var(--mc-duration-slow) var(--mc-ease-standard);
  --mc-motion-distance-sm: 4px;
  --mc-motion-distance-md: 8px;
  --mc-motion-distance-lg: 16px;

  /* ---------- Layer 3 · component (extract) ---------- */
  --mc-button-radius: var(--mc-radius-md);
  --mc-button-min-height: 48px;
  --mc-button-min-height-sm: 40px;
  --mc-button-min-height-lg: 56px;
  --mc-button-padding-inline: var(--mc-size-6);
  --mc-button-gap: var(--mc-size-2);
  --mc-button-primary-bg: var(--mc-surface-accent-strong);
  --mc-button-primary-bg-hover: var(--mc-color-olive-800);
  --mc-button-primary-bg-active: var(--mc-color-olive-900);
  --mc-button-primary-fg: var(--mc-text-on-accent);
  --mc-button-primary-bg-disabled: var(--mc-alpha-anthracite-12);
  --mc-button-primary-fg-disabled: var(--mc-text-disabled);
  --mc-button-secondary-bg: transparent;
  --mc-button-secondary-bg-hover: var(--mc-alpha-deepolive-08);
  --mc-button-secondary-fg: var(--mc-text-accent);
  --mc-button-secondary-border: var(--mc-border-strong);
  --mc-button-secondary-border-hover: var(--mc-border-accent);
  --mc-button-tertiary-fg: var(--mc-text-accent);
  --mc-button-danger-bg: var(--mc-color-danger-600);
  --mc-button-danger-fg: var(--mc-color-white);

  --mc-input-min-height: 48px;
  --mc-input-radius: var(--mc-radius-sm);
  --mc-input-bg: var(--mc-surface-raised);
  --mc-input-bg-disabled: var(--mc-surface-sunken);
  --mc-input-border: var(--mc-border-default);
  --mc-input-border-hover: var(--mc-border-strong);
  --mc-input-border-focus: var(--mc-border-focus);
  --mc-input-border-error: var(--mc-border-danger);
  --mc-input-fg: var(--mc-text-primary);
  --mc-input-placeholder: var(--mc-text-secondary);
  --mc-input-padding-inline: var(--mc-size-4);
  --mc-input-label-gap: var(--mc-size-2);
  --mc-input-help-gap: var(--mc-size-2);

  --mc-card-radius: var(--mc-radius-lg);
  --mc-card-bg: var(--mc-surface-raised);
  --mc-card-border: var(--mc-border-subtle);
  --mc-card-shadow: var(--mc-elevation-1);
  --mc-card-shadow-hover: var(--mc-elevation-2);
  --mc-card-padding: var(--mc-size-6);
  --mc-card-padding-lg: var(--mc-size-8);

  --mc-tariff-radius: var(--mc-radius-lg);
  --mc-tariff-border: var(--mc-border-subtle);
  --mc-tariff-border-featured: var(--mc-border-accent);
  --mc-tariff-border-featured-width: var(--mc-border-2);
  --mc-tariff-padding: var(--mc-size-6);
  --mc-tariff-min-height: 480px;

  --mc-badge-radius: var(--mc-radius-full);
  --mc-badge-padding-inline: var(--mc-size-3);
  --mc-badge-min-height: 24px;

  --mc-modal-radius: var(--mc-radius-xl);
  --mc-modal-max-width: 560px;
  --mc-modal-padding: var(--mc-size-8);
  --mc-modal-shadow: var(--mc-elevation-4);

  --mc-toast-radius: var(--mc-radius-md);
  --mc-toast-max-width: 420px;
  --mc-toast-padding: var(--mc-size-4);
}

/* ---------- Responsive layout overrides ---------- */
@media (min-width: 768px) {
  :root { --mc-layout-gutter: 24px; --mc-layout-margin: 32px; }
}
@media (min-width: 1024px) {
  :root { --mc-layout-margin: 48px; --mc-layout-header-height: 76px;
          --mc-button-min-height: 44px; --mc-input-min-height: 44px; }
}

/* ---------- Dark-section scope ----------
   Applied with class, not media query. MemoryCare has no OS dark mode:
   the "dark theme" is a section of the page (hero band, footer, report
   header) and must not flip with the visitor's system setting. */
.mc-on-dark {
  --mc-surface-page: var(--mc-color-anthracite-500);
  --mc-surface-raised: var(--mc-color-anthracite-400);
  --mc-surface-raised-hover: #52565A;
  --mc-surface-sunken: var(--mc-color-anthracite-600);
  --mc-surface-inverse: var(--mc-color-nude-500);
  --mc-text-primary: var(--mc-color-nude-500);
  --mc-text-secondary: var(--mc-color-ivory-500);
  --mc-text-accent: var(--mc-color-nude-500);      /* Deep Olive is 1.75 here — banned */
  --mc-text-link: var(--mc-color-nude-500);
  --mc-text-link-hover: var(--mc-color-white);
  --mc-border-subtle: var(--mc-alpha-ivory-12);
  --mc-border-default: var(--mc-alpha-ivory-24);
  --mc-border-strong: var(--mc-alpha-ivory-40);
  --mc-border-focus: var(--mc-border-focus-inverse);
  --mc-elevation-1: var(--mc-elevation-inverse-2);
  --mc-button-primary-bg: var(--mc-color-nude-500);
  --mc-button-primary-bg-hover: var(--mc-color-nude-400);
  --mc-button-primary-bg-active: var(--mc-color-ivory-400);
  --mc-button-primary-fg: var(--mc-color-anthracite-500);
  --mc-button-secondary-fg: var(--mc-color-nude-500);
  --mc-button-secondary-bg-hover: var(--mc-alpha-ivory-12);
  --mc-input-bg: var(--mc-alpha-ivory-12);
}

/* ---------- Global accessibility primitives ---------- */
*:focus-visible {
  outline: var(--mc-focus-width) solid var(--mc-border-focus);
  outline-offset: var(--mc-focus-offset);
  border-radius: var(--mc-radius-xs);
}
/* Focus on a Deep Olive fill: the ring must not disappear into the button.
   Two rings — inner ivory, outer deep olive. */
.mc-button--primary:focus-visible {
  outline: var(--mc-focus-width) solid var(--mc-color-ivory-500);
  outline-offset: calc(-1 * var(--mc-focus-width) - 1px);
  box-shadow: 0 0 0 4px var(--mc-alpha-deepolive-16);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --mc-duration-instant: 1ms; --mc-duration-fast: 1ms;
    --mc-duration-base: 1ms; --mc-duration-slow: 1ms; --mc-duration-slower: 1ms;
    --mc-motion-distance-sm: 0px; --mc-motion-distance-md: 0px; --mc-motion-distance-lg: 0px;
  }
  *, *::before, *::after {
    animation-duration: 1ms !important; animation-iteration-count: 1 !important;
    transition-duration: 1ms !important; scroll-behavior: auto !important;
  }
}
```

**Reduced motion is not "animations off".** Opacity cross-fades stay, at 1ms so
they are instant; translate distances collapse to 0; the only thing genuinely
removed is the gallery auto-advance and the calculator number roll-up, which
snap to their end value.

### A3.3 Breakpoints and grid

| Name | Min width | Columns | Gutter | Page margin | Notes |
|---|---|---|---|---|---|
| `base` | 360px | 4 | 16px | 16px | **Design and QA target. Not 375.** Older Android phones in the diaspora. |
| `sm` | 480px | 4 | 16px | 24px | Large phones |
| `md` | 768px | 8 | 24px | 32px | Tablet, 2-up tariff cards |
| `lg` | 1024px | 12 | 24px | 48px | Desktop, 3-up tariff cards |
| `xl` | 1280px | 12 | 24px | auto (centred, max 1200) | |
| `2xl` | 1440px | 12 | 24px | auto | No new layout, only more air |

Container: `width: 100%; max-width: var(--mc-layout-container-max); margin-inline: auto; padding-inline: var(--mc-layout-margin);`

Media queries are **min-width only**. No max-width queries anywhere except the
two documented exceptions: hiding the desktop nav, and the calculator's
stacked-slider layout.

---

### A3.4 Type: the two open problems, answered

The brief is right that this pair cannot ship as-is. The system answers both at
Layer 1 so the answer is one line to change:

**Problem 1 — Gill Sans is commercial.** Substitute **Cabin** (Google Fonts,
OFL). Cabin's stated design brief is a humanist sans in the Gill Sans /
Johnston tradition; its humanist axis and open apertures are the closest free
match. **Every mock, PDF and this document label it "Cabin — substitute for
Gill Sans".** If the owner later buys the Monotype web licence, the change is
`--mc-font-text`, one line, nothing else.

**Problem 2 — neither face covers Armenian, and Gloock does not cover Cyrillic
either.** This is worse than the brief states: Gloock ships Latin and Latin-ext
only, so the **Russian** headings fall back too, not just the Armenian ones.
Per-script stacks, declared once:

| Locale | Display | Text |
|---|---|---|
| `en` | Gloock | Cabin |
| `hy` | **Noto Serif Armenian** 400/600 | **Noto Sans Armenian** 400/600 |
| `ru` | **Playfair Display** 400 (high-contrast serif, closest Gloock analogue with Cyrillic) | **Noto Sans** 400/600 |

Implemented with `unicode-range` on `@font-face` so a mixed-script string (an
Armenian name inside an English sentence — this happens constantly here) picks
the right face per glyph with no developer effort:

```css
@font-face { font-family:"Gloock"; src:url("/fonts/gloock-400.woff2") format("woff2");
  font-weight:400; font-display:swap; unicode-range:U+0000-00FF,U+0100-017F,U+2000-206F; }
@font-face { font-family:"Noto Serif Armenian"; src:url("/fonts/noto-serif-armenian-400.woff2") format("woff2");
  font-weight:400; font-display:swap; unicode-range:U+0530-058F,U+FB13-FB17; }
@font-face { font-family:"Playfair Display"; src:url("/fonts/playfair-400-cyrillic.woff2") format("woff2");
  font-weight:400; font-display:swap; unicode-range:U+0400-04FF; }
```

Fonts are **self-hosted**, not loaded from `fonts.googleapis.com`: the diaspora
audience includes Russia, where Google Fonts is unreliable, and the bank's
review disliked third-party requests. Subset per locale, `woff2` only, preload
the two faces the current locale actually uses.

Total font budget: **≤ 180 KB per locale**, enforced in CI.

---

### A3.5 Accessibility encoded in the system

**Allowed contrast pairs — this is the whole permission list.** A combination
not on this table does not exist in the system, and the linter rejects it.

| Foreground token | Background token | Ratio | Permitted for |
|---|---|---|---|
| `text-primary` | `surface-page` | 9.61 | all text |
| `text-primary` | `surface-raised` | 10.53 | all text |
| `text-secondary` | `surface-page` | 4.87 | all text |
| `text-secondary` | `surface-raised` | 5.34 | all text |
| `text-accent` | `surface-page` | 5.49 | all text |
| `text-accent` | `surface-raised` | 6.01 | all text |
| `text-on-accent` | `surface-accent-strong` | 6.01 | all text |
| `color-white` | `surface-accent-strong` | 6.84 | all text |
| `text-inverse` | `surface-inverse` | 9.61 | all text |
| `text-danger` | `surface-page` | 6.09 | all text |
| `text-danger` | `surface-danger-subtle` | ≈5.6 | all text |
| ~~any~~ | `surface-accent-solid` (Olive) | ≤3.42 | **NO TEXT. EVER.** |
| `text-accent` | `surface-inverse` | 1.75 | **BANNED** |
| `surface-accent-solid` | any | ≤3.42 | decorative shapes ≥ 3:1 non-text only |

Encoded three ways so it cannot be violated by accident:
1. `.mc-on-dark` reassigns `--mc-text-accent` to Nude, so a component written
   once works on both grounds without the developer knowing Deep Olive is banned
   on Anthracite.
2. A Stylelint plugin (`stylelint-mc-contrast`, ships in the package) fails the
   build on any `color`/`background-color` pair not in this table.
3. `qa/contrast.spec.ts` — a Playwright axe-core run over every route at 360px
   and 1280px, in all three locales. Zero serious/critical violations is a
   merge gate.

**Focus.** `:focus-visible` only, never `:focus` — mouse users must not see
rings. 2px ring, 2px offset, `--mc-border-focus`. On Deep Olive fills the ring
inverts to inner-Ivory + outer halo (written out in A3.2). On the Anthracite
band the ring is Nude. **The ring is never removed, including on the language
switcher, the calculator sliders and the gallery thumbnails.**

**Target size.** Everything interactive is ≥ 44×44 CSS px in its hit area, even
where the visual is smaller. Small visuals get the area back with a
pseudo-element:

```css
.mc-hit-44 { position: relative; }
.mc-hit-44::after {
  content: ""; position: absolute; inset: 50% 50% 50% 50%;
  width: max(100%, var(--mc-layout-target-min));
  height: max(100%, var(--mc-layout-target-min));
  transform: translate(-50%, -50%);
}
```

Adjacent targets keep ≥ 8px of clear space. Applies to: gallery thumbnails,
close buttons, the language switcher, calculator slider handles, table row
actions in the visit list.

**Other system-level rules.**
- Skip link, first focusable element, `--mc-z-skiplink`.
- One `<h1>` per route; heading levels never skip.
- Every icon-only control has `aria-label` sourced from the string file, never
  hard-coded.
- Colour is never the only carrier of meaning: report status is icon + word,
  the featured tariff is a border + a badge with words, form errors are a red
  border + an icon + a sentence.
- `prefers-reduced-transparency` → `backdrop-filter` on the sticky header falls
  back to solid `--mc-surface-page`.
- Minimum text size 16px on the site, 15px in dense portal tables — never lower.
- Zoom to 200% at 360px must not produce horizontal scroll on any route.

---

## A4. Component specifications

Common to all: dimensions in CSS px; every component has `default hover active
focus-visible disabled` at minimum; `loading`, `error`, `selected`, `empty`
where marked. Each ships as `components/SPEC-<name>.md` with the same table plus
markup skeleton and ARIA.

### A4.1 Button

| Property | sm | md (default) | lg |
|---|---|---|---|
| Min height (mobile / ≥1024) | 40 / 36 | **48 / 44** | 56 / 52 |
| Padding inline | 16 | 24 | 32 |
| Font | `type.label` 14 | `type.label` 15 | `type.body` 16 |
| Icon size | 16 | 20 | 20 |
| Gap icon↔label | 8 | 8 | 12 |
| Radius | `radius-md` 10 | `radius-md` 10 | `radius-md` 10 |
| Hit area | 44×44 min in all sizes | | |

Variants and states:

| Variant | default | hover | active | focus-visible | disabled | loading |
|---|---|---|---|---|---|---|
| **primary** | bg `olive-700`, fg Ivory | bg `olive-800`, `translateY(-1px)` | bg `olive-900`, `translateY(0)` | inner Ivory ring + `deepolive-16` halo | bg `anthracite-12`, fg `anthracite-38`, no shadow, `cursor:default` | spinner 16px replaces icon, label stays, width locked, `aria-busy="true"` |
| **secondary** | transparent, 1px `border-strong`, fg `olive-700` | bg `deepolive-08`, border `olive-700` | bg `deepolive-16` | standard ring | border `anthracite-12`, fg `anthracite-38` | as above |
| **tertiary** (text) | fg `olive-700`, underline `1px` offset `3px` | fg `olive-800`, underline 2px | fg `olive-900` | standard ring | fg `anthracite-38`, no underline | — |
| **danger** | bg `danger-600`, fg white (6.84) | 90% toward black | 82% | standard ring | as primary | as primary |
| **primary-inverse** (on `.mc-on-dark`) | bg Nude, fg Anthracite (9.61) | bg `nude-400` | bg `ivory-400` | Nude ring, offset 2 | bg `ivory-12`, fg `ivory-40` | as primary |
| **secondary-inverse** | transparent, 1px `ivory-40`, fg Nude | bg `ivory-12` | bg `ivory-24` | Nude ring | — | — |

Motion: `transition: background-color var(--mc-motion-hover), transform var(--mc-motion-hover), box-shadow var(--mc-motion-hover)`. Translate on hover is 1px, not 2 — 2px was the old build and reads as a consumer app.

Rules: never two primary buttons in one viewport section. The primary CTA is
always **Request a free consultation**. **Pay online** is always `secondary`,
never primary, until acquiring is live.

Full-width: `.mc-button--block` below `md` for every form submit and every
tariff card CTA.

### A4.2 Text input / textarea / phone

| Property | Value |
|---|---|
| Min height | 48 mobile / 44 ≥1024 (textarea min 120) |
| Padding | `12px 16px` |
| Radius | `radius-sm` 6 |
| Border | 1px `border-default` → hover `border-strong` → focus 2px `border-focus` (inset, so height does not jump: `box-shadow: inset 0 0 0 2px`) |
| Background | `surface-raised` |
| Font | `type.body` 16 — **16px minimum prevents iOS auto-zoom on focus** |
| Label | `type.label`, above the field, gap 8, `--mc-text-primary`. **Always visible.** No placeholder-as-label — the audience is 40–60 and half the fields are in a second language. |
| Help text | `type.caption`, gap 8 below, `--mc-text-secondary` |
| Error text | `type.caption`, `--mc-text-danger`, with a 16px alert icon, gap 8 |
| Required | asterisk in `--mc-text-danger` + the word (localised) in the label, never asterisk alone |

States: `default · hover · focus · filled · disabled` (bg `surface-sunken`, fg
`text-disabled`, border `anthracite-12`) `· readonly` (no border, bg
transparent) `· error` (border `border-danger` 2px inset, `aria-invalid="true"`,
error text linked by `aria-describedby`) `· success` (border `border-accent`,
check icon; used only after async validation such as an email check).

Validation timing is a system rule, not Igor's choice: **validate on blur, never
on keystroke; re-validate on keystroke only after the field has already
errored.** Error messages appear below, never as a tooltip, never as a toast.

**Phone field.** `type="tel"`, `inputmode="tel"`, `autocomplete="tel"`.
Country-code selector on the inline-start, 88px wide, showing dial code and
ISO code as text (`+374 AM`) — **not a flag alone**, flags are ambiguous for
diaspora users holding two passports. Default country by IP with a visible,
changeable value; never locked. Accepts and preserves any of
`+1 818 555 0134`, `+33 6 12 34 56 78`, `+374 93 154 108`, `0093154108`.
Stores E.164. Never rejects on format before submit.

### A4.3 Select

Native `<select>` on `base`/`sm` (mobile pickers are better than anything we
build). Custom listbox from `md` up.

| Property | Value |
|---|---|
| Trigger | identical box metrics to text input |
| Chevron | 16px, `--mc-text-secondary`, inline-end 16, rotates 180° over `motion.hover` |
| Menu | `surface-raised`, `radius-md`, `elevation-3`, max-height 320, scroll, offset 4 from trigger, min-width = trigger width |
| Option | min-height 44, padding `10px 16px`, `type.body` |
| Option hover | bg `deepolive-08` |
| Option selected | bg `deepolive-16`, check icon 16 inline-end, `aria-selected="true"` |
| Option focused (keyboard) | 2px inset `border-focus` |
| Group label | `type.overline`, `--mc-text-secondary`, padding `12px 16px 4px`, non-selectable |
| Empty | "No matches" in `--mc-text-secondary`, min-height 44 |

Keyboard: full ARIA listbox pattern — ↑↓ Home End, type-ahead, Esc closes and
returns focus, Enter/Space selects. Type-ahead must match on the **localised**
label, not the value.

### A4.4 Checkbox

| Property | Value |
|---|---|
| Box | 20×20, `radius-xs` 2, border 2px `border-strong`, bg `surface-raised` |
| Hit area | 44×44 (row is clickable, label included) |
| Checked | bg `olive-700`, border `olive-700`, check glyph Ivory, 12px stroke 2 |
| Indeterminate | bg `olive-700`, 10×2 Ivory bar |
| Hover | border `olive-700`; checked → bg `olive-800` |
| Focus | 2px `border-focus` ring, offset 2 |
| Disabled | border `anthracite-20`, bg `surface-sunken`; checked-disabled bg `anthracite-38` |
| Error | border `border-danger` (used for the required consent checkbox) |
| Label | `type.body`, gap 12, aligned to the box's optical centre, wraps freely — Armenian consent copy runs three lines on a phone |
| Motion | check draws over `duration.fast`; box colour over `motion.hover` |

### A4.5 Radio

Identical metrics to checkbox but `radius-full` and a 8px Ivory dot on
`olive-700`. Group is `role="radiogroup"` with a `<legend>`. Arrow keys move
selection; Tab enters and leaves the group. Used for: subscription tier choice
in the portal, "who should receive the visit reminder" in Family Circle.

**Radio-card variant** (used by the tariff chooser inside the portal): the whole
card is the control — border 1px `border-subtle` → selected 2px `border-accent`
+ bg `deepolive-08`, radio dot top-inline-end, min-height 96.

### A4.6 Card (base)

| Property | base | md+ |
|---|---|---|
| Padding | 20 | 24 (`card-padding-lg` 32 for feature cards) |
| Radius | `radius-lg` 14 | same |
| Background | `surface-raised` | |
| Border | 1px `border-subtle` | |
| Shadow | `elevation-1` | |
| Hover (only if the whole card is a link) | `elevation-2`, `translateY(-2px)`, border `border-default` | |
| Focus-within | standard ring on the card | |

An interactive card exposes exactly one link, wrapping the title, with a
`::after` overlay covering the card ("stretched link"). Nested links inside a
stretched-link card are forbidden — this is where developers usually create
un-clickable buttons.

### A4.7 Tariff card

The most load-bearing component on the site. Fixed anatomy, top to bottom:

```
[ eyebrow badge (optional, 24h) ]
[ name           type.heading-2, display face ]
[ one-line description   type.body-sm, text-secondary, 2 lines max ]
[ ── divider 1px border-subtle, margin-block 20 ── ]
[ price block ]
    amount     type.price, display face, text-primary
    currency   "֏ AMD"  type.body, text-secondary, baseline-aligned
    period     type.body-sm, text-secondary, own line
[ CTA button, block, primary or secondary ]
[ ── divider ── ]
[ inclusions list — icon 16 olive-700 + type.body-sm, gap 12, row gap 12 ]
[ footnote  type.caption, text-secondary, mt auto ]
```

| Property | Value |
|---|---|
| Min height | 480 (`--mc-tariff-min-height`), equalised across the row by grid, never by JS |
| Padding | 24 mobile / 32 ≥1024 |
| Radius | `radius-lg` |
| Border | 1px `border-subtle` |
| Featured border | 2px `border-accent` (Deep Olive), no shadow change |
| Featured badge | `Badge--accent`: **Deep Olive fill, Ivory label (6.01)**. Not an Olive fill — Anthracite on Olive is 3.08 and Ivory on Olive is 3.42, so no label is legible on an Olive chip at any size. |
| CTA | featured card = `primary`; others = `secondary` |
| Gap between cards | 16 base / 24 md / 24 lg |

Layout: 1-up `base`, 2-up `md`, 3-up `lg` for **Express / Optimal / Maximum**.

**Inspection is a different component.** `TariffCard--standalone`: full-width,
horizontal at `md`+, `surface-sunken` background instead of `surface-raised`, no
shadow, `radius-lg`, a 1px `border-decorative` top rule, and it is placed
**above** the three-card row with the section label "One-off services" and its
own heading. It never sits in the same grid as the annual packages. Its price
block reads `20,000 ֏ AMD` with **no period line** — the absence of "/year" is
the design's way of saying one-off, reinforced by the copy slot.

**Special** is a fifth card in the row's footer position: no price, the string
"By calculator", CTA `secondary` scrolling to the calculator.

Hard content rules encoded in the component: there is **no `period` value
"month"** in the type — the union is `"year" | "one-off" | null`. There is no
`bestseller` prop; the featured flag is `emphasis: "leading"` and its badge
string comes from the string file (`tariff.badge.leading`). There is no
`visitType` value `"light"` or `"preventive"` — the only value is `"full"`.
These are TypeScript unions in `tokens.d.ts`, so a wrong value fails the build.

### A4.8 Plot calculator

| Element | Spec |
|---|---|
| Container | Card, `card-padding-lg`, `surface-raised`, max-width 720 centred |
| Slider track | height 4, `radius-full`, bg `border-default`; filled portion `surface-accent-strong` |
| Slider handle | 28×28 circle, bg `surface-raised`, 2px border `olive-700`, `elevation-2`; hit area 44×44; focus = 2px ring offset 2 + halo `deepolive-16` |
| Handle hover / active | scale 1.06 / 0.98 over `motion.hover` |
| Value readout | `type.heading-3`, inline-end of the label row, tabular numerals |
| Numeric input | Every slider is paired with a **number input** of identical value (48 tall, 96 wide, `type.numeric`). Sliders alone are unusable for a 55-year-old on a phone. |
| Steps | Area: 1 m², range 1–100, default 16. Monuments: 1, range 1–10, default 2. |
| Tick labels | Min, the free threshold (16 m² / 2 monuments) and max only |
| Threshold marker | 2px `border-decorative` vertical rule at 16 m² and at 2 monuments, with a `type.caption` label "included" |
| Result block | `surface-sunken`, `radius-md`, padding 20, separated by 24 |
| Result rows | Optimal and Maximum, each: name, base price, surcharge lines, total. Surcharge lines appear **only when non-zero**, animate in with `motion.enter` |
| Total | `type.price`, updates with a 220ms count-up; **snaps instantly under `prefers-reduced-motion`** |
| Express row | shown separately, labelled one-off, with its own surcharge rates |
| Over-ceiling state | Above 100 m² or 10 monuments the result block swaps to a `secondary` panel: explanatory sentence + primary CTA to consultation + secondary CTA to Inspection. Sliders clamp; they do not disable. |
| Live region | The total sits in `aria-live="polite" aria-atomic="true"`; sliders are `role="slider"` with `aria-valuetext` = the formatted price, so a screen-reader user hears the money, not "37" |
| Layout | Sliders stacked at all widths; result block below at `base`/`md`, alongside at `lg` (7/5 columns) |

Surcharge arithmetic is in the spec, not in Igor's head:
`annual_total = base + max(0, area − 16) × 10000 + max(0, monuments − 2) × 30000`
`express_total = 65000 + max(0, area − 16) × 2500 + max(0, monuments − 2) × 7500`

Currency formatting is a shared utility: grouped with a non-breaking thin space
(`160 000 ֏ AMD`), never a comma in `hy`/`ru`. Both the symbol and the letters
appear — a bank requirement.

### A4.9 Report card (the product)

Used in the visit list and as the sharable report header. Block order is fixed
and is a brand rule, not a layout preference:

```
1  STATUS ROW      icon 20 + word ("Visit completed") + date, type.label
2  PLOT LINE       cemetery · sector · plot, type.body-sm, text-secondary
3  CONFIRMATION    "GPS confirmed" chip + crew name, type.caption
   ── divider ──
4  PHOTOGRAPHS     gallery, 3:2, first image = the plot AFTER the visit
5  NOTES           crew note, type.body, container-narrow
6  VIDEO           optional, 16:9 poster with a play affordance
7  ACTIONS         Share link (secondary) · Download PDF (tertiary)
```

**Never open with a side-by-side before/after.** That composition is
cleaning-product advertising. Before-images live inside the gallery, labelled,
from position 2 onward.

| Property | Value |
|---|---|
| Container | Card, radius `lg`, padding 20/24 |
| Status icon — completed | check-in-circle, `--mc-text-accent` |
| Status icon — scheduled | calendar, `--mc-text-secondary` |
| Status icon — postponed | clock, `--mc-text-secondary`, badge `warning` |
| Status icon — access blocked | info, `--mc-text-danger`, badge `danger` |
| GPS chip | `surface-accent-wash`, `radius-full`, 24h, padding-inline 12, `type.caption`, Anthracite label (Olive wash at 12% keeps 8.9 contrast) |
| Loading | Skeleton: 3 grey bars + a 3:2 block, `surface-sunken`, shimmer 1400ms — **shimmer disabled under reduced motion** |
| Empty (no visits yet) | Illustration placeholder + heading + body + secondary CTA. Copy slot is `report.empty.*`; see §C. |
| Error | Card with a calm sentence and a "Try again" secondary button. **The string file has no emoji and no "Oops".** Enforced by a lint rule on the string files. |

### A4.10 Gallery

| Property | Value |
|---|---|
| Aspect ratio | **3:2 for plot photography, 16:9 for video, 1:1 never** |
| Grid | 1-up base; 2-up md; 3-up lg; gap 8/12/16 |
| Thumbnail radius | `radius-md` |
| Caption | Below the image, `type.caption`, `--mc-text-secondary`; every image is captioned with what it shows and its timestamp. Never a black bar over the photo. |
| Loading | `surface-sunken` block at the exact aspect ratio; `width`/`height` attributes always present — no layout shift on a slow diaspora connection |
| Lightbox | Scrim `surface-scrim`, image `max-height: 88vh`, controls 44×44, counter `type.caption`, Esc closes, arrows navigate, focus trapped, focus returns to the thumbnail |
| Zoom | Pinch on touch, double-click on desktop, max 3× |
| Autoplay | None. Nothing on this site moves on its own. |
| Placeholder (pre-September) | `surface-media-placeholder` block at the correct ratio with a centred `type.caption` label stating the intended content, e.g. `PHOTO · Plot after visit · 3:2 · 1600×1067 · replace after 09.2026 shoot`. Ships as an SVG in `placeholders/`. |

**Photo framing rules that belong to the system, not the photographer's taste:**
no black borders, no vignettes, no grayscale, no drop shadows on photographs, no
"before" and "after" text burned into the image, headstone inscriptions must be
legible at the 3:2 crop.

### A4.11 Badge

| Variant | bg | fg | Use |
|---|---|---|---|
| `neutral` | `surface-sunken` | `text-primary` | counts, plain labels |
| `accent` | `surface-accent-strong` (Deep Olive) | Ivory (6.01) | "Most chosen" on the featured tariff |
| `accent-soft` | `surface-accent-wash` (Olive 12%) | `text-primary` (8.9) | "GPS confirmed", "Included" |
| `warning` | `nude-600` | `text-primary` (8.2) | "Postponed — weather" |
| `danger` | `surface-danger-subtle` | `text-danger` (5.6) | "Could not access plot" |
| `inverse` | `alpha-ivory-24` | Nude | badges on the dark band |

Metrics: min-height 24, `radius-full`, padding-inline 12 (10 with a leading
icon), `type.caption` 13/600, icon 14, gap 6, `white-space: nowrap`,
`max-width: 100%` with ellipsis after 28 characters. A badge is never
interactive; if it needs a click it is a button.

**There is no Olive-fill badge with a light label.** It fails at 3.42 and was
the single most likely mistake in this palette.

### A4.12 Navigation (site header)

| Property | base–md | lg+ |
|---|---|---|
| Height | 64 | 76 |
| Background | `surface-page` at 92% + `backdrop-filter: blur(12px)`; solid fallback | same |
| Bottom border | 1px `border-subtle`, appears only after 8px scroll, fades over `motion.hover` | same |
| Logo | horizontal lock-up, 32 tall (see §E) | 36 tall |
| Links | in drawer | inline, gap 32, `type.body-sm`, `--mc-text-secondary`, hover `--mc-text-primary` with a 1px `border-decorative` underline animating in from the inline-start over `motion.hover` |
| Active link | `--mc-text-primary`, persistent underline, `aria-current="page"` |
| Language switcher | 3 segments `ARM · ENG · РУС`, `radius-full`, 1px `border-default`, each 44×36 min (44×44 hit), selected = `surface-accent-strong` + Ivory, `aria-pressed`. **Written in each language's own script**, never as flags. | same |
| CTA | `primary` `sm`, hidden below `md` (the sticky mobile CTA bar covers it) | visible |
| Menu button | 44×44, hamburger 20×14, 2px bars | hidden |
| Drawer | Full-height sheet from inline-end, width `min(88vw, 360px)`, `surface-raised`, `elevation-4`, slides over `motion.enter`, scrim `surface-scrim`, focus trapped, body scroll locked, Esc closes, items 56 tall, language switcher and phone number pinned at the bottom | — |

**Sticky mobile CTA bar** (`base`–`sm` only): fixed to the block-end, 72 tall,
`surface-raised`, top border 1px `border-subtle`, containing a block `primary`
button and a 44×44 phone-call icon button. Appears after the hero leaves the
viewport, hides while a form field has focus (it must never cover the keyboard's
target), respects `env(safe-area-inset-bottom)`.

### A4.13 Footer

Bank requirement: **contacts appear in the footer of every page.** Structure is
therefore fixed, not per-page.

| Property | Value |
|---|---|
| Background | `surface-inverse` (Anthracite), scoped `.mc-on-dark` |
| Padding block | 64 / 80 lg |
| Columns | 1 (base) → 2 (md) → 4 (lg): Brand · Product · Legal · Contact |
| Logo | horizontal lock-up, `light` version, 32 tall |
| Tagline | `HONORING MEMORY, CARING FOR LOVED ONES`, `type.overline`, **Olive is unreadable here (3.08) — the tagline in the footer is set in Nude**, letterspaced 0.14em. Olive tagline is a print/logo treatment only. |
| Link | `type.body-sm`, Nude, hover white + underline |
| Contacts block | Both names and roles, both phone numbers as `tel:` links, `info@memorycare.am` as `mailto:`, legal entity name, legal address, VAT/registration number |
| Legal address | `PLACEHOLDER — legal address pending` rendered in a visibly bracketed style and listed in `OPEN-ITEMS.md`. Never invented. |
| Legal links | Privacy policy · Refund policy · Terms of service · Service limitations — all four, every page |
| Payment note | "Card payments are not yet enabled. First subscriptions are settled by bank transfer." — only while true; the string is flagged `temporary: true` in the string file |
| Social | Only links that exist. No dead icons. If a network has no account, the icon is absent, not greyed. |
| Copyright | `© 2026 MemoryCare LLC`, `type.caption`, Nude |

### A4.14 Modal / sheet

| Property | base | md+ |
|---|---|---|
| Form | Bottom sheet, full width, `radius-xl` block-start corners only, `max-height: 92dvh`, drag-handle 36×4 `border-strong` | Centred dialog, `max-width: 560` (`720` for the report share), `radius-xl` |
| Padding | 24 | 32 |
| Enter | translateY 100% → 0, `motion.enter` | opacity 0→1 + `translateY(8px)→0`, `motion.enter` |
| Exit | reverse, `motion.exit` | reverse |
| Scrim | `surface-scrim`, fades over `motion.enter` | same |
| Header | Title `type.heading-2`, close 44×44 inline-end | same |
| Footer | Actions stacked, primary first (top) on mobile; inline, primary at inline-end on desktop | |
| Body | Scrolls independently; header/footer fixed; 1px `border-subtle` appears on the header when the body is scrolled | |

Behaviour: `role="dialog" aria-modal="true"`, labelled by the title id, focus
moves to the dialog on open and returns to the invoker on close, focus trapped,
Esc closes, background `overflow: hidden` with scroll position preserved,
scrim click closes **except** for destructive confirmations (cancel
subscription), which require an explicit button.

**Never used for:** errors (inline), success confirmation (toast or an inline
panel), marketing interruption (there are no interstitials on this site at all).

### A4.15 Toast

| Property | Value |
|---|---|
| Position | Block-end centre on mobile (above the sticky CTA bar, 88px offset), block-start inline-end on desktop, 24 from the edges |
| Width | `min(92vw, 420px)` |
| Padding | 16 |
| Radius | `radius-md` |
| Background | `surface-raised`, `elevation-3`, 1px `border-subtle`; a 3px `border-decorative` inline-start rule carries the variant colour |
| Variants | `success` (rule `olive-700`, check icon), `info` (rule `border-strong`), `warning` (rule `nude-600`), `error` (rule `danger-600`) |
| Text | Title `type.label`, optional body `type.body-sm` `--mc-text-secondary` |
| Action | one `tertiary` button max, e.g. "Undo" |
| Close | 44×44 |
| Duration | 5000ms; 8000ms with an action; **error toasts never auto-dismiss** |
| Motion | Enter `translateY(8px)` + fade, `motion.enter`; exit `motion.exit`; timer pauses on hover and on focus-within |
| Stack | Max 3; older ones collapse; newest nearest the edge |
| A11y | Container is `role="status" aria-live="polite"`; error variant `role="alert" aria-live="assertive"` |

**Toasts never carry information the user needs to keep.** A failed payment, a
postponed visit or a guarantee-revisit confirmation is a screen or an inline
panel, not a toast.

---

# B. UX implications of the system

Only the places where the system dictates behaviour.

**B1 — Every component ships five states or it is not done.** `default ·
loading · empty · error · success`. A component spec with no empty state is
rejected in review. The portal's first-entry screen is the most important empty
state in the product: the client has just paid and there is nothing to show. It
is a designed screen with the subscription summary, the scheduled first-visit
window and what will arrive, not a blank list.

**B2 — Bad-news screens are first-class components, not error handling.** Three
exist as named specs: `SPEC-status-postponed.md`, `SPEC-status-no-access.md`,
`SPEC-guarantee-revisit.md`. All three use the Report card shell with a
`warning`/`danger` badge, a plain-language sentence, the new date if there is
one, and one action. None of them uses the Toast, the Modal or the generic
error card.

**B3 — Responsive rules that are not negotiable.**
- Design and QA at **360px**, not 375. The diaspora carries older Android.
- Anything below `md` is one column. There are no 2-up grids on a phone
  anywhere, including the gallery.
- Tables do not exist below `md`. The visit list becomes a stack of Report
  cards. A horizontally scrolling table is not an acceptable fallback.
- The sticky mobile CTA bar hides on focus-within of any form.
- Touch and pointer are both supported on every control; nothing is
  hover-only. Every hover affordance has a persistent visible equivalent.
- `dvh`, not `vh`, for anything full-height — mobile browser chrome.
- Images always carry intrinsic `width`/`height`. CLS budget 0.05.

**B4 — Focus order follows the DOM.** No `tabindex` above 0 anywhere in the
codebase. Where the visual order differs from the reading order (the tariff row
at `lg`, the calculator result), the DOM order is the reading order and CSS
reorders, never the reverse.

**B5 — The system has no OS dark mode.** `.mc-on-dark` is a section scope, set
by us. A visitor's system preference must not repaint a page containing
photographs of a grave in colours we did not check.

**B6 — Guest report view is a distinct layout, not a permission flag.** It uses
`ReportCard`, `Gallery` and `Footer`, and it is physically unable to render
`TariffCard`, `Calculator`, `Badge--accent` or any `primary` button: those
components are not imported into that route's bundle. Selling next to a
photograph of a grave cannot happen by accident if the code cannot express it.

**B7 — Link preview.** The OG image for a shared report is a static
`brand/og/report-share.png` — mark, the words "Visit report", the date rendered
server-side. **A photograph is never the OG image.** Enforced by a unit test on
the meta tags.

---

# C. Content implications of the system

The system imposes length limits, and they are expressed as data, not as advice.

`content/content-limits.json` — read by the CMS/string-file linter and by a
Storybook add-on that renders every component at its limit in all three
languages:

```json
{
  "$comment": "Max grapheme counts per slot. 'ref' is English. hy/ru are the enforced ceilings — Armenian runs 15-25% and Russian 10-20% longer than English for the same meaning.",
  "nav.item":            { "ref": 16, "hy": 22, "ru": 20, "overflow": "none — shorten the source" },
  "button.label":        { "ref": 22, "hy": 30, "ru": 28, "overflow": "wrap to 2 lines, button grows" },
  "button.label.sticky": { "ref": 18, "hy": 24, "ru": 22, "overflow": "none — single line, fixed bar" },
  "badge.label":         { "ref": 16, "hy": 22, "ru": 20, "overflow": "ellipsis" },
  "tariff.name":         { "ref": 14, "hy": 20, "ru": 18, "overflow": "none" },
  "tariff.description":  { "ref": 74, "hy": 92, "ru": 88, "overflow": "clamp 2 lines" },
  "tariff.inclusion":    { "ref": 58, "hy": 72, "ru": 68, "overflow": "wrap, no clamp" },
  "hero.h1":             { "ref": 62, "hy": 74, "ru": 70, "overflow": "none — the clamp() scale is tuned to this" },
  "hero.subhead":        { "ref": 150, "hy": 185, "ru": 175, "overflow": "wrap" },
  "section.eyebrow":     { "ref": 28, "hy": 34, "ru": 32, "overflow": "wrap" },
  "card.title":          { "ref": 48, "hy": 60, "ru": 56, "overflow": "clamp 2 lines" },
  "form.label":          { "ref": 30, "hy": 40, "ru": 36, "overflow": "wrap" },
  "form.error":          { "ref": 90, "hy": 110, "ru": 105, "overflow": "wrap" },
  "toast.title":         { "ref": 44, "hy": 56, "ru": 52, "overflow": "clamp 2 lines" },
  "report.status":       { "ref": 24, "hy": 32, "ru": 30, "overflow": "none" },
  "gallery.caption":     { "ref": 80, "hy": 100, "ru": 95, "overflow": "clamp 2 lines" },
  "footer.link":         { "ref": 26, "hy": 34, "ru": 32, "overflow": "wrap" },
  "meta.title":          { "ref": 60, "hy": 60, "ru": 60, "overflow": "none — SEO hard limit" },
  "meta.description":    { "ref": 155, "hy": 155, "ru": 155, "overflow": "none — SEO hard limit" }
}
```

How the limits are enforced:
1. `npm run lint:strings` fails the build on any overflow in any locale.
2. Storybook has a **Pseudo-locale** toggle that renders English at +30% length
   with accents (`Rëqüést à fréé çönsültàtïön…`). Every component must survive it
   before it is accepted. This catches layout breakage before translation exists.
3. Where "overflow: none" is declared, the component has no ellipsis and no
   clamp — it will break the layout visibly, on purpose, so the copywriter fixes
   the string rather than the developer hiding it.

Additional content rules the system encodes rather than requests:

- **String files are the only source of copy.** No literal user-facing text in
  any component. `lint:no-hardcoded-strings` fails the build.
- **A denylist ships with the linter** and fails the build on:
  `bestseller`, `monthly`, `preventive visit`, `light visit`, `QR`,
  `memory page`, `testimonial`, `trusted by`, `families served`, `since 20`,
  `Memory Care` (spaced), `MEMORYCARE`, `Oops`, and every emoji codepoint.
- **Numbers are never in the copy.** Prices come from a typed `products.json`;
  the string file holds `{price}` placeholders. A price cannot drift between the
  pricing page, the calculator and the portal.
- **The tagline is a fixed asset string** with no full stop, stored once:
  `brand.tagline = "HONORING MEMORY, CARING FOR LOVED ONES"`. The linter fails
  on a trailing period.
- **Headings use `text-wrap: balance`; body uses `text-wrap: pretty`.**
  Armenian and Russian get `hyphens: auto` with `lang` set correctly on `<html>`;
  English does not (hyphenation reads cheap in an editorial layout).
- `font-variant-numeric: tabular-nums` on every price, date, coordinate and
  counter, so numbers do not jitter when the calculator updates.

---

# D. The handoff package

## D1. What Igor receives

One repository (or one zip, versioned) — `memorycare-design-handoff-v1.0/`.
Nothing is delivered by chat, screenshot or email attachment. If it is not in
this tree, it is not a requirement.

```
memorycare-design-handoff-v1.0/
├── README.md                        Start here. 1 page. Order of operations.
├── CHANGELOG.md                     Every version, what changed, what he must re-check
├── ACCEPTANCE-CHECKLIST.md          §D5. What he signs off against
├── DEVELOPER-DECISIONS.md           §D6. The eleven things that are his call
├── OPEN-ITEMS.md                    Everything we owe him, with an owner and a date
│
├── tokens/
│   ├── tokens.json                  SOURCE OF TRUTH (W3C DTCG)
│   ├── sd.config.js                 Style Dictionary build config
│   ├── build/
│   │   ├── mc-tokens.css            generated — the file the app imports
│   │   ├── mc-tokens.scss           generated
│   │   ├── tailwind.tokens.js       generated — for the Tailwind theme, if he picks Tailwind
│   │   └── tokens.d.ts              generated — typed unions (tariff period, visit type, badge variant)
│   ├── CONTRAST-MATRIX.md           §A3.5, the permission table
│   └── stylelint-mc-contrast/       the lint plugin, installable
│
├── components/
│   ├── 00-INDEX.md                  every component, its status, its Figma node id
│   ├── SPEC-button.md
│   ├── SPEC-input.md
│   ├── SPEC-select.md
│   ├── SPEC-checkbox.md
│   ├── SPEC-radio.md
│   ├── SPEC-card.md
│   ├── SPEC-tariff-card.md
│   ├── SPEC-calculator.md
│   ├── SPEC-report-card.md
│   ├── SPEC-gallery.md
│   ├── SPEC-badge.md
│   ├── SPEC-navigation.md
│   ├── SPEC-footer.md
│   ├── SPEC-modal.md
│   ├── SPEC-toast.md
│   ├── SPEC-status-postponed.md
│   ├── SPEC-status-no-access.md
│   └── SPEC-guarantee-revisit.md
│   (each: anatomy diagram · measurement table · state matrix · props/variant
│    list · ARIA and keyboard contract · responsive behaviour · content limits ·
│    "do not" list · Figma node link)
│
├── layout/
│   ├── GRID.md                      breakpoints, columns, gutters, container
│   ├── PAGE-TEMPLATES.md            section order per route, with component names
│   └── ROUTES.md                    every URL, its locale variants, its meta rules
│
├── content/
│   ├── content-limits.json
│   ├── strings.en.json              complete, final English
│   ├── strings.hy.json              keys present, values marked TODO-TRANSLATION
│   ├── strings.ru.json              same
│   ├── products.json                the five products, prices, surcharge rates, credit rules
│   └── COPY-RULES.md                the denylist and why each entry is on it
│
├── brand/
│   ├── LOGO-USAGE.md                §E. clear space, minimum sizes, forbidden uses
│   ├── logo/production/             §E2. the eleven prepared SVGs
│   ├── logo/source/                 the nine original 1080² SVGs, untouched, for reference
│   ├── favicon/                     §E3
│   ├── og/                          og-default.png, og-report-share.png (1200×630)
│   ├── fonts/                       self-hosted woff2, subset per script
│   └── FONTS.md                     licences, subsets, unicode-range, the Gill Sans note
│
├── placeholders/
│   ├── README.md                    what each placeholder becomes after the Sept shoot
│   ├── photo-3x2-plot-after.svg
│   ├── photo-3x2-plot-before.svg
│   ├── photo-3x2-crew.svg
│   ├── video-16x9-report.svg
│   └── portrait-1x1-team.svg
│
├── qa/
│   ├── contrast.spec.ts             axe-core, every route, 3 locales, 2 widths
│   ├── strings.spec.ts              denylist, length limits, tagline full stop
│   ├── meta.spec.ts                 OG image is never a photograph
│   └── VISUAL-BASELINES/            reference screenshots at 360 / 768 / 1280
│
└── figma/
    └── FIGMA-MAP.md                 §D3. node-id → component-spec → code-file table
```

## D2. What lives in Figma versus what lives in files

The single rule that prevents six months of drift:

> **Figma is the source of truth for composition. Files are the source of truth
> for values. Neither is authoritative on the other's territory.**

| Question | Answer lives in |
|---|---|
| What colour is this? | `tokens/tokens.json` |
| How much space is between these? | `tokens.json` + the component spec |
| What does this screen look like assembled? | Figma |
| What order are the sections in? | `layout/PAGE-TEMPLATES.md` (Figma illustrates it) |
| What are the states? | `components/SPEC-*.md` (Figma shows a variant board) |
| What is the copy? | `content/strings.*.json` |
| What happens on hover? | The spec |
| What does the empty state say? | `strings.en.json` |
| What is the exact hex of this pixel? | Never eyedrop Figma. `tokens.json`. |

**Igor never inspects a Figma layer for a number.** If Figma disagrees with
`tokens.json`, `tokens.json` wins and Figma is a bug we fix. This is stated in
`README.md` in bold, because the last round of this project shipped colours that
had been sampled off a JPEG.

## D3. Figma file structure

**Two files, not one, and not twelve.** A two-person company cannot maintain a
multi-file library graph.

**File 1 — `MemoryCare · Foundations & Components`** (published as a library)

| Page | Contents | Naming |
|---|---|---|
| `00 · Read me` | How to use this file, who to ask, the "tokens.json wins" rule, current version | — |
| `01 · Foundations` | Colour swatches with the contrast matrix drawn as a grid, type scale specimen in all three scripts, spacing ruler, radius set, elevation set, motion demo frames | `Foundation/Colour/…` |
| `02 · Components` | One section per component, in the same order as `components/00-INDEX.md` | `Button/Primary`, `Input/Text`, `Card/Tariff` |
| `03 · Patterns` | Composed blocks used more than once: pricing row, report header, form block, footer, sticky CTA | `Pattern/PricingRow` |
| `04 · Brand assets` | The eleven production logo lock-ups, favicon set, placeholder frames | `Brand/Logo/Horizontal-Compact` |
| `99 · Archive` | Anything superseded, dated, never deleted | `[2026-08-27] Old palette` |

**File 2 — `MemoryCare · Product`** (consumes File 1)

| Page | Contents |
|---|---|
| `00 · Read me` | Route map, status legend |
| `01 · Site — Home` | 360 / 768 / 1280 frames |
| `02 · Site — Pricing` | + calculator states |
| `03 · Site — How it works / Sample report / Family Circle` | |
| `04 · Site — About / Contacts / Legal` | |
| `05 · Portal — Onboarding & empty` | |
| `06 · Portal — Visits & Report` | |
| `07 · Portal — Family Circle & permissions` | |
| `08 · Portal — Payment & Profile` | |
| `09 · Bad news & edge states` | postponed, no access, guarantee revisit, payment failed, cancellation |
| `10 · Flows` | FigJam-style arrows between frames, no new pixels |
| `99 · Archive` | |

**Naming, everywhere:** `Category/Subcategory/Name` with `Property=Value` for
variants — `Button/Primary` with `Size=md, State=hover, Icon=leading`. Frames in
File 2: `<route> · <breakpoint> · <state>` → `Pricing · 360 · calculator-over-ceiling`.

**Variables → tokens mapping.** Four Figma variable collections, matching the
three layers plus layout, so the mapping is mechanical and can be round-tripped
with Tokens Studio:

| Figma collection | Modes | Maps to |
|---|---|---|
| `1 Primitive` | (none) | `primitive.*` |
| `2 Semantic` | `Light`, `On dark` | `semantic.*` — the two modes are exactly `:root` and `.mc-on-dark` |
| `3 Component` | (none) | `component.*` |
| `4 Layout` | `360`, `768`, `1280` | responsive overrides in `mc-tokens.css` |

Figma variable names are the token path with `/` instead of `.` and no `mc`
prefix: `semantic.text.accent` → `Semantic/Text/Accent`. A ten-line script in
`figma/sync/` converts in both directions; nobody retypes a value.

**Maintenance rules for two people:**
- Only the design lead publishes the library. One publisher, always.
- Every publish has a description in the format `v1.2 — added Toast/Warning;
  changed nothing existing` and is mirrored into `CHANGELOG.md` the same day.
- Component variants are capped: if a component needs more than 24 variant
  combinations, it is two components.
- No detached instances in File 2. A detached instance is a review failure.
- Branching is not used. Two people editing one file is cheaper than merges.

## D4. How Igor moves from a Figma frame to production code

Written as the actual sequence, in `README.md`:

1. **Open the route in File 2 → Product.** Read the frame name to get route,
   breakpoint and state.
2. **Read `layout/PAGE-TEMPLATES.md` for that route.** It lists the sections
   top to bottom by component name and container width. Build the page skeleton
   from this, not by measuring the Figma frame.
3. **For each section, open `components/SPEC-<name>.md`.** Build the component
   from the spec's measurement table and state matrix. Use Figma only to confirm
   he has the right component and the right composition.
4. **Never type a value.** Every number and colour comes from
   `tokens/build/mc-tokens.css`. If a value is missing, stop and file it in
   `OPEN-ITEMS.md` — do not approximate.
5. **Copy comes from `content/strings.en.json` by key.** The key is printed in
   the Figma layer name of every text node, in the form `{{hero.h1}}`, so the
   frame and the string file are visibly linked.
6. **Run `npm run lint:tokens && npm run lint:strings && npm run test:a11y`
   before pushing.** All three are in the package and all three are merge gates.
7. **Compare against `qa/VISUAL-BASELINES/`** at 360, 768 and 1280.
8. **Tick the row in `ACCEPTANCE-CHECKLIST.md`.**

Figma Dev Mode is enabled and every component in File 1 carries a `Code Connect`
link to its spec file. Dev Mode's generated CSS is **explicitly not to be
copied** — it emits raw hexes. A note to that effect sits on page `00 · Read me`.

## D5. Acceptance checklist — what Igor signs off against

`ACCEPTANCE-CHECKLIST.md`, per route, boolean, no partial credit. Abridged:

**Tokens and styling**
- [ ] `mc-tokens.css` is imported once, globally, and is unmodified from the package.
- [ ] `grep -rE "#[0-9a-fA-F]{3,6}"` over `src/` returns zero results outside `mc-tokens.css`.
- [ ] `grep -rE ":\s*[0-9]+px"` returns only values that are `var()`-derived or documented exceptions.
- [ ] `npm run lint:tokens` passes.
- [ ] No token names from the forbidden list (`--gold`, `--navy`, `--mut`, …) exist.

**Accessibility**
- [ ] axe-core: zero serious/critical on every route, 3 locales, at 360 and 1280.
- [ ] Every interactive element reachable and operable by keyboard alone.
- [ ] Visible focus ring on every control, including sliders, language switcher, gallery thumbs.
- [ ] All hit areas ≥ 44×44.
- [ ] 200% zoom at 360px width: no horizontal scroll on any route.
- [ ] `prefers-reduced-motion`: no translate, no shimmer, no count-up, no auto-advance.
- [ ] Every image has meaningful `alt`; decorative images have `alt=""`.
- [ ] Forms: label, error linked by `aria-describedby`, `aria-invalid`, error summary on submit.

**Content and brand**
- [ ] `npm run lint:strings` passes: denylist clean, length limits met in all 3 locales.
- [ ] Tagline appears with no full stop, everywhere.
- [ ] "MemoryCare" spelling is correct in every instance; no "Memory Care", no "MEMORYCARE", no "MC".
- [ ] No invented statistics, testimonials, review counts or years in business.
- [ ] No QR code and no memory page mentioned anywhere, including alt text and meta.
- [ ] Real contacts present: both names, both phones, `info@memorycare.am`.
- [ ] Legal address renders as a marked placeholder, not as invented text.
- [ ] Prices come from `products.json`; no price is typed in a component or a string.
- [ ] Every price shows both `֏` and `AMD`.
- [ ] Olive never carries text; no Olive-fill button or badge with a light label exists.

**Behaviour**
- [ ] Every component has default / loading / empty / error / success rendered in Storybook.
- [ ] The three bad-news screens exist and are reachable in Storybook.
- [ ] Calculator arithmetic matches the formulas in `SPEC-calculator.md` — unit tested, including the over-ceiling branch.
- [ ] Credit logic matches `products.json`: 60-day window, larger of the two, fires only at annual signing, no Inspection→Express credit.
- [ ] Guest report view: bundle contains no `TariffCard`, no `Calculator`, no `primary` CTA. Verified by a bundle assertion, not by looking.
- [ ] Shared report OG image is the static asset; `meta.spec.ts` passes.
- [ ] Phone field accepts `+1`, `+33`, `+7`, `+374` and local formats; stores E.164.
- [ ] Cancellation with pro-rata refund is completable without contacting us.
- [ ] Visit reminder is opt-in and can be addressed to a different person.
- [ ] Family Circle permission matrix implemented as specified — roles are not identical.

**Performance and delivery**
- [ ] LCP ≤ 2.5s on a throttled 4G profile at 360px, on the Home route.
- [ ] CLS ≤ 0.05. Every image has intrinsic dimensions.
- [ ] Fonts self-hosted, ≤ 180 KB per locale, `font-display: swap`, correct `unicode-range`.
- [ ] No request to `fonts.googleapis.com` or any third-party CDN for a brand asset.
- [ ] Logo in the header is the prepared horizontal lock-up, not a cropped 1080² file.
- [ ] Favicon set complete; `mark-simplified` used at 16 and 32.

**Bank (Ameriabank) — every one is a hard gate**
- [ ] About page exists with company description.
- [ ] Contacts in the footer of **every** page.
- [ ] Full service descriptions for all five products.
- [ ] Legal restrictions / service limitations page.
- [ ] Real prices in AMD, symbol and letters.
- [ ] Privacy policy in English.
- [ ] Refund policy.
- [ ] Terms of service / service delivery terms.

## D6. Deliberately Igor's decision, not ours

`DEVELOPER-DECISIONS.md`. We will not answer questions about these, and we will
not review them:

1. **Framework and rendering strategy** — Next.js, Astro, SvelteKit, plain
   Vite; SSG vs SSR. We only require: server-rendered HTML for the marketing
   routes (SEO and the bank's review), and per-locale URLs.
2. **CSS methodology** — CSS Modules, vanilla-extract, Tailwind, plain CSS. Our
   only requirement is that `mc-tokens.css` is the sole source of values. If he
   picks Tailwind, `tailwind.tokens.js` is in the package.
3. **Component library, if any** — Radix, Ark, Headless UI, or hand-rolled. Our
   specs are behaviour contracts, not implementations. Radix or Ark will satisfy
   the ARIA requirements faster; that is a recommendation, not a requirement.
4. **State management, data fetching, caching.**
5. **i18n library** — next-intl, i18next, Paraglide. Requirement: ICU
   pluralisation (Russian has three plural forms and Armenian has two — this
   will matter for "N visits"), and `lang` correctly set on `<html>`.
6. **Form and validation library** — react-hook-form + zod, Felte, whatever.
   Requirement: the validation *timing* rules in `SPEC-input.md`.
7. **Phone input implementation** — libphonenumber-js or equivalent.
   Requirement: the behaviour in `SPEC-input.md`, not a particular package.
8. **Image pipeline** — format negotiation, AVIF/WebP, CDN, srcset generation.
   Requirement: the aspect ratios and intrinsic dimensions in `SPEC-gallery.md`.
9. **Hosting, CI, error monitoring, analytics implementation.** (Which events we
   track is ours; how they are sent is his.)
10. **Backend, database, API shape, PDF generation, file storage.**
11. **Animation implementation** — CSS transitions, Motion One, Framer Motion.
    Requirement: the durations, easings and distances are the token values, and
    `prefers-reduced-motion` is honoured.

Corollary, stated as plainly: **choosing a colour, a spacing value, a radius, a
font size, a duration, a copy string, or the order of blocks in the report card
is never his decision.** If he needs one of those and cannot find it, that is our
failure and it goes in `OPEN-ITEMS.md`.

## D7. Open items we still owe (in `OPEN-ITEMS.md`, with owners)

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Deep Olive `#575E3B` confirmed or replaced by the designer | Designer | Nothing — one line at Layer 1 |
| 2 | Horizontal lock-up from the designer (we ship a constructed one meanwhile — §E) | Designer | Header polish, not build |
| 3 | Colour mark that survives a Nude ground (hands currently Ivory, 1.1 contrast) | Designer | Any colour mark on Nude |
| 4 | Content-cropped SVG exports from the designer (we ship our own — §E) | Designer | Nothing |
| 5 | Gill Sans web licence decision, or ratify Cabin | Owner | Type tokens are already substituted; only labelling changes |
| 6 | Armenian and Cyrillic display face ratified (Noto Serif Armenian / Playfair Display proposed) | Designer + owner | hy/ru heading rendering |
| 7 | Legal address | Owner | Footer, About, bank submission |
| 8 | Real photography from the September shoot | Owner | All placeholders |
| 9 | Company registration / VAT number for the footer | Owner | Bank submission |
| 10 | Final legal copy for the four legal pages | Owner + counsel | Bank submission |
| 11 | Family Circle permission matrix values ratified by the owner | Owner | Portal build |
| 12 | 16px simplified mark approved | Designer | Favicon |

---

# E. The logo assets — production preparation

## E1. What we actually have (measured, not estimated)

All nine SVGs are `viewBox="0 0 1080 1080"`. Measured content bounding boxes,
computed from the path data:

| File group | Content bbox (x, y, w, h) | Padding | Aspect |
|---|---|---|---|
| `logo mark_*` | `112.7, 170.2, 854.7, 739.7` | left 112.7 · right 112.6 · **top 170.2 · bottom 170.2** | 1.156 : 1 |
| `primary logo_*` (vertical lock-up) | `112.9, 55.2, 854.7, 965.4` | left 112.9 · right 112.4 · top 55.2 · bottom 59.4 | 0.885 : 1 |
| `wordmark_*` (word + tagline) | `130.5, 446.0, 819.0, 188.1` | top 446 · bottom 446 | 4.354 : 1 |
| — word line only | `168.0, 446.0, 744.0, 118.6` | — | 6.273 : 1 |
| — tagline only | `130.5, 604.1, 819.0, 30.0` | — | 27.3 : 1 |
| Inside the vertical lock-up: mark | `112.9, 55.2, 854.7, 739.6` | — | identical mark |
| Inside the vertical lock-up: word block | `130.8, 832.5, 819.0, 188.1` | gap below mark **37.6** | identical wordmark |

Two facts that matter: the wordmark file is **97% empty space** — 819×188 of
content in 1,166,400 px² of canvas — and the vertical lock-up reuses the mark
and the wordmark at 1:1 scale with a 37.6-unit gap. That second fact is what
makes a horizontal lock-up constructible today.

## E2. Preparation — the eleven production SVGs

Method (scripted, in `brand/logo/prepare.mjs`, so it is reproducible when the
designer sends corrected files):

1. Replace `viewBox="0 0 1080 1080"` with the measured content bbox.
2. Remove `width`/`height` attributes entirely and add
   `preserveAspectRatio="xMidYMid meet"` — the SVG then scales from CSS and
   never imposes a square.
3. Replace the `<style>` block and `class="cls-N"` with `fill` attributes, and
   in the mono versions replace the literal fill with `fill="currentColor"` so
   one file serves every context.
4. Add `role="img"` and `<title>MemoryCare</title>`; add `aria-hidden="true"`
   where the logo sits next to the visible wordmark text.
5. Run SVGO: `--precision=2 --multipass`, keeping `viewBox`, removing metadata,
   ids and the `<defs>`/`<style>` machinery.
6. Assert the result is < 12 KB and renders identically to the source at 512px
   (pixel-diff gate in `brand/logo/verify.mjs`).

Delivered set, `brand/logo/production/`:

| # | File | viewBox | Use |
|---|---|---|---|
| 1 | `mark-color.svg` | `112.7 170.2 854.7 739.7` | Anthracite or pure-white grounds **only** — the Ivory hands vanish on Nude (contrast 1.1) |
| 2 | `mark-mono.svg` | same | `currentColor`. The default everywhere. |
| 3 | `wordmark-color.svg` | `130.5 446 819 188.1` | word + tagline, two-colour |
| 4 | `wordmark-mono.svg` | same | `currentColor` |
| 5 | `wordmark-word-only-mono.svg` | `168 446 744 118.6` | no tagline; header, small sizes |
| 6 | `lockup-vertical-color.svg` | `112.9 55.2 854.7 965.4` | print, social avatar backgrounds, hero |
| 7 | `lockup-vertical-mono.svg` | same | |
| 8 | **`lockup-horizontal-color.svg`** | `0 0 1111 261` | constructed — §E4 |
| 9 | **`lockup-horizontal-mono.svg`** | same | **the site header** |
| 10 | **`lockup-horizontal-tagline-mono.svg`** | `0 0 1216 292` | footer, letterhead, vehicle |
| 11 | **`mark-simplified-mono.svg`** | `0 0 32 32` | ≤ 20px: favicon, app icon, WhatsApp avatar |

The nine originals are kept untouched in `brand/logo/source/`, and
`prepare.mjs` regenerates production from them. Nobody ever edits a production
SVG by hand.

## E3. The horizontal lock-up — construction, exact

The designer has not supplied one and the header needs one now. We construct it
from her own artwork at her own proportions; when hers arrives, we swap the file
and nothing else changes.

**Compact (header) — `lockup-horizontal-mono.svg`.** Mark at the inline-start,
word line only, no tagline (a 30-unit-tall tagline is illegible at header size).

- Word line, unscaled: `744 × 118.6`.
- Mark height set to **2.2× the word-line height** = `260.9`; mark width
  = `260.9 × 1.1556` = `301.5`. This is the ratio that makes the mark read as an
  icon beside the word rather than as a second focal point — the vertical
  lock-up's own ratio (6.24×) is unusable horizontally.
- Gap = **0.55× word-line height** = `65.2`. (The vertical lock-up's gap is
  37.6 against a 739-tall mark = 0.32 of the wordmark block height; 0.55 of the
  word-line height keeps the same optical looseness turned 90°.)
- Canvas: `301.5 + 65.2 + 744 = 1110.7 ≈ 1111` wide × `260.9 ≈ 261` tall.
  **Aspect 4.26 : 1.**
- The word is centred on the mark's vertical centre:
  `y = (260.9 − 118.6) / 2 = 71.15`.

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1111 261"
     preserveAspectRatio="xMidYMid meet" role="img" fill="currentColor">
  <title>MemoryCare</title>
  <!-- mark: source bbox 112.7,170.2,854.7,739.7 → scale 260.9/739.7 = 0.35271 -->
  <g transform="translate(0,0) scale(0.35271) translate(-112.7,-170.2)">
    <!-- paths from MemoryCare_logo mark_dark.svg -->
  </g>
  <!-- word line: source bbox 168,446,744,118.6 → scale 1, placed after mark + gap -->
  <g transform="translate(366.7,71.15) translate(-168,-446)">
    <!-- word-line paths from MemoryCare_wordmark_dark.svg (exclude tagline paths, y > 580) -->
  </g>
</svg>
```

**With tagline — `lockup-horizontal-tagline-mono.svg`.** Same construction using
the full wordmark block (`819 × 188.1`): mark height = `1.55 × 188.1 = 291.6`,
mark width `336.9`, gap `60`, canvas `1216 × 292`, **aspect 4.16 : 1**, wordmark
block vertically centred at `y = (291.6 − 188.1)/2 = 51.75`.

**Colour variants** are the same geometry with the designer's fills: hands
Nude/Ivory, petals Olive, "Memory" Ivory, "Care" Olive, tagline Olive.

## E4. How the site header uses it

| Breakpoint | Asset | Rendered height | Rendered width |
|---|---|---|---|
| ≥ 768px | `lockup-horizontal-mono.svg` | 36px | ~153px |
| 480–767px | `lockup-horizontal-mono.svg` | 32px | ~136px |
| < 480px | `mark-mono.svg` + live `<span>MemoryCare</span>` in Gloock 20px | 28px mark | auto |

Below 480px the drawn word is dropped and replaced with **live text**, because
the drawn word at 22px is softer than type at the same size and because the live
text is selectable and translatable. The `<span>` carries `font-family:
var(--mc-font-display)` and the two-colour treatment via a nested `<b>` —
`Memory` in `--mc-text-primary`, `Care` in `--mc-text-accent`. Note this is
**Deep Olive, not Olive**: at 20px, Olive at 3.42 is unreadable. On the
Anthracite footer band both halves are Nude.

Header colour resolution: the header sits on `surface-page`, so
`mark-mono.svg` inherits `color: var(--mc-text-primary)` = Anthracite. In the
footer it inherits Nude. One file, two contexts, zero variants to maintain.

## E5. Clear space, minimum sizes, forbidden uses (`LOGO-USAGE.md`)

**Clear space** = the height of the "M" in the wordmark, on all four sides.
Expressed relative to the asset so it survives scaling: for the horizontal
lock-up, clear space = `0.42 × total height`. Encoded as a CSS token,
`--mc-logo-clearspace: 0.42em` applied via padding on the logo wrapper, so no
one has to measure.

**Minimum sizes** (verified by rendering, not assumed):

| Asset | Minimum |
|---|---|
| Vertical lock-up | 64px wide |
| Horizontal compact | 120px wide (mark lands at 28px) |
| Horizontal with tagline | 240px wide (below this the tagline breaks up) |
| Mark, full detail | **24px** — at 16px the woven medallion collapses to a blur |
| `mark-simplified-mono` | 16px — five petals and a solid centre, no hands, no weave |

**Forbidden** — this list exists because each one has already happened somewhere
in this project's history: colour mark on a Nude ground; any recolouring outside
the five brand values; rotation; outline or drop shadow; the mark inside a
circle or a badge; the mark alone used as the hero image (that is the current
site's mistake); stretching to a non-native aspect; the tagline set with a full
stop; the tagline at under 11px; "Memory Care", "MEMORYCARE" or "MC"; the
1080² source files used directly in any layout.

## E6. Favicon and icon set (`brand/favicon/`)

| File | Size | Source |
|---|---|---|
| `favicon.svg` | any | `mark-simplified-mono.svg`, `fill="#33373C"`, with a `prefers-color-scheme: dark` media rule inside the SVG switching to `#EFE5D5` |
| `favicon-32.png` | 32 | `mark-mono` on `#F3F0E9` |
| `favicon-16.png` | 16 | **`mark-simplified`** on `#F3F0E9` |
| `apple-touch-icon.png` | 180 | `mark-color` on `#33373C`, 16% padding, no rounding (iOS masks) |
| `icon-192.png` / `icon-512.png` | PWA | `mark-color` on `#33373C`, 16% padding |
| `maskable-512.png` | 512 | `mark-mono` Nude on `#33373C`, content inside the central 80% safe zone |
| `og-default.png` | 1200×630 | Anthracite ground, horizontal lock-up centred, tagline below |
| `og-report-share.png` | 1200×630 | Anthracite ground, mark + the words "Visit report". **Never a photograph.** |

The 16px simplified mark is a small piece of new drawing we owe: five petals at
the same angles as the master, a solid Olive centre disc, no hands, no weave.
It is item 12 in `OPEN-ITEMS.md` and is the only logo artwork we create rather
than derive.

---

## F. Versioning and what happens after handoff

- The package is semver'd. `1.x` = additive, Igor pulls and continues.
  `2.0` = a value changed and he must re-check the routes named in
  `CHANGELOG.md`.
- Token changes are never delivered in conversation. They are a package version.
- A weekly 30-minute call while the build runs, with `OPEN-ITEMS.md` as the only
  agenda. Anything raised outside that call gets written into the file rather
  than answered ad hoc, so the file stays the record.
- When the September photography lands, it is a `1.x` release replacing the
  files in `placeholders/` with real assets at identical names and aspect
  ratios. No component changes.
