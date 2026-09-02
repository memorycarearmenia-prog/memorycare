# Handover to the developers

Read this before the design documents. It tells you what is decided, what
is runnable, and what is deliberately not here.

## What is in this folder

| File | What it is |
|---|---|
| `tokens.css` | The design tokens as CSS custom properties, in a `@layer tokens`. **Authoritative.** Every contrast ratio in the comments was computed from these hex values, not asserted. |
| `tokens.json` | The same values in DTCG-ish JSON, for Style Dictionary or an equivalent. Generated from the same source as the CSS, so they cannot drift. |
| `home.html` | A **runnable** page — header, hero and the tariff row — built on `tokens.css`. Open it in a browser. It is not a mockup of the markup; it is the markup. |
| `preview-1440.png` | That page rendered at 1440. |
| `assets/` | The logo mark in three treatments, and `medallion.svg` (the seal, `fill: currentColor`). |

`home.html` is the reference implementation for the parts that are
designed. Copy its structure; do not re-derive it from the screenshots.

## Scope

**Desktop web only.** Owner's decision, 01.09. No mobile screens are
specified. The page must still not break in a narrow window, but there is
no mobile design to build against, and none is expected of you.

Two audit findings survive that decision because neither is about mobile,
and both are yours to fix:

- **The nav is unopenable between 1024 and 1300px.** `menu.js` treats the
  layout as mobile below 1300 while the CSS shows the desktop menu, so a
  click on a parent item calls `preventDefault()` and toggles a class
  instead of navigating. That range is the most common laptop width there
  is. One breakpoint set, shared by CSS and script.
- **`user-scalable=no` is set.** Pinch-zoom is disabled at every width,
  failing WCAG 1.4.4. Remove it. The viewport tag in `home.html` is
  correct — copy it.

## The rules that are not preferences

These four come out of measured contrast and break the page if ignored.

1. **Olive `#7C8654` never carries text and never receives text.** It
   measures 3.12 on Nude, 3.42 on Ivory, 4.14 on Dark Olive. It lives in
   the `--mc-decor-*` namespace, which is defined as *paint that never has
   a foreground*. If you are about to set `color` on one of those tokens,
   you have the wrong token.
2. **Sky blue is a dark-ground colour.** 10.26 on Dark Olive, **1.26 on
   Nude** — invisible. On light grounds it may only be a tint fill (the
   seal disc, a chip ground), never type.
3. **The consultation form may never sit inside a dark band.** The error
   colour measures 2.12 on Dark Olive. `--mc-text-feedback-error` is
   deliberately **not defined** inside `.mc-band--dark`, so the mistake
   fails loudly rather than silently.
4. **Nude is the page ground, Ivory is the objects on it.** They differ by
   1.10 in contrast — the eye cannot tell them apart, so the token name
   has to. `--mc-surface-ground` vs `--mc-surface-object`.

Two more, from the build:

- **Cards in a row are equal height, always**, with the button pushed to
  the foot by a growing spacer — not by hand-tuned padding. The alignment
  has to survive a copy change.
- **A card without a badge reserves the badge's height** (46px). Without
  it the three titles sit at different heights and the row reads as an
  accident.

## Fonts — read this before you wire anything up

