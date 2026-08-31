# Review of `UIUX_design.zip` — what must change

**31.08.2026.** An independent pass over the delivered prototype and its bound
design system, checked against the specification package, the owner decisions
and the verification protocol. Nothing below is an impression: every finding
carries a file, a line or a measured number.

**Overall.** The work is honest and unusually disciplined. The token layering is
real, the three-layer rule is enforced, the dark scope is a class and not a
media query, the forbidden-word list is clean, the prices are correct, the two
service promises are identical in all four of their occurrences, the brand name
never appears as two words, and the delivered `review/FINDINGS.md` reports its
own failures instead of hiding them — including the ones that reflect badly on
it. That is rare and worth saying before the list of defects.

The defects below are real and most are cheap to fix.

---

## Blockers

### B1 · The page has no `lang` attribute at all

**Where** `MemoryCare Prototype.dc.html` — `<html>` with no attributes.
**Evidence** `grep -o '<html[^>]*>'` returns `<html>`.
**Expected** A trilingual product declares its language on the root element.
**Why it matters** Three consequences, all real. A screen reader announces
Armenian and Russian in an English voice. Search engines cannot tell the
locales apart. And the design system's own `:lang(hy)` rule — the one that
disables uppercase in Armenian, `tokens/scopes.css:112` — **can never fire**,
so Armenian will be set in capitals, which the specification forbids.
**Fix** `<html lang="en">`, switched per locale. In production this is
`params.locale`.

### B2 · The display font stack has no Armenian face

**Where** `tokens/primitive.css:71`
`--mc-font-display:"MC Dram","Gloock",Georgia,serif;`
**Evidence** No Armenian-capable family in the stack. Georgia carries no
Armenian.
**Why it matters** Every Armenian heading and every Armenian price falls back to
a generic serif. The text stack was built correctly — it carries Noto Sans
Armenian — but the display stack was not, and headings are exactly where the
brand is most visible. Armenian is the primary market.
**Fix** Add an Armenian display face to the stack, or state explicitly that
Armenian headings are set in the text face and add it as the fallback. Either is
defensible; silence is not.

### B3 · Secondary text on the sunken surface fails contrast

**Where** `styles/product.css:56` — `.mc-calculator__surcharges` sets
`color:var(--mc-text-secondary)` at caption size, inside
`.mc-calculator__result` which sets `background:var(--mc-surface-sunken)`
(`product.css:53`).
**Evidence** `#606161` on `#E4D8C4` measures **4.41**. The threshold is 4.5.
**Why it matters** This is the surcharge arithmetic on the pricing calculator —
the numbers that exist specifically so a diaspora client can check the price
before calling. It is also the one pair the design system's own comment claims
is safe: `semantic.css:23` annotates `--mc-text-secondary` as "4.98 / 5.46",
which is true on Nude and on Ivory but not on the third surface it is used on.
**Fix** Either use `--mc-text-primary` in that block, or stop using
`surface-sunken` behind secondary text. The same pair also occurs on
`.mc-report__block--recommend` (`product.css:100`) — check it too.
**And add the missing gate.** The specification's closed list of allowed pairs
was checked against tokens, not against rendered combinations. This defect is
what that gap looks like.

### B4 · Armenian script appears in the English version

**Where** `TariffCard` instances — `armenian="(Զննում)"`, `"(Էքսպրես խնամք)"`
and the rest; rendered as `Express (Էքսպրես խնամք)` in the pricing bands.
**Evidence** Armenian codepoints present throughout the English-only prototype.
**Status** **This one is not your error.** You implemented `DECISIONS-2` §5
exactly as written, and the dedicated `armenian` prop shows it was deliberate.
**The owner has reversed that ruling on 31.08.2026.**
**The rule now** Each locale is written in one script. The English version
contains no Armenian and no Cyrillic; the Russian version contains no Armenian.
Product names are `Inspection`, `Express`, `Optimal`, `Maximum`, `Special` and
nothing else. The only characters that may cross a locale boundary are the dram
sign and proper nouns with no translation, such as a cemetery name.
**Fix** Remove the `armenian` prop from `TariffCard` and every call site, and
strip the parentheticals from the strings. Then add the gate: grep each locale
file for the `\u0530-\u058F` range and expect nothing but the dram sign.

---

## Major

### M1 · The language switcher is below the minimum hit area

**Where** `styles/controls.css:160` — `.mc-segmented__item{min-height:36px}`
**Evidence** 36px against a required 44px. The system contains a correct
`.mc-hit-44` helper at `scopes.css:68`, and this component does not use it.
**Why it matters** It is the control every non-English visitor touches first, on
a phone, and our audience is 40–60. It is also the one component where a small
target is least excusable.
**Fix** Apply `.mc-hit-44`, or raise `min-height` to `var(--mc-layout-target-min)`.

### M2 · A literal hex in a token layer, and a seventh grey

**Where** `tokens/scopes.css:9` — `--mc-surface-raised-hover:#52565A;`
**Evidence** The only literal colour outside `primitive.css` in the whole system.
**Why it matters** It breaks the system's own rule — stated in the header of
`primitive.css`, "the only layer where a literal appears" — and it introduces a
grey that exists in no palette and was never checked. It passes contrast (5.93
with Nude), so this is a discipline defect rather than a visual one, but it is
exactly the crack through which a seventh and an eighth colour arrive.
**Fix** Promote it to `primitive.css` as `--mc-color-anthracite-350` with its
measured pairs, or reuse `--mc-color-anthracite-400`.

