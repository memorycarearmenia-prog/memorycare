# PROPOSAL — Product / UX architecture

Rebrand 2026-09-01. Slot: product & UX. Owns structure, flow, conversion.

Governing sources, in precedence order: `docs/rebrand-2026-09-01/BRIEF.md` →
`docs/design-package-v1/LEAD-REVIEW.md` (where not superseded by the 31.08 facts) →
`docs/design-package-v1/FINAL-UX.md` (prior art) → the 31.08 audit
(`FINDINGS.md`, `INVENTORY.md`, `GAPS.md`).

---

## REVISION NOTE — 01.09, after the coordinator's pricing correction

The first draft of this file was written against the pricing table in the first version of
`BRIEF.md`, which had been copied from `CLAUDE.md` and was stale. The governing document is the
owner's decision of **26.08.2026** (`docs/TARIFF-REDESIGN-2026-08-26.md`), whose §8 names
`CLAUDE.md`'s table as outdated. What I changed, all of it in §0.2, §3 and §10:

1. **Five products, not four.** `Հատուկ խնամք / Special` is added, priced by calculator or
   consultation, always beginning with a Զննում. It is the fifth card. §3.6.
2. **Every price moved** except Զննում: Express **65,000**, Optimal **160,000**,
   Maximum **200,000**.
3. **The light/heavy split is rejected — all visits are full visits.** Optimal is **4 full
   visits, one in each season**; Maximum is **6 full visits**. My first draft's filled-vs-ring
   year rail encoded a distinction that does not exist; the rail is now one mark type, which makes
   it strictly better — Optimal's four marks land one per season group, so the sentence the product
   sells on is literally visible. §3.2.
4. **Credit rules rewritten.** One 60-day window, credit only at the signing of an annual
   subscription, never into an Express, either-Զննում-or-Express and never both. §3.4.
5. **The 40,000 repeat Express is deleted and designed out**, not merely omitted. §3.5.
6. **A calculator is specified**, because it is an owner decision of 26.08, not an option. §3.7.
   My first draft deleted it on the reasoning that a flat price leaves nothing to compute; that was
   wrong — the price is flat *within* 16 m² and 2 monuments, and the calculator is what prices
   everything beyond that envelope. The deletion is reversed in full, including the surcharges.
7. **The weather-window guarantee** is added to the product copy and to the trust architecture (§9),
   where it is unusually good material.
8. Four further 26.08 decisions that no earlier document carried into the site are folded in: the
   assigned crew, the two optional delivery preferences, the flowers/candle option on the tariffs
   page, and payment for the year in full only. §3.8.

Also: the 242 audit screenshots have since appeared at `docs/site-audit-2026-08-31/screens/` and I
have used them. `packages-add-1__en__1440__default-fold.png` shows the live order page selling
`PACKAGE 3 · 180000 ֏ · 6 visits · 2 full visits · 4 preventive visits` — the rejected price, the
rejected composition **and** the rejected light/heavy split on one screen, under `condition 5` to
`condition 10`. That single screenshot is the clearest statement of what this rebrand has to remove.

---

## 0. Preface — what I read, what I could not read, and what I ruled on

### 0.1 The screenshots

`screens/` was **absent when I began** — as was `docs/rebrand-2026-09-01/` itself; the brief was
filed only at `docs/site-audit-2026-08-31/docs/rebrand-2026-09-01/BRIEF.md`. Both appeared during
the writing of this proposal, and I have gone back to the 242 real screens. What follows is what
I read, in the order I read it — the contact sheets first, the individual screens after.

The contact sheets, and what they gave me:

- `sheets/fold-home.png` — home at 360/768/1024/1440/1920 × hy/ru/en. Confirms: an animated
  cloud background (Vanta) behind a floating translucent card, "WHAT IS LOREM IPSUM?" as the H1
  in all three locales, `ՀԱՅ РУС ENG` present in the *closed* 360 header, and a broken-image FAB
  bottom-right on every frame.
- `sheets/spot-1440.png` — `mission`, `values`, `news`, `notfound` are four identical bare 404
  panels; `account-index` is a left rail of profile fields beside a body of Lorem Ipsum;
  `packages-add-1` re-asks name / phone / email beside a single green package card reading
  `ՓԱԹԵԹ 1 · 180000 ֏`; `root` serves the Armenian home page.
- `sheets/states-forms.png` — contact is Name / E-mail / Phone / Message as underline-only
  inputs with no labels; register is Name / Phone / E-mail / Password with bare `(i)` glyphs and
  no consent control; focus produces no visible change.

From the individual screens, one more thing that changes a ruling:

- `packages-add-1__en__1440__default-fold.png` — the authenticated order page. A single green card
  reading `PACKAGE 3 · 180000 ֏`, then `Annual subscription · 6 visits · 2 full visits ·
  4 preventive visits`, then `condition 5` through `condition 10`, then `Order`. Beside it, a rail
  repeating the signed-in user's own name, phone and e-mail back at them. Every commercial fact on
  that screen is a rejected one, and the light/preventive split it prints is the exact distinction
  the owner struck out on 26.08.
- `account-index__en__1440__default-fold.png` — the same rail beside four paragraphs of Lorem
  Ipsum under the heading `MANAGEMENT SYSTEM`. There is no plot, no visit and no report anywhere
  in it, which is consistent with GAPS §3: the object model behind the portal does not exist.

That is enough to rule on every route in scope.

### 0.2 Conflicts I found between the sources, and how I ruled

The governing chain of fact is: **the owner's decision of 26.08.2026** (prices, composition,
credits, the calculator) → **the 31.08 brandbook** (colour, type, the mark) → the 31.08 audit →
the 29.08 design package. Five conflicts had to be resolved before any structure could be drawn.

| # | Conflict | Ruling |
|---|---|---|
| 1 | `CLAUDE.md` and the first version of the brief carry a four-product table at 180,000 / 240,000 with a light/heavy visit split and a 30-day credit. `TARIFF-REDESIGN-2026-08-26.md` §5 and §8 supersede all of it and name `CLAUDE.md`'s table as outdated. | **The 26.08 line-up governs.** Five products; 20,000 / 65,000 / 160,000 / 200,000 / calculator; all visits full; one 60-day window. Everything in §3 is built on it. |
| 2 | The live site sells `40,000 ֏` as a repeat Express, and the first brief listed it as current. 26.08 §1.2 and §4 record it as **considered and rejected by the owner**, for devaluing the subscription. | **Deleted, and designed out** so it cannot return — §3.5. FINDINGS #3 already calls the live 40,000 a blocker; it is selling a withdrawn price for a product that does not exist. |
| 3 | FINAL-UX §1: "Express is credited … **or** Inspection … the larger"; the first brief: Inspection 30 days, Express 60. 26.08 §14 corrects both: one window, one credit, and Զննում is **never** credited into an Express. | 26.08 §14 governs. §3.4. |
| 4 | FINAL-UX makes Special "never a card, never a price"; the corrected brief says "**Special is a fifth card on the site**". | Both are right about different failures. Special is a card — a **full-width card beneath the row**, holding the calculator. A priceless column standing inside a row of published prices is where a hesitant reader stops; a priceless card *below* the row, with a working calculator in it, is a fifth product. §3.6. |
| 5 | The 31.08 brandbook makes the wordmark single-colour **Olive**; Olive on Nude measures 3.12 and never carries text. FINAL-UX's header wordmark is two-tone. | Header live text is single-colour **Dark Olive** on light, **Nude** on dark. The drawn Olive wordmark is used only at display size on Dark Olive (4.14, clears AA-large). UI's territory — flagged, not decided here. |

