# MemoryCare — Final UX Specification

**Status:** agreed. This document supersedes the five round-one proposals and the
five round-two memos. Where they disagreed, the resolution is written here as a
statement, not as an argument.
**Author:** UX Architect, on behalf of the five-person team.
**Date:** 30.08.2026 · **Language:** English (source for HY / RU localisation).
**Scope:** the marketing site and the client portal.

---

## 0. How to read this, and what wins

Precedence, top to bottom. Anything lower that disagrees with anything higher is
wrong and must be changed, not debated:

1. `DECISIONS.md` and `DECISIONS-2.md` — owner rulings.
2. `BRIEF.md`.
3. This document.
4. `tokens.json`, `products.json`, `strings.en.json`, the component specs.

Three rules that govern the whole product and are repeated nowhere else:

- **The report is the product.** Everything on the marketing site exists to make
  a stranger believe the report is real; everything in the portal exists to
  deliver it without drama.
- **Invent nothing.** No testimonials, no counts, no years in business, no
  "trusted by N families", no competitor is named anywhere in any language. We
  are pre-launch with zero paying customers; guarantees and process are our only
  trust currency.
- **No QR code, no digital memory page, anywhere, in any tense.** Year-2 scope.
  It does not exist, not even as "coming soon".

---

## 1. The locked facts every screen is built on

Prices are AMD, identical for every client. Currency is always written with both
the symbol and the letters: `160,000 ֏ AMD`. Tiers cover a plot up to 16 m² and
up to 2 monuments.

| Product (English first, Armenian in parentheses on first mention per page) | Price | What it is | Band |
|---|---|---|---|
| **Inspection** (Զննում) | 20,000 ֏ AMD | One assessment visit: we locate the plot, record its condition, photo and video, and give a priced list of recommended work. **No cleaning is performed.** | One-off |
| **Express** (Էքսպրես խնամք) | 65,000 ֏ AMD | One full visit: deep cleaning of the whole plot and all monuments. Report, portal access. | One-off |
| **Optimal** (Օպտիմալ խնամք) | 160,000 ֏ AMD / year | **4 full visits, one in each season.** Marked *Our recommendation*. | Annual |
| **Maximum** (Մաքսիմում խնամք) | 200,000 ֏ AMD / year | **6 full visits** across the year. | Annual |
| **Special** (Հատուկ խնամք) | priced after an Inspection | Larger plot, more monuments, several family plots. Never a card, never a price. | Neither — a route |

Rules that must be visible in the interface:

- There are **two** annual subscriptions, Optimal and Maximum. Special is not a
  third card and never appears in a comparison row.
- Every visit is a **full visit**. The words *light*, *preventive*, *heavy*,
  *monthly*, *bestseller*, *most popular*, *tier 1*, *basic*, *premium* do not
  exist in any language.
- Optimal is marked **"Our recommendation"**. Never "Most chosen" — we have zero
  customers and it would be a claim about behaviour that has not happened.
- **Surcharges** (flat, identical for Optimal and Maximum): +10,000 ֏ AMD/year
  per m² above 16; +30,000 ֏ AMD/year per monument above 2. One-off Express:
  +2,500 ֏ AMD per m², +7,500 ֏ AMD per monument.
- **Credit:** on signing an annual subscription, one already-paid one-off is
  credited in full — either Inspection (20,000) **or** Express (65,000), never
  both; if both were paid, the larger. Window **60 days** from paying for the
  one-off. It fires only at the moment the subscription is signed. There is no
  credit between one-off services. **The credit is attached to the plot**, once
  per plot. Express is 65,000 ֏ AMD every time; there is no reduced repeat price.
- **First-year figure, shown publicly:** `160,000 − 65,000 = 95,000 ֏ AMD for the
  first year, and 160,000 ֏ AMD in each year after that.` See §11.4 for the
  binding wording constraints.
- **A subscription year is twelve months from the signing date.** Seasons are a
  promise inside those twelve months, worded "one visit in each season". If no
  suitable weather window occurred for the winter visit, that visit is **added**
  to spring; four visits are guaranteed regardless. Renewal runs against the
  client's own anniversary, not a company calendar.
- **No auto-charge.** A renewal offer goes out 30 days before the anniversary and
  a single reminder 7 days before; the client acts. A card is never silently
  charged a year later.
- **Two public service promises, identical in all six places they appear, and
  nobody may soften or sharpen them locally:**
  - `We call or write within one business day.` — with Yerevan business hours and
    the UTC offset stated next to it, so a client in Los Angeles can convert it.
  - `Your report arrives within 48 hours of the visit.`
- **Three guarantees**, named and numeric: free repeat visit within 7 days if the
  client is unhappy with a report; liability for damage; pro-rata refund on
  cancellation, computed on the amount actually paid.

---

## 2. Sitemap

Locale is in the URL from day one — `/en/`, `/hy/`, `/ru/` — even though English
ships first. `/` redirects to `/en/`. Language is switched manually and persists
in a cookie; a shared link is never silently redirected to another locale.

### 2.1 Marketing site

```
/en/                                Home
/en/pricing/                        Pricing — two bands, calculator, guarantees
/en/how-it-works/                   How it works
/en/sample-report/                  Sample report — the product demo
/en/family-circle/                  Family Circle — the differentiator
/en/guarantees/                     MemoryCare Guarantees, full text
/en/about/                          About the company (bank requirement)
/en/contacts/                       Contacts
/en/consultation/                   Consultation request (page + modal twin)
/en/consultation/thank-you/         Confirmation (conversion target)
/en/pay/                            Payment options
/en/pay/bank-transfer/              Invoice and wire instructions
/en/pay/thank-you/                  Payment initiated / awaiting transfer
/en/legal/                          Index of the four documents
/en/legal/privacy/                  Privacy policy
/en/legal/refund/                   Refund policy — the pro-rata rule lives here
/en/legal/terms/                    Terms of service
/en/legal/limitations/              Service limitations and restrictions
/en/404/   /en/500/   /sitemap.xml   /robots.txt
```

Stable anchors used by nav, footer, calculator and ads:
`#inspection` `#express` `#optimal` `#maximum` `#special` `#calculator`
`#guarantees` `#faq`.

**Navigation model.** Primary nav is five items and never more: Pricing · How it
works · Sample report · Family Circle · About. Contacts lives in the footer and
behind the header phone target. Utility slot, right of nav: language switcher
(`ՀԱՅ · ENG · РУС`, native script), `Sign in` as a text link, then
`Request a consultation` as the primary button.

Footer on every page (bank requirement): Company (About, Contacts, Guarantees) ·
Services (the five products, each anchoring into Pricing) · Legal (the four
documents) · Contact block: both founders with `tel:` links, `info@memorycare.am`,
the legal-address placeholder visibly marked as a placeholder, and the line
`MemoryCare LLC, Yerevan, Armenia · © 2026`.

### 2.2 Portal

```
/portal/login/                      Sign in — magic link and password, side by side
/portal/login/check-email/          Interstitial
/portal/activate/:token/            First-time activation from the welcome email
/portal/                            Dashboard — the list of plots
/portal/plots/:plotId/              Plot overview
/portal/plots/:plotId/visits/       Visit list, scheduled and completed
/portal/plots/:plotId/documents/    Invoices, contract, condition record
/portal/plots/:plotId/settings/     Plot identity, name display, local contact
/portal/visits/:visitId/            Report screen (authenticated)
/portal/visits/:visitId/revisit/    Guarantee re-visit request
/portal/family/                     Family Circle roster
/portal/family/invite/              Send an invitation
/portal/family/:memberId/           Member detail: role, plot scope, remove
/portal/invite/:token/              Invitation acceptance (unauthenticated entry)
/portal/orders/new/                 Order a one-off service
/portal/orders/:orderId/            Order status
/portal/billing/                    Subscription, payments, invoices
/portal/billing/change/             Change plan or plot parameters
/portal/billing/transfer/           Transfer ownership of a plot
/portal/billing/cancel/             Cancellation with the pro-rata refund
/portal/profile/                    Name, contacts, language
/portal/profile/notifications/      Reminder opt-in and recipient routing
/portal/support/                    Message us / call us
```

### 2.3 Public, outside the portal

```
/r/:shareToken/                     Guest report view — no login, no prices, no upsell
/r/:shareToken/expired/             Revoked link
/r/:shareToken/tell-us/             The one permitted guest action (see §13.3)
```

The guest report deliberately sits on a short root path. It is pasted into
WhatsApp and read on a five-inch screen by a seventy-year-old.
`memorycare.am/r/8fk2wq` is a link a person can retype; anything under `/portal`
implies a login wall and gets ignored.

---

## 3. Object model and role model

### 3.1 The object model is the Plot

A client can hold several plots — Special exists precisely for that — and the
unit a person thinks in is "my mother's grave", not "my Optimal plan". Every
portal URL is scoped to a plot; the dashboard is a list of plots, not a list of
invoices. If the schema is scoped to the subscription, the second plot breaks the
whole information architecture and it is rebuilt in month three.

Enough for a developer to design a schema:

```
account
  id · name · email · phone_e164 · locale · created_at
  (an account is a person who can sign in; it is not a customer record)

plot                                     ← the central object
  id
  owner_account_id                       → account (exactly one, always)
  cemetery                               enum/reference, free entry allowed
  sector · row                           free text, may be empty at signup
  coordinates {lat, lng}                 recorded by the crew on the first visit
  display_name                           e.g. "the Hakobyan family"
  deceased_name                          nullable
  name_display  ∈ {family_name, full_name, none}   default family_name
                                         see §13.4 — full_name is OFF by default
  area_m2 · monuments_count              drive every surcharge
  notes
  created_at

contact                                  ← three per plot is normal, not an edge case
  id · plot_id
  kind ∈ {owner, local_contact, family}
  name · phone_e164 · channel ∈ {whatsapp, sms, call, email}
  third_party_consent_at                 required before we message a local contact
  account_id                             nullable — a local contact has no account

membership                               ← Family Circle
  id · plot_id · account_id
  role ∈ {owner, manager, member}        guest is not a membership, see share_link
  invited_by · invited_at · accepted_at · removed_at

subscription
  id · plot_id
  product ∈ {optimal, maximum}
  signed_at                              the year runs 12 months from here
  ends_at = signed_at + 12 months
  visits_total                           4 or 6
  list_price_amd
  amount_paid_amd                        ← the refund basis. Never the list price.
  credit_applied {source_order_id, amount_amd}   nullable, at most one, per plot
  status ∈ {active, cancelled, expired}
  renewal_offer_sent_at · renewal_reminder_sent_at
  cancelled_at · refund_amd

order                                    ← one-off purchases: Inspection, Express, extra work
  id · plot_id · product · amount_amd · paid_at
  credit_expires_at = paid_at + 60 days
  credited_into_subscription_id          nullable

visit
  id · plot_id · subscription_id (nullable for one-offs) · order_id (nullable)
  planned_window {from, to}              a month range until it is dated
  scheduled_for · status ∈ {scheduled, completed, rescheduled, no_access,
                            preparing, revisit_requested}
  arrived_at · departed_at
  gps {lat, lng, recorded_at}
  counts_against_quota  boolean          false for a re-visit and for a no-access visit
  parent_visit_id                        set on a guarantee re-visit

report                                   ← one per visit; the product
  id · visit_id · published_at
  crew_note                              120–320 characters, the one first-person voice
  work_performed[]                       ticked items
  media[] {kind: photo|video, group: arrival|after|obstruction, ratio, order}
  recommendations[] {text, price_amd}    price visible only to owner and manager
  pdf_url

share_link
  token                                  ≥128 bits of entropy
  report_id · created_by · created_at · revoked_at
  (non-expiring by default; revocable from the sheet that created it)

invoice · payment                        AMD amounts, reference string, method
```

