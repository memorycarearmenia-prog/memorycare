# Rebrand brief — Igor's site under the 31.08 brandbook

Read this before writing anything. Every fact here is verified; do not
contradict it and do not invent around it.

## The job

Igor built a working site at `mc.makyan.com` for MemoryCare. It is off-brand,
carries fabricated proof, and predates the brandbook delivered 31.08.2026.
We are rebranding **the whole site** — every route, every state, desktop and
mobile — onto the new identity, and we want it **modern, beautiful and
professional**, motion included.

Five specialists work in parallel. Each writes one proposal. The design lead
then converges them into a single specification. Argue for your view; do not
hedge; where you disagree with the obvious answer, say so and say why.

## The business, in one paragraph

Memory Care LLC, Yerevan. A subscription service for professional care of
family memorial plots on Yerevan cemeteries, with photo/video/GPS-verified
visit reports delivered through a client portal. Pre-launch: **zero paying
customers**, the September pilot is the first real client work. Two
audiences, one brand, one page: the Armenian diaspora (US, France, Russia,
Europe; 35–60; emotional driver: guilt over distance) and the local Yerevan
premium segment (40–60; rational driver: no time). Never write diaspora-only
copy. Lead with the outcome, then name both reasons naturally.

Tone: light premium minimalism, lots of white space, large typography,
restrained editorial elegance, warm but professional. Explicitly NOT
funeral-cliché — no dominant black, no crosses, no gothic lettering, no
candles. Not guilt-pressure, not sentimental, not cold-corporate. Reference
points the team likes: tending.app, headspace.com, stripe.com, airbnb.com.

## Brand — the 31.08 brandbook, source of truth

`assets/brand/brandbook/MemoryCare_brandbook.pdf`, rendered to
`assets/brand/brandbook/page-{2,3,4}-*.png`. Vectors in
`assets/brand/logo-v6/svg/`, full set and file IDs in
`assets/brand/logo-v6/README.md`.

**The mark.** Two open hands in Nude cradling a five-petal forget-me-not
(Անմոռուկ) in Olive, its centre a woven interlaced medallion drawn as open
line-work in blue. Four lock-ups: primary logo, logo mark, wordmark,
monochrome. The wordmark is **single-colour Olive**. The tagline
"HONORING MEMORY, CARING FOR LOVED ONES" is blue, uppercase, wide tracking,
**no full stop**.

**Colours — five official, plus one interface value.**

| Name | HEX |
|---|---|
| Dark Olive | `#212212` |
| Olive | `#7C8654` |
| Nude | `#EFE5D5` |
| Ivory white | `#F3F0E9` |
| Sky blue | **`#A4D6E8`** (working value — see below) |
| Deep Olive | `#575E3B` (interface only, not in the brandbook) |
| Error | `#8C3A2E` (validation only) |

Sky blue is contested: the brandbook's colour page prints `#D4ECF9`, but
every delivered vector, PNG, JPG and PDF paints `#A4D6E8`, and the book's own
logo page renders `#A4D6E8`. We use **`#A4D6E8`** until the designer rules.
Design so that swapping it later is a one-token change.

**Measured contrast — these are rules, not preferences.**

| Pair | Ratio | |
|---|---|---|
| Dark Olive on Nude | 12.93 | pass |
| Dark Olive on Ivory | 14.17 | pass |
| Nude on Dark Olive | 12.93 | pass |
| Ivory on Dark Olive | 14.17 | pass |
| Sky blue `#A4D6E8` on Dark Olive | 10.26 | pass |
| Deep Olive on Nude / Ivory | 5.49 / 6.01 | pass |
| Error on Nude / Ivory | 6.10 / 6.69 | pass |
| Olive on Nude / Ivory / Dark Olive | 3.12 / 3.42 / 4.14 | **fails for text** |
| Sky blue on Nude / Ivory | 1.26 / 1.38 | **invisible** |
| Deep Olive on Dark Olive | 2.36 | **never** |
| Error on Dark Olive | 2.12 | **invisible** |

Four structural consequences:
1. **Olive never carries text and never receives text.** Fills, petals,
   dividers, decorative panels only.
2. **Sky blue is a dark-ground colour.** Beautiful type on Dark Olive,
   invisible on light — there it may only be a tint fill.
3. **The consultation form may never sit inside a dark band** — the error
   colour is invisible there.
