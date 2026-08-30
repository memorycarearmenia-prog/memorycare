# R2 — Content, Voice and UX Writing: review and convergence memo

**From:** Content Strategist / UX Writer (author of `03-content.md`)
**Read:** `DECISIONS.md`, `BRIEF.md`, `01-ux-architect.md`, `02-visual-lead.md`,
`04-conversion.md`, `05-design-system.md`
**Date:** 30.08.2026 · English

Everything in **bold code style** below is a production string. Where I say a
line is wrong, I supply the replacement. Character counts are given as
`(n ch)` including spaces.

---

# 1. Conflicts between the five proposals

## 1.1 Is Express in the subscription row or in the one-off band?

**Positions.** 02 (§A.4 tariff cards) and 05 (§A4.7) both build a three-card row
of **Express / Optimal / Maximum**, with Inspection pulled out as a separate
component. 04 (§A6) and I (§C.3) build **two bands**: one-offs (Inspection,
Express) above, annual (Optimal, Maximum, Special) below. 01 (§A3.2) builds three
subscription cards, then Inspection, then Special — leaving Express with no home
at all.

**What breaks either way.** In the 02/05 row, a 65,000 ֏ one-off sits in the same
grid, the same card shape and the same price type size as a 160,000 ֏/year
subscription. The eye reads that row as a price ladder and Express becomes "the
cheap plan" — which is precisely the failure mode the brief guards against for
Inspection. It also makes the credit rule a footnote on two cards in two
different bands. In the two-band layout, the risk is that Express looks like an
also-ran and loses the traffic it is meant to catch.

**Resolution: two bands. Inspection + Express above, Optimal + Maximum + Special
below.** The brief's own words are "Inspection is shown apart from the three
annual subscriptions" — the three annual products are Optimal, Maximum and
Special, so Express is not one of them and cannot sit in their row. The second
reason is commercial: the credit rule (60 days, one only, larger of the two) is a
property of the *band*, not of two unrelated cards, and stating it once under the
band is the difference between a clear promise and a support queue. Express does
not lose prominence, because the band carries the fork copy in 1.2 below, and
because 04 is right that Inspection and Express must be set at the same price
type size as the subscriptions — shrinking a price is what makes a product read
as cheap.

Band labels, canonical:

- Band 1 heading: **`One-off services`** (16 ch)
- Band 1 eyebrow on each card: **`One-off · not a subscription`** (28 ch)
- Band 2 heading: **`Annual subscriptions`** (20 ch)

Consequence for 05: `TariffCard` needs `variant: "one-off" | "annual"` and the
3-up grid applies only to the annual band; the one-off band is 2-up at `md`+ and
stacked below it. `Special` is a card in the annual band, not "a fifth card in the
row's footer position" (05 §A4.7) and not a line under the calculator (04 §A6) —
one place, one shape.

## 1.2 The pricing-page fork wording

04 §A6 opens the pricing page with a two-door fork. The doors are written as
**"No, I haven't seen it in years"** and **"Yes — I want it cared for"**.

**This breaks the voice rule and it must not ship.** "I haven't seen it in years"
makes the reader say their own absence out loud, in the first person, before they
have read a price. That is the guilt construction the brief forbids, and putting
it in the reader's mouth is worse than saying it in ours.

The mechanism is good — a fork beats a five-way comparison. Corrected doors:

- Door 1 label: **`I want to know what it needs`** (28 ch) → routes to Inspection
- Door 2 label: **`I want it looked after`** (22 ch) → routes to the annual band
- Fork heading: **`Two ways to start`** (17 ch)
- Fork sub: **`Some people want an assessment first. Some already know what they
  want done. Both routes are below.`** (99 ch)

## 1.3 Report block order and where the crew note sits

**Positions.** Brief §8 and I: confirmation → GPS → photographs → video → crew
note → recommendations. 01 §A4.4: confirmation → **crew note → work performed** →
photographs → video. 02: confirmation → GPS → what was done → photographs → crew
note. 05 §A4.9: status → plot → GPS chip → **photographs → notes → video**, and
"first image = the plot **after** the visit".

**What breaks.** 05's "first image is the after shot" contradicts 02's explicit
`CONDITION ON ARRIVAL` → `AFTER THE VISIT` sequence and contradicts the
evidentiary logic: a report that opens on the clean stone with no reference frame
is a marketing image, not a record. And a client who scrolls will meet the
"before" second and read it as an afterthought.

**Resolution.** One order, taken from 01 for the top and from 02 for the
photographs:

1. Masthead — mark, `Visit report`, plot identity, cemetery
2. Confirmation — date, `Visit completed`, crew, arrival/departure
3. GPS — the plot diagram + coordinates
4. Crew note (01 is right: the human sentence belongs before the images, because
   it tells the reader what they are about to look at)
5. Work performed — ticked list
6. Photographs — **arrival first, then after**, labelled above each group
7. Video
8. Recommended work (see 1.4)
9. Documents / actions
10. Next visit — **owner, manager and member only, never guest**

05's `first image = after` is struck. 02's sequential presentation stands; the
optional 2-up "Compare" block further down is fine.

## 1.4 Do prices ever appear on a report?