**Display: GHEA Mariam** (the family name has GHEA in capitals — read from
the font's name table). **Text: Montserrat.** **Armenian text: Montserrat
Arm**, a separate family, not a subset — name it explicitly. Self-host all
of them. The display face is in `assets/fonts/ghea-mariam/` as OTF;
convert to WOFF2 and subset before shipping.

**The dram sign, ֏ (U+058F) — the position as of 02.09.2026.**

It is **in GHEA Mariam**, in all four styles, verified by reading each
file's cmap. It is **not in Montserrat**.

The consequence is good: the `price` and `price-xl` roles are set in the
display face, so **a price renders the sign natively, with no fallback at
all.**

What still needs handling is ֏ inside *Montserrat* text — the arithmetic
line under a price, the verification rail, body copy. There the glyph is
absent and the browser will fall back. So the isolated slice stays, and it
now points at a face we own:

```css
@font-face {
  font-family: "MC Dram";
  src: url("/fonts/GHEAMariamReg-dram.woff2") format("woff2");
  unicode-range: U+058F;          /* this character and nothing else */
  font-display: swap;
}
```

Subset that file to the single glyph — the whole face is ~150 KB.

Note what this pairing is: ֏ in GHEA Mariam beside Montserrat digits is a
**deliberate pairing of two brand faces**, not an accidental system
fallback. Check it optically at the sizes used and adjust the sign's size
or baseline in the token if it needs it.

**Withdrawn:** an earlier version of this handover said the live site
already shows the sign falling back at a different weight. The 02.09 audit
measured both runs and found an identical stack, size and weight — the
live site sets everything in `system-ui`, so digits and sign come from the
same place. That claim was inherited from the 31.08 audit and was not
supported.

## Colour value still open

Sky blue is `#A4D6E8` in these tokens. The brandbook's colour page prints
`#D4ECF9`; every delivered vector, PNG, JPG and PDF paints `#A4D6E8`, and
the book's own logo page renders `#A4D6E8`. The designer must rule.
**Change it in exactly one place** — `--mc-color-sky-500` — and add a CI
grep for the literal so it cannot creep back in anywhere else.

## What is NOT built

`home.html` covers the header, the hero and the tariff row. Everything
else is specified but not drawn:

- Home sections 3, 4 and 6–12 — how it works, what a visit includes,
  Family Circle (the one dark band on the page), trust, the honesty panel,
  founders, FAQ, the consultation form, footer.
- The entry rail for the Inspection product, the credit block, and the
  Special card with its price calculator.
- The portal.
- **The six routes the bank requires** — About, a full five-product
  tariffs page, legal restrictions, an English privacy policy, a refund
  policy and service-delivery terms. Copy for all six is written, in
  `04-content/06-legal-and-about.md`.

Specs are in `03-design/`; `00-FINAL-REBRAND.md` governs, the five
proposals under it carry the detail. Copy is in `04-content/`, with every
string carrying a slot ID and a character budget.

## What you must not build

- Anything asserting a fact that is not true today: customer counts,
  testimonials, review stars, years in business, a partners strip.
  The live build ships four fabricated figures and three invented
  testimonials illustrated with photographs of real public figures. All of
  it goes, including as an "empty state for later".
- The 40,000 ֏ repeat Express. It is a withdrawn price for a product that
  no longer exists, and it is live on the site right now. There should be
  no field for it in the model and a build-time string check against it.
- The words "light visit" and "heavy visit", or any translation. The owner
  rejected the distinction — all visits are full visits. **This includes
  enum values and column names in the platform schema**; a distinction in
  the schema resurfaces in a report template.
- A carousel. The current one costs 151 KB, produced six audit findings,
  and does not advance.
- Any mention of a QR code or a digital memorial page. Year-2 scope.

## Performance and accessibility floors

LCP ≤ 2.0s, INP ≤ 150ms, CLS ≤ 0.03. Home ≤ 750 KB, legal pages ≤ 320 KB.
WCAG 2.2 AA, measured rather than asserted. Body text never below 16px;
no informational text below 14px anywhere — the verification rail carries
the actual proof for a 40–60 audience. Every hover affordance needs a
keyboard and touch equivalent. Real focus states: `home.html` sets one,
the live build removes the default and replaces nothing.

Motion is calm and small: 120ms for state, 220ms for entrance, 320ms
ceiling, transform and opacity only, and a complete `prefers-reduced-motion`
path. **One exception**, and it is deliberate: the price calculator's
result animates as the sliders move, because recomputing in the open is
the transparency argument made visible. It is the only number on this site
permitted to change on screen — the site's defining sin was inventing
numbers.
