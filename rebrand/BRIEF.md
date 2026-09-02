# MemoryCare rebrand — master brief for the build team

Five specialists, one lead. We are rebuilding the site Igor built, on our
brand, to a standard that can go to a bank and to a customer.

**The output is a working static site**, not mockups. Screenshots are
rendered from it. That is deliberate: 22 routes × 3 locales cannot be
hand-drawn honestly, and Igor needs code, not pictures.

---

## Non-negotiable owner rules

1. **Nothing is removed from the functionality.** Every field, control and
   link that exists still exists and still works.
2. **Adding is allowed** and often required.
3. **No page is removed.** The four routes that serve a 404 template today
   get real content instead.
4. **Adding pages is allowed** and required — six of them by the bank.
5. **Only our brand colours.** One stray hex fails the work.
6. **All content is real and true today.** Not plausible — true.
7. **Ask, do not guess.** Anything unsourced is marked `[BLOCKED]`.

**The one carve-out:** rules 1 and 3 protect functionality and pages, not
false statements, and rule 6 excludes invented content. The fabricated
statistics, the six placeholder testimonials and the empty partners strip:
the *components* survive, repurposed or flagged off; the *false content*
does not. The withdrawn `40,000 ֏` price must not appear anywhere.

---

## Brand

| Name | Hex | Job |
|---|---|---|
| Dark Olive | `#212212` | body text on light; the dark band ground |
| Olive | `#7C8654` | **decor only** — fills, rules, dividers, marks |
| Nude | `#EFE5D5` | the page ground |
| Ivory white | `#F3F0E9` | objects on the page: cards, sheets, inputs, header |
| Sky blue | `#A4D6E8` | dark-ground type; tint fill on light |
| Deep Olive | `#575E3B` | links and accent text on light (not in brandbook) |
| Error | `#8C3A2E` | validation only (not in brandbook) |

**Measured contrast — facts:**
Dark Olive on Nude 12.93 · on Ivory 14.17 · Nude on Dark Olive 12.93 ·
Ivory on Dark Olive 14.17 · Sky on Dark Olive 10.26 · Deep Olive on Nude
5.49 / Ivory 6.01 · Error on Nude 6.10 / Ivory 6.69.
**Fails:** Olive on Nude 3.12, Ivory 3.42, Dark Olive 4.14 ·
Sky on Nude 1.26, Ivory 1.38 · Error on Dark Olive 2.12.

**Four structural rules:**
1. Olive never carries text and never receives text.
2. Sky blue is a dark-ground colour; on light it is a tint fill only.
3. No form showing validation errors may sit in a dark band.
4. Nude is the ground, Ivory is the objects on it.

**Type.** Display **GHEA Mariam** (capitals — real family name, in
`assets/fonts/ghea-mariam/`, four OTFs, and **it contains ֏ U+058F**).
Text **Montserrat**; Armenian text **Montserrat Arm**, a separate family.
֏ inside Montserrat runs needs an isolated `unicode-range: U+058F` slice
pointing at GHEA Mariam.

Floors: body never below 16px, no informational text below 14px, inputs
16px, tabular figures wherever a number can change.

**Mark.** Hands in Nude cradling a five-petal forget-me-not in Olive,
centre a woven medallion in Sky blue. Wordmark single-colour Olive.
Tagline Sky blue, uppercase, wide tracking, no full stop. The medallion
is 29 filled paths, no strokes, and stops being legible below 48px.
Vectors in `assets/brand/logo-v6/svg/`.

---

## Products — the owner's decision of 26.08.2026

**All visits are full visits.** The light/heavy split is rejected; those
words appear nowhere, including in a database column.

| Product | Composition | Price |
|---|---|---|
| Զննում | One orientation visit: locate the plot, full written inventory, photo and video of the condition, a list of the work needed, a quote for minor repair. **No cleaning.** | 20,000 ֏ |
| Էքսպրես | One full visit: deep cleaning of the whole plot and every monument — steam, professional neutral-pH chemistry, wet/dry vacuum. **Never say "Kärcher"; high-pressure washing is forbidden on monuments.** | 65,000 ֏ |
| Օպտիմալ | Annual: **4 full visits, one in each season** | 160,000 ֏/yr |
| Մաքսիմում | Annual: **6 full visits** | 200,000 ֏/yr |
| Հատուկ խնամք | Non-standard; always begins with an inspection | calculator |