4. **Nude is the page ground; Ivory is the objects that sit on it** (cards,
   the report sheet, inputs) and the light label on dark fills.

**Typography.** Display **Ghea Mariam**; text **Montserrat**, with Armenian
in the separate family **Montserrat Arm** — the stack must name it
explicitly. Both cover Latin, Cyrillic and Armenian. Unverified: whether
either carries **֏ (U+058F)** — keep the currency symbol as its own element
with its own font stack so a missing glyph degrades for that one character
instead of breaking a price.

## ⚠️ CORRECTION issued after the brief went out — pricing

**The pricing table first circulated in this brief was stale.** It was
copied from `CLAUDE.md`, which was never updated after the owner
re-decided the whole line-up on **26.08.2026**
(`docs/TARIFF-REDESIGN-2026-08-26.md`). That document's §8 names
`CLAUDE.md`'s "Pricing — locked" table as outdated in exactly these
respects. The 31.08 audit independently treats the 26.08 line-up as the
expected one. **Later owner decision wins. Use the table below and
nothing else.**

Every number in the superseded table was wrong: the prices, the visit
counts, the light/heavy split, the credit window and the repeat rule.

## Pricing — the owner's decision of 26.08.2026

**All visits are full visits.** The "light visit / heavy visit"
distinction is **rejected** — "все визиты полноценные". Do not use it
anywhere, in copy or in a comparison table.

| Product | Composition | Price |
|---|---|---|
| **Զննում** (Inspection) | One orientation visit: locate the cemetery and the plot, full written inventory of everything seen, photo/video of the condition, a list of the work needed, and a quote for minor repair where there is any. **No cleaning is performed.** | **20,000 ֏** |
| **Էքսպրես** (Express) | One full visit: deep cleaning of the whole plot and the monuments — steam generator, Kärcher, vacuum, professional chemistry. Photo and video reports, portal access. Express is the atomic unit of the range; the subscriptions are counted in them. | **65,000 ֏** |
| **Օպտիմալ** (Optimal) — flagship | Annual subscription: **4 full Express visits, one in each season.** | **160,000 ֏ / year** |
| **Մաքսիմում** (Maximum) | Annual subscription: **6 full Express visits.** | **200,000 ֏ / year** |
| **Հատուկ խնամք** (Special) | Non-standard cases: more visits (12/yr for example), a plot over 16 m², more than two monuments, several family plots on different cemeteries. **Always begins with a Զննում.** | **priced by calculator / consultation** |

**Special is a fifth card on the site.** It was absent from the first
version of this brief. Its internal price floor: a Special visit is never
cheaper than a Maximum visit (~33,333 ֏).

**Credit rules — get these exactly right, three specialists tripped over
the old ones.**

- Զննում 20,000 ֏ is credited **only on signing an annual subscription**,
  within **60 days**. It is **not** credited into an Express.
- Express 65,000 ֏ is credited in full into an annual subscription within
  **60 days**.
- **The one-credit rule:** on signing, **either** the Զննում (20,000)
  **or** the Express (65,000) is credited — one of the two, never both. A
  client who bought both gets the larger (65,000) credited; their Զննում
  remains a paid inspection. There is no credit between one-off products.
- **There is no discounted repeat Express.** The price is always 65,000 ֏.
  A "repeat at 40,000 / 45,000" was considered and **rejected by the owner
  on 26.08** — it devalued the subscription and what the client had already
  paid. The site currently sells 40,000 ֏; that is a withdrawn price for a
  product that does not exist, and removing it is a blocker.

**A calculator belongs on the tariffs page** — an open formula, two
sliders, the same price for everyone, visible before anyone has to call.
Design for it.

Optimal sells in one sentence: **"four full visits, one in each season."**
The winter visit runs in a suitable weather window rather than on a
calendar date (the protocol limit is temperature — no washing at or below
+4…+10 °C, or with a frost expected within 48 h). **Four visits are
guaranteed regardless**: if no window opened over the winter, the visit is
**added** to spring — two visits in spring. That is a term of the
contract, not a failure, and the site should say so.

"Monthly" remains forbidden. Optimal is marked **"Our recommendation"**,
never "most chosen" or "bestseller" — zero customers. In Armenian use
`առաջատար`.

Flat price at any plot size for the standard products. Prices are AMD; any
$/€ figure must be marked approximate.

## Languages

