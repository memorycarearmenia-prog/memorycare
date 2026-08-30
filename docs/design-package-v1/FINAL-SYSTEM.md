# MemoryCare — Final Design System and Handoff Specification

**Version:** 1.0 · FINAL · 30.08.2026
**Author:** Design System and Handoff Engineer
**Language of every deliverable:** English
**Scope:** marketing site + client portal
**Supersedes:** `01-ux-architect.md`, `02-visual-lead.md`, `03-content.md`,
`04-conversion.md`, `05-design-system.md` and all five round-two memos.
Where any of those disagrees with this file, **this file wins**. Where
`DECISIONS.md` or `DECISIONS-2.md` disagrees with this file, **they win** and
this file is a bug.

---

## 0. How to read this document

### 0.1 Order of precedence — memorise this, it settles every argument

```
1  DECISIONS.md + DECISIONS-2.md        owner rulings, absolute
2  BRIEF.md                             the approved brief
3  measured fact                         contrast, glyph coverage, fold arithmetic
4  FINAL-SYSTEM.md (this file)          convergence of the five disciplines
5  the five round-one proposals          detail only, never authority
```

### 0.2 The one-paragraph contract

Everything visual in MemoryCare is a token. Igor never picks a colour, a radius,
a duration, a gap or a string. He picks a component, gives it a variant and a
state, and the system resolves the value. If he needs a number that is not in
`tokens/build/mc-tokens.css`, **that is a defect in this document, not a
decision for him** — he writes it into `OPEN-ITEMS.md` and we answer within one
business day. Exactly eleven things are deliberately his call; they are in §13
and nowhere else.

### 0.3 Two rules that hold the package together

> **Figma is the source of truth for composition. Files are the source of truth
> for values.** Neither is authoritative on the other's territory.

> **A value that is not in `tokens.json` does not exist** — including a value
> the design lead is certain about. Never eyedrop Figma. The last round of this
> project shipped a palette sampled off a JPEG.

### 0.4 Vocabulary — one name per thing, in code, in Figma, in conversation

| Canonical | Retired names |
|---|---|
| `ReportSheet` | report card, report artefact, proof card, report screen |
| `ReportPreview` | the cropped hero object, "proof card" |
| `VisitListRow` | report card used as a list row |
| `VerificationRail` | verification rail (02), ReportRail, "status row + plot line" |
| `GpsVerification` | GPS chip, GPS proof, GPS verification element, map pin |
| `PlotDiagram` | bearing rose, plot graphic |
| `TariffCard` (`variant: one-off \| annual`) | pricing card, product card, tier card |
| `PricingBand` (`--one-off` / `--annual`) | OneOffBand, the row, Band 1/2 |
| `PlotCalculator` | calculator, calculator block |
| `MobileActionBar` | sticky action bar, StickyCtaBar, sticky mobile CTA bar |
| `ReportShareBar` | the report's own sticky bar |
| `PermissionMatrix` | roles table, permission table |
| `ProgressRail` | "what happens next" |
| `FirstEntryScreen` | doubt screen, first entry |
| `StatusScreen--rescheduled / --no-access / --revisit` | bad-news states |
| `GuaranteesBlock` | guarantees |
| `HonestyPanel` | honesty block, founding note |
| `PricingFork` | the fork |
| `TrustLadder` | trust ladder |
| `LanguageSwitcher` (a `SegmentedControl` instance) | — |
| `type.rail` | rail (02), meta type |
| `type.overline` | eyebrow |
| **Error** — `--mc-color-feedback-error` | danger, terracotta, functional red |
| Roles: **Owner · Family manager · Family member · Guest** | Manager, Member, relative, viewer, payer, subscriber |
| **Local contact** | beneficiary, nominated relative |
| **The crew** | our team, technicians, operatives |
| **The plot** | the site, the object, the grave site |
| **MemoryCare LLC** | Memory Care LLC, MEMORYCARE, MC, Memory-Care |
| **֏ AMD** — always both | ֏ alone, AMD alone, 160k, AMD 160,000 |

Statuses — data value → UI string:
`completed` → Completed · `scheduled` → Scheduled · `preparing` → Being prepared
· `rescheduled` → **Moved** · `no-access` → **Could not reach the plot** ·
`revisit-requested` → Repeat visit requested.
The words `postponed`, `access blocked`, `bestseller`, `most popular`,
`monthly`, `light visit`, `preventive visit` do not exist in any file in any
language.

---

## 1. Token architecture

### 1.1 Three layers, no skipping

```
Layer 1  PRIMITIVE   mc.color.olive.500          a raw value with no meaning
   │                 mc.size.4                   never referenced by a component
   ▼
Layer 2  SEMANTIC    mc.surface.raised           the decision; scope-switchable
   │                 mc.text.accent
   ▼
Layer 3  COMPONENT   mc.button.primary.bg.hover  the contract with the markup
```

Rules, enforced by `npm run lint:tokens` and in review:

1. A component stylesheet may reference **Layer 3 only**.
2. A Layer 3 token may reference **Layer 2 only**.
3. A Layer 2 token may reference **Layer 1 only**.
4. Layer 1 is the only place a literal hex, px, ms or cubic-bezier appears.
5. Skipping a layer is allowed nowhere. If a component needs a primitive, the
   semantic token is missing — add it.
6. **No component may reference `--mc-color-olive-700` (Deep Olive) directly.**
   All accent colour goes through `--mc-text-accent` / `--mc-border-accent` /
   `--mc-surface-accent-strong`, which the `.mc-on-dark` scope rewrites. The
   linter rejects `var(--mc-color-olive-700)` outside `mc-tokens.css`.

Why three layers here specifically: the palette has one unratified value (Deep
Olive), one unratified type pair (Gill Sans licence, Armenian coverage) and
three locales. Each is a one-line change at Layer 1 or 2 and zero changes at the
component level.

### 1.2 Naming grammar

```
mc . <layer> . <category> . <role> [. <variant>] [. <state>] [. <scale-step>]
```

| Rule | Example |
|---|---|
| Everything is prefixed `mc` (the portal embeds third-party payment widgets) | `--mc-color-olive-500` |
| Lower-kebab in CSS · lower-dot in JSON · `Title/Slash` in Figma | `--mc-surface-raised` ⇄ `mc.surface.raised` ⇄ `Semantic/Surface/Raised` |
| Names describe **role**, never appearance | `--mc-text-accent`, never `--mc-text-olive` |
| Names never encode a measurement | `--mc-nav-item-padding-inline`, never `--mc-nav-width-240` |
| Names never encode English copy | `--mc-button-secondary-*`, never `--mc-btn-learn-more` |
| Logical properties only | `padding-inline`, `border-block-end`, `inset-inline-start` |
| Scale steps numeric and open-ended | `100…900` colour, `0…50` size |
| States are a closed set | `default hover active focus disabled loading selected error` |
| No abbreviations except `bg`, `fg`, `min`, `max` | — |

**Forbidden token names** (all have appeared in this project's history; any of
them in a pull request is an automatic reject): `--gold`, `--gold2`, `--navy`,
`--lilac`, `--blue`, `--mut`, `--dim`, and **any token name containing
`danger`, `success` or `warning`**. The last three are banned by
`DECISIONS.md §2` — the owner forbade the *family*, not only the hues, and
`lint:tokens` fails the build on those three substrings anywhere in a token
name.

### 1.3 What each layer is allowed to contain

| Layer | Contains | Does not contain |
|---|---|---|
| 1 Primitive | the 5 brand hexes, the 1 error hex, alphas of those, sizes, radii, borders, durations, easings, z, font stacks, weights | anything with a job |
| 2 Semantic | surface, text, border, elevation, layout, motion, type roles | any literal value |
| 3 Component | one group per component, `<component>.<variant>.<prop>.<state>` | any literal value; any reference to Layer 1 except the three documented hover/active steps of Deep Olive |

---

## 2. `tokens/tokens.json` — complete, copy this into the file

W3C Design Tokens Community Group format, because Style Dictionary, Tokens
Studio and Figma Variables all read it. Aliases use `{dot.path}`.

```json
{
  "$schema": "https://tr.designtokens.org/format/",
  "$description": "MemoryCare design tokens v1.0 FINAL — 2026-08-30. SOURCE OF TRUTH for every value in the product. Generated CSS is committed but never hand-edited. NOTE: Cabin is used as a free substitute for Gill Sans (commercial Monotype, unlicensed for web). It is not the brand text face.",

  "primitive": {
    "$description": "Layer 1. Raw values. Never referenced by a component.",

    "color": {
      "olive": {
        "500": { "$type": "color", "$value": "#7C8654", "$description": "Brandbook Olive. Decorative fills, petals, tagline in print, dividers. NEVER carries text and NEVER carries a label on top of it (3.08-3.42)." },
        "700": { "$type": "color", "$value": "#575E3B", "$description": "Deep Olive. WORKING VALUE adopted by the owner 29.08.2026, pending the designer's own value. Interface only. Not in the logo, not in the brandbook." },
        "800": { "$type": "color", "$value": "#4E5535", "$description": "Deep Olive x0.90 toward black. Hover only." },
        "900": { "$type": "color", "$value": "#474D30", "$description": "Deep Olive x0.82 toward black. Active only." }
      },
      "nude": {
        "400": { "$type": "color", "$value": "#F2EADD", "$description": "Nude 80% + white 20%. Hover step for Nude fills on the dark scope." },
        "500": { "$type": "color", "$value": "#EFE5D5", "$description": "Brandbook Nude. THE PAGE GROUND. Never a card background." },
        "600": { "$type": "color", "$value": "#E4D8C4", "$description": "Nude 92% + Anthracite 8%. Sunken panels, neutral status grounds. Anthracite on it = 8.51." }
      },
      "ivory": {
        "400": { "$type": "color", "$value": "#F8F6F1", "$description": "Ivory 70% + white 30%. Raised-hover." },
        "500": { "$type": "color", "$value": "#F3F0E9", "$description": "Brandbook Ivory white. RAISED OBJECTS on the light ground, the header bar, and light text on Anthracite. Never a full-bleed page band." }
      },
      "anthracite": {
        "400": { "$type": "color", "$value": "#4A4D51", "$description": "Anthracite 88% + Ivory 12%. Raised object inside the dark scope." },
        "500": { "$type": "color", "$value": "#33373C", "$description": "Brandbook Anthracite. Body text on light; the dark band ground." },
        "600": { "$type": "color", "$value": "#292C30", "$description": "Anthracite x0.80 toward black. Sunken inside the dark scope." },
        "mix760": { "$type": "color", "$value": "#606161", "$description": "Anthracite 76% + Nude 24%, resolved to a solid hex. Secondary text. 4.98 on Nude, 5.46 on Ivory. Opacity is NEVER used for text in this system." }
      },
      "white": { "$type": "color", "$value": "#FFFFFF" },
      "feedback": {
        "error": { "$type": "color", "$value": "#8C3A2E", "$description": "THE SIXTH COLOUR AND THE LAST ONE (DECISIONS.md §2). Muted terracotta. Form validation and payment failure ONLY. There is deliberately no -success and no -warning sibling; lint:tokens fails the build on those substrings." }
      }
    },

    "alpha": {
      "anthracite": {
        "08": { "$type": "color", "$value": "rgba(51,55,60,0.08)" },
        "12": { "$type": "color", "$value": "rgba(51,55,60,0.12)" },
        "20": { "$type": "color", "$value": "rgba(51,55,60,0.20)" },
        "38": { "$type": "color", "$value": "rgba(51,55,60,0.38)", "$description": "Disabled affordances only. 2.01 on Nude — fails contrast by design, never the only signal." },
        "60": { "$type": "color", "$value": "rgba(51,55,60,0.60)", "$description": "The overlay scrim. One value, no second scrim." }
      },
      "ivory": {
        "12": { "$type": "color", "$value": "rgba(243,240,233,0.12)" },
        "24": { "$type": "color", "$value": "rgba(243,240,233,0.24)" },
        "40": { "$type": "color", "$value": "rgba(243,240,233,0.40)" }
      },
      "olive": {
        "12": { "$type": "color", "$value": "rgba(124,134,84,0.12)", "$description": "Accent wash. Anthracite on it = 8.59 over Nude, 9.30 over Ivory." },
        "24": { "$type": "color", "$value": "rgba(124,134,84,0.24)", "$description": "Media placeholder ground only." }
      },
      "deepolive": {
        "08": { "$type": "color", "$value": "rgba(87,94,59,0.08)" },
        "16": { "$type": "color", "$value": "rgba(87,94,59,0.16)" }
      },
      "feedback": {
        "error10": { "$type": "color", "$value": "rgba(140,58,46,0.10)", "$description": "The error tint. An alpha, never a second hex — exactly one non-brand hue enters the palette. Error text on it: 5.27 over Nude, 5.76 over Ivory." }
      }
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

    "radius": {
      "0":    { "$type": "dimension", "$value": "0", "$description": "Bands, photographs, the report sheet, dividers, the plot diagram, the verification rail." },
      "sm":   { "$type": "dimension", "$value": "2px", "$description": "Buttons, inputs, cards, tariff cards, badges, modals, sheets, toasts, menus. The ONLY non-zero rectangular radius in the system." },
      "full": { "$type": "dimension", "$value": "9999px", "$description": "Slider thumb, avatar disc, petal bullet only." }
    },

    "border": {
      "0": { "$type": "dimension", "$value": "0" },
      "1": { "$type": "dimension", "$value": "1px" },
      "2": { "$type": "dimension", "$value": "2px" },
      "3": { "$type": "dimension", "$value": "3px" }
    },

    "duration": {
      "instant": { "$type": "duration", "$value": "80ms" },
      "fast":    { "$type": "duration", "$value": "140ms" },
      "base":    { "$type": "duration", "$value": "220ms" },
      "slow":    { "$type": "duration", "$value": "320ms" }
    },

    "ease": {
      "standard":   { "$type": "cubicBezier", "$value": [0.2, 0, 0, 1] },
      "decelerate": { "$type": "cubicBezier", "$value": [0, 0, 0, 1] },
      "accelerate": { "$type": "cubicBezier", "$value": [0.3, 0, 1, 1] }
    },

    "z": {
      "base":     { "$type": "number", "$value": 0 },
      "sticky":   { "$type": "number", "$value": 100 },
      "header":   { "$type": "number", "$value": 200 },
      "dropdown": { "$type": "number", "$value": 300 },
      "overlay":  { "$type": "number", "$value": 400 },
      "modal":    { "$type": "number", "$value": 410 },
      "toast":    { "$type": "number", "$value": 500 },
      "skiplink": { "$type": "number", "$value": 600 }
    },

    "fontFamily": {
      "display":  { "$type": "fontFamily", "$value": ["MC Dram", "Gloock", "Georgia", "serif"],
                    "$description": "Gloock Regular 400, single weight. Latin + Latin-ext coverage is UNVERIFIED; Cyrillic and Armenian coverage is UNVERIFIED and assumed absent. hy/ru headings fall back to the TEXT face at 600 — never to a second serif. See §6.4." },
      "text":     { "$type": "fontFamily", "$value": ["MC Dram", "Cabin", "Noto Sans Armenian", "Noto Sans", "system-ui", "-apple-system", "Segoe UI", "sans-serif"],
                    "$description": "Cabin is a SUBSTITUTE for Gill Sans (commercial Monotype, unlicensed for web). Label it as such in every mock, PDF and export. Cabin's coverage of Cyrillic and of U+058F is UNVERIFIED — the MC Dram face and the unicode-range declarations make the build correct either way." },
      "currency": { "$type": "fontFamily", "$value": ["MC Dram", "Noto Sans Armenian", "Noto Sans", "system-ui", "sans-serif"],
                    "$description": "Bound to U+058F only. Guarantees the dram sign renders whatever Cabin and Gloock contain." },
      "mono":     { "$type": "fontFamily", "$value": ["ui-monospace", "SF Mono", "Roboto Mono", "monospace"],
                    "$description": "GPS coordinates, invoice numbers, payment references, share tokens. Nothing else." }
    },

    "fontWeight": {
      "regular":  { "$type": "number", "$value": 400 },
      "semibold": { "$type": "number", "$value": 600 }
    }
  },

  "semantic": {
    "$description": "Layer 2. The decisions. Two scopes: :root (light) and .mc-on-dark (the Anthracite band).",

    "surface": {
      "page":            { "$type": "color", "$value": "{primitive.color.nude.500}", "$description": "Every full-bleed section is this colour. Testable, lint-enforced." },
      "raised":          { "$type": "color", "$value": "{primitive.color.ivory.500}", "$description": "Every object lifted off the ground: cards, the report sheet, inputs, the header bar." },
      "raised-hover":    { "$type": "color", "$value": "{primitive.color.ivory.400}" },
      "sunken":          { "$type": "color", "$value": "{primitive.color.nude.600}" },
      "inverse":         { "$type": "color", "$value": "{primitive.color.anthracite.500}" },
      "inverse-raised":  { "$type": "color", "$value": "{primitive.color.anthracite.400}" },
      "accent-strong":   { "$type": "color", "$value": "{primitive.color.olive.700}", "$description": "Primary button fill on light. Ivory label = 6.01." },
      "accent-solid":    { "$type": "color", "$value": "{primitive.color.olive.500}", "$description": "Decorative fills ONLY. NO LABEL MAY SIT ON THIS SURFACE." },
      "accent-wash":     { "$type": "color", "$value": "{primitive.alpha.olive.12}" },
      "float":           { "$type": "color", "$value": "{primitive.color.ivory.500}", "$description": "Menus, popovers and toasts take the OPPOSITE light of the band beneath them; .mc-on-ivory rewrites this to Nude." },
      "scrim":           { "$type": "color", "$value": "{primitive.alpha.anthracite.60}" },
      "media-placeholder": { "$type": "color", "$value": "{primitive.alpha.olive.24}" },
      "feedback-error-subtle": { "$type": "color", "$value": "{primitive.alpha.feedback.error10}" }
    },

    "text": {
      "primary":   { "$type": "color", "$value": "{primitive.color.anthracite.500}", "$description": "9.61 on page, 10.53 on raised." },
      "secondary": { "$type": "color", "$value": "{primitive.color.anthracite.mix760}", "$description": "4.98 on page, 5.46 on raised. Permitted at >=14px. NEVER used for proof data (rail values) — those are text.primary." },
      "accent":    { "$type": "color", "$value": "{primitive.color.olive.700}", "$description": "5.49 on page, 6.01 on raised. Rewritten to Nude inside .mc-on-dark." },
      "link":      { "$type": "color", "$value": "{primitive.color.olive.700}" },
      "link-hover":{ "$type": "color", "$value": "{primitive.color.olive.800}", "$description": "6.30 on page, 6.90 on raised." },
      "on-accent": { "$type": "color", "$value": "{primitive.color.ivory.500}" },
      "inverse":   { "$type": "color", "$value": "{primitive.color.nude.500}", "$description": "9.61 on inverse." },
      "feedback-error": { "$type": "color", "$value": "{primitive.color.feedback.error}", "$description": "6.10 on page, 6.69 on raised, 1.57 on inverse — FORBIDDEN on any dark ground." },
      "disabled":  { "$type": "color", "$value": "{primitive.alpha.anthracite.38}", "$description": "2.01 on page. FAILS BY DESIGN. Never the only signal: aria-disabled + no pointer cursor accompany it always." }
    },

    "border": {
      "subtle":        { "$type": "color", "$value": "{primitive.alpha.anthracite.08}" },
      "default":       { "$type": "color", "$value": "{primitive.alpha.anthracite.12}", "$description": "The object hairline. Every raised object on a light ground carries one." },
      "strong":        { "$type": "color", "$value": "{primitive.alpha.anthracite.20}" },
      "accent":        { "$type": "color", "$value": "{primitive.color.olive.700}" },
      "decorative":    { "$type": "color", "$value": "{primitive.color.olive.500}", "$description": "Rules, dividers, ornament. 1px at 100% opacity. Never under text, never at partial opacity." },
      "focus":         { "$type": "color", "$value": "{primitive.color.olive.700}" },
      "focus-inverse": { "$type": "color", "$value": "{primitive.color.nude.500}" },
      "feedback-error":{ "$type": "color", "$value": "{primitive.color.feedback.error}" },
      "inverse":       { "$type": "color", "$value": "{primitive.alpha.ivory.24}" }
    },

    "elevation": {
      "0":       { "$type": "shadow", "$value": "none", "$description": "The default for EVERY object in the system. Elevation is a ground change plus a 1px hairline." },
      "overlay": { "$type": "shadow", "$value": "0 16px 40px rgba(51,55,60,0.16)", "$description": "The ONLY shadow. Modal, drawer, bottom sheet, lightbox, toast. Nothing else may reference it." }
    },

    "layout": {
      "container-max":    { "$type": "dimension", "$value": "1200px" },
      "container-narrow": { "$type": "dimension", "$value": "760px" },
      "header-height":    { "$type": "dimension", "$value": "56px" },
      "actionbar-height": { "$type": "dimension", "$value": "64px" },
      "target-min":       { "$type": "dimension", "$value": "44px" },
      "focus-width":      { "$type": "dimension", "$value": "{primitive.border.2}" },
      "focus-offset":     { "$type": "dimension", "$value": "{primitive.border.2}" },
      "logo-clearspace":  { "$type": "dimension", "$value": "0.42em" }
    },

    "motion": {
      "hover":  { "$type": "transition", "$value": { "duration": "{primitive.duration.fast}", "timingFunction": "{primitive.ease.standard}" } },
      "enter":  { "$type": "transition", "$value": { "duration": "{primitive.duration.base}", "timingFunction": "{primitive.ease.decelerate}" } },
      "exit":   { "$type": "transition", "$value": { "duration": "{primitive.duration.fast}", "timingFunction": "{primitive.ease.accelerate}" } },
      "expand": { "$type": "transition", "$value": { "duration": "{primitive.duration.base}", "timingFunction": "{primitive.ease.standard}" } },
      "distance-sm": { "$type": "dimension", "$value": "4px" },
      "distance-md": { "$type": "dimension", "$value": "8px" }
    },

    "type": {
      "display-1":  { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.display}", "fontSize": "clamp(2rem, 1.25rem + 3.3vw, 3.5rem)", "lineHeight": "1.08", "letterSpacing": "-0.01em", "fontWeight": "{primitive.fontWeight.regular}" } },
      "display-2":  { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.display}", "fontSize": "clamp(1.75rem, 1.2rem + 2.4vw, 2.75rem)", "lineHeight": "1.12", "letterSpacing": "-0.005em", "fontWeight": "{primitive.fontWeight.regular}" } },
      "heading-1":  { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.display}", "fontSize": "clamp(1.625rem, 1.25rem + 1.6vw, 2.25rem)", "lineHeight": "1.18", "letterSpacing": "0", "fontWeight": "{primitive.fontWeight.regular}" } },
      "heading-2":  { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.display}", "fontSize": "clamp(1.5rem, 1.3rem + 0.85vw, 1.75rem)", "lineHeight": "1.24", "letterSpacing": "0", "fontWeight": "{primitive.fontWeight.regular}" }, "$description": "Minimum resolves to 24px. Gloock is NEVER set below 24px — its hairlines break up." },
      "heading-3":  { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "clamp(1.125rem, 1.05rem + 0.3vw, 1.25rem)", "lineHeight": "1.35", "letterSpacing": "0", "fontWeight": "{primitive.fontWeight.semibold}" } },
      "body-lg":    { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem)", "lineHeight": "1.6", "letterSpacing": "0", "fontWeight": "{primitive.fontWeight.regular}" } },
      "body":       { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "clamp(1rem, 0.96rem + 0.18vw, 1.0625rem)", "lineHeight": "1.6", "letterSpacing": "0", "fontWeight": "{primitive.fontWeight.regular}" }, "$description": "16px mobile -> 17px desktop. 16px is the iOS no-zoom floor for inputs." },
      "body-sm":    { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "0.9375rem", "lineHeight": "1.55", "letterSpacing": "0", "fontWeight": "{primitive.fontWeight.regular}" } },
      "label":      { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "0.9375rem", "lineHeight": "1.4", "letterSpacing": "0.01em", "fontWeight": "{primitive.fontWeight.semibold}" } },
      "caption":    { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "0.875rem", "lineHeight": "1.45", "letterSpacing": "0.01em", "fontWeight": "{primitive.fontWeight.regular}" } },
      "rail":       { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "0.875rem", "lineHeight": "1.4", "letterSpacing": "0.06em", "fontWeight": "{primitive.fontWeight.semibold}" }, "$description": "14px, per the owner ruling — it carries the PROOF (date, cemetery, plot, crew, coordinates) for a 40-60 audience on a phone. Labels are uppercase in Latin/Cyrillic and sentence case in Armenian. VALUES ARE NEVER UPPERCASE IN ANY SCRIPT and are tabular." },
      "overline":   { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.text}", "fontSize": "0.8125rem", "lineHeight": "1.3", "letterSpacing": "0.12em", "fontWeight": "{primitive.fontWeight.semibold}" }, "$description": "13px. The absolute floor of the system. Decorative section eyebrows only — never data. Sentence case in Armenian." },
      "price":      { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.display}", "fontSize": "clamp(1.75rem, 1.3rem + 1.9vw, 2.5rem)", "lineHeight": "1.0", "letterSpacing": "-0.01em", "fontWeight": "{primitive.fontWeight.regular}" }, "$description": "The AMOUNT only. The unit '֏ AMD' is always set in type.body in the TEXT face on its own line beneath. If qa/glyphs.spec.ts reports the display face has no tabular figures, this token falls back to the text face at 600 — one token change, no component edits." },
      "numeric":    { "$type": "typography", "$value": { "fontFamily": "{primitive.fontFamily.mono}", "fontSize": "0.875rem", "lineHeight": "1.5", "letterSpacing": "0.02em", "fontWeight": "{primitive.fontWeight.regular}" } }
    }
  },

  "component": {
    "$description": "Layer 3. The contract with the markup. Every value here resolves to Layer 2.",

    "button": {
      "radius":         { "$type": "dimension", "$value": "{primitive.radius.sm}" },
      "min-height":     { "$type": "dimension", "$value": "48px" },
      "min-height-sm":  { "$type": "dimension", "$value": "40px" },
      "min-height-lg":  { "$type": "dimension", "$value": "56px" },
      "padding-inline": { "$type": "dimension", "$value": "{primitive.size.6}" },
      "gap":            { "$type": "dimension", "$value": "{primitive.size.2}" },
      "primary":   { "bg": { "default": { "$type": "color", "$value": "{semantic.surface.accent-strong}" },
                             "hover":   { "$type": "color", "$value": "{primitive.color.olive.800}" },
                             "active":  { "$type": "color", "$value": "{primitive.color.olive.900}" },
                             "disabled":{ "$type": "color", "$value": "{primitive.alpha.anthracite.12}" } },
                     "fg": { "default": { "$type": "color", "$value": "{semantic.text.on-accent}" },
                             "disabled":{ "$type": "color", "$value": "{semantic.text.disabled}" } } },
      "secondary": { "bg": { "default": { "$type": "color", "$value": "transparent" },
                             "hover":   { "$type": "color", "$value": "{primitive.alpha.deepolive.08}" },
                             "active":  { "$type": "color", "$value": "{primitive.alpha.deepolive.16}" } },
                     "fg": { "default": { "$type": "color", "$value": "{semantic.text.accent}" } },
                     "border": { "default": { "$type": "color", "$value": "{semantic.border.accent}" } } },
      "tertiary":  { "fg": { "default": { "$type": "color", "$value": "{semantic.text.accent}" },
                             "hover":   { "$type": "color", "$value": "{semantic.text.link-hover}" } } }
    },

    "input": {
      "min-height":     { "$type": "dimension", "$value": "48px" },
      "radius":         { "$type": "dimension", "$value": "{primitive.radius.sm}" },
      "bg":             { "$type": "color", "$value": "{semantic.surface.raised}" },
      "bg-disabled":    { "$type": "color", "$value": "{semantic.surface.sunken}" },
      "border":         { "$type": "color", "$value": "{semantic.border.strong}" },
      "border-hover":   { "$type": "color", "$value": "{primitive.alpha.anthracite.38}" },
      "border-focus":   { "$type": "color", "$value": "{semantic.border.focus}" },
      "border-error":   { "$type": "color", "$value": "{semantic.border.feedback-error}" },
      "fg":             { "$type": "color", "$value": "{semantic.text.primary}" },
      "placeholder":    { "$type": "color", "$value": "{semantic.text.secondary}" },
      "padding-inline": { "$type": "dimension", "$value": "{primitive.size.4}" }
    },

    "card": {
      "radius":     { "$type": "dimension", "$value": "{primitive.radius.sm}" },
      "bg":         { "$type": "color", "$value": "{semantic.surface.raised}" },
      "border":     { "$type": "color", "$value": "{semantic.border.default}" },
      "border-hover": { "$type": "color", "$value": "{semantic.border.decorative}" },
      "padding":    { "$type": "dimension", "$value": "{primitive.size.5}" },
      "padding-lg": { "$type": "dimension", "$value": "{primitive.size.8}" }
    },

    "tariff-card": {
      "border":           { "$type": "color", "$value": "{semantic.border.default}" },
      "border-leading":   { "$type": "color", "$value": "{semantic.border.accent}" },
      "border-leading-width": { "$type": "dimension", "$value": "{primitive.border.2}" },
      "padding":          { "$type": "dimension", "$value": "{primitive.size.6}" }
    },

    "badge": {
      "radius":         { "$type": "dimension", "$value": "{primitive.radius.sm}" },
      "min-height":     { "$type": "dimension", "$value": "24px" },
      "padding-inline": { "$type": "dimension", "$value": "{primitive.size.3}" }
    },

    "modal": {
      "radius":    { "$type": "dimension", "$value": "{primitive.radius.sm}" },
      "max-width": { "$type": "dimension", "$value": "560px" },
      "padding":   { "$type": "dimension", "$value": "{primitive.size.6}" },
      "shadow":    { "$type": "shadow", "$value": "{semantic.elevation.overlay}" }
    },

    "toast": {
      "radius":    { "$type": "dimension", "$value": "{primitive.radius.sm}" },
      "max-width": { "$type": "dimension", "$value": "420px" },
      "padding":   { "$type": "dimension", "$value": "{primitive.size.4}" },
      "shadow":    { "$type": "shadow", "$value": "{semantic.elevation.overlay}" }
    },

    "rail": {
      "width-lg":   { "$type": "dimension", "$value": "222px" },
      "label-color":{ "$type": "color", "$value": "{semantic.text.secondary}" },
      "value-color":{ "$type": "color", "$value": "{semantic.text.primary}" },
      "rule":       { "$type": "color", "$value": "{semantic.border.default}" }
    },

    "slider": {
      "track-height": { "$type": "dimension", "$value": "4px" },
      "track-bg":     { "$type": "color", "$value": "{semantic.border.strong}" },
      "track-fill":   { "$type": "color", "$value": "{semantic.surface.accent-strong}" },
      "thumb-size":   { "$type": "dimension", "$value": "28px" },
      "thumb-bg":     { "$type": "color", "$value": "{semantic.surface.raised}" },
      "thumb-border": { "$type": "color", "$value": "{semantic.border.accent}" }
    }
  }
}
```

