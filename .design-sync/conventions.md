## Building with MONTEC

MONTEC is a **dark-first, quiet-luxury** system. Near-black ground, one brass
accent, serif for display and sans for information. Restraint is the brand: no
second accent colour, no loud CTA, no exclamation marks.

### 1. Wrap everything in `<Surface>` — this is not optional

`Typography`, `Button`'s `primary`/`ghost` variants and `Logo variant="reversed"`
all render in Warm Paper (`#FAF8F3`). **On a white page they are invisible.**
`Surface` supplies the ground and the matching text colour, so components never
depend on an ambient body style the host app may not have.

```jsx
<Surface tone="obsidian">…</Surface>   // default: near-black ground, paper text
<Surface tone="anthracite">…</Surface> // mid-tone panel ground
<Surface tone="paper">…</Surface>      // warm off-white ground, near-black text
```

Props: `tone` (above, default `"obsidian"`), `padding` (number, default `32`).
Pair the tone with the variant: `paper` + `Logo variant="primary"`, `obsidian` +
`Logo variant="reversed"` and any `Typography`. `Surface` ships in the bundle
(`window.MontecDesignSystem.Surface`) without its own component card.

### 2. Styling idiom: token objects + inline styles — there are NO utility classes

This library does **not** ship a utility-class vocabulary. The stylesheet
contains only a CSS reset, the `@font-face` rules and a `body` default — there is
no `bg-obsidian`, no `text-body`, no spacing scale to compose with. Never write
class names for MONTEC styling; they will not resolve. Instead import the token
objects and style inline (that is exactly how the library's own components are
built):

```jsx
import { colors, fontFamilies, typeScale, line } from '@montec/design-system'
```

- `colors` — `obsidian` `brass` `brassSoft` `anthracite` `anthraciteDeep` `paper`
  `paper2` `grey` `brassWash` `obsidianWash`
- `fontFamilies` — `serif` `sans` `serifArmenian` `sansArmenian`
- `line` — the brass hairline rule used for dividers and card borders
- `typeScale` — the six levels, with the sizes `Typography` renders

**Colour discipline:** Brass is the *only* accent and should stay around 6% of a
composition — hardware, rules, one emphasised word. Reach for `anthracite` for
panels before you reach for brass.

### 3. Components

- `<Typography variant="display|h2|lead|eyebrow|body|caption" lang="en|hy" as?>` —
  the whole type hierarchy. Serif carries headlines and product names; sans
  carries body and interface. Never swap them. Armenian copy **must** pass
  `lang="hy"` — the Latin faces have no Armenian glyphs and will silently fall
  back.
- `<Button variant="primary|secondary|ghost" size="default|small">` — there is
  deliberately no sale/urgent/destructive variant ("no discounts, ever"). If a
  design seems to need one, the design is off-brand.
- `<Logo variant="primary|reversed|monochrome-dark|monochrome-light|avatar"
  withWordmark size>` and `<Monogram size>` — the mark renders in one colour via
  `currentColor`; never gradient-fill or recolour it.

### 4. Where the truth lives

Read `styles.css` and its imports for the real tokens and font faces, and each
component's `.d.ts` (exact prop unions) and `.prompt.md` (usage) before styling.
Those files are authoritative; this summary is not.

### 5. Idiomatic example

```jsx
<Surface tone="obsidian">
  <div style={{ display: 'flex', flexDirection: 'column', gap: 24, maxWidth: 640 }}>
    <Typography variant="eyebrow">01 / 13 — Weekender</Typography>
    <Typography variant="h2">The Founder</Typography>
    <Typography variant="body">
      A vessel for those who write history, not just participate in it.
    </Typography>
    <div style={{ borderTop: `1px solid ${line}`, paddingTop: 20 }}>
      <Button variant="primary">REQUEST ACCESS</Button>
    </div>
  </div>
</Surface>
```
