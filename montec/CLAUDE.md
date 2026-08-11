# MONTEC — quiet luxury leather accessories — project context

This file is the source of truth for MONTEC brand, product, and copy facts,
scoped to this `/montec/` folder. **MONTEC is a separate business from
Memory Care** (the grave-care subscription service covered by the repo-root
`CLAUDE.md`) — the two share this repository for convenience only, kept in
fully separate top-level folders, no shared brand/copy/pricing facts. Don't
let context from the root `CLAUDE.md` bleed into MONTEC work or vice versa.

If a file under `/montec/` disagrees with this file, **this file wins** —
flag the mismatch to the user instead of trusting stale copy.

## Canonical product reference photos (locked rule, per the user 2026-08-02)

`montec/assets/products/<sku>/turnaround-grid.png` are the **эталонные**
(reference/canonical) photo cards for every Batch 001 product — one
9-panel studio turnaround per SKU, folder named in kebab-case (e.g.
`the-founder`, `the-treasury`, `the-closer`). **Whenever a product name
comes up in conversation or in a task, look at (or recall) its
turnaround-grid image before describing, designing around, or writing
copy about that product** — these images are the ground truth for what
each product actually looks like (silhouette, hardware, logo placement,
color), not the text descriptions alone. `the-capital/` has two renders
(`turnaround-grid.png` + `turnaround-grid-alt.png`); treat
`turnaround-grid.png` as primary unless told otherwise.

## What this business is

MONTEC — a quiet-luxury leather accessories brand for business and finance
professionals. Designed in Armenia; made from 100% full-grain, vegetable-
tanned Italian leather with Italian brass hardware throughout (confirmed
2026-08-02 via the user's own product-concept documents — see Reference
materials below). Exact tannery name and manufacturing location (Armenia
vs. Italy vs. elsewhere) still not locked — see Open TODOs. Targets the
local Armenian premium market and international/export markets **equally**
— no single audience gets default messaging (same principle the Memory
Care project already learned the hard way: don't write copy that reads as
excluding one segment).

## Company & team structure (confirmed 2026-08-02)

- **Parent company: FiCorp.** Owners: **Ararat** and **Taron**. (Note:
  "Ararat" here is an owner's personal name, coincidental with the
  Ararat/mountain symbolism discussed under Name & positioning below —
  don't conflate the two or assume the brand story references the owner.)
- **The user (this conversation) is MONTEC's biz dev — and also the
  "founder" referenced in the Business Plan / GTM / Financial Model
  narrative** (confirmed 2026-08-02, resolving a discrepancy — those
  planning docs describe "the founder" personally producing pieces and
  operating both leather workshops; that founder role is the user).
  Artem and Levon are additional craftsmen who exist alongside/beyond
  the founder's own hands-on capability, not a contradiction of it.
- **Artem** — master craftsman (мастер).
- **Levon** — second master craftsman, based in **Kapan** (Syunik region,
  Armenia). Levon is **becoming the primary/main craftsman** — i.e. a
  transition is underway from Artem to Levon as lead maker. Don't assume
  Artem is out of the picture entirely unless told so explicitly; the
  user only said Levon is becoming the main one.
- **Labor cost model (confirmed 2026-08-02):** Artem/Levon are paid
  **per order/piecework, not a fixed salary** — there is no labor cost
  while there are no orders. This is why the Financial Model's
  "near-zero fixed cost, make-to-order" logic holds even with named
  craftsmen in the picture — their pay is a variable COGS line, not
  fixed opex.
- **Sales channel:** primarily **B2B**, but not exclusively — don't design
  the site/funnel as if it's B2C-only; keep B2B enablement (wholesale
  inquiries, bulk/corporate gifting, etc.) in scope alongside any direct
  consumer path. Corporate gifting is confirmed (2026-08-02, via the new
  planning docs — see "New planning documents" below) as the **primary
  launch channel/wedge**, ahead of the direct-to-consumer store.
- **Sister brand — OUT OF SCOPE:** FiCorp also runs **Bagrat's Bags**, a
  budget-tier leather brand. **MONTEC does not touch this** — MONTEC is
  premium-only positioning; never blend copy, pricing logic, or product
  concepts between the two brands. If budget-tier questions come up,
  flag that they belong to Bagrat's Bags, not MONTEC. (Physical workshop
  infrastructure is shared between the two brands per the Business Plan —
  that's an operational fact, not a licence to blend brand/product
  decisions.)

## Name & positioning

**MONTEC** = **Mont** (mountain — heritage, permanence, old-world weight;
open to tie into Armenian identity/Ararat later) + **Tec** (technology/
innovation — functional, modular design). Per the user's own framing:
*"old money quiet luxury accessories made in [the new] century for [the
new] century business and finance people."* The brand promise is that
duality held at once — timeless materials and silhouette, engineered with
genuinely modern function (see THE UNIT's dock system and THE ARENA desk
mat below, which have no equivalent in the reference brand).

**Tone:** quiet, understated, confident — never flashy or logo-forward.
Same register as the reference brand's own language: "quiet confidence,"
letting materials and craftsmanship speak. Persona is specifically
business/finance dealmakers, not executives-in-general — every product
name reinforces that narrative (see Batch 001 below).

## Reference brand — Von Baer (vonbaer.com)

Explicit primary reference for product line, materials, and business model,
per the user 2026-08-02. **There will be deliberate differences — see
"How MONTEC differs" below; do not copy Von Baer wholesale.**

**Superseded 2026-08-02 by a deep competitive-research document**, saved
2026-08-03 to `montec/docs/reference/von-baer-deep-research.pdf` (8
pages, downloaded from Drive and verified as a valid PDF matching the
Drive file's exact byte size) — far more detailed and sourced (Estonian
business registry, Inforegister, Tracxn, Trustpilot, Sitejabber) than the
original web-search reconstruction. Key findings:

- **Legal entity:** Von Baer OÜ, Estonia, reg. code 12944953, registered
  11.11.2015. Address: Tala tn 2, Lasnamäe, Tallinn 11415. Share capital
  €8,000. VAT EE101897727. EMTAK activity code is literally "retail sale
  of footwear" (47721) — never re-filed in 10 years.
- **Owners:** Albert Varkki (50%, board since founding) and Igor Monte
  (50%, board only since 21.07.2023). **Igor Monte was previously named
  Igor Syunin** — the surname italianization coincided with the brand's
  pivot to an "Italian heritage" positioning. Neither founder is a
  leatherworker; both are Tallinn-based entrepreneurs (b. 1990–91) who
  started the business at 24–25.
