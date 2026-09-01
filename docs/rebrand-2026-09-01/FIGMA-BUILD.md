# Figma build — what is in the file, and what the build discovered

File `m1sxpu4Zxf8ANLre4FETOl`, page **06 · Rebrand — 1440**.

## Built

**Foundations.** 41 colour variables across a Light and a Dark mode:
18 primitives (the five brandbook colours plus the derived ramp) and 23
semantics, each aliased per mode. 32 text styles — a Desktop and a Mobile
ramp of 16 each. The old ramp is renamed `zz RETIRED/*` with a note, not
deleted, so nothing loses its style before the screens are rebuilt.

**Screens.** Header with the visible descriptor slot, hero, and the
tariffs section with the year rail.

## What the build found — four things no proposal could have known

### 1. The tripwire fired, and it caught me rather than a misuse

`decor/sky-tint-on-dark` was defined as unset in the Light mode with a
magenta guard. I then used it for the report seal on the Ivory sheet and
the seal came out magenta.

The guard was right to fire and the token was wrong. The brief permits
Sky blue as a **tint fill** on light — "a panel, a chip ground, the
medallion" — and forbids it only as type. The system proposal collapsed
fill and type into one dark-only token. Split into:

- `decor/sky-tint` — a fill, legal in both modes, never carries text.
- `text/eyebrow-on-dark` — type, still unset on light, where Sky is 1.26.

Worth recording that the mechanism worked exactly as designed: a silent
wrong colour became a loud one, in the file, in under a minute.

### 2. ֏ (U+058F) renders in none of the faces available

Tested at 64px in **Source Serif 4, Montserrat, Noto Sans and Noto
Serif** — the probe strip is on the canvas beside the page. Every one
drops the glyph and leaves a blank. The tariff cards therefore read
`AMD` rather than faking a symbol we do not have.

This has been carried as "unverified" since 29.08. It is now verified in
the negative, and it is not a Figma quirk: the live site already shows
the same symbol falling back to a system face, rendering at a different
weight and size from the digits beside it. The price is the most
important string on the site.

**Consequence:** the isolated font stack scoped to `unicode-range:
U+058F` is mandatory, not an optimisation, and somebody has to source a
face that actually contains the glyph. Montserrat Arm is the likely
carrier and is itself unverified. Until then, no price on this site is
typeset.

### 3. The medallion has a minimum size, and now we know it

Rendered from the delivered vector at 240px it is a clean woven
interlace. At **48px it still reads**; below that the filled outlines
begin to close up, because the interlace was drawn as filled shapes
rather than centrelines. 48px is therefore the floor for the seal, and
this is the first concrete number for the minimum-size rule the
brandbook does not contain.

### 4. Ghea Mariam is absent, and so is every Armenian-capable serif

Checked against all 8,927 families the file can reach. Montserrat is
present in every weight. The display face in the Figma file is
**Source Serif 4, a documented stand-in**, named in every text style's
description so nobody mistakes it for the specification. The built site
uses Ghea Mariam.

## Two structural rules applied, both previously learned the hard way

**Cards in a row are equal height, always.** The row is fixed to its
tallest child, every card fills it, and the button is pushed to the foot
by a growing spacer rather than by hand-tuned padding — so the alignment
survives a copy change instead of depending on three descriptions
happening to be the same length.

**A card without a badge reserves the badge's height.** 46px in all
three cards. Without it the three titles sit at different heights and
the row reads as an accident.

## The year rail works

Twelve cells, one per month, the same component in every card. Optimal's
four marks land one per season group, so *"four full visits, one in each
season"* is drawn rather than claimed. Every mark is Olive — 3.12 on
Nude, clearing the 3:1 non-text floor with almost no margin — and
therefore also carries a 1px Deep Olive outline at 5.49, with the visit
count printed as a numeral in the same card. Colour is never the sole
carrier of the information.

## Not yet built

Sections 2–4 and 6–12 at 1440, the whole 360 breakpoint, the portal, and
the six routes the bank requires. The entry rail for Զննում, the credit
block and the Special card with its calculator are specified in
`PROPOSAL-ux.md` §3 and not yet drawn.
