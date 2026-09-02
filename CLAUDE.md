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

- Name: **MemoryCare** (one word, mixed case).

  ⚠️ **The legal entity's exact registered spelling is UNCONFIRMED and is
  a bank blocker.** Three sources give two answers: this file and
  `PROJECT-MEMORY-FULL.md` §1 say **Memory Care LLC** (two words); §3 of
  the same archive hedges — "MemoryCare LLC / Memory Care"; and the 31.08
  audit's FINDINGS #19 states the standing rule is **MemoryCare LLC** (one
  word) and treats the two-word form on the live site as a defect.

  Nobody has opened the registration certificate. Whatever the site prints
  must match it **exactly** — a mismatch between the site and the registry
  is among the most common reasons a bank submission is returned, and
  acquiring is on the critical path to October revenue. → Davit, with the
  certificate in hand. The **registration number appears nowhere in this
  repository**, and the address `0051, Komitas 47/1, bldg 9, Yerevan` is
  recorded but flagged as needing the lawyer's confirmation.

  The brand name is the **only** element that never changes under any
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
  | Dark Olive on Sky blue | 10.26 | pass |
  | Nude on Dark Olive | 12.93 | pass |
  | Ivory on Dark Olive | 14.17 | pass |
  | Sky blue on Dark Olive | 10.26 | pass |
  | **Olive on Nude** | **3.12** | **fails** |
  | **Olive on Ivory** | **3.42** | **fails** |
  | **Olive on Sky blue** | **2.48** | **fails — and fails the 3.0 non-text floor too** |
  | **Olive on Dark Olive** | **4.14** | **fails for text; clears AA-large (3.0), which is why the wordmark works** |
  | **Sky blue on Nude** | **1.26** | **invisible** |
  | **Sky blue on Ivory** | **1.38** | **invisible** |

  ⚠️ **Corrected 02.09.2026.** Every Sky-blue row above was previously
  computed against `#D4ECF9`, the value printed on the brandbook's colour
  page — while the working value is `#A4D6E8`, what the artwork actually
  paints. Three of the corrections are harmless. **One is not: Olive on
  Sky measured 3.18 in the old table and is 2.48 in reality.** The old
  number said an Olive rule or mark on a Sky panel cleared the 3.0 floor
  a meaningful non-text graphic needs. It does not. Anyone trusting that
  row would have drawn an invisible divider.

  If the designer rules for `#D4ECF9`, recompute this table again rather
  than reverting it from memory.

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

## The contractor's site — the 02.09.2026 audit is current truth

`mc.makyan.com`, Igor's build. **`docs/site-audit-2026-09-02/` is the most
complete pass and supersedes the 28.08 and 31.08 archives.** 380
screenshots, 36 route×locale DOM captures, axe and Lighthouse per route,
public **and authenticated** — the owner supplied a login. Screens and DOM
are gitignored (92 MB); everything else is committed.

The public site is byte-for-byte unchanged since 31.08: Lorem Ipsum as the
English `h1` and translated into the other two locales, the four invented
proof figures, the withdrawn `40,000 ֏` price, `user-scalable=no`.

**What the login hides — these change decisions, so they live here:**

- **Changing the password requires no current password.** One submit
  changes password, e-mail and phone. A borrowed session becomes permanent
  account takeover and the owner loses the recovery address at the same
  moment.
- **The amount travels in a hidden field on both money forms**
  (`price=180000`, `price=240000`). Whether the server re-derives it is
  untested — testing meant creating a real order.
- **The order form has no visible field at all.** A customer subscribes to
  a year of grave care without ever saying which grave. There is no plot
  object and no way to create one.
- **Nothing can be cancelled anywhere** — no button, no dialog, in any
  locale. Ameriabank requires published cancellation terms.
- `/{loc}/account/payments/` — a sidebar item shown to paying customers —
  **404s**. Two endpoints are hard-coded to `/am/`, including the pay
  endpoint, so a Russian customer gets Armenian responses at the moment
  money moves. On a 360px screen the Pay button sits at `left: 371px`,
  entirely off-screen.
- The account area scores **52–57** on accessibility against 81 for the
  public pages.
