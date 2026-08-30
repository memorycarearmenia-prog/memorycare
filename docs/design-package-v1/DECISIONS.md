# Owner decisions — binding, 29.08.2026

These override anything in the individual proposals. The owner (Hayk,
CBDO) ruled on each personally.

## 1. Legal entity name

**`MemoryCare LLC` — one word, exactly as the brand.**

Use this spelling everywhere: footer, offer, invoices, receipts, legal
pages, bank package, meta tags. The earlier "Memory Care LLC" spelling in
the project memory is superseded. Brand name in running text remains
**MemoryCare**, one word, two capitals.

## 2. Functional colour — one, and only one

**A single muted red is added, for errors only.** Terracotta in the
spirit of the palette, e.g. `#8C3A2E`, used exclusively in form
validation and payment failure.

- Success and warning are expressed typographically — wording, glyph,
  rule weight. No green. No amber.
- The reasoning: an error with no colour gets missed, and a missed error
  in this product is an unfinished payment.
- This is the **sixth** colour and the last one. Nothing else is added.
  Anyone proposing a seventh is wrong.

Token name must make the restriction obvious, e.g.
`--mc-color-feedback-error` with no sibling `-success` / `-warning`.

## 3. First-year price with the credit — show it

**160,000 − 65,000 = 95,000 ֏ for the first year** is shown publicly, in
the calculator and on the pricing page.

- It is honest arithmetic derived from our own credit rule, not a
  discount, and must never be worded as one. No "save", no strike-through
  on 160,000, no "special offer".
- Frame it as the mechanic: an Express visit already paid for is credited
  in full when the annual subscription is signed within 60 days.
- Do not put it in the hero and do not put it on the Express card as the
  headline price — Express is a real product at 65,000, not a lead-in.

## 4. Reminders of constraints already settled

- **Credit window is 60 days**, not 30. The 30-day figure in the older
  pricing table is stale. One credit only: either Inspection *or*
  Express, never both, and only at the moment the annual subscription is
  signed.
- **Scope is the marketing site *and* the client portal.**
- **Text face: Cabin**, labelled everywhere as a substitute for Gill Sans
  (commercial, unlicensed for web). Display face: Gloock Regular.
- **Photography: neutral branded placeholders**, each labelled with the
  shot that replaces it after the September pilot, with exact ratio and
  crop.
- **Legal address: visible placeholder** plus an entry in the open-items
  list. Not yet supplied.

## 5. Open technical item — verify before build

Does **Cabin** contain the Armenian dram glyph **֏** (U+058F)? If not,
prices break. If missing, specify a fallback face for the currency glyph
only, and state it in the type spec. This session has no network access
to check; it must be verified.