02 §A.4: *"Prices never appear on a report, in any view."* 01 §A4.4 and my §A.10.4
allow the recommended-work block with prices for Owner and Family manager only.
05 §B6 removes the whole commercial surface from the guest route at bundle level.

**What breaks.** 02's absolute rule is safer for the brand but means a client who
is told "your kerb is cracked" has no way to find out what fixing it costs
without a phone call — which is exactly the friction the diaspora buyer resents,
and it pushes the price conversation into a channel we cannot control.

**Resolution: 01 and I are right, with 02's rule applied one level down.** Prices
appear only in block 8, only for Owner and Family manager, on a changed ground
with a full-width rule above, and **never inside the guest view or the member
view — removed server-side, not hidden**. Guest and member see the observation
without the number. The framing line does the work:

- Block heading: **`Work we would recommend`** (23 ch)
- Intro: **`Nothing here happens unless you ask for it. These are observations,
  not urgent, unless we say so.`** (95 ch)

## 1.5 Is there any interactive element on the guest report?

01 §A2.3 allows exactly one non-commercial action on `/r/`. 02 §B7 removes the
sticky bar and every CTA. 05 §B6 makes the guest route physically unable to
render a `primary` button. My own doc said "That is all. No pricing link, no 'get
your own', no sign-up."

**Resolution: 01 wins, and I was wrong.** The split case (payer in Los Angeles,
mother in Yerevan with no account) is the case the brief calls central. If
Siranush opens the report and something is wrong, a dead page forces her to phone
her son abroad. One tertiary **text link**, never a button, never a filled
surface:

- Link: **`Something is not right with this report`** (39 ch)
- Screen heading: **`Tell us what is wrong`** (21 ch)
- Body: **`We will look at it and come back to you. You do not need an account
  and nothing here costs anything.`** (101 ch)
- Fields: `Your name` · `Phone or email` · `What is wrong?`
- Sent: **`We have your message. Someone will call you today or tomorrow, and we
  have told {owner_first_name} as well.`** (110 ch)

For 05: this is a `tertiary` variant, so the "no `primary` button in the guest
bundle" rule survives intact. Add `tertiary` to the guest route's allowed set.

## 1.6 The primary CTA label

**Positions.** 04 §A3 and 05 §A4.1 mandate **`Request a free consultation`** as
the one site-wide string. 01 §C1 says 29 characters is too long and prescribes
**`Free consultation`**. 02 §C sets the sticky-bar budget at 16 and grudgingly
accepts `Free consultation` at 18. My own doc used `Request a consultation`.

**What breaks.** Four labels for one action across five documents is exactly the
recognition-splitting that 04 correctly warns about. But `Request a free
consultation` is 27 ch against 05's own `button.label` ceiling of 22 (ref), which
means the mandated string fails the linter 05 ships.