Credits: inspection credited **only on signing an annual subscription**,
within 60 days, never into a single visit. Single visit credited in full
within 60 days. **One credit only** — either, never both. No discounted
repeat.

Surcharge beyond a standard envelope of **16 m² and two monuments**:
+10,000 ֏/yr per m², +30,000 ֏/yr per monument (single visit: +2,500 and
+7,500). Sliders cap at 100 m² / 10 monuments. 160,000 ÷ 16 = exactly
10,000 ֏ per m² per year — an added metre costs what an included one does.

**Every route into year one costs the same 160,000 ֏.** That is the credit
block's headline: *starting small costs you nothing.*

---

## True things worth saying

- A visit does not close until the report holds **eight photographs —
  four angles before, the same four after — two videos, and one GPS point
  recorded at the plot on the day.**
- GPS is **verification**, not location.
- The winter visit runs in a weather window, not on a date. **Four visits
  are guaranteed regardless** — a missed one is added to spring. A
  contract term, not a failure.
- Registered **2026**. The pilot is the first client work.

## Never

`the only` · `the first` · `nobody else` · `unlike others` · `unique` ·
`since 20xx`. No competitor named or alluded to. No guilt. No "peace of
mind". No words in a dead person's mouth. No QR or memorial page.

---

## The bank — Ameriabank internet acquiring, in force 26.05.2026

§4.10 requires **twelve** items on the site. Full mapping in
`docs/PROMPT-BANK-COMPLIANCE-UIUX.md`. The ones that create pages:
About · full service descriptions · legal restrictions · real prices in
AMD · delivery terms including restrictions outside Armenia · return and
refund terms · privacy policy · **a separate cookie policy** · **security
capabilities and card-data rules** · special-offer restrictions (our
credit rules) · **payment-system colour marks** · free-trial terms (N/A,
declare it).

§4.9.2 requires all information **including advertising** to comply with
the law — which is what makes the invented statistics a legal exposure.
§4.11 requires every link to be real: nineteen routes currently answer
200 while rendering a 404.

§3.10: no surcharge or different conditions for card payment.
§3.5: transactions inside Armenia in AMD only.

---

## The ten places the current build measurably harms the user

Fix these; leave everything else where it is.

1. `acct-packages` at narrow widths — the Pay button sits at `left:371px`
   in a 360px viewport, document 452px wide, table row overlapping itself.
2. `acct-payments` — a sidebar item shown to paying customers 404s.
3. `acct-order-1..4` — **six hidden inputs and a submit button, no visible
   field at all.** A customer subscribes to a year of grave care without
   saying which grave. `acct-objects` is empty with no way to add one.
4. Nothing can be cancelled anywhere, in any locale.
5. `acct-profile` — the password change has no current-password field.
6. The 404 template drops the language switcher on all 19 routes.
7. Submenus open on hover only, no keyboard path.
8. Focus states removed and not replaced.
9. No `h1` on any page; 17 distinct font sizes.
10. Contrast: `#888` on `#F5F5F5` = 3.25, on `#EDEDED` = 3.03; white on
    `#FF0000` = 4.00 on the Pay button — off-palette and it goes.

---

## Build conventions — everyone follows these

- Static HTML, one file per route per locale, under `rebrand/site/<loc>/`.
- **All colour comes from `assets/tokens.css`.** A hard-coded hex fails.
- All copy comes from `strings/<loc>.json`. No text typed into HTML.
- `lang` attribute correct on `<html>`; `hreflang` between locales.
- Desktop is the design target (1440), and the page must not break or
  scroll sideways at any width down to 360. Removing horizontal scroll is
  a defect fix, not a mobile design.
- Semantic markup, one `h1` per page, real focus states, keyboard paths.
- No JS framework. Progressive enhancement only.