Two schema facts that are easy to get wrong and expensive to fix:

- **Account ≠ beneficiary ≠ notification recipient.** Three separate contact
  records per plot. A single `user.phone` makes the Los Angeles journey
  unbuildable.
- **The credit is recorded as a payment against the subscription, not as a price
  change.** `list_price_amd` stays 160,000 and `amount_paid_amd` becomes 95,000.
  The refund arithmetic reads `amount_paid_amd`; if the credit is modelled as a
  discounted price, the refund overpays. See §12.

### 3.2 The role model

Four roles. Three are memberships; the fourth is a link.

| Role | Who this is, concretely | Auth |
|---|---|---|
| **Owner** | The payer. Exactly one per plot, always. | Full account |
| **Family manager** | A trusted relative — usually the eldest sibling or the one in Yerevan. Sees everything about care and money-in-context, but cannot spend. | Full account, by invitation |
| **Family member** | The aunt, the cousins. Sees care, never sees money. The default suggested role on the invite screen. | Full account, by invitation |
| **Guest** | Someone holding a `/r/` link. Half of all report opens. | None, ever |
| *Local contact* | Not a role and not an account: a person in Yerevan (typically the mother) who receives reports as plain links and may meet the crew. Recorded on the plot, messaged only after an explicit third-party consent. | None, ever |

Data values: `owner | manager | member`. UI strings: Owner · Family manager ·
Family member · Guest. Never "payer", "subscriber", "viewer", "beneficiary" on
screen.

---

## 4. Journeys

### 4.1 Anna, 47, Glendale — the diaspora buyer

| # | Stage | Where | What she does | What must be true |
|---|---|---|---|---|
| 1 | Trigger | Search or Instagram, 23:40 local | Taps a link | Title and meta disambiguate from dementia care; LCP under 2.5 s on 4G at 360px |
| 2 | Eight-second judgement | `/en/` hero | Sees a *report*, with a date and GPS, not our emblem | The report preview is real HTML, cropped by the fold on purpose |
| 3 | "Is this real?" | `/en/sample-report/` | Opens the full sample | It is the actual component with placeholder media, not a screenshot in a laptop mock-up |
| 4 | "What does it cost — for *me*?" | `/en/pricing/#calculator` | Moves two sliders | No email gate before the number. Ever. One price list, stated in words next to the sliders. |
| 5 | "Who are they?" | `/en/about/`, footer | Checks names, Armenian numbers, legal entity | Two named humans with real mobile numbers; `MemoryCare LLC`; `info@memorycare.am` |
| 6 | "What if it is bad?" | `#guarantees` | Reads three guarantees | Guarantees on Home, on Pricing, and on their own page |
| 7 | Action | Consultation modal | Name, +1 number, cemetery, consent, submits | The US number is accepted without her thinking about it |
| 8 | Gap | WhatsApp | Hayk writes on WhatsApp first, calls only if she prefers | An unannounced +374 call at an odd hour is not answered and is increasingly silenced as suspected fraud |
| 9 | Pay | `/en/pay/bank-transfer/` | Wires from a US bank | Instructions on screen and as a PDF her bank will accept; AMD amount, indicative USD marked approximate |
| 10 | Silence | Portal, email | 1–5 days while the transfer travels | `Awaiting payment` state exists, plus a day-3 message from a named human. This is where the first refund request would otherwise be born. |
| 11 | Activation | Welcome email → `/portal/activate/:token/` | Sets a password or uses a magic link | Lands on the **first-entry screen**, never an empty table |
| 12 | **The doubt fortnight** | Portal | Waits for the first visit | The screen must not look empty; it must look scheduled. This is the highest-risk moment in the product. |
| 13 | Payoff | Report notification → report → share | Opens it, forwards it to the family group | Share is a first-class button; the link preview carries no photograph |

### 4.2 Armen, 54, Yerevan — the local premium buyer

| # | Stage | Where | What he does | What must be true |
|---|---|---|---|---|
| 1 | Trigger | Word of mouth, mid-day, forty seconds | Arrives on a phone | The same page and the same copy as Anna. No local/diaspora fork. |
| 2 | Scan | Home | Skips to pricing | Pricing is one tap from the mobile action bar |
| 3 | Compare | `/en/pricing/` | Optimal against Maximum on one axis: 4 visits or 6 | Two cards, one variable. Visit count is the largest thing on the card after the price. |
| 4 | Verify method | `/en/how-it-works/` | Looks for the equipment and the chemistry | Steam, pressure washer, vacuum, professional chemistry — named concretely |
| 5 | Objection | — | "I could do this myself in one Saturday" | The counter is time and repetition: four visits, seasonal, scheduled, without him. Never a guilt construction. |
| 6 | Action | He taps the phone number, not the form | `tel:` is live in the header, the action bar, the footer and every contact block |
| 7 | Convert | Phone → bank transfer | Handoff to the portal identical to Anna's |

Consequence for structure: **every home-page block must be comprehensible on its
own**, because he reads three of them and skips four. No block may depend on the
block above it for meaning.

### 4.3 Vahe, 41, Los Angeles — buying for his mother in Yerevan

The case the brief calls central. **He pays. She is the one who cares.** She has a
smartphone, uses WhatsApp, and will never create an account.

1. **Consultation.** Vahe fills three fields. The optional disclosure
   `Add a note or a family contact` holds the free-text note and two fields for a
   family member in Yerevan. One tap for the minority who need it, zero cost for
   everyone else.
2. **Onboarding call.** Hayk records the plot identity — cemetery, sector, row,
   the name on the monument — and the local contact, including her channel and
   her consent to be messaged. The name-display choice is made here and defaults
   to family name only.
3. **Payment.** Vahe wires from the US. Invoice in AMD, indicative USD marked
   approximate, `MemoryCare LLC` on the document.
4. **Activation.** Vahe activates and sees one plot with his mother's plot
   identity, and the first visit as a dated window.
5. **Routing.** Siranush is a *local contact*, not a member. She receives the
   day-before reminder and every report as a plain `/r/` link on WhatsApp. She
   never sees a login screen, never sees a price, and **never receives a renewal,
   payment or upgrade message** — that is a rule in the string file, not a
   preference. Sending "renew your subscription" to a grieving 72-year-old who
   did not pay is a brand-ending message.
6. **The share loop.** Vahe opens the report, taps Share, pastes the link into the
   family group. Twelve relatives open the guest view. None of them sees a price,
   a plan name, a next-visit date or a button.
7. **Escalation.** If Siranush thinks something is wrong, the guest report carries
   exactly one non-commercial action:
   `Something is not right with this report` → three fields → files a guarantee
   re-visit against that visit and notifies Vahe. Support, never sales.
8. **Mortality.** Vahe is the sort of person who thinks about it. Ownership
   transfer exists (§9.3), and if the owner has died the family calls a number and
   we move the subscription against documents. Care continues on the schedule
   already paid for while that is settled.

---

## 5. Global chrome and responsive rules

### 5.1 Breakpoints — one set, for everyone

| Name | Min width | Columns | Gutter | Margin | What changes here |
|---|---|---|---|---|---|
| `base` | **360** | 4 | 16 | 20 | **QA floor.** Design frames may be drawn at 375, but nothing ships until it passes at 360×640 |
| `sm` | 600 | 8 | 24 | 40 | Cards go 2-up; footer 2×2 |
| `md` | 900 | 8 | 24 | 40 | Primary nav expands; hamburger retires |
| `lg` | 1200 | 12 | 24 | auto, max 1200 | Verification rail becomes a right column; calculator becomes two columns |
| `xl` | 1440 | 12 | 32 | auto | More air. No new layout. |

Media queries are min-width only. Text measure is capped at 68 characters
everywhere, 60–65 on legal pages and inside a report.

### 5.2 What changes at each breakpoint

| Element | 360 | 600 | 900 | 1200 | 1440 |
|---|---|---|---|---|---|
| Header | 56px: menu · lock-up · call | 56px, same | **72px**, full nav + language + CTA | 72px | 72px, wider gutters |
| Logo | mark 28px + live `MemoryCare` | same | mark 32px + live text | same | same |
| Language switcher | pinned at the bottom of the drawer | drawer | in the header | header | header |
| Mobile action bar | present, 64px + safe area | present | **absent** — the header CTA is visible | absent | absent |
| One-off band | stacked | 2-up | 2-up | 2-up | 2-up |
| Annual band | stacked, Optimal first | 2-up | 2-up | 2-up | 2-up |
| Calculator | one column, result directly under the sliders | one column | one column | two columns, result 42% and sticky within the card | same |
| Report photographs | 1-up, full-bleed | 1-up | 2-up | 2-up, document max 720px | same |
| Verification rail | horizontal ruled strip under its content | strip | strip | right column, 222px | right column |
| Sample-report annotations | numbered list below the document | below | below | side callouts | side callouts |
| Permission matrix | four stacked role cards, each a can/cannot list; the table is a link | table | table | table | table |
| Portal navigation | bottom tab bar, 56px + safe area, four tabs | tab bar | **240px left sidebar** | sidebar | sidebar |
| Footer | one column, ordered by importance | 2×2 | 4 columns | 4 columns | 4 columns |
| Section padding | 56px | 72px | 88px | 112px | 112px |

Vertical rhythm is an 8px base at every width.

### 5.3 Header

Ivory bar with a permanent 1px hairline rule at the bottom — permanent, not
appearing on scroll, because a 1.1 tonal step without a rule reads as a printing
error. There is no `backdrop-filter` and no shadow.

- The header composition is the **mark plus live text** `MemoryCare` at every
  width — the drawn wordmark is never used in the header. Live text is
  selectable, translatable, sharp at any pixel density and needs no new asset.
  "Memory" takes the primary text colour, "Care" takes **Deep Olive** — never
  Olive, which is unreadable as text at any size.
