# 03 — Content, Voice and UX Writing
**MemoryCare — marketing site + client portal**
Content Strategist / UX Writer · English master copy · v1, 30.08.2026

Everything below is production copy. Paste it. Where a string is a variable,
it is written `{like_this}`. Where a decision belongs to someone else, it is
flagged **[OPEN]**.

---

## 0. Rules I applied to every string in this document

These are compliance rules, not style preferences. Every one comes from the
brief or from the bank's conditions.

1. **Nothing is invented.** No testimonials, no counts, no years, no "trusted
   by N families", no delivery dates. Where a page would normally carry social
   proof, it carries a guarantee or a described method instead.
2. **No QR code, no digital memory page.** The phrase does not appear in this
   document and must not appear in any build.
3. **We never claim to be the only ones.** hush.am exists, has photo reports,
   and is checkable. Our claims are always about the specific combination and
   about what we commit to in writing.
4. **"Memory care" is disambiguated in every meta description.** Every one
   pairs the name with "cemetery", "grave" or "memorial plot" in the first
   twelve words. This is a hard SEO and honesty requirement, not a nicety.
5. **Money format:** `160,000 ֏ AMD`. Symbol immediately after the numeral,
   currency code in Latin letters after a space. Both are always present, in
   body copy, in tables, in the calculator, in the portal and in email. Never
   `160k`, never `160,000֏` alone, never "AMD 160,000". Any USD/EUR figure is
   labelled "approximate" and never appears in a total.
6. **Banned words** (full stop-list in §B.2): monthly, bestseller, light visit,
   preventive visit, deceased, the departed, remains, object, disposal, plot
   maintenance package "deal", "just", "simply", "amazing", "!". No emoji
   anywhere in the product — including error states, especially error states.
7. **Every visit is a full visit.** There is no tier of visit. Copy never
   implies one visit is smaller than another.
8. **Inspection is never described as a subscription** and never sits inside
   the annual card row.
9. **We do not use guilt.** No "when was the last time you visited". No "she
   would have wanted". The reader's situation is treated as normal.
10. **We call people by their relationship, not by a category.** "Your
    mother's grave", "your family's plot" — not "the deceased's site".

---

# A. CONTENT

## A.1 Global elements

### A.1.1 Header

Header navigation (5 items max on desktop, hamburger below 900px):

```
How it works · Pricing · Sample report · Family Circle · About
```

Header CTA button: `Request a consultation`
Header secondary (portal): `Sign in`

Language switcher label (screen-reader only): `Choose site language`
Options: `Հայերեն` · `English` · `Русский`
(No French. Do not build a fourth slot.)

**Header lock-up note for the designer:** there is no horizontal logo
lock-up. My copy assumption is that the header shows the **mark alone**
(no wordmark, no tagline) at small sizes, with the wordmark "MemoryCare"
set in Gloock beside it from 900px up. The tagline never appears in the
header — it is a brand asset, not navigation. See §C.1.

### A.1.2 Footer (identical on every page — bank requirement)

```
MemoryCare
Honoring memory, caring for loved ones

Care for family memorial plots in Yerevan cemeteries.
Scheduled visits, photo and video reports, GPS confirmation.

Contact
Hayk Manukyan, Chief Business Development Officer
+374 93 154 108
Davit Hambardzumyan, Chief Executive Officer
+374 55 315 323
info@memorycare.am
We answer on WhatsApp and Viber on both numbers.

Company
MemoryCare LLC, Yerevan, Armenia
Registered address: {LEGAL_ADDRESS}        [OPEN — not supplied]
Company registration number: {REG_NUMBER}  [OPEN — not supplied]

Site
How it works · Pricing · Sample report · Family Circle ·
About · Contacts

Legal
Privacy Policy · Refund Policy · Terms of Service ·
Service Limitations

© 2026 MemoryCare LLC. All rights reserved.
```

Footer note on hours, used verbatim:
`We reply to enquiries within one working day, Yerevan time (UTC+4).`
**[OPEN — CEO must confirm one working day is achievable before this ships.]**

### A.1.3 The two CTAs, everywhere

Primary: `Request a consultation`
Supporting line under it, when there is room:
`Three fields, no account needed. We call you back.`

Secondary: `See pricing` (marketing pages) / `Pay by bank transfer`
(checkout paths).

Never `Learn more`. Never `Register` as a primary action. Never `Order` as a
button that leads to a login form — that is the current site's worst moment.

### A.1.4 The consultation form (used on 6 pages — one component)

```
Heading:     Request a free consultation
Intro:       Tell us where the plot is and how to reach you. We call
             back within one working day, at a time that suits your
             time zone.

Field 1  Label:        Your name
         Placeholder:  —
         Error:        Please enter your name.

Field 2  Label:        Phone or email
         Helper:       Any country. Include the country code for a
                       phone number, for example +1 or +33.
         Error (empty):   Please give us one way to reach you.
         Error (format):  This does not look like a phone number or an
                          email address. Please check it.

Field 3  Label:        Cemetery or city
         Helper:       If you are not sure of the cemetery name, the
                       district or the city is enough.
         Error:        Please tell us roughly where the plot is.

Optional Label:        Anything we should know (optional)
         Placeholder:  For example: the best hours to call you, or who
                       else in the family we should speak to.

Consent checkbox:
         I agree to MemoryCare contacting me about this request.
         Error: Please confirm we may contact you.

Button:  Request a consultation
Button (sending):  Sending…
```

Success state (replaces the form in place, does not navigate away):

```
Thank you. Your request has reached us.

We will call or write within one working day, Yerevan time. If you
would rather not wait, write to us on WhatsApp at +374 93 154 108.

While you wait, this is what a report looks like: See a sample report
```

Failure state:

```
We could not send your request.

The message did not reach us — please try again. If it fails a second
time, write to info@memorycare.am or on WhatsApp at +374 93 154 108
and we will take it from there.

[Try again]
```

---

## A.2 Home

### Block 1 — Hero (proof on the first screen)

```
Eyebrow:   Yerevan cemeteries · scheduled care
H1:        You will see exactly what was done at the grave, and when.

Sub:       MemoryCare looks after your family's memorial plot in
           Yerevan on a fixed schedule. After every visit you get
           photographs, video and the GPS point where our crew stood
           — so you can check the work without taking anyone's word
           for it.

Primary:   Request a consultation
Secondary: See a sample report

Under CTA: Three fields, no account needed. Prices are on the site,
           the same for everyone.
```

**Why this headline.** It is the only sentence that states the product
(proof) and defuses the diaspora's real fear (paying a stranger abroad and
never knowing) in one breath, without a word of guilt and without naming
either audience.

Hero visual, right or below: a **report card**, not the emblem.
Caption under the placeholder image:

```
A visit report. Every one carries the date, the plot, the crew, the
GPS point and the photographs.
```

Placeholder instruction for the developer (visible in the file, not on the
page): `PLACEHOLDER 3:2 — report screen mock. Real photography after the
September shoot.`

### Block 2 — What we do (three columns)

```
Section H2: What a subscription covers

1. We visit on a schedule
   Four or six visits a year, spread across the seasons. Every visit
   is a full visit — cleaning of the whole plot and the monuments,
   not a look around.

2. We clean properly
   Steam, pressure washing, vacuum extraction and chemistry chosen
   for stone. The method is matched to the material, so granite,
   basalt and tuff are treated differently.

3. We prove it
   Photographs before and after, video, and the GPS coordinates
   recorded on site. It arrives in your portal and you can forward
   it to anyone in the family.
```

### Block 3 — The report (the product)

```
H2:   The report is the product
Body: We do not ask you to trust us. Each visit ends with a record:
      the date, the plot, the crew who went, the GPS point, photographs
      of the plot before the work and after it, and a short video.
      It opens on a phone and it can be forwarded by a plain link, so
      relatives who will never sign in to anything can still see it.

CTA:  Open a sample report
```

### Block 4 — Family Circle

```
Eyebrow: Family Circle
H2:      One plot, one family, separate accounts

Body:    Care is rarely one person's decision and it should not be one
         person's inbox. Invite your brother, your aunt, your cousin in
         Moscow. Each of them gets their own access and sees every
         report. You decide who can order extra work and who can change
         the subscription — the person who pays keeps that control.

CTA:     How Family Circle works
```

### Block 5 — Guarantees (trust block; this replaces testimonials)