- **Scale:** only 5 employees. 2026 revenue forecast €1.86M (up from
  ~€272k/quarter in mid-2025 — real ~45% CAGR). Estimated business
  valuation ~€3.5–4M. Heavily seasonal (Q4/Q1 peaks, Q2/Q3 troughs) —
  hit a "problem" credit-class flag in July 2026 over a tax debt, cleared
  within 48 hours.
- **Brand story is a constructed, layered legend:** Layer 1 (2015–2021,
  original) — "two childhood friends fighting the epidemic of boring
  bags." Layer 2 (2022–24) — added the "Cuoio Superiore" Italian
  vegetable-tanning certification as external validation. Layer 3
  (2025–26, current) — rewrote "Our Story" to imply "founded 1961,"
  which actually refers to the Tuscan tannery's tanning method, not the
  brand. The page's stale meta-description still contains Layer 1 text
  — a visible seam from the rewrite.
- **Name origin:** "Von Baer" borrows the identity of Karl Ernst von Baer
  (1792–1876), a real Baltic-German naturalist with zero connection to
  leather goods — pure constructed legitimacy (aristocratic-sounding +
  Estonian + no living rights-holder to object).
- **Price history:** flagship item was ~€299 a few years ago; today
  $1,495–1,995 — roughly a **5x price jump** over ~8 years, achieved via
  (1) external certification, (2) invented heritage, (3) no-discount
  policy, (4) professional-persona segmentation, (5) media-logo social
  proof — not via a materially different product.
- **Product range:** wallets/cardholders (8+ styles, e.g. No.1, No.2,
  10X, W2, Essential, Grand, City, Harrington, Elegance, Voyager),
  briefcases, laptop/messenger bags, garment bags, wheeled carry-ons,
  backpacks, desk/desktop accessories, dopp kits, passport wallets,
  luggage tags, glasses cases, women's line. **Naming system is numbers +
  plain English nouns (No.1, 10X, Essential, Grand)** — no archetypal
  "THE + role" names like MONTEC's.
- **Their best growth lever — profession-based segmentation:** collections
  aren't "briefcases," they're "briefcases for investment bankers," "for
  litigators," "for auditors," "for PE professionals," "interview bags for
  finance." This is their single most valuable, directly copyable
  playbook move for MONTEC's own SEO/positioning.
- **SEO machine is the real asset:** ~600+ collection URLs from
  multiplying category × material × profession × gift-recipient × budget
  facets; a defensive "no discounts, ever" page to intercept coupon-site
  traffic; third-person FAQ blocks written for AI/voice search.
- **"As Featured In" (Forbes/Vogue/GQ/WaPo) is mostly hollow** — the
  linked articles are unrelated (Anna Wintour profile, HuffPost ring
  piece, etc.), i.e. HARO-style expert-quote insertions and PR-newswire
  syndication, not real coverage about the brand. Cheap and legal, but
  falls apart on click — a real risk for a C-suite buyer who checks.
- **B2B channel is real and named:** embossing shown for PwC, Heidelberg
  Materials, Tervisekassa (Estonian health fund); small Estonian
  government contracts (Ministry of Culture, Kaitseliit) function as
  reference/legitimacy, not revenue (<1% of turnover).
- **Personalization:** free hand-pressed blind embossing (bags/briefcases
  emboss on a leather luggage tag, not the item itself — reduces
  spoilage risk; wallets/cardholders emboss directly), up to 4
  uppercase initials, gift box included.
- **Warranty:** 5 years total (2yr EU statutory + 3yr manufacturer),
  functional hardware (zippers, locks, handles) covered for defects.
- **Reputation is genuinely split:** Trustpilot ~4.9/5 (~192–196 reviews;
  recurring praise: leather smell on unboxing, fast shipping, Igor's
  personal replies) vs. Sitejabber 2.7/5 (10 reviews; a complaint that
  negative reviews get flagged as "defamatory"). Site claims "1000+
  reviews, 4.9/5" — that figure is their own in-house review app, not an
  independent platform; a careful reader would notice the gap.
- **Named vulnerabilities worth exploiting for MONTEC:** the "since 1961"
  legend collapses on a 30-second check (MONTEC can lean into being
  genuinely new instead); the media-logo section falls apart on click;
  the mega-menu is unusable for humans (crawler-only IA — MONTEC can win
  on navigational simplicity); returns/negative-review handling is a
  real weak point (a demonstrably easy MONTEC return policy is a real
  edge); no true top-of-market tier exists above ~$1,995 (MONTEC's
  numbered/limited batches can credibly sit above it); no real scarcity
  model (anyone can buy — MONTEC's application-based model is a direct
  structural counter-move).
- **What NOT to copy:** the borrowed heritage story (MONTEC has a real
  one — Yerevan, the diaspora, a concrete first batch — stronger than an
  invented Tuscan one); the bloated crawler-oriented mega-menu; media
  logos without real linked coverage (MONTEC's buyer is C-suite — they
  click).

### How MONTEC differs (confirmed so far)

- **Naming system:** MONTEC uses a unified power/authority/finance lexicon
  across every SKU (Founder, Executive, Closer, Arena, Capital, Treasury,
  Access, Backbone, Standard...) — Von Baer's naming is plain/classic
  (Classic, No.1, 10X, W2). This is a deliberate, load-bearing brand
  differentiator — keep it consistent in all future SKUs.
