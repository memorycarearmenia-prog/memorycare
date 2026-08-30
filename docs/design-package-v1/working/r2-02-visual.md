# r2 — 02 Visual Design Lead: review and resolutions

Round 2. English. 30.08.2026.
Input: `DECISIONS.md` (binding), `BRIEF.md`, and proposals 01, 02 (mine), 03, 04, 05.

This memo resolves. It does not restate my proposal. Where my round-1 document is
wrong I say so and the correction stands as the resolution.

Ranking rule I applied throughout: **owner decisions > brief > measured fact
(contrast, glyph coverage, fold arithmetic) > the strongest argument > seniority.**
Seniority never won anything below.

---

## 1. Conflicts and resolutions

### 1.1 The dark hero — the one I got wrong

**The disagreement.** I put the hero on an Anthracite full-bleed band with an
Ivory report sheet on it (02 §A.2, section rhythm 1/5/10). 04 requires the report
card with GPS *and* the primary CTA above the fold at 375px, and forbids the logo
as hero art. 01 puts the hero on Nude with a transparent header. The brief asks
for "light premium minimalism… explicitly NOT funeral cliché, no dominant black".
05 makes `.mc-on-dark` a section scope and forbids any OS-driven repaint.

**What breaks each way.** A dark hero costs fold height: my own spec gives dark
bands more padding (80/80 mobile vs 72/72) because dark grounds close in, and it
forces the header to switch logo colour on scroll — a flash on a slow diaspora
connection, plus a second header variant to maintain. It also spends the page's
scarcest asset (darkness) on the first screen, where the brief's tone rule is
strictest. A light hero risks the report sheet not separating from the ground —
but Ivory-on-Nude with a hairline is exactly the "paper on stone" device I argued
for, and it is *more* on-concept than putting the paper under a lamp.

**Resolution — light hero. I was wrong.** Hero ground is **Nude**. The report
preview is an **Ivory sheet with a 1px `alpha.anthracite.12` hairline**, no
shadow. The page keeps **two** Anthracite bands, not three: **Family Circle** and
the **closing CTA band that runs into the footer**. The consultation form does
*not* sit on the dark band (see 1.6 — the error red has no legible value on
Anthracite, so a form there cannot show a validation error).

**The fold arithmetic, so this is checkable rather than a matter of taste.** QA
floor is 360×640 (see 1.9), header 56, usable content ≈ 500px:

| Element | Height |
|---|---|
| Overline 13/18 | 18 |
| gap | 12 |
| **H1, 32/38, hard max 2 lines** | 76 |
| gap | 16 |
| Standfirst 16/26, 3 lines | 78 |
| gap | 20 |
| Report preview, cropped by the fold on purpose | 180 |
| gap | 16 |
| Primary CTA, 48 | 48 |
| **Total** | **464** — ~36px spare |

A 3-line H1 costs 38px and pushes the CTA under the fold. Therefore:
**hero H1 hard maximum is 48 characters in English**, ~24 per line at 32px. This
kills 03's hero H1 (58 chars, §A.2 Block 1), my own 52-char budget, 01's 56 and
05's `hero.h1: 62`. One number, everywhere: **48 / hy 58 / ru 55.**

Same arithmetic kills 03's hero standfirst (228 characters — eight lines at 360,
208px, the fold is gone). **Standfirst budget: 105 characters English.** Content
must rewrite; the sub currently carries three ideas and needs one.

The logo-as-hero-art prohibition is unanimous and is already in 05 §E5's forbidden
list. Closed.

### 1.2 Radii and shadows

**The disagreement.** I specified radius 2px everywhere and **zero shadows in the
entire system**. 05 specifies `radius-md` 10 on buttons, `radius-lg` 14 on cards,
an `elevation-1…4` ladder, `elevation-1` on every card and a `translateY(-2px)`
hover lift. 01 writes "shadows read as SaaS" and then gives the header "a hairline
shadow after 24px of scroll".

**What breaks.** 10/14px radii plus a shadow on every card is the wellness-template
tell the brief names by implication (tending/headspace are the *references*, not
the target). But absolute zero shadow is dogma: a drawer, a lightbox and a bottom
sheet genuinely need to detach from the page, and a scrim alone does not do it for
an Ivory sheet sliding over a Nude page.

**Resolution — I concede half.**
- **Radius scale is 0 · 4 · 8 · full.** `0` for bands, photographs, the report
  sheet, dividers, the plot diagram. **`4`** for buttons, inputs, cards, tariff
  cards, badges, chips. `8` for modals, drawers and bottom sheets only. `full` for
  the slider thumb and Family Circle initial discs only. 2px was too austere at a
  48px button on a phone; 10/14 is a consumer app. 05 deletes `radius-sm/md/lg/xl/2xl`.
