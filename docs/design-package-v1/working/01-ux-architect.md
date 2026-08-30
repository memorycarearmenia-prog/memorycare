# MemoryCare — UX Architecture
**Role:** UX Architect · **Deliverable:** structure, flow, behaviour
**Language:** English (source language for later ARM/RUS localisation)
**Date:** 30.08.2026

---

## 0. Five decisions that govern everything below

I am stating these first because every wireframe in this document depends on them. Each is a judgement call and each carries its reason.

**D1. The site has one object model, and it is the Plot — not the Subscription.**
A client can hold several plots (the Special tier explicitly says "several family plots"), and the emotional unit a person thinks in is "my mother's grave", not "my Optimal plan". Every portal URL is therefore scoped to a plot, and the dashboard is a list of plots, not a list of invoices. *Reason: if we scope to subscription, the second plot breaks the whole IA and we rebuild in month three.*

**D2. Nude is the page ground; Ivory is the raised surface and the type-on-dark.**
The brief asks for these two to be given fixed jobs. Mine: `#EFE5D5` Nude = page background everywhere on light screens. `#F3F0E9` Ivory = cards, the report canvas, input fills, and all text sitting on Anthracite. A card is therefore *lighter* than its ground, which is the correct direction for a light premium look and gives us elevation without shadow. *Reason: shadows read as SaaS; a 1.1-ratio tonal step reads as paper.*

**D3. The report is a document, not a feed.**
It has a fixed masthead, a fixed block order, and it prints. The guest link renders the same document with three blocks removed. *Reason: the brief says the report is the product; a product needs a stable form the client recognises on the sixth opening.*

**D4. Consultation is the primary path; the calculator is the trust device that feeds it.**
The calculator's terminal action is not "buy" — it is "request consultation with this configuration attached". The number the client saw is carried into the lead record and shown back to them in the confirmation. *Reason: the brief's stated purpose for the calculator is killing the fear of "a different price for the American". That fear is only killed if the number survives the handoff to a human.*

**D5. Locale lives in the URL from day one: `/en/…`, `/hy/…`, `/ru/…`.**
Even though we ship English first. *Reason: retrofitting a locale segment after launch invalidates every indexed URL and every WhatsApp-shared report link.*

---

# PART A — UX

## A1. Information architecture

### A1.1 Marketing site sitemap

Root redirect: `/` → `/en/` (later: language negotiation by `Accept-Language`, with a manual switcher that persists in a cookie and never silently redirects a shared link).

```
/en/                                Home
├── /en/pricing/                    Pricing (5 products + calculator + guarantees)
├── /en/how-it-works/               How it works
├── /en/sample-report/              Sample report  ← the product demo
├── /en/family-circle/              Family Circle  ← the differentiator
├── /en/guarantees/                 MemoryCare Guarantees (full text)
├── /en/about/                      About the company (bank requirement)
├── /en/contacts/                   Contacts
├── /en/consultation/               Consultation request (standalone page + modal twin)
│   └── /en/consultation/thank-you/ Confirmation (conversion-tracking target)
├── /en/pay/                        Payment options (transfer now, card later)
│   ├── /en/pay/bank-transfer/       Invoice + wire instructions
│   └── /en/pay/thank-you/
└── /en/legal/
    ├── /en/legal/privacy/          Privacy policy
    ├── /en/legal/refund/           Refund policy (pro-rata rules live here)
    ├── /en/legal/terms/            Terms of service
    └── /en/legal/limitations/      Service limitations & restrictions
```

Utility, unlinked from the primary nav:
```
/en/404/    /en/500/    /sitemap.xml    /robots.txt
/en/legal/  index page listing the four documents (footer link target)
```

**Navigation model.**
- Primary nav (desktop, max 5 items): Pricing · How it works · Sample report · Family Circle · About. Contacts is not in the primary nav; it is the phone icon + the footer. *Judgement: five items is the ceiling before a nav starts reading as a corporate brochure, which is exactly the failure mode named in the brief.*
- Utility slot, right of nav: language switcher, then **Client login** (text link), then **Free consultation** (button).
- Mobile: hamburger → full-screen panel. Order in panel: the five nav items, divider, Guarantees, Contacts, divider, Client login, language switcher, then a pinned full-width consultation button at the bottom of the panel.
- Footer, on every page (bank requirement): 4 columns desktop / stacked accordion-free list mobile — Company (About, Contacts, Guarantees), Services (the five products, each anchoring into Pricing), Legal (the four documents), Contact block (both names + phones as `tel:` links, `info@memorycare.am` as `mailto:`, legal address placeholder, MemoryCare LLC line).

**Anchors that must be stable** (used by nav, footer, calculator and ads):
`#inspection`, `#express`, `#optimal`, `#maximum`, `#special`, `#calculator`, `#guarantees`, `#faq`.

### A1.2 Portal sitemap

```
/portal/login/                          Login (email magic-link primary, password secondary)
/portal/login/check-email/              Interstitial
/portal/activate/:token/                First-time activation from the welcome email
/portal/                                Dashboard — list of plots  (D1)
/portal/plots/:plotId/                  Plot overview: next visit, last report, care team
/portal/plots/:plotId/visits/           Visit list (past + scheduled)
/portal/plots/:plotId/documents/        Invoices, contract, condition record
/portal/visits/:visitId/                Report screen (authenticated)
/portal/visits/:visitId/revisit/        Guarantee re-visit request
/portal/family/                         Family Circle roster
/portal/family/invite/                  Send invitation
/portal/family/:memberId/               Member detail: role, scope, remove
/portal/invite/:token/                  Invitation acceptance (unauthenticated entry)
/portal/orders/new/                     Order a one-off service
/portal/orders/:orderId/                Order status
/portal/billing/                        Subscription, payment method, invoices
/portal/billing/change/                 Upgrade / downgrade / change plot parameters
/portal/billing/cancel/                 Cancellation + pro-rata refund (self-serve)
/portal/profile/                        Name, contacts, language
/portal/profile/notifications/          Reminder opt-in + delegate recipient
/portal/support/                        Message us / call us
```

Public, outside `/portal`:
```
/r/:shareToken/                         Guest report view — no login, no prices, no upsell
/r/:shareToken/expired/                 Revoked or expired link
```

I put the guest report on a short root path deliberately: it is pasted into WhatsApp and read on a 5-inch screen by a 70-year-old aunt. `memorycare.am/r/8fk2wq` is a link a person can retype. A `/portal/...` path implies a login wall and gets ignored.

---

## A2. User journeys

### A2.1 Journey 1 — Diaspora (Anna, 47, Glendale CA)

| # | Stage | Where | What she does | What must be true |
|---|---|---|---|---|
| 1 | Trigger | Instagram / Google `grave care Yerevan` | Taps a link at 23:40 local | Landing page LCP < 2.5s on 4G; title disambiguates from dementia care |
| 2 | 8-second judgement | `/en/` hero | Sees a *report* on screen one, with a GPS chip and a date | The hero shows the artefact, not the emblem |
| 3 | "Is this real?" | Scroll to Proof block → `/en/sample-report/` | Opens the full sample report | Sample report is a real screen, not a screenshot in a laptop mockup |
| 4 | "What does it cost — for *me*?" | `/en/pricing/#calculator` | Moves two sliders, sees a number | No email gate before the number. Ever. |
| 5 | "Who are they?" | `/en/about/`, footer | Checks names, Armenian phone numbers, legal entity | Two named humans with real numbers, one email on the real domain |
| 6 | "What if it's bad?" | `#guarantees` | Reads the three guarantees | Guarantees are on Home, Pricing and their own page |
| 7 | Action | Consultation modal | Name, phone (+1), city/cemetery, submits | International phone accepted without her thinking about it |
| 8 | Gap | WhatsApp / call | Hayk calls within the promised window | Confirmation states the window in *her* terms ("within one business day, Yerevan time (UTC+4)") |
| 9 | Pay | `/en/pay/bank-transfer/` | Wire transfer | Instructions downloadable as PDF for her bank |
| 10 | Portal | Welcome email → `/portal/activate/:token` | Sets a password / uses magic link | Lands on the **first-entry state**, not an empty table |
| 11 | Doubt gap (0–14 days) | Portal, email | Waits for the first visit | Scheduled-visit state must actively narrate the wait (see A4.1) |
| 12 | Payoff | Report notification → report | Opens, then **shares to the family group** | Share is a first-class button, not a hidden menu item |

