# Logo v6 — the 31.08.2026 brandbook mark

Source of truth for the mark. Everything in `../logo-final/` and `../logo/`
is historical.

## Fills, read out of the vector files (not sampled)

| Class | Value | What it paints |
|---|---|---|
| `.cls-1` | `#7c8654` Olive | petals, wordmark glyphs |
| `.cls-2` | `#efe5d5` Nude | hands |
| `.cls-3` | **`#a4d6e8`** | woven medallion, tagline |

Monochrome variants are the same geometry with one fill:
`_light` = `#efe5d5` (for dark grounds), `_dark` = `#212212` (for light).

## ⚠️ The Sky-blue conflict — unresolved, needs Mariam

The brandbook's colour page declares **Sky blue `#D4ECF9`**. Every piece of
delivered artwork — all nine SVGs, the PNGs, the JPGs and the PDFs — uses
**`#A4D6E8`** instead. These are visibly different blues; `#A4D6E8` is
noticeably deeper.

Verified three ways: the vector `<style>` blocks state `#a4d6e8`; the
brandbook's own logo page (page 2) renders the medallion as `#A4D6E8`;
the colour page (page 3) renders its swatch as `#CEEDFA`, matching its
printed `#D4ECF9`. So **the book contradicts itself** — its palette page
does not describe its own logo page.

Both clear WCAG on the dark ground (`#D4ECF9` 13.18, `#A4D6E8` 10.26) and
both are invisible on Nude and Ivory, so this is not an accessibility
question — it is a question of which blue the brand actually is.

**Working decision until Mariam rules:** use `#A4D6E8`. It is what the
artwork physically contains, it cannot be changed without re-exporting
twelve files, and building the interface on `#D4ECF9` would put two
different blues side by side the moment a Sky-blue eyebrow sits next to
the logo. Ask her to correct the colour page; if she prefers `#D4ECF9`,
she must re-export the lock-ups.

## Files here

| File | Origin |
|---|---|
| `01-primary-on-dark-4500.jpg` | delivered raster, 4500² |
| `02-primary-on-light.png` | delivered raster, 4500² |
| `svg/MemoryCare_logo-mark_color.svg` | delivered vector, verbatim |
| `svg/MemoryCare_logo-mark_light.svg` | **derived** — the colour file recoloured to a single `#efe5d5` fill |
| `svg/MemoryCare_logo-mark_dark.svg` | **derived** — the same, recoloured to `#212212` |

The derived files were made because re-downloading each variant is
expensive; the designer's own exports have identical path geometry (checked
against `MemoryCare_logo mark_light.svg`) and differ only in collapsing the
three style classes into one. Prefer her originals when you can fetch them.

## The full delivered set — Google Drive

Folder: https://drive.google.com/drive/folders/1apRhTrj1gzV6ZGJgCfI5fzUqgtCx_N7j

Three lock-ups × three treatments, each as SVG, PNG, JPG, plus PDF for the
primary logo:

- **Primary logo** (mark + wordmark + tagline) — color / light / dark
- **Logo mark** (mark alone) — color / light / dark
- **Wordmark** (type alone) — color / light / dark

Vector file IDs, for direct fetch:

| File | ID |
|---|---|
| primary logo_color 2.svg | `1U8hM7dBjR5cVX-djIvmkSke0DVC6QisP` |
| primary logo_light 2.svg | `1OcZWwSrQvWNI8r7PKE6qKVENS9TE5vkr` |
| primary logo_dark 2.svg | `1z1KEeR8xn_vlAfWnY13wvpLmq1xhzwVG` |
| logo mark_color.svg | `1yjXqAMfTquuvAV72WYww4NY68VP26cGP` |
| logo mark_light.svg | `18Gq8MQ1U_V4QKGgynkve0dFv-Egnqtgr` |
| logo mark_dark.svg | `1B4DHn2VkrFvevlh1yekNmgtbb620NKGu` |
| wordmark_color 2.svg | `1IshDsr8tS9xoTH02fRiApKKvo3lW833w` |
| wordmark_light 2.svg | `1K_TKgpeFlTE0YgzIj9scqYEC-pt7u3AE` |
| wordmark_dark 2.svg | `1tq-6rnlaU1naE3V1UH6Gh7Rr83QRgX0m` |

The `MemoryCare brandbook.pdf` in that folder (`16hTQXOwokSCzrRhZIdfucGTrBVgmx7fp`)
is byte-identical in size to the copy at
`../brandbook/MemoryCare_brandbook.pdf`.

## Still missing

The vectors close the biggest gap, but the brandbook still has no
clear-space rule, no minimum size, no misuse page, and no favicon or
app-icon crop of the medallion at 16 / 32 / 180 / 512.
