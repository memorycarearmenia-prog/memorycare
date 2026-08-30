# Memory Care — website project context

This file is auto-loaded by Claude Code at the start of every session in this
repo. It is the source of truth for brand, pricing, and copy facts.

> **Superseded 2026-08-13 by the business archive.** The owner confirmed
> `docs/PROJECT-MEMORY-FULL.md` (digest of
> `MemoryCare-Full-Archive-2026-08-12.zip`, dated 06–12.08.2026) is the
> **current source of truth for the whole business** — company, product
> line, pricing, slogan, languages, ops, legal, financials. Everything
> below has been rewritten to match it. **Do not fall back on
> `docs/BUSINESS-CONTEXT.md`, `docs/site-update-prompt.md`,
> `docs/site-update-prompt-professionalism.md`, or any pre-2026-08-06 note
> in this file's git history** — those describe an earlier, now-superseded
> round of decisions (old slogan "The care that matters.", 3 tariffs,
> 4 languages) and have not been reconciled with the archive. Treat them as
> stale until someone rewrites them to match `docs/PROJECT-MEMORY-FULL.md`.
> If a file in this repo (old component, old copy, one of the docs just
> named) disagrees with `docs/PROJECT-MEMORY-FULL.md`, **the memory file
> wins** — flag the mismatch to the user instead of trusting the stale doc.
>
> `docs/PROJECT-MEMORY-FULL.md` also carries the full non-website detail
> (legal status, financial model, field/chemistry protocol, hiring, vendor
> contracts, decision timeline, calendar) that doesn't belong in this
> website-focused file — read it directly for anything beyond brand/pricing/
> copy.

## What this business is

Memory Care LLC (Armenia, Yerevan) — a subscription service for
professional care of family memorial plots on Yerevan cemeteries, with
photo/video/GPS-verified visit reports through a client portal. Add-on for
Year 2 only (out of Year-1 scope entirely, not even as "optional"): a QR
code on the headstone linking to a digital memory page (gallery +
biography + guestbook) — do not build or mention it in Year-1 site work.

**Audience — both segments, one brand, one page:** (1) Armenian diaspora
(US, France, Russia, rest of Europe), 35–60, established, emotional
driver: guilt over distance. (2) Local premium segment in Yerevan, 40–60,
above-average income, rational driver: lack of time. Do not split into a
diaspora version and a local version, and do not write diaspora-only copy
("across the miles," "cheaper than flying yourself") — lead with the
outcome, then name both reasons naturally. (The business archive's own
market-sizing work leans diaspora-heavy for SAM math, but the product
brief itself still frames both personas without ranking one above the
other — keep the universal-messaging rule.)

**Tone:** light premium minimalism — lots of white space, large
typography, restrained "editorial" elegance, warm but professional.
Explicitly NOT funeral-cliché (no dominant black, crosses, gothic
lettering, candles), NOT guilt-pressure, NOT sentimental, NOT cold
corporate. References the team likes: tending.app, headspace.com,
stripe.com, airbnb.com.

## Brand identity

- Name: **MemoryCare** (one word, mixed case). Legal entity: Memory Care
  LLC. This is the **only** element that never changes under any
  circumstances — logo, palette, and every other visual choice are the
  designer's territory to challenge with justification.