- **Design/production split:** designed in Armenia (vs. Von Baer's Tallinn)
  using Italian leather (same leather origin as Von Baer) — confirmed by
  the user 2026-08-02. Manufacturing location (Armenia vs. Italy vs.
  elsewhere) is still open — see TODOs.
- **Functional innovation SKUs:** THE UNIT (modular laptop case that docks
  into THE EXECUTIVE briefcase) and THE ARENA (leather desk mat) have no
  direct Von Baer equivalent — these carry the "Tec" half of the name and
  should be treated as hero/differentiator products, not filler SKUs. The
  docking mechanism has a confirmed proprietary name: **MONTEC RAIL™** —
  "integrated framework for modular expansion," per THE EXECUTIVE's spec
  sheet. Use this name consistently wherever the dock system is described.
- **"Batch 001" / limited-access launch model:** confirmed by the user's
  own product-page template (2026-08-02, see Reference materials) — the
  product detail page CTA is **"REQUEST ACCESS"**, not an add-to-cart
  button, and pages are numbered "01/13," "02/13," etc. Working assumption
  is a limited-drop/waitlist launch (closer to a numbered-edition release
  than Von Baer's always-open catalog) — treat this as the working model
  for site copy/UX, but do a final explicit confirm with the user before
  building checkout/waitlist logic.

## Visual identity — CONFIRMED 2026-08-02

Source: user-supplied product-concept documents (see Reference materials
below). This supersedes the earlier "no visual identity provided yet"
assumption — do not re-ask for logo/colors/typography, they exist.

- **Logo:** a mountain-peak monogram — two overlapping triangular peaks
  forming a stylized "M"/mountain silhouette — used as a standalone icon
  and paired with the "MONTEC" wordmark. Directly visualizes the "Mont"
  half of the name.
- **Branding/emboss rule (locked, do not deviate):** the MONTEC mark is
  applied as **blind emboss** — relief pressed into the leather, tone-on-
  tone, no ink, no foil color contrast. Per the source doc verbatim: "видно
  тольĸо за счёт светотени, ниĸогда за счёт цветового ĸонтраста" (visible
  only through light/shadow, never through color contrast). Gold-foil
  emboss appears only in hero/cover imagery (e.g. the Batch 001 collection
  cover), not as the default product branding.
- **Colors — exact hex confirmed 2026-08-02** (from the Brand Book,
  `montec/docs/reference/montec-brand-book.html`): **Obsidian `#0A0A0A`**
  (ground — backgrounds, wordmark), **Brass `#B8975A`** (the one accent —
  hardware, rules, emphasis; brass-soft `#C9AE7C` variant), **Anthracite
  `#2B2B2B`** (mid-tone panels/dividers), **Warm Paper `#FAF8F3`** (light
  ground for print/documents). Ratio guide: Obsidian 70% · Anthracite/
  Paper 24% · Brass 6% — "brass is a seasoning, not a sauce." This
  replaces the earlier approximate `#F5F5F3` off-white note — compatible,
  just more precise now. Cognac/chestnut-brown remains the physical
  leather color (a product-material fact, not part of this graphic
  palette).
- **Typography — confirmed exact:** **Cormorant Garamond** (serif —
  headlines, the wordmark, product names, pull-quotes) + **Inter** (sans
  — body copy, captions, interface, specs). Never set body copy in the
  serif; never set the wordmark or a product name in the sans.
- **Logo — CORRECTION 2026-08-02:** the Brand Book's own logo section
  text describes the monogram as "an M in a thin ruled square" — **this
  is wrong/stale text and must be ignored.** The real, confirmed mark
  (per actual logo asset files, see `montec/assets/brand/logo/`) is the
  **mountain-peak monogram** described above — two overlapping triangular
  peaks forming a stylized M/mountain. Do not redraw the logo to match
  the Brand Book's text; fix the Brand Book's text to match the real
  logo when it's next edited.
- **Photography/video direction:** two registers — (1) editorial lifestyle
  (tailored suits, city streets, luxury car interiors — Porsche/Mercedes
  cameos seen in source photos) and product macro detail shots on black
  backgrounds with a small ✦ sparkle/glint accent; (2) cinematic hero
  video — cold blue-grey grade with warm amber accent isolated on leather/
  brass only, 35mm anamorphic look, "Christopher Nolan aesthetic," 9:16
  vertical, no on-screen text overlay except title cards. Two full video
  treatments already exist as creative direction (THE CLOSER transformation
  concept, THE ARENA 17-second product video) — see Reference materials.
- **Brand taglines — RESOLVED 2026-08-02.** Two lines chosen by the user
  as primary (used in different contexts, not a single site-wide tagline):
  **"Craftsmanship and strategy for those who write history"** and
  **"I am not rich enough to buy cheap things."** Two other candidates
  surfaced in the new planning docs are secondary/supporting voice lines,
  not "the" tagline: "The House of Quiet Leather" (Brand Book cover/
  footer) and "...made at home, sold only to those who ask" (GTM
  positioning line).

## Product detail page template — CONFIRMED 2026-08-02

The user's source docs include an actual page-template mockup (using THE
FOUNDER as the worked example) — applies to all 13 SKUs. Structure:

1. Header: MONTEC logo (top-left) · "BACK TO COLLECTION" (top-right).
2. Breadcrumb: "0X / 13 — [CATEGORY]" (e.g. "01 / 13 — WEEKENDER").
3. Product name in large serif display type (e.g. "The Founder").
4. One-line italic positioning subtitle (e.g. "Scale and Strategy").
5. Body paragraph — brand-voice description (see per-product copy below).
6. Hero + detail photography (lifestyle shot, macro hardware/emboss
   details, in-use shots).
7. **"THE AUDIT"** — a fixed 5-field technical spec table used identically
   across every SKU: **EXTERNAL** (leather grade), **ARCHITECTURE**
   (construction/structure), **VOLUME** (capacity/use-case), **HARDWARE**
   (materials/finish), **MARKINGS** (branding/emboss treatment). Keep this
   exact 5-field taxonomy for every future product page — it's a
   recognizable, load-bearing brand device, not incidental copy.
8. Price in AMD + **"REQUEST ACCESS"** CTA (see limited-drop model note
   above).
9. Footer: "Continue the Set" / "VIEW FULL COLLECTION" cross-link to the
   next product · "MONTEC · © 2026 Montec. Batch 001."

## MONTEC Batch 001 — full launch product list (locked, 13 SKUs)

Do not add, rename, or drop SKUs without the user confirming first.

Prices below are AMD, confirmed 2026-08-02 from the user's own product-
concept documents (see Reference materials) for 8 of 13 SKUs. The
remaining 5 (marked TBD) have no pricing document yet — do not invent.

### Heavy weight — bags & business
| # | Name | Type | Price (AMD) | Line |
|---|---|---|---|---|
| 1 | **THE FOUNDER** | Weekender | 270,000 | Flagship. "Scale and Strategy." A vessel for those who write history, not just participate in it. |
| 2 | **THE EXECUTIVE** | Briefcase | 230,000 | "The Control Center." Innovative briefcase with the MONTEC RAIL™ docking system other pieces attach to. |
| 3 | **THE UNIT** | Laptop module | TBD | Removable laptop case that docks into THE EXECUTIVE via MONTEC RAIL™. |
| 4 | **THE CLOSER** | Messenger bag | 190,000 | "Negotiation Weapon." Fast, bold, decisive — for the final handshake. |

### Office & command center
| # | Name | Type | Price (AMD) | Line |
|---|---|---|---|---|
| 1 | **THE ARENA** | Desk mat | 40,000 | "The Battlefield." Defines the boundaries of your influence on the workspace. |
| 2 | **THE BRIEF** | Men's clutch | TBD | Operational brief for what matters most (phone, keys, cards) on the move. |

### Financial block — small leather goods
| # | Name | Type | Price (AMD) | Line |
|---|---|---|---|---|
| 1 | **THE CAPITAL** | Bifold wallet | 40,000 | "Daily Resources." A classic foundation for the daily flow of trade. |
| 2 | **THE TREASURY** | Long wallet | TBD | Respect for larger assets and order in money. |
| 3 | **THE ACCESS** | Cardholder | 30,000 | "The Universal Pass." Minimalist entry, zero friction. |