One conflict I could not resolve and am escalating rather than guessing: **the flowers/candle
option** is an owner instruction of 26.08 (§7.5 — "a visible option on the tariffs page, not hidden
in the portal") but **no source anywhere gives it a price**. Specified as a slot in §3.8 and listed
in §12.

### 0.3 Where I override FINAL-UX, in one list

1. The pricing model — five products, the 26.08 prices, no light/heavy split, one credit window, and Special as a full-width card carrying the calculator (§3). FINAL-UX's 65,000-credit-into-160,000 arithmetic and its `95,000 first year` line survive the correction unchanged and are back in (§3.4).
2. **The report moves from home section 5 to home section 2.** §2.2.
3. **The consultation form itself lands on the home page** as the closing conversion block, replacing FINAL-UX's dark closing band and its link-to-a-form. §2.2, §4.
4. **`/guarantees/` is deleted as a route** and becomes a section plus a legal anchor. §1.2.
5. **Public self-registration is deleted.** §6.1.
6. The mobile language switcher pins to the **top** of the drawer, not the bottom. §1.4.
7. Exactly **two** dark areas on the home page (Family Circle, footer), not three.
8. Anthracite `#33373C` → Dark Olive `#212212` everywhere the old documents say "Anthracite".

Everything else in FINAL-UX §§3, 7, 9, 12, 13 that the 31.08 facts do not touch — the plot object
model, the role model, the report block order, the pro-rata refund arithmetic, the guest link, the
deceased's-name default — I adopt unchanged and do not restate.

---

## 1. Information architecture

### 1.1 The principle

The live build has **14 routes, none of which is a specified route** (GAPS §1). We are not patching
a sitemap; we are replacing one. The replacement is deliberately small: **eleven marketing routes,
four legal documents, four utility endpoints, and a portal.** Every route on this list either
converts, explains the product, or is a hard Ameriabank condition. Nothing exists because a
template had a slot for it.

### 1.2 Marketing sitemap — launch

Locale prefix on everything: `/hy/`, `/en/`, `/ru/`. **`hy`, never `am`** (FINDINGS #17 — `am` is
Amharic, and the template already emits `og:locale=hy_AM`, so the correct value is on hand).

```
/                          302 by Accept-Language among hy|en|ru, default /en/
/{loc}/                    Home
/{loc}/pricing/            The four products, the credit rules, the guarantees
/{loc}/how-it-works/       Consultation → subscription → visit → report; limits; weather
/{loc}/sample-report/      The live report component with labelled placeholder media
/{loc}/family-circle/      The differentiator, the roles, the privacy model
/{loc}/about/              Company, founders, method, legal entity      [bank requirement]
/{loc}/contacts/           Two named humans, hours with UTC offset, short form
/{loc}/consultation/       The primary conversion (page twin of the modal)
/{loc}/consultation/thank-you/     Conversion target — a real URL, not an in-place swap
/{loc}/pay/                Two payment paths presented as equals
/{loc}/pay/thank-you/      Payment initiated / awaiting transfer
/{loc}/legal/              Index of the four documents
/{loc}/legal/privacy/      [bank requirement — must exist in English]
/{loc}/legal/terms/        Service-delivery terms + the three guarantees in full [bank]
/{loc}/legal/refund/       Return policy + the pro-rata arithmetic          [bank]
/{loc}/legal/limitations/  Legal restrictions and what we do not do         [bank]
/{loc}/404/   /{loc}/500/   /sitemap.xml   /robots.txt
/r/:shareToken/            Public guest report — no login, no price, no upsell
```

Stable anchors, reserved for nav, footer and future advertising:
`#inspection` `#express` `#optimal` `#maximum` `#credit` `#guarantees` `#report` `#family`
`#faq` `#consultation`.

**Merged.** `/guarantees/` folds into `/pricing/#guarantees` (the block) and
`/legal/terms/#guarantees` (the full text with limits). A guarantee is read at the moment the
price is read; a page of its own is a page nobody arrives on. **`/contact/` → `/contacts/`**
(plural, as specified; a 301 from the singular).

**Deleted outright.** History, Mission, Values, News, the partners section, the reviews carousel,
the before/after slider, and public self-registration (§6.1).

### 1.3 The four 404 routes — a ruling on each

All four answer **HTTP 200 with a 404 panel** today (FINDINGS #4), so search engines are indexing
four dead pages under the client's brand.

| Route | Ruling | Status | Destination | Why |
|---|---|---|---|---|
| `/{loc}/page/history/` | **Delete + redirect** | 301 | `/{loc}/about/` | A 2026 company has no history. The material a visitor wanted is the founders block. |
| `/{loc}/page/mission/` | **Delete + redirect** | 301 | `/{loc}/about/#why` | Mission is one paragraph of About, not a page. A standalone mission page is a page of adjectives — the exact register the brand forbids. |
| `/{loc}/page/values/` | **Delete + redirect** | 301 | `/{loc}/how-it-works/#what-we-do-not-do` | Our values are demonstrated by naming our limits, not by asserting three nouns. This redirect is an argument as much as a route. |
| `/{loc}/publications/news/` | **Delete + redirect** | 301 | `/{loc}/about/` | Zero posts and no publishing cadence. An empty news page is worse than no news page. Revisit only when there are six posts in hand. |
| any unknown URL | **Real 404** | **404** | `/{loc}/404/` | Designed page: heading, one line, five real links, one phone number, the language switcher. |
| `/{loc}/page/home/`, `/{loc}/contact/`, `/{loc}/account/*` | **Redirect** | 301 | new equivalents | The whole URL shape changes; nothing is left orphaned. |
| `/am/*` | **Redirect** | 301 | `/hy/*` | FINDINGS #17. |

Also required and currently absent: a real `robots.txt` (staging **disallow all**, production
allow), a real `sitemap.xml`, `<link rel="canonical">` and reciprocal `hreflang` on all three
locales of every page (FINDINGS #8, #18, #40), and a `/500/` template.

### 1.4 Navigation

**Primary nav is five items and never more, at every viewport, flat, with no submenu anywhere:**

> Pricing · How it works · Sample report · Family Circle · About

Deleting History / Mission / Values / News removes the *only* reason the site has submenus, which
kills FINDINGS #4, #28 and the hover-only-with-no-keyboard-equivalent failure in a single move.
That is the argument for a flat nav: it is not a preference, it is the accessibility fix.

**Desktop, ≥900px.** Header 72px, Ivory, permanent 1px Dark-Olive-at-12% hairline at the bottom
(permanent, not on scroll — a 1.10 tonal step between Ivory and Nude without a rule reads as a
printing error). Left: mark + live text `MemoryCare`. Centre-left: the five items. Right, in this
order: language switcher · `Sign in` (text link) · `Request a consultation` (primary button).
No dropdowns, no mega-menu, no hover-revealed anything.

**Mobile, 360–899px.** Header 56px: `[menu 44×44] [lock-up, centred] [call 44×44 → tel:]`. No CTA
in the bar — it lives in the action bar (§8.4). Tapping menu opens a **full-screen drawer**, and
the drawer's contents, in order:

1. **The language switcher, first row, three 44px-tall targets** — `ՀԱՅ · ENG · РУС`, native
   script, current one marked with `aria-current="true"` and a Deep Olive rule, not colour alone.
2. The five nav items, 56px rows.
3. `Sign in`.
4. `Request a consultation`, full-width primary.
5. Both founders' phone numbers as `tel:` and `wa.me` targets.
6. A full-width `Close` row at the foot.

FINAL-UX put the switcher at the bottom of the drawer. **I move it to the top.** A diaspora
visitor who lands on the Armenian page from a US search needs the language control before
anything else on the screen has any meaning; making them scroll a drawer to find it is the same
failure as FINDINGS #27, one scroll further away. It is also the control the audit measured at
**33 × 22.5px** — the hardest target on the site to hit is the one most likely to be needed first.

The switcher also appears in the footer on every page and at every width. Two reliable locations,
neither of them hover-dependent. It does **not** appear in the closed 360 header: three 44px
targets plus a menu button plus a call button plus the lock-up does not fit 360px without
shrinking something below the floor, and the current site's answer to that was to shrink it.

**Footer, every page, every locale** (part bank requirement, part trust — §9):
column 1 Company (About · Contacts · Family Circle) · column 2 Services (the four products, each
anchoring into `/pricing/`) · column 3 Legal (the four documents) · column 4 the contact block:
both founders with `tel:` and `wa.me`, `info@memorycare.am`, the legal address, the company
registration number, and `MemoryCare LLC, Yerevan, Armenia · © 2026`. One column at 360, ordered
by importance, phone numbers first. Language switcher above the copyright line.

**Anything not yet real is visibly marked as a placeholder and never formatted to look real.**
`+374 10-00-00-00` reads as a phone number; `[legal address — to be confirmed]` reads as a gap
(FINDINGS #14). Real contacts exist now and go in: Davit Hambardzumyan +374 55 315 323, Hayk
Manukyan +374 93 154 108, info@memorycare.am.

---

## 2. The home page

### 2.1 The order, and the one argument that sets it

Eleven sections plus footer. The order is driven by a single question: **what does a person 9,000km
away need before they will believe a promise they cannot check?**

| # | Section | Ground | The job it does |
|---|---|---|---|
| 1 | Hero | Nude | State the offer and show that visits are verified — in one screen |
| 2 | **The report** | Nude ground, **Ivory sheet** | Turn the promise into evidence. This is the product |
| 3 | How it works | Nude | Remove procedural uncertainty: what happens, in what order, when |
| 4 | What a visit includes / what we do not do | Nude | Answer "why not have a cousin do it" and pre-empt over-promising |
| 5 | **Tariffs** | Nude | Price, compared honestly. §3 |
| 6 | **Family Circle** | **Dark Olive** | The differentiator, given a full-width dark band |
| 7 | Trust & verification | Nude | How each claim above is checked. §9 |
| 8 | Honesty panel | Nude, 1px bordered | "We started in 2026. We have no reviews yet." |
| 9 | Founders | Nude | Two named people with published mobile numbers |
| 10 | FAQ | Nude | Six items, accordion, first open |
| 11 | **Consultation form** | Nude ground, **Ivory sheet** | The conversion. The form itself, not a link |
| 12 | Footer | Dark Olive | Bank requirement + contact + legal entity |

**Why the report is section 2, not section 5.** FINAL-UX put it fifth, after "why people use
this", "what a visit is" and "method". I am moving it directly under the hero, and this is the
most consequential structural decision in this document.

The hero's last element is the report sheet *cropped by the fold* — and what survives that crop is
the metadata strip, not a photograph (`14 September 2026 · Tokhmakh · Plot 12` and a `GPS
confirmed` chip). That crop is a promise the very next scroll must pay off. Putting three
explanatory sections between the crop and the payoff spends the strongest scroll momentum the page
will ever have on material the reader has not yet been given a reason to care about. And the order
of belief runs evidence-then-explanation, not the reverse: once a reader has seen a dated,
GPS-stamped, timestamped record of one visit, every subsequent section is cheap to believe. Read
in the other order, "method" is a company describing itself.

Two dark bands on the page and only two. The hero stays light: a dark hero costs fold height,
forces a second header variant, and spends the page's scarcest asset on the one screen where the
tone rule ("not funeral-cliché, no dominant black") is strictest.

**The consultation form is section 11, on the page, on an Ivory sheet.** FINAL-UX ended the page
with a dark band carrying a button that links to a form. The 31.08 contrast table forbids the form
on a dark ground (error `#8C3A2E` measures 2.12 on Dark Olive — invisible). Rather than treat that
as a restriction to route around, I take it as the answer: the closing band goes light, and the
thing on it is the form itself. A page that ends in a button that opens a page that contains a
form loses conversions at two doors instead of none.

### 2.2 Section by section — content slots

Slot IDs are `HOME-n`; the full string budget list is §10.

**1 · Hero** — Nude.
`HOME-1` overline (what we do, disambiguating from dementia care) · `HOME-2` H1 · `HOME-3`
standfirst · `HOME-4` verification strip: one line, three items separated by middots — GPS-tagged ·
photo and video · report within 48 hours · `HOME-5` primary CTA `Request a consultation` +
`HOME-6` support line `No payment now. No account needed.` · `HOME-7` secondary text link
`See a full report` → `#report` · the **report preview**, an Ivory sheet on the Nude ground,
metadata strip at the top, cropped by the fold on purpose.

No animated background. The Vanta cloud layer goes: it costs three CDN scripts (FINDINGS #32),
a large share of the 4.8–5.9MB page weight (#31), and it moves on its own, which §5.5 of the
design package forbids and which is wrong for this subject regardless.

**2 · The report** — Nude ground, Ivory sheet, radius 0, 1px hairline, no shadow.
`HOME-8` section overline · `HOME-9` H2 · `HOME-10` one line of standfirst · **the report sheet**,
rendered as the real component with labelled placeholder media, in the §7.5 block order that
LEAD-REVIEW verified: confirmation → GPS as its own block → photographs grouped `On arrival`
before `After the work`, chronological → crew note last. Three annotations
(`HOME-11/12/13`), as side callouts from 1200 and a numbered list below the sheet at 360.
`HOME-14` link `See the full report` → `/sample-report/`.

**No before/after slider, ever, and the after-image is never the opening image** (LEAD-REVIEW §3;
FINDINGS names the slider for removal). The reason is not aesthetic: a drag control on a
photograph of a family grave turns grief into a toy, and the audit could not even capture its
states because it has none.

**3 · How it works** — Nude. Three numbered steps, Olive line icon, two-word label, one line each:
`HOME-15/16/17` Plan → Visit → Report. Beneath them, both public promises verbatim and identical
to every other place they appear: `HOME-18` `We call or write within one business day.` with
Yerevan hours and the UTC offset beside it, and `HOME-19` `Your report arrives within 48 hours of
the visit.` `HOME-20` link → `/how-it-works/`.

Both promises are currently absent from the entire site in all three languages (FINDINGS #13).

**4 · What a visit includes** — Nude. `HOME-21` H2, then a 2×2 grid at 360 of four method items
(`HOME-22..25`): equipment, chemistry chosen for stone, the crew, the record. Then, at the **same
visual weight**, `HOME-26` `What we do not do` with three items (`HOME-27..29`) linking to
`/legal/limitations/`. Naming limits raises trust more than any adjective, and it gives the bank's
"legal restrictions" requirement a home a human will actually read.

**5 · Tariffs** — Nude. On the home page this is the four named products as **four lines with
prices** plus the Special line and the one-price-list line, not the full card row — the cards, the
credit block and the calculator live on `/pricing/`. `HOME-30a` carries the sentence
`Every visit is the same full visit. The only difference is how many.` Full spec in §3.

**6 · Family Circle** — **Dark Olive band**. `HOME-30` eyebrow in **Sky blue** (10.26 on Dark
Olive) · `HOME-31` H2 in Nude · `HOME-32` one-sentence definition · three bullets `HOME-33..35`
with the petal bullet mark · an avatar row of four initial discs · `HOME-36` link
→ `/family-circle/`. Primary button here is a **Nude fill with a Dark Olive label** (12.93).
No form on this band.

**7 · Trust & verification** — Nude. §9 supplies the content.

**8 · Honesty panel** — Nude, 1px Deep Olive border, radius 2. `HOME-37`, at body size or one step
above. **Never small print, never a footnote, never grey.** Styling this as a disclaimer inverts
its job: it is the most persuasive paragraph on the page precisely because nobody else writes it.

**9 · Founders** — Nude. Two cards: 1:1 portrait, name, role, `tel:`, `wa.me`. `HOME-38..41`.

**10 · FAQ** — Nude, accordion, first item open, six items (`HOME-42..53`, Q+A pairs). Includes
what happens if the crew cannot reach the plot, whether prices differ for clients abroad (no), and
what happens in winter. **No competitor is named, in any question or answer.**

**11 · Consultation** — Nude ground, Ivory sheet. §4.

---

## 3. Tariff presentation

Built on the owner's decision of 26.08.2026. Five products. **All visits are full visits** — the
light/heavy distinction is rejected and the words do not appear anywhere, in copy, in a comparison
table, or in a database column.

| Product | What it is | Price |
|---|---|---|
| **Զննում** / Inspection | One orientation visit: locate the plot, full written inventory, photo and video of the condition, the list of work needed, a quote for minor repair. **No cleaning.** | 20,000 ֏ AMD |
| **Էքսպրես** / Express | One full visit: deep clean of the whole plot and the monuments. Report, portal access | 65,000 ֏ AMD |
| **Օպտիմալ** / Optimal | **4 full visits, one in each season** | 160,000 ֏ AMD / year |
| **Մաքսիմում** / Maximum | **6 full visits** | 200,000 ֏ AMD / year |
| **Հատուկ խնամք** / Special | Non-standard: more visits, a plot over 16 m², more than two monuments, several family plots. **Always begins with a Զննում** | by calculator |

### 3.1 The structure

```
   ┌──────────────────────────────────────────────────────────────────┐
 0 │  ԶՆՆՈՒՄ · 20,000 ֏ AMD                                           │  entry rail — Ivory on
   │  One visit · no cleaning · a written record of what it needs     │  Nude, hairline, not a card
   └──────────────────────────────────────────────────────────────────┘

   ┌───────────────┐   ┌─────────────────────────┐   ┌───────────────┐
   │  Express      │   │  ★ Our recommendation   │   │  Maximum      │   the range — three cards,
   │  1 full visit │   │  Optimal                │   │  6 visits/yr  │   equal height, 2px Deep
   │  65,000       │   │  4 visits/yr · one per  │   │  200,000      │   Olive border on Optimal
   │  ONE-OFF      │   │  season · 160,000       │   │  PER YEAR     │   only
   └───────────────┘   └─────────────────────────┘   └───────────────┘

   ┌──────────────────────────────────────────────────────────────────┐
   │  How money you have already paid is carried forward              │  credit block, always open
   └──────────────────────────────────────────────────────────────────┘
   ┌──────────────────────────────────────────────────────────────────┐
   │  ՀԱՏՈՒԿ ԽՆԱՄՔ / Special      [ the calculator lives in here ]    │  fifth card, full width
   └──────────────────────────────────────────────────────────────────┘
   ┌──────────────────────────────────────────────────────────────────┐
   │  Add to any visit: flowers · a candle                            │  the ritual row
   └──────────────────────────────────────────────────────────────────┘
   MemoryCare Guarantees — three items, named, numeric, with remedies
```

**Why a rail, a row and two panels rather than five cards.** Five priced columns is a spreadsheet,
and two of these five do not belong on the same axis as the other three. Զննում buys
**information**, not care; it is the easiest yes on the page and it is the operational entry point
that locks the plot's GPS point, so it sits at the top where it is met first. Special has **no
price to print**, and a priceless card standing inside a row of published prices is exactly where a
hesitant reader stops. The three cards in the middle are the only three products that differ on one
axis — **how many full visits** — and that is the comparison the page has to make easy.

The client-council record of 26.08 §6 backs the shape: all five personas converged on the same
route, **Զննում → (Express) → Optimal with the credit**, and **not one of them chose Maximum**. So
Maximum's job on this page is to be the anchor that makes Optimal read as right-sized, not to
compete for attention. That is why it gets a secondary button and no border.

### 3.2 The comparison problem: 1 vs 4 vs 6

Now that every visit is the same visit, the comparison collapses to one honest sentence, and it
goes directly beneath the row heading:

> **Every visit is the same full visit. The only difference between these three is how many.**

That sentence does most of the work. The rail below does the rest.

**The year rail.** Every card carries the same 12-cell strip — one cell per month of the
subscription year, grouped into four seasons — with the visits marked on it. Same component, same
width, same position in every card, so the three strips stack into one readable comparison the
moment the eye crosses the row.

| | Marks |
|---|---|
| Զննում (on its rail) | one Deep Olive tick in the first cell, then nothing |
| Express | one mark, then nothing |
| **Optimal** | **4 marks — exactly one in each season group** |
| **Maximum** | **6 marks, evenly distributed** |

All marks are identical: a 12×12 filled Olive square with a 1px Deep Olive outline. There is no
second mark type, because there is no second kind of visit.

This is the strongest argument for the rail. Optimal sells on one sentence — *"four full visits,
one in each season"* — and on the rail that sentence is not a claim, it is the picture. The four
marks land one per season group and the reader sees the promise before reading it. No other
component on this site can do that.

- Season group labels only at 360 (`Spring · Summer · Autumn · Winter`); month initials from 900.
- Cells are a 1px Dark-Olive-at-20% hairline grid.
- Olive on Nude measures **3.12**, clearing WCAG 1.4.11's 3:1 floor for meaningful non-text
  graphics with almost no margin, which is why every mark also carries the 1px Deep Olive outline
  (5.49). The marks are additionally labelled — the visit count is printed as a numeral in the same
  card — so the rail is never the only carrier of the information.
- **The rail never animates and never fills on scroll.** Nothing on this site moves on its own.
- One footnote line under the legend, once per section, not per card:
  `The winter visit runs in a suitable weather window. If none opens, it is added to spring — four visits either way.`

This is the one place in the system where Olive earns a job. It carries no text and receives none;
it is a decorative fill, which is precisely its permitted role.

**The arithmetic line**, under each price, in tabular figures:

| Product | Line |
|---|---|
| Express | `65,000 ֏ AMD · one full visit` |
| Optimal | `160,000 ֏ AMD / year · 4 full visits · 40,000 ֏ per visit` |
| Maximum | `200,000 ֏ AMD / year · 6 full visits · ≈33,300 ֏ per visit` |

Because the visits are now genuinely identical, this is a true per-unit price and needs no
"average" hedge — which is a real gain from the 26.08 simplification. It also states plainly,
without a discount badge we could not substantiate and would not write, that a subscription visit
costs a little over half a one-off visit.

### 3.3 Card anatomy — fixed, top to bottom

1. **Badge reserve, 46px**, present in all three cards whether or not a badge is drawn. Without it
   the card titles sit at different heights and the row reads as an accident (LEAD-REVIEW §8).
2. Badge — **Optimal only**: `Our recommendation`, Deep Olive fill, Ivory label, 14px uppercase,
   radius 2. **Never "most chosen", "bestseller", "most popular", "premium", "basic", "monthly"**,
   in any language. In Armenian: `առաջատար`.
3. Product name, display face. **One script per locale**: the English card says `Optimal` and
   carries no Armenian; the Armenian card says `Օպտիմալ` and carries no Latin.
4. Unit chip, 14px uppercase: `ONE-OFF` / `PER YEAR`.
5. **The year rail** (§3.2).
6. Visit count — the largest element after the price: `4` + `full visits a year`.
7. The one-sentence pitch. Optimal's is fixed and is the product's whole proposition:
   `Four full visits, one in each season.`
8. Price. Tabular figures. **The `֏` glyph is emitted in its own element with its own font stack**
   and the letters `AMD` always follow — the bank requires the currency stated, and FINDINGS #21
   records the glyph currently falling back to a system face and sitting visibly smaller than the
   digits beside it.
9. The arithmetic line (§3.2).
10. Three to four feature lines, **the same slot count in every card** so the rows align across a
    translation into Armenian.
11. The credit line, one sentence, product-specific (§3.4).
12. A growing spacer.
13. CTA at the foot. **Optimal's is the only primary button in the row.** Express and Maximum are
    Deep Olive hairline secondaries. Three consistent signals mark the recommendation — border,
    badge, button weight — and none of them costs the button its language.

Cards in a row are **equal height, always**, and the button is pushed to the foot by the spacer,
not by hand-tuned padding (LEAD-REVIEW §8).

### 3.4 The credit rules, and the best sentence on the page

The rules, exactly:

- **Զննում 20,000 ֏ is credited only on the signing of an annual subscription**, within **60 days**
  of the visit. It is **never** credited into an Express.
- **Express 65,000 ֏ is credited in full into an annual subscription** within **60 days**.
- **One credit only.** At signature, **either** the Զննում **or** the Express is credited — never
  both. A client who bought both gets the larger (65,000) credited, and their Զննում remains a paid
  inspection. There is no credit between one-off products.
- A credited Express **counts as the first visit of the subscription year** (26.08 §14).
- **There is no discounted repeat Express.** 65,000 ֏, every time.

Run the arithmetic and something falls out that the page should lead with:

```
Straight to Optimal                             160,000                = 160,000 ֏ AMD  ·  4 full visits
Զննում first, then Optimal within 60 days        20,000 + 140,000      = 160,000 ֏ AMD  ·  4 full visits, plus the inspection
Express first, then Optimal within 60 days       65,000 +  95,000      = 160,000 ֏ AMD  ·  4 full visits, the Express being the first
```

**Every route costs the same 160,000 ֏ in the first year.** So the credit block is not headed
"discounts" or "how credits work"; it is headed with the fact:

> **Starting small costs you nothing.**
> Whichever way you begin, the first year is 160,000 ֏ AMD and four full visits.

That is the most persuasive true sentence available to this business, and it is the one the client
council's five personas each arrived at independently. It removes the only real objection to the
trust ladder — that trying it first is a surcharge for caution — and it removes it with arithmetic
rather than reassurance.

The block sits **directly beneath the row, always expanded, never behind a tooltip, an asterisk or
a footnote**, containing the three worked lines above and then four bullets:

- One credit for each plot, once, at the moment the subscription is signed.
- One amount only. If you have paid for both, the larger of the two is credited.
- Sixty days from the visit. The portal shows the date the credit runs out.
- There is no cheaper repeat Express. A second Express is 65,000 ֏ AMD, like the first.

Each card also carries its own one-line version at slot 11, so a reader who never reaches the block
still gets the rule at the point of decision.

**Credit windows are shown as a plain date** — `Credit available until 14 October 2026` — never as
a countdown timer. A timer on a memorial-care purchase is a pressure device and the brand forbids
it.

### 3.5 Designing out the 40,000 ֏ repeat

The rejected price is live on the site today (FINDINGS #3), which means removing it from the
rendered page is not sufficient — it will come back the next time someone reasons from an old
document. Three structural measures:

1. **One price constant per product**, held once, in one place, with no second "repeat" or
   "returning client" price field anywhere in the model. There is no field for the value to live
   in.
2. **A build-time content check** that fails the build on the literal strings `40 000`, `40,000`,
   `45 000` and `45,000` anywhere in the price surfaces, in all three locales.
3. **The pricing FAQ answers it out loud**: `Is a second Express cheaper? No — it is 65,000 ֏ AMD
   every time.` A rule stated publicly is much harder to quietly reintroduce than a rule held in a
   document.

### 3.6 Special — the fifth card

A **full-width card beneath the credit block**, Ivory sheet on Nude, 2px radius, hairline border.
Not a column in the row (§3.1).

Contents, in order: name → the one-line definition (`For a plot over 16 m², more than two
monuments, more visits, or several family plots`) → **the calculator** (§3.7) → the price floor
stated honestly as a principle rather than a number the visitor must trust: `A Special visit is
never priced below a Maximum visit.` → the entry rule, stated as a benefit rather than a hurdle:
**`Special always begins with a Զննում — we price it after we have seen the plot, not before.`** →
CTA `Start with an Inspection` (primary) and `Book a consultation` (secondary).

Making the Զննում the required first step of Special is the single best thing about this product's
shape, and the page should say why: nobody can price a 40 m² plot with five monuments from a
description over the phone, and a company that quotes one anyway is guessing with your money.

### 3.7 The calculator

An owner decision of 26.08 §2: **an open formula, two sliders, the same price for everyone, visible
before anyone has to call.** The point is not the arithmetic; it is that the arithmetic is
*published*. This is a trust instrument that happens to output a number.

**Anatomy at 360, top to bottom.** One column; two columns from 1200 with the result panel at 42%
and sticky within the card.

1. Heading, and one line: `The same formula for everyone. Nothing is decided on the phone.`
2. **Base selector** — three radio chips, not a dropdown: `Optimal (4 visits)` · `Maximum
   (6 visits)` · `Express (one visit)`. Optimal preselected.
3. **Slider 1 — Plot area.** Range 16–100 m², step 1, default **16**. Labelled
   `Up to 16 m² is included`. Value shown as text beside the slider **and** editable as a number
   input, because a slider alone cannot be operated precisely by a 58-year-old on a phone and
   because a keyboard user needs the field.
4. **Slider 2 — Monuments.** Range 2–10, step 1, default **2**. Labelled `Up to 2 are included`.
5. **The result panel**, and this is the part that matters: **the arithmetic is shown, not the
   total alone.**

```
Optimal, 4 full visits a year                                  160,000 ֏ AMD
Plot area        24 m²   =  16 included + 8 × 10,000 ֏          + 80,000 ֏ AMD
Monuments         3      =   2 included + 1 × 30,000 ֏          + 30,000 ֏ AMD
                                                              ─────────────────
                                                    per year    270,000 ֏ AMD
```

6. **The rate explanation, published**, because it is the whole reason to show a formula:
   `160,000 ֏ ÷ 16 m² = 10,000 ֏ per square metre per year. An added metre costs exactly what an
   included metre costs.` And for the one-off: `A one-off surcharge is the annual one divided by
   four — one visit instead of four.`
7. **At the default position the calculator shows the list price and says so**:
   `Standard plot — 160,000 ֏ AMD. No surcharge.` It must never open on a blank or a dash. A
   calculator that starts empty teaches the visitor that the page is a form.
8. **At either ceiling** (100 m² or 10 monuments) the result panel replaces the total with:
   `Larger than this we price individually, after an Inspection.` → `Start with an Inspection`.
9. CTA row: `Start with an Inspection` (primary) · `Request a consultation` (secondary, carrying
   the configuration).

**The rates**, from 26.08 §2, flat and identical for Optimal and Maximum:

| | Included | Annual subscription | One-off Express |
|---|---|---|---|
| Area | up to 16 m² | **+10,000 ֏ / year per m² above 16** | **+2,500 ֏ per visit per m²** |
| Monuments | up to 2 | **+30,000 ֏ / year per monument above 2** | **+7,500 ֏ per visit per monument** |

**Behaviour.** Recalculates on `input`, not on release, so the number moves with the thumb — but
the number itself **never animates, never counts up, and never rolls**: it is replaced. Debounce
0ms visually, 300ms before writing to the hidden field. Full keyboard operation:
arrow keys ±1, PageUp/PageDown ±5, Home/End to the ends, `role="slider"` with
`aria-valuenow` / `aria-valuetext` announcing `24 square metres`, and an `aria-live="polite"`
region on the total that announces only after 500ms of quiet so a keyboard user dragging through
ten values is not read ten totals.

**The configuration follows the visitor.** `Start with an Inspection` and `Request a consultation`
both carry `calc_config = {base, area, monuments, computed_total}` into the consultation form as a
hidden field, and the success state echoes it back in words: *"You configured: 24 m², 3 monuments,
Optimal — 270,000 ֏ AMD per year."* Hayk should never have to ask a question the visitor has
already answered.

**Where it lives.** Inside the Special card on `/pricing/`, and **nowhere else**. There is no
calculator on the home page: the home page's job is the four named prices, and a control that asks
a visitor two questions before showing them anything is the wrong first meeting.

### 3.8 Four service decisions from 26.08 that no earlier document put on the site

These are product facts, not marketing, and each one needs a slot.

1. **The assigned crew.** `Your plot is looked after by the same team.` Worded as an assignment,
   **never as a guarantee of an unchanged roster** — 26.08 §3.4 flags that as a legal trap as the
   company grows. Slot: the trust section on the home page, and a feature line in each of the three
   cards.
2. **Two delivery preferences, both optional, both offered as one question at signup** — 26.08 §3.5:
   `How would you like to receive reports, and do you want to know before a visit?`
   - `Send each report as a plain link I can forward` — no login, no password. This is the `/r/`
     guest link (§7.3) sold as a feature rather than hidden as a share action. **Default on**: half
     of all report opens are by people without accounts.
   - `Call or message me the day before a visit` — **default off**, opt-in, and **routable to
     someone else** (the relative in Yerevan). Not a default, by owner decision.
   - Both are changeable afterwards in `/portal/profile/notifications/`, and the portal remains the
     archive of record either way.
3. **Flowers or a candle at a visit** — 26.08 §7.5, a visible option **on the tariffs page**, not
   buried in the portal: *"a grave is not a stone."* Slot: a single ruled row beneath the Special
   card, `Add to any visit`, with the item, one line, and a price. **No source gives this a price**
   — §12.
4. **The year, in full.** Monthly and seasonal payment were rejected by the owner, and so was
   payment in two instalments. The page says the term plainly (`Paid once, for the year`) and never
   implies otherwise. This is the one remaining friction the client council recorded and it is a
   deliberate choice, so the site should not apologise for it or hide it until checkout.

### 3.9 Guarantees

Three, named, numeric, each with its remedy, appearing beneath the tariffs on `/pricing/`, on the
home page, and in full at `/legal/terms/#guarantees`:

1. A **free repeat visit within 7 days** if you are unhappy with a report — counted **from the
   delivery of the report, not from the visit**, so a late report cannot eat the window
   (26.08 §7.1).
2. **Liability for damage**, stated as a figure — a 500,000 ֏ reserve plus insurance. The number
   and the policy reference come from the lawyer; **the word "insured" alone is not acceptable**
   (26.08 §7.2). §12.
3. A **pro-rata refund** on cancellation, computed on the amount actually paid:
   `refund = amount_actually_paid × (visits_not_performed ÷ visits_total)`, rounded **up** to the
   nearest 100 ֏, in the client's favour, no cap. Shown as arithmetic in the cancellation flow
   before confirmation. Under the corrected prices, LEAD-REVIEW §5's worked example is exact again:
   a client who paid **95,000** after an Express credit and has had 1 of 4 visits is refunded
   **95,000 × 3/4 = 71,250 → 71,300 ֏**. Computed from the 160,000 list price it would return
   120,000 — more than the client ever paid.

### 3.10 Stacking order at 360

Զննում rail → **Optimal first**, then Express, then Maximum → credit block → Special with the
calculator → the ritual row → guarantees. On a phone there is no centre, and first beats middle.
The desktop row reads left-to-right as a ladder; the mobile stack reads as a recommendation with
two alternatives. That inversion is deliberate.

---

## 4. Primary conversion: the free consultation request

### 4.1 Where it lives

One component, three containers: **the home page's section 11**, **`/consultation/`** (the page
twin, with a right rail from 1200), and **a modal** opened by every `Request a consultation`
button in the site. The modal and the page share one implementation; the modal is the page's form
in a dialog with a scrim, radius 8, focus trapped, `Escape` closes, focus returns to the trigger.

**Constraint, structural:** the form may never sit inside a dark band, because error `#8C3A2E`
measures 2.12 on Dark Olive and is invisible there. Every container is a **Nude ground with an
Ivory sheet**. This is a rule, not a preference, and it is the reason the home page's closing band
is light (§2.1).

### 4.2 Fields — what we ask

| # | Field | Type | Req | Rules |
|---|---|---|:--:|---|
| 1 | Name | text | ✅ | 2–60 characters, any script. `autocomplete="name"` |
| 2 | Phone or email | **one field**, auto-detected | ✅ | Leading `+` or digit → phone with a country selector; otherwise email. Stored E.164 |
| 3 | Cemetery or city | combobox, free entry always accepted | ✅ | Suggestions for the Yerevan cemeteries, plus `Not sure` as a first-class valid answer |
| 4 | `Add a note` | disclosure holding a textarea + two optional fields (name and phone of a relative in Yerevan) | ❌ | 0–500 characters, counter appears at 400 |
| 5 | Consent | checkbox | ✅ | One line with a link to `/legal/privacy/`. Date and IP recorded server-side |
| — | hidden | — | — | `utm_*`, `page_path`, `locale`, `referrer`, `product` when arriving from a tariff card, and `calc_config` when arriving from the calculator (§3.7) |

**Three visible fields, one disclosure, one checkbox.**

### 4.3 What we deliberately do not ask

Preferred contact time (guessed wrong more often than right, and answered better in the first ten
seconds of the call). Budget. Which package (asking it converts a conversation into a commitment
and this form's entire premise is that the commitment comes after the conversation). Plot size or
monument count — the calculator already asks anyone for whom it matters, and asking everybody
implies a surcharge that the large majority of visitors will never pay. The name of the deceased
(never on a public form; it is a consent decision that belongs on the plot, off by default). Postal
address. Relationship to the deceased. "How did you hear about us" — that question moves to the
**thank-you page**, after the conversion, where a no-answer costs nothing.

**No CAPTCHA.** Spam is handled server-side. A CAPTCHA on the primary conversion of a premium
service, in front of a 55-year-old on a phone, is a self-inflicted wound.

### 4.4 International phone handling

This is exactly where forms fail a diaspora audience, so it is specified rather than left to a
library default.

- One `<input type="tel">` with `inputmode="tel"` and `autocomplete="tel"`, preceded by a country
  selector at 44×44 minimum showing the **dial code and the ISO code as text** — `+374 AM`,
  `+1 US`, `+33 FR`, `+7 RU`. **Never a flag alone**: flags are political, and unreadable at 20px.
  Searchable in all three scripts.
- Default country by IP, **always visibly overridable**, and never re-guessed after the user has
  changed it once.
- Accept and normalise `+1 818 555 0142`, `(818) 555-0142`, `818.555.0142`,
  `+33 6 12 34 56 78`, `093154108`. Store E.164, display formatted per country.
- **Never block on paste.** People paste from their contacts with invisible characters; strip and
  normalise silently.
- `This number is on WhatsApp` is a checkbox, **checked by default for any non-`+374` number**,
  because that is how this audience actually communicates.
- **If the number will not parse and the user presses submit a second time, accept it and flag the
  lead for manual review.** A lost lead costs 160,000 ֏; a malformed number costs Hayk one minute.

### 4.5 Validation and error recovery

- Validate **on blur**, never on keystroke. Once a field is already in error it re-validates on
  keystroke, so a person watching themselves fix it sees it clear.
- The error message renders **below** its field at 14px in `#8C3A2E`, the field border goes 2px
  inset in the same colour, and a 16px glyph precedes the message. **Colour is never the only
  signal** — roughly 8% of a male 40–60 audience is colour-deficient.
- On submit failure, focus jumps to the first invalid field and a summary appears at the top of the
  form with `role="alert"`, linking to each field by id.
- **The submit button is never disabled before submission.** A disabled button with no explanation
  is the most common accessible-form failure. On press it goes to `Sending…` and the form locks.
- Every input is 16px or larger, or iOS zooms on focus.
- **Values survive every failure**, including a lost network. Nothing a person typed is ever thrown
  away by our code.
- **The server-error state is the most important error on the site**: keep every value, show
  `We could not send that. Your details are still here — please try again.`, a retry button, and
  **both founders' direct numbers plus `info@memorycare.am` as a manual path**. A person who has
  decided to spend 160,000 ֏ and hit a 500 must not be left with nothing to do.
- Every field has a real `<label>`. The current site has **zero labels on eighteen pages**
  (FINDINGS #10) and **no visible focus change at all** (FINDINGS #24): 2px Deep Olive focus ring
  at 2px offset, `:focus-visible`, never removed.

### 4.6 Success, and what we promise

In the modal, success replaces the form **in place**, no page change. On `/consultation/` and on
the home page, success navigates to **`/consultation/thank-you/`** — a real URL, because it is the
conversion target every future ad and every analytics setup will need, and an in-place swap gives
them nothing to fire on.

The success state contains, in order:
1. `Thank you, {name}.`
2. **The promise, verbatim and identical to its five other occurrences:**
   `We call or write within one business day.` — with `Yerevan business hours, 09:00–18:00
   (UTC+4)` on the line beneath it, so a reader in Glendale can convert it without arithmetic.
3. Who, by name: `Hayk will write to you on WhatsApp from +374 93 154 108 first, and call only if
   you prefer.` Both numbers as live `tel:` and `wa.me` targets.
4. An echo of what they told us — the contact detail, the cemetery, and the calculator
   configuration if one was attached (`You configured: 24 m², 3 monuments, Optimal — 270,000 ֏ AMD
   per year.`) — so a typo is caught now rather than after a missed call.
5. Two onward actions, both non-committal: `See a full report` and `How it works`.
6. Only then, low in the page: `How did you hear about us?` — one optional question.

**Nothing on this page asks for money, an account or a password.**

---

## 5. Secondary flow: choosing a package and paying

### 5.1 Where it starts and what it is

Every tariff CTA (`Choose Optimal`) goes to **`/pay/?product=optimal`**, carrying `calc_config`
when the visitor came through the calculator. The page states the term before anything else:
**paid once, for the year** — monthly, seasonal and two-instalment payment were all rejected by the
owner, and the page never implies otherwise or defers the fact to checkout. `/pay/` presents two paths
**as equals**, not as one working and one broken:

- **Bank transfer — available now.** Choose the product → confirm name, contact and the cemetery →
  we generate an invoice → wire instructions on screen and as a PDF → `Tell us when you have sent
  it`.
- **Card payment — when the bank enables it. No date is promised.**

Showing a greyed-out card button with no explanation reads as a broken site; labelling it honestly
reads as a young company, which is what we are. **Never a date**: card acquiring depends on
Ameriabank clearing the eight site conditions, and a missed date on the payment page is the worst
possible first broken promise.

### 5.2 Where it hands off to the platform

The marketing site and the contractor's platform (target ~20.09.2026) are separate workstreams and
the boundary must be a line, not a blur.

**The marketing site owns:** every marketing route, the consultation form, `/pay/` and the invoice
request, and the four legal documents. It **never** holds card data, never creates an account, and
never renders a report belonging to a real client.

**The platform owns:** checkout and card capture, the account, the plot, the visit, the report, the
Family Circle, billing, cancellation and the guest link.

**The handoff** is a single POST of a signed order intent — `{product, locale, contact, cemetery,
utm, calc_config, credit_reference}` — to the platform, followed by a redirect. The marketing site receives back
only an opaque order id and shows `/pay/thank-you/`. Nothing about the client's plot ever lives in
two systems.

**Until the platform is live**, the card path is not a dead button: it is replaced by
`Request an invoice`, which opens the consultation form pre-filled with the chosen product and a
different heading. One flow to build, two labels, no broken state. That is what ships on day one.

### 5.3 The eight bank conditions, mapped

| Condition | Where it is satisfied |
|---|---|
| About page | `/{loc}/about/` |
| Contacts in every footer | Footer, §1.4 |
| Full service descriptions | `/{loc}/pricing/` + `/{loc}/how-it-works/` |
| Legal restrictions | `/{loc}/legal/limitations/`, linked from How it works |
| Real prices in AMD | Every price carries `֏` **and** the letters `AMD` |
| Privacy policy in English | `/en/legal/privacy/` |
| Return policy | `/{loc}/legal/refund/`, holding the pro-rata arithmetic |
| Service-delivery terms | `/{loc}/legal/terms/` |

No copy pass ships without all eight present. They are also, not coincidentally, eight of the best
trust assets we have (§9).

---

## 6. The portal entry

### 6.1 Registration — deleted

**Public self-registration is removed.** `/{loc}/account/register/` 301s to `/{loc}/consultation/`.

The argument, in two sentences: an account created before a purchase has no plot, no visit and no
report in it, so it is an empty room we invite people into and then have to explain — and today's
register form takes a name, a phone, an email and a password **with no consent control, no privacy
link and no password confirmation** (FINDINGS #9), which is a live legal exposure for zero
conversion benefit. Accounts are created by us, at the moment of payment, and the client enters
through **`/portal/activate/:token/`** from the welcome email.

This is contestable — it removes a visible "Register" affordance a stakeholder may expect. It is
still right: the primary conversion is a conversation, and a second, weaker call to action beside
it splits the page's intent.

### 6.2 Sign in — `/portal/login/`

Two methods, **side by side, magic link first**:
- **Email me a sign-in link** (primary). Single field, then `/portal/login/check-email/`.
- **Sign in with a password** (secondary, a disclosure).

Magic link leads because the user is a 55-year-old who bought one annual subscription and will next
sign in three months later; the probability they remember a password is low and the cost of a
failed sign-in on this product is a phone call to Hayk.

`Forgot your password?` is a 44px target (it currently measures 147.5 × 19.5 — FINDINGS #25).

**Locale is never silently changed.** `/en/portal/…` today redirects an English speaker into an
Armenian sign-in page (FINDINGS #15). Sign-in preserves the requested locale through the whole
round trip, including the email.

**Sign-out is a POST**, never a link. An automated crawl ended a live session during the audit
(FINDINGS #16); any prefetcher, antivirus link-scanner or chat-app preview will do the same.

### 6.3 Reset — `/portal/reset/`

One field. The response is always the same whether or not the address exists:
`If that address is registered, we have sent a sign-in link.` No account enumeration.

### 6.4 Account index — first run, before any report exists

**This is the most important screen in the product** and the current one is a sidebar of profile
fields beside a body of Lorem Ipsum (`spot-1440.png`). A client has just paid a large sum to a
company they have never met, and there is nothing to show them.

**The screen must not look empty. It must look scheduled.**

1. `Welcome, {name}.`
2. **Status card**, Ivory on Nude, full width: the plot identity → `Subscription active` → **the
   first-visit window as the largest text on the card** (`First visit: 12–16 September`) → one line
   naming who will come and stating that the crew records a GPS point on arrival.
3. **Progress rail** — four labelled dots: `Subscription active` ✓ · `Plot located` · `First visit`
   · `Report`. Dot 1 filled, dot 2 ringed, 3 and 4 outline. This is the whole psychological job of
   the screen: it converts an empty state into a timeline with a position on it.
4. **What happens next** — three rows, each with a time: within two days we confirm the plot
   coordinates · the day before the visit you get a reminder if you asked for one · **within 48
   hours of the visit, your report.**
5. **Two actions**: `Invite a family member` (**primary** — it gives her something to do on a
   screen with nothing to read, and it has the highest retention value of anything here) and
   `See a sample report` (secondary).
6. Support row: `Hayk — +374 93 154 108`, as `tel:` and `wa.me`.

One question is asked once, here or at signup, and never again: **how would you like to receive
reports, and do you want to know before a visit?** Three checkboxes (§3.8 item 2) — the plain
forwardable link **on** by default, the day-before notice **off** by default and routable to a
relative in Yerevan. It is the only question on this screen, and answering it is the second thing
there is to do.

Above the fold at 360: items 1, 2 and the top of 3. **If the client must scroll to learn when the
first visit is, this screen has failed.**

Once reports exist the screen becomes the plot dashboard (FINAL-UX §7.2), unchanged.

### 6.5 Add-package — `/portal/orders/new/`

Today `/account/packages/add/1/` re-asks the signed-in user's own name, phone and e-mail back at
them beside a single green card selling `PACKAGE 3 · 180000 ֏ · 2 full visits · 4 preventive
visits` — a rejected price, a rejected composition and a rejected visit split on one screen
(`packages-add-1__en__1440__default-fold.png`) — it is a registration form wearing a package. Replaced by an **authenticated
request**: plot selector (only when there is more than one) → service cards with prices, with the
recommended work from the last report pre-selectable → date preference (as soon as possible, or a
named month) → notes → a price summary → `Send request`.

**It is a request, not a checkout**, and the button's helper line says so, because card acquiring
is not live. Nothing on this screen implies a charge has been made.

### 6.6 Portal chrome

Header 56px: mark, plot switcher (only when there is more than one plot), avatar menu. Below 900
a **bottom tab bar**, 56px + `env(safe-area-inset-bottom)`, four tabs — **Plots · Visits · Family ·
Account**; from 900 a 240px left sidebar. List rows are 72px minimum and the whole row is the
target.

---

## 7. Family Circle

The differentiator. hush.am has photo reports and GPS grave locating and has had them since ~2015;
what it does not have is a portal, sub-accounts, or a shared family view. **We never claim to be
the only ones doing grave care with photo reports in Yerevan.** We claim the combination.

### 7.1 The shared-view model

Four roles. Three are memberships; the fourth is a link.

| Role | Who this actually is | Auth |
|---|---|---|
| **Owner** | The payer. Exactly one per plot, always | Full account |
| **Family manager** | The trusted relative, usually the eldest sibling or the one in Yerevan. Sees everything about care, cannot spend | Full account, by invitation |
| **Family member** | The aunt, the cousins. Sees care, never sees money. **The default suggested role** | Full account, by invitation |
| **Guest** | Anyone holding an `/r/` link. Roughly half of all report opens | None, ever |
| *Local contact* | Not a role and not an account: the person in Yerevan who meets the crew. Recorded on the plot, messaged only after an explicit third-party consent | None, ever |

Data values `owner | manager | member`. On screen: Owner · Family manager · Family member · Guest.
Never "payer", "subscriber", "viewer", "beneficiary".

The permission matrix is FINAL-UX §9.1 adopted verbatim, minus the rows that referenced the deleted
calculator and surcharges. The four rules that fall out of it:

1. **A family member never sees money.** Not the plan name, not a price, not the renewal date, not
   an invoice. This is the role for the aunt and it is the default.
2. **A family manager can spend nothing without the owner.** A manager's order becomes a request
   that lands on the owner's dashboard as a decision. That is what makes it safe to hand a relative
   real control.
3. **Only the owner cancels, transfers, or changes how the plot is named in reports.** One person
   owns the money, always; and the name is a consent decision.
4. **Past reports stay readable forever, including after cancellation** — owner, manager, member,
   and anyone holding a link already shared. Read-only: no new visits, no renewal prompt, no
   upsell, no price on those screens. Access to reports about a family member's grave is not a SaaS
   feature to be switched off.

### 7.2 The invite flow, concretely

**`/portal/family/` — the roster.** Initial disc, name, role, `invited` / `active`, and which plots
they can see. The owner row is pinned first and cannot be removed. `Invite a family member` is the
primary action. Beneath it, a collapsed `What each role can do` accordion holding the matrix.

**`/portal/family/invite/`:**
1. Name — optional.
2. **Phone or email** — required, the same auto-detecting field and the same country selector as
   the consultation form (§4.4). One component, used twice.
3. **Role, as three radio cards with a one-line consequence each, never a dropdown.** A dropdown
   hides the consequence of the choice, and the consequence here is whether a relative can see what
   the family paid. Card 3 (`Family member`) is preselected.
4. Plot scope checkboxes — shown only when there is more than one plot.
5. Optional message, 200 characters.
6. **Delivery choice: `Send by email` / `Send by WhatsApp`.** WhatsApp produces a pre-filled
   `wa.me` message the owner sends from their own phone. This matters more than it sounds: the
   invitee is a 70-year-old aunt who does not open email, and an invitation that arrives from a
   familiar name in WhatsApp is opened and one from `noreply@` is not.
7. `Send invitation`.

The confirmation states exactly what the invitee will receive and that the invitation is **valid
for 14 days**.

**`/portal/invite/:token/` — what the invitee sees.** Brand block → `{Name} invited you to the
Family Circle for {plot}` → **what this role can do, three plain bullets** → set a password, or
continue with a sign-in link → `Accept`.

**Acceptance lands directly on the most recent report.** Not on a dashboard, not on a welcome
screen — on the photographs. The payoff is immediate, and it is the entire reason the feature
retains people.

**`/portal/family/:memberId/`** — role, plot scope, remove. Removal is immediate and says so.

### 7.3 The guest link

`/r/:shareToken/` — no login, short root path (`memorycare.am/r/8fk2wq` is a link a person can
retype; anything under `/portal` implies a wall and gets ignored). No price, no plan, no upsell, no
account prompt anywhere on it, and the network payload is checked for the same — the audit could
not run that check because the route does not exist (GAPS §4).

**The deceased's name is off by default** on every report and every link. A report shows cemetery,
sector and plot. The name appears only if the owner switches it on; the setting lives on the plot,
is reversible, and turning it off removes the name from links already issued. The link is forwarded
into family group chats and part of the audience is in the EU.

The link preview (OG card) carries the mark, `Visit report`, and the date. **No photograph, no
cemetery, no name** — a WhatsApp preview of a grave in a group chat is not something we cause to
happen.

The one permitted guest action is `Something is wrong with this` → three fields, no consent
theatre, no account, nothing about signing up.

---

## 8. Mobile-first: what is different at 360, not merely narrower

360 is the QA floor and the primary channel. Frames may be drawn at 375; nothing ships until it
passes at 360×640.

### 8.1 Deliberately different, not just reflowed

| | 360 | ≥900 |
|---|---|---|
| Nav | Full-screen drawer, **language first** | Five inline items, language in the utility slot |
| Tariff row | Stacked, **Optimal first** | Row of three, ladder order, Optimal centre |
| Year rail | 12 cells, **season labels only**, no month names | 12 cells with month initials |
| Report annotations | **Numbered list below** the sheet | Side callouts from 1200 |
| Report photographs | 1-up, full-bleed, edge to edge | 2-up, document capped at 720px |
| Permission matrix | **Four stacked role cards**, each a can/cannot list | The table |
| Verification rail | Horizontal ruled strip under its content | Right column, 222px |
| Portal nav | Bottom tab bar, 4 tabs | 240px left sidebar |
| Footer | One column, **phone numbers first** | Four columns |
| Legal pages | Table of contents as an accordion | Sticky TOC from 1200 |

The permission matrix is the clearest case: **a horizontally scrolling frozen-column table is not
an acceptable mobile fallback for a 55-year-old.** Four cards is a different design, not a smaller
one.

### 8.2 Floors, all currently failed

- **Pinch-zoom enabled.** `user-scalable=no` and `maximum-scale=1.0` come out of the viewport meta
  on every page (FINDINGS #7, critical on 18/18 pages). The audience is 35–60.
- **Body 16px minimum.** Today the bulk of the page is 15px, with 132 elements at 14px, 24 at 13px
  and one at 12px (FINDINGS #26).
- **Uppercase chips and badges never below 14px.**
- **44×44 minimum hit area** for everything interactive, 48px tall for anything primary; visual
  size may be smaller than the hit area. 8px minimum between adjacent targets, **12px in the
  footer** where a mis-tap costs a lead. Today: hamburger 28×27, language links 33×22.5, order
  button 205×31 (FINDINGS #25).
- **Visible focus on every focusable element**: 2px Deep Olive ring at 2px offset, switching to
  Nude on Dark Olive, `:focus-visible`, never removed.
- **`<html lang>` correct per locale** (currently `en` on all 18 pages — FINDINGS #6), one `<h1>`,
  one `<main>`, a real `<footer>` (currently none of the three exist anywhere — FINDINGS #34).
- Every image has `alt`, every link has a discernible name (198 and 126 failures today —
  FINDINGS #11).

### 8.3 Thumb reach

- The primary action of any screen is in the bottom third or in the sticky bar.
- **Destructive and irreversible actions are never within 100px of the bottom edge** — cancel a
  subscription, remove a family member, revoke a link. They sit high, and they confirm.
- The drawer's close control is at the **bottom** as a full-width row *as well as* top-right,
  because the top-left of a 360×640 screen is the least reachable point for a right-handed
  one-handed grip. The drawer also closes on scrim tap and on `Escape`.
- Form submit buttons are full-width from 360 to 599.

### 8.4 The sticky CTA — yes, with four suppressions

**One sticky bar, and only one, ever.** Two pinned bars on a 640px viewport is a quarter of the
screen and is not a state that may exist.

Spec: present 360–899 only. 64px + `env(safe-area-inset-bottom)`. Ivory fill, 1px top hairline, no
shadow. Appears at `scrollY > 320` with a 160ms ease-out translate, respecting
`prefers-reduced-motion` (which renders it without the translate, not without the bar). Contents:
one 44px `call` target plus one full-remaining-width primary `Request a consultation`.

**Suppressed** on `/consultation/`, on the four legal pages, on every report and guest-report route,
**while any form field has focus** (it otherwise sits on top of the keyboard), and **while the home
page's consultation form is in the viewport** — a sticky button that scrolls to a form the reader
is already looking at is a button that makes the site feel stupid.

In the portal the bottom tab bar replaces it; the two never coexist.

---

## 9. Trust architecture with zero customers

We cannot show social proof. Everything below is a substitute that is **true today**, and each one
is a structure, not a sentence.

1. **Verification instead of testimony.** Every report carries a GPS point recorded on arrival, a
   timestamp, photo and video, and the crew's name. The sample report is on the public site at
   section 2 of the home page and at `/sample-report/` — **the strongest trust asset we own is the
   product itself, shown, not described.**
2. **Named humans with published mobile numbers.** Davit Hambardzumyan +374 55 315 323 and Hayk
   Manukyan +374 93 154 108, as `tel:` and `wa.me`, in the footer of every page, on About, on
   Contacts, in the drawer, and in the consultation success state. A founder's published mobile
   outweighs seventy anonymous reviews and costs nothing.
3. **Two numeric promises we control, stated identically in all six places they appear**, with
   nobody permitted to soften or sharpen them locally: `We call or write within one business day.`
   and `Your report arrives within 48 hours of the visit.` Business hours in Yerevan time with the
   UTC offset spelled out, every time, because "09:00–18:00" alone is useless in Glendale.
4. **Named limits.** `What we do not do`, at the same visual weight as what we do. Weather, locked
   sections, disputed access, and the rule that **no visit is ever silently skipped** — a winter
   visit with no suitable weather window is added to spring, and the visit count is guaranteed
   regardless.
5. **The honesty panel**, at body size on the home page: we started in 2026, we have no reviews
   yet, here is what we do instead. This is the single most persuasive paragraph available to a
   pre-launch company, and it only works at full size — as small grey print it becomes a
   disclaimer and does the opposite of its job.
6. **The legal-entity block** in every footer: MemoryCare LLC, registration number, legal address,
   both phones, `info@memorycare.am`. A bank requirement that doubles as the thing a cautious buyer
   abroad looks for first.
7. **Price transparency.** One price list, stated on the pricing page:
   `One price list — the same in Yerevan and in Los Angeles.` And in the FAQ, plainly: prices do
   not differ for clients abroad. A diaspora buyer's first suspicion is that they are being charged
   a distance premium; answer it before it is asked.
8. **Guarantees, named, numeric, with remedies**: a free repeat visit within 7 days if the client
   is unhappy with a report; liability for damage; a pro-rata refund computed on the amount
   actually paid. The refund arithmetic is shown as arithmetic in the cancellation flow before
   confirmation — `refund = amount_actually_paid × (visits_not_performed ÷ visits_total)`, rounded
   **up** to the nearest 100 ֏, in the client's favour, with no cap. Computed from the list price
   instead of the amount paid, this returns more than the client ever gave us; that is
   LEAD-REVIEW §5 and it still stands under the new prices (a client who paid 120,000 after an
   Express credit and has had 1 of 6 visits is refunded 100,000, not 150,000).
9. **The weather-window guarantee, stated as a term rather than a caveat.** The winter visit runs
   in a suitable weather window, not on a date, because the protocol limit is temperature — and if
   no window opens, the visit is **added to spring**. Four visits either way. This is unusually good
   material: the company volunteering the one thing a client would otherwise discover in February,
   and volunteering it with a remedy already attached. Nobody writing marketing copy invents a
   paragraph like that, which is exactly why it reads as true.
10. **The assigned crew.** `Your plot is looked after by the same team.` For someone who cannot be
    there, the fear is not that the work is bad but that it is anonymous. Worded as an assignment,
    never as a promise of an unchanged roster.
11. **`Starting small costs you nothing.`** (§3.4.) A trust ladder is only a trust ladder if the
    cautious route is not punished, and the arithmetic shows it is not. Published arithmetic is
    itself a trust instrument; the calculator (§3.7) is the same instrument applied to the awkward
    cases, and its real output is not a number but the sentence *nothing is decided on the phone*.
12. **The register of the whole thing.** No condolence copy, no guessing at why someone is buying,
   no grief imagery, no candles, no crosses. Calm, administrative, precise. For this audience,
   competence *is* the trust signal.

**And what may never appear, in any language, in any tense:** testimonials, star ratings, review
counts, customer counts, graves-serviced counts, years in business, a partners row, "trusted by",
"the only ones", any claim about what most clients choose, and any stock photograph of anything
other than our own work. The current site carries four fabricated figures and three fabricated
testimonials illustrated with photographs of real public figures under invented names
(FINDINGS #1, #2). All of it goes, and nothing takes its place except the nine items above.

---

## 10. Content requirements — the string slots

Handed to the content team. **Every budget below is the English budget.** Armenian runs 15–30%
longer and Russian 15–25%; **the component is built to `EN × 1.30` and the Armenian string is the
one that must be checked against the layout**, never the English. Where a budget is marked
**hard**, the string must not exceed it in any of the three languages and content chooses a
shorter formulation rather than the component growing.

Every slot is needed in **three languages**. One script per locale: the English site carries no
Armenian anywhere, the Russian site no Latin product names.

### Global — appears on every page

| # | Slot | Budget (EN) | Notes |
|---|---|---|---|
| 1 | Nav item ×5 | 18 ch each, **hard** | Pricing / How it works / Sample report / Family Circle / About |
| 2 | Primary button label | **22 ch, hard** | `Request a consultation` is exactly 22 |
| 3 | `Sign in` link | 12 ch, hard | |
| 4 | Language labels ×3 | 4 ch, hard | Native script: `ՀԱՅ` `ENG` `РУС` |
| 5 | Skip-to-content link | 24 ch | |
| 6 | Footer column headings ×4 | 16 ch, hard | |
| 7 | Footer service links ×4 | 22 ch | The four product names |
| 8 | Footer legal links ×4 | 30 ch | |
| 9 | Legal-entity block | 160 ch | Name, reg. number, address |
| 10 | Copyright line | 60 ch | |
| 11 | Founder role labels ×2 | 24 ch | |
| 12 | Business-hours line | 55 ch | Must contain the UTC offset |
| 13 | Meta title, per route per locale (15 routes) | **60 ch, hard** | Must disambiguate from dementia care |
| 14 | Meta description, per route per locale | **155 ch, hard** | |
| 15 | OG title / OG description | 60 / 110 ch | |

### The two promises — write once, use six times

| # | Slot | Budget | Notes |
|---|---|---|---|
| 16 | Callback promise | **48 ch, hard** | `We call or write within one business day.` |
| 17 | Callback hours qualifier | 46 ch | `Yerevan business hours, 09:00–18:00 (UTC+4)` |
| 18 | Report promise | **52 ch, hard** | `Your report arrives within 48 hours of the visit.` |

**These three strings are frozen.** Any variation anywhere is a defect.

### Home

| # | Slot | Budget | Notes |
|---|---|---|---|
| 19 | Hero overline | **32 ch, hard** | Says what we do; must survive out of context |
| 20 | Hero H1 | **48 ch, hard** | Two lines at 32px on 360 |
| 21 | Hero standfirst | **105 ch, hard** | Three lines at 360. Names both reasons, ranks neither |
| 22 | Verification strip, 3 items | 22 ch each, hard | |
| 23 | Hero CTA support line | 40 ch | `No payment now. No account needed.` |
| 24 | Report section overline / H2 / standfirst | 24 / 44 / 100 ch | |
| 25 | Report annotations ×3 | 90 ch each | GPS, timestamps, condition notes |
| 26 | Report section link | 24 ch | |
| 27 | How-it-works step labels ×3 | **14 ch each, hard** | Two words each: Plan / Visit / Report |
| 28 | How-it-works step lines ×3 | 80 ch each | |
| 29 | Method H2 | 44 ch | |
| 30 | Method items ×4 (label + line) | 20 / 90 ch | |
| 31 | `What we do not do` H3 | 30 ch | |
| 32 | `What we do not do` items ×3 | 70 ch each | |
| 33 | Family Circle eyebrow / H2 / definition | 24 / 40 / **120 ch hard** | The definition is one sentence |
| 34 | Family Circle bullets ×3 | 60 ch each | |
| 35 | Trust section H2 + items ×4 (label + line) | 40 / 22 / 90 ch | |
| 36 | **Honesty panel** | **240 ch, hard** | Body size, never small print |
| 37 | Founder cards ×2 (name, role, one line) | 32 / 24 / 70 ch | |
| 38 | FAQ questions ×6 | **70 ch each, hard** | Fit one line at 900 |
| 39 | FAQ answers ×6 | 320 ch each | |
| 40 | Closing form heading + support line | 44 / 90 ch | |

### Pricing

| # | Slot | Budget | Notes |
|---|---|---|---|
| 41 | H1 / subhead | 40 / 90 ch | |
| 42 | One-price-list line | **60 ch, hard** | `One price list — the same in Yerevan and in Los Angeles.` |
| 43 | **The sameness line** | **70 ch, hard** | `Every visit is the same full visit. The only difference is how many.` Sits under the row heading and does most of the comparison work |
| 44 | Զննում rail: name / one-line description / CTA | 22 / **90 ch hard** / 20 ch | |
| 45 | `One-off · not a subscription` chip | **26 ch, hard** | 14px uppercase; longest in RU |
| 46 | Product names ×5 | **22 ch, hard** | One script per locale |
| 47 | Unit chips `ONE-OFF` / `PER YEAR` | **12 ch, hard** | 14px uppercase |
| 48 | Visit-count caption ×3 | **20 ch, hard** | `full visits a year` |
| 49 | One-sentence pitch ×3 | **56 ch, hard** | Optimal's is fixed: `Four full visits, one in each season.` |
| 50 | Year-rail season labels ×4 | 10 ch each, hard | Month initials from 900 |
| 51 | Year-rail footnote | **120 ch, hard** | The weather-window rule, once per section |
| 52 | Per-visit arithmetic line ×3 | 44 ch, hard | |
| 53 | Feature lines, 4 per card × 3 cards | **54 ch each, hard** | Same slot count in every card; one of them is the assigned-crew line |
| 54 | Per-card credit line ×3 | **60 ch, hard** | |
| 55 | Card CTA labels ×3 | **20 ch, hard** | |
| 56 | `Our recommendation` badge | **22 ch, hard** | 14px uppercase. HY: `առաջատար` |
| 57 | **Credit block headline + subline** | **34 / 90 ch, hard** | `Starting small costs you nothing.` + the 160,000 sentence |
| 58 | Credit worked lines ×3 | 80 ch each | Arithmetic, shown as arithmetic |
| 59 | Credit bullets ×4 | 80 ch each | One of them is the no-cheaper-repeat rule |
| 60 | Credit-expiry line, portal | 46 ch | A plain date, never a countdown |
| 61 | Special card: name / definition / price-floor line / entry rule | 22 / **110 ch hard** / 60 / **110 ch hard** | The entry rule is the persuasive one |
| 62 | Special CTAs ×2 | 26 ch, hard | |
| 63 | Calculator heading + open-formula line | 40 / **80 ch hard** | `The same formula for everyone. Nothing is decided on the phone.` |
| 64 | Base-selector chips ×3 | **22 ch, hard** | `Optimal (4 visits)` etc. |
| 65 | Slider labels ×2 + included captions ×2 | 20 / **28 ch, hard** | `Up to 16 m² is included` |
| 66 | Result-panel row labels ×4 | 24 ch, hard | Base, area, monuments, total |
| 67 | Default-state line | 50 ch, hard | `Standard plot — 160,000 ֏ AMD. No surcharge.` |
| 68 | Ceiling-state line | **90 ch, hard** | Replaces the total at 100 m² / 10 monuments |
| 69 | Rate-explanation lines ×2 | 110 ch each | The published per-m² reasoning and the ÷4 rule |
| 70 | Slider `aria-valuetext` patterns ×2 | 30 ch | `24 square metres`, `3 monuments` |
| 71 | Ritual row: heading, item labels ×2, one line, price | 20 / 18 / 70 / 16 ch | **Price unknown — see §12** |
| 72 | Payment-term line | 40 ch, hard | `Paid once, for the year.` |
| 73 | Guarantee names ×3 | 30 ch each | |
| 74 | Guarantee remedies ×3 | 120 ch each | Each contains a number; #1 counts from report delivery, #2 needs the liability figure |
| 75 | Payment-reality line | 130 ch | Card payment, no date promised |
| 76 | Pricing FAQ ×6 (Q + A) | 70 / 300 ch | Must include: do prices differ abroad (no); is a second Express cheaper (no, 65,000 every time); what happens if winter has no weather window |

### How it works · Sample report · Family Circle · About · Contacts

| # | Slot | Budget | Notes |
|---|---|---|---|
| 77 | How it works: H1 / standfirst | 40 / 100 ch | |
| 78 | Timeline steps ×4 (number label, heading, body) | 14 / 30 / 220 ch | |
| 79 | `What a full visit includes` ×6–8 | 60 ch each | The arsenal — steam generator, Kärcher, vacuum, professional chemistry |
| 80 | `What we do not do` ×4 | 70 ch each | Links to `/legal/limitations/`. Includes the municipal-permission limit on construction work |
| 81 | **Weather-and-access paragraph** | **420 ch, hard** | The temperature limit, the weather window, and the added-to-spring guarantee, in that order |
| 82 | `We do not steam a monument that does not need it` line | 130 ch | Over-aggressive cleaning damages stone. Method as care, not as an equipment list |
| 83 | Assigned-crew line | **60 ch, hard** | Assignment, never an unchanged-roster promise |
| 84 | First-visit paragraph | 220 ch | Never described as a survey; only Զննում is a survey |
| 85 | Sample report: H1 / one-line header | 40 / 90 ch | |
| 86 | Report block labels ×6 | **22 ch each, hard** | Confirmation, GPS, On arrival, After the work, Crew note, Next visit |
| 87 | Report annotations ×4 | 130 ch each | |
| 88 | Link-preview explainer block | 200 ch | Demonstrates the OG rule and answers the privacy question |
| 89 | Delivery-preference question + 3 checkbox labels | 80 / **56 ch hard** | Asked once, at signup or first entry (§3.8) |
| 90 | Family Circle: H1 / definition | 40 / **120 ch hard** | |
| 91 | Family Circle steps ×3 | 90 ch each | |
| 92 | Role names ×4 | **20 ch, hard** | Owner / Family manager / Family member / Guest |
| 93 | Role can/cannot lines, 3 + 2 per role | 56 ch each, hard | Must fit a 360 card |
| 94 | The Yerevan-relative paragraph | 200 ch | The person who meets the crew needs no account and never sees a price |
| 95 | Privacy note | 260 ch | Removal is immediate; links can be revoked |
| 96 | About: two opening paragraphs | 400 ch each | |
| 97 | About: why-it-exists paragraph | 300 ch | |
| 98 | About: method items ×3 | 120 ch each | |
| 99 | Contacts: hours block | 120 ch | UTC offset spelled out |
| 100 | Contacts: map placeholder label | 60 ch | Visibly a placeholder |

### Forms, states and system messages

| # | Slot | Budget | Notes |
|---|---|---|---|
| 101 | Consultation heading / support line | 44 / 90 ch | |
| 102 | Field labels ×5 | **24 ch, hard** | Real `<label>`s, not placeholders |
| 103 | Field helper texts ×3 | 70 ch each | |
| 104 | Note-disclosure prompt | 140 ch | `For example: the best hours to call you…` |
| 105 | Consent line | **110 ch, hard** | One line with a link. Not a wall of text |
| 106 | Error messages ×9 | **70 ch each, hard** | One per rule in §4.2, plus the two phone variants |
| 107 | Error summary heading | 60 ch | `role="alert"` |
| 108 | Submit label / sending label | 22 / 14 ch, hard | |
| 109 | Success: heading, promise echo, who-will-call, next actions ×2 | 40 / (16–18) / 110 / 24 ch | |
| 110 | Server-failure message + retry label | 130 / 20 ch | Must include the manual fallback |
| 111 | `How did you hear about us?` + 6 options | 40 / 24 ch | Thank-you page only |
| 112 | Country-selector search placeholder | 40 ch | Searchable in three scripts |
| 113 | WhatsApp checkbox label | 44 ch | |
| 114 | Portal first-run: greeting, status card ×4 lines, rail labels ×4, next-steps ×3, actions ×2, support row | 24 / 40 / 22 / 90 / 24 / 50 ch | §6.4 |
| 115 | Invite flow: heading, role-card titles ×3, role consequence lines ×3, delivery labels ×2, confirmation | 40 / 20 / **70 ch hard** / 20 / 180 ch | §7.2 |
| 116 | Invitation-received page: heading, role bullets ×3, accept label | 80 / 60 / 20 ch | |
| 117 | Guest report: header line, `The visit took place`, feedback labels ×3 | 60 / 30 / 24 ch | No price, no upsell |
| 118 | Empty states ×6 | 90 ch each | Never the word "empty"; always names the next event |
| 119 | 404: heading, line, five link labels, phone line | 30 / 90 / 22 / 40 ch | |
| 120 | 500: heading + line | 30 / **90 ch hard** | `Something on our side is not working. Your data is safe.` |
| 121 | Bad-news states ×3 | 180 ch each | Visit rescheduled (the new date must be present), crew could not reach the plot, guarantee re-visit requested |
| 122 | Cancellation flow: heading, the arithmetic line, confirm/cancel labels | 40 / 90 / 20 ch | Arithmetic shown before confirmation |
| 123 | Transactional email subjects ×7 + preheaders | **60 / 90 ch, hard** | Welcome, report ready, invitation, reminder, renewal offer, invoice, transfer |

**Words banned in every language:** bestseller · most popular · most chosen · premium · basic ·
tier 1 · **light visit** · **heavy visit** · **preventive visit** · monthly · limited offer ·
hurry · only · unique · trusted by · years of experience · guaranteed satisfaction.

Three of those are new since the 26.08 decision and matter most, because the live site prints all
three today: **every visit is a full visit**, there is no light one and no preventive one, and
**Maximum is 6 visits and is never described as monthly.** The words must not survive in a database
column, an admin label or a report template either — a distinction that exists in the schema will
eventually surface in the interface. Internally the operations team keeps two visit profiles (a
first deep visit and the maintaining visits that follow); **that is a checklist, not a product**,
and the client-facing promise is one sentence: every visit returns the plot to the same condition.

---

## 11. What makes this specific to a company that photographs graves for families abroad

Stated plainly, because the brief asks and because a generic answer would be the failure mode.

- **The year rail** exists because the thing a person buying this actually wants to know is not "4"
  but "how often will someone be standing there". Nothing else on this site is a calendar, and
  since 26.08 made every visit identical, Optimal's four marks land one per season — the sentence
  the product sells on, drawn rather than asserted.
- **The report at section 2**, before price and before explanation, because the buyer cannot go and
  look, and the entire product is the substitute for going and looking.
- **The deceased's name off by default**, and an OG preview with no photograph, because the link is
  forwarded into a family group chat and lands on a screen we do not control.
- **WhatsApp as a first-class delivery channel** for the Family Circle invitation, because the
  invitee is 70 and does not open email, and because the diaspora's default is not our default.
- **Business hours with the UTC offset attached to every promise**, because half the audience reads
  them at 23:40 in Glendale.
- **`Starting small costs you nothing.`** — the credit block headed by its arithmetic rather than by
  the word "discount", because the register forbids urgency and because the arithmetic happens to
  be more persuasive than any offer we could construct: every route into the first year costs the
  same 160,000 ֏.
- **A published formula rather than a quote on request**, because the awkward cases here are a
  40 m² plot with five monuments and a family arguing about it across three time zones, and the
  worst thing that can happen to that family is a number that arrives by phone and cannot be
  checked.
- **The weather window stated as a contract term with a remedy attached**, because the alternative
  is a client in Lyon discovering in February that winter is negotiable.
- **The honesty panel at body size**, because a pre-launch company that says so is more credible
  than one that manufactures 150,000 customers — which is precisely what this site does today.
- **`Not sure` as a first-class answer** to "cemetery or city", because a person who has not been
  home in nine years genuinely does not know, and a form that punishes that loses the lead we most
  want.

---

## 12. Open items for the design lead

1. **The flowers / candle option has no price in any source.** It is an explicit owner instruction
   of 26.08 §7.5 that it be visible on the tariffs page rather than buried in the portal. The slot
   is designed (§3.8, content slot 71); the number is missing. **Blocking for the pricing page.**
2. **Guarantee #2 needs a figure.** 26.08 §7.2 requires the liability limit stated as a number — a
   policy reference and an amount — not the word "insurance". The archive gives a 500,000 ֏ reserve
   plus insurance; the lawyer supplies the publishable form.
3. **`Special` in a row of published prices.** I have ruled it a full-width card below the row
   rather than a fifth column (§3.6). If the owner wants it in the row, the row needs a fourth
   column with no price in it, and I would argue against that.
4. **Deleting public `/register/`** (§6.1) is the ruling most likely to be challenged by a
   stakeholder, since the affordance exists on the live site today.
5. **The wordmark colour in the header** (§0.2 #5) — UI's call, but the header spec depends on it.
6. **֏ (U+058F) coverage in Ghea Mariam and Montserrat Arm** is still unverified, and
   `LEAD-NOTES.md` records that Ghea Mariam is not available in Figma at all. The currency glyph
   stays in its own element with its own stack regardless, so a missing glyph degrades one
   character rather than breaking a price.
7. **Two 26.08 items I have deliberately not designed**, because they are backlog rather than
   decisions: the "+2 visits on memorial dates (Merelots, the anniversary)" idea, which the owner
   neither accepted nor rejected; and payment in instalments, which the owner rejected and which
   the client council recorded as the single remaining friction for the older local buyer. If
   either is reopened, the tariff row changes shape and this section is the place it changes.
8. **`CLAUDE.md` and `PROJECT-MEMORY-FULL.md` §3 still carry the superseded line-up** — 26.08 §8
   says so explicitly and they have not been rewritten. Everyone reading this proposal against
   `CLAUDE.md` will find a contradiction; `CLAUDE.md` is the one that is wrong. It should be fixed
   at source before the next round, or it will produce this same error again.
