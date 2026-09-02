# Fonts — what is here, verified by reading each file

Every claim below comes from reading the font's `cmap` table, not from a
specimen or a brandbook page.

| File | Family | Glyphs | Latin | Cyrillic | Armenian | ֏ U+058F |
|---|---|---|---|---|---|---|
| `GHEAMariamReg/RIt/Bld/Blit.woff2` | GHEA Mariam | 827 | yes | yes | yes | **yes** |
| `Montserrat-var.woff2` | Montserrat, wght 100–900 | 1312 | yes | yes | **no** | **no** |
| `NotoSansArmenian-var.woff2` | Noto Sans Armenian | 430 | yes | no | yes | **yes** |
| `mc-dram.woff2` | GHEA Mariam, subset | 1 | — | — | — | **yes** |

`mc-dram.woff2` is **684 bytes** — GHEA Mariam Regular subset to U+058F
alone. It is what the isolated `unicode-range` slice loads, so ֏ inside a
Montserrat run is drawn by a face we control instead of by whatever the
operating system happens to have.

---

## ⚠️ The brandbook names a font that does not exist

The typography page shows the text face as **Montserrat**, with an
Armenian sample labelled **"Montserrat Arm"**. Both halves of that are a
problem.

**Montserrat has no Armenian and no dram sign.** Read from the Google
Fonts variable file: 1,312 glyphs, Latin and Cyrillic, `Ա` absent, `֏`
absent. So the brandbook's own claim that the pair covers Latin, Cyrillic
and Armenian is true of GHEA Mariam and **false of Montserrat**.

**"Montserrat Armenian" is not a published family.** Queried against the
Google Fonts API directly: `Noto Sans Armenian` exists, `Noto Serif
Armenian` exists, `Montserrat Armenian` returns nothing. Either Mariam
holds a licensed or custom file under that name, or the Armenian sample on
that page was set in a different face and labelled Montserrat.

**This is a question for the designer, not something to solve by
substitution.** → Mariam: which file is "Montserrat Arm", and can we have
it?

## What we build with until she answers

**Noto Sans Armenian** is the documented stand-in for Armenian body text.
It is a real, licensable, Armenian-designed face; it carries ֏; and at
21 KB it costs almost nothing. It is **not** a match for Montserrat's
proportions and it is not presented as one — it is named as a stand-in in
the CSS and in this file so nobody mistakes it for the specification.

The font stack therefore resolves per locale:

- **en / ru** — Montserrat, with `mc-dram` for ֏.
- **am** — Noto Sans Armenian for Armenian text, Montserrat for Latin
  fragments, `mc-dram` for ֏. Replace the first of those the day Mariam
  supplies the real file.

## Conversion

OTF and TTF sources were converted to WOFF2 with fontTools. The GHEA
Mariam originals are in `assets/fonts/ghea-mariam/`. Nothing here is
hinted or otherwise modified beyond the format change and, for
`mc-dram`, the subset.