- Display face, 24px minimum, never wrapping, never `MC`, never `MEMORYCARE`.
  Below 360px the mark drops and the word stays: for a visitor who arrived from an
  English search that returns dementia care, the name is the one thing that may
  never be dropped.
- **The tagline never appears in the header.**
- 360–899: `[menu 44×44] … [lock-up centred] … [call 44×44 → tel:]`. No CTA button
  in the bar; it lives in the action bar.
- 900+: lock-up left · five nav items · language switcher · `Sign in` ·
  `Request a consultation`.

### 5.4 Mobile action bar

Present from 360 to 899 only. 64px + `env(safe-area-inset-bottom)`, Ivory fill,
top hairline. Appears at `scrollY > 320`. One 44px call target plus one
full-remaining-width primary button, `Request a consultation`.

It is **suppressed**: on `/en/consultation/`, on the four legal pages, while any
form field has focus, on every report and guest-report route, and on `/en/pricing/`
while the calculator result panel is in the viewport. **One fixed bar at the
bottom of the screen, ever.** Two pinned bars on a 640px viewport is a quarter of
the screen and is not a state that may exist.

### 5.5 Touch, focus, motion

- 44×44 minimum for anything interactive, 48px tall for anything primary; visual
  size may be smaller than the hit area. 8px minimum between adjacent targets,
  12px in the footer where a mis-tap costs a lead.
- Focus ring: 2px Deep Olive at 2px offset on every focusable element, never
  removed; on an Anthracite ground it switches to Nude. `:focus-visible`.
- Portal list rows 72px minimum, whole row is the target.
- **Nothing on this site moves on its own.** No autoplay, no carousel, no
  count-up on any number, no rotation of the brand mark, no parallax. Loading is
  a 2px Deep Olive arc or a fading opacity pulse on a label — never a spinning
  logo. Every transition respects `prefers-reduced-motion`.

### 5.6 Type and colour constraints that bind layout

- Body 16px minimum on mobile, 17px desktop; **14px is the floor for any text
  that carries meaning**; 13px exists only for a decorative uppercase overline.
  Nothing in the product is smaller than 13px, in any medium, including the
  tagline and the legal pages.
- The display face is never set below 24px. Below that, headings are the text
  face at 600.
- Radius: `0` for bands, photographs, the report sheet, dividers and the plot
  diagram; `2px` for buttons, inputs, cards, badges, modals, sheets, toasts;
  `full` only for the slider thumb, the petal bullet and avatar discs.
- **No shadows.** Elevation is a ground change plus a 1px hairline. The single
  exception is a scrim behind a modal, drawer, bottom sheet or lightbox.
- **Olive never carries text and no text is ever legible on Olive.** Accent text,
  links and primary button fills are Deep Olive. On Anthracite, text is Nude or
  Ivory and the primary button is a Nude fill with an Anthracite label.
- **The error colour `#8C3A2E` appears in exactly two situations: form validation
  and payment failure.** It has no success or warning sibling — success and
  attention are carried by a word, a glyph and a rule weight. It is invisible on
  Anthracite (1.57), which is why **the consultation form may never sit on a dark
  band**, and it is forbidden outright on any screen that shows a photograph of a
  grave, in the report PDF, as a button fill, as a status badge, on 404 and 500,
  and anywhere near the 60-day credit window.
- Prices are set with tabular figures and the currency glyph is emitted in its own
  element with its own font binding, so a missing `֏` can never break a price. The
  letters `AMD` are always printed next to the symbol.
- Every mock, exported page and PDF carries the line: *"Cabin is used as a free
  substitute for Gill Sans (commercial Monotype). It is not the brand text face."*

---

### 5.7 Above the fold at 360 — every route, in one place

The budget is 640 minus the 56px header minus browser chrome: **about 500px**.
Anything not listed here is deliberately below the fold.

| Route | What must be visible without scrolling at 360×640 |
|---|---|
| `/en/` | Overline · H1 (48 characters maximum) · standfirst (105 characters) · the verification strip · the primary CTA and its support line · the **metadata strip of the report preview**, with the image cropped by the fold on purpose |
| `/en/pricing/` | H1 · subhead · `One price list — the same in Yerevan and in Los Angeles.` · the top of the fork. The first price met is a one-off price. |
| `/en/how-it-works/` | H1 · one line of standfirst · step 1 of the timeline, complete |
| `/en/sample-report/` | The one-line header · the report masthead · the confirmation block with the date. The GPS block sits immediately under the fold and pulls the scroll. |
| `/en/family-circle/` | H1 · the one-sentence definition · the top of role card 1 |
| `/en/guarantees/` | H1 · guarantee 1 complete, with its remedy |
| `/en/about/` | H1 · the first paragraph · the top of the founders block |
| `/en/contacts/` | Both founder cards with `tel:` targets. Nothing above them. |
| `/en/consultation/` | The form heading · the support line · the Name field and the top of the contact field |
| `/en/pay/` | Both payment paths as two headed choices, neither cropped |
| `/en/legal/*` | H1 · the last-updated date · the table of contents, collapsed |
| `/r/:shareToken/` | Masthead · `The visit took place` · the date. A guest must know the visit happened before scrolling. |
| `/portal/` first entry | Greeting · the status card including **the first-visit window** · the top of the progress rail |
| `/portal/` dashboard | The greeting and the whole of plot card 1 |
| `/portal/plots/:id/visits/` | The scheduled group heading and its first row |
| `/portal/visits/:id/` | Masthead · confirmation with the date and status · the top of the GPS block |
| `/portal/family/` | The roster heading, the owner row and the invite button |
| `/portal/billing/` | The current plan card in full, including the anniversary line |
| `/portal/billing/cancel/` step 3 | The refund table down to and including the rounded amount |

---

## 6. Marketing pages, block by block

"Above the fold at 360" means the first paint on a 360×640 viewport, which is
640 minus the 56px header, minus browser chrome — roughly **500px of usable
height**. Every fold claim below has been counted against that number.

### 6.1 Home — `/en/`

| # | Block | Ground | Contents, in order |
|---|---|---|---|
| 1 | **Hero / proof** | Nude | Overline (what we do, disambiguating) → H1 → standfirst → one-line verification strip → primary CTA + support line → the **report preview**, cropped by the fold |
| 2 | **Why people use this** | Nude | One block, outcome first, both reasons named in one line of body text and neither ranked. Never two cards addressing "you are far away" and "you have no time" — that is diaspora-only copy addressed to one of two readers on the same page. |
| 3 | **What a visit is** | Nude | Numbered three-step strip: Plan → Visit → Report. Olive line icon, two-word label, one line each. |
| 4 | **Method** | Nude | Equipment and chemistry, four items in a 2×2 grid at 360. Answers "why not do it myself". |
| 5 | **The report** | Nude, with the sample as an Ivory sheet | A cropped real report sheet + three annotations + `See a full report` → `/en/sample-report/` |
| 6 | **Family Circle** | **Anthracite** | Definition, three bullets, avatar row, link. The differentiator gets a full-width dark band, not a bullet. |
| 7 | **Guarantees** | Nude | Three items: name, number, remedy. Directly after How-it-works/method material and before anything commercial, because that is when the risk question actually fires. |
| 8 | **Honesty panel** | Nude, bordered | "We started in 2026. We have no reviews yet." At body size or a step above — never small print. Styling it as a disclaimer inverts its job. |
| 9 | **Pricing teaser** | Nude | The four named products as **four lines with prices**, not cards, plus the Special line, plus `One price list — the same in Yerevan and in Los Angeles.` and a link to `/en/pricing/`. No calculator on Home. |
| 10 | **Founders** | Nude | Two people: name, role, `tel:`, `wa.me`, 1:1 portrait placeholder. A published founder's mobile number outweighs seventy anonymous reviews and costs nothing. |
| 11 | **FAQ** | Nude | Six items, accordion, first open. Includes what happens if we cannot reach the plot. No competitor is named. |
| 12 | **Closing CTA** | **Anthracite**, running into the footer | Heading, one line, Nude-fill button with an Anthracite label. **The consultation form itself is not on this band** — the error colour is invisible there. |
| 13 | Footer | Anthracite | As §2.1 |

**Above the fold at 360:** overline, H1 (hard maximum **48 characters** in
English, two lines at 32px), standfirst (**105 characters**, three lines), the
verification strip, the primary CTA, and the **top of the report preview**. The
preview is cropped by the fold deliberately, and what survives the crop is the
**metadata strip, not the image** — `14 September 2026 · Tokhmakh · Plot 12` and
the `GPS confirmed` chip. A cropped photograph proves nothing; a date and a
coordinate do.

Two dark bands on this page, and only two: Family Circle and the closing band.
The hero is light — a dark hero costs fold height, forces a second header
variant, and spends the page's scarcest asset on the screen where the tone rule is
strictest.

### 6.2 Pricing — `/en/pricing/`

Order, top to bottom:

1. **Page header** — H1, one line of subhead, the coverage line (up to 16 m² and
   up to 2 monuments), and `One price list — the same in Yerevan and in Los
   Angeles.`
2. **The fork** — two doors, stacked below 600: `I want to know what it needs` →
   Inspection · `I want it looked after` → the annual band. Heading
   `Two ways to start`. The doors are never written in the reader's first person
   and never name their absence.
3. **Band A — One-off services.** Inspection 20,000 ֏ AMD · Express 65,000 ֏ AMD.
   Two cards, sunken ground, 2-up from 600, band label `One-off services`, and an
   overline on each card reading `One-off · not a subscription`. **Prices are set
   at the same type size as the annual prices** — shrinking a price is what makes
   a product read as cheap. No "/ year" line. Each card carries one short line:
   `Credited toward an annual subscription signed within 60 days.`
4. **The credit block**, immediately beneath Band A, always visible, never behind
   a tooltip and never a footnote. Heading `How a one-off payment is credited`,
   then the worked example with the arithmetic, then four bullets: the 60-day
   window; one amount only, the larger of the two; it applies at signature and
   never between one-off services; Express is 65,000 ֏ AMD every time. Plus
   `One credit for each plot.`
5. **Band B — Annual subscriptions.** Optimal and Maximum, **two cards**, raised,
   2-up from 600, stacked below with **Optimal first** — on a phone there is no
   centre, and first beats middle. Card anatomy: badge (Optimal only) → product
   name with the Armenian original beneath → visit count as the largest element
   after the price → price `160,000 ֏ AMD / year` → four feature lines → CTA.
   Optimal carries a 2px Deep Olive border, a `Our recommendation` badge in Deep
   Olive with an Ivory label placed **above the product name**, and is the **only
   card in the band with a primary button**; Maximum's CTA is secondary. Three
   consistent signals — border, badge, button weight — and none of them costs the
   button language.
