# Build the MemoryCare website from the design specification

You are a senior front-end engineer. You are given a complete design
specification and you will build the MemoryCare marketing site and client
portal from it. Not a mock-up — a real, running, deployable site.

Read this entire brief before writing any code. Then read the specification
files listed in §2 before writing any code either.

---

## 1. What this is

MemoryCare is a subscription service for the professional care of family
memorial plots in Yerevan cemeteries. A client subscribes for a year, a crew
visits on a schedule, and after every visit the client receives a report:
before/after photographs, video and GPS confirmation that the crew was on that
specific plot.

**The single most important fact.** We do not sell cleaning. We sell proof. The
report is the product. A client opens it six to nine times a year, forwards it
to a brother or an aunt, and judges the whole company by it. Build accordingly:
the report screen is not a detail page, it is the thing.

**The audience.** Armenian diaspora abroad, 35–60, who cannot travel and pay
from another country to a company they have never met — and local Yerevan
clients, 40–60, who could go themselves but have no time. One site serves both.
Mobile-first is not a preference: most of the traffic is a phone, often late at
night, often on a slow connection abroad.

**The company is pre-launch with zero paying customers.** That governs the
content rules in §6 and is not negotiable.

---

## 2. Your inputs, and which one wins

You are given `MemoryCare-design-v1.0/`. Read in this order:

1. **`LEAD-REVIEW.md`** — the verification protocol. **Highest authority.** It
   holds the recomputed contrast table, the conflicts found between the other
   documents and how each was ruled, and the two facts about typefaces that were
   verified by rendering. When anything disagrees with this file, this file is
   right.
2. **`DECISIONS.md`** and **`DECISIONS-2.md`** — the owner's rulings. Binding.
3. The four specifications, peers, each authoritative in its own domain:
   - **`FINAL-UX.md`** — sitemap and URL slugs, the object and role model, the
     three user journeys, every page and portal screen block by block, every
     state, the permission matrix, form specifications, the calculator, the
     cancellation flow, responsive rules.
   - **`FINAL-UI.md`** — the visual system: surfaces, type scale, grid, spacing,
     every component in every state, page layouts at 360 and 1440, photography
     direction.
   - **`FINAL-CONTENT.md`** — every user-facing string with a stable key, the
     voice definition and stop-list, every state and system message, meta tags.
     **Use these strings verbatim.** Do not write your own copy.
   - **`FINAL-SYSTEM.md`** — the token architecture with a complete
     `tokens.json` and the matching CSS custom properties, component
     specifications with measurements, and the acceptance checklist.
4. **`BRIEF.md`** — background only. Two errors in it are corrected in
   `LEAD-REVIEW.md` §4.

`working/` is the reasoning history. It never wins an argument.

**Brand assets** are in `02-brand/`: the brandbook, nine SVG lock-ups, PNGs and
the Illustrator source. `BRAND-NOTES.md` carries the palette and the two defects
found on acceptance — read it before you place a logo anywhere.

**The Figma file** shows 25 built screens and is the visual reference:
`https://www.figma.com/design/m1sxpu4Zxf8ANLre4FETOl`
Where the Figma canvas and a written specification disagree, **the
specification wins** — the canvas was corrected against it once already and may
drift again.

If two sources of equal rank disagree and you cannot settle it from a higher
rank, build nothing for that item and record it in `OPEN-QUESTIONS.md` with both
readings and your recommendation.

---

## 3. What to build

### Stack

Next.js 14+ App Router, TypeScript strict, plain CSS with custom properties.

No Tailwind, no CSS-in-JS runtime, no component framework underneath. The
reason is not taste: the client portal will eventually be built by a different
team on a stack we do not control, and a stylesheet plus custom properties is
the only contract that survives that handover.

### Routes

Take the sitemap and the slugs from `FINAL-UX.md` — do not invent your own.