- Nineteen routes answer 200 while rendering a 404. `robots.txt` and
  `sitemap.xml` do not exist, and all 36 pages carry `INDEX, FOLLOW`.
- The variable webfont is downloaded **twice per page and applied to
  nothing** — the whole site renders in `system-ui`.

⚠️ **Four claims in our earlier reports were overturned. Do not repeat
them.** Full account in
`docs/site-audit-2026-09-02/CORRECTIONS-TO-OUR-CLAIMS.md`.

1. **The dram sign does not fall back on the live site.** Digits and ֏
   measure an identical stack, size and weight. The claim reached
   `CLAUDE.md`, the developer handover, two prompts and three replies
   before being tested.
2. **The reviews carousel does advance.** All six slides carry identical
   text and only the photograph changes, which fooled a byte comparison.
3. **The testimonial names are the literal placeholder `Անուն Ազգանուն`,
   and there are six, not three.** The substantive problem — photographs
   of people presented as customers of a company with none — stands.
4. **CLS is 0.099 on desktop**, not the 0.000 we quoted from the mobile
   profile. Desktop is now the whole scope.

Not covered by that audit, with a procedure to close it in its
`03-GAPS.md`: nothing was submitted, no payment made, and logout and
post-logout session behaviour were not tested.

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

## Pricing — the owner's decision of 26.08.2026

⚠️ **This table replaces the one that stood here until 01.09.2026.** The
old table (60,000 / 180,000 / 240,000, a light-visit/heavy-visit split,
30-day credits, a 40,000 repeat Express, four products) was superseded by
the owner on **26.08.2026** and this file was never updated.
`docs/TARIFF-REDESIGN-2026-08-26.md` §8 names this very section as
outdated; the 31.08 site audit independently treats the 26.08 line-up as
the expected one. The stale table was circulated to a design team on
01.09 before the error was caught. **`docs/TARIFF-REDESIGN-2026-08-26.md`
is the source of truth for pricing** — read it for the reasoning, the
calculator table and the rejected ideas.

**All visits are full visits.** The light/heavy distinction is
**rejected** — "все визиты полноценные". Do not use those words anywhere.

| Product | Composition | Price |
|---|---|---|
| **Զննում** (Inspection) | One orientation visit: find the cemetery and the plot, full written inventory, photo/video of the condition, list of the work needed, quote for minor repair. **No cleaning.** | **20,000 ֏** |
| **Էքսպրես** (Express) | One full visit: deep cleaning of the whole plot and monuments — steam cleaner, professional neutral-pH chemistry, wet/dry vacuum. **No high-pressure washing on a monument.** Photo/video reports, portal access. Express is the atomic unit; subscriptions are counted in them. | **65,000 ֏** |
| **Օպտիմալ** (Optimal) — flagship | Annual: **4 full visits, one in each season** | **160,000 ֏ / year** |
| **Մաքսիմում** (Maximum) | Annual: **6 full visits** | **200,000 ֏ / year** |
| **Հատուկ խնամք** (Special) | Non-standard: more visits (e.g. 12/yr), plot over 16 m², more than two monuments, several family plots on different cemeteries. **Always begins with a Զննում.** Fifth card on the site. Internal floor: a Special visit is never cheaper than a Maximum visit (~33,333 ֏). | **calculator / consultation** |

⚠️ **Never write "Kärcher" as shorthand for the cleaning method.** The word
names both our chemistry (RM 623, neutral pH ~7) and three machines, one of
which is a pressure washer — and **high-pressure washing is forbidden on
monuments**: above 500 psi it irreversibly damages polished granite, lalvar
and basalt, and tuff tolerates no more than 100 psi. The K 7 is for paths,
fences and hardstanding only, never a headstone (owner's clarification,
13.08.2026). Copy that lists "Kärcher" beside "deep cleaning" reads as
pressure-washing a grave — wrong, and alarming to anyone who knows stone.
Describe the method: steam, neutral chemistry, vacuum.

**Credits — three separate rules, all owner decisions of 26.08:**

- Զննում 20,000 ֏ is credited **only on signing an annual subscription**,
  within **60 days**. It is **not** credited into an Express.