### Lifestyle & accessories
| # | Name | Type | Price (AMD) | Line |
|---|---|---|---|---|
| 1 | **THE VOYAGER** | Dopp kit | 40,000 | "Personal Comfort." Standards and rituals maintained at any coordinate. |
| 2 | **THE VISION** | Glasses case | 30,000 | "Focus Protection." Armor for the lenses through which you analyze opportunity. |

### Foundation — belts
| # | Name | Type | Price (AMD) | Line |
|---|---|---|---|---|
| 1 | **THE BACKBONE** | Brown belt | TBD | The spine. Character and reliability under load. |
| 2 | **THE STANDARD** | Black belt | TBD | The benchmark. Discipline and flawless protocol. |

Per-SKU "THE AUDIT" spec highlights (full 5-field text lives in the
product-page template, not repeated per line above): every item is 100%
full-grain vegetable-tanned Italian leather with Italian brass hardware;
THE EXECUTIVE uniquely has the MONTEC RAIL™ modular-dock architecture;
THE CAPITAL and THE ACCESS are explicitly hardware-free (no visible
metal) for a cleaner, more minimal build.

## Pricing — 8 of 13 SKUs confirmed, 5 still TBD

Confirmed AMD prices are in the product tables above (source: user's own
product-concept documents, 2026-08-02). Still missing: THE UNIT, THE
BRIEF, THE TREASURY, THE BACKBONE, THE STANDARD. Do not invent these five
— ask the user. Do not derive a "relationship to Von Baer's pricing"
narrative (match/undercut/premium) in copy — Von Baer is research
reference only, never mentioned on the live site.

## Languages / markets

Launch order confirmed 2026-08-02: **English first**, then **Armenian and
Russian**. No French — MONTEC's language set is 3 (EN/HY/RU), **not** the
4-language set (EN/HY/RU/FR) used by the unrelated Memory Care project in
this same repo. Don't copy that assumption over by habit.

## Audience

Both local Armenian premium (Yerevan) market and international/export
market equally — confirmed 2026-08-02. Universal positioning, same
principle as noted above.

## Reference materials (source files, kept in this repo)

Raw files the user has been supplying since 2026-08-02, saved as-is —
**most not yet reviewed/analyzed**, just filed. Treat anything marked
"not yet reviewed" as unverified until actually opened.

`montec/docs/reference/`:
- `product-page-template-concept.pdf` — the product detail page layout
  (worked example: THE FOUNDER), applies to all 13 SKUs. *(Reviewed.)*
- `batch-001-catalog.pdf` — full Batch 001 catalog: per-SKU photography,
  pricing, and "THE AUDIT" spec sheets for 8 of the 13 products.
  *(Reviewed.)*
- `the-closer-video-concept.pdf` — cinematic hero-video shot list/prompts
  for THE CLOSER (v2, single-actor transformation concept, Nolan-esque
  cold grade, 9:16). *(Reviewed.)*
- `the-arena-video-concept.pdf` — 17-second product video shot list for
  THE ARENA desk mat, plus caption copy variants. *(Reviewed.)*
- `the-founder-audio.mp3` — an audio asset for THE FOUNDER (likely a
  voiceover/ad-read). **Not yet reviewed** — no audio transcription tool
  available in this environment.
- `content-calendar-45-days-launch.xlsx` — 45-day launch content
  calendar. **Not yet reviewed** — binary spreadsheet, needs the xlsx
  skill/tool to open properly rather than a quick save-and-glance.
- `character-bible-v1.docx` / `character-bible-v2.docx` — two versions of
  a "Character Bible" (likely defines the recurring brand-film protagonist
  seen in THE CLOSER video concept — the transforming owner/dealmaker
  persona). **Not yet reviewed** — binary docx. Both versions kept; v2 is
  not assumed to fully supersede v1 until confirmed.