Marketing site: home, pricing, how it works, sample report, family circle,
about, contact, and four legal pages, plus 404 and 500.

Client portal: entry after payment, visit list, visit report, guest report view
at a token URL, family circle and invitation, payment, payment pending, payment
failed, profile and settings, cancellation. Plus the bad-news screens — visit
postponed by weather, crew could not reach the plot, guarantee re-visit request.

### Desktop and mobile — both are deliverables

**Mobile-first is the build order, not the scope.** Every route ships a real
desktop layout as well as a real mobile one. A desktop page that is a stretched
phone page is a failed page.

Build each page at 360 first, because that is where the constraints bite and
where most of the traffic is. Then design up. Never the reverse: a layout
authored at 1440 and squeezed down always loses the fold arithmetic, and the
fold is where the request form lives.

What "a real desktop layout" means here, concretely:

- **Content is not full-bleed.** Text measure stays near 65 characters; the
  grid, margins and the signature two-column split are specified in
  `FINAL-UI.md` §4.1 — including the verification rail in its own columns with
  a deliberately empty column beside it. Use them.
- **The header changes, it does not scale.** At 360 it is a mark, a wordmark and
  a menu affordance at 56px tall. At 1440 it is the full horizontal lock-up,
  visible navigation and a primary action, at 72px. Both are specified.
- **Blocks that stack on mobile become columns on desktop** where the
  specification says so — the hero and its proof sheet, the three how-it-works
  cards, the three guarantees, the calculator's controls beside its result, the
  request form beside the contact block, the footer in three columns.
- **The report screen gains the rail.** On mobile the verification facts sit in
  a block; at `lg` and above they move into the rail beside the sheet. This is
  the layout the whole visual concept is built around — get it right.
- **1440 is the design width; the page must hold above it.** Cap the content
  container and let the ground extend. Test at 1920 and at 2560 — a band that
  keeps growing until the text measure breaks is a bug.
- **Between 600 and 900 nothing may be broken.** That range is tablets and
  small laptop windows, and it is where hand-built desktop layouts usually fall
  apart. Check it explicitly.

Both widths are gated: visual regression baselines exist at 360 **and** 1440
(§7.9), and the axe and locale checks run at both.

### Locales

Three, equal: **`hy` Armenian, `ru` Russian, `en` English.** Not two, not four —
French was dropped from Year 1.

Route them as the specification says. All three must be present and switchable
even where a translation is still a placeholder — and a placeholder must be
visibly marked, never silently English.

**Armenian sets taller and wider than Latin.** Lay every component out against
the longest locale, not against English. Anything that fits only in English is
broken.

### Data

There is no backend. Build against typed fixtures that mirror the real shapes:
plot, subscription, visit, report, member, invitation, payment. Put them in
`src/fixtures/` with the same names the specification uses, so swapping them for
an API is a single seam.

The consultation form posts to a stub endpoint that logs and returns success.
Leave a single clearly-marked integration point for HubSpot.

---

## 4. Non-negotiable rules

Every one of these comes from measurement recorded in `LEAD-REVIEW.md`, not from
preference. Violating any of them is a failed build.

1. **Olive `#7C8654` never carries text and never receives text.** 3.12 on Nude,
   3.42 on Ivory, 3.08 on Anthracite. Decorative fill only.
2. **Deep Olive `#575E3B` is the only interactive colour on light grounds** —
   links, accent text, primary button fill.
3. **Deep Olive is never used on Anthracite** — 1.75. On a dark ground the
   primary button is Nude fill with an Anthracite label.
4. **One functional colour exists: error `#8C3A2E`.** No success token, no
   warning token, and the naming must prevent one being added. Success and
   warning are expressed with words, glyphs and rule weight.
5. **Error red never sits on Anthracite** — 1.57, invisible. Therefore **a form
   may never be placed inside a dark band.** Enforce this in the `Section`
   component, not in a code comment.