6. **Guarantees** — the same component as Home, here beneath the bands and above
   the calculator.
7. **Calculator** — §11. Ivory sheet on the Nude ground, full width.
8. **Special** — one ruled line beneath the calculator. No card, no price:
   *"Larger plot, several family plots, or a case that does not fit? We price it
   after an Inspection."* → `Start with an Inspection`. A priceless card in a row
   of published prices is where a hesitant reader stops.
9. **Payment reality** — bank transfer now, card payment when the bank enables it,
   **no date promised**.
10. **Pricing FAQ** — five items, including "Do prices differ for diaspora
    clients?" answered plainly: no.
11. Closing CTA band + footer.

**Above the fold at 360:** H1, subhead, the one-price-list line, and the top of
the fork. The first price a visitor sees is a one-off price, which is the correct
order of magnitude to meet first.

### 6.3 How it works — `/en/how-it-works/`

1. Page header.
2. **Timeline**, four steps, vertical at 360 with a 2px Olive rail: Consultation
   → Subscription and schedule → The visit → The report. Number in the display
   face, heading, two or three sentences, one 3:2 placeholder each.
3. **What a full visit includes** — six to eight checklist items, two columns
   from 900.
4. **What we do not do** — the same visual weight, four items, linking to
   `/en/legal/limitations/`. Naming the limits raises trust more than any
   adjective, and the bank's "legal restrictions" requirement needs a home people
   actually read.
5. **Weather and access** — the honest paragraph: seasons, rain, locked sections,
   disputed access, and what happens then. States plainly that no visit is
   silently skipped, and that a winter visit with no suitable weather window is
   added to spring.
6. **The first visit** — *"On the first visit the crew locates the plot and
   records its GPS point, and then does the full work, so every later report can
   be compared with the first."* It is never described as a survey; only
   Inspection is a survey.
7. Report preview strip → `/en/sample-report/`.
8. CTA + footer.

### 6.4 Sample report — `/en/sample-report/`

This page renders the **actual report component** with labelled placeholder media
inside the marketing chrome. It must never be a picture of a report.

1. Short header: what arrives after every visit, and when (48 hours).
2. **The report sheet**, full width at 360, max 720px centred from 1200, in the
   exact block order of §7.5.
3. **Annotation layer** — side callouts from 1200 explaining GPS verification,
   timestamps, the video and the condition notes; at 360 they become a numbered
   list **below** the document, never overlaying it.
4. **"How the link looks when you send it to family"** — a rendered message-preview
   card demonstrating the OG rule: mark, `Visit report`, date. No photograph, no
   cemetery, no name. This block demonstrates the product and pre-empts the
   privacy question at the same time.
5. CTA + footer.

### 6.5 Family Circle — `/en/family-circle/`

1. Header and a one-sentence definition.
2. **How it works** — three steps: you invite → they get their own access → they
   see reports and can ask for work.
3. **The roles** — four stacked role cards at 360, each with a plain can/cannot
   list; the full matrix is a link and a table from 900. A horizontally scrolling
   frozen-column table is not an acceptable mobile fallback for a 55-year-old.
4. **The Yerevan relative** — stated publicly: the person who meets the crew does
   not need an account and never sees a price.
5. **Privacy note** — who can see what, how to remove someone, that removal is
   immediate, and that a shared link can be revoked.
6. CTA + footer.

### 6.6 Guarantees — `/en/guarantees/`

The full text of the three guarantees, each with its remedy and its honest limit,
then the pro-rata arithmetic worked through with a number, then links to the four
legal documents. The `GuaranteesBlock` component appears in four places — Home,
Pricing, this page, and the portal visit list — and is one component.

### 6.7 About — `/en/about/`

What MemoryCare is, in two paragraphs → why it exists → the two founders with
direct numbers and 1:1 portrait placeholders → how we work: method, verification,
equipment → the legal-entity block: `MemoryCare LLC`, registration number
placeholder, legal address placeholder, `info@memorycare.am`, both phones → the
honesty line about 2026 → CTA + footer.

**No History, Mission, Values or News pages.** Those are the failure the brief
names.

### 6.8 Contacts — `/en/contacts/`

Two person cards with `tel:`, `wa.me` and role → email → **working hours in
Yerevan time with the UTC offset spelled out**, because "9:00–18:00" alone is
useless to a reader in Glendale → a short form (name, contact, message, consent)
→ the legal-entity block → a map slot, marked as a placeholder pending the legal
address.

### 6.9 Consultation — `/en/consultation/` and the modal

One component in two containers. Field spec in §10.1. The page version adds a
right rail from 1200 — the three guarantees, `No payment now. No account
needed.`, and both phone numbers for people who would rather call; at 360 that
rail goes **below** the form. The form heading and the first field are above the
fold at 360. The form never sits on a dark band.

### 6.10 Payment — `/en/pay/`

Two paths presented as equals rather than as one working and one broken:
**Bank transfer (available now)** and **Card payment (when the bank enables it —
no date promised)**. Transfer path: choose the product → confirm the plot
parameters → generate the invoice → wire instructions on screen and as a PDF →
`Tell us when you have sent it`. Showing a disabled card button with no
explanation reads as a broken site; labelling it honestly reads as a young
company, which is what we are.

### 6.11 Legal pages ×4

One template: H1 → last-updated date → table of contents (sticky from 1200,
accordion at 360) → body at 60–65 characters per line, 17px minimum, line height
1.7 → contact block. Read by a bank officer and by a worried 55-year-old; both
need it legible. The mobile action bar is suppressed here.

---

## 7. Portal, screen by screen

Portal chrome: header 56px with the mark, the plot switcher when there is more
than one plot, and an avatar menu. Bottom tab bar below 900 — **Plots · Visits ·
Family · Account**, 56px + safe-area inset — becoming a 240px left sidebar from
900. A *visit* is the event; a *report* is the record of it; the portal navigates
by visit.

### 7.1 First entry after payment — `/portal/` with zero visits

The most important screen in the product. The client has paid a large sum to a
company they have never met and there is nothing to show. **The screen must not
look empty; it must look scheduled.**