`montec/assets/products/<sku>/turnaround-grid.png` — 9-panel studio
turnaround renders (front/back/side/3-4/top/bottom/hardware/stitching/
logo-emboss), one per SKU, covering all 13 Batch 001 products (folders use
the SKU's kebab-case name, e.g. `the-founder`, `the-treasury`). SKU
assignment was inferred by visual match, not user-labeled, then confirmed
by the user 2026-08-02 — including `the-closer` (the slim single-strap-
loop bag), which is confirmed correct. `the-capital/` has two
near-identical renders (`turnaround-grid.png` + `turnaround-grid-alt.png`),
not yet deduped.

`montec/assets/brand/logo/` — logo asset pack, reviewed: black-on-white,
gold-on-white, gold-on-black variants of the mountain-peak monogram +
wordmark; a size spec sheet (S=15mm mark / M=45mm / L=70mm logo, "ORIGIN"
detail 3.5–4mm) with a new tagline candidate: **"I am not rich enough to
buy cheap things."** — not yet reconciled with the earlier tagline
candidate "Craftsmanship and strategy for those who write history."
(collection cover) — two tagline candidates now exist, ask the user which
is canonical (or if both are used in different contexts) before locking
site copy.

## Google Drive folder (catalogued AND sorted, 2026-08-02)

`montec/docs/reference/drive-folder-inventory.md` — a full name/type/size
catalog of the user's Google Drive folder
(`drive.google.com/drive/folders/1HrLH8PfL08PCGhL5fdOGhri3PljU3ocf`).
**405 files, ~3.08 GB** — iPhone camera-roll photos (HEIC/JPG/PNG/WEBP),
video footage (MOV/MP4, some 600–900 MB), several
`gemini_generated_video_*.mp4` AI-generated video outputs, and no
documents (PDF/DOCX/Sheets/Slides).

**Sorted into 18 subfolders inside that same Drive folder** (all 405
files reviewed by content where possible — images were actually viewed,
HEIC/WEBP converted first; video was classified by filename pattern only,
since video content can't be viewed). These are **copies** — originals
remain untouched in the folder root (no move/delete capability exists in
the Drive tools available here; the user accepted copies over moves).
Verified counts (queried directly from Drive, not agent self-reports):

| Folder | Count | Notes |
|---|---|---|
| the-founder | 35 | |
| the-executive | 38 | |
| the-arena | 30 | |
| the-access | 17 | |
| the-capital | 16 | |
| the-unit | 15 | |
| the-treasury | 11 | |
| the-backbone | 9 | |
| the-voyager | 8 | |
| the-brief | 6 | |
| the-vision | 6 | |
| the-standard | 6 | |
| the-closer | 2 | |
| **unsorted-misc** | **82** | other-brand keychains (Kentron, MTC, "Papa"), raw leather/material shots with no product shape, multi-product flat-lays, a few corrupted downloads |
| screenshots-and-references | 69 | competitor photos (Von Baer, Motherhouse, Time Resistance, etc.), UI/spec-sheet screenshots, moodboards |
| ai-generated-video-clips | 26 | hash-named / `gemini_generated_*` files |
| raw-video-footage | 17 | real `IMG_NNNN.MOV` phone footage |
| logo-assets | 12 | logo variant renders |

Total = 405, reconciled exactly against the original folder count.
`unsorted-misc` being the single largest bucket is expected — it's mostly
non-MONTEC material (other brands' keychains, raw material photography)
rather than a sign the sort failed.

## New planning documents (2026-08-02, Drive "Documents" folder)

A full launch-package document set appeared in a new `Documents` subfolder
inside the user's Drive folder: Business Plan, Go-to-Market Strategy,
Content Strategy, Brand Book (HTML), Financial Model (xlsx), and the Von
Baer deep research (folded into the Von Baer section above). These were
cross-checked against everything already in this file; the discrepancies
found were resolved with the user one at a time — resolutions are already
merged into the relevant sections above. Summary of what was resolved:

- **The financial model/business plan's own 6-product table (The Access,
  The Bifold, The Desk, The Portfolio, The Attaché, The Founder-special-
  edition, priced in USD) does NOT replace the 13-SKU Batch 001 lineup.**
  The 13 SKUs (Founder/Executive/Unit/Closer/Arena/Brief/Capital/Treasury/
  Access/Voyager/Vision/Backbone/Standard, priced in AMD) remain canon.
  The Financial Model needs to be rebuilt against the 13 SKUs in AMD —
  see Open TODOs.
- **FiCorp (owners Ararat, Taron) and craftsmen Artem/Levon are absent
  from these new docs** — they frame the launch as a solo-founder
  bootstrap. Confirmed with the user: this needs correcting — FiCorp and
  the craftsmen should be added into the Business Plan/GTM text (see Open
  TODOs), not left out.
- **Corporate anchor deal — Nairi Insurance:** the Von Baer research names
  Nairi Insurance as the buyer of the "500 personalized card-holder"
  corporate programme the GTM/Business Plan describe as "in motion."
  **Confirmed real, but currently PAUSED** — Nairi is going through
  internal restructuring and every project on their side is on hold.
  Any doc describing this deal needs its status corrected from "in
  motion"/"live example" to "paused, pending Nairi's internal
  reorganization" — this also affects the Financial Model's Month-2
  revenue timing assumption (650 corporate units delivered M2/M8),
  which assumed the deal executes on that schedule.
- **New channels confirmed (additive, no conflict):** YouTube
  `@TheMontec` (long-form craft/heritage films), LinkedIn (corporate-
  gifting narrative to decision-makers), Facebook + WhatsApp Business
  (community/diaspora, direct conversations).
- **The 45-day content calendar already saved** as
  `content-calendar-45-days-launch.xlsx` is explicitly referenced by the
  Content Strategy doc ("the proven structure is a 45-day content
  calendar") — confirms it's the same artifact, not a stray file.
- **Business model confirmations (no conflict, reinforces existing
  notes):** "by application," "numbered batches," "no discounts, ever"
  are stated explicitly as locked brand rules in the Brand Book's "Old-
  Money Code" — this resolves Open TODO #3 (limited-drop model) as
  confirmed, not just a working assumption.

Source files — status as of 2026-08-03: the rebuilt/corrected working
versions of all five planning docs live in `montec/docs/planning/`
(`Montec_Business_Plan.docx`, `Montec_Go_To_Market_Strategy.docx`,
`Montec_Content_Strategy.docx`, `Montec_Brand_Book.html`,
`Montec_Financial_Model.xlsx` — see each doc's note above for what
changed). The Von Baer research needed no content changes, so it's saved
as-is at `montec/docs/reference/von-baer-deep-research.pdf`. The original,
unedited Drive versions were not separately saved into the repo — the
rebuilt versions supersede them and are the working files going forward.

**Financial Model — REBUILT 2026-08-02** against the 13-SKU AMD lineup
(the original 6-product/USD table is superseded). Repo copy:
`montec/docs/planning/Montec_Financial_Model.xlsx` (live formulas, not
static values). Drive copy: uploaded as
`Montec_Financial_Model_REBUILT_13SKU_AMD` (auto-converted to a native
Google Sheet on upload; the original xlsx stays alongside it in
Documents, un-deleted — no delete capability here, user can remove it
manually). Verified computed results: Year-1 DTC-only revenue 10,086,000
AMD, gross margin 70%, operating profit 4,453,620 AMD (44.2% margin),
minimum monthly cash never goes negative (floor 1,332,385 AMD) even with
the Nairi Insurance corporate channel paused. If Nairi resumes: +8,750,000
AMD revenue / +6,125,000 AMD gross profit (memo only, not a forecast).

**Business Plan — REBUILT 2026-08-02**, now the primary working version
(supersedes `montec-business-plan.docx`'s 6-product/USD narrative). Repo
copy: `montec/docs/planning/Montec_Business_Plan.docx`. Drive: upload as
`Montec_Business_Plan_REBUILT_13SKU_AMD` pending — Drive's `create_file`
tool was returning internal errors on 2026-08-03 (confirmed unrelated to
content/size — even a 4-byte test payload failed); retry once the
connector recovers, the original stays alongside it un-deleted per the
no-delete-capability constraint. Changes from the original: added FiCorp
(owners Ararat, Taron), Artem/Levon (Kapan, paid per order not salaried),
Bagrat's Bags relationship clarified (shared workshop only); replaced the
6-product/USD table with the full 13-SKU/AMD Batch 001 table; enriched
the Von Baer section with the full deep-research findings (legal entity,
owners, revenue, price-jump history, segmentation lesson); corrected
Nairi Insurance to "paused, not cancelled" throughout (Section 6 and the
Ask); re-keyed the Financial Summary (Section 7) to the rebuilt AMD
model's actual computed figures (DTC-only Year-1 base case, corporate
resumption as upside memo, not baseline).

**Go-to-Market Strategy — REBUILT 2026-08-02**, now the primary working
version (supersedes `montec-go-to-market-strategy.docx`). Repo copy:
`montec/docs/planning/Montec_Go_To_Market_Strategy.docx`. Drive upload
pending (same `create_file` outage as the Business Plan above — retry
together once the connector recovers). Changes: added FiCorp/Artem/Levon
context (Section 1, Budget Posture); corrected product naming from the
old 6-product set ("The Access card holder," "The Attaché briefcase") to
the locked 13-SKU names (THE ACCESS, THE FOUNDER, THE EXECUTIVE); Nairi
Insurance reframed from "in motion" to PAUSED throughout Section 4.1 and
the Launch Sequence (Section 5) — Phase 1 now treats DTC revenue as the
committed base case and corporate revenue (Nairi resumption or an
alternative) as upside whenever it lands, not a scheduled milestone;
added YouTube (@TheMontec), LinkedIn, Facebook and WhatsApp Business
alongside Instagram/TikTok in the channel list (Section 4.3), matching
the channels confirmed in the Content Strategy doc.

**Content Strategy — REBUILT 2026-08-02**, now the primary working
version (supersedes `montec-content-strategy.docx`). Repo copy:
`montec/docs/planning/Montec_Content_Strategy.docx`. Drive upload pending
(same outage). This doc's platform list (Instagram/TikTok/YouTube/
LinkedIn/Facebook/WhatsApp Business) and 45-day calendar reference were
already correct in the original — no Nairi or team-structure issues here.
The one real fix: generic product placeholders ("the folio," "the card
holder," "the briefcase") replaced with the actual locked 13-SKU names
(THE EXECUTIVE, THE ACCESS, THE BRIEF, THE CLOSER) in the Life pillar
(Section 3) and the signature reel concepts (Section 4) — "The Closer"
reel concept now explicitly ties to the real THE CLOSER messenger bag
SKU rather than a generic transformation metaphor. Also added a brief
FiCorp/Artem/Levon mention (Section 1) for consistency with the other
rebuilt docs.

**Brand Book — REBUILT 2026-08-02**, now the primary working version
(supersedes `montec-brand-book.html`). Repo copy:
`montec/docs/planning/Montec_Brand_Book.html`. Drive upload pending (same
outage). Three fixes, matching the Open TODO item calling for exactly
these: (1) Section 03 (Logo & Wordmark) — the stale "an M in a thin ruled
square" description is gone, replaced with the real mountain-peak
monogram ("two overlapping triangular peaks forming a stylized mountain
silhouette"), per the 2026-08-02 correction locked earlier in this file;
the monogram swatch's placeholder glyph was also swapped from a plain "M"
to a triangle mark with an updated caption. (2) Section 07 (Product
Naming) — the old 6-product table is replaced with the full, locked
13-SKU/AMD Batch 001 table (all 13 rows, price column added, TBD rows
flagged with a footnote), and the intro paragraph's example line now
points to THE FOUNDER as the hero piece it climbs toward. (3) Section 01
(Essence) — both chosen taglines are folded in with short attribution
lines: "I am not rich enough to buy cheap things" (the line for the
object) and "Craftsmanship and strategy for those who write history"
(the line for the customer). The Old-Money Code (Section 02), colour
palette (Section 04), typography (Section 05) and voice rules (Section
06) were already correct and untouched.

**Brand Book — EXPANDED 2026-08-09 to Edition 002**, modeled on a
real 31-page reference brandbook (ARISTOCRAT Orchestra, reviewed via
user screenshots) the user asked to match in thoroughness. Grew from 9
sections to 12 (still `montec/docs/planning/Montec_Brand_Book.html`,
same file, same anchors for 01–09 — no links broken). Added:
- **Section 03 (Logo) gained 5 subsections**: Clearspace (diagrammed —
  unit is the cap-height of the M), Minimum & recommended sizes
  (formalizes the S=15mm/M=45mm/L=70mm/ORIGIN=3.5–4mm figures that
  previously only existed as a standalone PNG asset —
  `montec/assets/brand/logo/logo-spec-sheet-sizes-tagline-hires.png` —
  not yet in the book itself), Positioning (primary top-left / secondary
  bottom-center, matching the already-locked product-page-template
  header and packaging-card conventions), Additional versions
  (monochrome-only rule; a NEW circular social-avatar lockup — did not
  exist as an asset before), and Don'ts (6 rules; "don't fill with
  colour" is the one that encodes the blind-emboss law as a visual
  rule, not just prose).
- **Section 04 (Colour) gained a secondary/tint palette**: 20% tints of
  Brass and Obsidian (computed programmatically:
  `#EDE5D4`/`#CAC8C4`), plus the Brass-soft `#C9AE7C` and Anthracite
  Deep `#3A3A3A` values that were already defined in the file's own CSS
  variables but never surfaced as documented, usable swatches.
- **Section 05 (Type) gained a type-hierarchy table** (Display/H1/Lead/
  Eyebrow/Body/Caption with exact px sizes — reverse-engineered from the
  book's own existing CSS, not invented) **and an Armenian/Cyrillic
  companion-typeface spec**: Noto Serif Armenian (pairs with Cormorant
  Garamond) + Noto Sans Armenian (pairs with Inter), both free/open-
  source (SIL OFL) and genuinely built for Armenian Unicode coverage —
  picked because Cormorant Garamond and Inter are Latin-only and MONTEC
  has confirmed HY as a launch-2 language. Flagged honestly rather than
  asserted: Inter's own character set is understood to include Cyrillic
  but this needs verifying on the exact font build before production;
  if Cormorant Garamond's build lacks Cyrillic, Noto Serif (Cyrillic)
  is the specified fallback for Russian display type. This is a
  recommendation to sign off, not yet used in production.
- **Section 10 (NEW) — Brand Pattern**: a fine brass-hairline grid on
  obsidian (CSS-drawn, no image asset), with when-to-use/avoid rules.
- **Section 11 (NEW) — Stationary**: business card, letterhead, a NEW
  "batch/authenticity card" concept (ties the numbered-batch mechanic
  to a physical keepable object inside the box — Montec had no
  equivalent to a certificate of authenticity before this), a pitch-deck
  title-slide cover (for the Business Plan/GTM/corporate-gifting
  pitches), and a social avatar + post-template spec. All five have
  working CSS flat-mockups rendered directly in the page (verified via
  a Playwright screenshot pass — business card, letterhead, batch card
  and slide all render correctly).
- **Section 12 (NEW) — Mockup Prompts**: five ready-to-run image-
  generation prompts (business card flat-lay, letterhead flat-lay,
  batch card inside the box, pitch-deck on a laptop screen, avatar in
  an Instagram-style phone screen) — written because **this session has
  no image-generation tool**, so the photoreal versions of Section 11
  can't be rendered directly; the user will run these through an
  external generator (Nano Banana / Midjourney) and the results can be
  dropped back in. Same pattern used earlier for the Kentron keychain
  request in this conversation.
Scope for this expansion was explicitly narrowed by the user before
starting: HTML first (PDF version later, not yet built), the full
stationary set (all 4 categories offered), typeface choice delegated to
me to research and propose, and photoreal mockups via prompts (not
direct generation, since no image tool exists here).

**PDF edition built 2026-08-09** — `montec/docs/planning/Montec_Brand_Guide.pdf`
(37 pages, landscape A4/297×210mm), plus its source
`montec/docs/planning/Montec_Brand_Guide_Print.html`. This is a
**separate page-spread layout**, not an export of the scrolling web
Brand Book — same content/copy, restructured into Aristocrat-style
full-bleed divider pages (giant section title + numbered sub-index) and
one-to-two-topic content pages, generated programmatically (Python
builds the paginated HTML, headless Chromium via Playwright renders it
to PDF — `page.pdf()` with the page size matching the CSS `.page` divs
exactly, no manual page-break tuning needed). Verified page-by-page with
`pdftoppm` renders read back through the Read tool, not just "it ran
without erroring" — caught and fixed two real layout bugs this way: (1)
the 3-box logo-variant grid overflowed off the page edge on two pages
(nested CSS grid needed explicit `min-width:0` on grid children — a
known CSS grid gotcha, not a MONTEC-specific issue); (2) every divider
page with a two-line giant title visually collided with its sub-section
index list at the bottom (fixed by moving the giant title up and
tightening the index list's line-height). Both confirmed fixed by
re-rendering before treating the file as done. Same 12-section content
as the HTML edition; keep both in sync if either is edited going
forward — the print version does NOT auto-update from the web one.

## Design system — `montec/design-system/` (built 2026-08-09)

A real, buildable React + TypeScript + Tailwind component package that
turns the Brand Book/Guide from documentation into code — same tokens,
same rules, same components. Built on explicit user decisions (asked
via AskUserQuestion before starting, all defaults accepted): stack
React+TS+Tailwind, Storybook configured from the start, **MVP scope
only** (tokens + typography + buttons + logo — NOT yet the product
card/THE AUDIT/SKU table/stationary suite from the Brand Guide),
located at `montec/design-system/` as its own `package.json` alongside
`montec/docs/` and `montec/assets/`.

**What's in it:** `src/tokens/colors.ts` + `typography.ts` (the exact
primary+secondary palette and 6-level type scale from Brand Guide
Sections 04–05, as importable JS objects, not just Tailwind config);
`<Logo>` (5 variants: primary/reversed/monochrome-dark/monochrome-
light/avatar) built around a hand-traced `<Monogram>` SVG (two
overlapping chevron/"Λ" strokes, stroke-based not filled-triangle,
traced by pixel-analyzing `montec/assets/brand/logo/logo-gold-on-
black.png` — coordinates in `Monogram.tsx`'s two `<path>` elements);
`<Typography>` (one component, `variant` prop for the 6 levels, `lang`
prop swaps in the Noto Serif/Sans Armenian companion faces chosen in
the Brand Guide); `<Button>` (primary/secondary/ghost — deliberately
has no sale/urgent/destructive variant, enforcing the Old-Money Code's
"no discounts, ever" rule at the component level, not just in prose).

**Verified, not just built:** `npm run build` (tsup → dist/ESM+CJS+d.ts,
then Tailwind CLI → dist/styles.css) and `tsc --noEmit` both ran clean.
Storybook (`storybook build`) compiled all 4 story files. Static
Storybook export had a CSS-preload error under both a plain `http-server`
and Python's `http.server` (an environment/headless-Chromium quirk, not
a code bug) — switched to `storybook dev` and screenshotted through
that instead; all components then visually verified via Playwright
screenshots read back through the Read tool: the traced monogram
matches the reference PNG closely across all 5 logo variants, the type
hierarchy renders with correct serif/sans pairing, all 3 button
variants render correctly, and all 10 colour tokens render with exact
hex values.

**Not yet done:** the product card / THE AUDIT spec table / SKU-pricing
table / stationary suite (business card, letterhead, batch card,
pitch-deck cover, social post template) components — explicitly scoped
out of this first pass. Actually syncing this package to Claude Design
(`claude.ai/design`) via the `/design-sync` skill is a distinct later
step, not done here — this pass only builds and verifies the source
package `/design-sync` would consume. `package-lock.json` is committed
for reproducibility; `node_modules/`, `dist/`, `storybook-static/` are
gitignored.

## Website — `montec/site/` (built 2026-08-11)

The Batch 001 site. Next.js 14 App Router with `output: 'export'` — the
build produces 25 static pages (home, collection, all 13 product pages,
The Code, Corporate gifting, The House, Request access + its confirmation,
sitemap, robots) into `out/`, no server. Scope was set by the user:
"полноценный солидный и современный сайт со всеми разделами," static
export, form → email via a service (no backend).

**Structure.** `lib/products.ts` is the single source of truth for the 13
SKUs — names, objects, groups, prices and the full THE AUDIT copy — and
every page reads from it, so the CLAUDE.md product tables have exactly one
code-side mirror. Product routes are generated from it via
`generateStaticParams`. Design tokens are imported from
`@montec/design-system` into `tailwind.config.ts` rather than restated, so
the site and the component package cannot drift apart.

**Design decisions (deliberate, don't undo without asking):**
- *Signature element* — the hero renders the blind-emboss law rather than
  describing it: the real macro photograph of the embossed mark sits
  nearly unlit and a soft light follows the pointer, so the mark is found
  through light and shadow, never colour contrast. Degrades on purpose —
  no fine pointer or reduced-motion means the light rests off-centre and
  the "move across the leather" hint is hidden.
- *The collection is a manifest, not a photo grid* — number, name, object,
  price, all 13 visible at once, with a pinned image reveal on hover. The
  01–13 numbering is legitimate because Batch 001 is a real finite
  sequence.
- *Specimen plates* — product shots are mounted on warm paper over the
  obsidian ground, because the source photography is studio-white.

**Brand rules held in code, not just prose:** the 5 unpriced SKUs carry
`price: null` and render "Price on request"; THE AUDIT's five fields are
identical and in order on all 13 pages; no testimonials, review counts or
stock claims anywhere, and the product JSON-LD omits `offers` entirely
when there is no price. There is no cart and no discount UI at all.

**Assets.** `public/products/<slug>/{front,three-quarter,hardware,emboss,
turnaround}.webp` were sliced from the canonical
`montec/assets/products/<sku>/turnaround-grid.png` files (the эталон
stays the source of truth; these are derived crops). Stored as WebP —
20 MB of PNG became 2.1 MB. Fonts (Cormorant Garamond, Inter, Noto
Serif/Sans Armenian) are self-hosted in `app/fonts.css`; zero external
requests.

**Forms.** Native form POSTs, working with JavaScript disabled, with a
honeypot. Delivered by Netlify Forms (`netlify.toml` is configured: base
`montec/site`, publish `out`) or any endpoint set in
`NEXT_PUBLIC_FORM_ENDPOINT`. The product page's REQUEST ACCESS link
carries `?piece=<slug>`, read on mount to preselect the piece.

**Verified by rendering, not assumption:** all internal links crawled (19
pages, none broken), desktop and 390 px mobile screenshots read back.
Three real defects were caught that way and fixed — the collection's
floated reveal panel squeezed the first rows narrower than the rest (now
a real grid column); the ֏ sign rendered malformed because neither
Cormorant Garamond nor Inter carries a glyph for U+058F (now set in Noto
Sans Armenian via a `<Price>` component — **keep using it, don't hand-set
֏ in the serif**); and mobile had no route to the four sections at all
(now a menu overlay).

**Known, accepted:** hovering a product link logs an "RSC payload" fetch
error in the console — standard `output: 'export'` behaviour on a plain
static host, with a clean fallback to normal navigation. Not yet built:
Armenian and Russian copy (fonts and the `font-serif-hy`/`font-sans-hy`
families are already wired for it), real lifestyle photography, and
per-SKU imagery for the pieces that only have turnaround renders.

**Drive upload status (2026-08-03):** the Drive `create_file` tool is
returning "Internal error encountered" on every attempt regardless of
content or size (confirmed with a 4-byte test payload) — a live outage,
not a data problem. Repo copies of all four rebuilt planning docs
(Business Plan, Go-to-Market Strategy, Content Strategy, Brand Book) are
committed and pushed; their Drive uploads (as `*_REBUILT_13SKU_AMD` /
`*_REBUILT` files in the Documents folder, alongside the un-touched
originals) are queued and will be retried once the tool recovers.

**Design Brief — Answers (NEW 2026-08-09)**, written in the voice of the
business owner for handoff to a web/brand designer — modeled on the
analogous MemoryCare design-brief-answers document at the user's request.
Repo copy: `montec/docs/planning/Montec_Design_Brief_Answers.docx`
(Russian, 7 sections / 33 questions, same structure as the MemoryCare
reference doc). Key framing decision: unlike MemoryCare's brief (which
still has an open/negotiable logo and only a temporary landing page),
MONTEC's brief states plainly that the brand identity is **already fully
locked** (exact hex colors, exact typography, the mountain-peak
monogram, both taglines, the blind-emboss rule, "THE AUDIT" taxonomy,
"REQUEST ACCESS" CTA) and that **no live website exists yet** — this is a
first build, not a redesign. Two fields left as explicit placeholders
for the user to fill in (not invented): a named contact person/phone,
and the project deadline. KPI targets (Q32) are also left open/TBD since
no numeric targets exist yet in this file, unlike MemoryCare's brief
which has real committed KPI numbers — flagged rather than fabricated.

## Known external channels

- **Instagram: `instagram.com/montecleather`** — confirmed real handle,
  shared by the user 2026-08-02. Content could not be reviewed — Instagram
  is blocked by this session's network egress policy (403, same class of
  block as vonbaer.com). If the account's existing posts/bio need to
  inform brand copy or the content calendar, the user will need to
  describe/screenshot them rather than relying on a live fetch here.
- **YouTube: `@TheMontec`** — long-form craft/heritage films (confirmed
  2026-08-02, Content Strategy doc).
- **LinkedIn, Facebook, WhatsApp Business** — LinkedIn carries the
  corporate-gifting narrative to decision-makers; Facebook/WhatsApp
  Business serve community/diaspora direct conversations (confirmed
  2026-08-02, Content Strategy doc).

## Things NOT to invent

- Don't invent the manufacturing location (Armenia vs. Italy) — open TODO.
- Don't invent the exact tannery name — open TODO (leather grade itself —
  full-grain, vegetable-tanned, Italian — is confirmed, just not the
  specific tannery/mill).
- Don't invent prices for THE UNIT, THE BRIEF, THE TREASURY, THE BACKBONE,
  or THE STANDARD — still TBD, ask the user.
- Don't invent customer reviews, testimonials, or "sold in N countries"
  claims — MONTEC is pre-launch.
- Don't deviate from the blind-emboss-only branding rule (no color-
  contrast logo treatment on product leather) without the user signing
  off — it's a stated brand law, not a stylistic default.
- Don't drop or rename the "THE AUDIT" 5-field spec taxonomy (EXTERNAL /
  ARCHITECTURE / VOLUME / HARDWARE / MARKINGS) when writing new product
  pages — keep it identical across all 13 SKUs.

