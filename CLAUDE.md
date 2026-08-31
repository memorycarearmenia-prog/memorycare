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
- **Symbol — the brandbook mark, delivered 31.08.2026.** Source of truth:
  `assets/brand/brandbook/MemoryCare_brandbook.pdf` (page 2), rendered to
  `assets/brand/brandbook/page-2-logo.png`. Full-size art:
  `assets/brand/logo-v6/01-primary-on-dark-4500.jpg` and
  `02-primary-on-light.png` (both 4500²).

  The mark: two open hands in **Nude** cradling a five-petal
  **forget-me-not** (Անմոռուկ) in **Olive**, whose centre is a **woven
  interlaced medallion drawn as open line-work in Sky blue** — not a
  filled disc, and not cream as in the 29.08 book. Four lock-ups are
  delivered: primary logo (mark + wordmark + tagline), logo mark alone,
  wordmark alone, and two monochrome versions (all-dark on Nude,
  all-Nude on dark).

  ⚠️ **The wordmark is SINGLE-colour Olive.** The 29.08 rule that
  "Memory" is Ivory and "Care" is Olive is **retired** — in every lock-up
  in the new book "MemoryCare" is set in one colour: Olive on dark
  grounds, Dark Olive or Nude in the monochrome versions.

  The tagline "HONORING MEMORY, CARING FOR LOVED ONES" is set in
  **Sky blue**, uppercase, **no full stop** (that part of the 29.08 rule
  stands).

  ⚠️ Everything under `assets/brand/logo-final/` (the 27.08 "Version 5"
  set) and `assets/brand/logo/` is now **historical**. So are
  `forget-me-not-reference.jpeg`, `eternity-symbol-reference.jpeg` and
  `logo-reference.jpeg`. Do not pull the mark from any of them.
- **Colors — OFFICIAL, from the brandbook delivered 31.08.2026.**
  Source of truth: `assets/brand/brandbook/MemoryCare_brandbook.pdf`
  (page 3). **Five** colours, with the designer's own names and CMYK:

  | Name | HEX | CMYK |
  |---|---|---|
  | **Dark Olive** | `#212212` | 67 / 60 / 79 / 76 |
  | **Olive** | `#7C8654` | 52 / 34 / 78 / 12 |
  | **Nude** | `#EFE5D5` | 6 / 8 / 15 / 0 |
  | **Ivory white** | `#F3F0E9` | 3 / 3 / 7 / 0 |
  | **Sky blue** | `#D4ECF9` | 17 / 0 / 0 / 0 |

  **What changed from 29.08:** Olive, Nude and Ivory white are byte-for-byte
  identical. **Anthracite `#33373C` no longer exists** — the dark is now
  **Dark Olive `#212212`**, a near-black warm olive rather than a cool
  grey. **Sky blue `#D4ECF9` is new** and is the medallion and tagline
  colour. Anything built on `#33373C` must be rebuilt: Figma variables,
  the design-system kit, the report PDF template, `index.html`, the
  LinkedIn banner and avatar, and the six prompts already handed to other
  AIs, each of which embeds the old palette verbatim.

  Never use `#33373C`, the 27.08 pixel-sampled set
  (`#7E855C` / `#35363A` / `#EBE4D4`), `#5E6A3A`, `#6B7075`, `#FAFAF7`, or
  the retired Midnight Navy / Antique Gold / Celestial Blue scheme.

  ⚠️ **Sky blue is contested — the brandbook contradicts itself.** The
  colour page says `#D4ECF9`; every delivered vector, PNG, JPG and PDF
  paints the medallion and tagline **`#A4D6E8`**, and the book's own logo
  page renders as `#A4D6E8` too. Both pass on Dark Olive (13.18 vs 10.26)
  and both vanish on light, so this is about which blue the brand is, not
  about contrast. **Working value: `#A4D6E8`** — it is what the artwork
  physically contains and cannot be changed without re-exporting twelve
  files. Mariam must correct the colour page or re-export. See
  `assets/brand/logo-v6/README.md`.

  ⚠️ **Do not pixel-sample the JPEG.** Sampling
  `01-primary-on-dark-4500.jpg` returns `#14180C` for the ground and
  `#6B9532` for the petals — both wrong, the same trap that produced the
  bad 27.08 values. The PDF's stated hex codes are the only source.

  **Measured contrast (WCAG, threshold 4.5 for text):**

  | Pair | Ratio | Verdict |
  |---|---|---|
  | Dark Olive on Nude | 12.93 | pass |
  | Dark Olive on Ivory | 14.17 | pass |
  | Dark Olive on Sky blue | 13.18 | pass |
  | Nude on Dark Olive | 12.93 | pass |
  | Ivory on Dark Olive | 14.17 | pass |
  | Sky blue on Dark Olive | 13.18 | pass |
  | **Olive on Nude** | **3.12** | **fails** |
  | **Olive on Ivory** | **3.42** | **fails** |
  | **Olive on Sky blue** | **3.18** | **fails** |
  | **Olive on Dark Olive** | **4.14** | **fails for text; clears AA-large (3.0), which is why the wordmark works** |
  | **Sky blue on Nude** | **1.02** | **invisible** |
  | **Sky blue on Ivory** | **1.07** | **invisible** |

  Two structural rules follow, and both are unchanged in spirit from
  before: **Olive still never carries text and never receives text** — it
  is fills, petals, dividers and decorative panels only. And **Sky blue is
  a dark-ground colour**: it carries text beautifully on Dark Olive and
  disappears entirely on Nude or Ivory, where it may only be used as a
  tint fill (a panel, a chip ground, the medallion), never as type.

  The new dark is a genuine improvement — `#212212` on Nude measures
  12.93 against Anthracite's 9.61, and it is warm rather than grey, which
  suits the brand better.
