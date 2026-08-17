# Nairi cost-recovery invoice — generator

Builds the invoice and its covering letter as a two-page A4 PDF.

```bash
python3 build.py                 # draft: requisites render as visible red blanks
python3 build.py --final         # final: blanks disappear, so fill them in first
node render.mjs nairi-invoice-draft
```

Amounts live in `CHARGED` / `NOT_CHARGED` at the top of `build.py` and mirror
`montec/docs/nairi-cost-recovery.md` — that file is the record of what the owner
confirmed, this one only renders it. Change the ledger first, then the script.

Fonts are embedded from `montec/site/public/fonts`. Note the third face: neither
Cormorant Garamond nor Inter has a glyph for ֏ (U+058F), so Noto Sans Armenian is
loaded scoped to the Armenian block only. Remove it and every dram sign in the
document silently turns into the wrong letter.

`render.mjs` prints through headless Chromium at exactly 210×297 mm. The invoice
page is a fixed-height flex column: content that overflows is clipped, not
paginated, so after any edit re-render and look at the last page before sending.
