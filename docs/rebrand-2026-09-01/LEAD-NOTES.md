# Design lead — running notes

## Figma foundation, done 01.09 while the five proposals were being written

File `m1sxpu4Zxf8ANLre4FETOl`. Six pages: Cover, Foundations, Components,
Site 360, Site 1440, Portal 360.

**Primitives updated to the 31.08 brandbook.** Added `primitive/dark-olive`
`#212212` and `primitive/sky` `#A4D6E8`. Repointed the three semantics that
still aliased the retired Anthracite — `surface/dark`, `text/primary` and
`action/label-on-dark` — onto Dark Olive. `primitive/anthracite` is now
orphaned; it will be deleted once the screens are rebuilt, not before, so
nothing silently loses its fill.

This much was mechanical: Anthracite no longer exists, so it had to move
regardless of what anyone proposes. Semantic naming and the type ramp are
held until the system proposal lands — they are contested and belong to
the convergence, not to me pre-empting it.

**Two primitives are now wrong and await a ruling.** `primitive/secondary`
is `#606161`, a cool grey chosen against Anthracite; beside the warm
`#212212` it reads dirty. `primitive/border` is `#D8D0BC`. Both need
re-deriving from the new palette.

## ⚠️ Ghea Mariam is not available in Figma

Checked against all 8,927 families the file can reach. **Montserrat is
present** in every weight, so the text face is real and the Armenian
sibling can be named in the stack at build time. **Ghea Mariam is absent**,
and so is every Armenian-capable serif — the only family matching
/armenian/ at all is `Charm`, which is a Thai display face.

Consequences:

1. The Figma file cannot show the real display face. It needs a documented
   stand-in, named so nobody mistakes it for the specification. Closest
   available in colour, contrast and proportion: **Source Serif 4**.
   Alternatives considered: Spectral (more contrast than Ghea Mariam),
   Literata (wider), Gloock (a high-contrast display face, and the one we
   just retired — using it again would invite confusion).
2. This is a Figma limitation only. The built site uses Ghea Mariam.
3. Armenian still does not render in Figma at all, so the screens stay
   English. That was already true and is unchanged.

## Open, for the convergence

- Sky blue `#A4D6E8` vs the brandbook's printed `#D4ECF9` — unresolved by
  the designer. Everything must be built so the swap is one token.
- `text/secondary` needs a value that is distinguishable from both
  `text/primary` (Dark Olive) and `text/accent` (Deep Olive `#575E3B`).
  Measured options on Nude: `#464B2F` 7.30, `#515837` 6.01, `#5D643F` 5.01.
  A warm neutral rather than a fourth olive may serve better — a system
  question, not a colour-picking one.
- `border/hairline` on Nude: `#BBC0A5` measures 1.50, `#C4C9B1` 1.36.
