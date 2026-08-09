# @montec/design-system

The MONTEC brand, as code. A React + TypeScript + Tailwind component
library generated from the Brand Book / Brand Guide
(`montec/docs/planning/Montec_Brand_Book.html`,
`Montec_Brand_Guide.pdf`) — same tokens, same rules, same components,
now usable in an actual product instead of only described in a PDF.

Source of truth for every brand fact encoded here is
`montec/CLAUDE.md` and the Brand Book/Guide. If this package and those
documents ever disagree, the documents win — fix the code, not the docs.

## Scope (first pass — MVP, 2026-08-09)

This is deliberately **not** the full brand system yet. It covers:

- **Tokens** (`src/tokens/`) — colours (primary + secondary/tint palette)
  and typography (font families, the six-level type scale, Armenian/
  Cyrillic companion faces).
- **`<Logo />`** — the wordmark + monogram lockup, all five documented
  variants (primary, reversed, monochrome-dark/light, avatar).
- **`<Typography />`** — the six-level type hierarchy as one component,
  with an `lang="hy"` prop for the Armenian companion faces.
- **`<Button />`** — primary/secondary/ghost, matching the Old-Money
  Code's "no discounts, no urgency" voice rules (no sale/urgent variant
  exists on purpose).

**Not yet built** (Brand Guide Sections 07–11 — product card, THE AUDIT
spec table, SKU/pricing table, and the stationary suite: business card,
letterhead, batch/authenticity card, pitch-deck cover, social post
template): scoped out of this pass by explicit user decision, next in
line when this package's scope is revisited.

## Install & use

```bash
npm install
npm run build          # → dist/ (ESM + CJS + .d.ts + styles.css)
npm run storybook       # → visual dev/preview at localhost:6006
npm run build-storybook # → static Storybook export
```

```tsx
import { Logo, Typography, Button, colors } from '@montec/design-system'
import '@montec/design-system/styles.css'

function ProductPage() {
  return (
    <div style={{ background: colors.obsidian }}>
      <Logo variant="reversed" size={36} />
      <Typography variant="eyebrow">01 / 13 — Weekender</Typography>
      <Typography variant="h2">The Founder</Typography>
      <Button variant="primary">REQUEST ACCESS</Button>
    </div>
  )
}
```

## Conventions an agent (or a new engineer) should know

- **Colour discipline**: Brass is the *one* accent (≈6% of visual
  weight). Never add a second accent hue to `tokens/colors.ts` without
  updating the Brand Book/Guide first — the ratio guide there is load-
  bearing brand law, not a suggestion.
- **Typography pairing**: `serif` (Cormorant Garamond) carries emotion/
  headlines/product names; `sans` (Inter) carries information/body
  copy. Never swap them. Armenian copy needs `lang="hy"` on
  `<Typography>` (or the `serif-hy`/`sans-hy` Tailwind font families
  directly) — Cormorant Garamond and Inter have no Armenian glyphs.
- **The monogram is one colour, always** (`currentColor` on `<Monogram
  />`) — no gradients, no multi-colour fills. This is the same rule
  that governs blind-emboss branding on the physical product: tone-on-
  tone only.
- **No "loud" button.** `<Button>` intentionally has no destructive/
  warning/sale variant. If a design calls for one, that's a signal the
  design is off-brand, not a missing prop.

## Why this exists

Built so the MONTEC brand can eventually be synced to Claude Design
(`claude.ai/design`) as a real design system — the design agent there
builds with a repo's actual compiled components, not generic ones. This
package is the prerequisite: a buildable `dist/`, Tailwind-preset
tokens, and Storybook stories are exactly the shape that sync tooling
consumes. Syncing it is a separate, later step — this pass only builds
and verifies the package itself.
