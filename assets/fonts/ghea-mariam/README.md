# GHEA Mariam — the display face, and it solves the dram sign

Supplied by the owner 02.09.2026 from fonter.am. Four files:
`GHEAMariamReg.otf`, `GHEAMariamRIt.otf`, `GHEAMariamBld.otf`,
`GHEAMariamBlit.otf` — Regular, Italic, Bold, Bold Italic. There is no
Medium or SemiBold, which is fine: the type ramp uses the display face at
400 only.

⚠️ **The family name is `GHEA Mariam`, with GHEA in capitals** — read from
the name table, not guessed. CSS family matching is case-insensitive so a
stack saying "Ghea Mariam" still resolves, but the `@font-face` family and
anything a person types into a font menu should use the real name.

## It contains ֏ — verified, not assumed

Read from each file's `cmap` table:

| Code point | | Reg | Italic | Bold | Bold It |
|---|---|---|---|---|---|
| **U+058F** | **֏ dram sign** | **yes** | **yes** | **yes** | **yes** |
| U+0531 | Ա Armenian capital | yes | yes | yes | yes |
| U+0561 | ա Armenian small | yes | yes | yes | yes |
| U+0410 | А Cyrillic capital | yes | yes | yes | yes |
| U+0041 | A Latin capital | yes | yes | yes | yes |
| U+20AC | € | yes | yes | yes | yes |

827 mapped glyphs in the roman, 825–826 in the italics. Latin, Cyrillic
and Armenian in one file, which is what the brandbook's typography page
claimed and what nobody had checked.

## What this closes, and what it does not

**Closes:** the display face for the whole site, in all three locales, and
the dram sign wherever a price is set in the display face. The `price` and
`price-xl` roles are GHEA Mariam 400, so **the price renders ֏ natively
with no fallback at all.**

**Does not close:** ֏ inside Montserrat text. The arithmetic line under a
price, the rail and body copy are Montserrat, and Montserrat does not have
the glyph. Those occurrences still fall back.

**So the isolated stack is still required — but we now know what to point
it at, and we already own it:**

```css
@font-face {
  font-family: "MC Dram";
  src: url("/fonts/GHEAMariamReg.woff2") format("woff2");
  unicode-range: U+058F;   /* this character and nothing else */
  font-display: swap;
}
```

Subset the file to that single glyph before shipping it — the whole face
is ~150 KB and the sign alone is a fraction of that. Then `--mc-font-dram`
resolves to a face we control, in every locale, at a cost of a couple of
kilobytes.

Note the consequence for the mismatch: ֏ drawn from GHEA Mariam beside
Montserrat digits is a *deliberate* pairing of two brand faces, not an
accidental system fallback. Check it optically at the sizes used and
adjust the sign's size or baseline in the token if it needs it.

## Convert before shipping

OTF is the source. Ship WOFF2, subset per locale, and generate fallback
metrics so the swap does not shift layout.
