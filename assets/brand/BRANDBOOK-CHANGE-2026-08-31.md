# Brandbook update, 31.08.2026 — what changed and what it breaks

The designer delivered a new `MemoryCare_brandbook.pdf` (4 pages: Logo,
Colors, Typography) plus two 4500² lock-up files. Confirmed as the latest
by delivery date. It **supersedes the 29.08 brandbook**, which is kept at
`brandbook/archive/MemoryCare_brandbook_2026-08-29_SUPERSEDED.pdf` for
reference only.

Everything below was read out of the PDF itself, not inferred.

---

## 1. Colours

| Name | HEX | CMYK | Status |
|---|---|---|---|
| Dark Olive | `#212212` | 67 / 60 / 79 / 76 | **new — replaces Anthracite** |
| Olive | `#7C8654` | 52 / 34 / 78 / 12 | unchanged |
| Nude | `#EFE5D5` | 6 / 8 / 15 / 0 | unchanged |
| Ivory white | `#F3F0E9` | 3 / 3 / 7 / 0 | unchanged |
| Sky blue | `#D4ECF9` | 17 / 0 / 0 / 0 | **new** |

**Anthracite `#33373C` is gone.** It appears nowhere in the new book. The
dark is now a warm near-black olive.

**Sky blue is new** and has two jobs in the book: the woven medallion at
the centre of the forget-me-not, and the tagline under the wordmark.

Do not pixel-sample the JPEG lock-up — it returns `#14180C` and `#6B9532`,
neither of which is a brand colour. The same mistake produced the bad
27.08 values. The PDF's stated codes are the only source.

## 2. Contrast, measured

| Pair | Ratio | |
|---|---|---|
| Dark Olive on Nude | 12.93 | pass |
| Dark Olive on Ivory | 14.17 | pass |
| Dark Olive on Sky blue | 13.18 | pass |
| Nude on Dark Olive | 12.93 | pass |
| Ivory on Dark Olive | 14.17 | pass |
| Sky blue on Dark Olive | 13.18 | pass |
| Deep Olive `#575E3B` on Nude | 5.49 | pass |
| Deep Olive on Ivory | 6.01 | pass |
| Error `#8C3A2E` on Nude | 6.10 | pass |
| Error on Ivory | 6.69 | pass |
| Olive on Nude | 3.12 | fails |
| Olive on Ivory | 3.42 | fails |
| Olive on Sky blue | 3.18 | fails |
| Olive on Dark Olive | 4.14 | fails for text, clears AA-large |
| Sky blue on Nude | 1.02 | invisible |
| Sky blue on Ivory | 1.07 | invisible |
| Deep Olive on Dark Olive | 2.36 | never |
| Error on Dark Olive | 2.12 | invisible |

Three rules follow:

1. **Olive still never carries or receives text.** Unchanged from before.
2. **Sky blue is a dark-ground colour.** It is excellent type on Dark
   Olive and invisible on Nude or Ivory, where it may only be a tint fill.
3. **The consultation form still may never sit inside a dark band** — the
   error colour is invisible there. This rule survives the palette change
   intact.

**Deep Olive `#575E3B` survives** as the sixth, interface-only working
value. On light grounds the body text is Dark Olive and Olive fails, so
nothing in the brandbook can distinguish a link from body text. Deep
Olive does, at 5.49 / 6.01.

**One simplification the new palette allows:** the primary button on light
grounds becomes **Dark Olive fill + Ivory label** (14.17) instead of Deep
Olive fill + Ivory label (6.01). That is an official colour doing the most
prominent job, and it leaves Deep Olive responsible for link and accent
text only.

## 3. Typography — both blocking problems are solved

| Role | Was (29.08) | Now |
|---|---|---|
| Display | Gloock | **Ghea Mariam** |
| Text | Gill Sans | **Montserrat** (Armenian: **Montserrat Arm**) |

The 29.08 book raised two blockers: Gill Sans is a commercial Monotype
face needing separate web, app and PDF licences, and neither face covered
Armenian — the primary market. **Both are resolved.** The new book shows
each family in Latin, Cyrillic and Armenian (Aa / Аа / Աա). Type tokens
can now be built, which they could not be a week ago.

Note that the Armenian Montserrat is a **separate family**, labelled
"Montserrat Arm" in the book. The font stack must name it; it is not a
subset of the Latin family.

Unverified here, no outbound network: whether either family carries
**֏ (U+058F)**. Montserrat Arm is the likely carrier. The currency symbol
stays its own element with its own font stack either way.

## 4. The mark

Two open hands in Nude cradling a five-petal forget-me-not in Olive, its
centre a **woven interlaced medallion drawn as open line-work in Sky
blue** — not a filled disc, and not the cream centre of the 29.08 book.

Four lock-ups: primary logo, logo mark alone, wordmark alone, and two
monochrome versions (all-dark on Nude, all-Nude on dark).

**The wordmark is single-colour Olive.** The 29.08 two-colour rule
("Memory" Ivory + "Care" Olive) is retired — it holds in no lock-up in the
new book.

The tagline carries **no full stop**. That rule stands.

## 5. What now needs rebuilding

Every one of these embeds `#33373C`, Gloock, Gill Sans, or the
two-colour wordmark:

- [ ] The Figma file `m1sxpu4Zxf8ANLre4FETOl` — 23 colour variables and
      13 text styles, then every screen that uses the Anthracite band
- [ ] `docs/design-package-v1/FINAL-UI.md`, `FINAL-SYSTEM.md`,
      `FINAL-UX.md`, `FINAL-CONTENT.md`
- [ ] `docs/design-package-v1/LEAD-REVIEW.md` §1 contrast table
- [ ] All six prompts in `docs/` handed to other AIs
      (`PROMPT-BUILD-DESIGN-SYSTEM`, `PROMPT-BUILD-WEBSITE`,
      `PROMPT-REVIEW-AND-HANDOVER`, `PROMPT-VISUAL-POLISH-AND-MOTION`,
      `PROMPT-AUDIT-AND-CAPTURE`, `PROMPT-MODERN-DESIGN-SYSTEM`)
- [ ] The design-system kit already delivered
- [ ] `index.html`
- [ ] The report PDF template
- [ ] The LinkedIn banner and avatar
- [ ] `docs/DESIGNER-BRIEF-MARIAM.md` and
      `docs/LETTER-MARIAM-BRANDBOOK.md` — several of the questions they
      ask have now been answered by this delivery and should not be sent
      as written

## 6. Still missing from the brandbook

Unchanged from the 29.08 list, none of it supplied here:

- Vector source for the new mark (AI / SVG / EPS). Only raster lock-ups
  arrived — `01-primary-on-dark-4500.jpg` and `02-primary-on-light.png`.
- Clear-space and minimum-size rules.
- Misuse page (what may not be done to the mark).
- Favicon and app-icon crops of the medallion at 16, 32, 180, 512.
- Licence confirmation for Ghea Mariam and Montserrat Arm, and the
  ֏ glyph check.