**The critical drop-off is step 11.** She has paid 160,000 ֏ to a company she has never met and there is nothing in her account. Everything I specify for the portal first-entry screen exists to survive that fortnight.

### A2.2 Journey 2 — Local premium (Armen, 54, Yerevan)

| # | Stage | Where | What he does | What must be true |
|---|---|---|---|---|
| 1 | Trigger | Word of mouth / search in Armenian | Arrives on a phone, mid-day, 40 seconds to spare | Same page, same copy — no local/diaspora fork |
| 2 | Scan | Home | Scrolls fast to Pricing | Pricing reachable in one tap from the sticky bar |
| 3 | Compare | `/en/pricing/` | Compares Optimal vs Maximum on visit count | Visit count is the largest number in the card |
| 4 | Verify method | `/en/how-it-works/` | Looks for the equipment and the chemistry | Method described concretely — steam, pressure washer, vacuum, professional chemistry |
| 5 | Objection | — | "I could do this myself in one Saturday" | The counter is *time and repetition*: 4 visits, seasonal, scheduled, without him |
| 6 | Action | Consultation or direct call | Often taps the phone number instead of the form | `tel:` links are live everywhere, header included |
| 7 | Convert | Phone → transfer | Pays quickly | Handoff to the portal identical to Anna's |

He converts faster and reads less. The consequence for structure: **every block on the home page must be independently comprehensible**, because he will read three of them and skip four. No block may depend on the block above it for meaning.

### A2.3 Journey 3 — The split case: payer in LA, beneficiary in Yerevan

Vahe, 41, Los Angeles, buys Optimal for his mother Siranush, 72, in Yerevan. **He pays. She is the one who cares.** She has a smartphone, uses WhatsApp, and will never create an account.

This is the case the brief names as most important, and the current structure of the consultation form cannot express it. Here is the model I propose.

**Three roles, separated at the data level:**

| Role | Who | Auth | Gets |
|---|---|---|---|
| **Account owner / payer** | Vahe | Full account | Everything: billing, plan changes, invitations |
| **Local contact** | Siranush | *No account required* | The day-before reminder by SMS/WhatsApp; may meet the crew; receives every report as a plain `/r/` link |
| **Family Circle member** | Vahe's brother in Moscow | Invited sub-account | Reports + one-off orders, no billing |

**Flow, end to end:**

1. **Consultation form, field 4 (conditional).** After the three required fields there is one optional line: *"Is there a family member in Yerevan we should coordinate with?"* → reveals two fields (name, phone). This is the whole split-case capture, and it costs one tap for everyone who does not need it. *Judgement: the brief's three-field form is right for volume, but this business is structurally a split-payer business; a hidden fourth field is the minimum honest capture.*
2. **Onboarding call.** Hayk records the plot identity — cemetery, sector/row, the name on the monument — and the local contact. **The person who is buried is a data field.** It appears in the report masthead as "Plot of the [family] family" or with the name, at the owner's choice, set once during onboarding and editable in the portal. I flag this explicitly because the brief never names it and a report with no identity on it is unusable in a family chat.
3. **Payment.** Vahe pays from the US. The invoice is in AMD with an indicative USD figure marked clearly as approximate.
4. **Portal activation.** Vahe activates. His dashboard shows one plot with the mother's plot identity.
5. **Notification routing — this is the mechanism the brief asks for.** `/portal/profile/notifications/` presents a per-plot matrix:

   | Event | Owner (Vahe) | Local contact (Siranush) | Family Circle |
   |---|---|---|---|
   | Day-before reminder | opt-in, off by default | **on by default when a local contact exists** | opt-in per member |
   | Visit completed / report ready | on | on (as a plain link) | on |
   | Visit postponed | on | **on, always — she may be planning to attend** | on |
   | Payment / invoice | on | never | never |
   | Subscription expiring | on | never | Manager role only |

   Siranush's channel is SMS or WhatsApp with a `/r/` link. She never sees a login screen, never sees a price, and never sees a renewal prompt. That last point is a rule, not a preference: sending "renew your subscription" to a grieving 72-year-old who did not pay is a brand-ending message.
6. **The share loop.** Vahe opens the report in the portal, taps Share, and gets a link he pastes into the family group. The OG preview shows the mark, "Visit report", and the date. No photograph. Twelve relatives open it on the guest view; none of them see a price.
7. **Escalation.** If Siranush is unhappy with a visit, she has no account — so the guest report carries **one** non-commercial action: "Something wrong with this report? Tell us" → a two-field form (name, phone) that files a guarantee re-visit request against that visit and notifies Vahe. This is the only interactive element permitted on the guest view, and it is support, not sales.

**What this implies for the developer:** account ≠ beneficiary ≠ notification recipient. Three separate contact records per plot. If the external developer models a single `user.phone`, the split case is unbuildable. This is the highest-priority thing to send them before 20 September.

---

## A3. Wireframes — marketing site

Notation: **[F]** = fixed / sticky, **[S]** = scrolls. "AF375" = above the fold at 375×667 (iPhone SE — the smallest device I am designing for; if it works there it works on an iPhone 15). Fold budget at 375 is **667px minus 56px header minus browser chrome ≈ 560px of usable first paint.**

### A3.0 Global chrome

**Header [F], 56px tall at 375, 72px at 768+.** Nude ground, 1px Olive divider at 20% opacity, and it gains a solid Nude fill plus a hairline shadow only after 24px of scroll (before that it is transparent over the hero).
- 375: `[hamburger 44×44] … [logo lock-up, centred, 32px tall] … [phone icon 44×44 → tel:]`
- 768: `[logo left] … [nav 5 items] [ARM/ENG/RUS] [Log in] [Free consultation]`
- 1440: same as 768 with wider gutters; nav items 24px apart.

**Sticky action bar [F], mobile only, 375–767.** Appears after the user passes the hero (scrollY > 480) and hides while scrolling up is not needed — it stays. 64px tall, Ivory fill, top hairline. Two targets: `[Free consultation — Deep Olive fill, Ivory label, 48px tall, 62% width]` `[Call — outline, 44×44 minimum, 38% width]`. It is suppressed on `/en/consultation/` (the form is already there) and on all four legal pages.

**Footer [S], every page.** Order at 375: logo mark + wordmark → tagline in Olive small caps (decorative use, large size, never below 14px) → the two names with phone numbers as separate 44px-tall rows → email row → legal address placeholder, visibly marked → four legal links → language switcher → "MemoryCare LLC, Yerevan, Armenia · © 2026". At 768+ this becomes four columns.

### A3.1 Home — `/en/`