- Express 65,000 ֏ is credited in full into an annual subscription within
  **60 days**.
- **One credit only:** on signing, **either** the Զննում **or** the
  Express is credited — never both. A client who bought both gets the
  larger (65,000); their Զննում stays a paid inspection. No credits
  between one-off products.

**There is no discounted repeat Express** — always 65,000 ֏. A repeat at
40,000 / 45,000 was considered and **rejected 26.08** for devaluing the
subscription. The live site still sells 40,000 ֏, which the audit calls a
blocker.

Also decided 26.08 and not yet reflected elsewhere: a **price calculator**
on the tariffs page (open formula, two sliders, same price for everyone,
visible before any call); report **sharing by plain link** in
WhatsApp/Viber as an option alongside the portal; a **day-before
notification** as an opt-in, not a default; and an **assigned crew** as a
service standard worded as assignment, never as a guarantee of unchanging
personnel.

Optimal sells in one sentence: **"four full visits, one in each season."**
The winter visit runs in a weather window, not on a date — the protocol
limit is temperature. **Four visits are guaranteed regardless**: if no
window opened, the visit is **added** to spring. That is a contract term,
not a failure. "Monthly" remains forbidden. Optimal is marked "Our
recommendation" (Armenian **`Մեր խորհուրդը`**), never "bestseller" —
zero customers.

⚠️ **`առաջատար` is REJECTED — 01.09.2026, on the Armenian writer's
ruling.** It means *market leader*, not *our recommendation*. As a badge
on a tariff card it makes, on the Armenian site, precisely the claim the
English and Russian sites are forbidden to make — and it is falsifiable
by anyone who has found the incumbent. Use **`Մեր խորհուրդը`** ("our
recommendation", 13 characters). The instruction to use `առաջատար` stood
in this file and in both team briefs and was propagated to five
specialists before a native writer caught it.


Flat price at any plot size for the standard products. Prices are AMD; any
$/€ figure must be marked approximate. A live FX API is a nice-to-have,
not required for launch.

⚠️ **Downstream documents still carrying the old line-up** (per
`TARIFF-REDESIGN` §8): the financial model v6.0, the client contract with
the lawyer, Igor's platform spec, and the designer's tariffs page. The
design package's `FINAL-CONTENT.md` carries yet a third variant. These
have not been reconciled.
## Site sections

1. Hero — the offer, with GPS/verified-reporting visual proof front and
   center (a before/after report example belongs on the first screen).
2. Тарифы — four tariffs above, "Զննում" visually set apart from the three
   annual packages (it's a one-off, not a subscription, and should read
   that way), Optimal marked as the leading choice (do not use the literal
   word "bestseller" in Armenian copy — use **`Մեր խորհուրդը`**; do NOT
   use `առաջատար`, which means market leader).
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

## Developer handover — runnable

`build/` holds the implementation the developers build from:
`tokens.css` and `tokens.json` (the same values, generated together so
they cannot drift), `home.html` — a **running** page carrying the header,
the hero and the tariff row on those tokens — the brand SVGs, and
`HANDOVER.md`.

`home.html` is the reference implementation, not a mockup. The Figma file
is the design record; this is the code.

⚠️ **The dram sign — corrected 02.09.2026.** ֏ (U+058F) is **present in
GHEA Mariam**, verified by reading the cmap of all four supplied files
(`assets/fonts/ghea-mariam/`). It is **absent from Montserrat**. Since the
`price` and `price-xl` roles are set in the display face, **a price
renders ֏ natively with no fallback.** Only ֏ inside Montserrat text — the
arithmetic line, the rail, body copy — still needs the isolated
`unicode-range: U+058F` slice, and that slice can now point at GHEA
Mariam, which we own.

⚠️ **An earlier claim here was wrong and is withdrawn.** This file
previously stated that the live site renders ֏ at a visibly different
weight and size from the digits beside it. The 02.09 audit measured both
runs separately and found an **identical** declared stack, size and weight
— the live site sets everything in `system-ui`, so the digits and the sign
come from the same place. The glyph is narrower because that is how the
character is drawn. The claim came from the 31.08 audit, I repeated it as
verified fact, and it was not supported by the evidence behind it.

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