6. **Surfaces:** Nude `#EFE5D5` is the page ground. Ivory `#F3F0E9` is objects —
   cards, sheets, forms, bars. They differ by 1.1 in contrast, so this is a rule,
   not a judgement: **Nude below, Ivory above.** Anthracite `#33373C` appears as
   at most two bands per page and never in the portal.
7. **Type floors:** nothing below 13px anywhere in any locale; 13px only for the
   decorative uppercase `overline`; informational text 14px minimum; body 16px
   minimum on mobile.
8. **Hit areas 44×44 minimum**, including invisible padding.
9. **Spacing is on the scale**
   `4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 72 · 80 · 96 · 128 · 144 · 160`
   and nothing else.
10. **Radii `0 · 2px · 8px · 9999px`.** 8px is for overlays only. Nothing else.
11. **No shadows** except one overlay elevation for modals, drawers and the
    lightbox.
12. **Section padding** per `FINAL-UI.md` §4.2, with the adjacency rule from
    `LEAD-REVIEW.md` §8: a light section following another light section opens
    at 0 and relies on the section above; a light section first after the header,
    or following a dark band, opens at its full value; dark bands always carry
    their full padding on both edges. Put this logic in the `Section` component.
13. **Cards in a row are equal height**, the row fixed to its tallest child, and
    a card's action pushed to its foot by a growing spacer — never by tuned
    padding. A card without a badge reserves the badge's height so titles align.
14. **Breakpoints 360 · 600 · 900 · 1200 · 1440.** 360 is the QA floor.

---

## 5. Two verified facts you must build around

**The dram sign `֏` (U+058F) is absent from Gloock, Cabin, Noto Sans and Noto
Serif.** Verified by rendering: the glyph does not fall back, it disappears.
Therefore the currency symbol is its own element with its own font stack:

```html
<span class="mc-price">160,000 <span class="mc-price__symbol">֏</span></span>
```

Ship a subset face for U+058F if no system font resolves it. Every price must
also be renderable as `160,000 AMD` — the word form is the default wherever the
glyph cannot be guaranteed, and the bank requires the letters anyway.

**Gill Sans, which the brandbook specifies, is a commercial Monotype face and is
not licensed.** Use **Cabin** — a humanist sans in the same tradition, on Google
Fonts — and label it in the code and the README as a substitute, so swapping it
later is a one-token change. Display face is **Gloock Regular**, single weight
only: build hierarchy from size, measure, colour and tracking, never weight, and
never set Gloock below 24px.

**Neither face covers Armenian.** Provide a documented fallback stack for
`:lang(hy)` and check Armenian pages in a real browser.

---

## 6. Content rules that change what you build

These are not copy notes. They constrain components and data models.

- **Invent nothing.** No testimonials, no counts, no "trusted by N families", no
  years in business. Do not build a testimonial component. Do not put a rating
  field on anything. The old site carried fabricated statistics and stock-photo
  testimonials with a recognisable actor's face — that is exactly what this
  build replaces.
- **Never render a QR code or a memorial page.** That product does not exist,
  not even as "coming soon".
- **Never claim to be the only ones.** hush.am has done grave care with photo
  reports in Yerevan since about 2015 and has roughly 72 reviews. Our position
  is the full combination — photo, video, GPS, portal, family circle — not
  exclusivity. No competitor is named on the site in any language.
- **`Optimal` is marked "Our recommendation", never "Most chosen".**
- **The guest report view renders no prices, no plans and no upsell** — gated
  server-side, not hidden with CSS. Model it as a distinct route and a distinct
  data projection so a stylesheet cannot defeat it.
- **A shared report's link preview never carries a photograph of a burial.** The
  OG image is mark, title and date only.
- **The deceased's name is off by default**, and turning it off must also remove
  it from links already shared.