## Open TODOs (do not consider MONTEC launch-ready until closed)

1. Pricing for the 5 remaining SKUs (THE UNIT, THE BRIEF, THE TREASURY,
   THE BACKBONE, THE STANDARD) — also needed as AMD inputs for the
   Financial Model rebuild (item 8 below).
2. Manufacturing location (Armenia vs. Italy vs. elsewhere) and the exact
   tannery/mill name.
3. ~~Final confirm on the limited-drop/"REQUEST ACCESS" launch model~~ —
   **CONFIRMED 2026-08-02** via the Brand Book's "Old-Money Code" (by
   application, numbered batches, no discounts ever, stated as locked
   brand rules, not a working assumption).
4. Armenian and Russian translations for all product copy (not started).
5. Warranty, shipping, returns, and personalization policy — Von Baer's
   terms (5yr warranty, free embossing, free shipping) are a reference
   point only, not yet decided for MONTEC.
6. Review `the-founder-audio.mp3` content once a transcription path exists
   (or the user provides a transcript) and fold anything relevant into
   this doc.
7. Photography/video assets for THE UNIT, THE BRIEF, THE TREASURY, THE
   BACKBONE, THE STANDARD — not present in the supplied catalog PDF.
8. ~~Rebuild the Financial Model~~ — **DONE 2026-08-02**, see the
   Financial Model note above. Repo copy rebuilt against the 13-SKU AMD
   lineup with the 5 TBD SKUs left as blue input cells; Drive re-upload
   still pending the `create_file` outage (see Drive upload status note).
9. ~~Add FiCorp (Ararat, Taron) and craftsmen Artem/Levon into the
   Business Plan and GTM Strategy~~ — **DONE 2026-08-02**, both docs
   rebuilt and repo copies committed; Drive re-upload pending the outage.
10. ~~Correct the Nairi Insurance corporate-deal status~~ — **DONE
    2026-08-02** across the Business Plan, GTM Strategy and Financial
    Model (all now say "real, currently paused"); Drive re-upload of the
    docx copies pending the outage (the Financial Model's Drive copy is
    already uploaded and correct).
11. ~~Fix the Brand Book's logo section text and 6-product naming
    table, fold in both taglines~~ — **DONE 2026-08-02**, see the Brand
    Book note above. Repo copy committed; Drive re-upload pending the
    outage.
12. **Retry the four pending Drive uploads** (Business Plan, GTM
    Strategy, Content Strategy, Brand Book) once `create_file` recovers
    from the 2026-08-03 outage — repo copies are all done and are the
    current source of truth in the meantime.