### M3 · An off-scale spacing value in the responsive tokens

**Where** `tokens/semantic.css:129` — at `min-width:900px`,
`--mc-layout-band-dark:112px`.
**Evidence** The declared scale is
`4 8 12 16 20 24 32 40 48 64 72 80 96 128 144 160`. 112 is not on it.
**Why it matters** The system claims, in `TOKENS-SPEC.md` rule 9, "spacing scale
only". One exception makes the lint rule unenforceable.
**Fix** 96 or 128. The light band at the same breakpoint uses 96, so 96 keeps the
relationship the specification sets between the two bands at the other two
breakpoints.

### M4 · Three strings on screen are not in the content specification

**Where** Home — "The whole process, step by step", "See it in the portal";
How it works — "What the report proves".
**Evidence** Self-reported in `review/FINDINGS.md` finding 4; confirmed against
`FINAL-CONTENT`.
**Why it matters** Not because the strings are bad — they are competent. Because
the copy is the one part of this product that was written against a stop-list, a
register and a legal review, and a build that writes its own strings has left
that discipline. The declaration is the right behaviour; the strings still have
to go or be adopted.
**Fix** Owner decision. Either adopt them as new keys in `FINAL-CONTENT` — my
recommendation, they are in register — or drop the two blocks that needed them.

### M5 · Fonts load from a third-party CDN

**Where** `tokens/fonts.css` — `@import` from `fonts.googleapis.com`.
**Evidence** Self-declared in the file's own comment and in `HANDOFF.md`.
**Why it matters** The specification requires self-hosted subset woff2 with no
third-party requests, and that is a bank condition, not a preference. It also
costs a round-trip on exactly the connections that are slowest — diaspora
clients abroad.
**Fix** Self-host subset woff2. It is already documented as a known deviation,
so this is a task, not an argument.

---

## Minor

### m1 · Recommended-work prices are invented figures

**Where** the report fixture — `35,000 ֏ AMD` for a kerb, `80,000 ֏ AMD` for
regilding lettering.
**Why it matters** They read as our real repair prices. No such price list has
been agreed, and the project rule is that nothing is invented.
**Fix** Mark them visibly as sample data in the fixture, or replace with a
neutral "priced after inspection".

### m2 · Seven `<h1>` elements in one document

**Where** the prototype holds every screen in one file.
**Why it matters** Correct for a prototype, wrong in production. Worth stating so
nobody carries the pattern across.
**Fix** One `<h1>` per route. Already implied by the route split.

### m3 · `prefers-reduced-motion` appears once

**Where** one block across the whole system.
**Why it matters** The specification asks for it to be honoured; a single global
block may be enough, but it has not been checked against the components that
actually animate — the modal, the drawer, the toast, the accordion.
**Fix** Verify each animating component under the setting.

---

## Confirmed correct — do not "fix" these

Checked and passing, so nobody re-opens them later:

- Palette exact: `#7C8654` `#EFE5D5` `#F3F0E9` `#33373C` `#575E3B` `#8C3A2E`.
- Olive carries no text anywhere; `--mc-surface-accent-solid` is annotated
  "NO LABEL MAY SIT HERE".
- Deep Olive is remapped to Nude inside `.mc-on-dark`, so the 1.75 pair cannot
  occur.
- One functional colour. No success token, no warning token, no `danger` button.
- Radii exactly `0 · 2 · 8 · 9999`.
- `--mc-tariff-badge-reserve:46px` — the badge-reserve rule is implemented, and
  the value matches the Figma build.
- Rail at 14px, `--mc-rail-width-lg:222px` matching the specified grid.
- No `prefers-color-scheme` anywhere — the deliberate refusal of OS dark mode,
  with the reason written in the file.
- Every price correct: 20,000 · 65,000 · 160,000 · 200,000 · 95,000.
- Both service promises appear four times each, identically.
- `MemoryCare` one word, eight occurrences, no variant spellings.
- The dram symbol appears 14 times and `AMD` 14 times — always paired.
- `{LEGAL_ADDRESS}` and `{WORKING_HOURS}` render as visible placeholders.
- Forbidden-word list clean: no `monthly`, `bestseller`, `light visit`,
  `preventive`, `discount`, `most chosen`, `deceased`, `departed`, `remains`,
  `disposal`.

---

## What the delivery got right that is worth keeping

The `.mc-hit-44` helper carries a comment explaining why all four insets must
not be set — that is a bug someone already hit, written down so it is not hit
again. `scopes.css` explains why OS dark mode is refused, in terms of the
product rather than the code. `TOKENS-SPEC.md` lists the components that must
**not** be created. `HANDOFF.md` lists the gates that could not run and how to
run each one in production instead of marking them green.

That is the behaviour you want from the next pass too.

---

## What to do next, in order

1. Fix B1, B2, B3. All three are small and all three are shipping defects.
2. Fix M1, M2, M3 — under an hour together.
3. Decide M4: adopt the three strings or drop the blocks.
4. Schedule M5 with the font files.
5. Add the missing gate: enumerate contrast over **rendered** pairs, not over
   token combinations. B3 exists because that gate does not.
6. Then continue the build — the eight routes that are deliberately absent, the
   first-entry portal screen the specification calls the most important empty
   state in the product, and the two locales.