- **Past reports stay readable after cancellation**, read-only, with no upsell.
- **Forbidden strings, in any language:** `monthly`, `bestseller`, `light
  visit`, `preventive visit`, `discount`, `save`, `most chosen`, `deceased`,
  `the departed`, `remains`, `object`, `disposal`. No exclamation marks, no
  emoji, no guilt constructions. Add a lint rule over the string files.
- **Currency shows `AMD` in words as well as the symbol.**
- **The two service promises are exact and identical everywhere they appear:**
  callback within one business day, report within 48 hours. Do not soften or
  sharpen them locally.
- **The refund is computed from the amount actually paid, never the list
  price**, by visits, rounded up to the nearest 100 ֏, and shown as arithmetic
  before confirmation. Computing from the list price refunds more than the
  client ever paid. The formula is in `LEAD-REVIEW.md` §5.

Placeholders you must render visibly, not silently omit: the legal address and
the registration number are not yet supplied, and both are bank requirements.
Every photograph is a labelled placeholder — report images 4:3 at 1600×1200,
marketing section images 3:2 at 1800×1200, crew portraits 1:1, video 16:9, link
previews 1.91:1.

---

## 7. Gates — automate every one, ship nothing that fails

1. **Contrast.** A test enumerates every text-on-surface pair the tokens permit
   and asserts ≥ 4.5. The closed list of allowed pairs is in `FINAL-SYSTEM.md`;
   a pair outside it fails the build.
2. **No literals.** No component stylesheet contains a hex, an rgb, or an
   off-scale spacing value. Enforce with a lint rule.
3. **Type floors** as in §4.7, checked against rendered output.
4. **Hit areas** ≥ 44×44 on every interactive element.
5. **All three locales** render every route with no overflow and no horizontal
   scroll at 360, 768, 1024, 1440 and 1920.
6. **The dram glyph** resolves, and the `AMD` word form is always available.
7. **Axe** reports zero violations on every route in every locale.
8. **Lighthouse** ≥ 95 for accessibility and best practices; full load under two
   seconds on a throttled connection. The current site takes 3.1 seconds and
   that is one of the things being fixed.
9. **Visual regression** baselines at 360 and 1440 for every route.
10. **The forbidden-string lint** passes over all three locale files.

Write `ACCEPTANCE.md` listing each gate with the command that proves it.

---

## 8. What you must not do

Do not redesign. Do not modernise the palette or add a colour. Do not introduce
a gradient, a shadow beyond the one overlay, or a pill-shaped button. Do not
substitute a component library for a specified component. Do not write your own
marketing copy — the strings exist. Do not put a before/after slider anywhere,
and never open a report with the "after" image: that is the register of
cleaning-product advertising and the specification forbids it.

If you believe a specified decision is wrong, implement it as specified and put
your argument in `OPEN-QUESTIONS.md`.

---

## 9. Order of work

1. Read the specification in the §2 order. Do not skim `LEAD-REVIEW.md`.
2. Scaffold the app, the routing and the three locales. Prove a page renders in
   all three before building anything real.
3. Tokens: `tokens.json` → CSS custom properties, three layers, with the lint
   rules that keep components on layer three.
4. Fonts, including the dram-symbol element and the Armenian fallback stack.
5. Layout primitives — `Section` first, carrying the adjacency rule and the
   no-form-on-dark rule.
6. The marketing site, page by page, verifying each at 360 before moving on.
7. The report screen. Give it the time it deserves; it is the product.
8. The rest of the portal, including every bad-news and empty state.
9. The gates in §7.
10. `README.md`, `ACCEPTANCE.md`, `OPEN-QUESTIONS.md`, and a written handover of
    what remains.

Work in small increments and verify continuously. Check every page at 360 in a
real browser, in Armenian, before you call it done.

---

## 10. Definition of done

A stranger opens the site on a phone, understands within one screen what is
sold and what proof they will receive, finds their price without calling
anyone, and submits a request in under a minute — in any of the three
languages, without a single contrast failure, and without encountering one
invented claim.

That is the bar. Not "it builds".
