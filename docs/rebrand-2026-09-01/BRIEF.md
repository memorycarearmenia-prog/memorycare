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

## Pricing — locked, do not alter

| Tariff | Composition | Price |
|---|---|---|
| **Զննում** (Inspection) | 1 light visit: photo/video of condition + priced list of recommended work. No cleaning | 20,000 ֏ |
| **Էքսպրես խնամք** (Express) | 1 heavy visit | 60,000 ֏ |
| **Օպտիմալ խնամք** (Optimal) — leading choice | 2 heavy + 4 light (6/yr) | 180,000 ֏ |
| **Մաքսիմում խնամք** (Maximum) | 3 heavy + 6 light (9/yr) | 240,000 ֏ |

Flat price for every client. Inspection is a one-off and must read as
visually apart from the three subscriptions; it is credited toward any
package within 30 days. Express is credited toward a subscription within 60
days; an unconverted repeat Express in the same calendar year is 40,000 ֏.
Maximum is 9 visits — never call it monthly. Optimal is marked
**"Our recommendation"**, never "most chosen" or "bestseller" (zero
customers; in Armenian use `առաջատար`).

Prices are AMD. Any $/€ figure must be marked approximate.

## Languages

**Three: ARM / ENG / RUS.** French is out of Year-1 scope. One script per
locale — the English site carries no Armenian script anywhere.
**Mobile-first**: diaspora traffic is majority mobile. The deliverable is a
desktop site built mobile-first.

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