| # | Block | Contents | Notes |
|---|---|---|---|
| 1 | **Hero / Proof** | Eyebrow (what we do, disambiguating) → H1 → one-sentence subhead → **report artefact** → primary CTA + secondary "See a full report" | AF375: eyebrow, H1, subhead, and the **top 180px of the report card**. The image must be cropped by the fold on purpose so it invites scroll. |
| 1a | *Report artefact* | A real card, not a photo of a phone: Ivory surface, top row = date + cemetery, then a `✓ GPS confirmed` chip, then a 4:3 placeholder image slot, then two thumbnails | This is the single most important object on the site. It is built in HTML, so it is sharp, translatable and fast. |
| 2 | **Two reasons** | Two short cards side by side at 768+, stacked at 375: "You are far away" / "You have no time" | The one place both audiences are named, equally, without ranking. |
| 3 | **What a visit is** | Numbered 3-step strip: Plan → Visit → Report. Each with a 40px Olive line-icon, a 2-word label, one line of text | Independently comprehensible (Armen's skim). |
| 4 | **Method** | Equipment and chemistry, 4 items in a 2×2 grid at 375 | Answers "why not do it myself". |
| 5 | **Pricing preview** | Three subscription cards (Optimal centre and marked *Most chosen*), then a visually separated Inspection strip below a divider, then "See all products and the calculator →" | Full pricing lives on `/en/pricing/`. Home carries a preview only, otherwise the page is 9,000px long. |
| 6 | **Family Circle** | Illustration slot + 3 bullets + link | The differentiator gets a full-width block, not a bullet. |
| 7 | **Guarantees** | Three items, each an icon + bold line + one sentence, on an Olive-tinted panel | Panel is decorative Olive at low opacity with Anthracite text — never Olive text. |
| 8 | **Who we are** | Two people, name, role, phone. Photo slots marked "September shoot" | Trust for a payer abroad. No fabricated numbers anywhere on this page. |
| 9 | **FAQ** | 6 items, accordion, first one open | Contains the honest competitive line and the "what if we can't access the plot" answer. |
| 10 | **Final CTA** | Anthracite full-bleed band, Ivory heading, Nude-fill button with Anthracite label | The one dark block on the page; it terminates the scroll. |
| 11 | Footer | as above | |

### A3.2 Pricing — `/en/pricing/`

1. **Page header** — H1, one line of subhead, and a line stating the coverage rule: up to 16 m², up to 2 monuments. AF375 ends inside block 2.
2. **Subscriptions** — three cards. At 375 they stack, Optimal **first** (not centre — on mobile "centre" does not exist, and putting the leading choice first beats putting it in the middle of a stack). At 768 they are 3-up with Optimal raised 12px and carrying a *Most chosen* ribbon. Card anatomy, top to bottom: name (EN + Armenian original in small caps beneath) → visit count as the biggest number on the card → price `160,000 ֏ AMD / year` → 4 feature lines → `Request consultation` (primary) → `Pay online` (secondary, currently rendering as `Pay by transfer`).
3. **Divider + Inspection** — a full-width horizontal rule and a heading change, then a card in a *different shape*: horizontal at 768+, Nude-on-Ivory inversion, no ribbon, badge reading `One-off`. Copy states plainly that no cleaning is performed. Below it, the credit rule in one sentence with a link to the full terms.
4. **Special** — a slim band: "Larger plot, more monuments, several family plots" → `Start with an Inspection` (primary) + `Open the calculator` (secondary).
5. **Calculator** — see A7. Full-width, Ivory surface, generous padding.
6. **Credit mechanics** — a small three-row explainer table. Explicit: one credit only, the larger one, 60 days, fires at signature, no credit between one-off products.
7. **Guarantees** — same component as Home block 7.
8. **Pricing FAQ** — 5 items: What is a full visit · What if my plot is larger · How do I pay from abroad · Can I cancel · Do prices differ for diaspora clients (answer: no, and say it plainly).
9. **CTA band** + footer.

### A3.3 How it works — `/en/how-it-works/`

1. Page header.
2. **Timeline**, 4 steps, vertical at 375 with a 2px Olive rail down the left at 20px, alternating left/right at 1440: Consultation → Subscription and schedule → The visit → The report. Each step: number in Gloock, heading, 2–3 sentences, one placeholder image slot 4:3.
3. **What a full visit includes** — checklist, 6–8 items, two columns at 768+.
4. **What we do not do** — same visual weight, 4 items. *Judgement: naming the limits raises trust more than any adjective, and the bank's "legal restrictions" requirement needs a home that people actually read. This block is that home, and it links to `/en/legal/limitations/`.*
5. **Weather and access** — the honest paragraph: seasons, rain, locked sections, disputed access, and what happens then (rescheduled, you are told, no visit is silently skipped).
6. Report preview strip → link to `/en/sample-report/`.
7. CTA + footer.

### A3.4 Sample report — `/en/sample-report/`

This page renders the *actual report component* with placeholder media, wrapped in the marketing chrome. It must not be a picture of a report.

1. Short header: "This is what arrives after every visit."
2. **The report component**, full width on mobile, max 720px centred at 1440, in the exact block order defined in A4.4.
3. **Annotation layer** — at 1440, callouts to the left and right of the document explaining GPS verification, timestamping, the video, the condition notes. At 375 the annotations become a numbered list *below* the document, never overlaying it.
4. "How the link looks when you send it to family" — a rendered WhatsApp-style preview card showing the OG rule in action: mark, "Visit report", date, no photograph. This block does double duty: it demonstrates the product and it pre-empts the privacy question.
5. CTA + footer.

### A3.5 Family Circle — `/en/family-circle/`

1. Header + one-sentence definition.
2. **How it works** — 3 steps: you invite → they get their own access → they see reports and can order services.
3. **The roles table** — the public, simplified version of the matrix in A5 (three roles, five rows). Full matrix lives in the portal.
4. **The Yerevan relative case** — this is where we explain, publicly, that the person who meets the crew does not need an account. It is the answer to a question the diaspora buyer has not yet formed.
5. Privacy note: who can see what, how to remove someone, that removal is immediate.
6. CTA + footer.

### A3.6 About — `/en/about/`

Bank requirement plus diaspora due diligence. Blocks: what MemoryCare is (2 paragraphs) → why it exists → the two founders (name, role, direct phone, photo slot) → how we work (method, verification, equipment) → legal entity block: MemoryCare LLC, registration number placeholder, legal address placeholder, `info@memorycare.am`, both phones → an honest "we started in 2026" line → CTA + footer. **No history/mission/values pages.** Those are the failure named in the brief.

### A3.7 Contacts — `/en/contacts/`

Two name cards with phone (`tel:`), WhatsApp (`wa.me`) and role → email → working hours in **Yerevan time with the UTC offset spelled out** (the diaspora reader is in another zone; "9:00–18:00" alone is useless to her) → a short form (name, contact, message) → legal entity block → map slot marked as placeholder pending the legal address.

### A3.8 Consultation — `/en/consultation/` and the modal

Identical component in two containers. See A6.1 for the field spec. Page version adds a right rail at 1440 (at 375 it goes *below* the form): the three guarantees, the "no obligation, no payment now" line, and both phone numbers for people who would rather call. The form is above the fold at 375 down to and including the first field.

### A3.9 Payment — `/en/pay/`

Two paths presented as equals rather than as a primary and a broken one: **Bank transfer (available now)** and **Card payment (opening soon — no date promised)**. Transfer path: choose product → confirm plot parameters → generate invoice → wire instructions on screen and as PDF → "tell us when you have sent it" confirmation. *Judgement: showing a disabled card button with no explanation reads as a broken site; labelling it honestly reads as a young company, which is what we are.*

### A3.10 Legal pages ×4

Single template: H1 → last-updated date → table of contents (sticky at 1440, collapsed accordion at 375) → body at 65–75 characters per line → contact block at the end. Body text 17px minimum, line height 1.7. These are read by a bank officer and by a worried 55-year-old; both need it legible.

---

## A4. Wireframes — portal

Portal chrome: header [F] 56px with mark + plot switcher (when >1 plot) + avatar menu. **Bottom tab bar [F] at 375–767**, 56px + safe-area inset, four tabs: Plots · Reports · Family · Account. At 768+ the tab bar becomes a 240px left sidebar [F] and the content column scrolls.

### A4.1 First entry after payment — `/portal/` with zero visits

The most important screen in the product. The client has paid and there is nothing to show. **The screen must not look empty; it must look scheduled.**

Block order at 375:
1. Greeting line: "Welcome, [name]." — Gloock, 28px.
2. **Status card**, Ivory on Nude, full width: plot identity → `Subscription active` chip → **"First visit: 12–16 September"** as the largest text in the card → beneath it, one line naming who will come and that the crew records GPS on arrival.
3. **Progress rail** — 4 dots, horizontal, labelled: Subscription active ✓ · Plot located · First visit · Report. Dot 1 filled Deep Olive, dot 2 in progress (ring), 3–4 outline. This converts an empty state into a *timeline with position*, which is the entire psychological job of this screen.
4. **"What happens next"** — three short rows with times: within 2 days we confirm the plot coordinates; the day before the visit you get a reminder if you asked for one; within 24 hours of the visit, the report.
5. **Two actions**: `Add a family member` (primary — gives her something to *do*, and it is the action with the highest retention value) and `See a sample report` (secondary, opens the marketing sample so she can see what is coming).
6. Support row: "Questions? Hayk — +374 93 154 108" with call and WhatsApp targets.

AF375 must contain items 1, 2 and the top of 3. If the client has to scroll to learn when the first visit is, this screen has failed.

### A4.2 Dashboard with plots — `/portal/`

Greeting → one plot card per plot (identity, cemetery, next visit date, last report thumbnail with a *neutral* crop, plan name, and a `View` target on the whole card, 88px minimum height) → `Add another plot` outline row → notification strip if anything needs attention (postponement, payment, expiring subscription).

### A4.3 Visit list — `/portal/plots/:plotId/visits/`

Reverse-chronological, with **scheduled visits at the top in a separate, visually distinct group** (Ivory rows with a dashed Olive left border) and completed visits below (solid rows, Deep Olive left border). Each row: date, status chip, one-line summary, chevron. Row height 72px, entire row tappable. Filter chips at 768+ only: All · Completed · Scheduled · Postponed. At 375, filtering is a needless control on a list of at most nine items per year — I am cutting it.

### A4.4 Report screen — `/portal/visits/:visitId/` (and the guest view)

Block order is fixed and is the brief's rule made concrete. **Confirmation first, photographs after.**

| # | Block | Contents | Guest sees |
|---|---|---|---|
| 1 | Masthead | Mark, "Visit report", plot identity, cemetery | yes |
| 2 | **Confirmation** | Large date · `✓ Visit completed` chip · crew arrival and departure times · `✓ GPS confirmed` chip → tap reveals a static map crop with a pin and coordinates | yes |
| 3 | Crew note | 1–3 sentences in plain language about what was done and the state of the plot | yes |
| 4 | Work performed | Checklist, ticked items only | yes |
| 5 | **Photographs** | Vertical stack at 375, one per screen-width, 4:3, tap to open full-screen with pinch-zoom. Captions below each. **Before/after appears here, as a labelled pair, not as a hero slider.** | yes |
| 6 | Video | One 20–40s clip, poster frame, muted, plays inline, never autoplays | yes |
| 7 | Condition and recommendations | Observations; recommended work as a plain list | **text yes, prices NO** |
| 8 | Documents | PDF download of the report | yes |
| 9 | Actions | `Share with family` · `Order additional work` · `Request a re-visit` | **only "Something wrong with this report?"** |
| 10 | Next visit | Date of the next scheduled visit | **no** — implies a plan, implies money |

Sticky at 375 while scrolling the report: a slim 48px bottom bar with `Share`. Nothing else. It is the action the product exists to produce.

**Guest view differences, restated as rules for the developer:** blocks 7-prices, 9-commercial, 10 are removed server-side, not hidden with CSS. No plan name, no price, no renewal, no "MemoryCare offers…" footer. The guest footer is one line: what MemoryCare is, and a `tel:` for questions. **No CTA button of any kind.**

### A4.5 Share sheet — modal on `/portal/visits/:visitId/`

Sheet from the bottom at 375. Contents: explanation of what the recipient will see (one line, and it matters — the owner needs to know she is not sending prices to her aunt) → the link in a read-only field with a `Copy` button → `WhatsApp` and `Viber` buttons → `Email` → a divider → **`Link is active. Revoke`** with the creation date. Revocation is one tap plus a confirm. *Judgement: a permanent unrevocable link to a photograph of a family grave is not acceptable; revocation must be visible in the same sheet that creates it, not buried in settings.*

### A4.6 Family Circle — `/portal/family/`

Roster: rows of member (avatar initials, name, role chip, "invited" vs "active", scope = which plots). Owner row is pinned first and cannot be removed. `Invite a family member` primary button. Below the roster, a collapsed `What each role can do` accordion containing the full matrix from A5.

`/portal/family/invite/`: name (optional) → phone or email → **role selector as three radio *cards*, each with a one-line description**, not a dropdown (a dropdown hides the consequence of the choice) → plot scope checkboxes if more than one plot → optional personal message, 200 chars → `Send invitation`. Confirmation states exactly what the invitee will receive.

`/portal/invite/:token/`: brand block → "[Name] invited you to the Family Circle for [plot identity]" → what you will be able to do (from the role) → set a password or continue with a magic link → accept.

### A4.7 Order a one-off service — `/portal/orders/new/`

Plot selector (if >1) → service list as cards with prices (Inspection, Express, and additional works from the last report's recommendations, pre-selectable) → date preference: "as soon as possible" or a month picker → notes → **price summary including any plot surcharges, computed with the calculator's own logic** → `Send request`. It is a request, not a checkout: card acquiring is not live. Say so on the button label's helper line.

### A4.8 Billing — `/portal/billing/`

Current plan card (name, price, plot parameters, period, renewal date) → payment method (bank transfer for now) → invoice list with PDF downloads → `Change plan` → `Cancel subscription` as a plain text link in Deep Olive, at the bottom, not a red button. *Judgement: hiding cancellation is both a dark pattern and a bank-requirement violation; making it a shouting red button is equally wrong for this brand. A calm, findable link is correct.*

### A4.9 Cancellation with pro-rata refund — `/portal/billing/cancel/`

Four steps, one screen each, with a visible `Step n of 4`.
1. **Reason** — 5 radio options + free text, all optional, `Skip` visible.
2. **What you will lose** — plain list: remaining visits (count and their scheduled dates), portal access end date, family members who lose access. No guilt copy. No "are you sure??".
3. **Your refund** — the arithmetic shown as a table: annual price · visits completed · value consumed · **refund amount** · method (transfer back to the paying account) · timing. Then a line noting that a completed visit is never refunded.
4. **Confirm** — one button, and a `Keep my subscription` escape at equal weight.
Success: confirmation screen + email, refund reference number, and a line saying they can return without penalty.

**Open question I am escalating, because the brief does not answer it and it cannot be designed around:** is pro-rata computed *by visits consumed* (160,000 / 4 = 40,000 per visit) or *by days elapsed*? These give materially different numbers — a cancellation on day 100 with one visit done yields a 120,000 refund by visits and roughly 116,000 by days. The refund policy page and this screen must state one rule. **I recommend by visits consumed**: it is comprehensible, it matches how the client experiences the service, and it never produces the situation where a client who has had one visit is told they consumed 27% of a service they received one quarter of.

### A4.10 Profile and notifications — `/portal/profile/notifications/`

Per-plot table of the events in A2.3, each with toggles per recipient, plus a `Local contact` block (name, phone, channel: SMS or WhatsApp) with an explicit consent checkbox: "This person has agreed to receive messages from us." Third-party consent is a real legal exposure and the checkbox is not decorative.

---

## A5. Family Circle permission matrix

Four roles. **Owner** (the payer), **Manager** (a trusted relative, typically the one in Yerevan or the eldest sibling), **Member** (sees everything about care, touches no money), **Guest** (a `/r/` link holder, no account).

| Capability | Owner | Manager | Member | Guest (link) |
|---|:--:|:--:|:--:|:--:|
| View reports (photos, video, GPS) | ✅ | ✅ | ✅ | ✅ (single report only) |
| View the visit schedule | ✅ | ✅ | ✅ | ❌ |
| Download the report PDF | ✅ | ✅ | ✅ | ✅ |
| Share a report by link | ✅ | ✅ | ✅ | ❌ |
| Revoke a share link | ✅ | own links | own links | ❌ |
| See prices anywhere in the portal | ✅ | ✅ | ❌ | ❌ |
| Order a one-off service | ✅ | ✅ (request → owner approves) | ❌ | ❌ |
| Approve an order that carries a charge | ✅ | ❌ | ❌ | ❌ |
| Request a guarantee re-visit | ✅ | ✅ | ✅ | ✅ (as a message, no account) |
| Reschedule a visit | ✅ | ✅ | ❌ | ❌ |
| Change / upgrade the subscription | ✅ | ❌ | ❌ | ❌ |
| Cancel the subscription | ✅ | ❌ | ❌ | ❌ |
| View invoices and payment details | ✅ | ❌ | ❌ | ❌ |
| Invite a family member | ✅ | ✅ (Member only) | ❌ | ❌ |
| Remove a family member | ✅ | ❌ | ❌ | ❌ |
| Edit plot identity (name on monument, notes) | ✅ | ✅ | ❌ | ❌ |
| Set the local contact and reminders | ✅ | ✅ | own only | ❌ |
| Transfer ownership | ✅ | ❌ | ❌ | ❌ |

Rules that fall out of the table and must be implemented as such:
- **Member never sees money.** Not the plan name, not the price, not the renewal date. This is the role for the aunt and the cousins, and it is the default suggested role on the invite screen.
- **Manager can spend nothing without the Owner.** Manager orders create a request that lands in the Owner's dashboard as a decision. This is what makes it safe to hand a relative real control.
- **Only the Owner can cancel or transfer.** One person owns the money, always.
- **Ownership transfer exists** because the payer may die, and this service is bought by people who are thinking about exactly that. It is a two-step confirm with email verification on both sides. The brief omits it; I consider it non-optional for this product.

---

## A6. Form specifications

### A6.1 Consultation request (primary conversion, page + modal)

| Field | Type | Req | Rules | Error copy |
|---|---|:--:|---|---|
| Name | text | ✅ | 2–60 chars, any script (Armenian, Cyrillic, Latin) | "Please tell us your name." |
| Phone or email | tel/email, single field with auto-detection | ✅ | If it starts with `+` or a digit → phone with country selector; otherwise email. E.164 validation for phone; RFC-lite for email | "Enter a phone number or an email so we can reach you." / "This phone number doesn't look complete — check the country code." |
| City or cemetery | combobox | ✅ | Free text with suggestions (Tokhmakh, Zeytun, Nubarashen, Yerablur, "Not sure") | "Which cemetery, or which city? 'Not sure' is a valid answer." |
| Family member in Yerevan | disclosure → name + phone | ❌ | Same phone rules | inherits |
| Preferred contact time | 3 chips: Morning / Afternoon / Evening (Yerevan time) | ❌ | — | — |
| Message | textarea | ❌ | 0–500 chars, counter appears from 400 | "Keep it under 500 characters." |
| Consent | checkbox | ✅ | Links to `/en/legal/privacy/` | "Please confirm so we can contact you." |
| — | hidden | — | `calc_config` (area, monuments, tier, computed price), `utm_*`, `page_path`, `locale` | — |

**Behaviour**
- Validation on **blur**, never on keystroke; re-validation on keystroke only once a field is already in error (so a person watching themselves fix it sees it clear).
- Errors render **below** the field, in Deep Olive, 15px, with a 20px icon, and the field border goes 2px Deep Olive. **Colour is never the only signal** — the icon and the text carry it, because ~8% of a male 40–60 audience is colour-deficient.
- Submit sets the button to a loading state with the label "Sending…" and disables the form. Never disable the submit button before submission; a disabled button with no explanation is the most common accessible-form failure.
- On error, focus jumps to the first invalid field and a summary appears at the top of the form, linked to each field, with `role="alert"`.
- Success: replace the form in place with a confirmation block (not a redirect on the modal; a redirect to `/en/consultation/thank-you/` on the standalone page for tracking). Confirmation states: we will call within one business day; Yerevan working hours with the UTC offset; both direct phone numbers; and if a calculator config was attached, it is echoed back — "You configured: 24 m², 3 monuments, Optimal — 270,000 ֏ AMD/year."

**International phone handling — the specification, because this is where forms fail for a diaspora audience.**
- One `<input type="tel">` with `inputmode="tel"` and `autocomplete="tel"`, preceded by a country selector (44×44 minimum, showing dial code as text — never a flag alone; flags are political and unreadable at 20px).
- Default country from IP geolocation, but **always visibly overridable**, and never re-guessed after the user has changed it.
- Accept and normalise: `+1 818 555 0142`, `(818) 555-0142`, `818.555.0142`, `+33 6 12 34 56 78`, `093154108`. Store E.164. Display formatted per country.
- **Do not block on paste.** People paste numbers from contacts with invisible characters; strip and normalise silently.
- If the number cannot be parsed but the user insists (second submit), accept it and flag the lead for manual review rather than losing it. *Judgement: a lost lead costs 160,000 ֏; a malformed phone number costs one minute of Hayk's time.*
- WhatsApp checkbox: "This number is on WhatsApp" — checked by default for non-`+374` numbers, because that is how the diaspora actually communicates.

### A6.2 Other forms — deltas only

- **Contact form** (`/en/contacts/`): name ✅, phone-or-email ✅, message ✅ (min 10 chars), consent ✅.
- **Invitation**: phone or email ✅, role ✅ (default Member), plot scope ✅ if >1 plot, name ❌, message ❌ 200 chars.
- **Guarantee re-visit**: pre-filled visit reference (read-only), "what was wrong" ✅ 20–1000 chars, up to 3 photo uploads ❌ (10 MB each, HEIC accepted — the audience is on iPhones), preferred window ❌. Confirmation must state the 7-day guarantee and give a name, not a ticket number alone.
- **Guest report feedback** (the only interactive element on `/r/`): name ✅, phone ✅, message ✅. Three fields, no consent checkbox theatre, no account.
- **Cancellation**: covered in A4.9.

---

## A7. The calculator — interaction specification

**Purpose (restated, because it drives every decision here): to show a diaspora client that the price is the same for them as for anyone.** It is a trust instrument that happens to do arithmetic.

### Layout
375: single column inside an Ivory card, 20px padding, full-bleed to the page margins.
768+: two columns — controls left (58%), result panel right (42%), result panel sticky within the card while the controls scroll.

### Anatomy, top to bottom at 375
1. Heading + one line: "Your plot, your price. The same for every client."
2. **Tier selector**: two segmented buttons, `Optimal (4 visits)` / `Maximum (6 visits)`, 48px tall, Optimal preselected. Below them a text link: `Or price a one-off Express visit` — which switches the whole calculator to one-off mode.
3. **Slider 1 — Plot area.** Label left, **value right in a 17px numeric field the user can also type into** (sliders are a nightmare with a 55-year-old's thumb on a 375 screen; the number field is the accessible escape hatch and it is not optional). Range 4–100 m², step 1, default **16**. Track: Olive at 30% for the base range 0–16, Deep Olive for the surcharge range above 16 — so the surcharge is *visible as geometry* before it is read as a number. Thumb 28px visual, 44px hit area. Below the track, three tick labels: `16 m² included` at its true position, `50`, `100`.
4. **Slider 2 — Monuments.** Range 1–10, step 1, default **2**. Same construction. Tick label `2 included`.
5. **Result panel.**
   - Line 1: `Optimal — 4 full visits` (Anthracite, 15px)
   - Line 2: the price, Gloock, 34px at 375: `160,000 ֏ AMD / year`
   - Line 3 onward, the breakdown, only rendering rows that are non-zero:
     `Base (up to 16 m², 2 monuments) — 160,000 ֏`
     `+8 m² above 16 — +80,000 ֏`
     `+1 monument above 2 — +30,000 ֏`
     `Total — 270,000 ֏ AMD / year`
   - Indicative reference line, smaller, Anthracite at 70%: `≈ $690 · charged in AMD`. **Marked as approximate, with the rate date.** No live FX for launch.
6. **Actions**: `Request a consultation with these figures` (primary, Deep Olive fill, Ivory label, 48px, full width) and `What is included in a full visit?` (text link).
7. Fine print: prices cover the plot as configured; the final figure is confirmed after the Inspection.

### Behaviour
- **Live recalculation on drag**, with the number animating only on `pointerup` — a number counting during a drag is unreadable. Track fill updates during the drag.
- **Debounce 120 ms** on the typed number field.
- **Every state is in the URL**: `?tier=optimal&area=24&monuments=3`. This makes the configuration shareable, restores it on back-navigation, and lets Hayk send a client the exact number they discussed.
- **Keyboard**: arrows ±1, PageUp/PageDown ±10, Home/End to range ends. `role="slider"` with `aria-valuenow`, `aria-valuetext` ("24 square metres"), and a live region announcing the total on release — not during the drag.
- **Ceiling behaviour (100 m² / 10 monuments).** At the ceiling the thumb stops and the result panel is *replaced*, not annotated: heading "Let's price this properly.", one paragraph, and `Book an Inspection — 20,000 ֏` as the primary action with `Request a consultation` secondary. Entry to Special is always through Inspection, as the brief requires. Reaching the ceiling must not feel like an error — no red, no warning icon.
- **One-off Express mode**: same two sliders, surcharges `+2,500 ֏/m²` and `+7,500 ֏/monument`, result reads `65,000 ֏ AMD — one visit`, and a persistent note that this amount is credited toward an annual subscription signed within 60 days.
- **Credit preview.** When one-off mode is active there is a third line: "If you subscribe to Optimal within 60 days: 160,000 − 65,000 = **95,000 ֏** for the first year." This is the single strongest number on the entire site and it currently appears nowhere. *Judgement: worth its own line even though it adds arithmetic to a screen I otherwise want quiet.*
- **No email gate. No "see your price" reveal. No lead capture before the number.** Any of those destroy the block's only purpose.

---

## A8. State matrix

Every screen ships with these five. Rules that apply globally first:

- **No emoji in any error, anywhere.** The brief names this and it is right.
- **No red.** We have no red in the palette and we are not adding one. Errors use Deep Olive plus an icon plus explicit text. Destructive confirmations use Anthracite emphasis and clear wording.
- **Skeletons, not spinners**, for content that has a known shape (reports, lists). Spinners only for actions the user just initiated.
- **Photographs never load into a black box.** Placeholder fill is Nude, not grey or black.
- **Every error names a next step and a human.** "Call Hayk — +374 93 154 108" is a valid recovery path and often the correct one for this audience.

### A8.1 Marketing pages

| Screen | Empty | Loading | Error | Success |
|---|---|---|---|---|
| Home | n/a | Above-fold text renders first; image slots hold their aspect ratio to prevent layout shift | If the report artefact's media fails: Nude placeholder + caption, page still complete | n/a |
| Pricing / calculator | n/a | Sliders render at defaults immediately, no fetch required | If the config in the URL is out of range, clamp silently to the nearest valid value | Config carried into the consultation form |
| Sample report | n/a | Skeleton in the exact document shape | Placeholder blocks with captions | n/a |
| Consultation form | Untouched fields, no error styling | Button "Sending…", form locked | Field-level errors + top summary; on network failure: "We couldn't send that. Try again, or call us — +374 93 154 108." Field values are preserved. | In-place confirmation with the next step and the timing window |
| 404 | Calm page: "This page doesn't exist." + five real links + phone. **No joke, no illustration of a lost person.** | n/a | n/a | n/a |
| 500 | "Something on our side is not working. Your data is safe. Call us — [phone]." | n/a | n/a | n/a |

### A8.2 Portal screens

| Screen | Empty | Loading | Error | Success |
|---|---|---|---|---|
| Dashboard | The first-entry state, A4.1 — never a blank list | Skeleton: one plot card outline | "We can't load your plots right now. Your subscription is active." + Retry + phone | Content |
| Visit list | "Your first visit is scheduled for [date]." with the progress rail | 3 skeleton rows | Retry + phone | — |
| Report | n/a | Skeleton in document order: masthead → confirmation → grey-free image blocks | If media fails: "The photographs are still uploading. They usually appear within an hour of the visit." + a `Notify me when ready` button. **Never "Something went wrong".** | — |
| Report — processing | The real state for the first hours after a visit: confirmation and GPS present, photographs replaced by "Photographs are being prepared — usually ready within 24 hours" | — | — | Media arrives, opt-in notification fires |
| Family Circle | "Only you have access. Family members you invite can see reports without seeing prices." + Invite button | 2 skeleton rows | Retry | "Invitation sent to [contact]. It is valid for 14 days." |
| Invitation accept | — | — | Expired: "This invitation has expired. Ask [owner name] to send a new one." Revoked: same, without blame. | Lands directly on the most recent report — the payoff, immediately |
| Order one-off | Service list is never empty | Skeleton cards | Retry | "Request received. We'll confirm within one business day." Status = Pending, visible in the portal |
| Billing | n/a | Skeleton | "We can't reach billing. Nothing has changed on your subscription." | — |
| Cancellation | — | Refund calculating: inline skeleton on the amount only | "We couldn't calculate your refund automatically. Please call — [phone] — we'll do it with you and it won't affect your rights." | Amount, reference number, timing, and the door left open |
| Guest report `/r/` | — | Skeleton | Expired/revoked: "This link is no longer active. Ask the family member who sent it for a new one." Nothing about accounts, nothing about prices. | — |

### A8.3 The bad-news states — the ones nobody designs

These are full designed states, not toasts.

**(a) Visit postponed by weather.**
Where: dashboard notification strip, visit-list row, a dedicated card, plus a push/email if opted in.
Card contents, in order: `Visit postponed` chip in Olive (decorative Olive, Anthracite text) → the original date, struck through, and **the new date, larger** → one plain sentence of reason ("Heavy rain on 14 September. Cleaning in rain damages stone and gives a poor result.") → "Your subscription is unaffected — you still receive all 4 visits" → `Suggest a different date` and `Call us`.
Rule: **the new date must be present**. "Postponed, we'll be in touch" is the message that loses the client. If a new date is genuinely unknown, the copy is "We will confirm a new date by [specific date]" — a commitment with a deadline, never an open end.

**(b) Crew could not access the plot.**
This is the hardest one. The client paid, we went, we came back with nothing.
Contents: `Visit attempted` chip → date and time of arrival → **GPS confirmation that we were there** (this is the whole reason GPS exists — it turns a failure into proof of effort) → one photograph of the obstruction, chosen with care: a locked gate, a blocked path. **Never a photograph of a neighbouring grave.** → plain explanation → **"This visit does not count against your subscription"** stated explicitly and prominently → what we need from them ("the section is locked; if you have a contact at the cemetery office, tell us — otherwise we will resolve it and return") → `Call us` + `We'll arrange access` action.
Judgement: showing the GPS trace on a failed visit is counter-intuitive and correct. It is the difference between "they didn't go" and "they went and were stopped".

**(c) Client requests the guarantee re-visit.**
Entry from the report (owner/manager/member) or the guest link (guest).
Screen 1: "Tell us what's wrong" — free text + up to 3 photos.
Screen 2: confirmation — "We will return within 7 days at no cost." Names the person who will call. Gives a reference.
Portal after: the visit row gains a `Re-visit requested` chip; when scheduled it shows the date; the re-visit produces its own report, linked to the original as `Re-visit for [date]`, and **does not count against the subscription's visit quota**. That last rule needs to be stated on screen or the client will assume it does.

**(d) Payment overdue / subscription expiring.** Owner only, never Members, never the local contact. Calm, dated, with the exact consequence and a single action.

---

# PART B — UI implications of the structure

Only where structure forces the visual decision.

### B1. Breakpoints and grid

| Breakpoint | Range | Columns | Gutter | Margin | Max content |
|---|---|---|---|---|---|
| S (design first) | 375–599 | 4 | 16 | 20 | fluid |
| M | 600–1023 | 8 | 24 | 40 | fluid |
| L | 1024–1439 | 12 | 24 | 64 | 1120 |
| XL | 1440+ | 12 | 32 | auto | **1200**, centred |

Text measure is capped at **68 characters** regardless of breakpoint. On legal pages and the report, 60–65. Beyond that a 50-year-old loses the line return, which is the single most common readability failure on wide screens.

Vertical rhythm on an 8px base. Section padding: 56px at S, 80px at M, 112px at L/XL.

### B2. What collapses, and what does not

| Element | S (375) | M (768) | L/XL |
|---|---|---|---|
| Nav | Hamburger → full-screen panel | Full nav, 5 items | Full nav + utility |
| Pricing cards | Stacked, **Optimal first** | 3-up equal | 3-up, Optimal raised 12px |
| Inspection card | Stacked below a divider, distinct fill | Horizontal | Horizontal, full width |
| Calculator | Single column, result below controls | 2-col, result sticky | 2-col |
| Report annotations (sample page) | Numbered list below the document | Below | Side callouts |
| Portal nav | Bottom tab bar, 4 tabs | Bottom tab bar | 240px left sidebar |
| Report photos | 1-up, full-bleed | 2-up | 2-up, 720px document width |
| Family matrix table | **Horizontal scroll with the capability column frozen** — I am not converting it to cards; the value of a permission matrix is the comparison, and cards destroy it. A scroll affordance (fade + hint) appears on the right edge. | Full table | Full table |
| Footer | Single column, ordered by importance | 2×2 | 4 columns |
| Sticky action bar | Present | Hidden (header button is visible) | Hidden |

### B3. Touch targets and interaction sizing

- Minimum **44×44 px** for every interactive element, and **48px** for anything primary. Visual size may be smaller than the hit area (a 24px icon inside a 44px target).
- Minimum **8px** between adjacent targets; **12px** in the footer, where phone numbers, email and legal links sit close together and a mis-tap costs a lead.
- Slider thumbs: 28px visual, 44px hit area, and a numeric input alongside as the accessible alternative.
- Full-width primary buttons at S: 48px tall, 20px horizontal padding, label 17px.
- Table rows and list rows in the portal: 72px minimum, entire row is the target.
- Bottom tab bar: 56px + `env(safe-area-inset-bottom)`.

### B4. Typography scale (structural, not decorative)

Gloock has one weight. Hierarchy therefore comes from **size, measure and space** — and Cabin (labelled everywhere as *a substitute for Gill Sans*) carries all weight variation.

| Token | S | L | Face |
|---|---|---|---|
| Display / H1 | 34 | 52 | Gloock Regular |
| H2 | 26 | 36 | Gloock Regular |
| H3 | 20 | 24 | Cabin 600 |
| Body L | 18 | 19 | Cabin 400 |
| **Body (base)** | **17** | **18** | Cabin 400 |
| Small | 15 | 15 | Cabin 400 |
| Caption / legal | **14 floor** | 14 | Cabin 400 |

**Nothing below 14px anywhere in the product, including footnotes, captions and legal text.** The audience is 40–60. Line height 1.6 body, 1.7 legal, 1.15 display. Numerals tabular in every price, invoice and calculator readout.

### B5. Contrast and focus — hard rules

- Body text: Anthracite on Nude (9.61) or on Ivory (10.53).
- Links and accent text on light: **Deep Olive only** (5.49 / 6.01).
- Primary button on light: Deep Olive fill, Ivory label (6.01). On Anthracite: Nude fill, Anthracite label (9.61).
- **Olive never carries text at body size.** Its permitted uses: decorative fills, petals, dividers, low-opacity panels, and the logo tagline **at 16px or larger where it functions as a graphic element** — and even there I would restrict it to the footer and the hero, never as UI text.
- **Focus ring: 2px Deep Olive, 2px offset, on every focusable element, and it is never removed.** On an Anthracite ground the ring switches to Nude. `:focus-visible` semantics.
- Every icon that carries meaning has a text label or `aria-label`. No icon-only buttons in the portal except the header's phone and the tab bar (which has labels).

### B6. The header logo problem

There is no horizontal lock-up, and the vertical one is unusable in a 56px header. My proposal:

**Build a header-only horizontal lock-up from the existing vector assets.** Take the *logo mark* SVG, crop it to a tight bounding box (the 1080×1080 padding must be removed — this is a build task for the designer, one export), and set it left of the *wordmark* SVG, also tightly cropped. Optical spacing between them equal to the wordmark's cap height. **No tagline in the header** — at header scale it is 8–9px, illegible, and it is Olive, which fails contrast. The tagline lives in the footer, in the hero, and on print, at 16px+.

Sizing: mark 32px tall at S, 36px at M/L. Wordmark cap height aligned to the mark's optical centre. Total lock-up width ≈ 148px at S — which is why the mobile header centres the lock-up between two 44px targets: 44 + 148 + 44 = 236px, comfortable inside 375 minus 40px of margins.

**Colour version by ground** (this resolves the vanishing-hands defect):
- Header on Nude/Ivory (the normal case) → **the dark/mono lock-up**: mark in Anthracite, "Memory" in Anthracite, "Care" in Olive. Two-colour identity preserved, hands visible, no contrast failure. *Judgement: I am overriding the "Memory in Ivory" rule for the light header because Ivory-on-Nude is invisible — a 1.1 ratio. The brandbook rule assumes a dark or white ground; the header has neither.*
- Header over the hero if the hero is Anthracite → the full colour lock-up as specified.
- Footer (Anthracite ground) → full colour lock-up, with the tagline in Olive at 16px.
- Favicon / app icon / OG image → mark only, tightly cropped, on Anthracite.
- **Never** the colour lock-up on Nude. That is the defect, and the fix is a rule, not a redraw.

Minimum clear space: half the mark's height on all sides. Minimum mark size: 24px (below that the woven medallion turns to mud, and at favicon size we use a simplified single-path forget-me-not — one more export to request).

---

# PART C — Content slots and character budgets

For the writer. Counts are **characters including spaces**, in English, and assume **Armenian runs ~15% longer and Russian ~20% longer** — so every budget below already carries that headroom, and English drafts should aim at the lower end of each range. **Hard ceilings are marked "max"; exceeding them breaks the layout, not the taste.**

### C1. Global

| Slot | Budget | Notes |
|---|---|---|
| Nav item ×5 | 8–16 max | Must not wrap at 768 |
| Primary button label | 14–26 max | "Request a free consultation" = 29, too long for S at 17px — use "Free consultation" |
| Secondary button label | 10–22 max | |
| Footer tagline | fixed | `HONORING MEMORY, CARING FOR LOVED ONES` — no full stop, never edited |
| Footer legal line | 40–70 | |
| Meta title, per page | 50–60 max | **Must disambiguate from dementia care** — pair "MemoryCare" with "grave care" or "cemetery plot care" in every one |
| Meta description | 140–158 max | |
| OG title | 40–60 | |

### C2. Home

| # | Slot | Budget |
|---|---|---|
| 1 | Hero eyebrow | 24–42 |
| 1 | **H1** | **34–56 max** (3 lines at 34px on 375) |
| 1 | Hero subhead | 90–150 |
| 1 | Primary CTA / secondary CTA | 14–26 / 12–24 |
| 1a | Report card: date label / GPS chip / caption | 12–20 / 10–16 / 30–60 |
| 2 | Two-reasons card heading ×2 | 18–34 |
| 2 | Two-reasons card body ×2 | 90–160 |
| 3 | Step label ×3 | 6–14 |
| 3 | Step body ×3 | 60–110 |
| 4 | Method item heading ×4 | 12–26 |
| 4 | Method item body ×4 | 50–90 |
| 5 | Pricing card name / visits line / price / feature ×4 | 8–18 / 14–28 / fixed / 20–48 |
| 5 | "Most chosen" ribbon | 8–14 max |
| 6 | Family Circle H2 / body / bullets ×3 | 20–40 / 120–200 / 30–60 |
| 7 | Guarantee heading ×3 | 16–34 |
| 7 | Guarantee body ×3 | 70–130 |
| 8 | Person name / role / one-line bio ×2 | fixed / 10–24 / 60–110 |
| 9 | FAQ question ×6 | 30–70 |
| 9 | FAQ answer ×6 | 180–420 |
| 10 | Final CTA heading / body / button | 24–48 / 70–120 / 14–26 |

### C3. Pricing

| Slot | Budget |
|---|---|
| H1 / subhead / coverage line | 20–40 / 80–140 / 50–90 |
| Product name (EN) / Armenian original | 6–14 / fixed |
| Visit-count line | 14–28 |
| Price line | fixed — always `160,000 ֏ AMD / year` form: symbol **and** the word AMD |
| Feature line ×4 per card | 20–48 |
| Inspection badge / description / "no cleaning" line | 8–12 / 120–200 / 40–70 |
| Special band heading / body | 24–48 / 90–150 |
| Credit rule, short form | 90–150 |
| Credit table rows ×3 | 30–70 |
| Calculator heading / subline | 20–40 / 50–90 |
| Slider labels ×2 / tick labels ×3 | 10–20 / 6–18 |
| Result tier line / breakdown row ×4 / FX note | 16–34 / 24–52 / 40–70 |
| Ceiling state heading / body | 20–40 / 100–170 |
| Credit preview line | 70–120 |
| Calculator fine print | 90–160 |
| Pricing FAQ ×5 | 30–70 / 180–420 |

### C4. Other marketing pages

| Page | Slot | Budget |
|---|---|---|
| How it works | Step heading ×4 / body ×4 | 16–34 / 180–320 |
| | "What's included" item ×8 | 20–48 |
| | "What we don't do" item ×4 | 20–60 |
| | Weather & access paragraph | 200–380 |
| Sample report | Intro heading / body | 26–50 / 90–150 |
| | Annotation ×4 | 60–120 |
| | Link-preview explainer | 90–150 |
| Family Circle | H1 / definition | 18–36 / 100–170 |
| | Step ×3 | 60–110 |
| | Role name ×3 / role description ×3 | 6–14 / 50–100 |
| | Yerevan-relative block heading / body | 26–50 / 180–300 |
| | Privacy note | 120–200 |
| About | Section heading ×5 | 16–34 |
| | Paragraph ×5 | 250–500 |
| | Legal entity block lines | 20–60 each |
| Contacts | Person card: name / role / hours line | fixed / 10–24 / 40–80 (must include the UTC offset) |
| Legal ×4 | H1 / section heading / paragraph | 16–34 / 20–50 / 200–600 |
| 404 / 500 | Heading / body | 20–40 / 80–140 |

### C5. Portal

| Screen | Slot | Budget |
|---|---|---|
| First entry | Greeting / status heading / next-visit line | 12–28 / 20–40 / 24–46 |
| | Progress dot label ×4 | 8–20 max |
| | "What happens next" row ×3 | 60–110 |
| Dashboard | Plot card: identity / next-visit / plan | 16–40 / 20–40 / 8–18 |
| Visit list | Status chip ×5 | 8–18 max |
| | Row summary | 30–70 |
| **Report** | Masthead label / plot identity | 12–20 / 16–40 |
| | Confirmation heading / GPS chip / times line | 16–30 / 10–16 / 24–46 |
| | **Crew note** | **120–300** — the human voice of the product; the single most-read text in the company |
| | Work-performed item ×8 | 16–40 |
| | Photo caption ×6 | 24–60 |
| | Recommendation item ×4 | 30–80 |
| | Action labels ×3 | 10–24 |
| Share sheet | Explainer line / revoke label | 60–110 / 10–20 |
| Family Circle | Empty-state body / role chip ×4 | 90–150 / 6–12 |
| | Role description in the invite selector ×3 | 40–90 |
| Orders | Service card name / description ×n | 8–20 / 60–110 |
| Billing | Plan summary line / cancel link | 30–70 / 14–26 |
| Cancellation | Step heading ×4 / "what you lose" item ×3 / refund row ×5 | 20–40 / 30–70 / 20–50 |
| **Bad news** | Postponed: chip / reason / reassurance | 10–20 / 90–170 / 50–90 |
| | No access: chip / explanation / "doesn't count" line / ask | 12–22 / 120–220 / 40–70 / 90–150 |
| | Re-visit: confirmation heading / body | 20–40 / 100–170 |
| Errors | Every error heading / body | 20–40 max / 70–140 |
| Emails | Subject ×6 | 30–52 max (mobile clients truncate at ~55) |
| | Preheader ×6 | 60–90 |
| Notifications | Push title / body | 20–40 / 60–110 |
| **OG for `/r/`** | Title / description | fixed: `Visit report` + date / 40–70, **no plot identity, no photograph** |

---

# PART D — What I think is wrong or missing in the brief

Ordered by how expensive it is to fix late.

1. **Pro-rata refund has no defined basis.** By visits or by days? The screen, the policy page and the developer all need one answer. I recommend **by visits consumed**. Blocking issue for `/portal/billing/cancel/` and for the bank submission.
2. **Account ≠ beneficiary ≠ notification recipient is not in the data model.** The brief describes the split-payer case as central but specifies a three-field form and a single-user portal. Three contact records per plot, or Journey 3 is unbuildable. **Send this to the external developer before 20 September** — it is a schema decision, not a UI one.
3. **The plot has no identity model.** No cemetery, sector, row, coordinates, or name-on-the-monument field is specified anywhere, yet the report masthead, the guest link and the crew's own navigation all require it. Also needs an explicit owner choice about whether the deceased's name is displayed — that is a consent question, not a design one.
4. **Credit window conflict.** The brief says 60 days for both one-offs; the repo's project memory says 30 days for Inspection and 60 for Express. I have built to the brief (60/60). Someone must confirm, because it is printed on the pricing page and it is a commercial promise.
5. **The Express credit is a 40% first-year discount and nothing guards it.** 65,000 credited against 160,000 means the first year costs 95,000 — the strongest number we have, and also the most abusable. Needs a stated rule: once per client, or once per plot? I have designed for **once per plot**.
6. **No account-creation moment is specified.** The consultation form deliberately has no registration, payment is by transfer, and then the portal exists. The bridge is a welcome email with an activation token, and it needs to be designed and written. I have specified `/portal/activate/:token/`; someone needs to own the email.
7. **Ownership transfer is missing.** The payer of a memorial-care subscription is, statistically, someone thinking about mortality. If he dies, the family loses the account. Two-step transfer with verification on both sides.
8. **Share-link lifecycle is undefined.** Expiry, revocation, and whether a link survives cancellation. I have specified revocable, non-expiring by default, and dead on cancellation — confirm.
9. **The logo tagline is Olive text and Olive fails contrast.** In the mark it is a graphic and exempt; as a UI string at 14px it is a violation. My rule: tagline is 16px+ and decorative only. It never appears in the header.
10. **Third-party notification consent.** We will be messaging a person who never contacted us (the local contact in Yerevan). The checkbox in A4.10 is the minimum; someone should check whether Armenian data law wants more.
11. **The legal address is still a placeholder** and it gates the bank submission, the footer, the About page and the Contacts map. It is the oldest open item in this project and it is now on the critical path.
12. **"Special — by calculator" is contradictory.** Special is defined as calculator-priced, but the calculator's ceiling routes to Inspection and the brief says entry to Special is always through Inspection. I have resolved it as: the calculator prices Optimal and Maximum within the ceiling; above it, no price is shown and the route is Inspection. If Special is meant to have a self-serve price, that is a different design and I need to know.