**Build:** `style-dictionary build --config tokens/sd.config.js` emits
`build/mc-tokens.css`, `build/mc-tokens.scss`, `build/tailwind.tokens.js` and
`build/tokens.d.ts`. Generated files are **committed but never hand-edited**; a
pre-commit hook rebuilds and fails on drift.

---

## 3. `tokens/build/mc-tokens.css` — complete, copy this into the file

```css
/* ============================================================================
   MemoryCare design tokens v1.0 FINAL — GENERATED from tokens/tokens.json.
   DO NOT EDIT. Change tokens.json and rebuild.

   NOTE ON TYPE: Cabin is used as a free substitute for Gill Sans (commercial
   Monotype, unlicensed for web). It is not the brand text face.
   ============================================================================ */

/* ---------- @font-face: the currency binding comes FIRST ----------
   U+058F (֏) is bound to a face that certainly carries it, independently of
   locale and independently of what Cabin or Gloock turn out to contain.
   Every stack below terminates in a generic family: no stack can dead-end,
   and no missing glyph can render as tofu. See §6.4 and qa/glyphs.spec.ts. */

@font-face {
  font-family: "MC Dram";
  src: url("/fonts/noto-sans-armenian-400.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
  unicode-range: U+058F;
}
@font-face {
  font-family: "Gloock";
  src: url("/fonts/gloock-400.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
  unicode-range: U+0000-00FF, U+0100-017F, U+2000-206F;
}
@font-face {
  font-family: "Cabin";
  src: url("/fonts/cabin-400.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
  unicode-range: U+0000-00FF, U+0100-017F, U+2000-206F, U+20B4-20BF;
}
@font-face {
  font-family: "Cabin";
  src: url("/fonts/cabin-600.woff2") format("woff2");
  font-weight: 600; font-style: normal; font-display: swap;
  unicode-range: U+0000-00FF, U+0100-017F, U+2000-206F, U+20B4-20BF;
}
@font-face {
  font-family: "Noto Sans Armenian";
  src: url("/fonts/noto-sans-armenian-400.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
  unicode-range: U+0530-058F, U+FB13-FB17;
}
@font-face {
  font-family: "Noto Sans Armenian";
  src: url("/fonts/noto-sans-armenian-600.woff2") format("woff2");
  font-weight: 600; font-style: normal; font-display: swap;
  unicode-range: U+0530-058F, U+FB13-FB17;
}
@font-face {
  font-family: "Noto Sans";
  src: url("/fonts/noto-sans-cyrillic-400.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
  unicode-range: U+0400-04FF, U+0500-052F;
}
@font-face {
  font-family: "Noto Sans";
  src: url("/fonts/noto-sans-cyrillic-600.woff2") format("woff2");
  font-weight: 600; font-style: normal; font-display: swap;
  unicode-range: U+0400-04FF, U+0500-052F;
}

:root {
  /* ========== LAYER 1 · PRIMITIVE · COLOUR ========== */
  --mc-color-olive-500: #7C8654;   /* decorative only — never under or behind text */
  --mc-color-olive-700: #575E3B;   /* Deep Olive, interface only, WORKING VALUE */
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
  --mc-color-feedback-error: #8C3A2E;  /* the sixth colour. The last one. */

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
  --mc-alpha-feedback-error-10: rgba(140,58,46,.10);

  /* ========== LAYER 1 · PRIMITIVE · SIZE ========== */
  --mc-size-0: 0rem;     --mc-size-0-5: .125rem; --mc-size-1: .25rem;
  --mc-size-2: .5rem;    --mc-size-3: .75rem;    --mc-size-4: 1rem;
  --mc-size-5: 1.25rem;  --mc-size-6: 1.5rem;    --mc-size-8: 2rem;
  --mc-size-10: 2.5rem;  --mc-size-12: 3rem;     --mc-size-16: 4rem;
  --mc-size-20: 5rem;    --mc-size-24: 6rem;     --mc-size-30: 7.5rem;
  --mc-size-40: 10rem;   --mc-size-50: 12.5rem;

  /* Three radii. There is no 4px, 6px, 8px, 10px, 14px or 20px in this system. */
  --mc-radius-0: 0;
  --mc-radius-sm: 2px;
  --mc-radius-md: 8px;              /* overlays only: modal, drawer, sheet, lightbox */
  --mc-radius-full: 9999px;

  --mc-border-0: 0; --mc-border-1: 1px; --mc-border-2: 2px; --mc-border-3: 3px;

  --mc-duration-instant: 80ms;
  --mc-duration-fast: 140ms;
  --mc-duration-base: 220ms;
  --mc-duration-slow: 320ms;
  --mc-ease-standard:   cubic-bezier(.2,0,0,1);
  --mc-ease-decelerate: cubic-bezier(0,0,0,1);
  --mc-ease-accelerate: cubic-bezier(.3,0,1,1);

  --mc-z-base: 0; --mc-z-sticky: 100; --mc-z-header: 200; --mc-z-dropdown: 300;
  --mc-z-overlay: 400; --mc-z-modal: 410; --mc-z-toast: 500; --mc-z-skiplink: 600;

  --mc-font-display: "MC Dram", "Gloock", Georgia, serif;
  --mc-font-text: "MC Dram", "Cabin", "Noto Sans Armenian", "Noto Sans",
                  system-ui, -apple-system, "Segoe UI", sans-serif;
  --mc-font-currency: "MC Dram", "Noto Sans Armenian", "Noto Sans",
                      system-ui, sans-serif;
  --mc-font-mono: ui-monospace, "SF Mono", "Roboto Mono", monospace;
  --mc-weight-regular: 400;
  --mc-weight-semibold: 600;

  /* ========== LAYER 2 · SEMANTIC · SURFACE ========== */
  --mc-surface-page: var(--mc-color-nude-500);
  --mc-surface-raised: var(--mc-color-ivory-500);
  --mc-surface-raised-hover: var(--mc-color-ivory-400);
  --mc-surface-sunken: var(--mc-color-nude-600);
  --mc-surface-inverse: var(--mc-color-anthracite-500);
  --mc-surface-inverse-raised: var(--mc-color-anthracite-400);
  --mc-surface-accent-strong: var(--mc-color-olive-700);
  --mc-surface-accent-solid: var(--mc-color-olive-500);
  --mc-surface-accent-wash: var(--mc-alpha-olive-12);
  --mc-surface-float: var(--mc-color-ivory-500);
  --mc-surface-scrim: var(--mc-alpha-anthracite-60);
  --mc-surface-media-placeholder: var(--mc-alpha-olive-24);
  --mc-surface-feedback-error-subtle: var(--mc-alpha-feedback-error-10);

  /* ========== LAYER 2 · SEMANTIC · TEXT ========== */
  --mc-text-primary: var(--mc-color-anthracite-500);
  --mc-text-secondary: var(--mc-color-anthracite-mix760);
  --mc-text-accent: var(--mc-color-olive-700);
  --mc-text-link: var(--mc-color-olive-700);
  --mc-text-link-hover: var(--mc-color-olive-800);
  --mc-text-on-accent: var(--mc-color-ivory-500);
  --mc-text-inverse: var(--mc-color-nude-500);
  --mc-text-feedback-error: var(--mc-color-feedback-error);
  --mc-text-disabled: var(--mc-alpha-anthracite-38);

  /* ========== LAYER 2 · SEMANTIC · BORDER ========== */
  --mc-border-subtle: var(--mc-alpha-anthracite-08);
  --mc-border-default: var(--mc-alpha-anthracite-12);
  --mc-border-strong: var(--mc-alpha-anthracite-20);
  --mc-border-accent: var(--mc-color-olive-700);
  --mc-border-decorative: var(--mc-color-olive-500);
  --mc-border-focus: var(--mc-color-olive-700);
  --mc-border-focus-inverse: var(--mc-color-nude-500);
  --mc-border-feedback-error: var(--mc-color-feedback-error);
  --mc-border-inverse: var(--mc-alpha-ivory-24);

  /* ========== LAYER 2 · SEMANTIC · ELEVATION ==========
     Two values. Elevation is a ground change plus a 1px hairline. */
  --mc-elevation-0: none;
  --mc-elevation-overlay: 0 16px 40px rgba(51,55,60,.16);

  /* ========== LAYER 2 · SEMANTIC · LAYOUT ========== */
  --mc-layout-container-max: 1200px;
  --mc-layout-container-narrow: 760px;
  --mc-layout-header-height: 56px;
  --mc-layout-actionbar-height: 64px;
  --mc-layout-gutter: 16px;
  --mc-layout-margin: 20px;
  --mc-layout-section-block: clamp(3rem, 2rem + 5vw, 7.5rem);
  --mc-layout-target-min: 44px;
  --mc-layout-logo-clearspace: 0.42em;
  --mc-focus-width: var(--mc-border-2);
  --mc-focus-offset: var(--mc-border-2);

  /* ========== LAYER 2 · SEMANTIC · MOTION ========== */
  --mc-motion-hover: var(--mc-duration-fast) var(--mc-ease-standard);
  --mc-motion-enter: var(--mc-duration-base) var(--mc-ease-decelerate);
  --mc-motion-exit: var(--mc-duration-fast) var(--mc-ease-accelerate);
  --mc-motion-expand: var(--mc-duration-base) var(--mc-ease-standard);
  --mc-motion-distance-sm: 4px;
  --mc-motion-distance-md: 8px;

  /* ========== LAYER 2 · SEMANTIC · TYPE ========== */
  --mc-type-display-1-font: var(--mc-font-display);
  --mc-type-display-1-size: clamp(2rem, 1.25rem + 3.3vw, 3.5rem);
  --mc-type-display-1-lh: 1.08;
  --mc-type-display-1-ls: -0.01em;

  --mc-type-display-2-font: var(--mc-font-display);
  --mc-type-display-2-size: clamp(1.75rem, 1.2rem + 2.4vw, 2.75rem);
  --mc-type-display-2-lh: 1.12;
  --mc-type-display-2-ls: -0.005em;

  --mc-type-heading-1-font: var(--mc-font-display);
  --mc-type-heading-1-size: clamp(1.625rem, 1.25rem + 1.6vw, 2.25rem);
  --mc-type-heading-1-lh: 1.18;

  --mc-type-heading-2-font: var(--mc-font-display);
  --mc-type-heading-2-size: clamp(1.5rem, 1.3rem + .85vw, 1.75rem); /* min 24px */
  --mc-type-heading-2-lh: 1.24;

  --mc-type-heading-3-font: var(--mc-font-text);
  --mc-type-heading-3-size: clamp(1.125rem, 1.05rem + .3vw, 1.25rem);
  --mc-type-heading-3-lh: 1.35;
  --mc-type-heading-3-weight: var(--mc-weight-semibold);

  --mc-type-body-lg-size: clamp(1.0625rem, 1rem + .25vw, 1.1875rem);
  --mc-type-body-lg-lh: 1.6;
  --mc-type-body-size: clamp(1rem, .96rem + .18vw, 1.0625rem);
  --mc-type-body-lh: 1.6;
  --mc-type-body-sm-size: .9375rem;
  --mc-type-body-sm-lh: 1.55;

  --mc-type-label-size: .9375rem;
  --mc-type-label-lh: 1.4;
  --mc-type-label-ls: .01em;

  --mc-type-caption-size: .875rem;
  --mc-type-caption-lh: 1.45;

  --mc-type-rail-size: .875rem;      /* 14px — owner ruling, not 11-12 */
  --mc-type-rail-lh: 1.4;
  --mc-type-rail-ls: .06em;

  --mc-type-overline-size: .8125rem; /* 13px — the absolute floor */
  --mc-type-overline-lh: 1.3;
  --mc-type-overline-ls: .12em;

  --mc-type-price-font: var(--mc-font-display);
  --mc-type-price-size: clamp(1.75rem, 1.3rem + 1.9vw, 2.5rem);
  --mc-type-price-lh: 1;
  --mc-type-price-ls: -0.01em;

  --mc-type-numeric-font: var(--mc-font-mono);
  --mc-type-numeric-size: .875rem;
  --mc-type-numeric-ls: .02em;

  /* ========== LAYER 3 · COMPONENT ========== */
  --mc-button-radius: var(--mc-radius-sm);
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
  --mc-button-secondary-bg-active: var(--mc-alpha-deepolive-16);
  --mc-button-secondary-fg: var(--mc-text-accent);
  --mc-button-secondary-border: var(--mc-border-accent);
  --mc-button-tertiary-fg: var(--mc-text-accent);
  --mc-button-tertiary-fg-hover: var(--mc-text-link-hover);

  --mc-input-min-height: 48px;
  --mc-input-radius: var(--mc-radius-sm);
  --mc-input-bg: var(--mc-surface-raised);
  --mc-input-bg-disabled: var(--mc-surface-sunken);
  --mc-input-border: var(--mc-border-strong);
  --mc-input-border-hover: var(--mc-alpha-anthracite-38);
  --mc-input-border-focus: var(--mc-border-focus);
  --mc-input-border-error: var(--mc-border-feedback-error);
  --mc-input-fg: var(--mc-text-primary);
  --mc-input-placeholder: var(--mc-text-secondary);
  --mc-input-padding-inline: var(--mc-size-4);
  --mc-input-label-gap: var(--mc-size-2);
  --mc-input-help-gap: var(--mc-size-2);

  --mc-card-radius: var(--mc-radius-sm);
  --mc-card-bg: var(--mc-surface-raised);
  --mc-card-border: var(--mc-border-default);
  --mc-card-border-hover: var(--mc-border-decorative);
  --mc-card-padding: var(--mc-size-5);
  --mc-card-padding-lg: var(--mc-size-8);

  --mc-tariff-border: var(--mc-border-default);
  --mc-tariff-border-leading: var(--mc-border-accent);
  --mc-tariff-border-leading-width: var(--mc-border-2);
  --mc-tariff-padding: var(--mc-size-6);

  --mc-badge-radius: var(--mc-radius-sm);
  --mc-badge-min-height: 24px;
  --mc-badge-padding-inline: var(--mc-size-3);

  --mc-modal-radius: var(--mc-radius-md);
  --mc-modal-max-width: 560px;
  --mc-modal-padding: var(--mc-size-6);
  --mc-modal-shadow: var(--mc-elevation-overlay);

  --mc-toast-radius: var(--mc-radius-sm);
  --mc-toast-max-width: 420px;
  --mc-toast-padding: var(--mc-size-4);
  --mc-toast-shadow: var(--mc-elevation-overlay);

  --mc-rail-width-lg: 222px;
  --mc-rail-label-color: var(--mc-text-secondary);
  --mc-rail-value-color: var(--mc-text-primary);
  --mc-rail-rule: var(--mc-border-default);

  --mc-slider-track-height: 4px;
  --mc-slider-track-bg: var(--mc-border-strong);
  --mc-slider-track-fill: var(--mc-surface-accent-strong);
  --mc-slider-thumb-size: 28px;
  --mc-slider-thumb-bg: var(--mc-surface-raised);
  --mc-slider-thumb-border: var(--mc-border-accent);
}

/* ============================================================================
   RESPONSIVE OVERRIDES — min-width only, breakpoints 360/600/900/1200/1440
   ============================================================================ */
@media (min-width: 600px) {
  :root { --mc-layout-gutter: 24px; --mc-layout-margin: 40px; }
}
@media (min-width: 900px) {
  :root { --mc-layout-header-height: 72px; }
}
@media (min-width: 1200px) {
  :root { --mc-button-min-height: 44px; --mc-input-min-height: 44px; }
}
@media (min-width: 1440px) {
  :root { --mc-layout-gutter: 32px; }
}

/* ============================================================================
   SCOPE: the Anthracite band. Applied with a CLASS, never a media query.
   MemoryCare has no OS dark mode — a visitor's system setting must never
   repaint a page containing photographs of a grave in colours we did not check.
   ============================================================================ */
.mc-on-dark {
  --mc-surface-page: var(--mc-color-anthracite-500);
  --mc-surface-raised: var(--mc-color-anthracite-400);
  --mc-surface-raised-hover: #52565A;
  --mc-surface-sunken: var(--mc-color-anthracite-600);
  --mc-surface-inverse: var(--mc-color-nude-500);
  --mc-surface-float: var(--mc-color-anthracite-400);

  --mc-text-primary: var(--mc-color-nude-500);
  --mc-text-secondary: var(--mc-color-ivory-500);
  --mc-text-accent: var(--mc-color-nude-500);   /* Deep Olive is 1.75 here */
  --mc-text-link: var(--mc-color-nude-500);
  --mc-text-link-hover: var(--mc-color-white);
  --mc-text-on-accent: var(--mc-color-anthracite-500);

  --mc-border-subtle: var(--mc-alpha-ivory-12);
  --mc-border-default: var(--mc-alpha-ivory-24);
  --mc-border-strong: var(--mc-alpha-ivory-40);
  --mc-border-accent: var(--mc-color-nude-500);
  --mc-border-focus: var(--mc-border-focus-inverse);

  --mc-button-primary-bg: var(--mc-color-nude-500);
  --mc-button-primary-bg-hover: var(--mc-color-nude-400);
  --mc-button-primary-bg-active: var(--mc-color-ivory-400);
  --mc-button-primary-fg: var(--mc-color-anthracite-500);
  --mc-button-secondary-fg: var(--mc-color-nude-500);
  --mc-button-secondary-border: var(--mc-alpha-ivory-40);
  --mc-button-secondary-bg-hover: var(--mc-alpha-ivory-12);
  --mc-button-tertiary-fg: var(--mc-color-nude-500);
  --mc-input-bg: var(--mc-alpha-ivory-12);
  --mc-card-bg: var(--mc-surface-inverse-raised);
  --mc-card-border: var(--mc-alpha-ivory-12);
}

/* A form may NEVER be placed inside .mc-on-dark: the error colour is 1.57 on
   Anthracite and a validation error would be invisible. Enforced by
   stylelint-mc-contrast and asserted in qa/contrast.spec.ts. */

/* ============================================================================
   SCOPE: a band whose ground is Ivory (the header bar is the only one).
   Floating layers take the OPPOSITE light of the band beneath them, so a menu
   never opens Ivory-on-Ivory.
   ============================================================================ */
.mc-on-ivory { --mc-surface-float: var(--mc-color-nude-500); }

/* ============================================================================
   GLOBAL ACCESSIBILITY PRIMITIVES
   ============================================================================ */
*:focus-visible {
  outline: var(--mc-focus-width) solid var(--mc-border-focus);
  outline-offset: var(--mc-focus-offset);
  border-radius: var(--mc-radius-sm);
}
/* On a Deep Olive fill the ring would vanish into the button. Two rings:
   inner Ivory, outer Deep Olive halo. */
.mc-button--primary:focus-visible {
  outline: var(--mc-focus-width) solid var(--mc-color-ivory-500);
  outline-offset: calc(-1 * var(--mc-focus-width) - 1px);
  box-shadow: 0 0 0 4px var(--mc-alpha-deepolive-16);
}

/* 44x44 hit area for a control whose visual is smaller.
   NOTE: the earlier `inset: 50% 50% 50% 50%` version SILENTLY DID NOT WORK —
   setting all four insets makes width/height inert and the box collapses to
   zero. This is the corrected rule. */
.mc-hit-44 { position: relative; }
.mc-hit-44::after {
  content: "";
  position: absolute;
  top: 50%;
  inset-inline-start: 50%;
  width: max(100%, var(--mc-layout-target-min));
  height: max(100%, var(--mc-layout-target-min));
  transform: translate(-50%, -50%);
}

/* Prices. The amount may be display type; the unit is always text type, and
   the dram sign is always bound to --mc-font-currency. */
.mc-price__amount { font-family: var(--mc-type-price-font);
                    font-size: var(--mc-type-price-size);
                    line-height: var(--mc-type-price-lh);
                    font-variant-numeric: tabular-nums; }
.mc-price__unit   { font-family: var(--mc-font-text);
                    font-size: var(--mc-type-body-size);
                    color: var(--mc-text-secondary); display: block; }
.mc-currency      { font-family: var(--mc-font-currency); }

/* Tabular figures wherever a number can change or must align. */
.mc-tabular, .mc-price__amount, .mc-rail__value,
[class*="mc-calculator"] output { font-variant-numeric: tabular-nums; }

/* Armenian never sets uppercase — Armenian caps read as shouting. */
:lang(hy) .mc-overline,
:lang(hy) .mc-rail__label { text-transform: none; letter-spacing: .06em; }
/* Rail VALUES are never uppercase in any script. */
.mc-rail__value { text-transform: none; }

@media (prefers-reduced-motion: reduce) {
  :root {
    --mc-duration-instant: 1ms; --mc-duration-fast: 1ms;
    --mc-duration-base: 1ms;    --mc-duration-slow: 1ms;
    --mc-motion-distance-sm: 0px; --mc-motion-distance-md: 0px;
  }
  *, *::before, *::after {
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 1ms !important;
    scroll-behavior: auto !important;
  }
}
```