- **Fifth interface colour — `#575E3B` "Deep Olive", WORKING VALUE,
  still needed.** Not in the brandbook; adopted by the owner 29.08.2026
  and re-verified against the new palette 31.08.2026.

  The reason it survives the palette change: on light grounds the body
  text is now Dark Olive, and Olive still fails at 3.12 / 3.42, so there
  is no brandbook colour that can mark a link or an accent apart from
  ordinary body text. Deep Olive does that job at **5.49 on Nude** and
  **6.01 on Ivory**, with **6.01** for Ivory on it and **6.84** for white
  on it. It is the same 72° hue and 23% saturation as Olive at lightness
  30% instead of 43% — the brand olive taken deeper.

  **Usage split — five brand colours plus this one, do not invent a
  seventh.**
  - On light grounds (Nude / Ivory): body text **Dark Olive**; links and
    accent text **Deep Olive**; primary button **Dark Olive fill with an
    Ivory label** (14.17) — this replaces the old Deep-Olive-fill button
    and removes one dependency on a non-official value; secondary button
    a Deep Olive hairline with a Deep Olive label.
  - On the dark ground (Dark Olive): text **Nude** or **Ivory**;
    accent and eyebrow text **Sky blue** (13.18); primary button **Nude
    fill with a Dark Olive label** (12.93).
  - **Deep Olive is never used on Dark Olive** — it measures 2.36 there.
  - **Olive** keeps its original job and only that: fills, petals, the
    tagline in print lock-ups, dividers, decorative panels.
  - **Error `#8C3A2E`** is unchanged and still passes on light
    (6.10 / 6.69) and is still invisible on the dark ground (2.12) —
    so the consultation form may still never sit inside a dark band.

  Deep Olive exists **only in the interface**. The logo and the brandbook
  are untouched by it.

  ⚠️ Nude and Ivory white differ by only 1.10 in contrast — near identical
  to the eye. The convention, written down so they stop being used
  interchangeably: **Nude is the page ground, Ivory is the objects that
  sit on it** (cards, the report sheet, inputs) and the light label on
  dark fills.
- **Typography — from the brandbook, 31.08.2026. Both earlier problems
  are solved.** Display: **Ghea Mariam**. Text: **Montserrat** (the
  Armenian sample is labelled **Montserrat Arm**, a separate family —
  the font stack must name it explicitly, it is not a subset of the Latin
  family).

  **Gloock and Gill Sans are both retired.** This removes the two blocking
  issues recorded on 29.08: there is no longer a commercial Monotype
  licence to buy, and both faces are shown in the book covering **Latin,
  Cyrillic and Armenian** (Aa / Аа / Աա) — so the Armenian site no longer
  falls back to a system font. Type tokens can now be built.

  In the lock-ups: the wordmark is Ghea Mariam, the tagline is Montserrat
  uppercase with wide tracking.

  Still unverified, because this session has no outbound network: whether
  either family contains **֏ (U+058F)**. Montserrat Arm is the likely
  carrier. Keep the currency symbol as its own element with its own font
  stack so a missing glyph degrades for that one character instead of
  breaking the price.
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

0. **The 31.08 brandbook invalidates a lot of built work.** Anthracite
   `#33373C` is retired, Sky blue `#D4ECF9` is new, and the type pair
   changed. The Figma file, the four specifications, all six prompts
   handed to other AIs, the design-system kit, `index.html`, the report
   PDF template and the LinkedIn assets all embed superseded values and
   need rebuilding. Checklist:
   `assets/brand/BRANDBOOK-CHANGE-2026-08-31.md` §5.


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