**Resolution: one label everywhere — `Request a consultation` (22 ch).** It hits
05's ceiling exactly, survives Armenian at 30 and Russian at 28 in 05's own
table, and fits a full-width mobile button at 15px. The word "free" is not lost:
it moves to the line that is always adjacent to the button, where it is also
doing a second job (04's own reassurance line, which is better than mine):

- Button, every instance: **`Request a consultation`** (22 ch)
- Supporting line under it: **`No payment now. No account needed.`** (34 ch)
- Form heading: **`Request a free consultation`** (27 ch) — a heading, not a
  button, so the budget does not apply.

The sticky mobile bar therefore carries the same string, not a variant. To make
it fit at 360px, the bar is a 44px call icon plus one full-remaining-width
button — not 04's 56px two-button split and not 01's 62/38 split.

## 1.7 The consultation form: how many fields

01 §A6.1 adds a conditional local-contact disclosure, three preferred-time chips,
and a hidden calculator payload. 04 §A4 argues four fields, two required, and
explicitly rejects preferred contact time **and** any consent checkbox beyond a
one-line privacy statement.

**Resolution, splitting them:**
- **Preferred-time chips: cut.** 04 is right — we guess wrong and ask on the call.
- **Local-contact disclosure: keep.** 01's strongest structural insight, and it
  costs one tap for people who do not need it. Strings in §4.2 below.
- **Consent checkbox: keep, required.** 04 is wrong here, and this is not a
  conversion question. We will be storing a phone number, a cemetery, and later
  photographs of a family's grave, and the bank package requires an English
  privacy policy that the site actually honours. A one-line statement is not a
  record of consent. One checkbox, plain, no theatre.
- **Hidden calculator payload: keep** (01), and echo it back in the confirmation.

## 1.8 Optimal's "leading choice" marker

02 marks Optimal by inverting the card to Anthracite with `MOST CHOSEN` in Nude.
05 uses `Badge--accent`: Deep Olive fill, Ivory label, plus a 2px accent border.
04 asks for "an Olive band with Anthracite text". 01 wants a ribbon and a 12px
lift.

**Resolution: 05's badge.** 04's Olive band with Anthracite text is 3.08 and
fails; so does the version **I** proposed in my own §C.3 ("Olive fill with
Anthracite label, which passes" — it does not, and that line is withdrawn).
02's inversion is elegant but it puts the leading product on the one dark card in
a light row, which on a phone reads as "the expensive one" before it reads as
"the usual one". Deep Olive fill, Ivory label, string **`Most chosen`** (11 ch),
placed above the product name, not over the price.

## 1.9 Radius, and the "no shadows" rule

02 §A.3 specifies radius 0/2px and **no shadow anywhere in the system**. 05 ships
`radius-md 10` on buttons and a five-step elevation ladder up to
`0 20px 48px`. These cannot both be built.

Not my call, but it is a real contradiction that has to be settled before
`mc-tokens.css` is frozen, and it changes nothing in the copy. Flagging only.
My weak preference is 02's, because a 10px radius plus a shadow is the
"friendly SaaS" register the brief rules out — but the design lead and the system
engineer must pick one.

---

# 2. Contradictions with the owner decisions

## 2.1 Error red — three documents say "never red", including mine

**DECISIONS §2** adds one muted red, `#8C3A2E`, for form validation and payment
failure only.

Against it:
- **My §C.9:** *"Errors sit on Nude with Anthracite text. Never red. A red panel
  next to a photograph of a grave is unacceptable."*
- **01 §A8:** *"No red. We have no red in the palette and we are not adding one.
  Errors use Deep Olive."* And §A6.1: *"Errors render below the field, in Deep
  Olive."*
- **02 §A.4 inputs:** error state built as a 2px Anthracite border plus an
  Anthracite bar and dot.
- **02 §B8** goes further and recommends **two** functional colours. The ruling
  says one, and that it is the last.

Only 05 is already correct (`mc.color.danger.600 = #8C3A2E`).

**My §C.9 is rewritten as follows, and this is the wording that goes into the
convergence document:**

> Every error follows the same three-part shape: what happened, whose fault it
> is, what to do. The component has three slots (heading, body, action) plus an
> optional fourth line for the phone number. It accepts no icon slot beyond the
> single error glyph and no illustration slot.
>
> The error colour is used on the **border, the glyph and the message text
> only** — never as a panel fill, never as a heading colour, never anywhere on a
> screen that is showing a photograph of a grave. On a report screen the error
> component renders with no red at all: the failure there is ours, not the
> client's, and it is a sentence, not a validation. Success and attention states
> carry no colour: wording, glyph and rule weight only.

**Token naming.** DECISIONS requires a name that makes the restriction obvious,
`--mc-color-feedback-error`, with no `-success` / `-warning` sibling. 05 ships
`mc.color.danger.600` / `danger.100` and, worse, `Badge` variants named
`warning` and `danger` and `Toast` variants named `success` / `warning` /
`error`. The variant names re-create the sibling family the ruling forbids, and a
developer will eventually colour them. Rename:
- `mc.color.danger.*` → **`mc.color.feedback.error.*`**
- Badge variants → `neutral · accent · accent-soft · attention · error · inverse`,
  where `attention` is `nude-600` with `text-primary` and carries **no** red
- Toast variants → `neutral · error` only. A postponed visit, a completed
  payment and a sent invitation are all `neutral`, differentiated by their words.

## 2.2 The 95,000 ֏ figure

DECISIONS §3: shown publicly in the calculator and on the pricing page, framed as
the credit mechanic, never as a discount, never in the hero, never as the Express
card's headline price.

- **01 §D5 calls it "a 40% first-year discount".** Internal prose, but it is the
  vocabulary that leaks into a card label three weeks later. Strike the word.
  The internal description is: *the first-year figure that follows from the
  credit rule.*
- **No one wrote the public strings.** 01's calculator line is close but is bare
  arithmetic with no frame and no AMD wording. Full set in §4.5 below.
- My own document does not contain the figure at all. That is the gap this memo
  closes.

## 2.3 Legal entity spelling

DECISIONS §1 settles it: **`MemoryCare LLC`**, one word.

- My §D open item 6 ("somebody needs to check the registration certificate") is
  **closed**. Delete it.
- `BRIEF.md` §1 line 11 still reads "Memory Care LLC, Yerevan, Armenia" — stale,
  and 05's own denylist would fail the build on it. Someone should fix the brief.
- 05's denylist already blocks `Memory Care` (spaced) and `MEMORYCARE`. Good;
  keep it, and add `Memory-Care`.

## 2.4 Credit window

DECISIONS §4 and BRIEF: **60 days**, one credit only, the larger of the two, and
it fires only at signature. My copy is already on 60/60. 01 §D4 raises the 30-day
figure from the repo's `CLAUDE.md` as an open conflict — it is now closed: 60.
Nobody should re-open it from the repo file, which also carries stale prices
(60,000 / 180,000 / 240,000 and 6- and 9-visit tiers). Every price string in this
project comes from `BRIEF.md` §5.

## 2.5 Cabin, and the dram glyph

DECISIONS §4 and §5. Two things to hold:
- Every mock and every exported page carries the label
  **`Cabin — substitute for Gill Sans (commercial, unlicensed for web)`**.
  02 and 05 both do this. 01 does it once, in §B4. Make it a footer note in every
  deliverable.
- The **֏ (U+058F)** check is still open and is on the critical path for every
  price string in this document. My §C.11 stands. If Cabin lacks it, the fallback
  is declared for that codepoint alone, and the currency utility in 05 §A4.8 is
  where it belongs.

## 2.6 Working hours and the callback promise

Not an owner decision yet, and 04 wrote as if it were. 04 §A3 states hours
**"10:00–19:00 Yerevan time"** and a call length of **"10–15 minutes"**. Neither
is in the brief, neither is confirmed, and both are promises a first client will
measure us against. Until the CEO confirms them, the confirmation copy uses the
window only:

> **`We will call or write within one working day, Yerevan time (UTC+4). If you
> would rather not wait, write to us on WhatsApp at +374 93 154 108.`** (146 ch)

04's underlying idea — showing the visitor their own local equivalent — is good
and I want it. String, once hours are confirmed:
**`That is {local_window} where you are.`** (37 ch)

---

# 3. My copy that does not fit the layouts

Slot, the binding limit, and the shorter line.

| Slot | Limit | My original | Replacement |
|---|---|---|---|
| Hero H1 | 02: 38–46, hard max 52 (01: max 56; 05: 62) | "You will see exactly what was done at the grave, and when." (58) | **`See exactly what was done at the grave, and when.`** (49) — inside 01 and 05, two over 02's soft band, and 02 should take those two characters. If 02 holds at 46: **`See what was done at the grave, and when.`** (41) |
| Hero subhead | 02: 100–130 | 230 ch | **`Scheduled care for a family plot in Yerevan. Photographs, video and a GPS point after every visit.`** (98) |
| Hero under-CTA | — | "Three fields, no account needed. Prices are on the site, the same for everyone." (79) | **`No payment now. No account needed.`** (34) |
| Tariff feature bullet | 02: 48 | "Report after every visit: photographs, video, GPS." (50) | **`Photo, video and GPS report after every visit`** (45) |
| Tariff feature bullet | 02: 48 | "Covered by the MemoryCare guarantees." (37) | keep, drop the full stop: **`Covered by the MemoryCare guarantees`** (36) |
| Tariff description | 05: 74 | Inspection: my 3-sentence block | **`One assessment visit. We record the plot's condition. No cleaning.`** (66) |
| Tariff description | 05: 74 | Express | **`One full visit: deep cleaning of the plot and every monument.`** (61) |
| Tariff description | 05: 74 | Optimal | **`Four full visits, one each season. Report after every visit.`** (60) |
| Tariff description | 05: 74 | Maximum | **`Six full visits across the year. Report after every visit.`** (58) |
| Tariff description | 05: 74 | Special | **`Larger plot, more monuments, or several family plots.`** (53) |
| Guarantee title | 02: 30 | "A free repeat visit within 7 days" (33) | **`Free repeat visit in 7 days`** (27) |
| Guarantee body | 02: 110 | 135 ch | **`Tell us within seven days of a report and we come back and redo the work at our cost.`** (85) |
| Guarantee body | 02: 110 | damage item | **`If we damage a monument or the plot, we repair or replace it at our cost.`** (73) |
| Guarantee body | 02: 110 | cancel item | **`Cancel at any time and we return the visits you have paid for and not received, pro rata.`** (89) |
| Meta title, Home | 05/02: 60 max | 63 ch | **`MemoryCare — grave care in Yerevan cemeteries`** (45) |
| Meta title, Family Circle | 60 max | 64 ch | **`Family Circle — shared grave care reports \| MemoryCare`** (54) |
| Meta description, Home | 155 max | 195 ch | **`Care for family graves in Yerevan cemeteries on a yearly schedule, with photo, video and GPS reports after every visit. Not dementia care. From 20,000 AMD.`** (155) |
| Report status | 05: 24 | "Crew could not access the plot" (30) | **`Could not reach the plot`** (24) |
| Report status | 05: 24 | "Visit postponed by weather" (26) | **`Visit moved — weather`** (21) |
| Report block heading | 02: 24 | "The visit is done. The report is being prepared." (47) | **`Report being prepared`** (21) |
| Nav items | 01: 16 max | all five pass: `How it works` (12) · `Pricing` (7) · `Sample report` (13) · `Family Circle` (13) · `About` (5) | unchanged |
| Sticky bar button | 02: 16–18 | — | see §1.6: the bar carries `Request a consultation` (22) because it is now one full-width button, not two |

**One slot I am refusing to shorten.** 05's `form.error` ceiling is 90 ch and my
longest validation message is 76, so nothing needs cutting there — but I will not
accept 02's 80-character error ceiling for the two-line phone message. Split it
instead, which reads better anyway:

- **`This does not look like a phone number or an email address.`** (58)
- Second line: **`Please check the number and try again.`** (38)

---

# 4. New strings the others need and I did not write

## 4.1 Failed visit — the crew could not reach the plot (01 §A8.3b)

This is a screen, not an error, and it gets the same design budget as a report.
No red, no warning triangle.

```
Status chip:   Could not reach the plot
Heading:       We went to {plot_label} on {date} and could not reach it
Confirmation:  The crew arrived at {time} and recorded their position at the
               cemetery. The coordinates are below.
GPS block:     [same plot diagram as a normal report]
               Helper: This is where the crew stood. It is how you know they
               went.

What we found
{obstruction_description}
[Photograph of the obstruction — never a photograph of a neighbouring grave]

What happens now
We return on {return_date}. {action_taken}
This visit does not come out of your subscription. Your subscription still
covers all {n} visits.

If you would rather talk to someone, call Hayk on +374 93 154 108 — he has
the crew's account of it.

[Call Hayk]   [Suggest a different date]
```

Operator-written `{obstruction_description}`, from a fixed set — plain, no
euphemism, never "unforeseen circumstances":
- `The cemetery was closed for a funeral and the section was not open to us.`
- `A fence has gone up around the neighbouring plot and it blocks the path.`
- `Building materials have been left across the plot.`
- `We could not identify the plot from the details we have.`

`{action_taken}`, from a fixed set:
- `We have spoken to the cemetery administration and they expect the section to
  be open by then.`
- `We are asking the cemetery administration who left the materials there.`
- `Could you send us a photograph of the plot, or the name and dates on the
  stone? That is usually enough for us to find it.`

Push and email, budgets from 01 §C5 (subject max 52):
```
Subject:  We could not reach {plot_label} today          (≤52 with a short label)
Push:     We could not reach the plot today. There is a photograph and a date.
Preheader: We went, we were stopped, and we return on {return_date}.
```

## 4.2 Ownership transfer (01 §A5 — "the payer may die")

Nobody wrote a word of this and it is the flow most likely to be used at the
worst moment in a family's year. The register is administrative and calm. No
condolence copy — we do not know why the transfer is happening and guessing is
worse than not asking.

```
Entry, in Subscription and payments:
  Link:      Transfer ownership of this plot                     (31 ch)
  Helper:    The owner is the person who pays and who can change or cancel the
             subscription. There is one owner, and it can be changed.

Step 1 — choose
  Heading:   Transfer ownership of {plot_label}
  Body:      The person you choose takes over the subscription: the payments,
             the schedule, who is in the family circle, and the right to
             cancel. You keep access to every report unless they remove you.
  Field:     Who should take over?
             Helper: Choose someone already in the family circle, or enter
             their email and we will invite them.
  Field:     Anything they should know (optional)
  CTA:       Continue
  Alt:       Keep ownership

Step 2 — confirm, with what changes stated plainly
  Heading:   What changes when {name} takes over
  List:      {name} becomes the owner and can change or cancel the subscription.
             Invoices and payment requests go to {name}.
             You become a family manager: you see every report and can order
             work, but not change the subscription.
             The plot, its GPS point and every past report stay exactly as
             they are.
  Body:      Nothing changes until {name} accepts. We will ask them to confirm
             by email, and we will ask you to confirm as well.
  CTA:       Send the transfer request
  Alt:       Go back

Step 3 — pending
  Heading:   Waiting for {name} to accept
  Body:      We have written to {email}. The request is open for 14 days.
             Until they accept, nothing has changed and you are still the
             owner.
  CTA:       Send the request again
  Alt:       Cancel the transfer

Email to the person taking over
  Subject:  {owner_name} would like you to take over the care of {plot_label}
  Body:     {owner_name} looks after {plot_label} at {cemetery} through
            MemoryCare and has asked us to transfer it to you.
            If you accept, you become the owner: the subscription, the visit
            schedule, the invoices and the family circle. The reports already
            made stay where they are.
            Nothing is charged to you today. The next payment is due on
            {renewal_date} and we will write to you before it.
            [Accept]   [Decline]
            If you are not sure why you received this, speak to {owner_name}
            first, or call Hayk on +374 93 154 108. The request expires in
            14 days on its own.

Confirmation to both
  Subject:  {plot_label} is now looked after by {new_owner_name}
  Body:     The transfer is done. {new_owner_name} is the owner of the
            subscription for {plot_label}. {old_owner_name} keeps access to
            every report as a family manager.

Declined
  Heading:  {name} has not taken over the plot
  Body:     They declined the transfer. You are still the owner and nothing
            has changed. You can ask someone else, or leave it as it is.

Edge case — the owner cannot act (this is why the flow exists)
  Page:     If the owner of a subscription has died
  Body:     Call us on +374 55 315 323 and we will move the subscription to
            another member of the family. We will ask for a document
            confirming the death and for proof of your relationship, because
            we are not able to hand over a family's records on a phone call
            alone. Care of the plot does not stop while this is settled — the
            visits continue on the schedule already paid for.
```

That last block is the one the owner should read personally: it commits us to
continuing service during a transfer, which is an operational promise as much as
a copy decision.

## 4.3 Guest report view — the complete string set

My §A.10.5 was too thin, and 01, 02 and 05 all need exact strings for the route.

```
Top strip
  Visit report · MemoryCare
  {cemetery} · {plot_label} · {date}

[Confirmation, GPS, crew note, work performed, photographs, video —
 identical to the authenticated report]

Removed server-side, not hidden: prices, the recommended-work figures, the
next-visit date, the subscription name, every button, the sticky bar.

Foot of the page — the only mention of us
  This report was made by MemoryCare after a visit to the plot on {date}.
  {owner_first_name} shared it with you.
  MemoryCare cares for family memorial plots in Yerevan cemeteries.
  Questions: +374 93 154 108
  [About MemoryCare]        ← text link, not a button

One permitted action (see §1.5)
  Something is not right with this report

Link expired or revoked
  Heading: This link is no longer active
  Body:    The person who sent it can share it again. Nothing has been
           deleted — the report still exists.
  No sign-up prompt, no account prompt, no price.

Guest view on a report that is still being prepared
  Heading: The visit took place on {date}
  Body:    The photographs and video are still being prepared.
           {owner_first_name} will be able to send you the link again when
           they are ready.
```

OG, unchanged from my §A.10.6 and consistent with 02 and 05:
```
og:title        Visit report — {date}
og:description  A record of a MemoryCare visit to a family memorial plot in
                {cemetery}. Photographs, video and GPS confirmation.
og:image        brand/og/report-share.png — mark, "Visit report", date.
                Never a photograph. Never the plot identity.
```

## 4.4 Error states in the muted red

The colour appears in exactly two places: **form validation** and **payment
failure**. Everything else is neutral. Strings, with the rule attached to each.

**Form validation — red border, red glyph, red message text, no fill.**
```
Please enter your name.
Please give us one way to reach you.
This does not look like a phone number or an email address.
Please check the number and try again.
Please include the country code, for example +374, +1 or +33.
Please tell us roughly where the plot is.
Please confirm we may contact you.
Please enter their email address.
This does not look like an email address.
{email} already has access to this plot.
Please use at least 10 characters.
The calculator goes up to 100 m². For a larger plot we price the work after
an Inspection.                                    ← neutral, not red: not an error
```

**Payment failure — red glyph and red heading rule only, never a red panel.**
```
Card payment
  Heading: The payment did not go through
  Body:    Your card was not charged. This usually means the bank declined it
           rather than anything being wrong with your details.
  What to do:
           Try again, or use a different card.
           Pay by bank transfer instead — we will send an invoice.
           Call Hayk on +374 93 154 108 and we will take it from there.
  CTA:     Try again        Alt: Pay by bank transfer

Bank transfer not arrived
  Heading: We have not received your transfer yet          ← neutral, no red
  Body:    Transfers from abroad usually take one to three working days.
           Nothing is needed from you. If it has been longer than that,
           send us the payment reference and we will trace it.

Subscription payment failed on renewal
  Heading: We could not take this year's payment
  Body:    Your subscription and your reports are unaffected and nothing has
           been cancelled. Update the payment details or pay by transfer, and
           the schedule continues as it is.
```

**Everything that is NOT red**, restated so nobody colours it later: a postponed
visit, a blocked plot, a failed report load, an expired link, an expired
invitation, a guarantee re-visit request, a cancellation, a session timeout.
These are neutral. And on any screen showing a photograph of a grave, the error
component renders with no red at all.

Never, in any language: `Oops`, `Something went wrong`, `Error`, `Invalid`,
`Failed`, `Required field`, any emoji, any exclamation mark.

## 4.5 The 95,000 ֏ first-year explanation

Three placements, three lengths, all framed as the credit mechanic. No "save", no
strike-through on 160,000, no "offer", not in the hero, not as the Express card's
headline price.

**(a) In the calculator, one-off mode only — one line under the Express total:**
> **`If you take Optimal within 60 days, the 65,000 ֏ AMD you paid for this visit
> comes off the annual price: 160,000 − 65,000 = 95,000 ֏ AMD for the first
> year.`** (159 ch — two lines at 375, inside 01's 70–120 budget only if split;
> split it as a label plus a value:)
> - Label: **`If you take Optimal within 60 days`** (33 ch)
> - Value: **`160,000 − 65,000 = 95,000 ֏ AMD for your first year`** (51 ch)

**(b) On the pricing page, under the one-off band, as part of the credit block:**
```
H3:  How a one-off payment is credited

If you have already paid for an Inspection or an Express visit, that amount
comes off the price when you sign an annual subscription. An Express visit
paid at 65,000 ֏ AMD and an Optimal subscription at 160,000 ֏ AMD means
95,000 ֏ AMD for the first year, and 160,000 ֏ AMD in the years after.

- The credit applies within 60 days of paying for the one-off service.
- One amount is credited, not two. If you paid for both an Inspection and an
  Express visit, the larger of the two is credited.
- The credit is applied when the annual subscription is signed. It does not
  move between one-off services — an Inspection is not credited towards an
  Express visit.
- Express is 65,000 ֏ AMD every time. There is no reduced repeat price.
```
The second sentence — *"and 160,000 ֏ AMD in the years after"* — is not optional.
It is what stops the figure reading as a discount, and it prevents the renewal
conversation a year later going badly.

**(c) In the portal, after a one-off, as a fact with a date and no countdown:**
> **`Your Express visit is credited`** (30 ch)
> **`The 65,000 ֏ AMD you paid is credited against an annual subscription until
> {credit_end_date}. Optimal would be 95,000 ֏ AMD for the first year and
> 160,000 ֏ AMD after that.`** (170 ch)

No timer, no colour change as the date approaches, no second reminder. One
statement, in the subscription screen, and it disappears when the window closes:
> **`The credit window for your Express visit closed on {date}. Express is
> 65,000 ֏ AMD and Optimal is 160,000 ֏ AMD a year.`** (117 ch)

**Internal note for 01 and for the owner:** the abuse question 01 raises in §D5 —
once per client or once per plot — still needs an answer, and it must be settled
before this string ships, because the sentence changes. I would write it **once
per plot**, and if the owner agrees, the credit block gains one line:
> **`One credit for each plot.`** (25 ch)

## 4.6 "One price for Yerevan and Los Angeles"

Everyone asked for this line; three documents quote three different versions.
Canonical, one string, used in exactly three places:

> **`One price list — the same in Yerevan and in Los Angeles.`** (56 ch)

Placements: the pricing-page subhead position, above the fork; the calculator
heading area; and the pricing FAQ answer. Nowhere else — repeating it a fourth
time turns a statement of fairness into a protest.

The supporting sentence, used once, under the calculator:
> **`The price is on the page before you speak to anyone. It does not change
> depending on where you are calling from.`** (117 ch)

Rules that go with it, for the localisers: this is **the one place a country may
be named**, because naming Los Angeles here names fairness, not an audience.
It must not migrate into the hero, the About page or any headline.

---

# 5. Voice, stop-list and claim breaches in the other proposals

| # | Where | What it says | Why it fails | Fix |
|---|---|---|---|---|
| 1 | 04 §A6 | `No, I haven't seen it in years` | Guilt construction, in the reader's own voice, before any price | `I want to know what it needs` |
| 2 | 04 §A5 | `No charge, no argument.` | Combative — it presumes an argument, and implies other companies argue | `You pay nothing for that visit.` |
| 3 | 04 §A5 | `Not satisfied? We come back within 7 days.` | Rhetorical question as a heading; my stop-list bans it | `Free repeat visit in 7 days` |
| 4 | 04 §A3 | `Our hours are 10:00–19:00 Yerevan time` and `10–15 minutes` | Unconfirmed facts stated as commitments | Use the callback window only, until the CEO confirms (§2.6) |
| 5 | 04 §0 | `the equivalent of USD 400` | Internal only — but it must never reach a page. Any FX figure is labelled approximate and never appears in a total | Keep internal; the public rule is in my §A.3 payment block |
| 6 | 01 §A4.1 | `within 24 hours of the visit, the report` | Promises the report SLA that is still `{REPORT_SLA}` and unconfirmed by operations | Use `{REPORT_SLA}` until operations answer; interim copy: `after the visit` |
| 7 | 01 §A8.2 | `The photographs are still uploading. They usually appear within an hour of the visit.` | Same — invents an SLA, and a narrower one | `Some photographs are still uploading. The rest of the report is complete.` |
| 8 | 01 §A7 | `Let's price this properly.` | Implies the calculator's other prices are improper | `This one we should price together.` |
| 9 | 01 §D5 | `a 40% first-year discount` | The exact word the owner ruled out; internal today, on a card next month | `the first-year figure that follows from the credit rule` |
| 10 | 05 §A4.9 | Status label `Could not access plot` | Register: "access" is procedural, and it is 25 ch against a 24 ch ceiling | `Could not reach the plot` (24) |
| 11 | 05 §A4.15 | Toast variants `success` / `warning` | Re-creates the sibling colour family DECISIONS §2 forbids | `neutral` / `error` only (§2.1) |
| 12 | 02 §B8 | Recommends approving **two** functional colours | Directly contradicts the ruling: one, and it is the last | One muted red, errors only |
| 13 | 02 §A.4 | Report status states distinguished by **glyph and outline weight alone** | Colour is not the only signal — but neither can glyph weight be. Outline weight at 1px vs 2px is invisible to the audience we have | Every status carries its **word**: `Visit completed` · `Visit moved` · `Could not reach the plot` |
| 14 | 05 §C denylist | Blocks `since 20` | Correct, and it would also catch a stray `since 2015` about hush.am — which we must never publish. Keep, and add `the only`, `the first`, `nobody else`, `unlike other`, `no one in Yerevan` | Extend the denylist |
| 15 | 04 §C4 | `Photographs, video, GPS, a portal and accounts for the whole family — the full chain in one place.` | Safe and accurate as written — **approved**, and it is the model for how we talk about competitors: describe what we do, never what they lack | Keep verbatim |
| 16 | 01 §A2.3 step 5 | `sending "renew your subscription" to a grieving 72-year-old who did not pay is a brand-ending message` | Correct, and it should be a **written rule in the string file**, not a note in a doc | Add to the content rules: no renewal, price, payment or upgrade string may be addressed to a `local contact` or a `member` |

**One claim nobody made, and I want it kept out.** Neither 04's objection map nor
01's FAQ contains a comparison table against hush.am. 04 §C5 says explicitly not
to build one. That is right, and it should be a standing rule in the convergence
document: **no competitor is named on the site, in any language, in any form,
including in an FAQ answer.** We describe the combination we offer; the reader
can do their own searching, and if they do, we would rather they find us honest
than defensive.

---

# 6. Naming — one term per thing

Where two proposals name the same object differently, this is the term the user
sees. Left column is canonical.

## 6.1 Products, as displayed

The English name is the display name in the English site. The Armenian original
appears **only** on the pricing card, as a small subtitle under the English name
(01's card anatomy), and is the display name in the Armenian site.

| English (displayed) | Armenian | Price | Band |
|---|---|---|---|
| **Inspection** | Զննում | 20,000 ֏ AMD | One-off |
| **Express** | Էքսպրես | 65,000 ֏ AMD | One-off |
| **Optimal** | Օպտիմալ | 160,000 ֏ AMD / year | Annual · marked `Most chosen` |
| **Maximum** | Մաքսիմում | 200,000 ֏ AMD / year | Annual |
| **Special** | Հատուկ | By calculator | Annual |

⚠️ Only **Զննում** is confirmed in `BRIEF.md`. The other four Armenian forms are
carried over from the repo's project memory, where they appear as two-word names
(`Էքսպրես խնամք`, `Օպտիմալ խնամք`, `Մաքսիմում խնամք`) attached to a *superseded*
price list. **The owner or the localiser must confirm the Armenian display names
before the Armenian build**, including whether the word `խնամք` stays. Do not
guess this from the old file.

Never, in any language: `tier 1`, `tier 2`, `plan A`, `basic`, `premium`,
`bestseller`, `most popular`, `monthly`, `light visit`, `preventive visit`.

## 6.2 Everything else

| Canonical | Rejected variants and where they appear |
|---|---|
| **Request a consultation** (button) | `Request a free consultation` (04, 05 — becomes the form heading), `Free consultation` (01, 02), `Request consultation` (01), `Get started`, `Contact us` |
| **Request a free consultation** (form heading only) | — |
| **Sign in** | `Log in` (01 §A3.0), `Client login` (01 §A1.1) |
| **Visit report** | `Report` alone, `visit summary` |
| **Sample report** | `Report example`, `See a full report` (01 §A3.1) |
| **Most chosen** | `MOST CHOSEN` in caps except where the eyebrow token uppercases it in Latin; `bestseller`; `most popular`; `leading choice` (internal only) |
| **One-off · not a subscription** | `ONE-OFF · NO SUBSCRIPTION` (02), `One-off services` (05 — that is the *band heading*, keep it there) |
| **Full visit** | `deep clean`, `heavy visit`, `standard visit` |
| **Family Circle** | `family circle` lowercase in running text is wrong — it is a product name, capitalised both words |
| **Owner** | `account owner`, `payer`, `subscriber` |
| **Family manager** | `Manager` (01 §A5) — the bare word is ambiguous next to "crew" and "administration" |
| **Family member** | `Member` (01 §A5), `relative`, `viewer` |
| **Guest** | `link holder`, `anonymous viewer` |
| **Local contact** | `beneficiary` (01 §D2 — internal only, never on screen), `nominated relative` |
| **The crew** | `our team`, `the service team`, `operatives`, `technicians` |
| **The plot** / **your family's plot** | `the site`, `the object`, `the grave site`, `the burial` |
| **Plot identity** (internal) | shown to the user as the plot label only |
| **Visits** (portal tab) | `Reports` as a tab name — 01's bottom bar has both `Reports` and `Plots`; the tab is **Visits**, and a report lives inside a visit |
| **Copy link** (mobile) / **Copy the link to this report** (accessible name) | `Share`, `Send` |
| **Pay by bank transfer** | `Pay online` where acquiring is not live; `Pay online` stays as the secondary label only once cards are enabled |
| **MemoryCare LLC** | `Memory Care LLC`, `MEMORYCARE`, `MC` |
| **֏ AMD**, always both | `֏` alone, `AMD` alone, `160k`, `AMD 160,000` |

## 6.3 Two names I am changing in my own document

- I wrote **`Visits`** and **`Family Circle`** as portal screens but used
  `Reports` loosely in body copy. Corrected: a **visit** is the event, a
  **report** is the record of it, and the portal navigates by visit.
- I wrote **`Family manager — someone you trust with decisions`**. Against 01's
  matrix, the manager cannot approve a charge — the owner does. Corrected
  description: **`Family manager — sees every report and can request extra work.
  Cannot approve a charge, cancel the subscription or change payment details.`**
  (137 ch — over 01's 40–90 role-description budget, so on the invite screen it
  is truncated to: **`Sees every report, can request extra work. Cannot spend or
  cancel.`** (66 ch), with the full sentence in the expandable.)

---

# 7. What still has to be decided by a person, not by us

1. **Report SLA** (`{REPORT_SLA}`) — operations. Blocks six strings across the
   portal and two emails. 01 has already written "24 hours" into a screen; it
   must not ship until confirmed.
2. **Pro-rata basis — visits or days.** 01 and I both recommend **by visits
   consumed**. It changes the Refund Policy worked example, the cancellation
   screen and the bank submission.
3. **Credit: once per client or once per plot.** Changes one sentence in the
   credit block and one rule in the platform.
4. **Working hours and the callback window.** 04 has written specific hours; the
   CEO must confirm or we publish the window only.
5. **Legal address and registration number.** Oldest open item; gates the footer,
   About, Contacts and the bank package.
6. **Armenian product display names** (§6.1) — the four unconfirmed ones.
7. **Whether the ֏ glyph exists in Cabin.** Every price string depends on it.
8. **The commitment in §4.2:** that care continues on the paid schedule while a
   subscription is being transferred after a death. That is an operational
   promise and only the owners can make it.

---

**Closed by this memo, do not re-open:** the legal entity spelling
(`MemoryCare LLC`), the credit window (60 days), the error colour (one muted
red, errors only), and whether the 95,000 ֏ figure is public (it is, framed as
the mechanic, never as a discount).
