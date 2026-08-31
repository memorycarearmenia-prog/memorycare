# PROPOSAL — Product / UX architecture

Rebrand 2026-09-01. Slot: product & UX. Owns structure, flow, conversion.

Governing sources, in precedence order: `docs/rebrand-2026-09-01/BRIEF.md` →
`docs/design-package-v1/LEAD-REVIEW.md` (where not superseded by the 31.08 facts) →
`docs/design-package-v1/FINAL-UX.md` (prior art) → the 31.08 audit
(`FINDINGS.md`, `INVENTORY.md`, `GAPS.md`).

---

## 0. Preface — what I read, what I could not read, and what I ruled on

### 0.1 The screenshots

**The directory the task names, `docs/site-audit-2026-08-31/screens/`, does not exist**, and
neither does `docs/rebrand-2026-09-01/` — the brief is actually filed at
`docs/site-audit-2026-08-31/docs/rebrand-2026-09-01/BRIEF.md`. `INVENTORY.md` says 242 files
were captured into `screens/`; they were not carried into this working tree. Stating that
plainly rather than pretending to have seen them.

What I did look at, and what it gave me:

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

That is enough to rule on every route in scope. Where a ruling depends on something only a
missing screenshot could settle, I say so.

### 0.2 Conflicts I found between the sources, and how I ruled

The 31.08 brief supersedes the 29.08 design package on every point of fact. Five conflicts had to
be resolved before any structure could be drawn.

| # | Conflict | Ruling |
|---|---|---|
| 1 | BRIEF §Pricing: "Inspection is a one-off … visually apart from **the three subscriptions**". The same table makes Express **one heavy visit, credited toward a subscription** — i.e. not a subscription. | Express is a one-off and the interface must not call it annual. I satisfy the brief's *structural* instruction — Inspection set apart from a row of three — without the false label. See §3.1. |
| 2 | BRIEF: repeat Express in the same calendar year = 40,000 ֏. FINDINGS #3: that rule was "ОТМЕНЕНО" on 25.08.2026. FINAL-UX §1: "Express is 65,000 every time; there is no reduced repeat price." | Build to the BRIEF (later, and declared verified). **Flagged for the owner as the one pricing fact three sources disagree on.** |
| 3 | FINAL-UX/DECISIONS-2: one credit window, 60 days. BRIEF: Inspection 30 days, Express 60 days. | Two windows, per product, per the BRIEF. This is not the stale 30-day figure LEAD-REVIEW §4 struck out — that was a single global window; this is product-specific. |
| 4 | FINAL-UX's whole commercial apparatus — the fifth product **Special**, the m²/monument **surcharges**, the **calculator**, the **95,000 ֏ first-year line** — against BRIEF + CLAUDE.md: "**Flat single price for every client, no plot-size surcharge**", four products, locked. | **All four are deleted.** See §3.6. This is the largest single override in this document and it removes roughly a third of FINAL-UX. |
| 5 | The 31.08 brandbook makes the wordmark single-colour **Olive**; Olive on Nude measures 3.12 and never carries text. FINAL-UX's header wordmark is two-tone. | Header live text is single-colour **Dark Olive** on light, **Nude** on dark. The drawn Olive wordmark is used only at display size on Dark Olive (4.14, clears AA-large). UI's territory — flagged, not decided here. |

### 0.3 Where I override FINAL-UX, in one list