- **Slogan: "Honoring Memory, Caring for Loved Ones."** — used
  consistently across all 30+ archive documents through 11.08.2026,
  including the latest designer brief update. Localize per-language as
  needed; no separate localized slogan lines have been finalized yet in
  the archive (unlike the old, now-superseded "The care that matters."
  set — don't reuse those HY/RU/FR lines).
- **Symbol — FINAL, approved by both owners 27.08.2026.** Master
  reference: `assets/brand/logo-final/00-MASTER-version5.jpg` ("Version
  5"), usage notes in `assets/brand/logo-final/README.md`. The mark: a
  five-petal **forget-me-not** (Անմոռուկ) whose centre is a **woven
  interlaced medallion**, held between **two open hands**. Wordmark
  "MemoryCare" in a high-contrast serif, tagline below in olive small
  caps.
  ⚠️ **Corrected 29.08 from the designer's brandbook** (`assets/brand/
  brandbook/MemoryCare_brandbook.pdf`): the wordmark is **two-colour** —
  "Memory" in Ivory white, "Care" in Olive — not single-colour as this
  file previously said. Monochrome lock-ups exist for one-colour use.
  The tagline carries **no full stop**: "HONORING MEMORY, CARING FOR
  LOVED ONES" is set without a final period, consistently across every
  delivered file. The earlier "period is mandatory" rule is retired.
  ⚠️ For anyone reading older notes: earlier drafts specified the
  aravakhach as an 8-blade pinwheel and forbade calling it "rings" or
  "woven". The owners deliberately changed this — the final centre IS a
  woven medallion. Old files (`assets/brand/forget-me-not-reference.jpeg`,
  `eternity-symbol-reference.jpeg`, `logo-reference.jpeg`) are historical
  only, superseded by the master above.
- **Colors — OFFICIAL, from the designer's brandbook, received 29.08.2026.**
  Source of truth: `assets/brand/brandbook/MemoryCare_brandbook.pdf`.
  Four colours, with the designer's own names and CMYK:

  | Name | HEX | CMYK |
  |---|---|---|
  | **Olive** | `#7C8654` | 52 / 34 / 78 / 12 |
  | **Nude** | `#EFE5D5` | 6 / 8 / 15 / 0 |
  | **Ivory white** | `#F3F0E9` | 3 / 3 / 7 / 0 |
  | **Anthracite** | `#33373C` | 74 / 64 / 57 / 52 |

  These replace **every** earlier value in this repo, including the
  27.08 pixel-sampled set (`#7E855C` / `#35363A` / `#EBE4D4`) — those
  were measured off a JPEG and are wrong; delete them wherever found.
  Note that Olive and Anthracite match the pre-27.08 palette exactly
  (hover olive `#7C8654`, anthracite `#33373C`), so the older notes
  were closer than the sampled ones. Still do not use `#5E6A3A`,
  `#6B7075`, `#FAFAF7`, or the retired Midnight Navy / Antique Gold /
  Celestial Blue scheme. Anything built on any superseded hex needs
  rebuilding: Figma tokens, LinkedIn banner and avatar, design-system
  components, the report PDF template, `index.html`.

  ⚠️ **Accessibility gap.** Measured against WCAG on the official values:
  Olive gives 3.12 on Nude, 3.42 on Ivory, 3.08 on Anthracite, and Ivory
  on Olive is 3.42. The threshold for text is 4.5, so **Olive cannot
  carry text on any background and no text is legible on Olive** — an
  olive button with a light label fails. In the mark itself this is
  irrelevant (large forms), but every interface use is affected.
- **Fifth colour — `#575E3B` "Deep Olive", WORKING VALUE adopted by the
  owner 29.08.2026**, pending the designer's own value. It is not a new
  hue: same 72° hue and 23% saturation as Olive, lightness 30% instead of
  43% — the brand olive taken deeper. Approximate CMYK 7 / 0 / 37 / 63
  (the designer should recompute in her profile). It clears AA in every
  direction with ~20% margin: 5.49 as text on Nude, 6.01 on Ivory, 6.01
  for Ivory on it, 5.49 for Nude on it, 6.84 for white on it.

  **Usage split — one extra colour is enough, do not invent a sixth.**
  On light grounds (Nude/Ivory): body text Anthracite; links and accent
  text Deep Olive; primary button = Deep Olive fill with an Ivory label.
  On dark ground (Anthracite): text Nude or Ivory; primary button = Nude
  fill with an Anthracite label (9.61). Deep Olive is never used on
  Anthracite — it disappears there (1.75). Olive keeps its original job
  and only that: fills, petals, the tagline, dividers, decorative
  panels — it never carries text.

  Deep Olive exists **only in the interface**. The logo and the brandbook
  are untouched by it.

  ⚠️ Nude and Ivory white differ by only 1.1 in contrast — they are near
  identical to the eye. Which is background and which is type-on-dark
  needs to be written down, or they will be used interchangeably.
- **Typography — from the brandbook, 29.08.2026.** Display:
  **Gloock Regular** (Google Fonts, free, single weight only). Text:
  **Gill Sans**.
  ⚠️ **Two unresolved problems, both raised with the designer.**
  (1) Gill Sans is a commercial Monotype typeface — a web licence must be
  bought, and embedding in an app and in PDFs is licensed separately.
  (2) **Neither face covers Armenian**, and Armenian is the primary
  market and one of three equal site versions. Without a companion that
  carries Armenian, Cyrillic and Latin, the Armenian site will fall back
  to a system font. Do not build type tokens on this pair until the
  designer confirms coverage or proposes a companion.
- **Languages — THREE on launch: ARM / ENG / RUS.** French has been
  explicitly dropped from Year-1 scope (decided repeatedly across the
  06–11.08 documents — business plan, GTM, dev spec v2.0, designer
  update). Do not build or promise a 4th (FR) language switcher for
  Year 1; it may return later but there is no scoped work for it now.
  Mobile-first: diaspora traffic is majority mobile.
- Main site CTA: a free-consultation request (name + phone/WhatsApp), not
  a direct purchase — the annual subscription amount is significant enough
  that the decision happens after a conversation. Online payment via
  international cards is the secondary path, not primary.

**Live reference site:** `memorycarearmenia.netlify.app` was last
confirmed live 2026-08-02, before this slogan/pricing/language reset — its
content (old slogan, old 3-tariff pricing, 4-language switcher) should be
assumed **stale relative to the archive** until someone re-verifies it
against `docs/PROJECT-MEMORY-FULL.md` and updates it. Don't treat it as
current truth. This repo's `index.html` is a separate parallel/reference
build for design-system exploration and can drift from both the live site
and the archive — don't assume it matches either without checking.

A real platform (client portal + payments + reports, not just the
marketing site) is separately in development by an outside contractor,
target readiness ~20.09.2026 — see `docs/PROJECT-MEMORY-FULL.md` §8 for
its spec. The marketing site and that platform are related but distinct
workstreams; don't conflate them.

## Pricing — locked, do not change without explicit instruction

Four products, flat single price for every client (no plot-size surcharge,
no local/diaspora price difference):

| Tariff (Armenian client-facing name) | Composition | Price | Role |
|---|---|---|---|
| **Զննում** (Inspection) — new tariff | 1 visit by the light team: photo/video of current condition + priced list of recommended work. No cleaning performed | 20,000 ֏ | Low-risk entry point + operational recon (locks in the plot's GPS point for field teams). Credited toward any package if purchased within 30 days |
| **Էքսպրես խնամք** (Express) | 1 heavy/deep visit | 60,000 ֏ | Trial. Credited toward a subscription within 60 days. If not converted, a repeat Express in the same calendar year costs 40,000 ֏ (not 60,000) |
| **Օպտիմալ խնամք** (Optimal) — flagship/bestseller | 2 heavy + 4 light visits (6/yr) | 180,000 ֏ | Expected ~55% of the subscription mix |
| **Մաքսիմում խնամք** (Maximum) | 3 heavy + 6 light visits (9/yr — NOT 12, and never described as "monthly") | 240,000 ֏ | Premium tier |

Currency: prices are in AMD; if showing $/€ reference figures, mark them
clearly as approximate/indicative — the actual charge is in AMD. A live
FX API is a nice-to-have, not required for launch.

## Site sections

1. Hero — the offer, with GPS/verified-reporting visual proof front and
   center (a before/after report example belongs on the first screen).
2. Тарифы — four tariffs above, "Զննում" visually set apart from the three
   annual packages (it's a one-off, not a subscription, and should read
   that way), Optimal marked as the leading choice (do not use the literal
   word "bestseller" in Armenian copy — use "առաջատար" or similar).
3. Отчёт / "как выглядит доказательство" — a sample report screen; this is
   the actual product, treat it with real visual weight.
4. Как это работает — subscribe → visits → photo/video/GPS report. **No
   QR mention anywhere** — Year-2 scope only.
5. "Семейный круг" — family members get their own sub-account via invite,
   see all reports, can order one-off services; this ships with the
   platform, not deferred to Year 2. This is the core differentiator vs.
   every world analog (Tending, Grabpflege, Styks, GraveCareUkraine) — none
   of them combine photo+video+GPS+portal+family-circle.
6. Блок доверия — verification, regularity, transparency, for both
   audiences (not diaspora-only trust signals).
7. Language switcher — ARM/ENG/RUS only (see Languages above).
8. Clear CTA — free-consultation request as primary, "choose a package" /
   online payment as secondary.

## Known open TODOs

Real contacts are now in place (see `docs/PROJECT-MEMORY-FULL.md` §1):
Davit Hambardzumyan (CEO) +374 55 315 323, Hayk Manukyan (CBDO)
+374 93 154 108, info@memorycare.am active since 11.08, corporate phone
line active since ~12–17.08 with WhatsApp Business. If the live site or
`index.html` still show placeholder contacts (`+374 10 00 00 00`, a Gmail
address), that's now stale and should be replaced.

1. Real geo-tagged before/after photos — still placeholders as of the
   archive; professional shoot (drone + camera, budget allocated) planned
   during the September pilot.
2. Reconcile this repo's site content (slogan, pricing, language switcher,
   contacts) against the facts in this file and in
   `docs/PROJECT-MEMORY-FULL.md` — assume it's out of date until checked.
3. `docs/BUSINESS-CONTEXT.md`, `docs/site-update-prompt.md`, and
   `docs/site-update-prompt-professionalism.md` still describe the old
   (now-superseded) slogan/pricing/4-language setup and have not been
   rewritten — do not use them as a source, and flag to the user if asked
   to update them.
4. Mobile view quality — confirm it matches desktop; mobile is the primary
   channel for this audience.
5. Bank requirements for the site (8 items — About page, contacts in every
   footer, full service descriptions, legal restrictions, real AMD prices,
   English privacy policy, return policy, service-delivery terms) are a
   hard condition for enabling Ameriabank card acceptance — see
   `docs/PROJECT-MEMORY-FULL.md` §8. Don't ship a site copy pass without
   checking these are covered.
6. QR-memorial page — Year 2 only, a separate owner decision after Year 1;
   do not build, mention, or hint at it as "optional" in Year-1 material.

## Things NOT to invent

- Don't invent client testimonials, review counts, or "X families trust
  us" stats — the company is pre-launch (September pilot of 5–10 paid
  visits is the first real client work; 0 paying customers as of the
  archive). Use aspirational/process-trust copy instead ("verified
  visits," "GPS-tagged reports"), not fabricated social proof.
- Don't add pricing tiers, discounts, or visit counts beyond the table
  above without the user confirming it first.
- Don't reintroduce the retired slogan ("The care that matters." and its
  HY/RU/FR localizations), the old 3-tariff pricing, or the 4th (FR)
  language without an explicit new instruction from the owner — all three
  were live decisions before 06.08.2026 and were superseded by the
  business archive.

## Market research / social listening (2026-08-19) — read before market claims

A deep internet-monitoring pass (11 researchers: 10 specialized agents +
lead, ~282 verified findings across EN/RU/HY) was completed 19.08.2026.
Full results: `RESEARCH-FINAL-REPORT.md` and
`RESEARCH-ALL-FINDINGS-282.md` in the repo root (working copies with the
same content plus keyword lists and the 11 per-researcher reports live in
`docs/social-listening/`). Key facts that AFFECT existing claims in this
file:

1. **hush.am is an established DIRECT competitor in Yerevan** (since
   ~2015): cemetery-records database, GPS grave locating, one-year care
   package (4 visits: grass trimming, headstone cleaning, tidying,
   flowers) with before/after photo reports, Google Play app, ~72 reviews
   (94% recommend), US (818) phone → explicitly targets the LA/Glendale
   diaspora. The "no world analog combines photo+video+GPS+portal+
   family-circle" claim in §"Семейный круг" technically still holds (hush
   has no video reports, no client portal, no family sub-accounts, no
   subscription tiers), but **never claim "no one does grave care with
   photo reports in Yerevan"** — that is false. Position on the FULL
   combination + verification rigor + premium brand.
2. **Find a Grave has open, unfulfilled photo requests for Yerevan
   cemeteries** (Tokhmakh, Zeytun, etc.) — documented diaspora demand;
   also a channel/audience for outreach.
3. **"Memory care" in English is semantically owned by the dementia-care
   industry** (searches for "MemoryCare Armenia" surface Alzheimer's Care
   Armenia). SEO must use compound queries ("MemoryCare grave care
   Yerevan"), not the bare brand phrase.
4. The **gravestone-cleaning video genre** (TikTok/YouTube; one video
   ~140M views) is a proven content format: before/after + the person's
   story, dignity-first tone (cheerful tone caused public backlash —
   NBC-covered controversy).
5. Regional RU-language markets (Belarus, Ukraine) publish per-service
   price lists — pricing-communication benchmarks exist in
   `RESEARCH-ALL-FINDINGS-282.md`.

Caveats recorded in the reports: session search limits and egress blocks
meant hush.am/findagrave.com/tending.app figures come from search-snippet
evidence — manually verify exact numbers before quoting them publicly.
TikTok interiors, private FB groups, Telegram, VK were not searchable.