- **Shadows: exactly one token, `elevation-overlay`** = `0 16px 40px rgba(51,55,60,0.16)`,
  usable only by modal, drawer, bottom sheet, lightbox and toast. `elevation-1/2/3`
  and every card shadow and hover lift are deleted. Card hover = border
  `alpha.anthracite.12` → `olive-500` plus a title underline. No transform on any
  card or button.
- 01's header shadow is deleted; the header gets a 1px `alpha.anthracite.12`
  bottom rule after 8px of scroll (01 said "1px Olive at 20%", which is invisible
  on Nude — see 4.6).

### 1.3 Full-bleed Ivory bands

**The disagreement.** I used full-bleed Ivory for "document moments" (sample
report, calculator, legal pages). 05 states the rule as *"Ivory is never a page
background. Nude is never a card background"* and makes it lint-enforceable: any
full-bleed `<section>` is Nude.

**Resolution — 05 wins, I withdraw.** Full-bleed Ivory bands go. The report sheet
and the calculator panel are **Ivory objects on a Nude ground** — which is the
paper-on-stone idea stated more purely, and it survives an automated check. Nude
and Ivory differ by 1.1; a third near-identical light band buys perception nothing
and costs the system its only testable surface rule. My "no Ivory inside Ivory"
nesting rule becomes unnecessary and is deleted with it.

### 1.4 The tariff row — three positions, one truth

**The disagreement.**
- Me: Inspection as a ruled band above; row = **Express, Optimal, Maximum**;
  Special a ruled line below.
- 03 §C.3: two bands — one-offs (Inspection + Express) / annual (Optimal, Maximum,
  **Special as a third card**).
- 04 §A6: two bands, and **Special is not a card at all** — one line under the
  calculator.
- 05 §A4.7: three-card row Express/Optimal/Maximum, Inspection standalone above,
  **Special as a fifth card** in the row footer.
- 01 §A3.2: three subscription cards, then Inspection, then a Special band.

**What breaks.** Express is a one-off. Putting it in a row with two annual
subscriptions invites a client to compare 65,000 against 160,000 as though they
were the same kind of thing, which is a pricing misrepresentation before it is a
design problem. And a Special card — anywhere in a row — restores a five-way
comparison on a phone, which 04 correctly identifies as the failure mode of a
five-product page.

**Resolution — 04 and 03's band structure, with 04's Special.** I was wrong.

- **Band 1 — One-off services:** Inspection and Express, **two cards**, prices set
  at the same type size as the annual prices (never smaller — shrinking is what
  makes a thing read as cheap). Credit rule stated once beneath the band, four
  bullets, always visible, never a tooltip (03 §C.4 is right).
- **Band 2 — Annual subscriptions:** Optimal and Maximum, **two cards**. Nothing
  else in this band.
- **Special:** one ruled line beneath the calculator, with the Inspection route.
  Not a card, not a band, on any page.

Consequences to write into the specs: 05 deletes `TariffCard--standalone` and the
`Special` card variant; the grid is 2-up at `md`+ and 1-up below, never 3-up; my
"Inspection is a band, not a card" device is deleted (it made Inspection read as
lesser, which 04 forbids and is right to forbid); 01's home-page preview shows the
two annual cards plus a link, not three cards.

### 1.5 "Most chosen" — and a contrast error inside two proposals

**The disagreement.** Me: Optimal inverted onto Anthracite, 24px taller, badge in
Nude. 04: same width, more padding, **Olive band with Anthracite text**. 03: badge
above the product name, **Olive fill with Anthracite label** — and writes "which
passes". 05: **Deep Olive fill, Ivory label (6.01)**, 2px Deep Olive border, no
size change.

**The factual point.** Anthracite on Olive is **3.08**. Ivory on Olive is 3.42.
Nothing is legible on an Olive fill. 03's "which passes" is wrong, and 04's Olive
band with Anthracite text is the same error. 05 is the only one of us with it right.

