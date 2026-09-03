# The Figma file

**https://www.figma.com/design/KwXpkKa8Ck6qEt9hy0xfQF**

Six pages:

| Page | What is on it |
|---|---|
| **00 · Cover** | What the file is, and what it is not. |
| **01 · Foundations** | The seven brand colours with their measured contrast, the full contrast matrix, and the sixteen type roles. |
| **02 · Components** | Button (8 variants), the tariff card, the dram sign as a vector, and the site footer. |
| **03 · Screens — Public** | 16 routes at 1440, English. |
| **04 · Screens — Account** | 10 routes at 1440, English. |
| **05 · Handover** | What the owner settled on 03.09, and what is still open. |

## The screens are generated, not drawn

`extract.py` reads a paint tree from the built pages — the same DOM the
screenshots are taken from — and `pack-for-figma.py` compacts it into the rows
the Figma builder reads. So a screen in Figma cannot drift from the code: it
is regenerated from it.

Each screen is real Figma layers — text nodes with the real strings, fills
bound to the primitive colour variables — not a flattened image. The footer is
a component instanced on all 26 screens, exactly as it is a shared include in
the build. The header stays inline per screen because it carries the
current-page marker, which one component would lose.

## Three things the file cannot show

**The dram sign ֏ renders as nothing** in Figma — no installed font draws
U+058F — so every price in the screens reads without its currency. Use the
`Currency / Dram ֏` component wherever a price is set by hand; the screens
themselves are correct in the HTML and in the screenshots.

**Armenian renders as nothing** for the same reason, so the Armenian locale
lives only in the build and its 290 screenshots. Ruled by the owner 03.09.

**The display face is a stand-in.** GHEA Mariam is not installed here, so the
display roles are set in EB Garamond so proportions read correctly. Every
display text style says so in its description.

## The [BLOCKED] notes are not a mistake

`mission`, `values` and `history` carry a visible note saying they are built
from strings approved for other pages and need their own copy. That is true,
it is the content lead's open work, and it is left visible on purpose.