**Reduced motion is not "animations off".** Opacity cross-fades survive at 1ms
so they are instant; translate distances collapse to 0; the loading arc becomes
a static arc plus its text label. Because there is no count-up and no
auto-advance anywhere in this system, the reduced-motion path and the default
path differ only in duration — which is always the better outcome.

---

## 4. The allowed contrast pairs — a closed list

**A foreground/background combination that is not in this table does not exist
in the system.** `stylelint-mc-contrast` fails the build on any `color` /
`background-color` pair that is not here. All ratios below were measured against
the official hexes, not estimated.

### 4.1 Permitted

| # | Foreground | Background | Ratio | Permitted for |
|---|---|---|---|---|
| 1 | `text-primary` #33373C | `surface-page` #EFE5D5 | **9.61** | all text, any size |
| 2 | `text-primary` | `surface-raised` #F3F0E9 | **10.53** | all text |
| 3 | `text-primary` | `surface-sunken` #E4D8C4 | **8.51** | all text |
| 4 | `text-primary` | `surface-accent-wash` over Nude | **8.59** | all text (the GPS chip) |
| 5 | `text-primary` | `surface-accent-wash` over Ivory | **9.30** | all text |
| 6 | `text-secondary` #606161 | `surface-page` | **4.98** | text ≥14px only |
| 7 | `text-secondary` | `surface-raised` | **5.46** | text ≥14px only |
| 8 | `text-accent` #575E3B | `surface-page` | **5.49** | all text, links, icons |
| 9 | `text-accent` | `surface-raised` | **6.01** | all text |
| 10 | `text-link-hover` #4E5535 | `surface-page` | **6.30** | all text |
| 11 | `text-link-hover` | `surface-raised` | **6.90** | all text |
| 12 | `text-on-accent` #F3F0E9 | `surface-accent-strong` #575E3B | **6.01** | primary button label, `Badge--accent` |
| 13 | `color-white` | `surface-accent-strong` | **6.84** | permitted, but Ivory (row 12) is the brand choice |
| 14 | `text-inverse` #EFE5D5 | `surface-inverse` #33373C | **9.61** | all text on the dark band |
| 15 | `color-ivory-500` | `surface-inverse` | **10.53** | all text on the dark band |
| 16 | `text-inverse` | `surface-inverse-raised` #4A4D51 | **6.81** | all text on a dark card |
| 17 | `color-ivory-500` | `surface-inverse-raised` | **7.47** | all text on a dark card |
| 18 | `surface-inverse` #33373C | `color-nude-500` fill | **9.61** | the dark-scope primary button (Nude fill, Anthracite label) |
| 19 | `text-feedback-error` #8C3A2E | `surface-page` | **6.10** | error text, border, glyph |
| 20 | `text-feedback-error` | `surface-raised` | **6.69** | error text, border, glyph |
| 21 | `text-feedback-error` | `surface-feedback-error-subtle` over Nude | **5.27** | error panel text |
| 22 | `text-feedback-error` | `surface-feedback-error-subtle` over Ivory | **5.76** | error panel text |
| 23 | `color-white` | `color-feedback-error` fill | **7.61** | permitted but unused — the error colour never fills a button |
| 24 | `color-ivory-500` | `color-feedback-error` fill | **6.69** | permitted but unused, same reason |

### 4.2 Forbidden — and why each one is the mistake this palette invites