1. Greeting: `Welcome, {name}.`
2. **Status card**, Ivory on Nude, full width: plot identity → `Subscription
   active` → **the first-visit window as the largest text on the card** ("First
   visit: 12–16 September") → one line naming who will come and that the crew
   records a GPS point on arrival.
3. **Progress rail** — four labelled dots: Subscription active ✓ · Plot located ·
   First visit · Report. Dot 1 filled, dot 2 ringed, 3–4 outline. This converts an
   empty state into a timeline with a position, which is the whole psychological
   job of the screen.
4. **What happens next** — three rows with times: within two days we confirm the
   plot coordinates; the day before the visit you get a reminder if you asked for
   one; **within 48 hours of the visit, your report.**
5. **Two actions**: `Add a family member` (primary — it gives her something to do,
   and it has the highest retention value of anything on this screen) and
   `See a sample report` (secondary).
6. Support row: `Hayk — +374 93 154 108`, call and WhatsApp targets.

**Above the fold at 360:** items 1, 2 and the top of 3. If the client must scroll
to learn when the first visit is, this screen has failed.

### 7.2 Dashboard with plots — `/portal/`

Greeting → one `PlotCard` per plot (identity, cemetery, next visit, last-report
thumbnail on a neutral crop, plan name; the whole card is one target, 88px
minimum) → `Add another plot` → a notification strip only when something needs
attention: a postponement, a payment, a subscription approaching its anniversary.

### 7.3 Plot overview — `/portal/plots/:plotId/`

Plot identity and cemetery → next visit → last report → the care team → quick
links to Visits, Documents, Family, Plot settings. The plan and price line —
`160,000 ֏ AMD / year · renews 14 September 2027` — is present from day one for
the owner and the manager, so the renewal price is never a surprise a year later.
It is absent for members.

### 7.4 Visit list — `/portal/plots/:plotId/visits/`

Two groups. **Scheduled** at the top, visually distinct, with a dashed Olive
inline-start rule; **completed** below with a solid Deep Olive rule. Each row:
date, status word, one-line summary, chevron; 72px minimum, the whole row is the
target. No filter chips at 360 — filtering a list of at most nine items a year is
a needless control. The `GuaranteesBlock` sits permanently at the foot of this
screen.

### 7.5 Report screen — `/portal/visits/:visitId/`

The block order is fixed, and the same document renders for the guest with blocks
removed server-side. **Confirmation first, photographs after.**

| # | Block | Contents | Guest |
|---|---|---|---|
| 1 | **Masthead** | Mark · `Visit report` · plot identity · cemetery | yes |
| 2 | **Confirmation** | `The visit took place` · the date, large · crew arrival and departure times | yes |
| 3 | **GPS confirmation** | **Its own block, never a chip.** The plot diagram, the coordinates in tabular type, the caption *"This is where the crew stood. It is how you know they went."*, and `Show on map` as an outbound link to the viewer's own map application. We serve no map tiles and there is never a red pin — the marker is the Olive five-petal glyph. | yes |
| 4 | **Work performed** | Ticked list, maximum eight, first four plus `Show all` at 360 | yes |
| 5 | **Photographs** | Group `On arrival`, then group `After the work`, labelled above each group, chronological. One image per row at 360, 4:3, tap for full screen with pinch-zoom, caption below each. An optional `Compare` pair may follow the two groups. **Never a before/after slider, and never the after-image as the opening image** — that is the advertising register the brief forbids. | yes |
| 6 | **Video** | One 20–40 s clip, poster frame, muted, plays inline, never autoplays | yes |
| 7 | **The crew's note** | 120–320 characters, first person, plain language. The single most-read text the company writes. | yes |
| 8 | **Recommended work** | Observations, then prices, on a changed ground after a full-width rule. `Nothing here happens unless you ask for it.` | **text no, prices no** — removed server-side |
| 9 | **Documents** | Report PDF, A4, identical block order, **never any price in any variant**, so one file serves owner, member and guest | yes |
| 10 | **Actions** | `Share` · `Order additional work` · `Request a re-visit` | text link only |
| 11 | **Next visit** | The date of the next scheduled visit | **no** |

At 360 a slim 48px bar sticks to the bottom of the report carrying **`Share` and
nothing else**. The global action bar is suppressed here. The page `<title>` is
`Visit report — {date}` and nothing more; a plot identity in a browser tab is
visible over a shoulder and in any screen share.

### 7.6 Share sheet

A bottom sheet at 360. In order: one line explaining what the recipient will see —
this matters, because the owner needs to know she is not sending prices to her
aunt → the link in a read-only field with `Copy` → WhatsApp · Viber · Email → a
divider → **`Link is active · Revoke`** with the creation date and a confirm step.
Revocation must live in the sheet that creates the link; a permanent unrevocable
link to a photograph of a family grave is not acceptable.

### 7.7 Family Circle — `/portal/family/`

Roster of members: initial disc, name, role, `invited` or `active`, and which
plots they can see. The owner row is pinned first and cannot be removed.
`Invite a family member` is primary. Beneath it, a collapsed `What each role can
do` accordion holding the matrix from §9.

`/portal/family/invite/`: name (optional) → phone or email (required) → **role as
three radio cards with a one-line consequence each, never a dropdown** — a
dropdown hides the consequence of the choice → plot scope checkboxes when there is
more than one plot → optional message, 200 characters → `Send invitation`. The
confirmation states exactly what the invitee will receive and that the invitation
is valid for 14 days.

`/portal/invite/:token/`: brand block → "{Name} invited you to the Family Circle
for {plot}" → what this role can do → set a password or continue with a magic link
→ accept. Acceptance lands **directly on the most recent report** — the payoff,
immediately.

### 7.8 Order a one-off service — `/portal/orders/new/`

Plot selector when there is more than one → service cards with prices, including
the recommended work from the last report, pre-selectable → date preference:
as soon as possible, or a month → notes → a price summary computed with the
calculator's own arithmetic, including plot surcharges → `Send request`. It is a
request, not a checkout; card acquiring is not live, and the button's helper line
says so.

### 7.9 Billing — `/portal/billing/`

Current plan card: product, price, plot parameters, the twelve-month period, the
anniversary date and `We will offer renewal 30 days before this date. Nothing is
charged automatically.` → payment method → invoices with PDF downloads →
`Change plan` → `Transfer ownership of this plot` → `Cancel subscription` as a
calm Deep Olive **text link** at the bottom. Hiding cancellation is both a dark
pattern and a bank-requirement violation; making it a shouting red button is
equally wrong for this brand.

### 7.10 Plot settings — `/portal/plots/:plotId/settings/`

Plot identity (cemetery, sector, row) → **how the plot is named in reports**, the
setting described in §13.4 → local contact (name, phone, channel, third-party
consent) → notes for the crew.

### 7.11 Profile and notifications — `/portal/profile/notifications/`

A per-plot matrix of event against recipient, plus a `Local contact` block with
the explicit consent checkbox *"This person has agreed to receive messages from
us."* Third-party consent is a real legal exposure and the checkbox is not
decorative.

| Event | Owner | Family manager | Family member | Local contact |
|---|---|---|---|---|
| Day-before reminder | opt-in, off by default | opt-in | opt-in | **on by default when a local contact exists** |
| Visit completed / report ready | on | on | on | on, as a plain `/r/` link |
| Visit moved | on | on | on | **on, always** — she may be planning to attend |
| Could not reach the plot | on | on | on | on |
| Payment, invoice | on | never | never | **never** |
| Renewal offer, price, upgrade | on | never | never | **never** |

The last row is a hard rule in the string file: **no renewal, price, payment or
upgrade string may ever be addressed to a family member or a local contact.**

### 7.12 Sign in — `/portal/login/`

Magic link **and** password offered on the same screen, not a magic-link-only
flow: a magic link that lands in a corporate spam filter locks a client who has
just paid 160,000 ֏ out of the thing they paid for, at the worst possible moment.
`Send it again` also offers WhatsApp delivery. Both founders' phone numbers are on
this screen.

---

## 8. Every state of every screen

Global rules, before the tables:

- **No emoji anywhere in the product.** Never `Oops`, `Something went wrong`,
  `Error`, `Invalid`, `Failed`, `Required field`, and never an exclamation mark in
  an error.
- **Every error names a next step and a human.** `Call Hayk — +374 93 154 108` is
  a valid recovery path and is often the correct one for this audience.
- **Skeletons, not spinners**, for content with a known shape. Spinners only for
  an action the user just initiated.
- **Photographs never load into a black box.** The placeholder fill is Nude.
- Success is a word and a glyph. There is no success colour.
- Page- and screen-level error panels take a fixed shape — what happened, whose
  fault it is, what to do, plus an optional phone line — and the component has no
  icon or illustration property at all, so neither can be reached for under
  deadline. Field-level errors keep a 16px glyph, because colour may never be the
  only signal.

### 8.1 Marketing

| Screen | Default | Empty | Loading | Error | Success |
|---|---|---|---|---|---|
| Home | As §6.1 | n/a | Above-fold text paints first; every media slot reserves its aspect ratio so nothing shifts | Report-preview media fails → Nude placeholder plus its caption; the page is still complete | n/a |
| Pricing | Two bands | n/a | Sliders render at their defaults with no fetch | A URL config out of range clamps silently to the nearest valid value | The configuration is carried into the consultation form and echoed back |
| Calculator | Optimal, 16 m², 2 monuments | n/a | none required | Typed value out of range: the field corrects on blur with a plain note. **Not an error, no red** | — |
| Calculator at the ceiling | — | — | — | **Not an error.** The result panel is *replaced*: heading, one paragraph, `Book an Inspection — 20,000 ֏ AMD` primary and `Request a consultation` secondary | — |
| Sample report | The component | n/a | Skeleton in the exact document shape | Placeholder blocks with captions | n/a |
| Consultation form | Untouched fields, no error styling | — | Button reads `Sending…`, the form locks, the button is **never disabled before submission** | Field errors below their fields plus a summary at the top with `role="alert"`; network failure keeps every value and offers WhatsApp and a phone number | The form is replaced in place by a confirmation; the standalone page also redirects to `/en/consultation/thank-you/` |
| 404 | `This page does not exist.` plus five real links and a phone number. **No joke, no illustration of a lost person.** | — | — | — | — |
| 500 | `Something on our side is not working. Your data is safe.` plus a phone number | — | — | — | — |

### 8.2 Portal

| Screen | Default | Empty | Loading | Error | Success |
|---|---|---|---|---|---|
| Dashboard | Plot cards | **The first-entry screen, §7.1 — never a blank list** | One plot-card skeleton | `We cannot load your plots right now. Your subscription is active.` + Retry + phone | — |
| Visit list | Two groups | `Your first visit is scheduled for {window}.` with the progress rail | Three skeleton rows | Retry + phone | — |
| Report | §7.5 | n/a | Skeleton in document order: masthead → confirmation → GPS → image blocks | Media fails: `Some photographs are still uploading. The rest of the report is complete.` plus `Notify me when they are ready` | — |
| Report, being prepared | The real state in the hours after a visit: confirmation and GPS present, photographs replaced by `Report being prepared` | — | — | — | Media arrives; the opt-in notification fires |
| Share sheet | §7.6 | — | — | Copy failed → the link stays selectable as text | `Link copied.` |
| Family Circle | Roster | `Only you have access. Family members you invite can see reports without seeing prices.` + Invite | Two skeleton rows | Retry | `Invitation sent to {contact}. It is valid for 14 days.` |
| Invitation accept | — | — | — | Expired: `This invitation has expired. Ask {owner} to send a new one.` Revoked: the same, without blame. | Lands on the most recent report |
| Order one-off | Service cards | never empty | Skeleton cards | Retry + phone | `Request received. We will confirm within one business day.` Status `Pending`, visible in the portal |
| Billing | Plan card | — | Skeleton | `We cannot reach billing. Nothing has changed on your subscription.` | — |
| Cancellation | §12 | — | Inline skeleton on the refund amount only | `We could not calculate your refund automatically. Please call us and we will do it with you — it does not affect your rights.` | Amount, reference, timing, and the door left open |
| Sign in | Both methods | — | `Sending…` | Wrong password, expired link, locked out, session expired — each with its own plain sentence | — |
| Guest report `/r/` | §13.3 | — | Skeleton | Expired or revoked: `This link is no longer active. The person who sent it can share it again. Nothing has been deleted — the report still exists.` **No sign-up prompt, no price, no account prompt.** | — |
| Payment | — | — | — | **Card declined:** `The payment did not go through. Your card was not charged.` Three routes: try again, pay by transfer, call Hayk. An inline panel, never a modal and never a toast — a failed payment is a screen. | `Payment received.` |
| Bank transfer | `Awaiting payment` | — | — | **Not an error, no red:** `We have not received your transfer yet. Transfers from abroad usually take two to five working days. Nothing is needed from you.` Day-3 message from a named human; day-7 message repeating the bank details. | — |
| Renewal payment failed | — | — | — | `We could not take this year's payment. Your subscription and your reports are unaffected and nothing has been cancelled.` | — |

### 8.3 The bad-news states

These are fully designed screens with the same budget as a report, not toasts.
None of them carries the error colour: they are reports of something that
happened, not faults of the client.

**(a) Visit moved — `rescheduled`.**
Appears in the dashboard strip, the visit row, a dedicated card, and a push or
email if opted in. Order: status word `Visit moved` → the original date, struck
through, and **the new date, larger** → one plain sentence of reason, never a
euphemism: *"Heavy rain on 14 September. Cleaning in rain damages stone and gives
a poor result."* → `Your subscription is unaffected — you still receive all four
visits.` → `Suggest a different date` and `Call us`.
**The new date must be present.** "Postponed, we will be in touch" is the message
that loses the client. If a date is genuinely unknown, the copy is *"We will
confirm a new date by {date}"* — a commitment with a deadline, never an open end.

**(b) Could not reach the plot — `no-access`.**
The hardest one: the client paid, we went, we came back with nothing. Order:
status word `Could not reach the plot` → the date and the arrival time → **the
GPS block, in full** — this is the entire reason GPS exists, because it turns a
failure into proof of effort → one photograph of the obstruction, chosen with
care: a locked gate, a blocked path, **never a photograph of a neighbouring
grave** → the plain reason, from a fixed set the operator picks → **`This visit
does not come out of your subscription. Your subscription still covers all {n}
visits.`**, stated explicitly and prominently → what we need from them, if
anything → `Call Hayk` and `Suggest a different date`.
Showing a GPS trace on a failed visit is counter-intuitive and correct: it is the
difference between "they did not go" and "they went and were stopped".

**(c) Guarantee re-visit — `revisit-requested`.**
Entry from the report (owner, manager, member) or from the guest link (guest,
without an account). Screen 1: what is wrong, free text plus up to three photos,
HEIC accepted. Screen 2: `We will return within 7 days at no cost.`, the name of
the person who will call, and a reference. Afterwards the visit row carries
`Repeat visit requested`; when scheduled it shows the date; the re-visit produces
its **own report linked to the original**, and **does not count against the
subscription's visit quota** — which must be stated on screen, or the client will
assume it does.

**(d) Subscription approaching its anniversary.**
Owner only. Never a member, never a local contact. A dated, calm offer 30 days
before and one reminder 7 days before, with the exact price, a one-tap `Renew`
and an equally visible `Do not renew`. **Nothing is ever charged automatically.**

---

## 9. Family Circle: the permission matrix

### 9.1 The matrix

| Capability | Owner | Family manager | Family member | Guest (link) |
|---|:--:|:--:|:--:|:--:|
| View a report: photographs, video, GPS | ✅ | ✅ | ✅ | ✅ single report only |
| View the visit schedule | ✅ | ✅ | ✅ | ❌ |
| See the next-visit date | ✅ | ✅ | ✅ | ❌ |
| Download the report PDF | ✅ | ✅ | ✅ | ✅ |
| Share a report by link | ✅ | ✅ | ✅ | ❌ |
| Revoke a share link | ✅ any | own links | own links | ❌ |
| See prices anywhere in the portal | ✅ | ✅ | ❌ | ❌ |
| See recommended work **with prices** | ✅ | ✅ | ❌ | ❌ |
| Order a one-off service | ✅ | request → owner approves | ❌ | ❌ |
| Approve anything that carries a charge | ✅ | ❌ | ❌ | ❌ |
| Request a guarantee re-visit | ✅ | ✅ | ✅ | ✅ as a message |
| Reschedule a visit | ✅ | ✅ | ❌ | ❌ |
| Change or upgrade the subscription | ✅ | ❌ | ❌ | ❌ |
| Cancel the subscription | ✅ | ❌ | ❌ | ❌ |
| View invoices and payment details | ✅ | ❌ | ❌ | ❌ |
| Invite someone | ✅ any role | Family member only | ❌ | ❌ |
| Remove someone | ✅ | ❌ | ❌ | ❌ |
| Edit plot identity and crew notes | ✅ | ✅ | ❌ | ❌ |
| **Change how the plot is named in reports** | ✅ | ❌ | ❌ | ❌ |
| Set the local contact and reminders | ✅ | ✅ | own only | ❌ |
| Receive renewal, price or payment messages | ✅ | ❌ | ❌ | ❌ |
| **Transfer ownership** | ✅ | ❌ | ❌ | ❌ |
| **Accept a transfer of ownership** | — | ✅ | ✅ | ❌ |
| Read past reports after cancellation | ✅ | ✅ | ✅ | ✅ existing links |

### 9.2 The four rules that fall out of the table

1. **A family member never sees money.** Not the plan name, not a price, not the
   renewal date, not an invoice. This is the role for the aunt and the cousins and
   it is the default suggested role on the invite screen.
2. **A family manager can spend nothing without the owner.** A manager's order
   becomes a request that lands on the owner's dashboard as a decision. That is
   what makes it safe to hand a relative real control.
3. **Only the owner cancels, transfers, or changes how the deceased is named.**
   One person owns the money, always; and the name is a consent decision.
4. **Past reports stay readable forever, including after cancellation** — for the
   owner, the manager, the member and anyone holding a link that was already
   shared. Read-only: no new visits, no renewal prompt, no upsell, no price on
   those screens. Access to reports about a family member's grave is not a SaaS
   feature to be switched off.

### 9.3 Ownership transfer

It exists because the payer of a memorial-care subscription is, statistically, a
person who is thinking about mortality. The register is administrative and calm.
**No condolence copy** — we do not know why the transfer is happening and guessing
is worse than not asking.

Entry: `Transfer ownership of this plot`, in Billing, with the helper line *"The
owner is the person who pays and who can change or cancel the subscription. There
is one owner, and it can be changed."*

1. **Choose.** Who should take over — someone already in the Family Circle, or an
   email address we will invite. Optional note. `Continue` / `Keep ownership`.
2. **Confirm, with what changes stated plainly.** `{name}` becomes the owner and
   can change or cancel the subscription; invoices and payment requests go to
   `{name}`; **you become a family manager** — you see every report and can ask
   for work, but cannot change the subscription; the plot, its GPS point and every
   past report stay exactly as they are. Nothing changes until `{name}` accepts.
   `Send the transfer request` / `Go back`.
3. **Pending.** `Waiting for {name} to accept.` The request is open for 14 days.
   Until they accept, nothing has changed and you are still the owner.
   `Send the request again` / `Cancel the transfer`.
4. **Accepted** — both parties are emailed; the roster updates; the old owner is
   now a family manager. **Declined** — nothing has changed; you can ask someone
   else or leave it.

Email to the person taking over states what they inherit, that nothing is charged
to them today, when the next payment falls due, and that the request expires on
its own in 14 days.

**If the owner has died** — a page, findable from Contacts and from the Family
Circle screen: call `+374 55 315 323` and we move the subscription to another
member of the family, against a document confirming the death and proof of
relationship, because we cannot hand over a family's records on a phone call
alone. **Care of the plot does not stop while this is settled: the visits continue
on the schedule already paid for.** That last sentence is an operational
commitment as much as a copy decision.

---

## 10. Forms

Rules for every form in the product:

- Validation on **blur**, never on keystroke; once a field is already in error it
  re-validates on keystroke, so a person watching themselves fix it sees it clear.
- The error message renders **below** its field, at 14px, in the error colour,
  with the field border going 2px inset in the same colour and a 16px glyph.
  Colour is never the only signal — roughly 8% of a male 40–60 audience is
  colour-deficient.
- On submit failure, focus jumps to the first invalid field and a summary appears
  at the top of the form with `role="alert"` linking to each field.
- **Never disable the submit button before submission.** A disabled button with no
  explanation is the most common accessible-form failure. The button goes to
  `Sending…` and the form locks after the press.
- Every input is 16px or larger, or iOS zooms on focus.
- **No form ever sits on an Anthracite band**, because the error colour is
  invisible there (1.57).
- Values are preserved through every failure, including a network failure.
- No CAPTCHA. Spam is handled server-side.

### 10.1 Consultation request — the primary conversion

| Field | Type | Required | Rules | Error message |
|---|---|:--:|---|---|
| Name | text | ✅ | 2–60 characters, any script — Armenian, Cyrillic, Latin | `Please enter your name.` |
| Phone or email | one field, auto-detected | ✅ | Leading `+` or a digit → phone with a country selector; otherwise email. E.164 for phone. | `Please give us one way to reach you.` / `This does not look like a phone number or an email address.` + `Please check the number and try again.` / `Please include the country code, for example +374, +1 or +33.` |
| City or cemetery | combobox, free entry always accepted | ✅ | Suggestions plus `Not sure`, which is a valid answer | `Please tell us roughly where the plot is.` |
| `Add a note or a family contact` | one disclosure holding a textarea and two optional fields (name, phone of a family member in Yerevan) | ❌ | 0–500 characters, counter from 400. Prompt text: *"For example: the best hours to call you, or who else in the family we should speak to."* | `Keep it under 500 characters.` |
| Consent | checkbox | ✅ | One line with a link: *"I agree to MemoryCare contacting me about this request."* | `Please confirm we may contact you.` |
| — | hidden | — | `calc_config` (tier, area, monuments, computed price), `utm_*`, `page_path`, `locale` | — |

Three visible fields, one disclosure, one checkbox. **Preferred contact time is
cut** — we guess it wrong more often than right and it is answered better in the
first ten seconds of the call.

**International phone handling**, because this is exactly where forms fail a
diaspora audience:

- One `<input type="tel">` with `inputmode="tel"` and `autocomplete="tel"`,
  preceded by a country selector at 44×44 minimum showing the **dial code and the
  ISO code as text** (`+374 AM`) — never a flag alone; flags are political and
  unreadable at 20px. Searchable in three scripts.
- Default country by IP, **always visibly overridable**, and never re-guessed
  after the user has changed it.
- Accept and normalise `+1 818 555 0142`, `(818) 555-0142`, `818.555.0142`,
  `+33 6 12 34 56 78`, `093154108`. Store E.164, display formatted per country.
- **Do not block on paste.** People paste from their contacts with invisible
  characters; strip and normalise silently.
- If the number cannot be parsed and the user submits a second time, **accept it
  and flag the lead for manual review**. A lost lead costs 160,000 ֏; a malformed
  number costs one minute of Hayk's time.
- `This number is on WhatsApp` is checked by default for any non-`+374` number,
  because that is how the diaspora actually communicates.

**On success**, in place, without a page change on the modal: what happens, when,
and in terms she can convert — *"We will call or write within one business day,
Yerevan time (UTC+4)."* — plus **"Hayk will write to you on WhatsApp from
+374 93 154 108 first, and call only if you prefer."**, both direct numbers, and,
if a calculator configuration was attached, it is echoed back:
*"You configured: 24 m², 3 monuments, Optimal — 270,000 ֏ AMD / year."*

### 10.2 The other forms — deltas only

- **Contact** (`/en/contacts/`): name ✅, phone or email ✅, message ✅ (minimum 10
  characters), consent ✅.
- **Invitation**: phone or email ✅, role ✅ (default Family member), plot scope ✅
  when there is more than one plot, name ❌, message ❌ 200 characters.
  `{email} already has access to this plot.` is a real validation case.
- **Guarantee re-visit**: the visit reference pre-filled and read-only, what was
  wrong ✅ 20–1000 characters, up to three photographs ❌ (10 MB each, **HEIC
  accepted** — the audience is on iPhones), preferred window ❌. The confirmation
  states the 7-day guarantee and gives a **name**, not only a ticket number.
- **Guest report feedback** — the only interactive element on `/r/`: name ✅,
  phone or email ✅, what is wrong ✅. Three fields, no consent theatre, no
  account, no price, nothing about signing up.
- **Local contact block**: name, phone, channel, plus the explicit third-party
  consent checkbox. We are about to message a person who never contacted us.
- **Cancellation**: §12.

---

## 11. The calculator

**Purpose, restated because it drives every decision here: to show a client in Los
Angeles that the price is the same for them as for anyone.** It is a trust
instrument that happens to do arithmetic. It lives on `/en/pricing/#calculator`
and nowhere else — two live calculators double the maintenance of the one
component whose arithmetic can embarrass us and split the measurement of the
highest-value interaction on the site.

### 11.1 Anatomy at 360, top to bottom

1. Heading, plus `One price list — the same in Yerevan and in Los Angeles.`
2. **Mode**: the default is subscription mode, **showing both Optimal and
   Maximum simultaneously**, not a toggle between them — the whole architecture is
   "one variable, two values", and a control that hides one of the two values
   defeats it. Beneath them, a text link: `Or price a one-off Express visit`,
   which switches the calculator to one-off mode.
3. **Slider 1 — plot area.** Label left, **value right in a numeric field the
   user can also type into**. Sliders alone are unusable with a 55-year-old's
   thumb on a 360px screen; the number field is the accessible escape hatch and it
   is not optional. Range 4–100 m², step 1, **default 16**. The track shows Olive
   at 30% for the included range and Deep Olive above 16, so the surcharge is
   visible as geometry before it is read as a number. Thumb 28px visual, 44px hit
   area. Tick labels: `16 m² included` at its true position, `50`, `100`.
4. **Slider 2 — monuments.** Range 1–10, step 1, **default 2**, same
   construction, tick label `2 included`.
5. **Two permanently visible surcharge lines** under the sliders — the annual
   rates. Nothing goes behind an info icon. The Express surcharge line lives
   inside the Express row, where it applies.
6. **Result**, two rows in subscription mode:
   - `Optimal — 4 full visits` · `160,000 ֏ AMD / year`
   - `Maximum — 6 full visits` · `200,000 ֏ AMD / year`
   with the breakdown beneath, rendering only non-zero rows:
   `Base (up to 16 m², 2 monuments) — 160,000 ֏ AMD` · `+8 m² above 16 —
   +80,000 ֏ AMD` · `+1 monument above 2 — +30,000 ֏ AMD` ·
   `Total — 270,000 ֏ AMD / year`.
   Then an indicative reference line, marked approximate with its rate date:
   `≈ $690 · charged in AMD`. No live FX for launch.
7. **Actions**: `Request a consultation` (primary, full width, 48px) and
   `What is included in a full visit?` (text link).
8. Fine print: the price covers the plot as configured; the final figure is
   confirmed after the Inspection.

At 1200 the block becomes two columns — controls 58%, result 42%, the result panel
sticky **within the card**. It is never pinned to the viewport: a pinned result
bar plus the action bar is 168px of fixed chrome on a 640px screen, and the user
cannot see the tick labels and the total at the same time.

### 11.2 Behaviour

- Live recalculation during the drag. The track fill follows the thumb. **The
  number snaps. There is no count-up, ever** — a price that rolls like a slot
  machine is exactly the wrong register for this purchase, and it is the one
  animation on this site a 55-year-old reads as a trick. `aria-live="polite"`
  announces the total on release, not during the drag.
- Debounce 120 ms on the typed field.
- **All state is in the URL**: `?tier=optimal&area=24&monuments=3`. The
  configuration is shareable, survives back-navigation, and lets Hayk send a
  client the exact number they discussed. It is also carried into the consultation
  form as hidden fields and echoed back in the confirmation.
- Keyboard: arrows ±1, PageUp/PageDown ±10, Home/End to the ends. `role="slider"`
  with `aria-valuenow` and `aria-valuetext` ("24 square metres").
- **Ceiling — 100 m² or 10 monuments.** The thumb stops and the result panel is
  *replaced*, not annotated: a heading, one paragraph, `Book an Inspection —
  20,000 ֏ AMD` primary, `Request a consultation` secondary. Entry to Special is
  always through Inspection. **Reaching the ceiling is a normal outcome, not an
  error**: no red, no warning glyph, and the copy never implies the other prices
  were improper.
- **No email gate, no "reveal your price", no lead capture before the number.**
  Any of those destroy the block's only purpose.

### 11.3 One-off (Express) mode

The same two sliders with the one-off surcharges (+2,500 ֏ AMD per m², +7,500 ֏
AMD per monument). The result reads `65,000 ֏ AMD — one visit`, recomputed with
surcharges. A third row then appears — **only in this mode, never in the default
state** — carrying the first-year arithmetic.

### 11.4 The 95,000 line and its wording constraints

**Where it appears — four places, and nowhere else:**

1. In the **calculator**, one-off mode only, as the third result row, recomputed
   with that visitor's own surcharges. Split as a label and a value so it fits at
   360: `If you take Optimal within 60 days` /
   `160,000 − 65,000 = 95,000 ֏ AMD for your first year`.
2. On the **pricing page**, inside the credit block beneath the one-off band, in
   body type at the size of the sentences around it: *"Worked example: an Express
   visit is 65,000 ֏ AMD. If you then sign Optimal, the first year is
   160,000 − 65,000 = 95,000 ֏ AMD, and 160,000 ֏ AMD in each year after that."*
3. In the **portal**, after a one-off has been paid, on the plot overview, as a
   dated fact: *"The 65,000 ֏ AMD you paid is credited against an annual
   subscription until {date}. Optimal would be 95,000 ֏ AMD for the first year and
   160,000 ֏ AMD after that."* It disappears when the window closes, replaced by
   one neutral sentence stating the standard prices.
4. In the **written quote** sent after the consultation call, with the same
   arithmetic and the same sentence.

**Never:** the hero, the Optimal card, the Express card's price line, a badge, a
meta description, an advertisement, the sticky bar, the footer.

**Six wording rules, all enforceable by the string linter:**

1. **Always show the subtraction, never only the result.** Arithmetic reads as a
   rule; a bare 95,000 reads as a price somebody set for you.
2. **Always name the mechanism in the same sentence** — an amount you have
   already paid comes off. The money is not given away; it is transferred.
3. **Always state the second year in the same sentence** — "and 160,000 ֏ AMD in
   each year after that". This is the single most important guard: it turns 95,000
   from a price into a one-time consequence, and it is what stops the renewal
   conversation a year later from going badly.
4. **Forbidden words:** save, saving, discount, off (used alone), deal, offer,
   special, only, just, instead of, was/now, `%`. Internally too — "a 40% first
   year discount" is exactly the vocabulary that reaches a card label three weeks
   later.
5. **No visual discount grammar:** no strike-through on 160,000 anywhere ever, no
   colour on the 95,000, no larger type, no badge, no ribbon, no countdown timer,
   no scarcity styling as the 60-day date approaches, and never the error colour
   near it.
6. **Full currency form every time:** `95,000 ֏ AMD`.

**Four things that must be true elsewhere, or the figure devalues the 160,000:**
160,000 ֏ AMD is the only number on the Optimal card; the calculator's default
state is subscription mode showing 160,000; no screen ever shows 95,000 and
160,000 as two options for the same product at the same visual weight — they are a
sequence, not a choice; and the portal shows
`160,000 ֏ AMD / year · renews {date}` from day one.

---

## 12. Cancellation and the pro-rata refund

Cancellation must be completable without telephoning us. The bank requires it and
so does the guarantee.

### 12.1 The arithmetic

```
refund = amount_actually_paid × (visits_not_performed ÷ visits_total)
         rounded UP to the nearest 100 ֏, in the client's favour
```

- **The base is what the client actually paid, never the list price.** A client
  who paid 95,000 ֏ AMD after an Express credit and has had one of four visits
  receives `95,000 × 3/4 = 71,250 → 71,300 ֏ AMD`. Computed from 160,000 the same
  client would receive 120,000 — more than we took.
- **The basis is visits, not days.** The client can count visits himself, so the
  number is never disputed. Work already performed is already paid for, and a
  client who has had one of four visits is never told he consumed 27% of a year.
- Maximum divides by six and produces a fraction on almost every cancellation.
  The rounding rule is not optional.
- **There is no cap on the refund.** The guarantee only sells if it is
  unconditional.
- A re-visit and a no-access visit never count as performed.

### 12.2 The flow — `/portal/billing/cancel/`

Four steps, one screen each, with a visible `Step n of 4` and an escape of equal
weight on every step.

1. **Reason** — five options plus free text, **all optional**, `Skip` visible.
2. **What you will lose** — a plain list: the remaining visits with their
   scheduled windows, which family members lose access, and — stated explicitly —
   **`Your past reports stay available to you and to your family. They do not go
   anywhere.`** No guilt copy, no "are you sure?".
3. **Your refund — the arithmetic, shown before the confirmation, as arithmetic
   and not as a single figure:**

   | | |
   |---|---|
   | What you paid for this year | 95,000 ֏ AMD |
   | Visits in your plan | 4 |
   | Visits completed | 1 |
   | Visits not performed | 3 |
   | 95,000 × 3 ÷ 4 | 71,250 ֏ AMD |
   | Rounded up | **71,300 ֏ AMD** |
   | How it is returned | to the account the payment came from |
   | When | within {n} working days |

   Beneath the table, one line: a completed visit is not refunded, because the
   work has been done.
4. **Confirm** — one button, with `Keep my subscription` at equal weight beside
   it. The confirm button is a calm secondary with an Anthracite label. **It is
   never a red button**: the error colour is for validation and payment failure,
   and cancelling is not an error.

**Success:** a confirmation screen and an email carrying the amount, the reference
number, the timing, the fact that past reports remain readable, and a line saying
they can come back without penalty.

**If the amount cannot be computed:** *"We could not calculate your refund
automatically. Please call us and we will do it with you — it does not affect your
rights."* The screen never guesses a number.

The same arithmetic, with the same worked example, appears on
`/en/legal/refund/` and in the guarantees text.

---

## 13. Sharing, the guest view, and the name of the deceased

### 13.1 The share link

Minimum 128 bits of entropy. `X-Robots-Tag: noindex, nofollow` plus a `noindex`
meta on the route. Revocable from the sheet that created it, with the creation
date shown. Non-expiring by default. It survives cancellation, because past
reports stay readable forever.

Because we render a link preview, Meta's and Viber's crawlers will fetch that URL
unauthenticated. That is acceptable only because of §13.2.

### 13.2 The link preview

```
og:title        Visit report — {date}
og:description  A record of a MemoryCare visit. Photographs, video and
                GPS confirmation.
og:image        a static branded asset on an ANTHRACITE ground: the mark,
                "Visit report", the date
```

**No photograph, ever. No cemetery, no plot label, no name.** The cemetery in a
preview identifies the family to everyone in a group chat, including people the
owner did not choose to tell — and the link is forwarded past the family more
often than the family thinks. The ground is Anthracite because a Nude card renders
as a near-blank rectangle in a dark WhatsApp thread, and because the colour mark's
hands vanish on Nude.

### 13.3 The guest view — `/r/:shareToken/`

Renders blocks 1–7 and 9 of §7.5, identically. **Removed server-side, not hidden
with CSS:** all prices, the recommended-work block, the next-visit date, the
subscription name, every button, and the action bar.

The foot of the page is the only mention of us: one line saying what MemoryCare is
and who shared this, a `tel:` link, and a text link to About. **No navigation into
the marketing site**, because every marketing page carries a consultation CTA and
one tap from a photograph of a grave to a sales bar is the worst thing this brand
could do. The guest route is physically incapable of importing a tariff card, the
calculator, an accent badge or a primary button.

Exactly one interactive element, a tertiary text link:
`Something is not right with this report` → three fields → files a guarantee
re-visit against that visit and notifies the owner. Support, never sales.

This means roughly half our audience is a dead end by design. That is correct, and
the replacement path is written down so nobody "optimises" it in month four: the
owner is asked on the call whether there is a second family plot. That is why the
object model is the plot.

### 13.4 The deceased's name — off by default

A report shows **cemetery, sector and plot**. The name appears only if the client
switches it on.

- The setting lives on the **plot**, is worded plainly, is reversible, and only
  the owner may change it. `name_display ∈ {family_name, full_name, none}`,
  default `family_name`.
- **Turning it off must also remove the name from links already issued** — the
  report is rendered from the plot's current setting, not from a snapshot.
- The reason is stated to the client in one plain sentence: the link is forwarded
  into a family group chat and to people without accounts, and part of the family
  may be in the EU.
- In photographs: **the client's own monument inscription is legible by default**,
  because it is the proof that we cleaned *their* grave. **Every neighbouring
  plot's name is out of frame or out of focus, without exception.**

---

## 14. Transactional email, PDF and the invoice

These artefacts reach a diaspora client before the portal does, and none of the
design system applies to them.

- **Email template:** one column, 600px, table-based, inline styles with literal
  hex values generated from the tokens at build time, Georgia and Arial fallbacks
  for the two brand faces, no background images, no CSS variables, no webfonts.
  Text-first, one Anthracite header bar, a link to the report.
  **A report notification email never embeds a photograph** — it will render in an
  inbox preview pane at someone's work.
- **The emails that exist:** activation / welcome, report ready, visit tomorrow
  (opt-in), visit moved, could not reach the plot, payment received, transfer
  request and its confirmations, renewal offer and its single reminder,
  cancellation confirmation with the refund.
- **The report PDF:** A4, the same block order, **never any price in any
  variant**, so a single file serves owner, member and guest. The tagline is set
  from the print asset. A forwarded PDF carries the same exposure as a shared link
  and obeys the same rules.
- **The written quote** sent after the consultation call: one page — the plot as
  described, the plan, the price in AMD with the arithmetic, the credit if any,
  the three guarantees, two named humans with numbers, and the payment
  instructions. This is the artefact that gets forwarded to the brother, and "I
  need to ask my brother" is the largest single loss cause in this business.
- **The bank-transfer invoice:** `MemoryCare LLC`, the legal address, the AMD
  amount, and the reference the client types into their bank. It is the only
  artefact between "consultation" and "paid client".

---

## 15. Deliberately left to the developer

These are decisions we consciously did not make, because they are implementation
choices with no user-visible consequence beyond meeting the rules already stated
above. Each may be settled without coming back to us.

1. Framework, rendering strategy and hosting for the marketing site, provided the
   360px hero paints text first and holds the LCP budget on a throttled 4G
   connection in all three locales.
2. How the `/en/ /hy/ /ru/` locale segment is implemented in routing, and how the
   language cookie is set — provided a shared link is never silently redirected.
3. Share-token generation, storage and lookup, provided the entropy floor,
   `noindex` and revocation behaviour in §13.1 hold.
4. Image pipeline: derivative sizes, formats, lazy-loading strategy and the CDN,
   provided ratios are preserved, no layout shift occurs and no placeholder is
   grey or black.
5. Video hosting, transcoding and poster-frame extraction, provided nothing
   autoplays and nothing is served from a third party that would add a tracking
   request to a page of grave photographs.
6. The PDF generation library and whether it runs at publish time or on demand.
7. The email delivery provider, bounce handling and retry policy.
8. Magic-link token lifetime, password rules, session length and re-authentication
   thresholds, provided the client is never locked out of a report they have paid
   for without a second route in.
9. Anti-spam on public forms — rate limiting, honeypot, server-side scoring. **Not
   a visible CAPTCHA**, which is the only constraint we impose here.
10. The phone parsing and formatting library, and the IP geolocation source for
    the default country.
11. Database engine, indexing, migrations and the concrete column types behind the
    object model in §3.
12. Time-zone storage and the derivation of "one business day" against Yerevan
    business hours and Armenian public holidays, once those hours are confirmed.
13. File storage for uploads, HEIC-to-JPEG conversion, virus scanning and the
    10 MB enforcement point.
14. Audit logging, backup and restore, and the technical implementation of
    indefinite report retention.
15. Pagination or lazy-loading in the visit list, if a plot ever exceeds a
    plausible number of visits.
16. Offline and retry behaviour on a poor connection, provided no form ever loses
    a value.
17. Server-side page and event counting, since no third-party analytics ship at
    launch.
18. ICU message implementation and the plural forms for Armenian (two) and Russian
    (three) on every counted string — visits, monuments, m², days.
19. How the calculator's arithmetic is shared between the marketing site, the
    order screen and the refund table, so that one change of rate cannot produce
    two different numbers.
20. Whether the crew's mobile capture tool writes into the same `visit` record or
    into a staging table that is published into it.

---

## 16. Still open — not ours to decide

Listed rather than invented. Each blocks something concrete.

**Owner**

1. **Legal address and registration number.** The oldest open item, now on the
   critical path for the footer, About, Contacts, the invoice and the bank
   package. Ships as a visibly marked placeholder until supplied.
2. **Yerevan business hours**, to be printed beside "within one business day" with
   the UTC offset, and what a Friday-evening submission from Glendale means. The
   promise itself is settled; the hours are not.
3. **The Armenian display names of four products.** Only `Զննում` is confirmed in
   the brief; the other four are carried from a superseded price list and must be
   confirmed by the owner or the localiser before the Armenian build, including
   whether `խնամք` stays in the name.
4. **Bank account details and the invoice reference format** for the transfer
   path, and the expected number of working days for a refund to arrive, which is
   printed on the cancellation screen.
5. **Whether a share link may still be *created* after cancellation.** Existing
   links stay live, because past reports stay readable; creating new ones is a
   commercial question we did not answer.
6. **Whether individual crew members are named in a report**, or only "the crew".
   It changes the crew note, the confirmation block and the photograph brief.
7. **Data retention** for photographs and video, given "forever" as the access
   promise, and what happens to a plot's records if the family asks for erasure.
8. **A five-minute legal read** on two points: the consent line on the
   consultation form as a lawful basis, and messaging a local contact in Yerevan
   who never contacted us.

**Designer**

9. **Deep Olive `#575E3B`** is a working value adopted by the owner. The designer
   should ratify it or supply her own, with CMYK computed in her profile.
10. **A single display face covering Latin, Cyrillic and Armenian.** Until one
    exists, `hy` and `ru` headings fall to the text face at 600 — a heading in the
    text face reads as a deliberate system, a heading in a second serif reads as a
    broken font. This does not block the English build.
11. **Three pieces of artwork that are treated as available and are not:** the
    woven-medallion section divider, the five-petal bullet glyph, and a simplified
    single-path mark for favicon sizes. Until they land, the divider is a 1px Olive
    rule and there is no petal bullet.
12. The two OG images, on an Anthracite ground.

**To be verified before build — no network access in this session**

13. **Does Cabin contain `֏` (U+058F)?** Every price on the site depends on it.
    The build is safe either way because the glyph is emitted in its own element
    with its own font binding, but the check must be run.
14. **Gloock does not contain `֏`** — found independently by two reviewers, still
    untested. Any price set in the display face needs the same binding.
15. **Does Gloock have tabular figures, and does it cover Cyrillic?** If it lacks
    tabular figures, prices fall back to the text face at 600 — one token change.
16. Every other typeface coverage claim in this project is unverified and is
    resolved by a build-time glyph test over the shipped font files, not by
    anyone's memory.

**Operations**

17. **The consultation call itself** — the first sixty seconds, the five things we
    must learn, the five things we must say, and the one thing we must never do,
    which is quote a number different from the one the calculator showed. The
    calculator configuration must be visible to the caller in the lead record, or
    the whole "one price list" argument dies on the first call.
18. **The no-answer ladder** after a consultation request: WhatsApp message → one
    call at an hour appropriate to the client's own time zone → one email carrying
    the written quote → stop. Three touches over five days, then the lead rests.
19. **The September photography shoot** needs an operational artefact that does not
    exist: a shot list per plot, a marked standing position, a fixed tripod height
    and focal length, and a file-naming convention matching the placeholder names.
    The whole visual system depends on this input and it is about two weeks away.

---

## 17. One name per thing

Because five documents named the same objects five ways, and the string keys, the
component files and the conversation must now use one word each.

| Use this | Never these |
|---|---|
| **Report sheet** — the document | report card, report artefact, proof card, report screen |
| **Report preview** — the cropped object in the marketing hero | proof card, report card |
| **Visit row** — the item in the visit list | report card |
| **Report masthead** · **Confirmation block** · **GPS confirmation** | verification rail (for the report header), status row, plot line |
| **Plot diagram** (marketing graphic) · **coordinates** · `Show on map` (outbound) | map tile, map crop, map pin, red pin |
| **Mobile action bar**, 64px + safe area | sticky action bar, sticky CTA bar |
| **One-off services band** / **Annual subscriptions band** | the row, tier row, band 1 / band 2 |
| **Our recommendation** (`tariff.badge.leading`) | Most chosen, most popular, bestseller, leading choice, ribbon |
| **Owner · Family manager · Family member · Guest** (`owner \| manager \| member \| guest`) | payer, subscriber, viewer, relative, link holder |
| **Local contact** | beneficiary, nominated relative |
| **Status screens**: `rescheduled` (*Visit moved*), `no-access` (*Could not reach the plot*), `preparing` (*Report being prepared*), `revisit-requested` (*Repeat visit requested*), `completed`, `scheduled` | postponed, access blocked, error |
| **The crew** | our team, operatives, technicians, the service team |
| **The plot** / **your family's plot** | the site, the object, the grave site, the burial |
| **Visits** (portal tab); a report lives inside a visit | Reports as a tab name |
| **Request a consultation** (every button) · **Request a free consultation** (form heading only) · `No payment now. No account needed.` (support line) | Free consultation, Get started, Contact us, Order |
| **Sign in** | Log in, Client login |
| **Full visit** | deep clean, heavy visit, light visit, preventive visit, standard visit |
| **֏ AMD**, always both | ֏ alone, AMD alone, 160k, AMD 160,000 |
| **MemoryCare** · **MemoryCare LLC** | Memory Care, MEMORYCARE, MC, Memory-Care |
| **Error** (`--mc-color-feedback-error`) | danger, warning, success — no token in this system ends in `-success` or `-warning` |

Denylist, enforced at build time in every locale: bestseller · most popular ·
monthly · light visit · preventive visit · save · discount · offer · special ·
instead of · was/now · `%` next to a price · `line-through` on a price · the only
· the first · nobody else · unlike other · no one in Yerevan · `since 20…` ·
trusted by · any testimonial · any review count · any emoji · Oops · Something
went wrong · QR.