1. The pricing model (§0.2 #4) — Special, surcharges, calculator and the 95,000 line are gone.
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

**5 · Tariffs** — Nude. Full spec in §3.

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

### 3.1 The structural problem, and the ruling

Four products. Inspection (20,000) is one light visit with no cleaning. Express (60,000) is one
heavy visit. Optimal (180,000) is 6 visits a year. Maximum (240,000) is 9 visits a year. The brief
asks for Inspection "visually apart from the three subscriptions" — but Express is not a
subscription, and calling it one on a card would be a false statement about what the customer is
buying.

**Ruling: a ladder, not two bands.**

```
        ┌──────────────────────────────────────────────────────────────┐
   0    │  ԶՆՆՈՒՄ / Inspection · 20,000 ֏ AMD                          │  ← a rail, not a card
        │  One visit · no cleaning · a priced list of what it needs    │     full width, Ivory
        └──────────────────────────────────────────────────────────────┘     on Nude, hairline

   ┌────────────────┐  ┌────────────────────────┐  ┌────────────────┐
   │  Express       │  │ ★ Our recommendation   │  │  Maximum       │  ← three cards, equal
   │  1 visit       │  │  Optimal               │  │  9 visits/yr   │     height, 2px Deep
   │  60,000        │  │  6 visits/yr           │  │  240,000       │     Olive border on
   │  one-off       │  │  180,000 · per year    │  │  per year      │     Optimal only
   └────────────────┘  └────────────────────────┘  └────────────────┘
        ┌──────────────────────────────────────────────────────────────┐
        │  How money you have already paid is carried forward          │  ← always visible
        └──────────────────────────────────────────────────────────────┘
```

This satisfies the brief literally — Inspection is set apart from a row of three — without
labelling Express annual. The row is a **commitment ladder**: 1 visit → 6 → 9. The
one-off/subscription distinction is carried by a chip on each card (`One-off` / `Per year`) and by
the unit line under each price, which is where a buyer actually reads it.

Inspection is a rail rather than a card because a card in a row invites comparison on the same
axis, and Inspection is not on that axis: it buys **information**, not care. Its job is to be the
lowest-risk first step for someone who has not seen the plot in nine years, and — operationally —
to lock the plot's GPS point for the field team. It gets the top of the section because it is the
easiest yes on the page.

### 3.2 The comparison problem: 1 vs 6 vs 9 without a spreadsheet

The count is meaningless as a number. `6` and `9` are abstractions; what the buyer wants to know
is *how often will somebody actually be there*, and *what is the difference between the visits*.

**The year rail.** Every card carries the same 12-cell strip — one cell per month of the
subscription year — with the visits marked on it. Same component, same width, same position in
every card, so the three strips stack into a single readable comparison the moment the eye moves
across the row.

| | Marks on the rail |
|---|---|
| Inspection (on its rail) | one Deep Olive tick in cell 1, then nothing |
| Express | one filled square in cell 1, then nothing |
| Optimal | **2 filled + 4 open** = 6 marks, distributed across the year |
| Maximum | **3 filled + 6 open** = 9 marks, distributed across the year |

- **Filled Olive square 12×12** = a full clean. **Open 12×12 ring, 2px Olive** = a check and tidy.
- The legend appears **once per section, under the row**, never repeated inside each card.
- Cells are a 1px Dark-Olive-at-20% hairline grid; no month names at 360 (they will not fit
  legibly), season labels only — four groups of three.
- Olive on Nude measures **3.12**, which clears WCAG 1.4.11's 3:1 floor for non-text graphics with
  almost no margin, so each mark additionally carries a 1px **Deep Olive** outline (5.49). Colour
  is never the only differentiator: filled vs ring carries the heavy/light distinction on its own.
- **The rail never animates and never fills on scroll.** Nothing on this site moves on its own.

This is the one place in the system where Olive earns a job. It carries no text and receives none;
it is a decorative fill, which is precisely its permitted role.

**The arithmetic line.** Under the price, in tabular figures:

| Product | Line |
|---|---|
| Express | `60,000 ֏ AMD · one visit` |
| Optimal | `180,000 ֏ AMD / year · 6 visits · 30,000 ֏ average per visit` |
| Maximum | `240,000 ֏ AMD / year · 9 visits · ≈26,700 ֏ average per visit` |

Shown as arithmetic, not as a saving, and labelled **average** because a full clean and a check
are not the same work. It is the single most persuasive honest number on the page: it says
plainly that one Express visit costs twice what an Optimal visit costs, and it says it without a
"save 50%" badge, which we cannot substantiate and would not write.

### 3.3 Card anatomy — fixed, top to bottom

1. **Badge reserve, 46px**, present in all three cards whether or not a badge is drawn. Without it
   the three card titles sit at different heights and the row reads as an accident
   (LEAD-REVIEW §8).
2. Badge — **Optimal only**: `Our recommendation`, Deep Olive fill, Ivory label, 14px uppercase,
   radius 2. **Never "most chosen", "bestseller", "most popular", "premium" or "basic"**, in any
   language. In Armenian: `առաջատար`.
3. Product name, display face. **One script per locale** — the English card says `Optimal` and
   carries no Armenian; the Armenian card says `Օպտիմալ խնամք` and carries no Latin.
4. Unit chip, 14px uppercase: `ONE-OFF` / `PER YEAR`.
5. **The year rail** (§3.2).
6. Visit count — the largest element after the price. `6` + `visits a year`.
7. Composition line: `2 full cleans · 4 checks and tidying`.
8. Price. Tabular figures. **The `֏` glyph is emitted in its own element with its own font
   stack**, and the letters `AMD` always follow, per the bank requirement and FINDINGS #21.
9. The arithmetic line (§3.2).
10. Three to four feature lines, identical slot count in every card so the rows align.
11. The credit line, one sentence, product-specific (§3.4).
12. A growing spacer.
13. CTA at the foot. **Optimal's is the only primary button in the row**; Express and Maximum are
    Deep Olive hairline secondaries. Three consistent signals mark the recommendation — border,
    badge, button weight — and none of them costs the button its language.

Cards in a row are **equal height, always**; the button is pushed to the foot by the spacer, not by
hand-tuned padding, so the alignment survives a translation into Armenian (LEAD-REVIEW §8).

### 3.4 The credit rules, made readable

Three rules, two windows, one repeat price. These are the most confusable facts on the site and
they must never live in a tooltip, an asterisk or a footnote. They get a **block of their own,
directly beneath the row, always expanded**, headed `How money you have already paid is carried
forward`, containing three worked lines of arithmetic and four bullets.

```
Inspection → any package, within 30 days     180,000 − 20,000 = 160,000 ֏ AMD in year one
Express    → any package, within 60 days     180,000 − 60,000 = 120,000 ֏ AMD in year one
Express again, same calendar year, not converted             40,000 ֏ AMD instead of 60,000
```

Then, as bullets:
- One credit for each plot, once.
- One amount only. If both were paid, the larger of the two.
- It applies at the moment the subscription is signed, and never between one-off services.
- After year one, the package is at its full annual price.

Each card also carries its own one-line version at slot 11, so a reader who never reaches the block
still gets the rule at the moment of decision: `Credited toward any package signed within 30 days.`
/ `…within 60 days.`

The 30-day and 60-day windows are **counted from the date the one-off was paid**, and the portal
shows the remaining days as a plain date (`Credit available until 14 October 2026`), never a
countdown timer. A timer on a memorial-care purchase is a pressure device and the brand forbids it.

### 3.5 Above the fold, and stacking order at 360

At 360 the section stacks: Inspection rail → **Optimal first**, then Express, then Maximum. On a
phone there is no centre, and first beats middle. That inverts the desktop left-to-right order,
which is correct: the desktop row reads as a ladder (cheap → expensive), the mobile stack reads as
a recommendation with two alternatives.

### 3.6 What is deleted from FINAL-UX's pricing apparatus, and why

- **Special (a fifth product, priced after an Inspection)** — not in the locked table. Deleted.
- **The m² and per-monument surcharges** — CLAUDE.md and the brief both say flat single price, no
  plot-size surcharge, no local/diaspora difference. Deleted.
- **The calculator** — it existed only to compute the surcharges. With a flat price there is
  nothing to calculate, and a calculator that always returns the list price is a control that
  teaches the visitor the site is decorative. Deleted, along with `#calculator`, its two sliders,
  its sticky result panel, and the `calc_config` hidden field on the consultation form.
- **The 95,000 ֏ first-year line** — derived from the old 160,000/65,000 pair. Replaced by the
  160,000 and 120,000 lines above.

This removes an entire page of specification and roughly a third of the interactive surface of the
old design package. If the owner reinstates surcharges, the calculator comes back with them and
not before.

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
| — | hidden | — | — | `utm_*`, `page_path`, `locale`, `referrer`, `product` when arriving from a tariff card |

**Three visible fields, one disclosure, one checkbox.**

### 4.3 What we deliberately do not ask

Preferred contact time (guessed wrong more often than right, and answered better in the first ten
seconds of the call). Budget. Which package (asking it converts a conversation into a commitment
and this form's entire premise is that the commitment comes after the conversation). Plot size or
monument count (there are no surcharges — asking implies there are). The name of the deceased
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
  lead for manual review.** A lost lead costs 180,000 ֏; a malformed number costs Hayk one minute.

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
  decided to spend 180,000 ֏ and hit a 500 must not be left with nothing to do.
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
4. An echo of what they told us — the contact detail and the cemetery — so a typo is caught now
   rather than after a missed call.
5. Two onward actions, both non-committal: `See a full report` and `How it works`.
6. Only then, low in the page: `How did you hear about us?` — one optional question.

**Nothing on this page asks for money, an account or a password.**

---

## 5. Secondary flow: choosing a package and paying

### 5.1 Where it starts and what it is

Every tariff CTA (`Choose Optimal`) goes to **`/pay/?product=optimal`**. `/pay/` presents two paths
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
utm, credit_reference}` — to the platform, followed by a redirect. The marketing site receives back
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

Above the fold at 360: items 1, 2 and the top of 3. **If the client must scroll to learn when the
first visit is, this screen has failed.**

Once reports exist the screen becomes the plot dashboard (FINAL-UX §7.2), unchanged.

### 6.5 Add-package — `/portal/orders/new/`

Today `/account/packages/add/1/` re-asks name, phone and email beside a single green card
(`spot-1440.png`) — it is a registration form wearing a package. Replaced by an **authenticated
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
9. **The register of the whole thing.** No condolence copy, no guessing at why someone is buying,
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
| 43 | Inspection rail: name / one-line description / CTA | 22 / **90 ch hard** / 20 ch | |
| 44 | `One-off · not a subscription` chip | **26 ch, hard** | 14px uppercase; longest in RU |
| 45 | Product names ×4 | **22 ch, hard** | One script per locale |
| 46 | Unit chips: `ONE-OFF` / `PER YEAR` | **12 ch, hard** | 14px uppercase |
| 47 | Visit-count caption ×3 | 18 ch, hard | `visits a year` |
| 48 | Composition line ×3 | **56 ch, hard** | `2 full cleans · 4 checks and tidying` |
| 49 | Visit-type names ×2 | **16 ch each, hard** | The words that replace "heavy"/"light". Never "light" as a quality |
| 50 | Year-rail legend | 44 ch | Two items, once per section |
| 51 | Season labels ×4 | 10 ch each, hard | |
| 52 | Average-per-visit line ×2 | 40 ch, hard | Must contain the word `average` |
| 53 | Feature lines, 4 per card × 3 cards | **54 ch each, hard** | Same slot count in every card |
| 54 | Per-card credit line ×3 | **60 ch, hard** | |
| 55 | Card CTA labels ×3 | **20 ch, hard** | |
| 56 | `Our recommendation` badge | **22 ch, hard** | 14px uppercase. HY: `առաջատար` |
| 57 | Credit block heading | 52 ch | |
| 58 | Credit worked lines ×3 | 70 ch each | Arithmetic, shown as arithmetic |
| 59 | Credit bullets ×4 | 80 ch each | |
| 60 | Guarantee names ×3 | 30 ch each | |
| 61 | Guarantee remedies ×3 | 120 ch each | Each contains a number |
| 62 | Payment-reality line | 130 ch | Card payment, no date promised |
| 63 | Pricing FAQ ×5 (Q + A) | 70 / 300 ch | Includes the no-diaspora-premium answer |

### How it works · Sample report · Family Circle · About · Contacts

| # | Slot | Budget | Notes |
|---|---|---|---|
| 64 | How it works: H1 / standfirst | 40 / 100 ch | |
| 65 | Timeline steps ×4 (number label, heading, body) | 14 / 30 / 220 ch | |
| 66 | `What a full visit includes` ×6–8 | 60 ch each | |
| 67 | `What we do not do` ×4 | 70 ch each | Links to `/legal/limitations/` |
| 68 | Weather-and-access paragraph | **380 ch, hard** | Contains the added-to-spring rule |
| 69 | First-visit paragraph | 220 ch | Never described as a survey |
| 70 | Sample report: H1 / one-line header | 40 / 90 ch | |
| 71 | Report block labels ×6 | **22 ch each, hard** | Confirmation, GPS, On arrival, After the work, Crew note, Next visit |
| 72 | Report annotations ×4 | 130 ch each | |
| 73 | Link-preview explainer block | 200 ch | Demonstrates the OG rule and answers the privacy question |
| 74 | Family Circle: H1 / definition | 40 / **120 ch hard** | |
| 75 | Family Circle steps ×3 | 90 ch each | |
| 76 | Role names ×4 | **20 ch, hard** | Owner / Family manager / Family member / Guest |
| 77 | Role can/cannot lines, 3 + 2 per role | 56 ch each, hard | Must fit a 360 card |
| 78 | The Yerevan-relative paragraph | 200 ch | |
| 79 | Privacy note | 260 ch | Removal is immediate; links can be revoked |
| 80 | About: two opening paragraphs | 400 ch each | |
| 81 | About: why-it-exists paragraph | 300 ch | |
| 82 | About: method items ×3 | 120 ch each | |
| 83 | Contacts: hours block | 120 ch | UTC offset spelled out |
| 84 | Contacts: map placeholder label | 60 ch | Visibly a placeholder |

### Forms, states and system messages

| # | Slot | Budget | Notes |
|---|---|---|---|
| 85 | Consultation heading / support line | 44 / 90 ch | |
| 86 | Field labels ×5 | **24 ch, hard** | Real `<label>`s, not placeholders |
| 87 | Field helper texts ×3 | 70 ch each | |
| 88 | Note-disclosure prompt | 140 ch | `For example: the best hours to call you…` |
| 89 | Consent line | **110 ch, hard** | One line with a link. Not a wall of text |
| 90 | Error messages ×9 | **70 ch each, hard** | One per rule in §4.2, plus the two phone variants |
| 91 | Error summary heading | 60 ch | `role="alert"` |
| 92 | Submit label / sending label | 22 / 14 ch, hard | |
| 93 | Success: heading, promise echo, who-will-call, next actions ×2 | 40 / (16–18) / 110 / 24 ch | |
| 94 | Server-failure message + retry label | 130 / 20 ch | Must include the manual fallback |
| 95 | `How did you hear about us?` + 6 options | 40 / 24 ch | Thank-you page only |
| 96 | Country-selector search placeholder | 40 ch | Searchable in three scripts |
| 97 | WhatsApp checkbox label | 44 ch | |
| 98 | Portal first-run: greeting, status card ×4 lines, rail labels ×4, next-steps ×3, actions ×2, support row | 24 / 40 / 22 / 90 / 24 / 50 ch | §6.4 |
| 99 | Invite flow: heading, role-card titles ×3, role consequence lines ×3, delivery labels ×2, confirmation | 40 / 20 / **70 ch hard** / 20 / 180 ch | §7.2 |
| 100 | Invitation-received page: heading, role bullets ×3, accept label | 80 / 60 / 20 ch | |
| 101 | Guest report: header line, `The visit took place`, feedback labels ×3 | 60 / 30 / 24 ch | No price, no upsell |
| 102 | Empty states ×6 | 90 ch each | Never the word "empty"; always names the next event |
| 103 | 404: heading, line, five link labels, phone line | 30 / 90 / 22 / 40 ch | |
| 104 | 500: heading + line | 30 / **90 ch hard** | `Something on our side is not working. Your data is safe.` |
| 105 | Bad-news states ×3 | 180 ch each | Visit rescheduled (the new date must be present), crew could not reach the plot, guarantee re-visit requested |
| 106 | Cancellation flow: heading, the arithmetic line, confirm/cancel labels | 40 / 90 / 20 ch | Arithmetic shown before confirmation |
| 107 | Transactional email subjects ×7 + preheaders | **60 / 90 ch, hard** | Welcome, report ready, invitation, reminder, renewal offer, invoice, transfer |

**Words banned in every language:** bestseller · most popular · most chosen · premium · basic ·
tier 1 · monthly · light (as a quality) · limited offer · hurry · only · unique · trusted by ·
years of experience · guaranteed satisfaction. **`Maximum` is 9 visits and is never described as
monthly.**

---

## 11. What makes this specific to a company that photographs graves for families abroad

Stated plainly, because the brief asks and because a generic answer would be the failure mode.

- **The year rail** exists because the thing a person buying this actually wants to know is not "6"
  but "how often will someone be standing there". Nothing else on this site is a calendar.
- **The report at section 2**, before price and before explanation, because the buyer cannot go and
  look, and the entire product is the substitute for going and looking.
- **The deceased's name off by default**, and an OG preview with no photograph, because the link is
  forwarded into a family group chat and lands on a screen we do not control.
- **WhatsApp as a first-class delivery channel** for the Family Circle invitation, because the
  invitee is 70 and does not open email, and because the diaspora's default is not our default.
- **Business hours with the UTC offset attached to every promise**, because half the audience reads
  them at 23:40 in Glendale.
- **The average-per-visit arithmetic** instead of a discount badge, because the register forbids
  urgency and the arithmetic is more persuasive anyway.
- **The honesty panel at body size**, because a pre-launch company that says so is more credible
  than one that manufactures 150,000 customers — which is precisely what this site does today.
- **`Not sure` as a first-class answer** to "cemetery or city", because a person who has not been
  home in nine years genuinely does not know, and a form that punishes that loses the lead we most
  want.

---

## 12. Open items for the design lead

1. **The repeat-Express price, 40,000 ֏.** BRIEF says it is live; FINDINGS #3 says it was cancelled
   25.08.2026; FINAL-UX says no reduced repeat price exists. Three sources, three answers. I have
   built to the BRIEF. **The owner must confirm before any price ships.**
2. **`Express` inside "the three subscriptions".** I have resolved it as a ladder (§3.1). If the
   owner intends Express to be sold as an annual product, the composition line has to change, not
   the layout.
3. **The wordmark colour in the header** (§0.2 #5) — UI's call, but the header spec depends on it.
4. **Deleting `/register/`** (§6.1) is the ruling most likely to be challenged by a stakeholder.
5. **֏ (U+058F) coverage in Ghea Mariam and Montserrat Arm** is still unverified. The currency
   glyph stays in its own element with its own stack regardless, so a missing glyph degrades one
   character rather than breaking a price.
6. The brief and this proposal are filed in two different directories
   (`docs/site-audit-2026-08-31/docs/rebrand-2026-09-01/` vs `docs/rebrand-2026-09-01/`). Worth
   reconciling before the five proposals are converged.
