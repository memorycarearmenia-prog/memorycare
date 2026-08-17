# Nairi cost-recovery invoice — generator

Builds the invoice and its covering letter as a two-page A4 PDF.

```bash
python3 build.py                 # English draft
python3 build.py --hy            # Armenian draft
python3 build.py --final         # blanks disappear, so fill the requisites in first
node render.mjs nairi-invoice-en-draft
node render.mjs nairi-invoice-hy-draft
```

**Who each edition is for.** The English edition (invoice + covering letter) goes
to Nairi. The Armenian edition is the working copy for the bookkeeper, so it is
the invoice alone — a covering letter is for the client, not for accounting. Pass
`--letter` to include it anyway, if the Armenian is also sent to the client.

Both editions carry the same amounts and the same structure.
The Armenian strings live in `hy.py` and are **not native-verified** — Armenian
invoice wording is largely conventional, so the owner's bookkeeper should read
the document name, the party labels and the payment-term line before it is sent.

Amounts live in `CHARGED` / `NOT_CHARGED` at the top of `build.py` and mirror
`montec/docs/nairi-cost-recovery.md` — that file is the record of what the owner
confirmed, this one only renders it. Change the ledger first, then the script.

Fonts are embedded from `montec/site/public/fonts`, one stack for both languages:
Latin resolves to Cormorant/Inter, Armenian falls through to the Noto Armenian
faces. Those faces also supply ֏ (U+058F) — neither brand face has that glyph, so
remove them and every dram sign turns into the wrong letter, in the English
edition too.

The Armenian edition is set a notch tighter (8.5 pt against 9 pt, tighter rows and
label tracking) because the same content runs about a fifth longer in Armenian and
the page has no room to spare.

`render.mjs` prints through headless Chromium at exactly 210×297 mm. The invoice
page is a fixed-height flex column: content that overflows is clipped, not
paginated, so after any edit re-render and look at the last page before sending.