**Resolution.** Optimal is marked by: **2px Deep Olive border** (Maximum keeps a
1px hairline) + **badge: Deep Olive fill, Ivory label, `MOST CHOSEN`, placed above
the product name** (03's placement is right; a badge over a price is not). **No
inversion, no height change, no Olive fill under any label anywhere in the
system.** I withdraw the inverted card: with only two cards in the band it reads
as a light/dark opposition rather than a hierarchy, and it collides with the
two-dark-bands budget. 01's word "ribbon" is retired — a ribbon is a corner flag.

### 1.6 GPS — I over-designed it

**The disagreement.** I forbade map tiles and pins outright and specified an
abstract plot diagram (bearing rose + Olive five-petal marker). 04 wants "a GPS
coordinate, a map pin, a date" in the hero. 01 wants a tap-to-reveal static map
crop in the report. 03 has a `Show on map` action.

**What breaks.** Three of five want a map, and their reason is better than mine:
the diaspora objection is *"were they at **my** plot"*, and an abstract diagram
cannot answer that. A map crop the client recognises can. Against that, an
external tile request on every report open is a third-party call from a page full
of grave photographs, and it is slow on the connection 04 describes.

**Resolution — split by surface.**
- **Marketing (hero, method block):** the **plot diagram**. Ours, abstract, no
  external request, fast, and it is a graphic device rather than a claim.
  Two uses on the home page.
- **Report screen:** coordinates in tabular type + a **`Show on map`** action that
  opens a **static map crop in a lightbox**, on demand. Never inline, never
  auto-loaded, never a live embed.
- **The marker is the Olive five-petal glyph in both. Never a red pin** — that is
  a delivery app, and after decision 1.10 red means one thing only in this product.

### 1.7 Report block order and photography

**The disagreement.** Four different orders were proposed (01 §A4.4, 03 §A.10.4,
05 §A4.9, mine §A.4). Points of real difference: where the crew note sits, whether
the first photograph is "before" or "after", and the aspect ratio.

**Resolution — one canonical order, binding on all four documents:**

1. **Masthead** — mark, "Visit report", plot identity, cemetery
2. **Confirmation block** — date · status · crew · arrival/departure · **GPS
   confirmation with the plot diagram at the foot of the block** (03 §C.6 is right
   that the first screen is otherwise a receipt; the diagram is what saves it)
3. **Work performed** — checklist
4. **Photographs** — group "On arrival", then group "After the work"
5. **Video**
6. **The crew's note**
7. **Recommended work with prices** — owner and manager only; absent server-side
   in every other view
8. **Documents** — PDF
9. **Actions** — share / re-visit
10. **Next visit** — not in the guest view

- **05's "first image = the plot AFTER the visit" is reversed.** The report is a
  record; leading with the after-shot is the advertising register the brief
  forbids. Chronological, labelled groups, one image per row on mobile.
- **Aspect ratio: 3:2, 1600×1067.** 05's number, not my 4:3. 4:3 was a print
  habit; 3:2 is the native ratio of the camera the crew will actually hold, and my
  own frame-identical before/after rule is far easier to hold in the field at
  native ratio. My separate 4:5 comparison crop is deleted — comparisons are two
  3:2 frames stacked.
- The crew note stays after the photographs (majority, and 01's reason for moving
  it up is better answered by item 2's plot diagram).

### 1.8 Header lock-up

**Resolution — 05 §E3/E4 wins outright and supersedes my §A.6 sizes.** It is the
only proposal built on measured bounding boxes (the wordmark file is 97% empty
space; the vertical lock-up reuses mark and wordmark at 1:1 with a 37.6-unit gap,
which is what makes the horizontal construction legitimate rather than a crop).
Adopt the constructed `lockup-horizontal-mono.svg` at 36px ≥768 / 32px 480–767,
and below 480px the mark plus **live text** "MemoryCare".

Two corrections that stand regardless of proposal:
- In the live-text header wordmark, "Care" is **Deep Olive**, never Olive. 01 §B6
  specifies Olive — at ~20px that is text at 3.42 and it fails.
- **The footer tagline is Nude, not Olive.** Olive on Anthracite is 3.08. **This
  is my own error** — 02 §A.6.4 says "Olive small caps in the footer" and it
  contradicts my own contrast table two pages earlier. 01 §A3.0 and §B5 carry the
  same error and add "16px+ where it functions as a graphic element", which does
  not rescue it: the large-text exemption starts at 24px regular, and 3.08 fails
  the 3:1 non-text floor too. Olive tagline is a **print and logo-lockup treatment
  only**. 05 §A4.13 already had this right.
- The tagline never appears in the header. Unanimous. Closed.

### 1.9 Design and QA width: 360, not 375

05 is right — the diaspora carries older Android and 360 is the real floor. **All
budgets, including 04's "above the fold at 375" and my character table, are
re-baselined to 360×640.** 375 remains the drawing canvas only after a 360 check
passes. This is what produced the 48-character H1 in 1.1.

Related settlements, one number each, because four documents give four:
**header 56 mobile / 72 desktop** (the fold is the scarcest resource; 05's 64/76
costs 8px of hero for nothing). **Mobile action bar 64 + safe-area inset.**
**Page bottom padding 88 wherever that bar can appear.**

### 1.10 Calculator behaviour

- **No count-up on the total.** 05 specifies a 220ms count-up; 01 animates on
  `pointerup`. Both are the slot machine, one of them delayed. The number changes
  instantly, tabular, with `aria-live="polite"` announcing on release. This is the
  one place my round-1 position survives intact and I am keeping it: a price that
  rolls is the wrong register for this purchase.
- **Show Optimal and Maximum simultaneously, plus a separate Express one-off row.**
  I proposed a toggle; 01 proposed a segmented tier selector. Both are wrong —
  04's Question-2 architecture is "one variable, two values", and a control that
  hides one of the two values defeats it. Drop my toggle and 01's selector.
- Sliders keep 01's URL state, reduced to `?area=&monuments=`, and 05's paired
  number input (unanimous, and correct).
- 03's four permanently-visible surcharge lines are ~186px at 360 and push the
  total under the fold. **Two annual surcharge lines stay permanently visible under
  the sliders; the Express surcharge line moves inside the Express row where it
  applies.** Nothing goes behind an info icon (03 §C.5 is right about that).

### 1.11 Two-audience blocks

01 §A3.1 block 2 is two side-by-side cards: *"You are far away"* / *"You have no
time"*. 03 §B.3 rule 3 forbids exactly this — "never imply the reader could have
gone themselves, in either direction", and "You are far away" is diaspora-only
copy addressed to one of two readers who are on the same page.

**Resolution — 03 wins.** One block, outcome first, both reasons in one line of
body text, neither ranked. 01's two-card version is deleted.

---

## 2. Contradictions with the owner decisions

These are compliance items, not opinions.

**2.1 — DECISIONS §2, one functional colour. Three documents contradict it,
including mine.**
- **Mine (02 §B.8):** I asked for **two** semantic colours. Withdrawn. One is
  enough and the owner is right; see §6 for the integration.
- **01 §A8:** *"No red. We have no red in the palette and we are not adding one."*
  Superseded. 01's error styling (Deep Olive border + icon) must be rewritten to
  the error red, and its destructive-confirmation guidance kept.
- **03 §C.9:** *"Never red… Deep Olive is our accent for everything, including
  things that went wrong."* Superseded, same rewrite.
- **05 has the opposite problem — too much.** It ships `danger` **and** `warning`
  **and** `success`: `badge warning`, `badge danger`, toast variants
  `success/info/warning/error`, an input `success` state, `report-card.status-ok`,
  and a `danger` **button** variant. DECISIONS §2 permits **one** value, for form
  validation and payment failure, with **no sibling success or warning tokens**.
  All six must be deleted. Success and warning are typographic — wording, glyph,
  rule weight. The `danger` button variant is the sharpest violation: an error is
  never an action, and a destructive action (cancel subscription) is a secondary
  button with an Anthracite label, per 01 §A4.8, which is the right call.
- **Token naming:** rename `danger.600` → **`--mc-color-feedback-error`** with
  `--mc-text-error`, `--mc-border-error`, `--mc-surface-error-subtle` and nothing
  else. The owner asked for a name that makes the restriction obvious; `danger`
  invites a `success` sibling the moment someone is under deadline.

**2.2 — DECISIONS §1, `MemoryCare LLC`.** 03 §D item 6 still asks which spelling
is registered. It is answered: `MemoryCare LLC`, one word, everywhere — footer,
offer, invoices, legal pages, bank package, meta. Close the open item. 05's
string denylist already fails the build on `Memory Care` — good, keep it.

**2.3 — DECISIONS §3, `160,000 − 65,000 = 95,000`.** Only 01 §A7 gives it a home
(the calculator). It also belongs on the **pricing page, under the one-off band**,
and it has no copy string in 03 and no display slot in 05's `products.json`. Add
both. Three constraints to enforce in the string, because they are easy to lose in
translation: it is **the mechanic, never a discount** — no "save", no
strike-through on 160,000, no "special offer"; **not in the hero**; **not as the
Express card's headline price** (Express is 65,000, full stop). And 01 §D5 calls
it *"a 40% first-year discount"* — that phrasing is forbidden by DECISIONS §3 and
must not survive into any copy, brief or ticket.

**2.4 — DECISIONS §4, 60-day credit window.** All five build to 60. 01 §D4 flags a
30-day conflict with the repo memory; it is settled at 60 and the item closes.

**2.5 — DECISIONS §5, the ֏ glyph. Nobody answered it, and there is a worse
version of the question that nobody asked.**
03 §C.11 flags that ֏ may be missing from Cabin and must be checked. Correct — but
03 also notes ֏ is not in Gloock, and then **both my type scale (`price`,
`price-xl` = Gloock) and 05's (`mc.type.price` = display face, with "֏ AMD"
baseline-aligned next to the amount) set a price containing ֏ in Gloock.** Gloock
is Latin/Latin-ext only. That string will render the numerals in Gloock and the ֏
in a fallback face, at display size, on the most scrutinised number on the site.
That is a visible defect and it does not need a network check to know.

Resolution, unconditional, so it is safe whichever way the Cabin check lands:
- The **numeral** may be Gloock. The **`֏ AMD`** sits on the following line in the
  text face. 05's baseline-aligned currency next to a Gloock numeral is deleted.
- Every currency glyph is wrapped: `<span class="mc-currency">֏</span>` with its
  own one-line fallback stack `"Cabin", "Noto Sans Armenian", "Noto Sans",
  system-ui`. Noto Sans Armenian carries U+058F with certainty, so the fallback is
  correct even if Cabin turns out to have it.
- The check still gets run before build; if Cabin lacks ֏, one line changes.

**2.6 — DECISIONS §4, placeholders labelled with ratio and crop.** Mine and 05's
placeholders name ratio, pixel size, subject and source. **01's photo slots are
marked only "September shoot"** with no ratio and no crop — bring them to the same
standard, it is a one-line fix per slot.

**2.7 — Outside DECISIONS but worth flagging upward:** the repo's `CLAUDE.md`
still carries the **old** product table (180,000 / 240,000 / 20,000 / 60,000, a
30-day credit, a 40,000 repeat Express, "2 heavy + 4 light"). `BRIEF.md` and
DECISIONS carry the current one (160,000 / 200,000 / 65,000, 60 days, every visit
a full visit). Nobody's proposal used the stale numbers — but the next session
will read `CLAUDE.md` first. Someone must reconcile that file.

---

## 3. Gaps — things none of the five of us covered

**3.1 The report PDF is named by three of us and specified by none.** 01 gives it
a download button, 05 lists it as Igor's backend concern, I mentioned Gloock's
24px floor "including PDF". Missing: page size (**A4** — the readers are in
Yerevan, LA and Lyon; pick one and say so), that a PDF forwarded by email carries
the same exposure as a shared link and therefore obeys the same no-prices rule for
anyone but the owner, and — the real hole — **whether a client who cancels keeps
their reports.** They paid for the record. If portal access ends, the PDFs are all
they have. That is a product decision with a legal edge and it is not in anyone's
document.

**3.2 There is no email design spec at all.** 03 wrote the email copy, 01 named
the activation email, 05 lists no email template. Emails cannot use CSS variables,
cannot rely on Gloock or Cabin (Outlook), and — the important one — **a report
notification email must never embed a photograph**: it will render in an inbox
preview pane at someone's work. Rule: transactional email is text-first, one
Anthracite header bar, system font stack, no photographs, a link to the report.

**3.3 My loading spinner violates the logo rules.** I specified a 14px five-petal
glyph rotating as the only permitted loop in the system. 05 §E5's forbidden list
includes **rotation of the mark**, and it is right — a spinning brand mark on a
page about a grave is a bad idea on tone as well as on brand governance.
Withdrawn. Loading is a 2px Deep Olive arc, no brand element. Also: 05's eleven
production SVGs contain no 6px petal bullet either, which my feature lists and the
plot-diagram marker both require. **Add a twelfth asset: `petal-bullet-mono.svg`,
single path, no weave, no hands.**

**3.4 Webfont loading behaviour for hy/ru is unspecified and breaks 05's own CLS
budget.** Gloock is Latin-only, so an Armenian or Russian H1 paints in a system
serif and reflows when `Noto Serif Armenian` / `Playfair Display` arrive.
`font-display: swap` plus a 0.05 CLS budget cannot both hold. Specify
`size-adjust` / `ascent-override` on the fallback declarations, or
`font-display: optional` for display type on hy/ru. 05's self-hosting decision
(Russia + the bank's dislike of third-party requests) is right and should be kept.

**3.5 Consent banner: nobody said whether one exists.** 04 wants analytics, 03
refuses a modal in the portal, 04 forbids a banner over the CTA. An EU-resident
diaspora visitor plus third-party analytics means a consent obligation. **My
recommendation: no third-party analytics at launch — self-hosted, cookieless
measurement, therefore no banner at all.** If the owner wants GA, the banner
becomes a designed component and it must never overlay the hero CTA.

**3.6 The September shoot has no operational artefact.** I specified
frame-identical before/after pairs; 04 calls the report photography the
highest-value shoot in the project. Nobody produced the thing that makes it
happen: a written **shot list per plot, a marked standing position, a fixed tripod
height and focal length**, and a naming convention matching the placeholder file
names in 05 `placeholders/`. The whole visual system depends on this input and it
is roughly two weeks away.

**3.7 No LCP budget in the acceptance checklist.** 01 alone names LCP < 2.5s on
4G; 05 has a CLS budget but no LCP. Both belong in 05 §D5, measured at 360 on a
throttled connection, in all three locales.

**3.8 Report page `<title>`.** Specify `Visit report — {date}` and nothing else.
The plot identity in a browser tab is visible over a shoulder and in any
screen-share.

---

## 4. Factually wrong — contrast, type, layout, spec collisions

Numbered so they can be ticked off.

**4.1** 03 §C.3: *"Olive fill with Anthracite label, which passes."* It does not —
**3.08**. Same error in 04 §B4 ("Olive top band with Anthracite text"). Fix per 1.5.

**4.2** 01 §A3.0 and §B5: footer/hero tagline in **Olive** on Anthracite = **3.08**;
"16px+ as a graphic element" does not rescue it (the large-text exemption begins at
24px regular). **And my own 02 §A.6.4 makes the identical error.** Tagline is Nude
in the footer.

**4.3** 01 §B6: header wordmark "Care" in **Olive** on Nude = **3.42** at ~20px.
Deep Olive.

**4.4** The error red on the dark band: **`#8C3A2E` on Anthracite `#33373C` is
1.57.** It fails text (4.5) and even the non-text floor (3:1) — the same trap as
Deep Olive's 1.75, and nobody caught it because nobody put a form on a dark band
except me. This is the concrete reason the consultation form moves off the closing
Anthracite band (1.1). On Anthracite an error is Nude text plus a 2px Nude
inline-start rule plus the word. Written into §6 below.

**4.5** 05's `mc.text.secondary` `#606161` on Nude is **4.87** — it passes, with an
8% margin. Restrict it to **≥15px**; at 13–14px that margin is a rendering
difference, not a design one. And 05's own type scale sets `caption` at 13px in
`--mc-text-secondary`, which is exactly the combination to forbid.

**4.6** 01 §A3.0: header divider "1px Olive at 20% opacity" — Olive at 20% over
Nude is a ~1.05 tonal step. It is invisible. Use `alpha.anthracite.12`.

**4.7** Type-size floor: three different answers (mine 15 with 11–13 for
micro-labels; 01 "nothing below 14"; 05 "minimum 16, nothing below 13 exists" —
while its own `caption` token is 13 and `overline` is 12). **My 11px `rail` and
12px `eyebrow` are indefensible** for a 40–60 reader on a 360px phone at night.
One ladder, four lines, binding:
- **16px** — body and **every input** (below 16 iOS zooms on focus)
- **15px** — the floor for any text that carries meaning in a sentence
- **14px** — sentence-case captions and helper text
- **13px** — uppercase tracked micro-labels only (`overline`, report metadata), at
  600 weight and 0.12em. Nothing in the product is smaller than 13px in any medium.

**4.8** 01 §B4 hierarchy: H3 = Cabin 600 20/24 against Body-L 18/19 at desktop is a
3px step — that is not a hierarchy, it is a rendering accident. Unify with 05:
`heading-3` = text face 600, **18 mobile / 20 desktop**; `body-lg` 17/18;
`body` 16/17.

**4.9** 04 §B2: secondary button "**1.5px** outline". The border scale is
0/1/2/3. 1px at rest, 2px when selected.

**4.10** 05 §A4.7: tariff card `min-height: 480`. With the row now two cards
(1.4), a hard 480 forces empty space into both. Height is `auto`, equalised by the
grid row, never by JS and never by a fixed minimum.

**4.11** Armenian will not survive `content-limits.json` as written. 05 correctly
sets `overline` to **sentence case in Armenian** (Armenian uppercase reads as
shouting) — nobody else has that rule and it should be adopted globally, including
for `MOST CHOSEN` and the one-off band label. But sentence-case Armenian grows the
badge ~25%, and `badge.label` overflow is set to **`ellipsis`**. An ellipsised
"Most chosen" is worse than no badge. Change `badge.label` overflow to **wrap to
two lines** for `hy`/`ru`, or supply a shorter Armenian string — the copywriter's
call, but not the ellipsis.

**4.12** 05 §A4.1 primary button hover: `translateY(-1px)` plus a shadow change.
With shadows gone (1.2) the translate lifts off nothing. Hover is a background
shift to `olive-800` only.

**4.13** 05 §A4.9 status icons: "postponed → badge `warning`", "access blocked →
badge `danger`". Both variants are deleted by DECISIONS §2 — **and "could not
access the plot" is not an error.** It is a report of a visit that happened, with
GPS proof that the crew was there (01 §A8.3(b) makes this point well). Treating it
as a red state contradicts the whole argument for showing the GPS trace on a
failed visit. Neutral treatment, typographic status word, no error colour.

**4.14** 03 §A.10.6: the OG description names the **cemetery**, and the OG image is
"the mark on a **Nude** ground". Two problems. The brief says the preview carries
mark, "Visit report" and the date only — the cemetery in a preview identifies the
family to everyone in a group chat, including people the owner did not choose to
tell. And a Nude 1200×630 renders as a near-blank card in a dark WhatsApp thread.
**OG ground is Anthracite; description carries no location, no plot label.**

**4.15** 05 §A4.9 `ReportCard` is specified as the visit-list row *and* the
sharable report header *and* is referenced as the marketing hero object. Three
different components with three different content sets and three different
permission profiles. Split them — see the naming table below.

**4.16** 01 §A3.0 mobile header centres the lock-up between two 44px targets. With
the constructed horizontal lock-up at 32px ≈ 136px wide, that is 44 + 136 + 44 =
224 inside 360 − 32 margins = 328. It fits, but only just, and it leaves no room
for the language switcher on mobile. Confirm the switcher lives in the drawer at
`base`, not the bar (05 puts it pinned at the drawer bottom — correct).

---

## 5. One name per element

Where two of us named the same thing differently, this column is the name. It goes
into `components/00-INDEX.md` and the string-file keys.

| Use this | Retire these |
|---|---|
| **Report sheet** — the full document (sample-report page, portal report screen) | "report card" (mine), "the report component" (01), `ReportCard` used for the document (05) |
| **Report preview** — the cropped Ivory object in the marketing hero | "report artefact" (01), "proof card" (04 §B1), "report card" (04 §C1), "report screen mock" (03) |
| **Visit row** — the item in the portal visit list | `ReportCard` used as a list row (05) |
| **Report masthead** — mark + "Visit report" + plot identity strip | "sheet header strip" (mine), "masthead" (01), "confirmation header" top lines (03), "status row + plot line" (05) |
| **Confirmation block** — date, status, crew, times, GPS | "verification rail" (mine), "confirmation" (01), "confirmation header" (03) |
| **GPS confirmation** — the umbrella; its parts are the **GPS chip** (label), the **plot diagram** (marketing graphic), the **map crop** (report lightbox) | "GPS verification element" (mine), "GPS chip" (01/05), "map pin" (04) |
| **Overline** — the small uppercase label | "eyebrow" (mine, 01, 03) |
| **Meta type** (`mc.type.meta`) — tabular label/value metadata | "rail" (mine) |
| **Leading badge** — string key `tariff.badge.leading`, English "Most chosen" | "lead label" (mine), "Most chosen ribbon" (01), "most chosen marker" (04) |
| **One-off services band** / **Annual subscriptions band** | "the row", "Band 1 / Band 2", "subscriptions band", "tier row" |
| **Mobile action bar** | "sticky action bar" (01), "sticky mobile CTA bar" (04/05), "sticky CTA bar" (mine) |
| **Founding note** — the "we started in 2026, we have no reviews" panel | "honesty block" (03) |
| **First-entry screen** — portal, post-payment, zero visits | "doubt screen" (03), "first entry" (01/04) |
| **Error** (never "danger") — `--mc-color-feedback-error` and its siblings | `danger.600`, `text.danger`, `badge danger`, `toast error`, `button danger` (05) |
| **Local contact** — the Yerevan relative with no account | unnamed in 03 and 05; 01's term is adopted |
| **Founders' block** | "Who we are" (01), "Trust / About" (04), "team block" |

---

## 6. The error red, made ours

DECISIONS §2 is accepted without reservation and my two-colour request is
withdrawn. What follows is how it stops looking like Bootstrap.

**The value.** `#8C3A2E` as the owner specified. It is not an alarm red — it is
terracotta, and it sits in the palette's own family: warm, earthed, low
saturation, the colour of the ground the rest of the brand is made of. Held
against Olive `#7C8654` it reads as its complement rather than as an intruder,
which is exactly why the owner chose it and why a stock `#DC3545` would have
broken the page.

**Token set — four names, no siblings, so the restriction is visible in the code:**

```
--mc-color-feedback-error : #8C3A2E    (Layer 1, the only non-brand hue in the system)
--mc-text-error           : var(--mc-color-feedback-error)
--mc-border-error         : var(--mc-color-feedback-error)
--mc-surface-error-subtle : rgba(140,58,46,0.10)   /* an alpha, never a new hex */
```

05's `danger.100 #F6E4E0` is deleted and replaced by the alpha above: one hex
enters the palette, not two. There is deliberately **no** `--mc-*-success` and no
`--mc-*-warning`. Anyone who needs one has misread a state.

**Measured contrast, so nobody has to guess:**

| Pair | Ratio | Verdict |
|---|---|---|
| Error on Nude `#EFE5D5` | **6.11** | passes AA for text at any size |
| Error on Ivory `#F3F0E9` | **6.69** | passes |
| Ivory on Error (solid fill) | **6.69** | passes — but see the prohibition below |
| White on Error | 7.62 | passes |
| Error on `surface-error-subtle` over Nude | ≈5.6 | passes |
| **Error on Anthracite `#33373C`** | **1.57** | **never. Fails text and the 3:1 non-text floor.** |

**Where it may appear — the complete list. Three places.**

1. **Form validation.** A 2px inline border on the field (inset, so the field does
   not change height), a 16px error glyph, and the message beneath in
   `--mc-text-error` at 14px. The required-field marker in the label is the same
   colour. Colour is never the only signal: glyph + sentence carry it, per 01's
   note about colour-deficient readers in a male 40–60 audience.
2. **Payment failure.** An inline panel on `--mc-surface-error-subtle` with a 2px
   `--mc-border-error` inline-start rule and the heading in
   `--mc-text-error`. Not a modal, not a toast — 05 §A4.15 is right that a failed
   payment is a screen, not something that auto-dismisses. The owner's reasoning
   is exact: a missed error here is an unfinished payment.
3. **The error message in a form's failure state after submit** — the same
   component as (1), at the top of the form, with `role="alert"`.

**Where it may never appear — and this list matters more than the first.**

- **Never on an Anthracite ground.** 1.57. This is why the consultation form does
  not sit on the closing dark band. If a validation error must ever surface on
  dark, it is Nude text plus a 2px Nude inline-start rule plus the word "error"
  spelled out — no colour at all.
- **Never on the report screen, the guest view, or the report PDF.** A red mark
  beside a photograph of a grave is the single worst thing this system could do.
  03 §C.9's instinct was right even though its conclusion was superseded.
- **Never as a button fill.** 05's `danger` button variant is deleted. Cancelling
  a subscription is a calm secondary button with an Anthracite label (01 §A4.8).
- **Never as a status badge for "could not access the plot" or "visit postponed".**
  Those are reports, not faults (4.13).
- **Never in the calculator ceiling state.** Passing 100 m² is a normal outcome and
  a route to Inspection — 01 §A7 and 03's ceiling copy both say so.
- **Never on 404 or 500.** 01's calm pages are right.
- **Never as a countdown, a scarcity marker, or anything to do with the 60-day
  credit window.** 04 §A2 item 4 already forbids a red timer; the colour makes the
  temptation real, so it is written down.
- **Never a border around a photograph, never a fill behind body text, never a
  toast rule** (there is no error toast; errors are inline or a screen).

**Why this reads as ours.** It appears at most twice in a session, always at 2px
or as 14px type, never as a fill larger than a chip, always on a warm light
ground it was mixed to sit on, and it is structurally incapable of showing up
anywhere near a photograph. It is the only colour in the system with a written
prohibition list longer than its permission list — which is what makes it read as
a deliberate part of the palette rather than a framework default.

---

## 7. What still needs the owner, not us

1. **Whether a cancelled client keeps their reports** (3.1). Product + legal.
2. **Third-party analytics yes/no**, which decides whether a consent banner exists
   at all (3.5).
3. **Legal address and registration number** — still the oldest open item, still on
   the critical path for the bank package, the footer and About.
4. **Pro-rata basis: by visits consumed or by days elapsed** (01 §D1). Two
   different numbers on the same screen and in the refund policy. 01 recommends by
   visits; I agree, and it needs the owner's word because it is a commercial
   promise printed on a legal page.
5. **Callback SLA "within one working day"** — written into copy in three
   documents, unconfirmed by the founders.
6. **The ֏ glyph check in Cabin** (DECISIONS §5) — the fallback in 2.5 makes the
   build safe either way, but the check must still be run.
7. **The `CLAUDE.md` price table is stale** against BRIEF and DECISIONS (2.7).