| Foreground | Background | Ratio | Ruling |
|---|---|---|---|
| **anything** | `surface-accent-solid` Olive #7C8654 | ≤3.42 | **NO LABEL ON OLIVE, EVER.** Anthracite on Olive 3.08, Ivory on Olive 3.42. Two independent reviewers reached for this exact pair, which is why it is blocked in code and not only in prose. |
| Olive #7C8654 | Nude / Ivory / Anthracite | 3.12 / 3.42 / 3.08 | **Olive never carries text**, at any size. The "16px+ as a graphic element" exemption does not exist: the large-text exemption begins at 24px regular and 3.08 also fails the 3:1 non-text floor. The footer tagline is **Nude**, not Olive. |
| `text-accent` Deep Olive | `surface-inverse` Anthracite | **1.75** | Never. The `.mc-on-dark` scope rewrites `--mc-text-accent` to Nude so a component written once is correct on both grounds. |
| `text-feedback-error` | `surface-inverse` Anthracite | **1.57** | Never. Fails text and the 3:1 non-text floor. **Consequence: no form may sit on a dark band anywhere in the product.** If a validation error must ever surface on dark, it is Nude text + a 2px Nude inline-start rule + the word spelled out — no colour at all. |
| Anthracite at 70% opacity | Nude | **4.28** | Fails. **Opacity is banned for text system-wide.** Every "Anthracite 70%" in earlier documents is replaced by the solid token `--mc-text-secondary` (#606161, 4.98). |
| Anthracite at 60% opacity | Nude | 3.31 | Fails badly. Inactive language-switcher segments use `text-secondary`. |
| `text-disabled` (Anthracite 38%) | Nude | **2.01** | Fails by design. Never the only signal — `aria-disabled`, a reduced border and no pointer cursor accompany it always. |
| `text-secondary` | anything, below 14px | — | Not permitted. 4.98 has an 8% margin; below 14px that margin is a rendering difference, not a design one. |
| Ivory | Ivory | 1.0 | A floating layer never opens on its own light. `--mc-surface-float` takes the opposite light of the band beneath it. |

### 4.3 How the list is enforced — three independent mechanisms

1. **Scope rewriting.** `.mc-on-dark` reassigns `--mc-text-accent`,
   `--mc-border-accent` and the button tokens, so a component written once works
   on both grounds without the developer knowing Deep Olive is banned on
   Anthracite.
2. **`stylelint-mc-contrast`** (ships in `tokens/stylelint-mc-contrast/`) fails
   the build on any pair not in §4.1, and additionally on any rule that sets a
   `color` on an element whose computed background resolves to
   `--mc-surface-accent-solid`.
3. **`qa/contrast.spec.ts`** — Playwright + axe-core over every route, three
   locales, at 360px and 1280px. Zero serious/critical violations is a merge
   gate.

---

## 5. Layout, spacing, radii, motion, focus, hit areas

### 5.1 Breakpoints and grid — one set, owner-ruled

| Name | Min width | Columns | Gutter | Page margin | What changes here |
|---|---|---|---|---|---|
| `base` | **360** | 4 | 16 | 20 | **QA floor.** Older diaspora Android. Design frames may be drawn at 375, but a 360 pass is a merge gate. |
| `sm` | **600** | 8 | 24 | 40 | Tariff cards go 2-up; one-off band goes 2-up |
| `md` | **900** | 8 | 24 | 40 | Desktop nav expands; drawer disappears; header 72px |
| `lg` | **1200** | 12 | 24 | auto, container max 1200 | The `VerificationRail` becomes a right column |
| `xl` | **1440** | 12 | 32 | auto | More air. **No new layout.** |

- Media queries are **min-width only**. Two documented exceptions are permitted
  and only two: hiding the desktop nav, and the calculator's stacked-slider
  layout.
- Container: `width:100%; max-width: var(--mc-layout-container-max);
  margin-inline: auto; padding-inline: var(--mc-layout-margin);`
- Narrow container `760px` for legal pages, About, the report body text and the
  crew note.
- Figma `4 Layout` variable collection has exactly three modes: **360 / 900 /
  1440**.
- 360 is a QA gate, not a second design width. Every character budget, every
  fold calculation and every "above the fold" claim in this system is computed
  against **360 × 640**.

### 5.2 Spacing

4px base unit, expressed in rem so browser zoom and the audience's text-size
setting work. Steps: `0 · 2 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 ·
80 · 96 · 120 · 160 · 200`.

| Use | Value |
|---|---|
| Inside a control (icon ↔ label) | 8 |
| Label ↔ field, field ↔ help text | 8 |
| Between form rows | 20 |
| Card padding | 20 base / 24 `sm`+ / 32 for feature cards |
| Between cards in a band | 16 base / 24 `sm`+ |
| Between blocks inside a section | 24 base / 32 `md`+ |
| Between sections | `--mc-layout-section-block` = `clamp(3rem, 2rem + 5vw, 7.5rem)` |
| Page block-end padding wherever `MobileActionBar` can appear | 88 |
| Adjacent touch targets | ≥8 clear space |

### 5.3 Radii — three values, and the two that were deleted

| Token | Value | Applies to |
|---|---|---|
| `--mc-radius-0` | `0` | bands, photographs, the report sheet, dividers, the plot diagram, the verification rail, tables |
| `--mc-radius-sm` | **`2px`** | buttons, inputs, cards, tariff cards, badges, modals, sheets, toasts, menus, chips |
| `--mc-radius-full` | `9999px` | slider thumb, avatar disc, the petal list bullet |

`xs`, `sm`(6), `md`(10), `lg`(14), `xl`(20) and `2xl`(28) are **deleted from the
token file, not left unused** — an unused token gets used. There is no 4px and
no 8px radius in this system.

**Consequence, and it is deliberate:** the mobile bottom sheet no longer reads
as a sheet by its corners. It keeps the 36×4 drag handle and gains a 1px
`--mc-border-default` block-start rule instead. Raising the sheet's block-start
corners to 8px as a single documented exception is a **designer** decision and
sits in `OPEN-ITEMS.md`; until then the default is 2px.

### 5.4 Borders and elevation

- Border widths: `0 / 1 / 2 / 3`. **There is no 1.5px.** 1px at rest, 2px when
  selected or in error, 3px only for the inline-start rule on a panel.
- Every raised object on a light ground carries a **1px
  `--mc-border-default`** hairline. Nude and Ivory differ by only 1.1 in
  contrast; without the rule the step reads as a printing error.
- **Elevation is a ground change plus a hairline.** `--mc-elevation-overlay` is
  the only shadow in the system and may be referenced by exactly five
  components: `Modal`, `Drawer`, `BottomSheet`, `Lightbox`, `Toast`. Nothing
  else. No card shadow, no hover lift, no header shadow.
- The header's bottom rule is **permanent at every width**, not
  scroll-triggered. There is no `backdrop-filter` anywhere — three scripts, old
  Android, and it buys nothing over a solid Ivory bar.
- **Floating layers** (`Select`/`Combobox` menus, popovers, toasts) take
  `--mc-surface-float`, which resolves to the opposite light of the band beneath
  them, plus a 1px `--mc-border-strong` outline plus `--mc-elevation-overlay`.

### 5.5 Motion — six permitted behaviours, and the forbidden list

| Where | What | Duration / curve |
|---|---|---|
| Buttons, links, chips | background / border / underline colour change | `--mc-motion-hover` (140ms standard) |
| Section entrance | opacity 0→1 with `translateY(8px→0)`, once, staggered 60ms, max 3 items per section | `--mc-motion-enter` (220ms decelerate) |
| Accordion, disclosure | height + opacity | `--mc-motion-expand` (220ms standard) |
| Slider | track fill and thumb follow the pointer | 120ms linear |
| Overlay enter / exit | sheet `translateY(100%→0)`; dialog opacity + `translateY(8px→0)`; scrim fade | enter / exit |
| Images | fade in on decode | 200ms linear. **No skeleton shimmer.** |

**Loading indicator:** a 2px `--mc-text-accent` arc, 24px, 900ms linear
rotation. It is **not** a brand element. The five-petal glyph does not rotate —
rotation of the mark is a forbidden logo use, and a spinning brand mark on a
page about a grave is wrong on tone as well as on governance. Under reduced
motion the arc is static and the accompanying word ("Loading", "Sending") does
the work.

**Forbidden, explicitly and completely:** parallax of any kind; count-up or
rolling numerals anywhere, including the calculator total; auto-advancing
carousels; hover-zoom or Ken Burns on any photograph; scroll-jacking or pinned
scroll sequences; a rotating, blooming or pulsing medallion; falling petals;
typewriter text; a before/after wipe or drag-slider; any transition on the
Family Circle avatars; skeleton shimmer; any `transform` on a card or a button;
and **any animation whatsoever on the sample report, on a bad-news screen, or on
a guest report view**.

No spring physics anywhere. This product is opened to look at a photograph of a
grave. Motion confirms; it never entertains.

### 5.6 Focus

- `:focus-visible` only, never `:focus` — a mouse user must not see rings.
- 2px ring, 2px offset, `--mc-border-focus` (Deep Olive), `--mc-radius-sm`.
- On a Deep Olive fill the ring inverts: inner Ivory at −3px offset plus a 4px
  `--mc-alpha-deepolive-16` halo (written out in §3).
- Inside `.mc-on-dark` the ring is Nude.
- **The ring is never removed**, including on the language switcher, the
  calculator sliders, the gallery thumbnails and the map-link.
- Focus order follows the DOM. **No `tabindex` above 0 anywhere in the
  codebase.** Where visual order differs from reading order (the tariff band at
  `md`+, the calculator result at `lg`), the DOM order is the reading order and
  CSS reorders.
- On modal open, focus moves to the dialog; on close it returns to the invoker.
  Focus is trapped while open.

### 5.7 Hit areas

- Every interactive element has a hit area of **≥44×44 CSS px**, even where the
  visual is smaller, via `.mc-hit-44` (§3 — the corrected rule; the previous
  `inset: 50% 50% 50% 50%` version silently produced a zero-size box and the
  44×44 area did not exist).
- Applies to at minimum: gallery thumbnails, close buttons, the language
  switcher segments, calculator slider handles and stepper buttons, visit-list
  row actions, share-sheet channel buttons, the header call and menu buttons,
  the petal-bullet disclosure toggles.
- Adjacent targets keep ≥8px of clear space.
- Buttons are 48px tall on mobile and 44px from `lg`; inputs the same.
- **Nothing is hover-only.** Every hover affordance has a persistent visible
  equivalent, and touch and pointer are both supported on every control.

### 5.8 Non-negotiable responsive rules

- Design and QA at **360px**.
- Anything below `sm` (600) is **one column**, including the gallery.
- Tables do not exist below `sm`. The visit list becomes a stack of
  `VisitListRow`s. **`PermissionMatrix` is the single permitted exception** and
  it carries a frozen capability column, a scroll-fade affordance and a
  screen-reader-equivalent definition list.
- `dvh`, never `vh`, for anything full-height.
- Images always carry intrinsic `width`/`height`. CLS budget **0.05**.
- LCP ≤ **2.5s** on a throttled 4G profile at 360px, on Home, in all three
  locales.
- 200% zoom at 360px produces no horizontal scroll on any route.
- **Only one fixed bar may occupy the block-end at a time.** `MobileActionBar`
  is suppressed while the calculator result bar is mounted, and both are
  suppressed while any form field has focus.

---

## 6. Typography

### 6.1 The scale

| Role | Face | Size (360 → 1440) | Line height | Tracking | Weight | Used for |
|---|---|---|---|---|---|---|
| `display-1` | display | 32 → 56 | 1.08 | −0.01em | 400 | Hero H1 only |
| `display-2` | display | 28 → 44 | 1.12 | −0.005em | 400 | Page H1 on Pricing, Sample report, Family Circle |
| `heading-1` | display | 26 → 36 | 1.18 | 0 | 400 | Section headings |
| `heading-2` | display | **24** → 28 | 1.24 | 0 | 400 | Sub-section headings, tariff product names, modal titles |
| `heading-3` | **text** | 18 → 20 | 1.35 | 0 | 600 | Card titles, block headings inside a report |
| `body-lg` | text | 17 → 19 | 1.6 | 0 | 400 | Report body, legal pages, About — the three long-form surfaces |
| `body` | text | **16 → 17** | 1.6 | 0 | 400 | Everything else. **Every input.** |
| `body-sm` | text | 15 | 1.55 | 0 | 400 | Dense portal tables, tariff descriptions, footer links |
| `label` | text | 15 | 1.4 | 0.01em | 600 | Form labels, button labels |
| `caption` | text | 14 | 1.45 | 0.01em | 400 | Helper text, gallery captions, legal small print |
| `rail` | text | **14** | 1.4 | 0.06em | 600 | The verification rail, report metadata, GPS coordinates label/value pairs |
| `overline` | text | **13** | 1.3 | 0.12em | 600, uppercase | Decorative section eyebrows only |
| `price` | display | 28 → 40 | 1.0 | −0.01em | 400 | The amount only |
| `numeric` | mono | 14 | 1.5 | 0.02em | 400 | Coordinates, invoice numbers, payment references, share tokens |

### 6.2 The floors, and why each one is where it is

- **16px** is the body and input floor. Below 16, iOS zooms the viewport on
  focus.
- **14px** is the informational floor. Anything a reader must understand —
  captions, helper text, legal text, and every value in the verification rail —
  is at least 14px. The audience is 40–60 and reads on a phone at night.
- **13px** is the absolute floor of the system, permitted **only** for
  `overline`: uppercase, tracked, 600 weight, decorative, never data. Nothing in
  the product — including the tagline, including print, including the PDF — is
  smaller than 13px.
- **`rail` is 14px, not 11 or 12.** It carries the actual proof: date, cemetery,
  plot, crew, coordinates. It was the least legible type in the system carrying
  the most important content in the product. Owner-ruled.
- **Gloock is never set below 24px.** Its hairlines break up. `heading-2`'s
  clamp minimum is therefore 24px, and any heading that would resolve below 24px
  is set in the **text face at 600** instead — which is exactly what `heading-3`
  is.
- `text-secondary` is permitted at ≥14px only, and is **never** used for a rail
  value or any other proof datum. Proof is `text-primary`.

### 6.3 Script rules

- `overline` and `rail` **labels** are uppercase in Latin and Cyrillic and
  **sentence case in Armenian** — Armenian uppercase reads as shouting. This is
  a token-level `:lang(hy)` branch, not a developer judgement.
- **Rail and badge *values* are never uppercase in any script.**
- Headings use `text-wrap: balance`; body uses `text-wrap: pretty`.
- Armenian and Russian get `hyphens: auto` with `lang` correctly set on
  `<html>`; English does not — hyphenation reads cheap in an editorial layout.
- `font-variant-numeric: tabular-nums` on every price, date, coordinate,
  counter and calculator output, so numbers do not jitter.

### 6.4 The two type problems — every claim marked, and the rule that makes the build safe either way

This work was done without network access. **Every statement anyone has made
about what a font file contains is UNVERIFIED**, including statements made
confidently in round one. They are recorded in `brand/FONTS.md` with this exact
label and are resolved by a build-time test, not by anybody's memory.

| Claim | Asserted by | Status |
|---|---|---|
| **Cabin contains ֏ (U+058F), the dram sign** | `DECISIONS.md §5` asks; nobody answered | **UNVERIFIED.** If absent, every price on the site breaks. |
| **Gloock does not contain ֏** | two reviewers, independently | **UNVERIFIED** but treated as true — the fallback below costs nothing if it is false. |
| Gloock covers Latin + Latin-ext only | round one | **UNVERIFIED** |
| Gloock has no Cyrillic | round one | **UNVERIFIED** |
| Gloock has no Armenian | brief + two reviewers | **UNVERIFIED** (very likely true, still untested) |
| Gloock has tabular figures | assumed by every price spec | **UNVERIFIED** |
| Cabin's Cyrillic is adequate | round one | **UNVERIFIED** |
| Cabin has no Armenian | brief | **UNVERIFIED** |
| Noto Sans Armenian ships 400 and 600 | round one | **UNVERIFIED** |

**The five rules that make the build correct whichever way each claim resolves.**

**R1 — The dram sign is bound to its own face, first in every stack.**
`@font-face { font-family:"MC Dram"; src:url("/fonts/noto-sans-armenian-400.woff2");
unicode-range: U+058F; }` and `"MC Dram"` is the **first** family in
`--mc-font-display`, `--mc-font-text` and `--mc-font-currency`. Because the
`unicode-range` is a single codepoint, it affects nothing else. If Cabin turns
out to have ֏, the glyph is simply supplied by Noto instead and nobody can tell.
If Cabin does not, prices still render. This satisfies `DECISIONS.md §5`'s
requirement for "a fallback face for the currency glyph only, stated in the type
spec".

**R2 — The price is never one typeface's problem.** The **amount** may be set in
the display face; the unit **`֏ AMD` is always set in the text face**, at
`type.body`, on its own line beneath the amount (`.mc-price__unit`). The word
`AMD` is a bank requirement and is printed next to the symbol every time, so
even a total glyph failure leaves the price legible and legally sufficient.

**R3 — Every `@font-face` declares an explicit `unicode-range`, and every stack
terminates in a generic family.** A codepoint outside a declared range is never
requested from that file, so a missing glyph falls to the next family and
**never renders as tofu**. No stack can dead-end.

**R4 — One display face is the target; two is the maximum; three is refused.**
The system does **not** split the display face by script. Until a single face
covering Latin + Cyrillic + Armenian is chosen (`OPEN-ITEMS` #6, designer +
owner), `hy` and `ru` headings fall back to the **text face at 600**, never to a
second serif. A heading in the text face reads as a deliberate system; a heading
in a different serif reads as a broken font, and a mixed-script line — an
Armenian name inside an English sentence, which happens constantly here — would
render two competing serifs on one line. **This does not block the English
build.** If a single covering face proves not to exist for free, the maximum
permitted split is two: Gloock for Latin (+ Cyrillic if it has it) and one
Armenian companion chosen for a matching axis.

**R5 — `qa/glyphs.spec.ts` turns every unverified claim into a build failure.**
It runs in CI over the actual shipped `woff2` files with `fontkit` and asserts,
per locale stack:

- U+058F present in the family bound to `--mc-font-currency`;
- U+0531–U+058A and U+FB13–FB17 present in the `hy` stack;
- U+0400–U+04FF present in the `ru` stack;
- U+0030–U+0039 present, and tabular figures available, in whichever family
  sets prices — **if the display face has no tabular figures,
  `--mc-type-price-font` falls back to the text face at 600. One token change,
  no component edits.**
- total per-locale font weight ≤ **180 KB**.

A locale does not ship until its assertion passes. Nothing in this type spec
depends on anyone's recollection.

**R6 — The substitution label appears on every artefact.** *"Cabin is used as a
free substitute for Gill Sans (commercial Monotype, unlicensed for web). It is
not the brand text face."* — in `brand/FONTS.md`, in the `tokens.json`
`$description`, as a comment in the generated CSS, on Figma page
`01 · Foundations`, and in the footer of every exported spec PDF.

**Webfont loading:** fonts are **self-hosted**, never `fonts.googleapis.com` —
part of the audience is in Russia, where Google Fonts is unreliable, and the
bank's review disliked third-party requests. `font-display: swap` with
`size-adjust` / `ascent-override` declared on the fallback faces so the swap
does not break the 0.05 CLS budget. Preload only the two faces the current
locale actually uses.

---

## 7. Component specifications

**52 components.** 18 were specified in round one; 34 were identified as missing
in round two and are specified here for the first time. Each ships as
`components/SPEC-<name>.md` containing the block below verbatim plus a markup
skeleton and a Figma node id.

### 7.0 Rules common to every component

1. **Five states or it is not done:** `default · loading · empty · error ·
   success`. A spec with no empty state is rejected in review. Where a state is
   genuinely impossible, the spec says so in one sentence.
2. Interactive states are a closed set: `default hover active focus-visible
   disabled loading selected error`.
3. **No literal user-facing text in any component.** Copy comes from
   `content/strings.<locale>.json` by key; `lint:no-hardcoded-strings` fails the
   build.
4. **No numbers in copy.** Prices come from the typed `content/products.json`;
   strings carry `{price}` placeholders. A price cannot drift between the
   pricing page, the calculator, the portal and the invoice.
5. Every icon-only control carries an `aria-label` sourced from the string file.
6. **Colour is never the only carrier of meaning.** Report status is a glyph
   plus a word; the leading tariff is a border plus a badge with words; a form
   error is a border plus a glyph plus a sentence.
7. Every component must survive the Storybook **pseudo-locale** (+30% length,
   accented) before it is accepted.
8. **Buttons must survive two lines**, label centred. At `hy` +25%, a 22-character
   label is 27–28 characters. Nothing ellipsises a button label.
9. No `transform` on any card or button. No shadow except the five overlay
   components.

---

### 7.1 Form and control primitives

#### SPEC-Button

| Property | sm | **md (default)** | lg |
|---|---|---|---|
| Min height, mobile / ≥1200 | 40 / 36 | **48 / 44** | 56 / 52 |
| Padding inline | 16 | 24 | 32 |
| Font | `label` 15 | `label` 15 | `body` 16 |
| Icon | 16 | 20 | 20 |
| Gap icon ↔ label | 8 | 8 | 12 |
| Radius | `radius-sm` 2 | 2 | 2 |
| Hit area | 44×44 minimum in every size | | |

| Variant | default | hover | active | focus-visible | disabled | loading |
|---|---|---|---|---|---|---|
| **primary** | bg `olive-700`, fg Ivory (6.01) | bg `olive-800` | bg `olive-900` | inner Ivory ring + `deepolive-16` halo | bg `anthracite-12`, fg `text-disabled`, `cursor:default`, `aria-disabled` | 24px arc replaces the icon, label stays, width locked, `aria-busy="true"` |
| **secondary** | transparent, 1px `border-accent`, fg `text-accent` | bg `deepolive-08` | bg `deepolive-16` | standard ring | border `anthracite-12`, fg `text-disabled` | as primary |
| **tertiary** (text link) | fg `text-accent`, 1px underline at 3px offset | fg `link-hover`, underline 2px | fg `olive-900` | standard ring | fg `text-disabled`, no underline | — |
| **primary-inverse** (`.mc-on-dark`) | bg Nude, fg Anthracite (9.61) | bg `nude-400` | bg `ivory-400` | Nude ring, offset 2 | bg `ivory-12`, fg `ivory-40` | as primary |
| **secondary-inverse** | transparent, 1px `ivory-40`, fg Nude | bg `ivory-12` | bg `ivory-24` | Nude ring | — | — |

- **There is no `danger` button variant.** An error is never an action.
  Cancelling a subscription is a `secondary` button; the destructive
  confirmation inside the flow is a `secondary` button with an explicit label.
- **Never two primary buttons in one viewport section.**
- Motion: `transition: background-color var(--mc-motion-hover), border-color
  var(--mc-motion-hover)`. **No transform, no shadow change.**
- Full-width `.mc-button--block` below `sm` for every form submit and every
  tariff card CTA.
- Labels: `Request a consultation` (22) on every button site-wide except the
  `MobileActionBar`, which carries `Free consultation` (17). `Pay online` is
  always `secondary` until card acquiring is live.

#### SPEC-Input (text · email · textarea · phone)

| Property | Value |
|---|---|
| Min height | 48 mobile / 44 ≥1200; textarea min 120 |
| Padding | 12 block / 16 inline |
| Radius | 2 |
| Border | 1px `input-border` → hover `anthracite-38` → focus **2px inset** `border-focus` (`box-shadow: inset 0 0 0 2px`, so height never jumps) |
| Background | `surface-raised` |
| Font | `body` 16 — 16px is the iOS no-zoom floor |
| Label | `label` 15, **always visible above the field**, gap 8, `text-primary`. No placeholder-as-label: the audience is 40–60 and half the fields are in a second language. |
| Help text | `caption` 14, gap 8 below, `text-secondary` |
| Error text | `caption` 14, `text-feedback-error`, with a **16px error glyph**, gap 8 |
| Required marker | the word (localised) in the label plus an asterisk in `text-feedback-error` — never an asterisk alone |

States: `default · hover · focus · filled · disabled` (bg `surface-sunken`, fg
`text-disabled`, border `anthracite-12`) `· readonly` (no border, transparent
bg) `· error` (2px inset `border-feedback-error`, `aria-invalid="true"`, message
linked by `aria-describedby`) `· validating` (24px arc inline-end, no colour
change).

There is **no `success` state on an input.** A field that validated is simply
not in error. (The one exception the system allows — an async uniqueness check
on an invitee email — renders a `text-accent` check glyph and the word, not a
colour ramp.)

**Validation timing is a system rule, not a developer choice:** validate on
blur, never on keystroke; re-validate on keystroke only after the field has
already errored. Errors appear below the field, never as a tooltip, never as a
toast.

**Phone field.** `type="tel" inputmode="tel" autocomplete="tel"`.
`CountrySelect` on the inline-start. Accepts and preserves `+1 818 555 0134`,
`+33 6 12 34 56 78`, `+374 93 154 108`, `0093154108`. Stores E.164. **Never
rejects on format before submit.**

Validation strings that must exist (from `strings.en.json`): missing name ·
missing contact · "This does not look like a phone number or an email address."
+ "Please check the number and try again." · missing country code · missing
cemetery · missing consent · duplicate invitee · file too large · wrong file
type · out-of-range calculator entry · expired invitation · expired reset link ·
session expired · locked out.
**Never, in any language:** `Oops`, `Something went wrong`, `Error`, `Invalid`,
`Failed`, `Required field`, any emoji, any exclamation mark.

#### SPEC-NumberField *(new)*

Paired with **every** slider — sliders alone are unusable for a 55-year-old on a
phone. 48 tall, 96 wide, `numeric` type, tabular. Stepper buttons `−` / `+` at
**44×44** flanking the field. `role="spinbutton"` with `aria-valuemin`,
`aria-valuemax`, `aria-valuenow`, `aria-valuetext` = the formatted value with
its unit. Out-of-range entry clamps to the ceiling and shows a **neutral**
sentence, not an error — passing 100 m² is a normal outcome and a route to
Inspection.

#### SPEC-CountrySelect *(new)*

Dial code and ISO code as **text** — `+374 AM` — never a flag alone; flags are
ambiguous for diaspora holders of two passports. Searchable in all three
scripts. Defaults by IP with a **visible, changeable** value; never locked,
never re-guessed after the user has changed it. 88px wide, same box metrics as
the input it precedes.

#### SPEC-Combobox *(new)*

Cemetery / city: free text with suggestions, **free entry always accepted**.
`role="combobox" aria-expanded aria-controls aria-activedescendant`. Menu takes
`--mc-surface-float`. This is a distinct component from `Select`, which is a
closed listbox and cannot express free entry.

#### SPEC-Select

Native `<select>` at `base`/`sm` (the mobile picker beats anything we build);
custom listbox from `md`.

| Property | Value |
|---|---|
| Trigger | identical box metrics to `Input` |
| Chevron | 16px, `text-secondary`, inline-end 16, rotates 180° over `motion.hover` |
| Menu | `surface-float`, radius 2, 1px `border-strong`, `elevation-overlay`, max-height 320, offset 4, min-width = trigger |
| Option | min-height 44, padding 10/16, `body` |
| Option hover | bg `deepolive-08` |
| Option selected | bg `deepolive-16` + 16px check inline-end, `aria-selected="true"` |
| Option focused | 2px inset `border-focus` |
| Group label | `overline`, `text-secondary`, padding 12/16/4, non-selectable |
| Empty | "No matches", `text-secondary`, min-height 44 |

Full ARIA listbox keyboard: ↑↓ Home End, type-ahead on the **localised** label,
Esc closes and returns focus, Enter/Space selects.

#### SPEC-Checkbox

Box 20×20, radius 2, 2px `border-strong`, bg `surface-raised`. Hit area 44×44,
whole row clickable including the label. Checked: bg + border `olive-700`, Ivory
check glyph 12px stroke 2. Indeterminate: 10×2 Ivory bar. Hover: border
`olive-700`. Focus: 2px ring offset 2. Disabled: border `anthracite-20`, bg
`surface-sunken`. Error: 2px `border-feedback-error` (used by the required
consent checkbox). Label `body`, gap 12, aligned to the box's optical centre,
**wraps freely** — Armenian consent copy runs three lines on a phone.

#### SPEC-Radio · SPEC-RadioCard

Identical metrics to `Checkbox` but `radius-full` with an 8px Ivory dot on
`olive-700`. Group is `role="radiogroup"` with a `<legend>`; arrow keys move
selection, Tab enters and leaves the group.
**RadioCard:** the whole card is the control — 1px `border-default` → selected
2px `border-accent` + bg `deepolive-08`, dot at the block-start inline-end,
min-height 96.

#### SPEC-SegmentedControl *(new)*

Used by: the `LanguageSwitcher`, the calculator's mode switch, and the portal's
tier selector. 3 segments, radius 2, 1px `border-default`, each **44×36
minimum with a 44×44 hit area**, `aria-pressed` on each segment. Selected = bg
`surface-accent-strong` + Ivory label (6.01). Inactive = `text-secondary`
(never Anthracite at 60%, which is 3.31).
**`LanguageSwitcher` labels are written in each language's own script —
`ՀԱՅ · ENG · РУС` — never flags, never Latin transliterations.** At `base`–`sm`
it lives pinned at the bottom of the drawer, not in the bar.

#### SPEC-Slider

Track 4 tall, `radius-full`, bg `border-strong`, filled portion
`surface-accent-strong`. Thumb 28×28 circle, bg `surface-raised`, 2px
`border-accent`, **no shadow**; hit area 44×44; focus = 2px ring offset 2 plus a
`deepolive-16` halo. Hover/active scale 1.06 / 0.98 over `motion.hover`. Track
fill follows the drag at 120ms linear. `role="slider"` with `aria-valuetext` set
to the **formatted price**, so a screen-reader user hears the money, not "37".
Tick labels: minimum, the free threshold, maximum only. Threshold marker: a 2px
`border-decorative` vertical rule at 16 m² and at 2 monuments with a `caption`
label "included".

#### SPEC-FileUpload *(new)*

Used by the guarantee re-visit request. Up to **3 photographs, 10 MB each,
HEIC accepted** (a majority-iPhone diaspora audience). Drop zone 1px dashed
`border-strong`, radius 2, min-height 120, plus a 48px `secondary` "Choose
photographs" button — the button is the primary affordance, the drop zone is
not. States: `idle · uploading` (per-file arc + filename + percentage) `·
complete` (filename + `text-accent` check glyph + a 44×44 remove button) `·
too-large` · `wrong-type` · `failed`. The last three are inline field errors in
the error colour with a sentence naming the actual limit.

#### SPEC-Tooltip *(new, tightly restricted)*

**Definitions only:** what a GPS point is, what AMD is, what a full visit is,
what pro-rata means. It may **never** carry a rule, a price, a surcharge or
anything a decision depends on — those are always visible body text. Tap-to-open
on touch, dismissible, never hover-only, `aria-describedby`. Max 140 characters.

#### SPEC-Accordion *(new)*

Home FAQ (first item open), pricing FAQ, legal table of contents, "what each
role can do". Row min-height 56, 1px `border-default` between rows, chevron 20
rotating over `motion.expand`, `aria-expanded` on a real `<button>`, panel
`body`. Height + opacity over 220ms. Missing entirely from the round-one package
though three documents used it.

#### SPEC-Stepper *(new)*

Flow chrome for the cancellation journey. "Step n of 4" in `rail`, a back
control and a forward control **at equal visual weight**, and an escape at equal
weight. `aria-current="step"`.

---

### 7.2 Display and structure primitives

#### SPEC-Badge

| Variant | bg | fg | Ratio | Use |
|---|---|---|---|---|
| `neutral` | `surface-sunken` #E4D8C4 | `text-primary` | 8.51 | counts, plain labels, **"Moved"**, **"Could not reach the plot"** |
| `accent` | `surface-accent-strong` Deep Olive | Ivory | 6.01 | **"Our recommendation"** on the leading tariff |
| `accent-soft` | `surface-accent-wash` Olive 12% | `text-primary` | 8.59 / 9.30 | "GPS confirmed", "Included" |
| `error` | `surface-feedback-error-subtle` | `text-feedback-error` | 5.27 / 5.76 | form-level and payment-failure summaries **only** |
| `inverse` | `alpha-ivory-24` | Nude | — | badges on the dark band |

Metrics: min-height 24, **radius 2**, padding-inline 12 (10 with a leading
icon), `caption` 14 at 600, icon 14, gap 6.
**`badge.label` overflow is `wrap to two lines`, never ellipsis** — an
ellipsised "Our recommendation" is worse than no badge, and sentence-case
Armenian grows it ~25%.
A badge is never interactive; if it needs a click it is a button.
**There is no Olive-fill badge with any label**, at any size. There is no
`warning` badge and no `danger` badge — those names are banned by
`DECISIONS.md §2`; the states they described are `neutral` plus a word.

#### SPEC-Card

| Property | base | `sm`+ |
|---|---|---|
| Padding | 20 | 24 (`card-padding-lg` 32 for feature cards) |
| Radius | 2 | 2 |
| Background | `surface-raised` | |
| Border | 1px `border-default` | |
| Shadow | **none** | |
| Hover (only if the whole card is a link) | border → `border-decorative` + the title gains a 1px underline. **No lift, no shadow.** | |
| Focus-within | standard ring on the card | |

An interactive card exposes **exactly one** link, wrapping the title, with an
`::after` overlay covering the card. Nested links inside a stretched-link card
are forbidden — that is where un-clickable buttons come from.

#### SPEC-DataTable *(new)*

Used by the credit table, the `RefundTable` and the `PermissionMatrix`. Zebra
rules (Nude rows on an Ivory ground), 1px `border-default` rules, tabular
figures, radius 0, header row `label` 15 at 600, cells `body-sm` 15, row
min-height 48. **Does not exist below `sm`** except as `PermissionMatrix`.

#### SPEC-Divider--medallion

The woven-medallion section divider: an Olive centred ornament with a 1px
`border-decorative` rule running to the page margins either side.
**Used at most four times on the home page and nowhere else.**
⚠️ **The artwork does not exist yet** (`OPEN-ITEMS` #13). Until the designer
delivers or ratifies it, the divider renders as a plain 1px
`border-decorative` rule. The component ships with both branches so the swap is
an asset drop, not a code change.

#### SPEC-BulletPetal

The five-petal list glyph: 6px, `surface-accent-solid` Olive, offset 0.6em from
the baseline, `aria-hidden`. Used in feature lists and in the `PlotDiagram` as
the position marker. **It never rotates and never loops** — rotation of the mark
is a forbidden logo use. ⚠️ Artwork owed (`OPEN-ITEMS` #13); until then the
bullet is a 6px `radius-full` Olive disc.

#### SPEC-PullQuote

Display face, `heading-1`, `container-narrow`, a 1px `border-decorative` rule
above. **One per page maximum.** Never over a photograph.

#### SPEC-EmptyState *(new)*

Heading (`heading-3`), body (`body`), **one** action. **The component has no
`illustration` prop and no `icon` prop** — not "we do not use one", but the prop
does not exist, so it cannot be reached for under deadline.

#### SPEC-ErrorPanel *(page- and screen-level)*

Three slots and only three: **what happened · whose fault it is · what to do**,
plus an optional fourth line carrying a phone number. **No icon prop, no
illustration prop, no emoji, no "Oops".** On a light ground it uses
`surface-feedback-error-subtle` with a 3px `border-feedback-error` inline-start
rule and a heading in `text-feedback-error`. **On any screen showing a
photograph of a grave it renders with no colour at all** — the failure there is
ours, not the client's, and it is a sentence, not a validation.

#### SPEC-ErrorPage (404 / 500) *(new)*

Calm `heading-1`, one explanatory sentence, **five real links** (Home, Pricing,
Sample report, Family Circle, Contacts), and a `tel:` line. No joke, no
illustration, no error colour, no error code as a headline.

#### SPEC-Modal · Drawer · BottomSheet

| Property | base | `sm`+ |
|---|---|---|
| Form | Bottom sheet, full width, radius 2 with a 36×4 `border-strong` drag handle and a 1px `border-default` block-start rule, `max-height: 92dvh` | Centred dialog, `max-width: 560` (720 for the share sheet), radius 2 |
| Padding | 24 | 32 |
| Shadow | `elevation-overlay` | `elevation-overlay` |
| Enter | `translateY(100%→0)`, `motion.enter` | opacity 0→1 + `translateY(8px→0)`, `motion.enter` |
| Exit | reverse, `motion.exit` | reverse |
| Scrim | `surface-scrim` (Anthracite 60%), fades over `motion.enter` | same |
| Header | title `heading-2`, close 44×44 inline-end | same |
| Footer | actions stacked, primary first (top) | inline, primary at inline-end |
| Body | scrolls independently; a 1px `border-default` appears under the header once the body is scrolled | same |

`role="dialog" aria-modal="true"`, labelled by the title id, focus moves in on
open and returns to the invoker on close, focus trapped, Esc closes, background
`overflow:hidden` with scroll position preserved. Scrim click closes **except**
on a destructive confirmation, which requires an explicit button.
**Never used for:** errors (inline), success (toast or inline panel), marketing
interruption (there are no interstitials on this site at all).

#### SPEC-Toast

Two variants only: **`neutral` and `error`.** There is no `success` toast and no
`warning` toast — a completed payment, a sent invitation and a moved visit are
all `neutral`, differentiated by their words.

| Property | Value |
|---|---|
| Position | block-end centre on mobile, offset 88 above the `MobileActionBar`; block-start inline-end on desktop, 24 from the edges |
| Width | `min(92vw, 420px)` |
| Padding / radius | 16 / 2 |
| Ground | `surface-float` (the opposite light of the band beneath), 1px `border-strong`, `elevation-overlay`. On the Anthracite band: `surface-inverse-raised` with a Nude label. |
| Rule | 3px inline-start rule: `neutral` → `border-strong`; `error` → `border-feedback-error` |
| Text | title `label` 15; optional body `body-sm` `text-secondary` |
| Action | one `tertiary` button maximum |
| Close | 44×44 |
| Duration | 5000ms; 8000ms with an action; **error toasts never auto-dismiss** |
| Stack | max 3, newest nearest the edge |
| A11y | container `role="status" aria-live="polite"`; error variant `role="alert" aria-live="assertive"` |

**Toasts never carry information the user needs to keep.** A failed payment, a
moved visit or a guarantee-revisit confirmation is a screen or an inline panel.
The only guaranteed toast string in the product is `Link copied.`

#### SPEC-ProgressRail *(new)*

Four dots, horizontal, each labelled. States: `done` (filled `surface-accent-strong`)
· `in-progress` (2px `border-accent` ring, unfilled) · `pending` (1px
`border-strong`). `aria-current="step"` on the in-progress dot. Label max 20
characters, wraps to two lines at 360. Used on the `FirstEntryScreen`.

#### SPEC-StepStrip *(new)*

The numbered 3–4 step strip used by "what a visit is" on Home and by the
How-it-works timeline. Number set in the display face at `heading-2` (≥24px),
title `heading-3`, body `body`. At `md`+ a 1px `border-decorative` rail runs
behind the numbers; below `md` the rail is vertical at the inline-start.

---

### 7.3 Site chrome

#### SPEC-Navigation (site header)

| Property | `base`–`sm` | `md`+ |
|---|---|---|
| Height | **56** | **72** |
| Ground | `surface-raised` **Ivory**, scoped `.mc-on-ivory` | same |
| Bottom rule | **1px `border-default`, permanent at every width** — not scroll-triggered. The Nude/Ivory step is 1.1 and without a rule it reads as a printing error. | same |
| Logo | `mark-mono.svg` **28px** + live text `MemoryCare` at 24px | `mark-mono.svg` **32px** + live text at 24px |
| Nav links | in the drawer | inline, gap 32, `body-sm`, `text-secondary`; hover → `text-primary` with a 1px `border-decorative` underline drawing in from the inline-start over `motion.hover` |
| Active link | `text-primary`, persistent underline, `aria-current="page"` |
| Language switcher | pinned at the bottom of the drawer | `SegmentedControl`, inline |
| CTA | **absent** — it lives in the `MobileActionBar` | `primary` `sm`, `Request a consultation` |
| Call button | 44×44 `tel:` | in the footer and on Contacts |
| Menu button | 44×44, 20×14 hamburger, 2px bars | hidden |
| Drawer | full-height sheet from the inline-end, `min(88vw, 360px)`, `surface-raised`, `elevation-overlay`, scrim, focus trapped, body scroll locked, Esc closes, items 56 tall | — |

**The header logo composition is `mark + live text` at every width**, never the
drawn wordmark:

- The word is set in the display face at a **24px minimum** (the Gloock optical
  floor), never wraps, never becomes `MC` or `MEMORYCARE`.
- Two-colour: `Memory` = `--mc-text-primary`, `Care` = `--mc-text-accent`
  (**Deep Olive**, not Olive — Olive at 24px is 3.42 and unreadable). On the
  Anthracite footer both halves are Nude.
- **Below 360px the mark drops and the word stays.** For a visitor who arrived
  from an English search that returns dementia care, the company name is the one
  thing that may never be dropped.
- The tagline never appears in the header.
- Live text is selectable, translatable, sharp at any DPR and needs no asset.
- The 56px header fits: 28px mark + 2×14 padding = 56; a 44×44 target + 2×6 = 56.

Nav items, max five: `Pricing · How it works · Sample report · Family Circle ·
About`. Contacts is the phone icon and the footer. There is no `History`,
`Mission`, `Values` or `News`.

#### SPEC-MobileActionBar

`base`–`sm` only. Fixed block-end, **64px + `env(safe-area-inset-bottom)`**,
`surface-raised`, 1px `border-default` block-start rule, radius 0.
Contents: one 44×44 `tel:` icon button plus one full-remaining-width `primary`
button labelled **`Free consultation`** (17).
Appears at `scrollY > 320` at every width where it exists.
**Hides while any form field has focus** (it must never cover the keyboard's
target) and **is suppressed entirely** while the calculator result bar is
mounted and on the report and guest-report routes, where `ReportShareBar` owns
that position. Page block-end padding is 88 wherever it can appear.

#### SPEC-Footer

Bank requirement: **contacts in the footer of every page.** Structure is fixed,
not per-page.

| Property | Value |
|---|---|
| Ground | `surface-inverse` Anthracite, scoped `.mc-on-dark` |
| Padding block | 64 base / 80 `md`+ |
| Columns | 1 (`base`) → 2 (`sm`) → 4 (`md`+): Company · Services · Legal · Contact |
| Logo | `lockup-horizontal-tagline-mono.svg`, 32 tall, `currentColor` → Nude |
| Tagline | `HONORING MEMORY, CARING FOR LOVED ONES`, `overline` 13, **Nude** (Olive on Anthracite is 3.08 and fails), tracking 0.12em, **no full stop** |
| Links | `body-sm`, Nude, hover white + underline |
| Contacts | Hayk Manukyan, CBDO — `tel:+37493154108`; Davit Hambardzumyan, CEO — `tel:+37455315323`; `mailto:info@memorycare.am`; `MemoryCare LLC`; legal address; registration number |
| Legal address | rendered as a **visibly marked placeholder** — `[LEGAL ADDRESS — pending]` — never invented, and listed in `OPEN-ITEMS.md` |
| Legal links | Privacy policy · Refund policy · Terms of service · Service limitations — **all four, every page** |
| Payment note | "Card payments are not yet enabled. First subscriptions are settled by bank transfer." Flagged `temporary: true` in the string file. |
| Social | only accounts that exist. **No dead icons**; a network without an account has no icon, not a greyed one. |
| Copyright | `© 2026 MemoryCare LLC`, `caption`, Nude |

---

### 7.4 Pricing

#### SPEC-PricingBand (`--one-off` / `--annual`)

The pricing page has **two bands and no third**:

```
Pricing page
  page H1 · the "one price list" sentence
  PricingFork
  ── Band 1 · One-off services ──  Inspection 20,000  |  Express 65,000     (2 cards)
     credit rule, four bullets, in full, directly beneath the band, always visible
  ── Band 2 · Annual subscriptions ──  Optimal (leading)  |  Maximum        (2 cards)
  PlotCalculator
  Special — ONE RULED LINE beneath the calculator. Not a card. No price.
  GuaranteesBlock → HonestyPanel → PaymentRealityBlock → closing CTA → Footer
```

- Band heading `heading-1`; band eyebrow `overline`.
- **1-up below 600, 2-up from 600.** There is no 3-up tariff grid anywhere in
  the system.
- Prices in the one-off band are set at the **same type size** as the annual
  prices. Shrinking a price is what makes a product read as cheap.
- Express is a real product at 65,000, never a lead-in, and never sits in a row
  with two annual subscriptions.
- The credit block is never a tooltip and never a footnote.

#### SPEC-TariffCard

`variant: "one-off" | "annual"` · `emphasis: "leading" | null`

```
[ Badge--accent  "Our recommendation"   — leading card only, ABOVE the name ]
[ name                    heading-2, display face, ≥24px ]
[ Armenian name           body-sm, text-secondary — first mention only ]
[ one-line description    body-sm, text-secondary, max 2 lines ]
[ ── 1px border-default divider, margin-block 20 ── ]
[ price block ]
      .mc-price__amount   type.price, display face, text-primary, tabular
      .mc-price__unit     "֏ AMD" — text face, type.body, text-secondary, OWN LINE
      period              body-sm, text-secondary, own line: "/ year" | "one-off" | absent
[ CTA button, block ]
[ ── divider ── ]
[ inclusions list — BulletPetal + body-sm, gap 12, row gap 12 ]
[ credit line (one-off cards only)  caption, text-secondary ]
[ footnote  caption, text-secondary, margin-block-start: auto ]
```

| Property | Value |
|---|---|
| Height | **`auto`**, equalised by `display:grid; align-items:stretch` on the band with `min-height:0` on the card. **Never a fixed minimum and never JS** — a hard 480px either wastes 120px in English or overflows in Armenian. |
| Padding | 24 base / 32 `md`+ |
| Radius / border | 2 / 1px `border-default` |
| Leading card | **2px `border-accent` Deep Olive** + `Badge--accent`. No inversion, no height change, no lift. |
| CTA weight | the leading card is the **only** `primary` in its band; Maximum drops to `secondary` |

**How the leading choice is marked — the exact wording is owner-ruled.**
The badge string is **`Our recommendation`**, never `Most chosen`, never
`bestseller`, never `most popular`. With zero paying customers, "most chosen" is
a behavioural claim about client behaviour that has not happened, and it sits in
the same class as "trusted by N families", which this project is removing from
the old site. In Armenian the source is `Առաջատար`.
`badge.label` limits rise to **ref 18 / hy 24 / ru 22, wrap to two lines**.

Hard content rules encoded as TypeScript unions in `tokens.d.ts`, so a wrong
value fails the build:
`period: "year" | "one-off" | null` — **there is no `"month"`.**
`visitType: "full"` — **there is no `"light"` and no `"preventive"`.**
There is no `bestseller` prop; the flag is `emphasis: "leading"` and its badge
string comes from the string file.

Product data, from `content/products.json` and nowhere else:

| Display name | Armenian (first mention only) | Price | Band | Composition |
|---|---|---|---|---|
| **Inspection** | (Զննում) | 20,000 ֏ AMD | one-off | one assessment visit, full written condition record, photo and video, priced list of recommended work. **No cleaning is performed.** |
| **Express** | (Էքսպրես խնամք) | 65,000 ֏ AMD | one-off | one full visit: deep cleaning of the whole plot and every monument. Report, portal access. |
| **Optimal** | (Օպտիմալ խնամք) | 160,000 ֏ AMD / year | annual · **leading** | **4 full visits, one in each season** |
| **Maximum** | (Մաքսիմում խնամք) | 200,000 ֏ AMD / year | annual | **6 full visits** |
| **Special** | (Հատուկ խնամք) | by calculator | **not a card** | larger plot, more monuments, several family plots. Entry is always through Inspection. |

Tiers 1–4 cover a plot up to 16 m² and up to 2 monuments.
⚠️ Only `Զննում` is confirmed in the brief; the other four Armenian forms are
carried from a superseded price list and must be confirmed before the Armenian
build (`OPEN-ITEMS` #14). English name first, Armenian in parentheses on first
mention on the page; thereafter English only.

#### SPEC-PricingFork *(new)*

Two doors at the top of Pricing. Stacked below 600, 2-up from 600. Each door is
a `RadioCard`-shaped link, not a button.

- Heading: `Two ways to start` (17)
- Sub: `Some people want an assessment first. Some already know what they want done. Both routes are below.` (99)
- Door 1: **`I want to know what it needs`** (28) → Inspection
- Door 2: **`I want it looked after`** (22) → the annual band

The original door labels — "No, I haven't seen it in years" — are **rejected and
must not ship**: putting the reader's own absence in their mouth, in the first
person, before they have read a price, is exactly the guilt construction the
brief forbids.

#### SPEC-TrustLadder *(new)*

Three ruled steps, each with a price: **Know** (Inspection, 20,000) → **Do it
once** (Express, 65,000) → **Keep it cared for** (Optimal, 160,000 / year).
1px `border-decorative` rules between steps, radius 0, no cards, no arrows.

#### SPEC-PlotCalculator

Pricing page **only** — never on Home. Two live calculators would double the
maintenance of the one component whose arithmetic can embarrass us and split the
measurement of the highest-value interaction on the site.

| Element | Specification |
|---|---|
| Container | `Card`, `card-padding-lg`, `surface-raised`, max-width 720, centred |
| Sliders | area and monuments, **stacked at every width**, each paired with a `NumberField` |
| Steps | area: 1 m², range 1–100, default 16 · monuments: 1, range 1–10, default 2 |
| Tick labels | minimum, the free threshold (16 m² / 2 monuments), maximum |
| Threshold marker | 2px `border-decorative` vertical rule with a `caption` label "included" |
| Result block | `surface-sunken`, radius 2, padding 20, separated by 24. **Sits immediately below the sliders. It is never pinned to the viewport.** |
| Result content | **Optimal and Maximum shown simultaneously** — one variable, two values; a control that hides one of the two values defeats the block. Express appears as a separate one-off row. |
| Surcharge lines | two annual surcharge lines permanently visible under the sliders; the Express surcharge line lives inside the Express row. **Nothing goes behind an info icon.** |
| Total | `type.price`, tabular. **Updates instantly. No count-up, ever, under any motion preference.** A price that rolls like a slot machine is the wrong register for this purchase and is the one animation a 55-year-old reads as a trick. |
| Live region | the total is `aria-live="polite" aria-atomic="true"`, announced on pointer release |
| Over-ceiling | above 100 m² or 10 monuments the result block swaps to a neutral panel: an explanatory sentence, a `primary` CTA to the consultation and a `secondary` CTA to Inspection. Sliders **clamp**; they never disable. **This is not an error state and carries no error colour.** |
| Layout | result below the sliders at `base`–`md`, alongside at `lg` (7/5 columns) |

Arithmetic — in the spec, unit-tested, never in anyone's head:

```
annual_total  = base + max(0, area − 16) × 10 000  + max(0, monuments − 2) × 30 000
express_total = 65 000 + max(0, area − 16) × 2 500 + max(0, monuments − 2) × 7 500
```

Currency formatting is a shared utility: grouped with a non-breaking thin space
(`160 000 ֏ AMD`), never a comma in `hy`/`ru`. **Both the symbol and the letters
appear, always** — a bank requirement.

**Calculator → form handoff** (a contract, not a component): URL state
`?tier=&area=&monuments=`, hidden fields on the consultation form, and the
configuration **echoed back** in the confirmation — *"You configured: 24 m²,
3 monuments, Optimal — 270,000 ֏ AMD / year."* The caller must see the same
configuration in the lead record, or the "one price list" argument dies on the
first call.

#### The 95,000 ֏ first-year figure — where it appears, and how

Owner-ruled: shown publicly, in the calculator **and** on the pricing page,
framed as the credit mechanic and never as a discount.

**Four placements and no others:** (a) the pricing page, inside the credit block
beneath the one-off band, as a worked example in body type; (b) the calculator,
in Express mode only, as the third result row, recomputed with surcharges; (c)
the portal plot overview after a one-off has been paid, as a dated fact; (d) the
written quote sent after the consultation call.

**Explicitly not:** the hero, the Optimal card, the Express card's price line,
any badge, any meta description, the `MobileActionBar`, or the footer.

Six rules, all enforced by `lint:strings` and `qa/prices.spec.ts`:

1. **Always show the subtraction, never only the result:** `160,000 − 65,000 =
   95,000 ֏ AMD`. Arithmetic reads as a rule; a bare 95,000 reads as a price
   somebody set for you.
2. **Always name the mechanism in the same sentence** — an amount already paid
   comes off. The money is transferred, not given away.
3. **Always state the second year in the same sentence** — "and 160,000 ֏ AMD in
   each year after that". This is the guard that converts 95,000 from a price
   into a one-time consequence, and it is what prevents the renewal
   conversation going badly a year later. It is not optional.
4. **Forbidden words near a price:** `save`, `saving`, `discount`, `off` alone,
   `deal`, `offer`, `special`, `only`, `just`, `instead of`, `was`, `now`, `%`.
   A "40% first-year discount" is internal language that must never reach copy,
   a ticket or a brief.
5. **No visual discount grammar:** no `text-decoration: line-through` on any
   price anywhere, ever; no colour on the 95,000, no larger type, no badge, no
   ribbon. It is set in the same type role as the sentence containing it.
6. **Full currency form every time:** `95,000 ֏ AMD`.

What must remain true elsewhere or the figure devalues the 160,000:
160,000 is the **only** number on the Optimal card; the calculator's default
state is subscription mode showing 160,000; no screen shows 95,000 and 160,000
as two options of equal weight; Express's headline price stays 65,000; the
portal plan card shows `160,000 ֏ AMD / year · renews {date}` from day one.

Credit rules, from `products.json`:

- Window **60 days** from paying for the one-off. (The 30-day figure in the old
  repo table is stale and must never be used.)
- **One** credit only — either Inspection or Express, never both; if the client
  paid for both, the larger is credited.
- It fires **only at the moment the annual subscription is signed**. There is no
  credit between one-off products: an Inspection is never credited into an
  Express.
- **The credit is attached to the plot, not the client.** One credit, one plot,
  once. The object model is the plot, Special explicitly allows several family
  plots, and a credit that floats between plots is unarguable to implement and
  easy to abuse.
- **There is no discounted repeat Express.** The price is always 65,000.

#### SPEC-CreditCountdown *(new)* — a dated fact, not a timer

"Your 65,000 ֏ AMD is credited toward an annual subscription until
{credit_end_date}." `body` type on `surface-sunken`, radius 2.
**No timer, no counting number, no colour change as the date approaches, no
second reminder, no scarcity styling and above all no error colour.** That
register would end this brand. When the window closes the block is replaced by a
single neutral sentence stating the current prices.

#### SPEC-GuaranteesBlock *(new)*

One component, four surfaces: Home (immediately after How it works, before the
closing CTA), Pricing (beneath the annual band, above the calculator), its own
page `/en/guarantees/`, and the portal visit list as a permanent link.
Three items, each with a **name, a number and a remedy**:

- `Free repeat visit in 7 days` (27) — "Tell us within seven days of a report
  and we come back and redo the work at our cost." (85)
- `Damage to the plot` — "If we damage a monument or the plot, we repair or
  replace it at our cost." (73)
- `Pro-rata refund` — "Cancel at any time and we return the visits you have paid
  for and not received, pro rata." (89)

Followed by the honest-limits paragraph and links to all four legal pages.
Guarantees are our entire substitute for reviews; they take the slot
testimonials would have had.

#### SPEC-HonestyPanel *(new)*

"We started in 2026. We have no reviews yet." A bordered panel on
`surface-page`, 1px `border-decorative`, radius 0, set at **`body` size or one
step above — never as small print.** Styling it as a disclaimer inverts its job.
Placed directly under `GuaranteesBlock`.

#### SPEC-PaymentRealityBlock *(new)*

Bank transfer now; card payment when the bank enables it; **no date promised.**
Two `body` paragraphs and a link to `/en/pay/`. No countdown, no "coming soon"
badge.

#### SPEC-TeamBlock *(new)*

Two founders, on Home and on About: name, role, a `tel:` link, a `wa.me` link,
and a 1:1 portrait placeholder. A published founder's mobile number outweighs 72
anonymous reviews and costs nothing.

#### SPEC-ShareThisPage *(new)*

"Send this to your family" as a legitimate secondary conversion on marketing
pages only. WhatsApp · Viber · Copy link. Uses the **marketing** OG asset
(`og-default.png`), never the report OG rule. **Never rendered on a report
route, a guest route or a bad-news screen.**

---

### 7.5 The report — the product itself

#### SPEC-ReportSheet

An **Ivory sheet on the Nude ground**, radius 0, 1px `border-default`, no
shadow. Block order is fixed and is a brand rule, not a layout preference:

| # | Block | Guest sees |
|---|---|---|
| 1 | **Masthead** — mark, "Visit report", plot identity, cemetery | yes |
| 2 | **Confirmation** — date · status · crew · arrival and departure · **`GpsVerification` at the foot of the block** | yes |
| 3 | **Work performed** — ticked list, max 8, first 4 + "show all" on mobile | yes |
| 4 | **Photographs** — group "On arrival", then group "After the work" | yes |
| 5 | **Video** — optional, poster frame, never autoplay | yes |
| 6 | **The crew's note** — the one first-person voice in the product | yes |
| 7 | **Recommended work, with prices** — Owner and Family manager only, on a changed ground under a full-width rule | **removed server-side** |
| 8 | **Documents** — PDF | yes |
| 9 | **Actions** — Share · Order additional work · Request a repeat visit | text link only |
| 10 | **Next visit** | **no** |

- **The report opens with a calm confirmation that the visit happened, not with
  an image.** A report that opens on the clean stone with no reference frame is
  a marketing image, not a record.
- **Photographs are chronological: arrival first, then after.** The
  "first image = the plot after the visit" rule is **struck**. Leading with the
  after-shot is the advertising register the brief forbids.
- **A side-by-side before/after is never the opening image**, and there is no
  drag-slider and no wipe anywhere in the product.
- The crew note sits after the photographs — it reads as commentary on images
  already seen.
- Block 7 never appears in the report **PDF**, in any variant, for any role: the
  PDF is the artefact that circulates in a family chat, and it must be
  price-free like the guest view. One file serves Owner, member and guest.
- The recommended-work framing line: *"Nothing here happens unless you ask for
  it. These are observations, not urgent, unless we say so."*

States: `completed` · `preparing` ("The visit is done. The report is being
prepared.") · `media-partial` ("Some photographs are still uploading. The rest
of the report is complete.") · `failed` · `rescheduled` · `no-access`.
Loading: a `surface-sunken` block at the exact aspect ratio — **no shimmer**.
`<title>` is `Visit report — {date}` **and nothing else**: the plot identity in
a browser tab is visible over a shoulder and in any screen-share.

**Report SLA is 48 hours from the visit** — owner-ruled, printed identically
everywhere it appears. Callback is **within one business day**, with Yerevan
business hours stated next to it so a client in Los Angeles can convert it.
Nobody may soften or sharpen either number locally.

**The name of the deceased is off by default.** A report shows cemetery, sector
and plot. `plot.display_mode ∈ {none, family_name, full_name}` defaults to
**`none`**; it lives on the plot, is worded plainly, is reversible, and turning
it off **also removes the name from previously issued links**. The link is
forwarded into family group chats and to people without accounts, and part of
the audience is in the EU.

#### SPEC-ReportPreview

The cropped Ivory object in the marketing hero. **The part that survives the
fold is the metadata, not the image** — a cropped photograph proves nothing. The
sliver carries the masthead strip (`14 September 2026 · Tokhmakh · Plot 12`) and
the `GPS confirmed` chip. 180px tall at 360, deliberately cropped by the fold.
At `lg` it moves alongside the hero text.

#### SPEC-VerificationRail

02's signature device, and the component every report and visit screen depends
on. Label/value pairs in `type.rail` **at 14px**: date · cemetery · sector ·
plot · crew · arrival · departure · coordinates.

| Width | Behaviour |
|---|---|
| `lg`+ (1200) | right column, `cols 10–12`, 222px, 1px `border-default` inline-start rule, radius 0 |
| `base`–`md` (360–1199) | **a horizontal ruled strip beneath its content**: two rows of label/value pairs, 1px `border-default` rule between rows, values at the inline-end |

- Labels are `text-secondary`, uppercase in Latin/Cyrillic, **sentence case in
  Armenian**. **Values are `text-primary`, tabular, never uppercase in any
  script, and never `text-secondary`** — they are the proof.
- Every field has a defined empty form. **A missing value renders "Pending",
  never a blank cell.**
- `rail.label` max 12 characters, `rail.value` max 18.

#### SPEC-GpsVerification

The umbrella component; its parts are the **GPS chip** (the label), the
**PlotDiagram** (the graphic) and the **map link** (the action).

| Property | Value |
|---|---|
| Frame | 1:1, **120px** at `md`+ / **96px** below, radius 0, 1px `border-decorative`, `surface-page` fill |
| Diagram | a bearing rose of three concentric 1px Olive rules, a cross-hair, and a solid Olive five-petal glyph at 14px at the true offset |
| Coordinates | `type.rail` below the frame, tabular |
| Chip | `Badge--accent-soft`, string `GPS confirmed` |
| Action | `[Show on map]` — a **tertiary text link** that opens the visitor's own map app via a `geo:` / Apple Maps URL |

**We serve no map tiles.** A tile is someone else's brand on our proof, it
carries an attribution licence and a third-party request from a page full of
grave photographs, and it is slow on the connection this audience has. **The
marker is the Olive five-petal glyph, never a red pin** — a red pin is a
delivery app, and after the error-colour ruling red means exactly one thing in
this product.

States: `recorded` · `pending` ("Coordinates pending upload" — never an empty
cell) · `not-recorded`.

#### SPEC-Gallery

| Property | Value |
|---|---|
| **Ratios** | report photograph **4:3 · 1600×1200** · section image 3:2 · 1800×1200 · crew and equipment portrait **1:1 · 1000×1000** · video 16:9 · OG 1.91:1 · 1200×630 |
| Grid | 1-up `base`; 2-up `sm`; 3-up `md`+; gap 8 / 12 / 16 |
| Radius | **0** |
| Caption | below the image, `caption` 14, `text-secondary`; every image is captioned with what it shows and its timestamp. **Never a bar over the photograph.** |
| Loading | `surface-sunken` block at the exact ratio; intrinsic `width`/`height` always present |
| Lightbox | `surface-scrim`, image `max-height: 88dvh`, controls 44×44 on `surface-float`, counter `caption`, Esc closes, arrows navigate, focus trapped, focus returns to the thumbnail |
| Zoom | pinch on touch, double-click on desktop, max 3× |
| Autoplay | **none. Nothing on this site moves on its own.** |

**Photography rules that belong to the system, not to the photographer's
taste:** radius 0, no border, **no black border under any circumstance**, no
vignette, no shadow, no duotone, no olive wash, no grain, no film emulation, no
grayscale conversion, no "before"/"after" text burned into the image.
Natural exposure, neutral white balance, overcast or open shade. Camera at
standing eye height, level; the plot occupies the lower two-thirds. Never a low
heroic angle, never a drone directly over a grave. Crew appear working, hands
and equipment in frame, never posed, never smiling to camera. No flowers
arranged for the photograph, no candles, no crosses composed as graphic
elements. Faces of mourners never appear.
**The before and after frame must be identical** — same standing position, same
focal length, same height. That is the whole evidentiary point, and the crew
gets a marked standing position for it.
**The client's own monument inscription is legible by default** — it is the
proof that we cleaned *their* grave. **Every neighbouring plot's name and
inscription is out of frame or out of focus, without exception.**

**Placeholders until the September shoot.** A `surface-media-placeholder`
rectangle at the exact final ratio, 1px `border-decorative`, one Olive
five-petal glyph at 8% opacity bleeding off the block-end inline-end corner, and
in the block-end inline-start corner, in `caption` `text-secondary`, four facts
on two lines:

```
PLACEHOLDER · 4:3 · 1600×1200
"Condition on arrival — Tokhmakh, section 12" · September shoot
```

**Every placeholder names its ratio, its pixel size, its subject and its
source. A placeholder that does not name all four is not shippable.** No "image
coming soon", no camera icon, no grey box, no lorem.

Files: `photo-3x2-plot-arrival.svg`, `photo-3x2-plot-after.svg`,
`photo-3x2-section.svg`, `portrait-1x1-crew.svg`, `portrait-1x1-founder.svg`,
`video-16x9-report.svg`.

#### SPEC-ComparePair

Two **4:3** frames stacked, with a 1px Nude gutter, headed "Compare", placed
**below** the sequential arrival and after groups. Never the opening image,
never a drag-slider. (A separate 4:5 comparison crop does not exist in this
system.)

#### SPEC-ReportShareBar

The report screen's own fixed block-end bar. 48 tall + safe area,
`surface-raised`, 1px `border-default` block-start rule. **Contains Share and
nothing else.** It replaces `MobileActionBar` on the report and guest-report
routes — there is no consultation CTA anywhere near a photograph of a grave.

#### SPEC-ShareSheet *(new)*

A read-only link field with a Copy button, then WhatsApp · Viber · Email · SMS
channel buttons (44×44 each, 8px apart), then a 1px `border-default` divider,
then **"Link is active · created {date} · Revoke"** with a confirm step. The
revoke affordance lives in the sheet that creates the link — nowhere else will
anyone find it.
Toast on copy: `Link copied.`
Share-link security: **≥128 bits of entropy**, `X-Robots-Tag: noindex, nofollow`
plus a `noindex` meta on the route, revocable from this sheet, non-expiring by
default, dead on subscription cancellation.

**Link preview rule — hard.** The OG image for a shared report is the static
generated asset `brand/og/og-report-share.png`: Anthracite ground, mono light
mark at 96px, the words "Visit report", the date. **A photograph of a burial
never appears in a link preview**, and this is asserted by `qa/meta.spec.ts`,
not by inspection. `og:title = "Visit report — {date}"`.
`og:description = "A record of a MemoryCare visit. Photographs, video and GPS
confirmation."` — **no cemetery, no plot label, no name.** The preview is
rendered by Meta's and Viber's unauthenticated crawlers and is forwarded past
the family more often than the family thinks. The OG ground is Anthracite, never
Nude: a Nude 1200×630 renders as a near-blank card in a dark WhatsApp thread,
and the colour mark's hands vanish on Nude.

#### SPEC-GuestReportLayout *(new)*

A **route**, not a permission flag. `/r/:shareToken/` — short and retypable,
deliberately not under `/portal`, because it is pasted into WhatsApp and read on
a five-inch screen by a seventy-year-old aunt.

Structure: masthead → the report blocks 1–6 and 8 → a one-line foot → one
non-commercial action.
Removed **server-side, not hidden**: prices, recommended-work figures, the
next-visit date, the subscription name, every button, the action bar.
The route's bundle physically cannot import `TariffCard`, `PlotCalculator`,
`Badge--accent`, `MobileActionBar` or any `primary` button — asserted by a
bundle test, not by looking. Selling next to a photograph of a grave cannot
happen by accident if the code cannot express it.
The foot carries: what MemoryCare is, one sentence; who shared it; a `tel:`
link; and an `About MemoryCare` **text link**. **No navigation into the
marketing site** — one tap from a photograph of a grave to a sales bar is the
failure this whole route exists to prevent.
Expired/revoked state: "This link is no longer active. The person who sent it
can share it again. Nothing has been deleted — the report still exists." No
sign-up prompt, no account prompt, no price.

#### SPEC-GuestFeedbackForm *(new)*

The **only** interactive element permitted on `/r/`, reached by a `tertiary`
text link: `Something is not right with this report` (39).
Three fields — name, phone or email, what is wrong — no account, no consent
theatre, no price. Filing it opens a guarantee re-visit against that visit and
notifies the Owner. Support, never sales.
This exists because of the split case the brief calls central: if the mother in
Yerevan opens the report and something is wrong, a dead page forces her to
telephone her son abroad.

---

### 7.6 Portal

#### SPEC-PortalTabBar / SPEC-PortalSidebar *(new)*

Below `md`: a 4-tab bottom bar, **56px + `env(safe-area-inset-bottom)`** —
`Plots · Visits · Family · Account`. From `md`: a 240px sidebar.
Tab labels are words plus glyphs; **a visit is the event and a report is the
record of it, so the tab is `Visits`, never `Reports`.**

#### SPEC-PlotSwitcher *(new)*

In the portal header, rendered **only when the account has more than one plot.**
A `Select` whose options are plot labels; the current plot is
`aria-current="true"`.

#### SPEC-PlotCard *(new)*

The dashboard row: plot identity, cemetery, next visit, a last-report thumbnail
(neutral 3:2 crop), plan name. The whole card is one stretched link. Min-height
88. **A Family member never sees the plan name** (see the permission matrix).

#### SPEC-VisitListRow / SPEC-VisitListGroup *(new)*

A **scheduled** group (1px dashed `border-decorative` inline-start rule) above a
**completed** group (1px solid `border-accent` inline-start rule). Row min-height
72, the entire row is the target, chevron 20 at the inline-end, a status
`Badge--neutral` carrying the **word**. Below `sm` this replaces the table
entirely.

#### SPEC-FirstEntryScreen

The most important empty state in the product: the client has just paid
160,000 ֏ and there is nothing to show. It is a **designed screen**, not a blank
list. Contents, in order: the subscription summary with the price and the
renewal date; a `ProgressRail` of four steps; the scheduled first-visit window
as a month range until it is dated; what will arrive and when (report **within
48 hours** of the visit); the two founders with `tel:` and `wa.me` links; and a
link to the guarantees. **No upsell of any kind on this screen.**

#### SPEC-StatusScreen--rescheduled / --no-access / --revisit

Bad-news screens are **first-class components, not error handling**, and they
get the same design budget as a report. They use the `ReportSheet` shell with a
`Badge--neutral` carrying the word, a plain-language sentence, the new date if
there is one, and one action.
**None of them carries the error colour.** "Could not reach the plot" is not a
fault — it is a report of a visit that happened, **with GPS proof that the crew
was there**, and treating it as a red state contradicts the entire argument for
showing the GPS trace on a failed visit. The `no-access` screen shows the same
`GpsVerification` block as a normal report, with the helper line "This is where
the crew stood. It is how you know they went."
Neither uses a `Toast`, a `Modal` or the generic error panel.
`{obstruction_description}` and `{action_taken}` are operator-selected from
fixed sets — plain, never "unforeseen circumstances".
The screen must state: *"This visit does not come out of your subscription."*

#### SPEC-RoleSelector *(new)*

**Three radio-cards with one-line descriptions — never a dropdown**, because a
dropdown hides the consequence of the choice. Plus plot-scope checkboxes when
the account has more than one plot.
Role descriptions, truncated on the invite screen with the full sentence in an
expandable: *"Family manager — sees every report, can request extra work. Cannot
spend or cancel."* (66)

#### SPEC-PermissionMatrix *(new)*

**The one permitted horizontally scrolling table in the system**, from `sm` up:
frozen capability column, a scroll-fade affordance at the inline-end, and a
screen-reader-equivalent definition list. Below `sm`, and on the public Family
Circle page at every width, it renders as **four stacked role cards, each with a
"can / cannot" list** — a frozen-column scroll table at 360px is unusable for a
55-year-old.

| Capability | Owner | Family manager | Family member | Guest |
|---|:--:|:--:|:--:|:--:|
| View reports (photos, video, GPS) | ✅ | ✅ | ✅ | ✅ single report |
| View the visit schedule | ✅ | ✅ | ✅ | ❌ |
| Download the report PDF | ✅ | ✅ | ✅ | ✅ |
| Share a report by link | ✅ | ✅ | ✅ | ❌ |
| Revoke a share link | ✅ | own links | own links | ❌ |
| See prices anywhere in the portal | ✅ | ✅ | ❌ | ❌ |
| Order a one-off service | ✅ | request → Owner approves | ❌ | ❌ |
| Approve anything that carries a charge | ✅ | ❌ | ❌ | ❌ |
| Request a guarantee repeat visit | ✅ | ✅ | ✅ | ✅ as a message |
| Reschedule a visit | ✅ | ✅ | ❌ | ❌ |
| Change or upgrade the subscription | ✅ | ❌ | ❌ | ❌ |
| Cancel the subscription | ✅ | ❌ | ❌ | ❌ |
| View invoices and payment details | ✅ | ❌ | ❌ | ❌ |
| Invite a family member | ✅ | ✅ Member only | ❌ | ❌ |
| Remove a family member | ✅ | ❌ | ❌ | ❌ |
| Edit plot identity and display mode | ✅ | ✅ | ❌ | ❌ |
| Set the local contact and reminders | ✅ | ✅ | own only | ❌ |
| Transfer ownership | ✅ | ❌ | ❌ | ❌ |

Three rules fall out of the table and must be implemented as such:
**A Family member never sees money** — not the plan name, not the price, not the
renewal date. This is the role for the aunt and the cousins and it is the
default suggested role on the invite screen.
**A Family manager can spend nothing without the Owner** — a manager's order
becomes a decision in the Owner's dashboard. That is what makes it safe to hand
a relative real control.
**Only the Owner can cancel or transfer.** One person owns the money, always.
**No renewal, price, payment or upgrade string may ever be addressed to a Family
member or to a local contact.**

#### SPEC-NotificationMatrix *(new)*

Per-plot event × recipient toggles, plus a **local contact** block (name, phone,
channel: SMS or WhatsApp) with its own explicit third-party consent checkbox —
*"This person has agreed to receive messages from us."* We will be messaging a
seventy-two-year-old who never contacted us; the checkbox is the minimum and it
is not decorative.
The day-before visit reminder is **opt-in** and can be addressed to a different
person.

#### SPEC-AvatarRow

Family Circle: 48px Nude discs, initials in the text face at 600/16 (9.61 on
Nude), 1px `alpha-ivory-40` ring, −12px overlap, the Owner ringed in
`border-decorative` Olive. **No photographs of people and no stock avatars.**
No transition of any kind on these.

#### SPEC-RefundTable *(new)* and the cancellation flow

Cancellation is a four-step `Stepper` flow, completable **without telephoning
us** (a bank requirement as well as a decency one). Before the confirm step the
screen shows the arithmetic as arithmetic, never as a single figure:

```
refund = amount_actually_paid × (visits_not_performed ÷ visits_total)
         rounded UP to the nearest 100 ֏
```

| Row | Example |
|---|---|
| Amount you paid | 95,000 ֏ AMD |
| Visits in your plan | 4 |
| Visits completed | 1 |
| Visits not performed | 3 |
| Refund | 95,000 × 3 ÷ 4 = 71,250 → **71,300 ֏ AMD** |
| Method | to the account the payment came from |
| Timing | {payment_timing} |

**The base is what the client actually paid, never the list price.** Computing
the same case from 160,000 returns 120,000 and refunds more than we took. This
was the single most expensive defect the review found and it must reach the
lawyer, the refund policy page, the bank submission and the platform.
**The basis is visits, not days** — the client can count visits himself, so the
number is never disputed, and a client who has had one of four visits is never
told they consumed 27% of the year. **There is no cap on the refund**; the
guarantee only sells if it is unconditional.
The `RefundTable` and the `PlotCalculator` share **one** arithmetic module. Two
implementations of the same money rule is how they diverge.

**Past reports stay readable forever, including after cancellation.** Read-only,
no new visits, **no upsell on those screens.** Access to reports about a family
member's grave is not a SaaS feature to switch off.

#### SPEC-AuthScreens *(new)*

Sign in · magic-link interstitial · activation from token · password reset.
**Magic link and a password are offered on the same screen**, both set during
activation: a magic link that lands in a corporate spam filter locks a client
who has just paid 160,000 ֏ out of the product at the worst possible moment.
`Send it again` also offers WhatsApp delivery of the link. Both founders'
numbers appear on the login screen. Strings needed: locked out, session expired,
expired reset link, server error. The label is **`Sign in`**, never `Log in` or
`Client login`.

#### SPEC-BankTransferPanel *(new)* + invoice template

The path the first paying clients actually use, and it was undesigned in every
round-one document. Wire instructions on screen **and** as a PDF invoice
carrying `MemoryCare LLC`, the legal address, the registration number, the AMD
amount and the payment reference the client types into their own bank.
`type.numeric` for the account number and the reference, each with a 44×44 copy
button.
States on `/en/pay/thank-you/` and in the portal: **`Awaiting payment`** —
*"We have not seen it yet. International transfers usually take 2–5 working
days. Nothing is wrong."* — plus a day-3 message from a named human and a day-7
message repeating the bank details. The absence of this screen is where the
first refund request of this company would have come from.

#### Transactional email template

Not a component, but a deliverable nobody owned. **None of this design system
applies inside an email client**: no CSS custom properties, no `clamp()`, no
`dvh`, no reliable webfonts, no `:focus-visible`.

Rules: one column, 600px, table-based, **inline styles with literal hex values
generated from `tokens.json` at build time**, Georgia / Arial fallbacks for the
two brand faces, no background images, one Anthracite header bar with the mono
light lock-up.
**A report notification email never embeds a photograph** — it renders in an
inbox preview pane at someone's work. It carries the date, the plot label per
`display_mode`, and a link.
Owner: the design system engineer, not Igor. This is the artefact the diaspora
client sees before they ever reach the portal.

#### The written quote (PDF)

The artefact of the family decision — "I need to ask my brother" is the
number-one loss cause, and nobody had designed the thing that gets forwarded to
the brother. One page: the plot as described, the plan, the price in AMD with
the arithmetic, the credit if any, the three guarantees, the two named humans
with their numbers, and the payment instructions. **A4**, brand-set, generated
in the client's locale. Same block order and same no-price-in-the-forwardable
rule as the report PDF.

#### The report PDF

**A4.** Same block order as `ReportSheet`. **No prices in any variant, for any
role** — one file serves everyone, because a PDF forwarded by email carries the
same exposure as a shared link. The tagline is set from the print asset. The
dram-sign rule (§6.4 R1–R2) applies here too. Who generates it is Igor's; what
it contains is ours.

---

### 7.7 The hero — the one block whose arithmetic is binding

Hero ground is **Nude**, not Anthracite. The page carries exactly **two**
Anthracite bands: **Family Circle** and the **closing CTA band that runs into
the footer**. A dark hero costs fold height, forces a second header variant and
a colour flash on a slow connection, and spends the page's scarcest asset —
darkness — on the screen where the brief's tone rule is strictest. The report
preview is an **Ivory sheet with a 1px hairline** on the Nude ground, which is
the "paper on stone" idea stated more purely than putting the paper under a lamp.

**The consultation form may never sit on a dark band**, on any page: the error
colour is 1.57 on Anthracite and a validation error there would be invisible.

The fold arithmetic at **360 × 640**, header 56, usable content ≈ 500px:

| Element | Height |
|---|---|
| Overline 13/18 | 18 |
| gap | 12 |
| **H1, 32/38, hard maximum 2 lines** | 76 |
| gap | 16 |
| Standfirst 16/26, 3 lines | 78 |
| gap | 20 |
| `ReportPreview`, cropped by the fold on purpose | 180 |
| gap | 16 |
| Primary CTA, 48 | 48 |
| **Total** | **464 — about 36px spare** |

A three-line H1 costs 38px and pushes the CTA below the fold. Therefore, one
number, everywhere: **hero H1 hard maximum 48 characters English / 58 hy /
55 ru**, and **standfirst 105 characters English.**

Canonical hero H1: **`You will see exactly what was done, and when.`** (44).
"At the grave" is carried by the overline, by the `<title>` and by the report
preview directly beneath — and the disambiguation from dementia care that the
brief requires belongs in the overline, the `<title>` and the meta description,
which is where it is done.

Order at `base`–`sm`: overline → H1 → standfirst → **primary CTA** → cropped
`ReportPreview`. At `lg` the preview moves alongside. **The CTA is never below
the preview on a phone.**
A one-line verification strip in `rail` type sits under the standfirst:
`Date · Cemetery · GPS confirmed`, 24px. Proof before the ask, at no cost to the
fold.
**The logo is never the hero image.** That is the current site's mistake.

### 7.8 Consultation form — the final field set

| Field | Required | Rule |
|---|---|---|
| Name | ✅ | 2–60 characters, any script |
| Phone **or** email, one field | ✅ | international formats, `CountrySelect`, dial code as text |
| Cemetery or city — `Combobox`, free entry accepted | ✅ | it changes the quality of the callback, and that beats the volume cost |
| `Add a note or a family contact` — one disclosure | optional | holds the free-text note **and** the two Yerevan local-contact fields. One tap for the minority who need it, zero cost for everyone else. |
| Consent checkbox | ✅ | **Owner-ruled: it stays.** One line with a link: *"I agree to MemoryCare contacting me about this request."* Part of the audience is resident in the EU and the bank requires a demonstrable lawful basis. It is one line, not a wall of text. |

**Cut, and they stay cut:** preferred-contact-time chips (guessed wrong more
often than right; the callback window is stated instead), and the conditional
local-contact fields as separate visible rows (they live inside the disclosure;
the *data model* still carries three contact records per plot).

Because a required checkbox is the most common silent submit-blocker on a lead
form, and the invalid box is off-screen at 360px: on failed submit an error
summary with `role="alert"` appears at the top of the form, **focus moves to
it**, and each named field links to its own error.

Supporting line under every consultation button: **`No payment now. No account
needed.`** (34). Form heading: `Request a free consultation` (27) — a heading,
not a button, so the 22-character button budget does not apply.

Confirmation copy states the callback window in Yerevan time **and** the
visitor's own local equivalent, offers WhatsApp as the first channel — *"Hayk
will write to you on WhatsApp from +374 93 154 108 first, and call only if you
prefer"* — and echoes the calculator configuration back. An unannounced call
from an unknown +374 number at an odd hour is not answered by a US or French
recipient and is increasingly silenced by the carrier as suspected fraud.

---

## 8. Content limits and copy rules

### 8.1 `content/content-limits.json` — complete

```json
{
  "$comment": "Max grapheme counts per slot. 'ref' is English. hy/ru are the ENFORCED ceilings — Armenian runs 15-25% and Russian 10-20% longer than English for the same meaning. 'overflow: none' means the component has no ellipsis and no clamp: it will break the layout visibly, on purpose, so the copywriter fixes the string rather than the developer hiding it.",

  "nav.item":             { "ref": 16,  "hy": 22,  "ru": 20,  "overflow": "none — shorten the source" },
  "button.label":         { "ref": 22,  "hy": 30,  "ru": 28,  "overflow": "wrap to 2 lines, label centred, button grows" },
  "button.label.bar":     { "ref": 18,  "hy": 24,  "ru": 22,  "overflow": "none — single line, fixed bar" },
  "link.tertiary":        { "ref": 46,  "hy": 58,  "ru": 54,  "overflow": "wrap to 3 lines" },
  "badge.label":          { "ref": 18,  "hy": 24,  "ru": 22,  "overflow": "wrap to 2 lines — NEVER ellipsis" },
  "tariff.name":          { "ref": 14,  "hy": 20,  "ru": 18,  "overflow": "none" },
  "tariff.description":   { "ref": 74,  "hy": 92,  "ru": 88,  "overflow": "clamp 2 lines" },
  "tariff.inclusion":     { "ref": 58,  "hy": 72,  "ru": 68,  "overflow": "wrap, no clamp" },
  "hero.h1":              { "ref": 48,  "hy": 58,  "ru": 55,  "overflow": "none — the fold arithmetic depends on it" },
  "hero.standfirst":      { "ref": 105, "hy": 130, "ru": 122, "overflow": "none" },
  "section.overline":     { "ref": 28,  "hy": 34,  "ru": 32,  "overflow": "wrap" },
  "card.title":           { "ref": 48,  "hy": 60,  "ru": 56,  "overflow": "clamp 2 lines" },
  "form.label":           { "ref": 30,  "hy": 40,  "ru": 36,  "overflow": "wrap" },
  "form.error":           { "ref": 90,  "hy": 110, "ru": 105, "overflow": "wrap" },
  "toast.title":          { "ref": 44,  "hy": 56,  "ru": 52,  "overflow": "clamp 2 lines" },
  "report.status":        { "ref": 24,  "hy": 32,  "ru": 30,  "overflow": "none" },
  "report.crew-note":     { "ref": 320, "hy": 400, "ru": 380, "overflow": "wrap, no clamp", "min": 120 },
  "report.recommendation.item": { "ref": 90, "hy": 112, "ru": 106, "overflow": "wrap" },
  "rail.label":           { "ref": 12,  "hy": 16,  "ru": 15,  "overflow": "none" },
  "rail.value":           { "ref": 18,  "hy": 24,  "ru": 22,  "overflow": "none" },
  "gallery.caption":      { "ref": 80,  "hy": 100, "ru": 95,  "overflow": "clamp 2 lines" },
  "placeholder.caption":  { "ref": 90,  "hy": 110, "ru": 105, "overflow": "wrap" },
  "guarantee.title":      { "ref": 30,  "hy": 38,  "ru": 36,  "overflow": "wrap" },
  "guarantee.body":       { "ref": 110, "hy": 136, "ru": 130, "overflow": "wrap" },
  "credit.rule.bullet":   { "ref": 140, "hy": 175, "ru": 165, "overflow": "wrap" },
  "faq.question":         { "ref": 70,  "hy": 88,  "ru": 82,  "overflow": "wrap" },
  "faq.answer":           { "ref": 420, "hy": 520, "ru": 495, "overflow": "wrap" },
  "role.name":            { "ref": 16,  "hy": 22,  "ru": 20,  "overflow": "none" },
  "role.description":     { "ref": 90,  "hy": 112, "ru": 106, "overflow": "wrap; 66 on the invite screen with the full sentence in an expandable" },
  "legal.paragraph":      { "ref": 600, "hy": 740, "ru": 700, "overflow": "wrap" },
  "email.subject":        { "ref": 52,  "hy": 60,  "ru": 58,  "overflow": "none", "min": 30 },
  "email.preheader":      { "ref": 90,  "hy": 110, "ru": 105, "overflow": "none" },
  "push.title":           { "ref": 40,  "hy": 48,  "ru": 46,  "overflow": "none" },
  "push.body":            { "ref": 110, "hy": 132, "ru": 126, "overflow": "none" },
  "footer.link":          { "ref": 26,  "hy": 34,  "ru": 32,  "overflow": "wrap" },
  "meta.title":           { "ref": 60,  "hy": 60,  "ru": 60,  "overflow": "none — SEO hard limit" },
  "meta.description":     { "ref": 155, "hy": 155, "ru": 155, "overflow": "none — SEO hard limit" }
}
```

Enforcement: (1) `npm run lint:strings` fails the build on any overflow in any
locale; (2) Storybook's **pseudo-locale** toggle renders English at +30% length
with accents, and every component must survive it before acceptance — this
catches layout breakage before a translation exists; (3) where `overflow` is
`none`, the component has no ellipsis and no clamp, so it breaks visibly.

### 8.2 Copy rules the system enforces rather than requests

- **String files are the only source of copy.** No literal user-facing text in
  any component. `lint:no-hardcoded-strings` is a merge gate.
- **Numbers are never in copy.** Prices come from the typed
  `content/products.json`; strings carry `{price}` placeholders.
  `qa/prices.spec.ts` asserts that every rendered price traces to
  `products.json`.
- **English source strings are authored as ICU messages from the start**, not
  retrofitted. Russian has three plural forms and Armenian has two, and
  "N visits", "N monuments", "N m²" and "N days" appear in the calculator, the
  tariff cards, the credit block and the visit list.
- **The denylist fails the build on:** `bestseller`, `most popular`,
  `most chosen`, `monthly`, `preventive visit`, `light visit`, `heavy visit`,
  `QR`, `memory page`, `testimonial`, `trusted by`, `families served`,
  `since 20`, `the only`, `the first`, `nobody else`, `unlike other`,
  `no one in Yerevan`, `Memory Care` (spaced), `Memory-Care`, `MEMORYCARE`,
  `Oops`, `Something went wrong`, `Error`, `Invalid`, `Failed`,
  `Required field`, `save`/`discount`/`offer`/`%`/`was`/`instead of` within 80
  characters of a price, and **every emoji codepoint**.
- **`text-decoration: line-through` on a price is a build failure.**
- **`{…}` in a shipped locale that is not on the runtime-variable allowlist is a
  build failure**, so no placeholder can ship as literal braces.
- **The tagline is a fixed asset string with no full stop**, stored once:
  `brand.tagline = "HONORING MEMORY, CARING FOR LOVED ONES"`. The linter fails
  on a trailing period.
- **No competitor is named on the site, in any language, in any form, including
  in an FAQ answer.** We describe the combination we offer — photographs, video,
  GPS, a portal and accounts for the whole family, the full chain in one place —
  and never what anyone else lacks. And we never claim that nobody does grave
  care with photo reports in Yerevan: that is false and checkable.
- **Invent nothing.** No testimonials, no review counts, no "trusted by N
  families", no years in business, no client numbers. The company is pre-launch
  with zero paying customers.
- **Never mention a QR code on a headstone or a digital memory page.** Year-2
  scope; it does not exist; not even as "coming soon", not in alt text, not in
  meta.
- **Never write diaspora-only copy.** "You are far away" addresses one of two
  readers on the same page. One block, outcome first, both reasons in one line
  of body text, neither ranked. The two-card *"You are far away" / "You have no
  time"* construction is deleted.
- The one place a country may be named is the fairness line, used in exactly
  three places and nowhere else: **`One price list — the same in Yerevan and in
  Los Angeles.`** (56). It must not migrate into the hero, About or any
  headline.
- Every visit is a **full visit**. The first visit of a subscription is a full
  visit: *"On the first visit the crew locates the plot and records its GPS
  point, and then does the full work — so every later report can be compared
  with the first."* Only Inspection is a survey.
- A **subscription year is twelve months from the signing date.** Seasons are a
  promise inside those twelve months, worded as "one visit in each season". If
  no suitable winter weather window occurred, the visit is **added** to spring;
  four visits are guaranteed regardless. Renewal is offered against the client's
  own anniversary, never a company calendar, and **there is no auto-charge** — a
  renewal offer goes out 30 days before the anniversary and the client acts.
  Silently charging a card for a memorial service a year later is the wrong
  register for this brand.

---

## 9. Figma file structure

Built so **two people** can maintain it for six months without a library graph,
a branching workflow or a merge.

### 9.1 Two files, not one and not twelve

**File 1 — `MemoryCare · Foundations & Components`** — published as a library.

| Page | Contents | Layer naming |
|---|---|---|
| `00 · Read me` | How to use this file · who publishes · the **"tokens.json wins over Figma"** rule · the Cabin-substitute label · current version | — |
| `01 · Foundations` | Colour swatches with §4's contrast matrix drawn as a grid; the type specimen in all three scripts at every role; the spacing ruler; the three radii; the single overlay shadow; the six motion demo frames | `Foundation/Colour/Surface-Page` |
| `02 · Components` | One section per component, in the same order as `components/00-INDEX.md` | `Button/Primary`, `Input/Text`, `Card/Tariff` |
| `03 · Patterns` | Composed blocks used more than once: the pricing bands, the report masthead + confirmation, the form block, the footer, the mobile action bar, the guarantees block | `Pattern/PricingBand-Annual` |
| `04 · Brand assets` | The twelve production lock-ups, the favicon set, the OG frames, every placeholder frame at its exact ratio | `Brand/Logo/Horizontal-Compact` |
| `99 · Archive` | Anything superseded, dated, **never deleted** | `[2026-08-27] Old palette` |

**File 2 — `MemoryCare · Product`** — consumes File 1, publishes nothing.

| Page | Contents |
|---|---|
| `00 · Read me` | Route map, status legend, the frame-naming convention |
| `01 · Site — Home` | 360 / 900 / 1440 frames |
| `02 · Site — Pricing` | + every calculator state, including over-ceiling |
| `03 · Site — How it works · Sample report · Family Circle` | |
| `04 · Site — About · Contacts · Guarantees · Legal ×4` | |
| `05 · Portal — Auth, activation, first entry` | |
| `06 · Portal — Visits & Report` | + the guest route `/r/` |
| `07 · Portal — Family Circle & permissions` | |
| `08 · Portal — Payment, bank transfer, profile` | |
| `09 · Bad news & edge states` | moved · could not reach the plot · repeat visit · payment failed · awaiting transfer · cancellation with the refund table · 404 · 500 |
| `10 · Flows` | Arrows between existing frames. **No new pixels are drawn on this page.** |
| `99 · Archive` | |

### 9.2 Naming, everywhere

`Category/Subcategory/Name`, with `Property=Value` for variants —
`Button/Primary` with `Size=md, State=hover, Icon=leading`.
Frames in File 2: `<route> · <breakpoint> · <state>` →
`Pricing · 360 · calculator-over-ceiling`.
**Every text node's layer name is its string key in double braces** —
`{{hero.h1}}` — so the frame and `strings.en.json` are visibly linked and Igor
never transcribes copy from a picture.

### 9.3 Variables → tokens, mechanically

Four Figma variable collections, matching the three layers plus layout, so the
mapping is mechanical and round-trips through Tokens Studio:

| Figma collection | Modes | Maps to |
|---|---|---|
| `1 Primitive` | (none) | `primitive.*` |
| `2 Semantic` | **`Light`, `On dark`, `On ivory`** | `semantic.*` — the three modes are exactly `:root`, `.mc-on-dark` and `.mc-on-ivory` |
| `3 Component` | (none) | `component.*` |
| `4 Layout` | **`360`, `900`, `1440`** | the responsive overrides in `mc-tokens.css` |

Figma variable names are the token path with `/` instead of `.` and no `mc`
prefix: `semantic.text.accent` → `Semantic/Text/Accent`. A script in
`figma/sync/` converts in both directions. **Nobody retypes a value, ever.**

### 9.4 Maintenance rules for a two-person company

- **One publisher.** Only the design lead publishes the library.
- Every publish carries a description in the form `v1.2 — added Toast/Error;
  changed nothing existing`, and it is mirrored into `CHANGELOG.md` the same
  day.
- **Component variants are capped at 24 combinations.** Beyond that it is two
  components.
- **No detached instances in File 2.** A detached instance is a review failure.
- **Branching is not used.** Two people editing one file is cheaper than merges.
- Figma **Dev Mode** is enabled and every component in File 1 carries a Code
  Connect link to its `SPEC-*.md`. **Dev Mode's generated CSS is explicitly not
  to be copied** — it emits raw hexes. A note to that effect sits on
  `00 · Read me` and is repeated in the handoff `README.md`.

### 9.5 What lives in Figma versus what lives in files

| Question | Answer lives in |
|---|---|
| What colour is this? | `tokens/tokens.json` |
| How much space is between these? | `tokens.json` + the component spec |
| What does this screen look like assembled? | Figma File 2 |
| What order are the sections in? | `layout/PAGE-TEMPLATES.md` — Figma illustrates it |
| What are the states? | `components/SPEC-*.md` — Figma shows a variant board |
| What is the copy? | `content/strings.*.json` |
| What is the price? | `content/products.json` |
| What happens on hover? | the spec |
| What does the empty state say? | `strings.en.json` |
| **What is the exact hex of this pixel?** | **Never eyedrop Figma. `tokens.json`.** |

If Figma disagrees with `tokens.json`, **`tokens.json` wins and Figma is a bug
we fix.** This is stated in bold in `README.md`, because the previous round of
this project shipped a palette that had been sampled off a JPEG.

---

## 10. Logo production preparation

### 10.1 What we actually have — measured, not estimated

All nine supplied SVGs are `viewBox="0 0 1080 1080"`. Content bounding boxes
computed from the path data:

| File group | Content bbox (x, y, w, h) | Padding | Aspect |
|---|---|---|---|
| `logo mark_*` | `112.7, 170.2, 854.7, 739.7` | left 112.7 · right 112.6 · top 170.2 · bottom 170.2 | **1.156 : 1** |
| `primary logo_*` (vertical lock-up) | `112.9, 55.2, 854.7, 965.4` | left 112.9 · right 112.4 · top 55.2 · bottom 59.4 | **0.885 : 1** |
| `wordmark_*` (word + tagline) | `130.5, 446.0, 819.0, 188.1` | top 446 · bottom 446 | **4.354 : 1** |
| — word line only | `168.0, 446.0, 744.0, 118.6` | — | **6.273 : 1** |
| — tagline only | `130.5, 604.1, 819.0, 30.0` | — | **27.3 : 1** |
| inside the vertical lock-up: mark | `112.9, 55.2, 854.7, 739.6` | — | identical mark |
| inside the vertical lock-up: word block | `130.8, 832.5, 819.0, 188.1` | gap below the mark **37.6** | identical wordmark |

Two facts that matter. The wordmark file is **97% empty space** — 819×188 of
content inside 1,166,400 px² of canvas. And the vertical lock-up **reuses the
mark and the wordmark at 1:1 scale** with a 37.6-unit gap. That second fact is
what makes a horizontal lock-up constructible today from the designer's own
artwork at her own proportions.

### 10.2 Preparation method — scripted, so it is reproducible

`brand/logo/prepare.mjs`, run against `brand/logo/source/`:

1. Replace `viewBox="0 0 1080 1080"` with the measured content bbox.
2. Remove `width`/`height` attributes entirely; add
   `preserveAspectRatio="xMidYMid meet"` — the SVG then scales from CSS and
   never imposes a square.
3. Replace the `<style>` block and `class="cls-N"` with `fill` attributes; in
   the mono versions use `fill="currentColor"`, so one file serves every
   context.
4. Add `role="img"` and `<title>MemoryCare</title>`; add `aria-hidden="true"`
   where the mark sits beside visible wordmark text (the site header).
5. SVGO `--precision=2 --multipass`, keeping `viewBox`, removing metadata, ids
   and the `<defs>`/`<style>` machinery.
6. `brand/logo/verify.mjs` asserts each result is **< 12 KB** and pixel-diffs
   identically to the source at 512px.

**Nobody ever edits a production SVG by hand.** The nine originals stay
untouched in `brand/logo/source/`; when the designer sends corrected files,
`prepare.mjs` is re-run and nothing downstream changes.

### 10.3 The constructed horizontal lock-up — exact geometry

The designer has not supplied one and the header needs one now. It is
constructed from her own artwork; when hers arrives we swap the file and nothing
else changes.

**Compact — `lockup-horizontal-mono.svg`.** Mark at the inline-start, word line
only, no tagline (a 30-unit-tall tagline is illegible at header size).

- Word line, unscaled: **744 × 118.6**.
- Mark height = **2.2 × word-line height = 260.9**; mark width =
  `260.9 × 1.1556` = **301.5**. This ratio makes the mark read as an icon beside
  the word rather than as a second focal point; the vertical lock-up's own ratio
  (6.24×) is unusable horizontally.
- Gap = **0.55 × word-line height = 65.2**. (The vertical lock-up's gap is 37.6
  against a 739-tall mark = 0.32 of the wordmark-block height; 0.55 of the
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
  <g transform="scale(0.35271) translate(-112.7,-170.2)">
    <!-- paths from MemoryCare_logo mark_dark.svg -->
  </g>
  <!-- word line: source bbox 168,446,744,118.6 → scale 1, placed after mark + gap -->
  <g transform="translate(366.7,71.15) translate(-168,-446)">
    <!-- word-line paths from MemoryCare_wordmark_dark.svg, excluding tagline paths (y > 580) -->
  </g>
</svg>
```

**With tagline — `lockup-horizontal-tagline-mono.svg`.** Same construction using
the full wordmark block (819 × 188.1): mark height `1.55 × 188.1 = 291.6`, mark
width **336.9**, gap **60**, canvas **1216 × 292**, aspect **4.16 : 1**, wordmark
block vertically centred at `y = (291.6 − 188.1) / 2 = 51.75`.

**Colour variants** are the same geometry with the designer's fills: hands
Nude/Ivory, petals Olive, "Memory" Ivory, "Care" Olive, tagline Olive.

### 10.4 The delivered file list — twelve production assets

| # | File | viewBox | Where it is used |
|---|---|---|---|
| 1 | `mark-color.svg` | `112.7 170.2 854.7 739.7` | Anthracite or pure-white grounds **only** — the Ivory hands vanish on Nude (1.1) |
| 2 | `mark-mono.svg` | same | `currentColor`. **The default everywhere**, including the site header |
| 3 | `wordmark-color.svg` | `130.5 446 819 188.1` | word + tagline, two-colour; print, letterhead |
| 4 | `wordmark-mono.svg` | same | `currentColor` |
| 5 | `wordmark-word-only-mono.svg` | `168 446 744 118.6` | no tagline; used inside the constructed lock-ups |
| 6 | `lockup-vertical-color.svg` | `112.9 55.2 854.7 965.4` | print, social avatar backgrounds, the OG default |
| 7 | `lockup-vertical-mono.svg` | same | one-colour print, stamps |
| 8 | `lockup-horizontal-color.svg` | `0 0 1111 261` | constructed — invoices, the written quote, partner material |
| 9 | `lockup-horizontal-mono.svg` | `0 0 1111 261` | constructed — the report masthead, the email header bar, the PDF |
| 10 | `lockup-horizontal-tagline-mono.svg` | `0 0 1216 292` | **the site footer**, letterhead, vehicle livery |
| 11 | `mark-simplified-mono.svg` | `0 0 32 32` | ≤ 20px: favicon 16, app icon, WhatsApp avatar |
| 12 | `petal-bullet-mono.svg` | `0 0 24 24` | the list bullet and the `PlotDiagram` marker — a single path, no weave, no hands |

Files 11 and 12 are the **only new drawing this system owes**; both are
`OPEN-ITEMS` and both are derivable from the master. Until they land, the
favicon at 16px uses `mark-mono` (accepting the blur) and the bullet is a 6px
Olive disc.

**The site header does not use any drawn wordmark.** It uses `mark-mono.svg`
plus live text (§7.3). The constructed lock-ups exist for the footer, the OG
images, the report masthead, print, the invoice and the quote — every place they
run at or above their minimum widths.

### 10.5 `brand/LOGO-USAGE.md` — clear space, minimums, prohibitions

**Clear space** = the height of the "M" in the wordmark, on all four sides.
Expressed relative to the asset so it survives scaling: for the horizontal
lock-up, clear space = **0.42 × total height**, encoded as
`--mc-layout-logo-clearspace: 0.42em` applied as padding on the logo wrapper, so
nobody has to measure.

| Asset | Minimum size |
|---|---|
| Vertical lock-up | 64px wide |
| Horizontal compact | 120px wide (the mark lands at 28px) |
| Horizontal with tagline | 240px wide — below this the tagline breaks up |
| Mark, full detail | **24px** — at 16px the woven medallion collapses to a blur |
| `mark-simplified-mono` | 16px |

**Forbidden.** Every item on this list has already happened somewhere in this
project's history:

- the colour mark on a Nude ground;
- any recolouring outside the five brand values;
- **rotation of the mark, including as a loading spinner**;
- outline, drop shadow or glow;
- the mark inside a circle or a badge;
- **the mark used as the hero image** (the current site's mistake);
- stretching to a non-native aspect;
- the tagline set **with** a full stop;
- the tagline set below **13px**;
- `Memory Care`, `MEMORYCARE`, `MC`;
- "Care" set in Olive at interface sizes (3.42 — it is Deep Olive);
- the tagline in Olive on Anthracite (3.08 — it is Nude);
- the 1080² source files used directly in any layout.

### 10.6 Favicon, icons and OG

| File | Size | Source |
|---|---|---|
| `favicon.svg` | any | `mark-simplified-mono`, `fill="#33373C"`, with an internal `prefers-color-scheme: dark` rule switching to `#EFE5D5` |
| `favicon-32.png` | 32 | `mark-mono` on `#F3F0E9` |
| `favicon-16.png` | 16 | **`mark-simplified`** on `#F3F0E9` |
| `apple-touch-icon.png` | 180 | `mark-color` on `#33373C`, 16% padding, no rounding (iOS masks) |
| `icon-192.png` / `icon-512.png` | PWA | `mark-color` on `#33373C`, 16% padding |
| `maskable-512.png` | 512 | `mark-mono` Nude on `#33373C`, content inside the central 80% safe zone |
| `og-default.png` | 1200×630 | **Anthracite** ground, horizontal lock-up centred, tagline below |
| `og-report-share.png` | 1200×630 | **Anthracite** ground, mark + the words "Visit report" + the date rendered server-side. **Never a photograph. Never a location. Never a plot label.** |

---

## 11. The handoff package

### 11.1 One repository. If it is not in this tree, it is not a requirement

`memorycare-design-handoff-v1.0/`. Nothing is delivered by chat, screenshot or
email attachment. Every file has exactly **one owner** — the only person who may
change it — and is the source of truth for exactly **one** thing.

```
memorycare-design-handoff-v1.0/
├── README.md
├── DECISIONS.md
├── DECISIONS-2.md
├── FINAL-SYSTEM.md
├── CHANGELOG.md
├── OPEN-ITEMS.md
├── ACCEPTANCE-CHECKLIST.md
├── DEVELOPER-DECISIONS.md
│
├── tokens/
│   ├── tokens.json
│   ├── sd.config.js
│   ├── build/  mc-tokens.css · mc-tokens.scss · tailwind.tokens.js · tokens.d.ts
│   ├── CONTRAST-MATRIX.md
│   └── stylelint-mc-contrast/
│
├── components/
│   ├── 00-INDEX.md
│   └── SPEC-*.md            × 52
│
├── layout/
│   ├── GRID.md · ROUTES.md · PAGE-TEMPLATES.md · JOURNEYS.md
│
├── portal/
│   ├── PERMISSION-MATRIX.md · NOTIFICATION-MATRIX.md
│
├── visual/
│   ├── ART-DIRECTION.md · PHOTO-BRIEF.md · SHOT-LIST-SEPTEMBER.md · MOTION.md
│
├── content/
│   ├── strings.en.json · strings.hy.json · strings.ru.json
│   ├── content-limits.json · products.json · COPY-RULES.md
│
├── conversion/
│   ├── OBJECTION-MAP.md · CTA-PLACEMENT.md · POST-PAYMENT.md · CALL-GUIDE.md
│
├── brand/
│   ├── LOGO-USAGE.md · FONTS.md
│   ├── logo/source/ · logo/production/ · logo/prepare.mjs · logo/verify.mjs
│   ├── fonts/ · favicon/ · og/
│
├── templates/
│   ├── EMAIL-TEMPLATE.md · INVOICE-TEMPLATE.md · QUOTE-TEMPLATE.md · REPORT-PDF.md
│
├── placeholders/
│   ├── README.md
│   ├── photo-3x2-plot-arrival.svg · photo-3x2-plot-after.svg
│   ├── photo-3x2-section.svg · portrait-1x1-crew.svg
│   ├── portrait-1x1-founder.svg · video-16x9-report.svg
│
├── qa/
│   ├── contrast.spec.ts · strings.spec.ts · meta.spec.ts
│   ├── glyphs.spec.ts · prices.spec.ts · bundle.spec.ts
│   └── VISUAL-BASELINES/     360 / 900 / 1440
│
└── figma/
    ├── FIGMA-MAP.md
    └── sync/
```

### 11.2 File inventory — owner and source-of-truth statement

| Path | Owner | Source of truth for |
|---|---|---|
| `README.md` | Design system | The order of operations and the "tokens.json wins over Figma" rule |
| `DECISIONS.md`, `DECISIONS-2.md` | **Owner (Hayk)** | Binding rulings. Override every other file in this tree. |
| `FINAL-SYSTEM.md` | Design system | The converged system. Overridden only by the two above. |
| `CHANGELOG.md` | Design system | What changed per version and what Igor must re-check |
| `OPEN-ITEMS.md` | Design system (each entry owned individually) | Everything unresolved, with an owner, a blocker and a date |
| `ACCEPTANCE-CHECKLIST.md` | Design system | What Igor signs off against |
| `DEVELOPER-DECISIONS.md` | Design system | The eleven things that are Igor's call |
| `tokens/tokens.json` | Design system | **Every value in the product. No exceptions.** |
| `tokens/build/*` | Design system (generated) | Nothing — generated, committed, never hand-edited |
| `tokens/CONTRAST-MATRIX.md` | Design system | The closed permission list of colour pairs |
| `tokens/stylelint-mc-contrast/` | Design system | Machine enforcement of the above and of the Olive-label ban |
| `components/00-INDEX.md` | Design system | The component list, its status, its Figma node id |
| `components/SPEC-*.md` | Design system, claimant named in each | Anatomy · measurements · state matrix · props · ARIA and keyboard contract · responsive rule · content limits · "do not" list |
| `layout/GRID.md` | Design system | The single breakpoint set |
| `layout/ROUTES.md` | **UX architect** | Every URL, its locale variants, its meta and indexing rules |
| `layout/PAGE-TEMPLATES.md` | **UX architect** | Section order per route, by component name |
| `layout/JOURNEYS.md` | **UX architect** | The three journeys, including the split-payer case |
| `portal/PERMISSION-MATRIX.md` | **UX architect**, ratified by **Owner** | Who may do what; the data contract behind Family Circle |
| `portal/NOTIFICATION-MATRIX.md` | **UX architect** | Event × recipient routing, including the local contact |
| `visual/ART-DIRECTION.md` | **Visual lead** | The visual concept, section rhythm, Olive's jobs, the no-shadow rule |
| `visual/PHOTO-BRIEF.md` | **Visual lead** | The ratio table, treatment rules, framing |
| `visual/SHOT-LIST-SEPTEMBER.md` | **Visual lead** | Per-plot shot list, marked standing position, tripod height, focal length, file naming matching `placeholders/` |
| `visual/MOTION.md` | **Visual lead** | The six permitted behaviours and the forbidden list |
| `content/strings.en.json` | **Writer** | Every user-facing string. No literal text in any component. |
| `content/strings.hy.json`, `.ru.json` | **Writer** → localiser | Keys present, values `TODO-TRANSLATION` |
| `content/content-limits.json` | Design system, populated by **Writer** + **Visual lead** | Grapheme ceilings per slot per locale |
| `content/COPY-RULES.md` | **Writer** | The denylist, the voice principles, the validation tone rules |
| `content/products.json` | **Owner**, maintained by **Conversion** | Prices, surcharge rates, credit rules, the 60-day window, the refund formula. **The only place a price exists.** |
| `conversion/OBJECTION-MAP.md` | **Conversion** | Which block answers which objection, with what proof |
| `conversion/CTA-PLACEMENT.md` | **Conversion** | Count and placement of every CTA; the "never next to a photograph" rule |
| `conversion/POST-PAYMENT.md` | **Conversion** | The signals between payment and first visit, and the no-answer ladder |
| `conversion/CALL-GUIDE.md` | **Conversion** | The first sixty seconds, the five things we must learn, the five we must say, and the one we must never do — quote a different number from the one the calculator showed |
| `brand/LOGO-USAGE.md` | Design system | Clear space, minimum sizes, forbidden uses |
| `brand/FONTS.md` | Design system | Licences, subsets, `unicode-range`, the Gill Sans substitution label, **and every unverified glyph claim** |
| `brand/logo/source/` | **Designer** | The nine original 1080² SVGs, untouched |
| `brand/logo/production/` | Design system (generated by `prepare.mjs`) | The twelve prepared assets |
| `brand/fonts/` | Design system | Self-hosted `woff2`, subset per script, ≤180 KB per locale |
| `brand/favicon/`, `brand/og/` | Design system | The icon set; the two OG images |
| `templates/EMAIL-TEMPLATE.md` | Design system | The 600px table-based transactional email |
| `templates/INVOICE-TEMPLATE.md` | Design system | The bank-transfer invoice |
| `templates/QUOTE-TEMPLATE.md` | Design system + **Conversion** | The one-page written quote |
| `templates/REPORT-PDF.md` | Design system | A4, block order, the no-price rule |
| `placeholders/` | **Visual lead**, cut by Design system | Every placeholder, each naming ratio, pixel size, subject and source |
| `qa/*.spec.ts` | Design system | The merge gates |
| `qa/VISUAL-BASELINES/` | Design system | Reference screenshots at 360 / 900 / 1440 |
| `figma/FIGMA-MAP.md` | Design system | node-id → spec file → code file |

### 11.3 How Igor moves from a Figma frame to production code

Written as the actual sequence, and repeated verbatim in `README.md`:

1. **Open the route in File 2 → Product.** The frame name gives him the route,
   the breakpoint and the state.
2. **Read `layout/PAGE-TEMPLATES.md` for that route.** It lists the sections top
   to bottom by component name and container width. He builds the page skeleton
   from this, **not by measuring the Figma frame**.
3. **For each section, open `components/SPEC-<name>.md`.** He builds from the
   measurement table and the state matrix. Figma is used only to confirm he has
   the right component and the right composition.
4. **He never types a value.** Every number and colour comes from
   `tokens/build/mc-tokens.css`. **If a value is missing he stops and files it
   in `OPEN-ITEMS.md` — he never approximates.**
5. **Copy comes from `content/strings.en.json` by key.** The key is printed in
   the Figma layer name of every text node as `{{hero.h1}}`.
6. **Prices come from `content/products.json`**, never from a string and never
   from a component.
7. **He runs `npm run lint:tokens && npm run lint:strings && npm run test:a11y
   && npm run test:glyphs` before pushing.** All four are merge gates.
8. **He compares against `qa/VISUAL-BASELINES/` at 360, 900 and 1440.**
9. **He ticks the row in `ACCEPTANCE-CHECKLIST.md`.**

### 11.4 Versioning and what happens after handoff

- The package is semver'd. **`1.x` is additive** — Igor pulls and continues.
  **`2.0` means a value changed** and he must re-check the routes named in
  `CHANGELOG.md`.
- **Token changes are never delivered in conversation.** They are a package
  version.
- A weekly 30-minute call while the build runs, with `OPEN-ITEMS.md` as the only
  agenda. Anything raised outside that call is written into the file rather than
  answered ad hoc, so the file stays the record.
- When the September photography lands it is a `1.x` release replacing the files
  in `placeholders/` with real assets at **identical names and identical aspect
  ratios**. No component changes.

---

## 12. `ACCEPTANCE-CHECKLIST.md` — what Igor signs off against

Per route. Boolean. No partial credit. Every item is objectively verifiable by
running a command, reading a value, or observing a stated condition — no item
requires a judgement about whether something "looks right".

### Tokens and styling

- [ ] `mc-tokens.css` is imported exactly once, globally, and is byte-identical to the package copy.
- [ ] `grep -rE "#[0-9a-fA-F]{3,8}" src/` returns **zero** results.
- [ ] `grep -rE ":\s*[0-9]+(px|ms)" src/` returns only values that are `var()`-derived or appear in the documented-exception list in `README.md`.
- [ ] `grep -rE "var\(--mc-color-olive-700\)" src/` returns **zero** results — components use `--mc-text-accent` / `--mc-border-accent`.
- [ ] `grep -rEi "danger|success|warning" src/ tokens/` returns **zero** results.
- [ ] `grep -rE "border-radius" src/` returns only `var(--mc-radius-0|--mc-radius-sm|--mc-radius-full)`.
- [ ] `grep -rE "box-shadow" src/` returns only `var(--mc-elevation-overlay)` and the documented focus-ring halo, and only inside Modal, Drawer, BottomSheet, Lightbox and Toast.
- [ ] `grep -rE "transform:\s*translate" src/` returns zero results on any card or button rule.
- [ ] `npm run lint:tokens` exits 0.
- [ ] `stylelint-mc-contrast` exits 0; no colour pair outside §4.1 exists.
- [ ] No forbidden token name (`--gold`, `--navy`, `--mut`, `--dim`, `--blue`, `--lilac`) appears anywhere.

### Layout and responsive

- [ ] Media queries in `src/` use only the five breakpoints 360 / 600 / 900 / 1200 / 1440, min-width, with at most the two documented `max-width` exceptions.
- [ ] At 360px, no route produces horizontal scroll.
- [ ] At 360px zoomed to 200%, no route produces horizontal scroll.
- [ ] Below 600px, no route renders a 2-up grid, including the gallery.
- [ ] No `<table>` renders below 600px except `PermissionMatrix`.
- [ ] At most **one** fixed element occupies the block-end on any route at any scroll position (assert with a DOM query in `qa/`).
- [ ] `MobileActionBar` is absent from `/portal/visits/:id/` and from `/r/:token/`.
- [ ] Header height is 56px below 900 and 72px from 900.
- [ ] The header bottom rule is present at page load, before any scroll.

### Accessibility

- [ ] axe-core: **zero serious/critical** on every route, in all three locales, at 360 and 1280.
- [ ] Every interactive element is reachable and operable by keyboard alone.
- [ ] A visible focus ring appears on every control, including sliders, the language switcher, gallery thumbnails and the map link.
- [ ] Every hit area measures ≥44×44 (assert `getBoundingClientRect` in `qa/`, including the `.mc-hit-44` pseudo-element).
- [ ] `grep -rE "tabindex=\"[1-9]" src/` returns zero results.
- [ ] With `prefers-reduced-motion: reduce`: no translate, no shimmer, no count-up, no auto-advance, no rotation.
- [ ] Every image has meaningful `alt`; decorative images have `alt=""`.
- [ ] Every form field has a visible label, `aria-describedby` on its error, `aria-invalid` when errored, and an error summary with `role="alert"` on failed submit that receives focus.
- [ ] `lang` is correct on `<html>` for each locale; `:lang(hy)` renders overline and rail labels in sentence case.
- [ ] No text renders below 13px anywhere, in any locale, including the tagline and the PDF.

### Content and brand

- [ ] `npm run lint:strings` exits 0: denylist clean, every length limit met in all three locales.
- [ ] `npm run test:glyphs` exits 0: U+058F present in the currency family; hy and ru ranges covered; tabular figures available in the price family; ≤180 KB per locale.
- [ ] The tagline appears with **no full stop**, everywhere, including the PDF and the OG image.
- [ ] "MemoryCare" is spelled correctly in every instance; `Memory Care`, `Memory-Care`, `MEMORYCARE` and `MC` return zero matches.
- [ ] `MemoryCare LLC` appears in the footer, the invoice, the quote, the four legal pages and the meta tags.
- [ ] Zero invented statistics, testimonials, review counts, client numbers or years in business.
- [ ] `grep -rEi "\bQR\b|memory page" src/ content/` returns zero results, including alt text and meta.
- [ ] Both founders' names and both phone numbers appear as `tel:` links, and `info@memorycare.am` as `mailto:`, in the footer of **every** page.
- [ ] The legal address renders as the marked placeholder string, never as invented text.
- [ ] `npm run test:prices` exits 0: every rendered price traces to `products.json`; no `line-through` on any price; no denylisted word within 80 characters of a price.
- [ ] Every price renders **both** `֏` and `AMD`.
- [ ] The badge on Optimal reads `Our recommendation`; `most chosen` and `bestseller` return zero matches in every locale file.
- [ ] No Olive fill carries a label anywhere; no Olive text exists anywhere.
- [ ] The footer tagline is Nude, not Olive.
- [ ] "Care" in the header wordmark resolves to `--mc-text-accent`.

### Behaviour

- [ ] Every component renders `default / loading / empty / error / success` in Storybook, or the spec states in one sentence why a state is impossible.
- [ ] The three status screens (`rescheduled`, `no-access`, `revisit`) exist and are reachable in Storybook, and none of them contains `--mc-color-feedback-error`.
- [ ] Calculator arithmetic matches the two formulas in §7.3 — unit tested, including the over-ceiling branch and both boundary values (16 m², 2 monuments).
- [ ] Refund arithmetic matches `amount_paid × (visits_not_performed ÷ visits_total)` rounded **up** to 100 ֏ — unit tested with the worked case 95,000 × 3/4 = **71,300**, and asserted **not** to compute from a list price.
- [ ] The calculator and the refund table import the **same** arithmetic module (assert by import graph).
- [ ] Credit logic matches `products.json`: 60-day window, the larger of the two, fires only at annual signing, no Inspection→Express credit, **one credit per plot**.
- [ ] The consultation form accepts `+1`, `+33`, `+7`, `+374` and local formats, and stores E.164.
- [ ] The consent checkbox is present and required, and its failure state moves focus to the summary.
- [ ] `npm run test:bundle` exits 0: the `/r/:token/` bundle contains no `TariffCard`, no `PlotCalculator`, no `Badge--accent`, no `MobileActionBar` and no `primary` button.
- [ ] The guest report renders no price, no next-visit date, no subscription name and no recommended-work figures, verified against the **server response**, not the DOM.
- [ ] `npm run test:meta` exits 0: the report OG image is the static asset; `og:description` contains no cemetery, no plot label and no name; `<title>` is `Visit report — {date}`.
- [ ] `/r/:token/` returns `X-Robots-Tag: noindex, nofollow` and carries a `noindex` meta.
- [ ] Share tokens carry ≥128 bits of entropy and are revocable from the `ShareSheet`.
- [ ] `plot.display_mode` defaults to `none`; switching it off removes the name from previously issued links (integration test).
- [ ] Cancellation with the pro-rata refund is completable end to end without contacting us, and the arithmetic is shown before the confirm step.
- [ ] Reports remain readable after cancellation, read-only, with no upsell rendered on those screens.
- [ ] The visit reminder is opt-in and can be addressed to a different person, and the local-contact consent checkbox is present.
- [ ] The permission matrix is implemented exactly as §7.6 — a Family member receives no plan name, no price and no renewal date **from the server**.
- [ ] Report SLA text reads "within 48 hours" and the callback text reads "within one business day" in all six places, identically.
- [ ] No auto-charge exists on renewal; the renewal notice fires 30 days before the client's own anniversary.

### Performance and delivery

- [ ] LCP ≤ **2.5s** on a throttled 4G profile at 360px, on Home, in all three locales.
- [ ] CLS ≤ **0.05**. Every image carries intrinsic `width`/`height`.
- [ ] Fonts are self-hosted, ≤180 KB per locale, `font-display: swap`, with correct `unicode-range` and fallback metric overrides.
- [ ] Zero requests to `fonts.googleapis.com` or to any third-party CDN for a brand asset.
- [ ] Zero third-party analytics requests and **therefore no cookie banner exists** on any route.
- [ ] The header logo is the prepared asset plus live text, never a cropped 1080² file.
- [ ] The favicon set is complete and `mark-simplified` is used at 16px.

### Bank (Ameriabank) — every one is a hard gate for card acceptance

- [ ] An About page exists with a company description.
- [ ] Contacts appear in the footer of **every** page.
- [ ] Full service descriptions exist for all five products.
- [ ] A service-limitations / legal-restrictions page exists.
- [ ] Real prices in AMD, with the symbol **and** the letters.
- [ ] An English privacy policy exists.
- [ ] A refund policy exists and states the pro-rata formula and its base.
- [ ] Terms of service / service-delivery terms exist.

---

## 13. `DEVELOPER-DECISIONS.md` — what is deliberately Igor's call

We will not answer questions about these and we will not review them. Each has a
requirement attached; the requirement is ours, the choice is his.

1. **Framework and rendering strategy** — Next.js, Astro, SvelteKit, plain Vite;
   SSG or SSR. *Requirement:* server-rendered HTML for the marketing routes (SEO
   and the bank's review), and per-locale URLs `/en/ · /hy/ · /ru/` from day one.
2. **CSS methodology** — CSS Modules, vanilla-extract, Tailwind, plain CSS.
   *Requirement:* `mc-tokens.css` is the sole source of values. If he picks
   Tailwind, `build/tailwind.tokens.js` is in the package.
3. **Component library, if any** — Radix, Ark, Headless UI, or hand-rolled. Our
   specs are behaviour contracts, not implementations. *Recommendation, not a
   requirement:* Radix or Ark will satisfy the ARIA contracts faster.
4. **State management, data fetching and caching.**
5. **i18n library** — next-intl, i18next, Paraglide. *Requirement:* ICU
   pluralisation (Russian has three plural forms, Armenian two) and `lang`
   correctly set on `<html>`.
6. **Form and validation library** — react-hook-form + zod, Felte, anything.
   *Requirement:* the validation **timing** rules in `SPEC-Input.md` — on blur,
   never on keystroke, re-validate on keystroke only after a first error.
7. **Phone input implementation** — libphonenumber-js or equivalent.
   *Requirement:* the behaviour in `SPEC-CountrySelect.md` and `SPEC-Input.md`,
   not a particular package.
8. **Image pipeline** — format negotiation, AVIF/WebP, CDN, `srcset`.
   *Requirement:* the aspect ratios and intrinsic dimensions in
   `SPEC-Gallery.md`.
9. **Hosting, CI, error monitoring, and the analytics transport.** *Which*
   events we count is ours (`report_sample_opened`, `calculator_interacted`,
   `calculator_ceiling_reached`, `form_started`, `form_field_error` by field,
   `consultation_submitted`, `call_connected`, `quote_sent`,
   `payment_confirmed`, `portal_first_login`, `report_shared`,
   `guest_report_opened`, plus payment→first-report and first-login→first-report
   timings); *how* they are sent is his. **Constraint: server-side and
   cookieless at launch — no third-party analytics, therefore no consent
   banner.**
10. **Backend, database, API shape, PDF generation, file storage, share-token
    issuance.** *Requirement:* ≥128 bits of token entropy; the guest response is
    filtered **server-side**, not hidden client-side.
11. **Animation implementation** — CSS transitions, Motion One, Framer Motion.
    *Requirement:* the durations, easings and distances are the token values,
    the six permitted behaviours are the complete list, and
    `prefers-reduced-motion` is honoured.

**The corollary, stated as plainly as we can.** Choosing a colour, a spacing
value, a radius, a font size, a duration, a copy string, a price, or the order
of blocks in the report sheet **is never his decision**. If he needs one of
those and cannot find it, that is our failure and it goes in `OPEN-ITEMS.md`,
answered within one business day.

---

## 14. `OPEN-ITEMS.md` — everything unresolved, with an owner

**Blocking** = the build cannot ship this surface without it.
**Non-blocking** = the build proceeds; the item is a one-line swap when it lands.

### 14.1 Owner (Hayk / Davit) — commercial and legal

| # | Item | Blocks | Status |
|---|---|---|---|
| 1 | **Legal address.** The oldest open item. Renders today as the marked placeholder `[LEGAL ADDRESS — pending]`. | **BLOCKING** — the footer of every page, the About page, the Contacts page, the invoice, the written quote, and the Ameriabank submission | Not supplied |
| 2 | **Company registration / VAT number.** Same placeholder treatment: `[REG. NUMBER — pending]`. | **BLOCKING** — the footer, About, the invoice, the bank submission | Not supplied |
| 3 | **Working hours in Yerevan time**, to be stated next to the "within one business day" callback promise so a client in Los Angeles can convert it. Round one wrote "10:00–19:00" and "10–15 minutes" as if confirmed; neither is. | **BLOCKING** the confirmation screen, the confirmation email and the Contacts page | Unconfirmed |
| 4 | **Weekend and Armenian public-holiday rule** for "within one business day". Either the confirmation computes and states the actual day ("Hayk will write to you on Monday"), or the promise breaks in its first week. | Confirmation copy | Unconfirmed |
| 5 | **Final legal copy** for the four legal pages, including the refund formula and its base as written in §7.6. | **BLOCKING** the bank submission | Owner + counsel |
| 6 | **Legal read on two points:** the consent checkbox wording, and messaging the Yerevan local contact who never contacted us. | The consultation form and the notification matrix | Owner + counsel |
| 7 | **Ratification of the Family Circle permission matrix values** as written in §7.6. | Portal build | Owner |
| 8 | **Armenian display names for four products** — `Էքսպրես խնամք`, `Օպտիմալ խնամք`, `Մաքսիմում խնամք`, `Հատուկ խնամք`, including whether `խնամք` stays. Only `Զննում` is confirmed by the brief; the rest are carried from a superseded price list. **Do not guess this from the old file.** | **BLOCKING** the Armenian build only | Owner or localiser |
| 9 | **Real photography from the September shoot.** Every placeholder names its replacement, ratio and pixel size, so this is a `1.x` asset swap with no component change. | All placeholders | Owner |
| 10 | **The commitment that care continues on the paid schedule while a subscription is transferred after a death.** An operational promise, not a copy decision. | The ownership-transfer flow | Owner |
| 11 | **Ratification of `#575E3B` "Deep Olive"**, or the designer's own value. It is a working value the owner adopted; it is not in the brandbook. | Nothing — one line at Layer 1 | Owner + designer |

### 14.2 Designer — brand assets

| # | Item | Blocks | Status |
|---|---|---|---|
| 12 | **A single display face covering Latin + Cyrillic + Armenian.** Until it exists, `hy` and `ru` headings fall back to the text face at 600 (§6.4 R4). Two faces is the maximum permitted split; three is refused. | Nothing — the English build proceeds | Designer + owner |
| 13 | **Three pieces of artwork we owe:** the woven-medallion divider ornament, the five-petal bullet glyph (`petal-bullet-mono.svg`), and the 16px simplified mark (`mark-simplified-mono.svg`). All derivable from the master. Fallbacks are shipped: a 1px Olive rule, a 6px Olive disc, and `mark-mono` at 16px. | The favicon at 16px is blurred until #13 lands; nothing else | Designer |
| 14 | **A colour mark that survives a Nude ground.** The hands are currently Ivory on Nude at 1.1 contrast. Today the colour mark is restricted to Anthracite and pure-white grounds. | Any colour mark on Nude | Designer |
| 15 | **The designer's own horizontal lock-up.** We ship a constructed one (§10.3) built from her artwork at her proportions; when hers arrives we swap the file and nothing else changes. | Nothing | Designer |
| 16 | **Content-cropped SVG exports.** We generate our own with `prepare.mjs`. | Nothing | Designer |
| 17 | **Whether the mobile bottom sheet's block-start corners may rise to 8px** as a single documented exception to the 2px radius. Default until answered: **2px**, with the drag handle and a 1px block-start rule carrying the sheet. | Nothing | Designer |
| 18 | **Ratification of the sixth-colour treatment** — the error terracotta `#8C3A2E` used at 2px and at 14px only, never as a fill larger than a chip. | Nothing | Designer |

### 14.3 Verification — must be run before build, and the build is safe either way

| # | Item | Owner | The rule that makes it safe |
|---|---|---|---|
| 19 | **Does Cabin contain ֏ (U+058F)?** No network access in this session; UNVERIFIED. | Igor / design system, on first CI run | §6.4 **R1** — U+058F is bound to `"MC Dram"` (Noto Sans Armenian) first in every stack, by `unicode-range` on that single codepoint. If Cabin has it the result is visually identical; if not, prices still render. `qa/glyphs.spec.ts` fails the build if the glyph is absent from the bound family. |
| 20 | **Gloock does not contain ֏.** Two reviewers found this independently; still UNVERIFIED. | same | §6.4 **R2** — the amount may be display type, but the unit `֏ AMD` is always set in the **text face on its own line**, and the dram sign is inside `.mc-currency`. No price depends on the display face for correctness. |
| 21 | **Does Gloock have tabular figures?** UNVERIFIED, and assumed by every price spec. | same | `qa/glyphs.spec.ts` asserts it. If absent, `--mc-type-price-font` falls back to the text face at 600 — one token change, zero component edits. |
| 22 | **Does Gloock cover Cyrillic?** UNVERIFIED. | same | Irrelevant to correctness: `ru` headings fall back to the text face at 600 unless the test proves coverage, in which case one token changes. |
| 23 | **Gloock has no Armenian; Cabin has no Armenian; Cabin's Cyrillic quality.** All UNVERIFIED. | same | Explicit `unicode-range` on every face plus a generic terminator on every stack means a missing glyph falls through and **never renders as tofu**. |
| 24 | **Does Noto Sans Armenian ship 400 and 600?** UNVERIFIED. | same | If 600 is absent, `heading-3` and `label` in `hy` use the 400 face with the same size and tracking; the fallback is declared in `FONTS.md` and asserted by the glyph test. |

### 14.4 Closed by the owner rulings — do not re-open

The legal entity spelling (`MemoryCare LLC`, one word) · the credit window
(60 days) · the error colour (one muted terracotta, errors only, no siblings) ·
whether the 95,000 ֏ figure is public (it is, framed as the mechanic) · the
pro-rata basis (visits, on the amount actually paid, no cap) · what a
subscription year is (12 months from signing) · the callback window (one
business day) · the report SLA (48 hours) · the deceased's name (off by
default) · the credit's attachment (to the plot) · the leading-tier wording
("Our recommendation") · auto-renew (off) · third-party analytics (none, so no
cookie banner) · reports after cancellation (readable forever) · the consent
checkbox (stays) · English product names with the Armenian in parentheses on
first mention · the radius (2px) · shadows (overlays only) · the rail size
(14px) · the breakpoints (360/600/900/1200/1440) · the display face (one, with a
fallback mechanism, never a split by script).

### 14.5 Also stale, and someone must fix it

The repository's `CLAUDE.md` still carries the **old** product table
(180,000 / 240,000 / 20,000 / 60,000, a 30-day credit, a 40,000 repeat Express,
"2 heavy + 4 light" visits, `Memory Care LLC`, and a four-language switcher).
`BRIEF.md`, `DECISIONS.md` and this file carry the current one. Nobody built to
the stale numbers — but **the next session will read `CLAUDE.md` first.** It
must be reconciled against this document before any further work begins.

---

## 15. Convergence decisions taken in this document

Every one of these was a live disagreement after round two. Each is recorded so
nobody re-litigates it and nobody has to guess who decided.

| # | The disagreement | Decision | Why |
|---|---|---|---|
| 1 | Photograph ratio: 4:3 or 3:2 | **Report photographs 4:3, 1600×1200**; comparison pairs are two stacked 4:3 frames; crew portraits 1:1; marketing section images 3:2; video 16:9 | Overruled by the design lead on evidence from the pilot checklist: the routine report is shot **by a crew member on a phone**, tripod and phone holder, geotagging on — the professional photographer with drone and camera shoots marketing only and the checklist states explicitly that the protocol report is still taken by the crew. A phone's native still ratio is 4:3, so 4:3 is the no-crop ratio for the device that actually takes these photographs, and the extra vertical extent suits an upright monument. 3:2 stays for marketing section imagery, which is what the camera shoots. |
| 2 | Radius: 2px (owner, conversion) or 0/4/8/full (visual lead's round-two softening) | **0 / 2 / full.** The 8px sheet exception is an open item, defaulting to 2 | Owner-ruled. The unused steps are deleted from the token file, not left in — an unused token gets used. |
| 3 | Header ground: Ivory (visual lead, design system) or Nude (conversion) | **Ivory**, with a permanent 1px hairline | The header is an object on the ground, not a band, so it obeys the same rule as every other raised object. The lintable rule "every full-bleed section is Nude" survives; the header is allowlisted **by name** as the single Ivory bar, and no full-bleed Ivory *band* exists anywhere. |
| 4 | Header height: 56/72 (visual lead, fold arithmetic) or 64/76 (UX, target arithmetic) | **56 / 72** | The fold is the scarcest resource on this site and 8px of hero is worth more than 8px of header. The target objection is answered by the mark being 28px at mobile, not 32: 28 + 2×14 = 56, and a 44×44 target + 2×6 = 56. Both arithmetics hold. |
| 5 | Type floor: 12 (UX), 13 (visual lead), 14 (design system) | **13px absolute floor, `overline` only. 14px informational floor. 15px `body-sm`. 16px body and inputs.** | Owner ruled the rail at 14. The rest is the smallest ladder that satisfies the iOS zoom floor, the 40–60 audience and every existing token. |
| 6 | `text-secondary` permitted from 14px or from 15px | **14px** | 4.98 passes AA at any size. Restricting to 15 was caution, not a rule. The real protection is elsewhere and is stronger: **no proof datum is ever `text-secondary`** — every rail value is `text-primary`. |
| 7 | Full-bleed Ivory "document bands" (UX wanted a token and a three-route allowlist; visual lead withdrew them) | **No full-bleed Ivory bands.** The report sheet and the calculator are Ivory objects on Nude | The author of the device withdrew it and conceded the lintable rule. An allowlisted exception is exactly the thing that breaks; the object-on-ground reading is the same idea stated more purely. |
| 8 | Crew note before or after the photographs | **After** — position 6 | Post-revision majority, and the note reads as commentary on images already seen. The reason for moving it up (the report otherwise opens as a receipt) is answered better by the GPS block at the foot of the confirmation. |
| 9 | Loading indicator: the rotating five-petal glyph (visual lead round one, adopted by the design system) or something else | **A 2px Deep Olive arc. No brand element loops.** | The visual lead withdrew the petal spinner on realising rotation of the mark is a forbidden logo use — and a spinning brand mark on a page about a grave is wrong on tone as well as on governance. |
| 10 | Error tint: a second hex `#F6E4E0` or a 10% alpha | **The alpha.** Exactly one non-brand hex enters the palette | Two hexes for one colour is how a seventh colour is born. |
| 11 | Where the CTA label splits | **`Request a consultation` (22) on every button; `Free consultation` (17) in the mobile action bar only** | One recognisable label, one bar-shaped exception. "Free" is carried by the permanent support line *"No payment now. No account needed."* and by the form heading. Buttons wrap to two lines rather than shrink the label. |
| 12 | Home-page pricing: cards or a four-line list | **A four-line list plus one link to `/pricing/`** | Duplicating the card on Home forces duplicating the two-band split, doubling the maintenance surface on the page that most needs to stay short. |
| 13 | `plot.display_mode` default: `family_name` (round one) or `none` | **`none`** | Superseded by the owner's later ruling that the deceased's name is off by default. |
| 14 | Whether the guest report gets any interactive element | **One tertiary text link → a three-field support form.** No navigation into the marketing site | The split case is the brief's central case. A dead page forces a Yerevan mother to telephone her son abroad. But one tap from a photograph of a grave to a sales bar is the failure the route exists to prevent, so the exit is support, never sales, and never a filled button. |
| 15 | `badge.label` ceiling and overflow | **Raised to 18 / 24 / 22, wrap to two lines, never ellipsis** | "Our recommendation" is 18 characters and sentence-case Armenian grows it ~25%. An ellipsised recommendation badge is worse than no badge. |
| 16 | Toast placement on the dark band, and menus opening on their own ground | **`--mc-surface-float` takes the opposite light of the band beneath it**, plus a 1px outline and the overlay shadow | Removing shadows left three floating layers undefined. This is the smallest rule that closes all three without reintroducing an elevation ladder. |

---

## 16. The five things that must never happen, restated

1. **No text on Olive, and no Olive text.** 3.08–3.42 in every direction. It is
   the single most likely production mistake in this palette, two reviewers
   reached for it independently, and it is blocked in the linter rather than in
   prose.
2. **No form on a dark band.** The error colour is 1.57 on Anthracite; a
   validation error there is invisible.
3. **No price, no CTA and no upsell anywhere near a photograph of a grave** —
   not on the guest view, not in the report PDF, not in a link preview, not in a
   notification email.
4. **No invented proof.** No testimonial, no review count, no "trusted by N
   families", no years in business, no "most chosen" — and never the claim that
   nobody else does grave care with photo reports in Yerevan.
5. **No value typed by hand.** Not a colour, not a radius, not a duration, not a
   price, not a string. If it is not in `tokens.json`, `products.json` or
   `strings.en.json`, it does not exist — and a developer who has to ask means
   this document failed.