```
H2:   What we commit to in writing

1. A free repeat visit within 7 days
   If a report does not satisfy you, tell us within seven days and we
   come back and redo the work. You pay nothing for that visit.

2. We answer for damage
   If our crew damages a monument or the plot, we repair or replace it
   at our cost.

3. Cancel and get the rest back
   Cancel an annual subscription at any time and we refund the visits
   you have not had, pro rata. You can do it from the portal, without
   phoning us.

Footnote: The full conditions are in our Terms of Service and Refund
          Policy.
```

Immediately below, in smaller type — the honesty block. This is deliberate
and it is the strongest thing on the page:

```
We started in 2026 and we are taking on our first clients now. We have
no reviews to show you yet and we will not borrow anyone else's. What
we can show you is the method, the prices and the guarantees above —
and after the first visit, your own report.
```

### Block 6 — How it works (short version, links out)

```
H2: How it works

1  A conversation
   You tell us where the plot is. We agree the schedule and the tier.

2  We find and record the plot
   The first visit fixes the exact GPS point and photographs the
   current condition, so every later report is comparable.

3  Visits through the year
   Four or six full visits, spread across the seasons.

4  A report after every visit
   Photographs, video, GPS, and a note from the crew. In the portal
   and by link.

CTA: See how it works in detail
```

### Block 7 — Pricing teaser

```
H2:  Prices, the same for everyone

Body: One price list for clients in Yerevan and clients abroad. Tiers
      cover a plot of up to 16 m² with up to 2 monuments; anything
      larger is calculated openly with the calculator on the pricing
      page.

      Inspection — 20,000 ֏ AMD, a one-off assessment visit
      Express — 65,000 ֏ AMD, one full cleaning visit
      Optimal — 160,000 ֏ AMD a year, four full visits
      Maximum — 200,000 ֏ AMD a year, six full visits

CTA: See full pricing and the calculator
```

### Block 8 — Closing CTA

```
H2:  Talk to us before you decide anything
Body: An annual subscription is a real sum and you have never met us.
      Start with a conversation — we will tell you what the plot needs
      and what it will cost, and you can decide afterwards.
[Consultation form component]
```

**Meta — Home**
Title: `MemoryCare — grave and memorial plot care in Yerevan cemeteries`
Description: `MemoryCare cleans and maintains family graves in Yerevan
cemeteries on a yearly schedule, with photo, video and GPS reports after
every visit. Not a dementia care service. Prices from 20,000 AMD.`

---

## A.3 Pricing

```
H1:  Prices
Sub: One price list. The same for a client in Yerevan and a client in
     Los Angeles. Tiers 1–4 cover a plot of up to 16 m² with up to 2
     monuments — above that, the calculator below shows the exact
     figure before you speak to anyone.
```

### One-off, set apart (own band, above or below the three cards — visually
distinct, never a fourth card in the row)

```
Label:  One-off service
Name:   Inspection · Զննում
Price:  20,000 ֏ AMD, paid once

What it is:
We locate the plot and record it: a written account of its condition,
photographs, video, the GPS point, and a list of the work we recommend
with a price against each item.

No cleaning is carried out on an Inspection visit. It is the way to
find out what state the plot is in and what it would cost, before
committing to a year.

Note: If you take an annual subscription within 60 days, the 20,000 ֏
AMD you paid comes off the subscription price.

CTA: Request a consultation
```

### The three annual subscriptions

```
Section label: Annual subscriptions
Section note:  Every visit is a full visit — the whole plot and all
               monuments, cleaned. There is no smaller kind of visit.
```

**Card 1 — Express** (one-off, but priced as the entry to the year; see
layout note in §C.3)

```
Express
65,000 ֏ AMD, paid once

One full visit. Deep cleaning of the entire plot and the monuments:
steam, pressure washer, vacuum extraction, professional chemistry
matched to the stone.

Includes a full report and access to the client portal.

If you take an annual subscription within 60 days, this 65,000 ֏ AMD
comes off the subscription price.

[Request a consultation]
```

**Card 2 — Optimal** (marked as leading choice)

```
Badge:  Most chosen
Optimal
160,000 ֏ AMD a year

4 full visits — one each season.
Report after every visit: photographs, video, GPS.
Client portal and Family Circle.
Covered by the MemoryCare guarantees.

[Request a consultation]
```

**Card 3 — Maximum**

```
Maximum
200,000 ֏ AMD a year

6 full visits across the year.
Report after every visit: photographs, video, GPS.
Client portal and Family Circle.
Covered by the MemoryCare guarantees.

[Request a consultation]
```

**Card 4 — Special**

```
Special
Priced individually

For plots that do not fit the tiers: more visits a year, a larger area,
more than two monuments, or several family plots in different
cemeteries.

Every Special begins with an Inspection, so that we price real work on
a plot we have seen rather than a guess.

[Start with an Inspection]
```

### Credit — stated plainly, once, under the cards

```
H3:  How the one-off payment is credited

If you have already paid for an Inspection or an Express visit, that
amount comes off the price when you sign an annual subscription.

- The credit applies within 60 days of paying for the one-off service.
- One amount is credited, not two. If you paid for both an Inspection
  and an Express visit, the larger of the two is credited.
- The credit is applied at the moment the annual subscription is
  signed. It does not move between one-off services — an Inspection
  is not credited towards an Express visit.
- Express is 65,000 ֏ AMD every time. There is no reduced repeat price.
```

### Calculator block

```
H2:  Work out the price for your plot
Sub: Tiers cover up to 16 m² and up to 2 monuments. Move the sliders to
     the real size of your plot and you will see the exact annual
     figure. No call needed to find out the price.

Slider 1 label: Plot area
Slider 1 unit:  m²
Slider 1 helper: If you are not sure, an approximate figure is fine —
                 we measure it on the first visit and confirm the price
                 before any work.

Slider 2 label: Number of monuments
Slider 2 helper: Headstones and memorial structures on the plot.

Live output:
  Optimal   {price} ֏ AMD a year
  Maximum   {price} ֏ AMD a year
  Express   {price} ֏ AMD, one-off

Surcharge explainer (always visible, not behind a tooltip):
  Above 16 m²: +10,000 ֏ AMD a year for each additional m².
  Above 2 monuments: +30,000 ֏ AMD a year for each additional monument.
  The same surcharge applies to Optimal and to Maximum.
  For a one-off Express visit: +2,500 ֏ AMD per m² and +7,500 ֏ AMD per
  monument above the same limits.

Ceiling state (area > 100 m² or monuments > 10):
  Heading:  This one we should price together.
  Body:     A plot this size is outside what a calculator can price
            honestly. We start with an Inspection — 20,000 ֏ AMD — and
            give you a written price for the actual work.
  CTA:      Request a consultation
```

### Payment block

```
H2: How to pay

Bank transfer
Most of our first clients pay by bank transfer. We send an invoice with
the full details and confirm in the portal when the payment arrives.
Payments from abroad are normal for us.

Card payment
Card payment on the site is being set up with our bank and is not live
yet. We will not take a card number by phone or by message from anyone.

Every price on this page is in Armenian drams (AMD, ֏). If you see a
figure in dollars or euros anywhere on this site it is an approximate
conversion for orientation only — the amount charged is in AMD.
```

Then the guarantees block (same copy as Home, §A.2 Block 5), then the
consultation form.

**Meta — Pricing**
Title: `Pricing — grave care in Yerevan from 20,000 AMD | MemoryCare`
Description: `What memorial plot care costs in Yerevan: a one-off
inspection from 20,000 AMD, annual subscriptions of four or six full
visits. Cemetery care, not dementia care. Calculator, no call needed.`

---

## A.4 How it works

```
H1:  How it works
Sub: From the first conversation to the report that lands on your phone.
```

```
Step 1 — A conversation
You tell us which cemetery, roughly where the plot is, and who is in
the family. We tell you what the visits would involve and what it would
cost. Nothing is signed on this call.

Step 2 — We find the plot and record it
The first visit is about the plot itself. The crew locates it, records
the GPS point, photographs and films the current condition and writes
down what state the stone and the planting are in. Everything that
comes later is measured against that first record.
If you have taken an Inspection, this is that visit.

Step 3 — The schedule
Optimal is four full visits, one a season. Maximum is six across the
year. We agree the approximate weeks with you and confirm each date in
the portal. If you would like someone met at the plot — a relative in
Yerevan, for instance — you tell us who and we contact them.

Step 4 — The visit
The whole plot and every monument. Steam, pressure washer, vacuum
extraction, chemistry chosen for the stone: granite, basalt and tuff
are not treated the same way. Planting is tidied, rubbish removed,
paths and kerbs cleaned.

Step 5 — The report
Within {REPORT_SLA} of the visit the report is in your portal:
photographs before and after, video, the GPS point, the date and the
crew. You can send it by a plain link to anyone in the family — they do
not need an account and they will not be asked to buy anything.

Step 6 — If something is wrong
Tell us within seven days and we come back and redo the work at our
cost. That is written into our Terms of Service, not offered as a
favour.
```