⚠️ **SCOPE CORRECTION, 01.09 — desktop web only.** The owner has ruled
that we design and deliver the **desktop web version only**. No mobile
screens, no 360 breakpoint, no separate mobile ramp. Everything below
that says "mobile-first" is superseded: the deliverable is the desktop
site. The page must still not break on a narrow window, but we are not
designing, specifying or reviewing a mobile experience.

Recorded for the file: `CLAUDE.md` states that diaspora traffic is
majority mobile, and the 31.08 audit captured 360 / 768 / 1024 / 1440 /
1920. Desktop-only is therefore a deliberate narrowing, not an oversight.

**Three: ARM / ENG / RUS.** French is out of Year-1 scope. One script per
locale: the English and Russian sites carry no Armenian **words** — no
product names in Armenian letters, no untranslated labels.

**This rule is about words, not symbols.** The currency sign **֏ (U+058F)
lives in the Armenian Unicode block and is used in all three locales** —
it is the sign for the currency the client is actually charged in, not a
piece of Armenian copy. An earlier phrasing of this rule said "no Armenian
script anywhere", which would have forbidden the very character the same
brief mandates. Corrected.
**Desktop web only** — see the scope correction above.

## Site structure to design

Routes that exist today: `home`, `contact`, `login`, `register`, `reset`,
`history`, `mission`, `values`, `news`, `notfound`, `account-index`,
`packages-add-1`, `root`. `history`, `mission`, `values` and `news` currently
render the 404 template.

Sections the home page must carry:
1. Hero — the offer, with GPS/verified-reporting proof on the first screen.
2. Tariffs — four, Inspection set apart, Optimal marked as the recommendation.
3. The report — a sample report screen. **This is the actual product; give it
   real visual weight.**
4. How it works — subscribe → visits → photo/video/GPS report.
5. Family Circle — relatives get their own sub-account by invite, see all
   reports, can order one-off services. Ships with the platform.
6. Trust — verification, regularity, transparency, for both audiences.
7. Language switcher — ARM/ENG/RUS only.
8. CTA — free consultation request (name + phone/WhatsApp) as primary; card
   payment secondary. The subscription is large enough that the decision
   happens after a conversation.

**No QR / digital-memorial-page mention anywhere.** Year-2 scope.

## What must be removed from Igor's build

The 31.08 audit (`docs/site-audit-2026-08-31/FINDINGS.md`) found, among
others:
- Four fabricated proof figures on the home page: 150,000 customers,
  55+ services, 250,000+ graves, 15 years of experience. All false.
- Three fabricated testimonials with photographs of real public figures under
  invented names, five-star graphics and Lorem Ipsum quotes.
- A partners carousel of four empty placeholder tiles.
- A before/after slider (the design package forbids it — the after-image must
  never be the opening image).
- Desktop nav submenus that open on hover only, with no keyboard equivalent.
- A mobile menu that omits the language switcher.
- Four routes rendering the 404 template.

Read `FINDINGS.md` in full before proposing. Screenshots of every route,
locale, viewport and state are in `docs/site-audit-2026-08-31/`.

## Truth constraints

- No testimonials, no review counts, no "X families trust us", no years in
  business, no customer numbers. The company is pre-launch. Use
  process-trust instead: "verified visits", "GPS-tagged reports", "report
  within 48 hours", "callback within one business day".
- hush.am is a real, established Yerevan competitor since ~2015 with photo
  reports and GPS grave locating. **Never claim we are the only ones doing
  grave care with photo reports in Yerevan.** Our differentiator is the full
  combination — photo + video + GPS + client portal + family circle — plus
  verification rigor and a premium brand. No world analog combines all five.

## Accessibility and performance floors

WCAG 2.2 AA. Body text never below 16px on mobile. Uppercase chips and
badges never below 14px. Every hover affordance needs a keyboard and touch
equivalent. Every motion respects `prefers-reduced-motion`. Real focus
states, not the default outline removed. Armenian, Russian and English must
all fit the same components — Armenian and Russian run long.

## What to deliver

One markdown file at `docs/rebrand-2026-09-01/PROPOSAL-<slot>.md`.

Be specific enough to build from: name exact tokens, sizes, timings, easing
curves, breakpoints, element order. Show your reasoning where a choice is
contestable. Where you are proposing something that could look generic,
say what makes this one specific to a company that photographs graves for
families who live abroad.

Do not write code files. Do not touch Figma. Do not edit any file outside
your own proposal.