**[OPEN — `{REPORT_SLA}`.** I need a real number from operations: 24 hours,
48 hours, or "the same day". Until it is agreed, the string reads "shortly
after the visit", which is weak and should not survive to launch.]

**Meta — How it works**
Title: `How MemoryCare works — scheduled grave care in Yerevan`
Description: `How care for a family memorial plot in a Yerevan cemetery
works: the first survey visit, the seasonal schedule, the cleaning method,
and the photo, video and GPS report after each visit.`

---

## A.5 Sample report page

```
H1:  A sample report
Sub: This is what arrives after every visit. Nothing here is decorative
     — each part exists so that you can check the work.
```

Annotated walkthrough:

```
1. The header
   Date, cemetery, plot. The first thing you see is a plain
   confirmation that the visit happened.

2. The GPS point
   The coordinates recorded by the crew's device on the plot, on a map.
   It is how you know the crew was at your plot and not at a
   convenient one nearby.

3. Photographs
   The condition on arrival, then the condition on leaving, in the same
   frames. Full resolution — you can open any of them and look closely.

4. Video
   A short walk around the plot, so that you see it as a whole and not
   only in the frames we chose.

5. The crew's note
   What was done, what we noticed, and anything we think you should
   know — a cracked kerb, a leaning stone, a tree pressing on the plot.

6. What we recommend
   If we think work is needed beyond the subscription, it is listed
   here with a price. It sits at the end, after the report, never
   alongside the photographs.

7. The link
   Every report has a link you can send to the family. It opens without
   an account. It shows the report and nothing else — no prices, no
   offers.
```

Placeholder note for build:
`PLACEHOLDER — full report mock, 4:5 mobile and 16:10 desktop. Real
photography after the September shoot. Neutral brand-colour fills, no
stock imagery of graves under any circumstances.`

**Meta — Sample report**
Title: `A sample visit report | MemoryCare grave care, Yerevan`
Description: `See a real MemoryCare visit report for a Yerevan cemetery
plot: before and after photographs, video, GPS confirmation and the crew's
notes. Memorial plot care, not dementia care.`

---

## A.6 Family Circle

```
H1:  Family Circle
Sub: A grave belongs to a family, not to one inbox.

Body:
One person usually pays and one person usually chases. Everyone else
finds out second-hand. Family Circle is our answer to that: you invite
the people who should see the reports, and each of them gets their own
access.

They do not need to be in Armenia and they do not need to pay anything.
They open the portal, or they open the link you send them, and they see
the same reports you see.
```

### Roles — the permission matrix, in words

```
H2: Who can do what

Owner — the person who pays
Sees every report. Changes or cancels the subscription. Orders extra
work. Invites and removes people. Changes who has which role. There is
one Owner.

Family manager — someone you trust with decisions
Sees every report. Orders extra work at their own cost or asks you to
approve it. Invites viewers. Cannot cancel the subscription and cannot
change the payment details.

Family member — most relatives
Sees every report and every photograph. Can ask for a repeat visit
under the guarantee. Cannot order paid work and cannot change anything
about the subscription.

Guest — someone who opened a link you sent
Sees that one report. Nothing else. No prices, no account, no request
to sign up.
```

Invitation copy (the message a relative receives):

```
Subject: {owner_name} has added you to a family circle on MemoryCare

{owner_name} looks after {plot_label} through MemoryCare and would like
you to see the reports.

You will get access to the photographs, video and details of every
visit. There is nothing to pay and nothing to set up beyond a password.

[Accept the invitation]

If you do not know why you have received this, you can ignore it — the
invitation expires in 14 days and nothing happens.
```

**Meta — Family Circle**
Title: `Family Circle — shared access to grave care reports | MemoryCare`
Description: `Invite relatives anywhere in the world to see every visit
report for your family's plot in a Yerevan cemetery. Separate accounts,
separate permissions. Memorial plot care, not dementia care.`

---

## A.7 About

Bank requirement and a page the diaspora genuinely reads. Short, factual,
no mission statement.

```
H1: About MemoryCare

Who we are
MemoryCare LLC is a company registered in Yerevan, Armenia. We look
after family memorial plots in Yerevan cemeteries on behalf of families
who cannot get there themselves, or who do not have the time to do the
work properly.

What we do
Scheduled cleaning of memorial plots and monuments, using steam,
pressure washing, vacuum extraction and chemistry chosen for the
particular stone. After every visit we produce a report with
photographs, video and the GPS point of the plot, delivered through a
client portal that the whole family can be given access to.

Where we are in 2026
We are at the beginning. The company was founded in 2026 and we are
taking on our first clients now. We are saying that plainly rather than
implying a history we do not have. What we can put in front of you is
our method, our prices, our guarantees and, once we have worked for
you, your own reports.

Who to speak to
Davit Hambardzumyan, Chief Executive Officer — +374 55 315 323
Hayk Manukyan, Chief Business Development Officer — +374 93 154 108
info@memorycare.am
Both numbers take WhatsApp and Viber.

Company details
MemoryCare LLC
Registered address: {LEGAL_ADDRESS}          [OPEN]
Company registration number: {REG_NUMBER}    [OPEN]
Registered in the Republic of Armenia.
```

Nothing about mission, values, history or news. Those pages are what the
current site gets wrong; do not rebuild them.

**Meta — About**
Title: `About MemoryCare — memorial plot care company in Yerevan`
Description: `MemoryCare LLC is a Yerevan company caring for family graves
in Armenian cemeteries, with photo, video and GPS reporting. Not a dementia
care provider. Founded 2026. Company details and contacts.`

---

## A.8 Contacts

```
H1:  Contacts
Sub: A person answers these numbers. If you are calling from abroad,
     any hour is fine — leave a message and we will call back at a time
     that suits you.

Hayk Manukyan — Chief Business Development Officer
+374 93 154 108 · WhatsApp, Viber
Questions about services, prices and starting a subscription.

Davit Hambardzumyan — Chief Executive Officer
+374 55 315 323 · WhatsApp, Viber
Anything you would rather raise with the head of the company,
including a complaint.

info@memorycare.am
Written enquiries, invoices, documents.

Office
{LEGAL_ADDRESS}        [OPEN]
Yerevan, Armenia

Working hours
{WORKING_HOURS}        [OPEN]
We reply to written enquiries within one working day, Yerevan time
(UTC+4).
```

Then the consultation form.

**Meta — Contacts**
Title: `Contact MemoryCare — grave care in Yerevan, Armenia`
Description: `Phone, WhatsApp and email for MemoryCare, a Yerevan company
caring for family memorial plots in Armenian cemeteries. International calls
welcome. Not a dementia care service.`

---

## A.9 Legal pages — structure and framing text

I write the framing, the headings and the plain-language summaries. **A
lawyer supplies the clauses.** Every page carries the same top matter:

```
Last updated: {DATE}
This document applies to MemoryCare LLC, Yerevan, Armenia.
If anything here is unclear, write to info@memorycare.am and we will
explain it in plain language before you commit to anything.
```

House rule for all four pages: **each section opens with one sentence of
plain English in normal type, and the clause follows.** The plain sentence
is mine; the clause is the lawyer's. Older readers in a second or third
language will read the plain sentence and nothing else, and that sentence
must be true on its own.

### A.9.1 Privacy Policy

```
H1: Privacy Policy
Intro: What we record about you and your family's plot, why, and what
       you can ask us to delete.

Sections:
1. Who is responsible for your data — MemoryCare LLC, and how to reach
   the person responsible.
2. What we collect — name, contact details, cemetery and plot details,
   payment records, portal activity.
3. Photographs, video and GPS — the special case. Plain sentence:
   "The photographs and video we take at the plot, and the GPS point of
   the plot, are treated as your family's data. We do not publish them,
   sell them, or use them in our marketing without asking you first,
   in writing, for that specific image."
4. Why we hold it — performing the service, invoicing, legal duties.
5. Who else sees it — the people you invite, our crew, our payment
   provider and our bank. Nobody else.
6. Anyone you invite to Family Circle — what they see and what they do
   not.
7. How long we keep it.
8. Your rights — access, correction, deletion, a copy of your reports.
9. Cookies and site analytics.
10. International transfer — relevant because clients are in the USA,
    France and Russia.
11. How to complain.
[Clauses: lawyer]
```

### A.9.2 Refund Policy

```
H1: Refund Policy
Intro: When you get money back, how much, and how quickly.

Plain summary at the top, above the clauses:
"You can cancel an annual subscription at any time. We refund the
visits you have paid for and not received, in proportion. You do not
need to phone us to do it — it can be done in the portal. Money is
returned by the route it arrived."

Sections:
1. Cancelling an annual subscription — the pro-rata calculation, with a
   worked example in AMD.
2. One-off services — Inspection and Express, before and after the
   visit.
3. A visit we could not complete — what happens if the crew could not
   reach the plot, or the cemetery was closed.
4. The 7-day guarantee re-visit — a repeat visit, not a refund, and why.
5. How long a refund takes and by what route.
6. Bank transfer refunds and international payments.
7. How to ask for a refund and who answers.
[Clauses: lawyer]
```

Worked example, in my words, for section 1 (numbers to be checked by
finance):

```
An example. You pay 160,000 ֏ AMD for Optimal — four visits over the
year. Two visits have taken place and you cancel. Two of the four
visits remain, so we return 80,000 ֏ AMD.
```
**[OPEN — finance must confirm whether the pro-rata basis is visits
delivered or days elapsed. The copy above assumes visits. If it is days,
this example must be rewritten before launch.]**

### A.9.3 Terms of Service

```
H1: Terms of Service
Intro: What we undertake to do, what we need from you, and what happens
       when something goes wrong.

Sections:
1. Who these terms are between.
2. What is included in each product — Inspection, Express, Optimal,
   Maximum, Special — with the 16 m² / 2 monument limit stated.
3. Surcharges above those limits.
4. Scheduling, and what happens when a visit has to move.
5. Your obligations — accurate plot details, the right to authorise
   work on that plot.
6. Reports — what a report contains and how it is delivered.
7. Family Circle — invitations, roles and what an invited person may do
   on your behalf.
8. The MemoryCare guarantees — the 7-day re-visit, liability for
   damage, pro-rata refund. Plain sentence: "These are obligations, not
   goodwill. They apply whether or not you ask nicely."
9. Payment, invoicing and currency. Plain sentence: "Every amount is in
   Armenian drams (AMD, ֏). Any figure shown in another currency is an
   approximation for your convenience."
10. Suspension and termination, by either side.
11. Liability and its limits.
12. Governing law and disputes.
13. Changes to these terms and how we notify you.
[Clauses: lawyer]
```

### A.9.4 Service Limitations

The most useful of the four, and the one that prevents complaints. Framing
and the honest list are mine; the lawyer formalises.

```
H1: What we cannot do
Intro: Some things are outside the service, and some things are outside
       anyone's control. It is better that you know them now than
       discover them in a report.

Sections and plain content:

1. What is not included in a subscription
   Restoration of stone, re-cutting or regilding of lettering, repairs
   to kerbs and foundations, replacement of a monument, and any work
   requiring cemetery administration approval. We can quote for these
   separately.

2. Damage that was there before we arrived
   Cracks, subsidence, weathering and old repairs are recorded in the
   report and not concealed. We are not responsible for them and we
   will not clean over them and call it done.

3. Stone we will not treat aggressively
   Some surfaces — soft, flaking or previously coated stone — can be
   harmed by pressure or by chemistry. Where that is the case we clean
   gently, say so in the report, and explain what we chose not to do.

4. Weather and season
   Frozen ground, heavy rain and snow can make a visit pointless or
   unsafe. We move the visit and tell you the same day. The visit is
   not lost.

5. Access
   Cemetery closures, funerals in progress, construction, blocked
   paths, or a plot that has been enclosed since we last came. We
   photograph the obstruction, tell you, and return.

6. Locating a plot
   If you cannot tell us where the plot is, we search — but on some
   older cemeteries records are incomplete and we may not find it. If
   we do not find it we tell you what we did and refund the Inspection.

7. Planting and flowers
   We tidy and maintain existing planting. New planting and flowers are
   ordered separately.

8. What we will not do
   We do not carry out religious rites, and we do not act on behalf of
   one family member against another. If there is a disagreement inside
   a family about a plot, we pause and wait for it to be settled.
[Clauses where needed: lawyer]
```

**Meta — legal pages**
- Privacy: `Privacy Policy | MemoryCare grave care, Yerevan` /
  `How MemoryCare LLC handles your data, and the photographs, video and
  GPS records of your family's plot in a Yerevan cemetery.`
- Refund: `Refund Policy | MemoryCare grave care, Yerevan` /
  `How to cancel a MemoryCare memorial plot care subscription and how the
  pro-rata refund in AMD is calculated. Cemetery care, not dementia care.`
- Terms: `Terms of Service | MemoryCare grave care, Yerevan` /
  `The terms between MemoryCare LLC and clients whose family graves in
  Yerevan cemeteries we maintain, including the written guarantees.`
- Limitations: `Service limitations — what we cannot do | MemoryCare` /
  `What is not included in MemoryCare grave care in Yerevan: restoration,
  pre-existing damage, weather, access and locating older plots.`

---

## A.10 The client portal

### A.10.1 Sign in / access

```
H1:      Sign in
Sub:     Your reports and your family's plot.
Field:   Email
Field:   Password
Link:    I have forgotten my password
Button:  Sign in
Alt:     Have you been sent a report link? You do not need an account —
         open the link and it will show you the report.

Error (wrong credentials):
  That email and password do not match. Check them and try again, or
  reset your password.
Error (locked):
  Too many attempts. For safety we have paused sign-in for 15 minutes.
  If you need access sooner, call +374 93 154 108.
Error (server):
  We cannot reach the portal at the moment. This is on our side. Try
  again in a few minutes — your reports are safe.
```

Password reset:
```
Sent state:
  If there is an account for {email}, a reset link is on its way. It is
  valid for one hour.
New password:
  Choose a password
  At least 10 characters. A short phrase you will remember is better
  than a complicated word.
Error: Please use at least 10 characters.
Done:  Your password is changed. You can sign in now.
```

### A.10.2 First entry after payment — the doubt screen

The single most important portal screen. The client has paid a large sum and
nothing has happened yet.

```
H1:  Welcome, {first_name}. Everything is set up.

Body:
Your subscription is active and your plot is registered with us. The
first visit is the survey visit — the crew locates the plot, records the
GPS point and photographs its current condition, so that every later
report can be compared with it.

Status card:
  Plot            {cemetery}, {plot_label}
  Subscription    {tier} · {visits_total} full visits a year
  Paid            {amount} ֏ AMD on {date}
  First visit     {date_or_status}

If the first visit date is not yet fixed:
  First visit     Being scheduled — we will confirm the date here and
                  by email, and we will tell you before the crew goes.

What happens next
1. We confirm the date of the first visit.
2. The crew goes and records the plot.
3. Your first report appears here, usually within {REPORT_SLA} of the
   visit.

Meanwhile
[See a sample report]  — so you know what to expect
[Invite your family]   — they will see every report from the first one
[Add a note for the crew] — anything we should know about the plot

Nothing needs doing from you now. If you have a question, Hayk answers
on +374 93 154 108.
```

### A.10.3 Visits list

```
H1: Visits
Filter labels: All · Completed · Scheduled · Moved

Row (completed):
  {date} · {cemetery}, {plot_label}
  Report ready
  [Open report]

Row (scheduled):
  {date} · {cemetery}, {plot_label}
  Scheduled
  Remind me the day before ▸

Row (moved):
  {original_date} → {new_date}
  Moved — {reason_short}
  [Why this moved]

Empty state (no visits yet):
  Heading: No visits yet
  Body:    The first visit has not taken place. When it does, the
           report will be here — photographs, video and the GPS point.
           We will email you the moment it is ready.
  CTA:     See a sample report

Loading state:
  Loading your visits…
  (Skeleton rows. No spinner over a photograph. No animated
  illustration.)

Error state:
  Heading: We cannot load your visits right now
  Body:    This is a problem on our side, not with your subscription or
           your reports. Please try again in a moment.
  CTA:     Try again
  Under:   If it keeps happening, call +374 93 154 108.
```

### A.10.4 Report screen

Block order is fixed by the brief and I agree with it: confirmation first,
photographs after. Before/after as the opening image reads as a
cleaning-product advertisement.

```
1. Confirmation header
   Visit report
   {weekday}, {date}
   {cemetery} · {plot_label}
   Status: Completed
   Crew: {crew_names}

2. GPS
   Label: Recorded on site
   {lat}, {lng} · [Show on map]
   Helper: These coordinates were recorded by the crew's device at the
           plot on {date}.

3. Photographs
   Section heading: Photographs
   Group label 1:   On arrival
   Group label 2:   After the work
   Helper:          Tap any photograph to open it full size.

4. Video
   Section heading: Video from the visit
   Duration: {duration}
   Fallback if no video: No video was recorded on this visit.

5. The crew's note
   Section heading: Notes from the crew
   {note_text}
   Fallback: The crew recorded nothing beyond the work carried out.

6. Recommended work  (Owner and Family manager only — never in a guest
   view, never in a Family member view alongside prices)
   Section heading: Work we would recommend
   Intro: These are not urgent unless we say so. Nothing here happens
          unless you ask for it.
   Item:  {work} — {price} ֏ AMD  [Ask about this]

7. Sharing
   [Copy the link to this report]
   Helper: Anyone with this link can see this report. They will not see
           prices and will not be asked to sign up.
   Confirmation toast: Link copied.
```

Report empty/edge states:
```
Report being prepared:
  Heading: The visit is done. The report is being prepared.
  Body:    The crew has finished at the plot. We are checking the
           photographs and the video before sending them to you — it is
           usually ready within {REPORT_SLA}. We will email you.

Photographs still uploading:
  Some photographs are still uploading. The rest of the report is
  complete.

Report failed to load:
  Heading: We cannot open this report at the moment
  Body:    The report exists and nothing has been lost. This is a fault
           on our side. Please try again shortly.
  CTA:     Try again
```

### A.10.5 Guest view of a shared report

No prices, no upsell, no account prompt. This is roughly half of all opens.

```
Top strip:
  Visit report · MemoryCare
  {cemetery} · {plot_label} · {date}

Body: [Confirmation header, GPS, photographs, video, crew note — as
      above]

Foot of page (the only mention of us):
  This report was made by MemoryCare after a visit to the plot on
  {date}. It was shared with you by {owner_first_name}.
  About MemoryCare

That is all. No pricing link, no "get your own", no sign-up. If we ever
sell next to a photograph of a grave we lose this brand.
```

### A.10.6 Link preview text (OG) for a shared report

The link lands in a family group chat. A photograph of a burial must never
appear in the preview.

```
og:title        Visit report — {date}
og:description  A record of a MemoryCare visit to a family memorial
                plot in {cemetery}. Photographs, video and GPS
                confirmation.
og:image        The MemoryCare mark on a Nude ground. Never a
                photograph from the report. Never a photograph of a
                plot, a monument or a grave — under any circumstances,
                including when the client has shared it publicly.
og:site_name    MemoryCare
```

Shorter variant for WhatsApp's tighter preview:
```
Title:       Visit report — {date}
Description: MemoryCare · {cemetery} · photographs, video and GPS.
```

### A.10.7 Family Circle screens

```
H1: Family Circle
Sub: The people who can see the reports for {plot_label}.

Member row: {name} · {email} · {role}   [Change role] [Remove]

Empty state:
  Heading: No one else has access yet
  Body:    Invite a relative and they will see every report, from the
           first one. There is nothing for them to pay and no
           subscription of their own.
  CTA:     Invite someone

Invite form:
  Their name
  Their email
  What they can do
    ( ) Family member — sees every report. Cannot order work or change
        the subscription. Right for most relatives.
    ( ) Family manager — sees every report and can order extra work.
        Cannot cancel the subscription or change payment details.
  Button: Send the invitation
  Helper: They get an email with a link. The invitation is valid for
          14 days.

Sent:      The invitation is on its way to {email}.
Pending:   Invited {date} — has not accepted yet.  [Send again]
           [Cancel the invitation]

Remove confirmation:
  Heading: Remove {name} from the family circle?
  Body:    They will no longer be able to open reports for this plot.
           Reports you have already sent them by link will still open.
           You can invite them again at any time.
  Confirm: Remove {name}
  Cancel:  Keep their access

Role change confirmation (upgrade to manager):
  Heading: Let {name} order work?
  Body:    A family manager can order extra work on this plot. They
           still cannot cancel the subscription or change payment
           details.
  Confirm: Make {name} a family manager

Validation:
  Error: Please enter their email address.
  Error: This does not look like an email address.
  Error: {email} already has access to this plot.
  Error: You have reached the limit of {n} people on this plot. Remove
         someone, or call us and we will raise it.
```

### A.10.8 Payment and subscription

```
H1: Subscription and payments

Card:
  {tier} · {visits_total} full visits a year
  {amount} ֏ AMD a year
  Plot: {cemetery}, {plot_label}, {area} m², {monuments} monuments
  Renews on {date}
  Paid until {date}

Payment history row:
  {date} · {amount} ֏ AMD · {method} · [Invoice]

Bank transfer pending:
  Heading: We are waiting for your transfer
  Body:    The invoice is below. When the payment arrives — usually one
           to three working days for a transfer from abroad — we will
           confirm it here and by email. Nothing is needed from you in
           the meantime.
  CTA:     Open the invoice   ·   Copy the bank details

Card payment not live:
  Card payment on the site is being set up with our bank. For now we
  invoice and take payment by bank transfer, including from abroad.
  We will never ask you for card details by phone or by message.

Empty state:
  You have no payments recorded yet.

Change plan:
  Heading: Change your subscription
  Body:    Moving between Optimal and Maximum changes the number of
           visits in the year. We recalculate what you have paid and
           tell you the difference before anything is charged.
  CTA:     Talk to us about changing
```

### A.10.9 Cancellation with pro-rata refund — completable without a phone call

```
Step 1
  Heading: Cancel your subscription
  Body:    You can cancel at any time. We will refund the visits you
           have paid for and not received.
  Summary:
    Paid                {amount} ֏ AMD
    Visits completed    {n} of {total}
    Visits remaining    {m}
    Refund              {refund} ֏ AMD
  Helper: The refund goes back the way it came — to the account or card
          you paid from. Bank transfers abroad usually take {n} working
          days.
  CTA:     Continue
  Alt:     Keep my subscription

Step 2 — one question, not a survey, and skippable
  Heading: Before you go — is there anything we could have done?
  Body:    You do not have to answer. If something went wrong with a
           visit or a report, we would rather fix it than lose you.
  Options: The work was not what I expected
           The reports were not what I expected
           It is too expensive
           The plot no longer needs this
           Something in the family has changed
           Another reason
  Free text: Anything you want to tell us (optional)
  CTA:     Cancel my subscription
  Alt:     Actually, I would like to talk to someone first

  [If "the work was not what I expected" or "the reports were not what
  I expected" is chosen, show — once, without pressure:]
    You are entitled to a free repeat visit within 7 days of a report.
    If that would settle it, ask for one — cancelling stays available
    either way.
    [Ask for a repeat visit]  [Continue cancelling]

Step 3
  Heading: Your subscription is cancelled.
  Body:    We have refunded {refund} ֏ AMD to {method}. It usually
           arrives within {n} working days.
           Your reports stay in the portal and the links you have
           shared with your family go on working.
           If you want to come back, nothing is lost — your plot and
           its GPS point stay on record.
  CTA:     Back to my reports
```

### A.10.10 Profile and notifications

```
H1: Your details

Your name
Email                    Helper: Reports and invoices go here.
Phone                    Helper: Any country. Include the country code.
Preferred language       Հայերեն · English · Русский
Time zone                Helper: We use this so that we do not call you
                         at four in the morning.

Notifications
  [ ] Tell me when a report is ready            (default on)
  [ ] Remind me the day before a visit          (default off — opt-in)
      Send that reminder to someone else instead
      Name / phone / email
      Helper: Useful if a relative in Yerevan will meet the crew. They
              will receive only the reminder, not your reports.
  [ ] Tell me before the subscription renews    (default on)

Save:    Save changes
Saved:   Your details are saved.
Error:   We could not save your changes. Nothing has been lost — please
         try again.
```

### A.10.11 Guarantee re-visit request (client-initiated)

```
Entry point on the report screen:
  Link: Something is not right with this visit

Screen:
  Heading: Ask for a repeat visit
  Body:    If this report does not satisfy you, we come back and redo
           the work within seven days of the visit, at our cost. Tell
           us what is wrong so that the crew knows what to look at.
  Field:   What is wrong?
           Placeholder: For example: the kerb on the left is still
           dirty; the stone still has green marks along the base.
  Field:   Add a photograph (optional)
  CTA:     Ask for a repeat visit
  Helper:  We reply the same working day and agree a date with you.

Sent:
  Heading: We have your request.
  Body:    Hayk will contact you today to agree the date. The repeat
           visit is free and it does not use up a visit from your
           subscription.

Outside 7 days:
  Heading: This visit was more than seven days ago
  Body:    The free repeat visit applies within seven days of a report.
           Tell us anyway — if it is our mistake we will still put it
           right.
  CTA:     Tell us what happened
```

---

## A.11 System messages

House rules for all of them: subject line states the fact, first sentence
repeats it, no exclamation marks, no emoji, no marketing footer, plot named
so the recipient knows which one. Every message is sent in the recipient's
chosen language.

### A.11.1 Report ready

```
Subject: Your visit report is ready — {date}
Push:    The report from the visit on {date} is ready.

{first_name},

The crew visited {plot_label} at {cemetery} on {date}. The report is in
your portal: photographs before and after, video, and the GPS point
recorded at the plot.

[Open the report]

You can send this report to the family with a link — they do not need
an account.

MemoryCare · info@memorycare.am · +374 93 154 108
```

### A.11.2 Visit tomorrow (opt-in only)

```
Subject: A visit to {plot_label} tomorrow, {date}
Push:    The crew visits {plot_label} tomorrow.

{first_name},

Our crew is due at {plot_label}, {cemetery}, tomorrow, {date}.

Nothing is needed from you. The report will be in your portal after the
visit.

If you need to move this visit, call +374 93 154 108 or reply to this
message.
```

Version sent to a nominated relative rather than the client:

```
Subject: MemoryCare visits {plot_label} tomorrow, {date}

{recipient_name},

{owner_name} asked us to let you know: our crew is due at
{plot_label}, {cemetery}, tomorrow, {date}, in the {morning/afternoon}.

You do not have to be there. If you would like to meet the crew, call
+374 93 154 108 and we will agree a time.
```

### A.11.3 Visit postponed by weather

```
Subject: The visit to {plot_label} is moving — {new_date}
Push:    Tomorrow's visit is moving because of the weather.

{first_name},

We are moving the visit planned for {old_date}. {weather_reason} —
working in these conditions would not clean the stone properly and it
is not safe for the crew.

The new date is {new_date}.

The visit is not lost. It stays part of your subscription and the
schedule for the rest of the year does not change.

If {new_date} does not suit you, call +374 93 154 108 and we will find
another.
```

`{weather_reason}` is written by the operator, from a short set:
`The ground is frozen` / `Heavy rain is forecast all day` /
`Snow has covered the plot`. Never "adverse weather conditions". Never
"due to circumstances beyond our control".

### A.11.4 Crew could not access the plot

The hardest message in the system. The client is abroad and something at
their family's grave is wrong. Facts, photograph, next step, no apology
theatre and no vagueness.

```
Subject: We could not reach {plot_label} today — what we found
Push:    We could not reach the plot today. There is a photograph and
         a plan.

{first_name},

Our crew went to {plot_label} at {cemetery} today, {date}, and could
not get to the plot.

What we found: {obstruction_description}

We photographed it so that you can see exactly what we saw.

[See the photographs]

What we are doing: we return on {return_date}. {action_taken} You are
not charged for today and the visit stays part of your subscription.

If you would like to speak to someone about it, call Hayk on
+374 93 154 108 — he has the details from the crew.
```

`{obstruction_description}` examples, written by the operator, plainly:
- `The cemetery was closed for a funeral and the section was not open to
  us.`
- `A fence has been put up around the neighbouring plot and it blocks the
  path.`
- `Building materials have been left across the plot.`
- `We could not identify the plot with the details we have.`

`{action_taken}` examples:
- `We have spoken to the cemetery administration and they expect the
  section to be open again by then.`
- `We are asking the cemetery administration who put the materials there.`
- `Could you send us a photograph of the plot, or the name and dates on the
  stone? That is usually enough for us to find it.`

Never: "unfortunately", "we regret to inform you", "unforeseen
circumstances", or an apology longer than the facts.

### A.11.5 Payment received

```
Subject: Payment received — {amount} ֏ AMD
Push:    We have received your payment of {amount} ֏ AMD.

{first_name},

We have received {amount} ֏ AMD for {tier}, for {plot_label} at
{cemetery}.

Your subscription runs to {end_date} and covers {n} full visits.
The invoice is in your portal.

[Open the portal]

The first visit is {first_visit_status}.
```

### A.11.6 Subscription renewing

Sent 30 days before. Not a sales message.

```
Subject: Your subscription renews on {date}
Push:    Your MemoryCare subscription renews on {date}.

{first_name},

Your {tier} subscription for {plot_label} renews on {date} at
{amount} ֏ AMD for the year — {n} full visits.

In the past year we visited {n_completed} times and every report is in
your portal.

Nothing is needed from you. If you want to change the tier, change the
plot details, or stop, you can do all three in the portal or by calling
+374 93 154 108.

[Review my subscription]
```

Note: `{n_completed}` is a count of our own visits with reports behind it,
not a marketing statistic. It is the one number in this document that is
allowed, because the client can click and verify every one.

### A.11.7 Guarantee re-visit — acknowledgement and scheduling

```
Subject: We have your request for a repeat visit — {plot_label}

{first_name},

You told us the report from {date} was not right. We are coming back.

What you told us: "{client_text}"

Hayk will call you today to agree a date. The repeat visit is free and
it does not use one of the visits in your subscription.
```

Then, once scheduled:

```
Subject: The repeat visit to {plot_label} is set for {date}

{first_name},

The crew returns to {plot_label} on {date} to redo the work. They have
your note about {short_summary}.

You will get a new report after the visit, in the usual way.
```

---

## A.12 Buttons, labels, validation, tooltips — the full inventory

### Buttons

```
Request a consultation
See pricing
See a sample report
Open the report
Open a sample report
Copy the link to this report
Invite someone
Send the invitation
Send again
Cancel the invitation
Remove {name}
Keep their access
Make {name} a family manager
Ask for a repeat visit
Tell us what happened
Try again
Save changes
Sign in
Pay by bank transfer
Copy the bank details
Open the invoice
Talk to us about changing
Cancel my subscription
Keep my subscription
Actually, I would like to talk to someone first
Back to my reports
Show on map
```

Never: `Submit`, `OK`, `Learn more`, `Get started`, `Order`, `Buy now`,
`Continue shopping`, `Upgrade`.

### Form labels (canonical spellings)

```
Your name              Their name
Phone or email         Their email
Cemetery or city       Plot area
Email                  Number of monuments
Password               Preferred language
Choose a password      Time zone
What is wrong?         Add a photograph (optional)
Anything we should know (optional)
```

### Validation messages — the full set

```
Empty required:   Please enter your name.
                  Please give us one way to reach you.
                  Please tell us roughly where the plot is.
                  Please enter their email address.
Format:           This does not look like a phone number or an email
                  address. Please check it.
                  This does not look like an email address.
Phone country:    Please include the country code, for example
                  +374, +1 or +33.
Duplicate:        {email} already has access to this plot.
Too short:        Please use at least 10 characters.
Consent:          Please confirm we may contact you.
File too large:   That photograph is larger than {n} MB. Please send a
                  smaller one, or email it to info@memorycare.am.
Wrong file type:  We can accept JPG, PNG and HEIC photographs.
Out of range:     The calculator goes up to 100 m². For a larger plot
                  we price the work after an Inspection.
Expired link:     This invitation has expired. Ask {owner_name} to send
                  it again.
Expired reset:    This password link has expired. Reset links last one
                  hour — request a new one.
Session expired:  You have been signed out for safety. Sign in again —
                  nothing has been lost.
```

Validation tone rules: begin with "Please", name the field's real-world
meaning, never say "invalid", never say "required field", never blame
("You entered…"), never use red words like "Error". No exclamation marks.

### Tooltips and helper text

```
GPS point         The coordinates recorded by the crew's device at the
                  plot, on the day of the visit.
Full visit        The whole plot and every monument on it, cleaned.
                  There is no smaller kind of visit at MemoryCare.
16 m² limit       The tier prices cover a plot of up to 16 m² with up
                  to 2 monuments. Above that, the calculator shows the
                  exact figure.
Pro-rata refund   We refund the visits you have paid for and not yet
                  received.
Family manager    Can see reports and order extra work. Cannot cancel
                  the subscription or change payment details.
Report link       Anyone with the link can see this report. They will
                  not see prices and will not be asked to sign up.
AMD               Armenian dram. All our prices and charges are in AMD.
                  Any other currency shown is an approximation.
```

---

# B. VOICE

## B.1 Three principles, each with a right and a wrong

### Principle 1 — State the fact before the feeling

We are writing to someone who is deciding, often at 1 a.m., whether to give
money to strangers in another country to work at their mother's grave. What
settles that is information: what happens, when, at what cost, and how they
will know it was done. Feeling is what the photographs do. The words carry
the facts.

> **Right:** "The crew visited on 14 September. The report has the
> photographs, the video and the GPS point recorded at the plot."
>
> **Wrong:** "We know how much this place means to you. Our devoted team
> treated it with all the love and respect your family deserves."

The wrong version tells the reader how they feel and tells them nothing they
can check. It also puts our emotion in front of theirs, which is presumptuous.

### Principle 2 — Say what is true, including when it is not flattering

We have no clients, no history and no reviews. Every attempt to disguise
that produces the exact texture the current site has — invented numbers,
stock testimonials — and a reader over forty recognises it instantly. The
admission is the asset: a company that says "we are new, here is our method
and here are our guarantees" is more trustworthy than one claiming a decade.
The same rule holds when something goes wrong: the plain account beats the
apology.

> **Right:** "We started in 2026 and we are taking on our first clients now.
> We have no reviews to show you yet and we will not borrow anyone else's."
>
> **Wrong:** "Trusted by hundreds of Armenian families worldwide." /
> "Years of experience caring for Armenia's memorial heritage."

Corollary for competitors: we never say nobody else does photo reports in
Yerevan. hush.am does, it is checkable in one search, and being caught in
that claim would cost us more than the claim could ever earn. We describe
the combination we actually offer and let it stand.

### Principle 3 — Address a person about their family, never a client about an object

Every noun choice has a warm option and a bureaucratic one. We take the warm
one, without becoming sentimental. "Your family's plot" not "the site".
"Your mother's grave" not "the burial object". "The crew" not "the service
team". And no word in this product ever refers to a person who has died as
a category — no "deceased", no "the departed", no "remains".

> **Right:** "Our crew went to your family's plot at Tokhmakh today and
> could not reach it."
>
> **Wrong:** "The service provider was unable to access the client's burial
> object at the designated location."

The wrong version is not merely cold. It is what an insurance letter sounds
like, and the reader is holding a phone at midnight looking at a photograph
of their father's grave.

## B.2 Stop-list

**Words about death and the person who died — never used**

`deceased` · `the departed` · `the fallen` · `remains` · `body` ·
`burial object` · `the site` (meaning the grave) · `object` · `unit` ·
`property` (meaning the plot) · `disposal` · `disposal of waste` (say
"we take the rubbish away") · `plot maintenance asset` · `resting place`
(a euphemism, and it becomes cloying by the third use) · `passed on` ·
`gone but not forgotten` · `eternal rest` · `final resting place`

Say instead: `the grave` · `your family's plot` · `the plot` ·
`the monument` · `your mother` / `your father` / the relationship the
client used.

**Words that turn a grieving relative into a transaction — never used
in a message to a client**

`client` (in copy addressed to them — we say "you"; "client" is fine in
internal labels and in legal documents) · `user` · `customer` · `lead` ·
`account holder` · `subscriber` (in a message; fine in a status label) ·
`purchase` · `deal` · `offer` · `package deal` · `upsell` · `upgrade
now` · `limited time` · `don't miss` · `act now` · `spots remaining` ·
`only N left`

**Marketing register — never used**

`amazing` · `incredible` · `revolutionary` · `game-changing` ·
`seamless` · `effortless` · `hassle-free` · `peace of mind delivered` ·
`we've got you covered` · `worry-free` · `state-of-the-art` ·
`cutting-edge` · `best-in-class` · `world-class` · `premium experience` ·
`unlock` · `empower` · `elevate` · `curated` · `bespoke` · `journey`
(meaning a process) · `solution` (meaning our service) · `leverage` ·
`bestseller` · `most popular` (we say `most chosen`)

**Guilt — never used, in any construction**

`when was the last time you visited` · `how long has it been` ·
`she would have wanted` · `he deserves better than this` ·
`distance is no excuse` · `you can't be there, but we can` ·
`don't let another year pass` · `while you're away, the grass grows` ·
any before/after pairing whose caption implies neglect by the family
rather than the passage of time.

The reader's absence is a fact, not a failing. If a sentence would make
someone feel worse about not being in Yerevan, it is deleted, however well
it converts.

**Product vocabulary — banned by decision**

`monthly` (for any tier) · `bestseller` · `light visit` ·
`preventive visit` · `basic visit` · `2 full + 4 preventive` ·
`tier 1 / tier 2` in client-facing copy (use the product names) ·
`QR code` · `memory page` · `digital memorial` · `coming soon`
(for anything not yet agreed)

**Punctuation and typography**

- **No exclamation marks.** Not one, anywhere, in any language version.
  Not in the success toast, not in the welcome screen. An exclamation mark
  in this product is a tonal failure.
- **No emoji.** Not in the interface, not in email, not in push, and
  above all not in error states. `Something went wrong 🙁` is the exact
  thing this brand cannot survive.
- **No ALL CAPS** except the logo tagline as delivered.
- **No ellipses for suspense.** `Loading…` only.
- **No rhetorical questions as headlines.**
- **Sentence case for every heading and every button.** Not Title Case.
- Numbers: `4 full visits`, not `four (4) visits`. Dates written out —
  `14 September 2026` — never `14/09/26`, because a US and a European
  reader read that string differently.
- Currency: `160,000 ֏ AMD`. Always both. Never the symbol alone, never
  the code alone, never an abbreviation of the number.

**Constructions to avoid**

- Passive voice where it hides who acted. Not "the visit was postponed" —
  "we are moving the visit".
- "Unfortunately" and "we regret to inform you". Give the fact, then what
  we are doing.
- Apologies longer than the facts. One sentence of regret, at most, and
  only where we were actually at fault.
- Hedges: "may", "might", "should be able to". Either we commit or we say
  we do not know yet.
- Second-person imperatives that scold: "Don't forget to…", "Make sure
  you…".
- "Simply" and "just". Nothing about this is simple for the reader.

## B.3 Two audiences, one voice

They are not two tones. They are one tone answering two different unspoken
questions. Every important block should answer both without naming either.

| | Diaspora, 35–60, abroad | Local premium, 40–60, Yerevan |
|---|---|---|
| Unspoken question | "How do I know this happened at all?" | "Will this be done properly, and do I have to manage it?" |
| Answered by | GPS, video, timestamps, guest links, the guarantees | Method, equipment, stone-specific chemistry, the schedule, "nothing is needed from you" |
| Fear | Paying a stranger abroad; being charged a foreigner's price | Wasting a Saturday; hiring someone careless with the stone |
| Defused by | One price list, visible before any call; a real named person to phone | Named crew, described method, the recommendation section written as information not sales |

**The mechanics of serving both in one sentence.** Lead with the outcome,
which is identical for both. Then let the second sentence carry the two
reasons side by side, in neutral words, without ranking them:

> **Right:** "You will see exactly what was done at the grave, and when.
> Families abroad use it to check the work from another time zone; families
> in Yerevan use it because it saves them the day."
>
> **Wrong (diaspora-only):** "Thousands of kilometres away, you can still be
> there." / "Cheaper than a flight to Yerevan."
>
> **Wrong (local-only):** "Save your Saturday."

Rules that follow:

1. **Never name a country in body copy.** Not "for Armenians in America".
   The moment we do, the Yerevan reader knows the page is not for them.
2. **Time zones, not distance.** "At a time that suits your time zone" is
   useful to the diaspora and invisible to the local reader. "Across the
   miles" is exclusionary and sentimental at once.
3. **Never imply the reader could have gone themselves,** in either
   direction. That sentence wounds one audience and insults the other.
4. **International formats everywhere by default.** Phone fields, dates
   written out, currency always labelled. This is voice, not only
   engineering: it tells a reader in Lyon that we expected them.
5. **One price list, said out loud.** "The same for a client in Yerevan and
   a client in Los Angeles." This single line does more for diaspora trust
   than any amount of warm copy, and costs the local reader nothing. It is
   the one place a country may be named, because it is naming fairness.
6. **Armenian and Russian versions are translations of the meaning, not of
   the words.** Two notes for the localisers: the English "you" must become
   the polite form in Russian (Вы) and Armenian (Դուք) throughout, without
   exception; and the honesty block in §A.2 must be re-argued rather than
   translated literally, because "we are new" carries different weight in
   each market. Flag both to whoever does the localisation.

---

# C. UX AND UI IMPLICATIONS

Places where this copy imposes a requirement on layout. Each is a request to
the design lead, not a suggestion.

## C.1 Header without a horizontal lock-up

There is no horizontal logo lock-up and the tagline is set below the
wordmark. My proposal from the copy side: **header carries the mark alone
below 900px, and mark + "MemoryCare" wordmark in Gloock above it. The
tagline never appears in the header.** It belongs in the footer and on the
first screen of the About page, where it can sit at its designed
proportions. If the designer wants the tagline in the header, it needs a
horizontal lock-up commissioned, and that is a new brand asset, not a
crop.

Consequence: the word "MemoryCare" appears as live text in the header on
desktop. It must be one word, two capitals, and it must never wrap.

## C.2 Long labels, two-line buttons

- `Request a consultation` is 25 characters. At 320px, inside a card with
  padding, it will wrap. **Buttons must be designed to survive two lines**
  with the label centred, or the card CTA becomes `Request a call` — which I
  would rather avoid, since "consultation" signals that nothing is being
  sold on the click.
- `Actually, I would like to talk to someone first` (cancellation flow) is a
  deliberately long tertiary link. It is a text link, not a button, and it
  must be allowed to wrap to three lines on mobile.
- `Copy the link to this report` needs a compact variant for the report
  header on mobile: icon plus `Copy link`, with the full label as the
  accessible name.
- Role names in Family Circle (`Family manager`, `Family member`) must never
  be truncated to `Family man…`. If the row is too narrow, the role moves to
  its own line under the name.

## C.3 Pricing layout — the Inspection and Express problem

The brief requires Inspection to sit apart from the annual subscriptions,
and it also lists Express — a one-off — in the same table as the annual
tiers. That is two one-off products and three annual ones, and a naive
three-card row plus one banner will misrepresent it.

My recommendation: **two bands.**

```
Band 1 — One-off services (Nude ground, wider, less prominent)
  Inspection 20,000 ֏ AMD   |   Express 65,000 ֏ AMD
  With the credit rule stated once beneath the band.

Band 2 — Annual subscriptions (Ivory ground, three cards)
  Optimal (Most chosen) | Maximum | Special
```

This gets Inspection out of the subscription row, puts Express where it
truthfully belongs, and makes the credit rule a property of the band rather
than a footnote on two cards. **[Flagging this as a likely disagreement with
the design lead, who may want a clean four-card row.]**

The `Most chosen` badge needs a place in the card that is not the top-right
corner over a price — I would put it above the product name, as a small
Olive-filled label with Anthracite text. Olive carries no text, so the badge
is Olive **fill** with Anthracite label, which passes.

## C.4 The credit rule needs three lines, not a tooltip

The 60-day credit, one-amount-only, larger-of-the-two rule cannot live in a
tooltip: it is the rule most likely to produce an angry email. It needs a
persistent block under the one-off band, four bullets, always visible on
mobile. A disclosure that hides it is a support cost.

## C.5 Calculator — the surcharge explainer is not a tooltip either

Surcharges must be visible while the slider moves, not behind an info icon.
The diaspora fear the calculator exists to defuse is "a different price for
the American"; a hidden surcharge recreates it. Layout: sliders, then live
prices for all three products, then the four surcharge lines in permanent
smaller type.

The ceiling state (over 100 m² or 10 monuments) replaces the price output
entirely rather than greying it. It is a different message, not a disabled
one.

## C.6 Report screen — the block order costs a design compromise

Confirmation first, photographs second is right and I support it. But it
means the first screenful of the most emotionally loaded page in the product
is a metadata card. To keep it from reading as a receipt, it needs generous
type and air, a single Olive divider, and the GPS map visible as a small
element at the bottom edge of that block — enough visual interest to carry a
first screen without a photograph.

The `On arrival` / `After the work` group labels must be **above** their
groups, not overlaid on the images, and never as a side-by-side slider
handle. A drag-to-reveal before/after control is the cleaning-product idiom
the brief rules out.

## C.7 Recommended work — a hard containment requirement

Prices may appear on the report screen only for Owner and Family manager,
and only in the last block, visually separated by a full-width rule and a
change of ground colour. In the guest view the block does not render at all
— not collapsed, not "sign in to see". Absent.

This is the rule I would defend hardest in this whole document. One upsell
next to a photograph of a grave and the brand is over.

## C.8 Bad-news screens need the same design budget as the good ones

`Crew could not access the plot` is not an error state. It is a report of a
different kind, with a photograph, a reason and a date, and it needs a real
layout: status header in Anthracite on Nude, the operator's plain
description, the photograph, the return date, and a named person to call. If
it is built as a grey alert bar, it will do more damage than the obstruction
did.

The same applies to `postponed by weather`. It is a scheduling card, not a
warning.

## C.9 Error states — a component with a rule attached

Every error in this product follows the same three-part shape: **what
happened, whose fault it is, what to do.** The component must therefore have
three slots (heading, body, action) plus an optional fourth line for the
phone number. It must not accept an icon slot — no warning triangles, no
sad faces — and the illustration slot common to error components must not
exist.

Errors sit on Nude with Anthracite text. Never red. A red panel next to a
photograph of a grave is unacceptable, and Deep Olive is our accent for
everything, including things that went wrong.

## C.10 The honesty block needs to look deliberate

The "we started in 2026, we have no reviews" paragraph sits where a
testimonial carousel would be. If it is styled as small-print it reads as
a disclaimer and does the opposite of its job. It should sit in a bordered
panel on Nude, at body size or a step above, directly under the guarantees,
with the same weight a testimonial would have had. **[Second likely
disagreement: the design lead may want it smaller and further down.]**

## C.11 Currency format has a typographic consequence

`160,000 ֏ AMD` is long and appears inside price cards, calculator output,
tables and buttons. The ֏ glyph is **not present in Gloock** — it must be
verified in the substitute text face (Cabin) and in whatever Armenian
companion is chosen. **[OPEN — this needs a real check by the design lead
before type is locked. If Cabin lacks ֏, we need a fallback for that glyph
alone, and prices cannot be set in Gloock.]** Prices in Gloock at display
size may also need tabular figures, which a single-weight display face may
not offer.

## C.12 Two disclosures I am asking for, and one I am refusing

Asking for:
- **Service limitations** summarised in three lines on the pricing page,
  with a link to the full page. A reader who discovers the limits after
  paying is a refund.
- **Role permissions** as an inline expandable on the invite form, so the
  Owner can check what they are granting without leaving the flow.

Refusing:
- **A cookie-style consent modal on first portal entry.** The first entry
  screen is the moment of maximum doubt and it must not be covered by a
  dialog. Consent belongs in the footer banner and in the form checkbox.

## C.13 Mobile-specific

- The consultation form is the primary conversion on a phone. Four fields
  plus a checkbox must fit above the fold on a 667px viewport with the
  keyboard closed. If it does not, the optional field moves behind a
  `Add a note` disclosure — the optional field, never the cemetery field.
- `Copy the link to this report` must be reachable without scrolling past
  the photographs, because forwarding is the main mobile behaviour. It needs
  a duplicate in a sticky foot bar on the report screen.
- Phone numbers in the footer and on Contacts must be `tel:` links, and the
  WhatsApp mention must be a real `wa.me` link, not text. A 55-year-old in
  Glendale should not be copying digits.

---

## D. Open items I need answered before this ships

1. `{REPORT_SLA}` — how long after a visit is the report ready. Operations.
2. Pro-rata basis — visits delivered or days elapsed. Finance. The worked
   example in the Refund Policy depends on it.
3. `{LEGAL_ADDRESS}`, `{REG_NUMBER}`, `{WORKING_HOURS}` — still placeholders,
   and the bank requires the first two.
4. "Within one working day" — confirmed by the CEO as achievable, or
   softened before launch.
5. Family Circle member limit `{n}` — a number, for the validation message.
6. Legal entity name: this brief says **MemoryCare LLC**, the repo's project
   file says **Memory Care LLC**. Legal pages and the footer must use the
   registered form exactly. Somebody needs to check the registration
   certificate and tell me which it is.
7. Whether the ֏ glyph exists in the chosen text face. See §C.11.
8. Armenian and Russian localisation brief — the two notes in §B.3 item 6
   need to go to the localiser with the copy, not after it.
