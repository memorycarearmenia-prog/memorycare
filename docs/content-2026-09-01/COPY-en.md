# COPY — English site

**Written 01.09.2026. Slot: English copywriter.** Every string below is written
for the English locale directly; nothing here is a translation and nothing here is
written to be translated. Governing documents, in order: `FINAL-REBRAND.md` →
`PROPOSAL-strategy.md` §7 (the register) → `PROPOSAL-ux.md` §2, §3, §10 (structure
and slots) → `docs/rebrand-2026-09-01/BRIEF.md` (the verified facts).

## 0. How to read this file

- Every string carries its slot ID from `PROPOSAL-ux.md` §10 and its character
  count. Counts are `len()` of the exact string, typographic characters and the
  `֏` sign counted as one each. `⚠` marks a string over its budget; there are none
  I have left standing except two, both deliberate and both argued where they appear:
  slot 99 and the server-failure message in slot 110. Both are cases where the budget is
  cheaper to change than the sentence.
- `[BLOCKED — reason]` marks a string I cannot write truthfully today. It is never
  filled with a plausible-looking placeholder.
- English carries **no Armenian words**. The `֏` sign appears throughout, because it
  is the sign for the currency the client is charged in. The single deliberate
  exception is the language switcher, which shows each language in its own script;
  `ՀԱՅ` there is a language label, not copy.
- Currency format, without exception: **`160,000 ֏ AMD`**. Symbol against the numeral,
  the letters after a space. Never `֏` alone, never `AMD` alone, never `160k`.
- Dates are written out: `14 September 2026`. An American and a European reader read
  `14/09/26` differently, and half this audience is American.
- Product names in English are a **proposal**, argued in §L. Everything downstream of
  them in this file uses my recommended set; swapping to the cognate set is five strings.

---

## A. Global chrome — slots 1–18

### Navigation and header — slots 1–5

| Slot | String | ch | Budget |
|---|---|---|---|
| `1.1 nav` | Pricing | 7 | 18 |
| `1.2 nav` | How it works | 12 | 18 |
| `1.3 nav` | Sample report | 13 | 18 |
| `1.4 nav` | Family Circle | 13 | 18 |
| `1.5 nav` | About | 5 | 18 |
| `2 button` | Request a consultation | 22 | 22 |
| `3 link` | Sign in | 7 | 12 |
| `4.1 lang` | ՀԱՅ | 3 | 4 |
| `4.2 lang` | ENG | 3 | 4 |
| `4.3 lang` | РУС | 3 | 4 |
| `5 skip` | Skip to main content | 20 | 24 |
| `descriptor` | Grave care in Yerevan | 21 | 32 |

The **descriptor beside the logo** is copy, not decoration, and it is the same
string as the hero overline (slot 19). It is the site's two-second answer to a reader
who has just searched a brand name that means dementia care in English. It appears in
the header of every page, at every width, and it is never abbreviated to fit.

### Footer — slots 6–12

| Slot | String | ch | Budget |
|---|---|---|---|
| `6.1 col` | Company | 7 | 16 |
| `6.2 col` | Services | 8 | 16 |
| `6.3 col` | Legal | 5 | 16 |
| `6.4 col` | Contact | 7 | 16 |
| `7.1 svc` | Inspection | 10 | 22 |
| `7.2 svc` | Single visit | 12 | 22 |
| `7.3 svc` | Four visits a year | 18 | 22 |
| `7.4 svc` | Six visits a year | 17 | 22 |
| `8.1 legal` | Privacy policy | 14 | 30 |
| `8.2 legal` | Service delivery terms | 22 | 30 |
| `8.3 legal` | Refund policy | 13 | 30 |
| `8.4 legal` | Legal restrictions | 18 | 30 |
| `10 copyright` | © 2026 MemoryCare LLC, Yerevan, Armenia. | 40 | 60 |
| `11.1 role` | Chief Executive Officer | 23 | 24 |
| `11.2 role` | Business development | 20 | 24 |
| `12 hours` | Monday to Friday, 09:00–18:00 in Yerevan (UTC+4) | 48 | 55 |

`11.2` — Hayk Manukyan's full title is Chief Business Development Officer, 33
characters against a 24-character hard budget. The footer and the founder card carry
`Business development`; the About page prints the full title, where there is room for it.

**`9 legal entity`** — footer legal-entity block, budget 160 ch · 304 ch

> MemoryCare LLC [spelling UNCONFIRMED — see below] · Company registration number [BLOCKED — no registration number in any source; Davit or the lawyer supplies it] · Komitas Street 47/1, building 9, 0051 Yerevan, Armenia [address unconfirmed — the archive records it as requiring the lawyer's confirmation]

The publishable form, once both facts are confirmed, fits the budget:

| Slot | String | ch | Budget |
|---|---|---|---|
| `9 legal entity (target form)` | MemoryCare LLC · Registration number {REG_NUMBER} · Komitas Street 47/1, building 9, 0051 Yerevan, Armenia | 106 | 160 |

⚠ **The registered spelling of the entity is itself unconfirmed and is a bank blocker.**
`CLAUDE.md` and the archive §1 say `Memory Care LLC` in two words, the archive §3 hedges
with a slash, and the 31.08 audit rules `MemoryCare LLC` in one word and calls the live
site's two-word form a defect. Nobody has opened the certificate. Whatever the footer,
the copyright line and the About page print must match the registry exactly — a
mismatch is a common reason a bank submission comes back. Every occurrence in this file
is written `MemoryCare LLC` and every one of them is provisional on that certificate.

This is a bank condition and it is currently `0000, Yerevan` with no registration
number on the live site. It is one of the two half-covered conditions in
`FINAL-REBRAND` §4.1 and it is blocked on a person, not on a writer.

### The three frozen strings — slots 16–18

These are written once and used everywhere without variation. A softened or sharpened
copy of any of them anywhere in the product is a defect, not a stylistic choice.

| Slot | String | ch | Budget |
|---|---|---|---|
| `16 callback promise` | We call or write within one business day. | 41 | 48 |
| `17 hours qualifier` | Yerevan business hours, 09:00–18:00 (UTC+4) | 43 | 46 |
| `18 report promise` | Your report arrives within 48 hours of the visit. | 49 | 52 |

Slot 18 deliberately says **your report arrives**, not *appears in your portal*.
`FINAL-REBRAND` §6.3 records that nobody has ruled on what the site may claim about a
portal that is not live on launch day. A report that *arrives* is true whether it
arrives in the portal or as a plain forwardable link, so this string survives either
ruling. Every other portal reference in this file is written the same way. See §O.

---

## B. Home page — twelve sections, slots 19–40

### 1 · Hero — slots 19–23

| Slot | String | ch | Budget |
|---|---|---|---|
| `19 overline` | Grave care in Yerevan | 21 | 32 |
| `20 H1` | Grave care in Yerevan. Every visit documented. | 46 | 48 |
| `22.1 strip` | GPS point at the plot | 21 | 22 |
| `22.2 strip` | 8 photos, 2 videos | 18 | 22 |
| `22.3 strip` | Report within 48 hours | 22 | 22 |
| `5 CTA` | Request a consultation | 22 | 22 |
| `23 support` | No payment now. No account needed. | 34 | 40 |
| `7 link` | See a full report | 17 | 24 |

**`21 standfirst`** — hero standfirst · 101 ch / budget 105

> For families abroad and families in Yerevan with no free weekday: someone goes, and you see the work.

**On the h1.** It carries the category and the city, which is not a style decision:
`memory care` in English is the dementia-care industry's term, and a reader who has
searched the brand name has already been shown Alzheimer's services. The second
sentence is the one thing about us a stranger can go and check — the protocol in
section 3 and the report in section 2 are its evidence. It is a claim we settle on the
same screen, which is the only kind of claim this brand is allowed to open with.

Two alternates, both within budget, if the design lead wants a shorter first line:

| Slot | String | ch | Budget |
|---|---|---|---|
| `20 alt A` | Grave care in Yerevan, on the record. | 37 | 48 |
| `20 alt B` | Grave care in Yerevan. Proof after every visit. | 47 | 48 |

I recommend the primary. `on the record` is an idiom that a 55-year-old reading in a
second language may not carry, and alt B uses *proof* where the page can afford the
plainer *documented* — proof is the reader's word for it, and it is better earned by
them than claimed by us.

**On the standfirst.** It names both reasons — distance and no free weekday — in one
clause each, in the same grammatical position, so neither outranks the other, and
neither reader is addressed as a persona. It contains no *you can't be there*, no
*wherever you are in the world*, and nothing a reader who has not visited in nine
years could read as an accusation. The verb the whole page turns on is in it: **see**.

### 2 · The report — slots 24–26

| Slot | String | ch | Budget |
|---|---|---|---|
| `24 overline` | After every visit | 17 | 24 |
| `24 H2` | What a finished visit looks like | 32 | 44 |
| `26 link` | See the full report | 19 | 24 |

**`24 standfirst`** — report standfirst · 97 ch / budget 100

> Every visit closes with the same record: a GPS point, eight photographs, two videos, a crew note.

The report annotations sit beside the sheet from 1200 and as a numbered list beneath it
below that. Each one names a thing the reader can look at in the sheet next to it.

| Slot | String | ch | Budget |
|---|---|---|---|
| `25.1 annotation` | The GPS point is recorded on site, at the plot, on the day of the visit. | 72 | 90 |
| `25.2 annotation` | Every photograph carries the date and time it was taken, in Yerevan time. | 73 | 90 |
| `25.3 annotation` | Four angles on arrival, the same four after the work, from the same points. | 75 | 90 |

`25.1` is the sentence that separates our GPS from the GPS a reader may have seen
elsewhere in this category, and it does it without mentioning anyone else: ours answers
*was the crew standing there*, not *where is the grave*. The word **verification** does
the work; the word **location** never appears near it.

### 3 · How it works — slots 27–28

| Slot | String | ch | Budget |
|---|---|---|---|
| `27.1 step` | Plan | 4 | 14 |
| `27.2 step` | Visit | 5 | 14 |
| `27.3 step` | Report | 6 | 14 |
| `20 link` | How it works, in full | 21 | 24 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `28.1 step line` | We talk, we find the plot, and we agree what the year looks like. | 65 | 80 |
| `28.2 step line` | The crew works the whole plot and every monument on it, then records it. | 72 | 80 |
| `28.3 step line` | The report reaches you within 48 hours, and you can forward it as a link. | 73 | 80 |

Both frozen promises are printed under the three steps, verbatim: slot 16 with slot 17
beside it, and slot 18. Neither is currently anywhere on the live site, in any language.

### 4 · What a visit includes — slots 29–32

| Slot | String | ch | Budget |
|---|---|---|---|
| `29 H2` | What a full visit includes | 26 | 44 |
| `31 H3` | What we do not do | 17 | 30 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `30.1 label` | The equipment | 13 | 20 |
| `30.2 label` | The chemistry | 13 | 20 |
| `30.3 label` | The crew | 8 | 20 |
| `30.4 label` | The record | 10 | 20 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `30.1 line` | Steam generator, industrial vacuum, soft brushes. High pressure for paths, not for stone. | 89 | 90 |
| `30.2 line` | pH-neutral products only, chosen for the stone: granite, lalvar, basalt or tuff. | 80 | 90 |
| `30.3 line` | The same team is assigned to your plot, and they work the whole plot, not a part of it. | 87 | 90 |
| `30.4 line` | A visit cannot be closed until the GPS point, eight photographs and two videos exist. | 85 | 90 |

`30.1` and `30.2` are where *every visit is a full visit* stops being an assertion. The
second half of `30.1` is a limit stated inside a capability, which is the tone of the
whole section: high pressure cleans a path and destroys polished granite, so we say
which one it is for. No chlorine and no acid on any of the four stones is a rule we
keep and a rule most of this category's viral cleaning videos break.

| Slot | String | ch | Budget |
|---|---|---|---|
| `32.1 not` | No repairs or construction without the municipality's permission. | 65 | 70 |
| `32.2 not` | Nothing on a neighbouring plot, and no other grave in a photograph. | 67 | 70 |
| `32.3 not` | No painting, no moving parts of a monument, without agreeing it first. | 70 | 70 |

Named limits at the same visual weight as capabilities is the cheapest trust device on
the page, and it gives the bank's *legal restrictions* condition a home a human will
actually read. Each item links to `/legal/limitations/`.

### 5 · Tariffs on the home page — slot 30a

The home page carries the five names with their prices as lines, not the card row.
The cards, the credit block and the calculator live on `/pricing/`.

| Slot | String | ch | Budget |
|---|---|---|---|
| `30a sameness` | Every visit is the same full visit. The only difference is how many. | 68 | 70 |
| `home H2` | What it costs | 13 | 44 |
| `42 one price list` | One price list — the same in Yerevan and in Los Angeles. | 56 | 60 |
| `home line 1` | Inspection · 20,000 ֏ AMD · one visit, no cleaning | 50 | 60 |
| `home line 2` | Single visit · 65,000 ֏ AMD · one full visit | 44 | 60 |
| `home line 3` | Four visits a year · 160,000 ֏ AMD · one in each season | 55 | 60 |
| `home line 4` | Six visits a year · 200,000 ֏ AMD | 33 | 60 |
| `home line 5` | Larger or unusual plots · priced after an Inspection | 52 | 60 |
| `home link` | All prices and what is in them | 30 | 40 |

`42` is on the home page as well as the pricing page. A diaspora reader's first
suspicion is that they are being charged a distance premium; the sentence answers it
before it is asked, and naming the two cities is what makes it checkable rather than
reassuring. It is also true in the plainest sense: there is one list.

### 6 · Family Circle — slots 33–36 (dark band)

| Slot | String | ch | Budget |
|---|---|---|---|
| `33 eyebrow` | Included in every year | 22 | 24 |
| `33 H2` | Family Circle | 13 | 40 |
| `36 link` | How Family Circle works | 23 | 24 |

**`33 definition`** — Family Circle definition · 116 ch / budget 120

> One plot, one family, separate accounts: every report is visible to everyone you invite, and only you see the money.

| Slot | String | ch | Budget |
|---|---|---|---|
| `34.1 bullet` | Invite a relative by email or WhatsApp, in a minute. | 52 | 60 |
| `34.2 bullet` | They see every report from the first one, and pay nothing. | 58 | 60 |
| `34.3 bullet` | Only you see prices, invoices and the renewal date. | 51 | 60 |

The sentence that sells this section is not a feature list, and it is the one line on
the page I would fight hardest to keep:

> **Care is rarely one person's decision, and it should not be one person's inbox.**

It describes a family the reader recognises rather than a product we built. It names no
country, no distance and no audience, so the daughter in Nor Nork and the son in
Glendale read the same sentence and both find themselves in it. It sits above the
definition, at H2 weight or just under it. 68 characters.

### 7 · Trust and verification — slot 35

| Slot | String | ch | Budget |
|---|---|---|---|
| `35 H2` | How you can check all of this | 29 | 40 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `35.1 label` | The GPS point | 13 | 22 |
| `35.2 label` | The photographs | 15 | 22 |
| `35.3 label` | The same crew | 13 | 22 |
| `35.4 label` | The people | 10 | 22 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `35.1 line` | Recorded on site, at the plot, on the day. It answers who was there, not where it is. | 85 | 90 |
| `35.2 line` | Four angles on arrival and the same four after the work, taken from the same points. | 84 | 90 |
| `35.3 line` | Your plot is looked after by the same assigned team, and the report names them. | 79 | 90 |
| `35.4 line` | Two named people with published mobile numbers answer this business. Both are below. | 84 | 90 |

`35.3` is worded as an assignment and never as a promise that the roster will not
change — the owner's note of 26.08 flags an unchanged-roster promise as a legal trap as
the company grows, and it is a promise we would eventually break in front of the one
audience that would notice.

### 8 · The honesty panel — slot 36

**`36 honesty panel`** — body size, bordered, never small print · 235 ch / budget 240

> We started in 2026. We have no reviews to show you and we will not borrow anyone else's. What we can show you instead is the method: what happens on a visit, what arrives afterwards, what it costs, and the two people answerable for it.

This is the most persuasive paragraph available to a company with no customers, and it
is persuasive for a structural reason: **an incumbent cannot write it.** Ten years of
reviews are exactly what makes the sentence unavailable to them. It is the one asset we
hold that cannot be copied in an afternoon.

Three things about it are load-bearing and should survive any edit:

- **The date, not a period.** *We started in 2026* is checkable against the company
  register. *We are a young company* is a mood.
- **The refusal, stated as a refusal.** *We will not borrow anyone else's* is the
  sentence that inoculates the reader against the missing testimonials before they
  notice them, and it is a direct answer to what the live site does today — three
  invented testimonials illustrated with photographs of real public figures.
- **The colon, and what follows it.** An admission with nothing after it is an excuse.
  The four items after the colon are each a link to a place on this site where the
  reader can go and look.

It is set at body size or one step above, inside a 1px border, on the page ground.
Set as small grey print it becomes a disclaimer and does the opposite of its job.

### 9 · Founders — slot 37

| Slot | String | ch | Budget |
|---|---|---|---|
| `37.1 name` | Davit Hambardzumyan | 19 | 32 |
| `37.1 role` | Chief Executive Officer | 23 | 24 |
| `37.1 line` | Owns the company and answers for it. +374 55 315 323 | 52 | 70 |
| `37.2 name` | Hayk Manukyan | 13 | 32 |
| `37.2 role` | Business development | 20 | 24 |
| `37.2 line` | Answers the phone, and calls you back. +374 93 154 108 | 54 | 70 |
| `founders note` | Both numbers take WhatsApp and Viber. | 37 | 60 |

Numbers are live `tel:` and `wa.me` targets, not text. A founder's published mobile
outweighs seventy anonymous reviews for a person deciding at one in the morning whether
to send money to a country they do not live in, and it costs us nothing but the
willingness to answer it.

### 10 · FAQ — slots 38–39, six items, the first one open

**1.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `38.1 Q` | I am not sure exactly where the plot is. Can you still help? | 60 | 70 |

**`39.1 A`** · 301 ch / budget 320

> Yes. The cemetery, the district or just the city is enough, and “not sure” is a valid answer on our form. Finding the plot is the first thing an Inspection does: we locate it, record its GPS point, photograph and film its condition, and send you a written inventory with a price for the work it needs.

**2.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `38.2 Q` | What happens if the crew cannot reach the plot? | 47 | 70 |

**`39.2 A`** · 241 ch / budget 320

> We tell you the same day, with the crew's account of why — a funeral, a closed section, a dispute about access. The visit is not lost and it does not come out of your year. We go back, and you have the new date before you have to ask for it.

**3.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `38.3 Q` | What happens in winter? | 23 | 70 |

**`39.3 A`** · 317 ch / budget 320

> The winter visit runs in a suitable weather window rather than on a fixed date, because the limit is temperature: washing stone at or below +4…+10 °C, or with a frost due within 48 hours, damages it. If no window opens, the winter visit is added to spring. Four full visits either way. That is a term of the contract.

**4.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `38.4 Q` | Can the rest of my family see the reports without paying? | 57 | 70 |

**`39.4 A`** · 312 ch / budget 320

> Yes. Family Circle is part of every annual subscription. You invite relatives by email or WhatsApp, and they see every report from the first one, with nothing to pay and no subscription of their own. Prices, invoices and the renewal date stay visible to you alone. A report can also be forwarded as a plain link.

**5.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `38.5 Q` | How should I compare grave-care services? | 41 | 70 |

**`39.5 A`** · 311 ch / budget 320

> Five questions worth asking anyone, including us. What exactly is done on one visit, and on how much of the plot? What arrives afterwards, and how soon? Can the rest of the family see it without paying? Is the full price list published, including the cases that cost more? Who is accountable, by name and phone?

**6.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `38.6 Q` | What happens after I request a consultation? | 44 | 70 |

**`39.6 A`** · 289 ch / budget 320

> We call or write within one business day, Yerevan business hours, 09:00–18:00 (UTC+4). Hayk writes on WhatsApp from +374 93 154 108 first and calls only if you would rather talk. The conversation is about your plot and what it needs. Nothing is sold in it, and it costs nothing to have it.

The comparison question is the contested one. My judgement, and the four rewrites it
took to get there, are in §M. Short version: it ships, at five items, one fewer than
proposed, and the cut item is the reason.

### 11 · The consultation form — slot 40

| Slot | String | ch | Budget |
|---|---|---|---|
| `40 heading` | Request a free consultation | 27 | 44 |
| `40 support` | Three fields, one business day, no payment and no account. | 58 | 90 |

Full form copy — labels, helpers, validation, success, failure — is §J.

### 12 · Footer

Slots 6–12 above. The footer is a bank condition before it is a design element: real
contacts on every page, the legal entity, the registration number, the address. It is
also where the language switcher lives at every width, alongside the header.

---

## C. Pricing page — slots 41–76

### Page head — slots 41–43

| Slot | String | ch | Budget |
|---|---|---|---|
| `41 H1` | Grave care in Yerevan — prices | 30 | 40 |
| `41 subhead` | Five products, four published prices, and the formula for the fifth. | 68 | 90 |
| `42 one price list` | One price list — the same in Yerevan and in Los Angeles. | 56 | 60 |
| `43 sameness` | Every visit is the same full visit. The only difference is how many. | 68 | 70 |
| `72 payment term` | Paid once, for the year. | 24 | 40 |

`43` does most of the comparison work on this page, and it is the sentence the
26.08 decision made available: with the light/heavy split rejected, the difference
between the three annual products is a number and nothing else. It sits directly under
the row heading, where a reader looking for the catch will find it first.

### The entry rail — slots 44–45

| Slot | String | ch | Budget |
|---|---|---|---|
| `44 name` | Inspection | 10 | 22 |
| `44 description` | One visit, no cleaning: we find the plot, record its condition and price the work needed. | 89 | 90 |
| `44 CTA` | Book an Inspection | 18 | 20 |
| `45 chip` | NOT A SUBSCRIPTION | 18 | 26 |
| `price` | 20,000 ֏ AMD | 12 | — |

The Inspection is the easiest yes on the page and the shared door for both readers: for
someone abroad it answers *I do not even know what condition it is in*; for someone in
Yerevan it is a cheap test of whether we are any good. Its description says **no
cleaning** in the first six words, because the one way to lose this sale badly is to
let a reader think they bought a clean.

The strongest thing about the product is the last word of the description and it should
never be cut: what arrives is a written inventory **with a price on the work**. Nobody
else in this reader's tabs is quoting them anything without a phone call.

### The three cards — slots 46–56

| Slot | String | ch | Budget |
|---|---|---|---|
| `46.1 name` | Inspection | 10 | 22 |
| `46.2 name` | Single visit | 12 | 22 |
| `46.3 name` | Four visits a year | 18 | 22 |
| `46.4 name` | Six visits a year | 17 | 22 |
| `46.5 name` | By arrangement | 14 | 22 |
| `47.1 chip` | ONE-OFF | 7 | 12 |
| `47.2 chip` | PER YEAR | 8 | 12 |
| `48.1 caption` | one full visit | 14 | 20 |
| `48.2 caption` | full visits a year | 18 | 20 |
| `56 badge` | Our recommendation | 18 | 22 |

The names are argued in §L. Everything below uses them.

**Single visit — 65,000 ֏ AMD**

| Slot | String | ch | Budget |
|---|---|---|---|
| `49.1 pitch` | One full visit, whenever you ask for it. | 40 | 56 |
| `52.1 arithmetic` | 65,000 ֏ AMD · one full visit | 29 | 44 |
| `53.1a feature` | The whole plot and every monument, cleaned. | 43 | 54 |
| `53.1b feature` | Steam, vacuum, pH-neutral chemistry for the stone. | 50 | 54 |
| `53.1c feature` | An assigned crew, named in your report. | 39 | 54 |
| `53.1d feature` | 8 photographs, 2 videos, a GPS point, a crew note. | 50 | 54 |
| `54.1 credit` | Credited in full into a year taken within 60 days. | 50 | 60 |
| `55.1 CTA` | Book a single visit | 19 | 20 |

**Four visits a year — 160,000 ֏ AMD · our recommendation**

| Slot | String | ch | Budget |
|---|---|---|---|
| `49.2 pitch` | Four full visits, one in each season. | 37 | 56 |
| `52.2 arithmetic` | 160,000 ֏ AMD a year · 40,000 ֏ a visit | 39 | 44 |
| `53.2a feature` | The whole plot and every monument, every visit. | 47 | 54 |
| `53.2b feature` | Steam, vacuum, pH-neutral chemistry for the stone. | 50 | 54 |
| `53.2c feature` | The same assigned crew at every visit. | 38 | 54 |
| `53.2d feature` | Family Circle: every report, for the whole family. | 50 | 54 |
| `54.2 credit` | An Inspection or a single visit is credited into this. | 54 | 60 |
| `55.2 CTA` | Choose four visits | 18 | 20 |

**Six visits a year — 200,000 ֏ AMD**

| Slot | String | ch | Budget |
|---|---|---|---|
| `49.3 pitch` | Six full visits across the year. | 32 | 56 |
| `52.3 arithmetic` | 200,000 ֏ AMD a year · ≈33,300 ֏ a visit | 40 | 44 |
| `53.3a feature` | The whole plot and every monument, every visit. | 47 | 54 |
| `53.3b feature` | Steam, vacuum, pH-neutral chemistry for the stone. | 50 | 54 |
| `53.3c feature` | The same assigned crew at every visit. | 38 | 54 |
| `53.3d feature` | Family Circle: every report, for the whole family. | 50 | 54 |
| `54.3 credit` | An Inspection or a single visit is credited into this. | 54 | 60 |
| `55.3 CTA` | Choose six visits | 17 | 20 |

Three of the four feature lines are identical across the three cards, and that is the
design, not laziness: the row is a picture of `43`. The per-visit arithmetic under each
price is the answer to the only real objection this price list faces — 40,000 ֏ a visit
is a large number until you know what a visit is, and the two lines above it say what a
visit is. Never dressed as a saving: no `save`, no `only`, no struck-through figure,
no badge on the 95,000.

### The year rail — slots 50–51

| Slot | String | ch | Budget |
|---|---|---|---|
| `50.1 season` | Spring | 6 | 10 |
| `50.2 season` | Summer | 6 | 10 |
| `50.3 season` | Autumn | 6 | 10 |
| `50.4 season` | Winter | 6 | 10 |

**`51 footnote`** · 114 ch / budget 120

> The winter visit runs in a suitable weather window. If none opens, it is added to spring — four visits either way.

### The credit block — slots 57–60

| Slot | String | ch | Budget |
|---|---|---|---|
| `57 headline` | Starting small costs you nothing. | 33 | 34 |
| `57 subline` | Whichever way you begin, the first year is 160,000 ֏ AMD and four full visits. | 78 | 90 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `58.1 worked` | Four visits a year, bought outright: 160,000 ֏ AMD. | 51 | 80 |
| `58.2 worked` | Inspection first, then the year: 20,000 + 140,000 = 160,000 ֏ AMD. | 66 | 80 |
| `58.3 worked` | A single visit first, then the year: 65,000 + 95,000 = 160,000 ֏ AMD. | 69 | 80 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `59.1 bullet` | One credit for each plot, once, when the annual subscription is signed. | 71 | 80 |
| `59.2 bullet` | One amount only. If you have paid for both, the larger of the two is credited. | 78 | 80 |
| `59.3 bullet` | Sixty days from the visit. You are shown the date the credit runs out. | 70 | 80 |
| `59.4 bullet` | There is no cheaper repeat single visit. It is 65,000 ֏ AMD every time. | 71 | 80 |
| `60 expiry` | Credit available until 14 October 2026 | 38 | 46 |

This block is the best fact the business has and it should be read as arithmetic, not
as an offer. The heading is a consequence of a sum, printed above the sum: the cautious
route into the first year is not punished, and we can show it in three lines rather
than promise it in one. Nothing in it may be styled as a discount — the credit is money
the client already paid, carried forward.

`60` is a plain date, never a countdown. A timer on this purchase is a pressure device.

### The fifth card — slots 61–62

| Slot | String | ch | Budget |
|---|---|---|---|
| `61 name` | By arrangement | 14 | 22 |
| `61 definition` | For a plot over 16 m², more than two monuments, more than six visits, or several family plots. | 94 | 110 |
| `61 price floor` | A visit here is never priced below one in a six-visit year. | 59 | 60 |
| `61 entry rule` | It begins with an Inspection: we price the work after seeing the plot, not before. | 82 | 110 |
| `62.1 CTA` | Book an Inspection | 18 | 26 |
| `62.2 CTA` | Request a consultation | 22 | 26 |

The entry rule is the persuasive line on this card and it should be given the weight of
one, not buried as a condition. Nobody can price a 40 m² plot with five monuments from a
description over the phone, and a company that quotes one anyway is guessing with the
reader's money. Stated in that order — the benefit, then the requirement — a hurdle
becomes the reason to trust the number.

### The calculator — slots 63–70

| Slot | String | ch | Budget |
|---|---|---|---|
| `63 heading` | What a larger plot costs | 24 | 40 |
| `63 open formula` | The same formula for everyone. Nothing is decided on the phone. | 63 | 80 |
| `64.1 chip` | Four visits a year | 18 | 22 |
| `64.2 chip` | Six visits a year | 17 | 22 |
| `64.3 chip` | A single visit | 14 | 22 |
| `65.1 slider` | Plot area | 9 | 20 |
| `65.2 slider` | Monuments | 9 | 20 |
| `65.1 caption` | Up to 16 m² is included | 23 | 28 |
| `65.2 caption` | Up to 2 are included | 20 | 28 |
| `66.1 row` | Base price | 10 | 24 |
| `66.2 row` | Plot area | 9 | 24 |
| `66.3 row` | Monuments | 9 | 24 |
| `66.4 row` | Total for the year | 18 | 24 |
| `67 default` | Standard plot — 160,000 ֏ AMD. No surcharge. | 44 | 50 |
| `68 ceiling` | Larger than this we price individually, after an Inspection. | 60 | 90 |
| `70.1 aria` | {n} square metres | 17 | 30 |
| `70.2 aria` | {n} monuments | 13 | 30 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `69.1 rate` | 160,000 ֏ ÷ 16 m² = 10,000 ֏ a square metre a year. An added metre costs what an included one costs. | 100 | 110 |
| `69.2 rate` | For a single visit the surcharge is the annual one divided by four — one visit instead of four. | 95 | 110 |

`69.1` is the whole argument for publishing a formula rather than quoting on request,
and it is unusually strong because the arithmetic is clean: the surcharge is not a
penalty for a large plot, it is the same rate the base price is built from. A reader can
verify that in their head in four seconds, which is what makes it persuasive.

`68` is neutral copy, never in the error colour. Passing 100 m² is a normal outcome and
a route to an Inspection, not a mistake the reader made.

### The ritual row — slot 71

| Slot | String | ch | Budget |
|---|---|---|---|
| `71 heading` | Add to any visit | 16 | 20 |
| `71.1 label` | Flowers | 7 | 18 |
| `71.2 label` | A candle | 8 | 18 |
| `71 line` | The crew places them at the plot and photographs them in the report. | 68 | 70 |

**`71 price` — [BLOCKED — no source in the archive gives flowers or a candle a price.**
**Owner decision of 26.08 §7.5 requires the option to be visible on this page; the**
**number does not exist. → Davit.]** The row cannot ship without it: an add-on with no
price on a page whose argument is published prices would undo the page. It is one number.

### Guarantees — slots 73–74

| Slot | String | ch | Budget |
|---|---|---|---|
| `73.1 name` | A repeat visit within 7 days | 28 | 30 |
| `73.2 name` | Damage we cause | 15 | 30 |
| `73.3 name` | A refund if you cancel | 22 | 30 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `74.1 remedy` | If a report is not what we promised, we do the visit again at our cost, within 7 days of the report reaching you. | 113 | 120 |
| `74.3 remedy` | We refund the visits not yet made: the amount you paid × visits remaining ÷ visits total, rounded up in your favour. | 116 | 120 |

`74.1` counts the seven days **from the report reaching you**, not from the visit, so a
late report cannot eat the window. That is the detail that makes it a guarantee rather
than a sentence.

**`74.2 remedy` — [BLOCKED — the liability figure and the policy reference are not**
**settled. The archive records liability and worker insurance as open, and the owner's**
**own decision of 26.08 §7.2 requires an amount, not the word “insured”. → lawyer.]**
Until it is bound, guarantee 2 does not appear on the site at all. A guarantee we cannot
honour is worse than no guarantee, and this is the one a reader would test.

The publishable form, once the figure exists, is one sentence of this shape:
`If we damage the monument, we repair it at our cost, up to {amount} ֏ AMD, under policy {ref}.`

| Slot | String | ch | Budget |
|---|---|---|---|
| `75 payment reality` | Today you pay by bank transfer against a short contract. Card payment opens when the bank enables it; we promise no date. | 121 | 130 |

Never a date. Card acquiring depends on Ameriabank clearing the site conditions, and a
missed date on the payment line is the worst available first broken promise.

### Pricing FAQ — slot 76, six items

**1.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `76.1 Q` | Do prices differ for clients outside Armenia? | 45 | 70 |

**`76.1 A`** · 240 ch / budget 300

> No. One price list, the same for a client in Yerevan and a client in Los Angeles, in Armenian drams. Any figure we show in dollars or euros is approximate and moves with the exchange rate; the amount charged is the dram amount on this page.

**2.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `76.2 Q` | Is a second single visit cheaper? | 33 | 70 |

**`76.2 A`** · 198 ch / budget 300

> No. A single visit is 65,000 ֏ AMD every time. If you take an annual subscription within 60 days of one, the whole 65,000 ֏ is credited into it, and that visit counts as the first visit of the year.

**3.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `76.3 Q` | Does a larger plot cost more? | 29 | 70 |

**`76.3 A`** · 275 ch / budget 300

> Up to 16 m² and two monuments, no: the published price is the price. Beyond that there is one formula, the same for everyone: +10,000 ֏ AMD a year for each square metre above 16, and +30,000 ֏ AMD a year for each monument above two. The calculator above shows the arithmetic.

**4.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `76.4 Q` | Can I pay in instalments, or season by season? | 46 | 70 |

**`76.4 A`** · 156 ch / budget 300

> No. A subscription is paid once, for the year. Paying in parts was considered and decided against, and we would rather say so on this page than at checkout.

**5.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `76.5 Q` | Can I pay with a card issued outside Armenia? | 45 | 70 |

**`76.5 A`** · 196 ch / budget 300

> Not yet. Today payment is by bank transfer against a short contract, and we send the instructions and the invoice. Card payment opens when the bank enables it, and we do not promise a date for it.

**6.**
| Slot | String | ch | Budget |
|---|---|---|---|
| `76.6 Q` | What happens if winter never allows a visit? | 44 | 70 |

**`76.6 A`** · 244 ch / budget 300

> The visit is added to spring, and you receive four full visits. Washing stone at or below +4…+10 °C, or with a frost due within 48 hours, damages it, so the winter visit runs in a weather window rather than on a date. The count does not change.


---

## D. How it works — slots 77–84

| Slot | String | ch | Budget |
|---|---|---|---|
| `77 H1` | How grave care in Yerevan works | 31 | 40 |
| `77 standfirst` | What happens, in what order, and what we do not do. No account is needed to read this. | 86 | 100 |

### The four steps — slot 78

**Step 1**
| Slot | String | ch | Budget |
|---|---|---|---|
| `78.1 label` | 01 | 2 | 14 |
| `78.1 heading` | You ask | 7 | 30 |

**`78.1 body`** · 220 ch / budget 220

> You send three fields, or write on WhatsApp. We call or write within one business day, Yerevan business hours, 09:00–18:00 (UTC+4). The conversation is about the plot: where it is, what is on it, what condition it is in.

**Step 2**
| Slot | String | ch | Budget |
|---|---|---|---|
| `78.2 label` | 02 | 2 | 14 |
| `78.2 heading` | We find the plot | 16 | 30 |

**`78.2 body`** · 217 ch / budget 220

> Yerevan's cemeteries are not usefully mapped, so this comes first. We locate the plot and record its GPS point; every crew after that goes to those coordinates. If you do not know exactly where it is, this answers it.

**Step 3**
| Slot | String | ch | Budget |
|---|---|---|---|
| `78.3 label` | 03 | 2 | 14 |
| `78.3 heading` | The crew visits | 15 | 30 |

**`78.3 body`** · 215 ch / budget 220

> Before the work: the GPS point, four photographs from four fixed angles, and a walk-round video of 20–40 seconds. Then the work, on the whole plot and every monument. Then the same four angles, and the second video.

**Step 4**
| Slot | String | ch | Budget |
|---|---|---|---|
| `78.4 label` | 04 | 2 | 14 |
| `78.4 heading` | The report reaches you | 22 | 30 |

**`78.4 body`** · 197 ch / budget 220

> Your report arrives within 48 hours: eight photographs, two videos, the GPS point, the date and time, and the crew's note. You can forward it as a plain link, and whoever opens it needs no account.

The step headings are verbs with a subject: *you ask*, *we find*, *the crew visits*,
*the report reaches you*. Nobody in this sequence is left ambiguous, which is the whole
point of the page for a reader who cannot come and look.

### What a full visit includes — slot 79

| Slot | String | ch | Budget |
|---|---|---|---|
| `79.1` | The whole plot and every monument on it, every time. | 52 | 60 |
| `79.2` | Steam cleaning of the stone, with a steam generator. | 52 | 60 |
| `79.3` | Industrial wet-and-dry vacuum extraction. | 41 | 60 |
| `79.4` | Soft brushes and plastic scrapers only. No wire, ever. | 54 | 60 |
| `79.5` | pH-neutral products, chosen for the stone under them. | 53 | 60 |
| `79.6` | Weeding, clearing, levelling, and the rubbish taken away. | 57 | 60 |
| `79.7` | High pressure for paths and railings, not for monuments. | 56 | 60 |
| `79.8` | A tripod, so the before and after angles match. | 47 | 60 |

`79.8` is the least obvious item and one of the most persuasive: matching before and
after angles is a discipline, not a camera, and it is the reason two photographs of the
same stone can be compared at all. It is also the sentence that tells a suspicious
reader we are not selecting flattering angles after the fact.

### What we do not do — slot 80

| Slot | String | ch | Budget |
|---|---|---|---|
| `80.1` | No chlorine and no acid, on any stone, for any reason. | 54 | 70 |
| `80.2` | No repairs or construction without the municipality's permission. | 65 | 70 |
| `80.3` | No work on a neighbouring plot, and no other grave in a photograph. | 67 | 70 |
| `80.4` | No painting or moving parts of a monument without agreeing it first. | 68 | 70 |

`80.1` is a limit that reads as an advantage to anyone who has seen a headstone ruined
by bleach and a wire brush, which is most local readers over fifty. Chlorine leaves
sodium salts in the pores and they crystallise and split the stone from inside; on tuff,
with 28% porosity, it is irreversible. The page says the rule; `/legal/limitations/`
carries the reasoning in full.

**`81 weather and access`** · 379 ch / budget 420

> Stone cannot be washed at or below +4…+10 °C, or with a frost due within 48 hours: water in the pores freezes and the surface goes. So the winter visit runs in a weather window rather than on a date. If no window opens all winter, that visit is added to spring — two visits in spring — and you still receive four full visits. It is a term of the contract, not an exception to it.

| Slot | String | ch | Budget |
|---|---|---|---|
| `82 not everything is steamed` | We do not steam a monument that does not need it. Cleaning stone harder than it needs is how stone gets damaged. | 112 | 130 |
| `83 assigned crew` | Your plot is looked after by the same assigned team. | 52 | 60 |

**`84 first visit`** · 216 ch / budget 220

> The first visit of a subscription is a full visit like every other, and usually the longest, because a plot nobody has worked on takes longer. It is not a survey: the Inspection is the survey, and a separate product.

`83` is an assignment and not a promise about a roster. `84` exists because with the
light/heavy vocabulary gone there is a real risk the first visit quietly becomes a
survey again in someone's copy; it says the opposite in two sentences.

---

## E. Sample report — slots 85–89

| Slot | String | ch | Budget |
|---|---|---|---|
| `85 H1` | What a visit report contains | 28 | 40 |
| `85 header line` | A real report, with placeholder photographs until our own are taken in September. | 81 | 90 |

The page shows the component honestly. There is no stock photograph of a stranger's
grave anywhere on this site, and the media slots say what they are until the September
shoot fills them. A labelled placeholder costs us nothing; a stock cemetery photograph
used to sell care of someone's mother is a liability we would deserve.

| Slot | String | ch | Budget |
|---|---|---|---|
| `86.1 block` | Confirmation | 12 | 22 |
| `86.2 block` | GPS point | 9 | 22 |
| `86.3 block` | On arrival | 10 | 22 |
| `86.4 block` | After the work | 14 | 22 |
| `86.5 block` | Crew note | 9 | 22 |
| `86.6 block` | Next visit | 10 | 22 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `87.1 annotation` | The date, the cemetery, the sector and the plot. The name on the monument is off unless you turn it on. | 103 | 130 |
| `87.2 annotation` | The GPS point is recorded on site, at the plot, on the day. It answers who was there, not where the plot is. | 108 | 130 |
| `87.3 annotation` | Four angles on arrival and the same four after the work, from the same points, each with its date and time. | 107 | 130 |
| `87.4 annotation` | The crew's own note: what they found, what they did about it, and anything you should know. | 91 | 130 |

**`88 link preview`** · 190 ch / budget 200

> You can send a report to the family as a plain link: no account, no password, nothing to sign up for. The chat preview carries our mark, “Visit report” and the date — no photograph, no name.

The last sentence is the one that matters and it is a deliberate product decision, not
a technical note: the link gets forwarded into a family group chat, and a photograph of
a grave appearing unannounced on somebody's phone is not something we cause to happen.

| Slot | String | ch | Budget |
|---|---|---|---|
| `89 question` | How would you like to receive reports, and do you want to know before a visit? | 78 | 80 |
| `89.1 checkbox` | Send each report as a link I can forward | 40 | 56 |
| `89.2 checkbox` | Tell me the day before a visit | 30 | 56 |
| `89.3 checkbox` | Send the day-before message to someone else | 43 | 56 |

Asked once, at signup or on first entry, and changeable afterwards. `89.1` is on by
default because about half of all report opens are by people without accounts. `89.2` is
off by default, by owner decision.

---

## F. Family Circle page — slots 90–95

*Adjacent to the assigned scope; written because the home-page band (slots 33–36)
cannot be judged without the page it links to.*

| Slot | String | ch | Budget |
|---|---|---|---|
| `90 H1` | Family Circle — grave care in Yerevan | 37 | 40 |
| `90 definition` | One plot, one family, separate accounts: every report is visible to everyone you invite, and only you see the money. | 116 | 120 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `91.1 step` | You invite a relative by email or by WhatsApp, with a message from you. | 71 | 90 |
| `91.2 step` | They open the invitation and land on the most recent report, not on a form. | 75 | 90 |
| `91.3 step` | From then on they see every report, and nothing about money. | 60 | 90 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `92.1 role` | Owner | 5 | 20 |
| `92.2 role` | Family manager | 14 | 20 |
| `92.3 role` | Family member | 13 | 20 |
| `92.4 role` | Guest | 5 | 20 |

**Owner** — can:
| Slot | String | ch | Budget |
|---|---|---|---|
| `93 own can 1` | See every report, every price and every invoice. | 48 | 56 |
| `93 own can 2` | Invite, remove and change what a relative can see. | 50 | 56 |
| `93 own can 3` | Order visits, cancel, and transfer the plot. | 44 | 56 |
| `93 own cannot 1` | Cannot be removed by anyone else in the circle. | 47 | 56 |
| `93 own cannot 2` | Cannot have two owners on one plot at once. | 43 | 56 |

**Family manager** — can:
| Slot | String | ch | Budget |
|---|---|---|---|
| `93 mgr can 1` | See every report and the care of the plot. | 42 | 56 |
| `93 mgr can 2` | Ask for a visit, which reaches you as a request. | 48 | 56 |
| `93 mgr can 3` | Talk to us directly about the work. | 35 | 56 |
| `93 mgr cannot 1` | Cannot spend anything without you. | 34 | 56 |
| `93 mgr cannot 2` | Cannot cancel, transfer or rename the plot. | 43 | 56 |

**Family member** — can:
| Slot | String | ch | Budget |
|---|---|---|---|
| `93 mem can 1` | See every report, from the first one. | 37 | 56 |
| `93 mem can 2` | Download and forward any report. | 32 | 56 |
| `93 mem can 3` | Tell us if something in a report looks wrong. | 45 | 56 |
| `93 mem cannot 1` | Never sees a price, an invoice or a renewal date. | 49 | 56 |
| `93 mem cannot 2` | Cannot order work or change anything. | 37 | 56 |

**Guest** — can:
| Slot | String | ch | Budget |
|---|---|---|---|
| `93 gst can 1` | Open one report from a link, with no account. | 45 | 56 |
| `93 gst can 2` | Forward that link to anyone else. | 33 | 56 |
| `93 gst can 3` | Tell us if something in it looks wrong. | 39 | 56 |
| `93 gst cannot 1` | Sees no price and is asked to sign up for nothing. | 50 | 56 |
| `93 gst cannot 2` | The link can be switched off at any time. | 41 | 56 |

**`94 the relative in Yerevan`** · 200 ch / budget 200

> Someone in Yerevan can meet the crew without joining the circle. We record them as a contact on the plot and write to them only about the day of a visit, once they have agreed. They never see a price.

**`95 privacy`** · 243 ch / budget 260

> The name on the monument is off by default: a report shows the cemetery, the sector and the plot. Turn it on and you can turn it off again, and it goes from links already sent. Removing someone takes effect at once. Past reports stay readable.

The last sentence of `95` is a commitment worth more than it costs us: access to
reports about a family member's grave is not a feature to be switched off when the money
stops. Nobody asks for it; everybody notices it.

---

## G. About — slots 96–98

| Slot | String | ch | Budget |
|---|---|---|---|
| `96 H1` | About MemoryCare — grave care in Yerevan | 40 | 60 |

**`96.1 opening`** · 347 ch / budget 400

> MemoryCare LLC is a Yerevan company that looks after family plots in the city's cemeteries and documents every visit. It was registered in 2026 and it is owned by Davit Hambardzumyan, who runs it with Hayk Manukyan. There are two of us on this page with our own mobile numbers on it, and a crew that does the work. That is the whole company today.

**`96.2 opening`** · 376 ch / budget 400

> We sell four things: a single inspection, a single full visit, four full visits a year and six. Every visit is a full visit — the whole plot and every monument, cleaned — and no visit closes until the GPS point, eight photographs and two videos exist. The price list is published, the formula for a larger plot is published, and one list applies in Yerevan and in Los Angeles.

**`97 why it exists`** · 294 ch / budget 300

> The care is not the scarce thing: plenty of people in Yerevan can clear a plot. What is scarce is knowing it was done, by whom and on what day, when you cannot go and look. So what we built is the record: a GPS point at the plot, the same four angles before and after, a report you can forward.

| Slot | String | ch | Budget |
|---|---|---|---|
| `98.1 method` | Every visit is a full visit: the whole plot and every monument, not a look around. | 82 | 120 |
| `98.2 method` | pH-neutral products only, chosen for granite, lalvar, basalt or tuff. Never chlorine, never acid. | 97 | 120 |
| `98.3 method` | A visit is not closed until the GPS point, eight photographs and two videos exist. | 82 | 120 |

The honesty panel (slot 36) repeats on this page verbatim, and it is the last thing on
it. About is the page a cautious buyer opens second, after the price, and the panel
answers the question they came with rather than making them look for it.

The bank requires this page. It is also, by some distance, the cheapest trust asset we
have: a registered company, two named people, two working numbers, one address.

---

## H. Contacts — slots 99–100

| Slot | String | ch | Budget |
|---|---|---|---|
| `contacts H1` | Contact MemoryCare in Yerevan | 29 | 60 |

**`99 hours`** · 196 ch / budget 120 ⚠

> Monday to Friday, 09:00–18:00 in Yerevan (UTC+4) — that is 08:00 in Paris, 02:00 in New York and 23:00 the night before in Los Angeles. Write at any hour; we call or write within one business day.

The budget is 120 characters and the string above is longer. My argument for spending
the extra: the conversion cost of a reader in Glendale doing timezone arithmetic at one
in the morning is higher than the layout cost of one more line, and this is the single
place on the site where that arithmetic is done for them. If the design lead holds the
budget, the shorter form is:

| Slot | String | ch | Budget |
|---|---|---|---|
| `99 hours (short)` | Monday to Friday, 09:00–18:00 in Yerevan (UTC+4). Write at any hour — we answer within one business day. | 104 | 120 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `100 map placeholder` | Map of the office — not yet published | 37 | 60 |
| `contacts email` | info@memorycare.am | 18 | — |
| `contacts davit` | Davit Hambardzumyan · +374 55 315 323 | 37 | — |
| `contacts hayk` | Hayk Manukyan · +374 93 154 108 | 31 | — |
| `contacts channels` | Both numbers take WhatsApp and Viber. | 37 | — |

Anything not yet real is visibly a placeholder and is never formatted to look real.
`+374 10-00-00-00` reads as a phone number; the live site prints one today.

---

## I. 404 and 500 — slots 119–120

| Slot | String | ch | Budget |
|---|---|---|---|
| `119 heading` | This page does not exist | 24 | 30 |
| `119 line` | The address may have changed, or it may be mistyped. These are the pages that exist: | 84 | 90 |
| `119.1 link` | Prices | 6 | 22 |
| `119.2 link` | How it works | 12 | 22 |
| `119.3 link` | Sample report | 13 | 22 |
| `119.4 link` | Family Circle | 13 | 22 |
| `119.5 link` | About | 5 | 22 |
| `119 phone` | Or call Hayk: +374 93 154 108 | 29 | 40 |
| `120 heading` | This is our fault | 17 | 30 |
| `120 line` | Something on our side is not working. Your data is safe. | 56 | 90 |

No `Oops`, no `Something went wrong`, no illustration of a lost astronaut. Four routes
on the live site answer with this panel under HTTP 200 today; the panel is fine, the
status code and the missing links are the failure.

---

## J. The consultation form and system microcopy — slots 101–113, 118, 123

### The form — slots 101–105

| Slot | String | ch | Budget |
|---|---|---|---|
| `101 heading` | Request a free consultation | 27 | 44 |
| `101 support` | Three fields, one business day, no payment and no account. | 58 | 90 |
| `102.1 label` | Your name | 9 | 24 |
| `102.2 label` | Phone or email | 14 | 24 |
| `102.3 label` | Cemetery or city | 16 | 24 |
| `102.4 label` | Anything we should know | 23 | 24 |
| `102.5 label` | A relative in Yerevan | 21 | 24 |
| `113 checkbox` | This number is on WhatsApp | 26 | 44 |
| `112 country search` | Search by country or dial code | 30 | 40 |
| `108 submit` | Request a consultation | 22 | 22 |
| `108 sending` | Sending… | 8 | 14 |

| Slot | String | ch | Budget |
|---|---|---|---|
| `103.1 helper` | Any country. Include the dial code — for example +374, +1 or +33. | 65 | 70 |
| `103.2 helper` | The district or the city is enough. “Not sure” is a real answer. | 64 | 70 |
| `103.3 helper` | Only if someone here would like to meet the crew. We ask them first. | 68 | 70 |

**`104 note prompt`** · 133 ch / budget 140

> For example: the best hours to call you, who else in the family we should speak to, or anything you know about the state of the plot.

**`105 consent`** · 74 ch / budget 110

> I agree that MemoryCare may contact me about this request. Privacy policy.

`103.2` is written to make *not knowing where the plot is* a normal answer rather than
a failed field. A person who has not been home in nine years genuinely does not know,
and a form that punishes that loses the lead we most want. It is also the truthful
answer: finding the plot is the first thing an Inspection does.

`105` is one line with one link, not a wall of consent text. The live form has no
consent control at all today, on a page that collects a name, a phone and an email.

### Validation — slots 106–107

Every message begins with *Please*, names the field in real-world words, and never says
invalid, required, failed or error. Validation runs on blur, and on keystroke only once
a field is already in error, so a person watching themselves fix it sees it clear.

| Slot | String | ch | Budget |
|---|---|---|---|
| `106.1` | Please enter your name. | 23 | 70 |
| `106.2` | Please give us one way to reach you. | 36 | 70 |
| `106.3` | This does not look like a phone number or an email address. | 59 | 70 |
| `106.4` | Please include the dial code, for example +374, +1 or +33. | 58 | 70 |
| `106.5` | Please check the number and try once more. | 42 | 70 |
| `106.6` | We will take the number as you typed it and check it with you. | 62 | 70 |
| `106.7` | Please tell us roughly where the plot is. | 41 | 70 |
| `106.8` | Please confirm we may contact you about this. | 45 | 70 |
| `106.9` | That note is longer than 500 characters. Please shorten it a little. | 68 | 70 |
| `107 summary` | Two things need a moment before we can send this | 48 | 60 |

`106.6` is the message that fires on the **second** failed attempt at a phone number,
and it is not an error: the field is accepted and the lead is flagged for a human. A
lost lead costs 160,000 ֏ AMD; a malformed number costs Hayk one minute. The message
says what will happen, in the neutral colour, and the form submits.

`107` counts what is left rather than announcing a failure. The count is rendered by the
component: `One thing needs…` / `Two things need…`.

### Success — slot 109

| Slot | String | ch | Budget |
|---|---|---|---|
| `109 heading` | Thank you. Your request has reached us. | 39 | 40 |
| `109 promise` | We call or write within one business day. | 41 | 48 |
| `109 hours` | Yerevan business hours, 09:00–18:00 (UTC+4) | 43 | 46 |
| `109 who` | Hayk writes on WhatsApp from +374 93 154 108 first, and calls only if you prefer. | 81 | 110 |
| `109 action 1` | See a full report | 17 | 24 |
| `109 action 2` | How it works | 12 | 24 |

Then, in order: an echo of what the reader told us — the contact detail, the cemetery,
and the calculator configuration if one was attached — so a typo is caught now rather
than after a missed call; and only then, low on the page, one optional question.

| Slot | String | ch | Budget |
|---|---|---|---|
| `109 echo` | You told us: {contact} · {place} | 32 | — |
| `109 echo calc` | You configured: 24 m², 3 monuments, four visits a year — 270,000 ֏ AMD a year. | 78 | — |
| `111 question` | How did you hear about us? | 26 | 40 |
| `111.1 option` | A search | 8 | 24 |
| `111.2 option` | Facebook or Instagram | 21 | 24 |
| `111.3 option` | YouTube or TikTok | 17 | 24 |
| `111.4 option` | Someone told me | 15 | 24 |
| `111.5 option` | A funeral home | 14 | 24 |
| `111.6 option` | Somewhere else | 14 | 24 |

Nothing on this screen asks for money, an account or a password.

### Failure — slot 110

**`110 server failure`** · 152 ch / budget 130 ⚠

> That did not reach us and nothing you typed has been lost. Please try again — or write to info@memorycare.am, or to Hayk on WhatsApp at +374 93 154 108.

| Slot | String | ch | Budget |
|---|---|---|---|
| `110 retry` | Try again | 9 | 20 |

This is the most important error on the site. A person who has decided to spend
160,000 ֏ AMD and hits a 500 must never be left with nothing to do, so the message
carries a human path out of it. The budget is 130 characters and the string above is 152:
the phone number and the email address are the whole point of it, and I would rather
the panel grew than that either was cut. The 130-character form, if the budget holds:

| Slot | String | ch | Budget |
|---|---|---|---|
| `110 server failure (short)` | That did not reach us and nothing you typed is lost. Try again, or write to info@memorycare.am. | 95 | 130 |


### Empty states — slot 118

Never the word *empty*, and every one names the next event rather than the absence.

| Slot | String | ch | Budget |
|---|---|---|---|
| `118.1 visits` | The first visit has not happened yet. When it does, the report is here. | 71 | 90 |
| `118.2 reports` | A report appears here within 48 hours of each visit. | 52 | 90 |
| `118.3 family` | Only you have access so far. Invite a relative and they see every report. | 73 | 90 |
| `118.4 payments` | Nothing has been charged yet. Payments appear here with their invoices. | 71 | 90 |
| `118.5 plots` | One plot is on this account. Call us to add another. | 52 | 90 |
| `118.6 filter` | Nothing matches that filter. Change it, or choose All. | 54 | 90 |

No empty state carries an illustration and the component has no slot for one.

### Transactional email subjects and preheaders — slot 123

Subjects state the fact. A report notification lands in a preview pane at somebody's
work, so the subject never carries a name from a monument, never a photograph and never
a price. `{date}` renders written out: `14 September 2026`.

| Slot | String | ch | Budget |
|---|---|---|---|
| `123.1 subject` | Your visit report is ready — {date} | 35 | 60 |
| `123.1 preheader` | Photographs, video and the GPS point from the visit on {date}. | 62 | 90 |
| `123.2 subject` | We have your request — MemoryCare | 33 | 60 |
| `123.2 preheader` | We call or write within one business day, Yerevan time. | 55 | 90 |
| `123.3 subject` | Set up your MemoryCare access | 29 | 60 |
| `123.3 preheader` | Your subscription is active. Choose how you sign in. | 52 | 90 |
| `123.4 subject` | {name} has invited you to a family circle | 41 | 60 |
| `123.4 preheader` | You will see every report for {plot}. There is nothing to pay. | 62 | 90 |
| `123.5 subject` | A visit to your plot tomorrow, {date} | 37 | 60 |
| `123.5 preheader` | Nothing is needed from you. The report follows within 48 hours. | 63 | 90 |
| `123.6 subject` | Your year ends on {date} | 24 | 60 |
| `123.6 preheader` | Four full visits, and what the next year would cover. | 53 | 90 |
| `123.7 subject` | Your invoice from MemoryCare — {amount} ֏ AMD | 45 | 60 |
| `123.7 preheader` | The transfer details are in the invoice attached. | 49 | 90 |

`123.1` is the subject line the reader will see more often than any other string we
write, and it is the one place where the product's whole argument fits in seven words:
something happened, on a named day, and there is evidence of it. It never says
*Great news* and it never says *has been completed*: **ready** is the state the reader
cares about, and the date is what they will search the mailbox for two years from now.

---

## K. Meta titles and descriptions — slots 13–15, English routes

Category first, brand last, on every route. The bare brand phrase is never optimised
for, never bought and never a page's subject: in English it belongs to the dementia-care
industry, and traffic arriving on that intent bounces. Every title carries the category
words and the city.

**`/en/` — home**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | Grave care in Yerevan — photo, video and GPS reports | 52 | 60 |
| `14 description` | Care for a family plot in Yerevan's cemeteries, documented: eight photographs, two videos and a GPS point recorded at the plot on every visit. | 142 | 155 |

**`/en/pricing/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | Grave care prices in Yerevan — MemoryCare | 41 | 60 |
| `14 description` | Four published prices in Armenian drams, from 20,000 ֏ for an inspection to 200,000 ֏ a year for six full visits, and the formula for a larger plot. | 148 | 155 |

**`/en/how-it-works/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | How grave care in Yerevan works — MemoryCare | 44 | 60 |
| `14 description` | What happens on a visit to a plot in Yerevan: the equipment, the pH-neutral chemistry, the eight photographs, the two videos and the GPS point. | 143 | 155 |

**`/en/sample-report/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | A visit report for a Yerevan grave — example | 44 | 60 |
| `14 description` | What arrives after every visit: the GPS point, four angles on arrival, the same four after the work, two videos and the crew's note. | 132 | 155 |

**`/en/family-circle/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | Family Circle — shared grave-care reports, Yerevan | 50 | 60 |
| `14 description` | Everyone you invite sees every report from the plot in Yerevan, with no subscription of their own. Prices and invoices stay visible only to you. | 144 | 155 |

**`/en/about/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | About MemoryCare — grave care in Yerevan | 40 | 60 |
| `14 description` | A Yerevan company caring for family plots since its registration in 2026. Two named founders, published prices, and a documented protocol for every visit. | 154 | 155 |

**`/en/contacts/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | Contact MemoryCare — grave care in Yerevan | 42 | 60 |
| `14 description` | Two mobile numbers that answer, on WhatsApp and Viber, and info@memorycare.am. Yerevan business hours, 09:00–18:00 (UTC+4). | 123 | 155 |

**`/en/consultation/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | Request a consultation — grave care in Yerevan | 46 | 60 |
| `14 description` | Three fields and one business day. Tell us where the plot is and how to reach you; nothing is paid and no account is created to have the conversation. | 150 | 155 |

**`/en/404/`**
| Slot | String | ch | Budget |
|---|---|---|---|
| `13 title` | Page not found — MemoryCare, Yerevan | 36 | 60 |
| `14 description` | This address does not exist. The prices, the sample report and the contacts for grave care in Yerevan are one link away. | 120 | 155 |

**Open Graph — slot 15, home**
| Slot | String | ch | Budget |
|---|---|---|---|
| `15 og:title` | Grave care in Yerevan, documented every visit | 45 | 60 |
| `15 og:description` | Eight photographs, two videos and a GPS point at the plot. The report reaches you within 48 hours. | 98 | 110 |

The four legal routes take the same pattern: `Privacy policy — MemoryCare, Yerevan`,
`Refund policy — …`, `Service delivery terms — …`, `Legal restrictions — …`. Their
descriptions are one plain sentence each and none of them is written to rank.

Two things that belong to the build rather than to me, but that the copy depends on:
the locale is `hy`, never `am` — `am` is Amharic, and the site currently tells every
crawler its Armenian pages are Ethiopian — and the structured data is `Organization` +
`LocalBusiness`, **never** `MedicalBusiness` or `MedicalOrganization`. The naming
collision, encoded.

---

## L. Product names in English — the argument

Four of the five product names have never been written in English. The prior art
(`design-package-v1/FINAL-CONTENT.md` §4.2) proposes the cognate set and prints the
Armenian in parentheses on first mention, which the one-script-per-locale rule now
forbids outright. So this is a decision, not an inheritance, and it needs the owner.

### The two candidate sets

| | A · cognates | B · descriptive *(recommended)* |
|---|---|---|
| 20,000 ֏ | Inspection | **Inspection** |
| 65,000 ֏ | Express | **Single visit** |
| 160,000 ֏ | Optimal | **Four visits a year** |
| 200,000 ֏ | Maximum | **Six visits a year** |
| calculated | Special | **By arrangement** |

### Why B

**1 · `Express` promises speed, and we are not selling speed.** In English a service
called Express is the fast one, and the fast one is the one where less is done. That
reading works directly against the sentence the whole line-up now rests on — every visit
is a full visit. The Armenian `Էքսպրես` does not carry that load; the English word does.
`Single visit` says exactly what is bought and takes 12 characters.

**2 · `Optimal` and `Maximum` are a quality ladder, and there is no quality ladder.**
They are comparatives. A reader meeting them cold understands *good* and *best*, and
infers that the cheaper one is the compromised one — which is precisely the inference
the 26.08 decision exists to kill. Under the corrected line-up the only difference
between them is a count, so naming them by the count makes the honest claim structural
instead of leaving it to a caption to correct an implication the name created. `basic`,
`premium` and `tier` are already banned for the same reason; `Optimal` and `Maximum` are
the same idea in Latin.

**3 · The count name is the pitch.** *Four visits a year, one in each season* is the
sentence the flagship sells on. When the name is `Four visits a year`, the name, the
year rail, the visit numeral and the arithmetic line all say the same thing four times
in one card. Redundancy is not a fault here: it is what checkable looks like.

**4 · `Special` is a promotional word in English.** *Today's specials*, *special
offer* — the register is a discount, on a page where the entire stop-list exists to keep
discount language out. It is also the least informative name on the page for the one
product a reader has to work to understand. `By arrangement` states the price mechanism,
which is the actual product: a number arrived at after somebody has seen the plot.

**5 · `Inspection` survives untouched**, in both sets. It is exact, it is in the right
register, and it says *survey, not cleaning* before the description has to.

### The cost of B, stated plainly

**The names diverge across locales.** A family talking to each other across the Armenian
and English sites will say `Օպտիմալ` and `four visits a year` about the same product.
That is a real support cost and it is the whole case for set A. Three things reduce it:
the price is unambiguous in every locale (160,000 ֏ AMD is the same string everywhere),
the visit count is in the name in English, and the invoice and the contract carry a
product code that is language-independent. If the owner would rather hold one set of
names across three locales, that is a legitimate call and set A ships — it is five
strings, and every other string in this file stands unchanged.

**What I would not accept in either set:** a mixed one. `Inspection · Express · Four
visits a year · Six visits a year` reads as two naming systems in one row and tells the
reader that somebody changed their mind halfway. Pick a set.

**Capitalisation.** Sentence case: `Four visits a year`, not `Four Visits A Year`. Title
case in English signals a proprietary product tier, which is the impression we are
trying to avoid, and it reads as American marketing to a European eye.

**[BLOCKED — owner decision. Set B is written throughout this file. Nothing else in it
depends on the choice.]**

---

## M. The comparison FAQ — my judgement

The condition attached to this item was mine to test: *if the copy lead cannot write it
without a sneer, we cut it*, and `FINAL-REBRAND` §4.6 adds a second — *it ships only if
we clear every item on it at the moment of writing.*

**It ships, at five items, with one of the six proposed items cut.** The cut is the
finding, so it goes first.

### The item I cut, and why

The strategist's proposed checklist ended on *What happens if the monument is damaged?*
It is a fair question and it is the one I would ask. **We do not clear it today.**
Guarantee 2 has no liability figure and no policy reference; `FINAL-REBRAND` §6.2 blocks
it on the lawyer. Publishing a checklist that includes a question we answer with *we are
working on it* is exactly the own goal the ruling warns about, and it is worse than not
publishing the checklist: it invites the reader to run the test on the one item we fail.
It goes back in the day the figure is bound, and it is the strongest item on the list.

### The five that stand, each with the answer we can show today

| The question | What we point at |
|---|---|
| What exactly is done on one visit, and on how much of the plot? | *What a full visit includes*, eight items, and the sentence that every visit is a full visit — the whole plot and every monument. |
| What arrives afterwards, and how soon? | The sample report, and the frozen 48-hour promise. |
| Can the rest of the family see it without paying? | Family Circle, included in every year, four roles published. |
| Is the full price list published, including the cases that cost more? | Four prices on the page and a calculator that shows its arithmetic. |
| Who is accountable, by name and phone? | Two founders, two mobile numbers, a registered company, one address. |

Ordering matters, and §4.6 is right about it: the first item is **what is done on one
visit**, not how many. Under the corrected line-up the visit count is a tie, and a
checklist that opened on the count would point the reader straight at it.

### On the sneer test

I could write it without one, and the draft that convinced me was the fourth. The first
three failed, all in the same way: every item was phrased as a thing to *watch out for*,
which is an accusation with the defendant left blank. *Does anyone actually go?* is not
a checklist item, it is an insinuation. The version that works asks each question
neutrally, in the reader's own words, about a service they have not chosen yet — and
crucially it opens with **“Five questions worth asking anyone, including us.”** Those
three words are what make it an act of good faith rather than a trap: we are inside the
set being tested, not standing outside it holding the marking scheme.

No competitor is named, alluded to, or described. Nothing in the item is reverse-
engineered from anyone's weakness; each question is one I would ask about a service I
was buying for my own family, and each one is answered on this site by a link rather
than by a claim.

**One condition I attach for the build:** this item must be re-tested against the site
every time the site changes. It is the only string on the page whose truth depends on
five other pages continuing to exist. If Family Circle slips, item 3 fails, and the FAQ
becomes a list of promises rather than a list of links. Put it in the release checklist.

---

## N. Blocked — the nine strings I will not invent

| # | String | Why it is blocked | Who unblocks it |
|---|---|---|---|
| 1 | `9` company registration number | No source in the repo or the archive carries it. It is a **bank condition** and it is printed on every page. | Davit / the lawyer |
| 1b | `9`, `10`, `96.1` the entity's registered spelling | Three sources, two answers: `Memory Care LLC` and `MemoryCare LLC`. Nobody has opened the certificate, and the site must match the registry exactly. | Davit, with the certificate |
| 2 | `9` legal address | The archive records `0051, Komitas Street 47/1, building 9` as *requiring the lawyer's confirmation*. An unconfirmed address printed as fact on eighteen pages is the wrong kind of error. | The lawyer |
| 3 | `71` flowers / candle price | No source gives it a number. The owner requires the option to be visible on the tariffs page. | Davit |
| 4 | `74.2` damage guarantee | Needs an amount and a policy reference. Liability and worker insurance are recorded as open. Until then the guarantee is absent, not softened. | The lawyer |
| 5 | `46` product names in English | A decision, not a translation. Set B is written; see §L. | Davit |
| 6 | Portal tense | Nobody has ruled what the site may claim about a portal that is not live on launch day. Everything here is written to survive either ruling. | Hayk + Igor |
| 7 | Report photographs | The September shoot has not happened. The sample-report page says so in its own header line rather than using a stock photograph. | The shoot |
| 8 | Any guarantee not yet legally bound | `74.1` and `74.3` are ours to keep and are written. Anything else waits. | The lawyer |

None of these is filled with a placeholder that looks like a fact. `+374 10-00-00-00` on
the live site is what that looks like when it goes wrong: it reads as a phone number.

---

## O. Where I deviate, and where I disagree

### 1 · Two strings that cannot fit their own budgets — a defect in §10, not a preference

**Slot 45, the one-off chip, is budgeted at 26 characters hard.** The canonical term for
it in `FINAL-CONTENT` §4.5 is `One-off · not a subscription` — **28 characters**. The
canonical string does not fit its own slot, in the shortest of the three languages.
I have written `NOT A SUBSCRIPTION` (18), because the unit chip beside it already says
`ONE-OFF` and the repetition was the part paying for the overflow. Either the budget
moves to 30 or the canonical term changes; both documents currently say both things.

**Slot 99 (hours) and slot 110 (server failure)** are the two strings I have knowingly
written over budget, and both are argued where they appear. Slot 99 converts Yerevan
time into three cities the audience actually lives in; slot 110 carries a phone number
and an email address for a person who has just lost a 160,000 ֏ AMD decision to a 500.
Both are cases where the sentence is worth more than the line. Shorter forms are
supplied for both if the design lead holds the budget.

### 2 · The two frozen promises exist in two different wordings

`PROPOSAL-ux.md` §10 freezes `We call or write within one business day.` and `Your
report arrives within 48 hours of the visit.` `FINAL-CONTENT` §4.4 freezes `We reply
within one business day, Yerevan time (UTC+4).` and `The report is in your portal within
48 hours of the visit.` **Two documents each declare a different string frozen**, which
is the precise failure the freeze exists to prevent.

I have used the UX strings, because `FINAL-REBRAND` §3 gives UX the string slots. Two
further reasons to make that the permanent ruling: the UX report promise says *arrives*
rather than *is in your portal*, so it stays true whichever way blocked item 6 is ruled;
and splitting the hours into their own string (slot 17) lets the promise and the timezone
sit on two lines, which is how a person actually reads them. `FINAL-CONTENT` §4.4 should
be corrected rather than left to be found by whoever writes the emails.

### 3 · Prior art that is now forbidden, and should be marked so

`FINAL-CONTENT` §4.2 instructs: *English name first, Armenian in parentheses on first
mention on a page.* One script per locale forbids exactly that, and the file is otherwise
the most useful piece of prior art in the repo — which is what makes the instruction
dangerous. It will be followed by whoever reads that file next unless it is struck.

### 4 · One home-page FAQ swap

`PROPOSAL-ux.md` §2.2 asks the home FAQ to carry *whether prices differ for clients
abroad*. Slot 76 requires the same question on the pricing page. Rather than print one
question and answer twice, the home page carries the one-price-list line (slot 42) in the
tariffs section, where a reader forms the suspicion, and the full question and answer
live in the pricing FAQ. The home FAQ slot it frees goes to *what happens after I request
a consultation* — the question a reader has with their hand on the button, and the one
place where the callback promise can be read as an answer rather than as a claim.

### 5 · Strings §10 does not have a slot for, and that the site needs

| Slot | String | ch | Budget |
|---|---|---|---|
| `+1 FX note` | Prices are in Armenian drams. Any figure in another currency is approximate. | 76 | 120 |
| `+2 home tariff H2` | What it costs | 13 | 44 |
| `+3 home tariff link` | All prices and what is in them | 30 | 40 |
| `+4 Family Circle line` | Care is rarely one person's decision, and it should not be one person's inbox. | 78 | 90 |
| `+5 founders note` | Both numbers take WhatsApp and Viber. | 37 | 60 |

`+1` is a bank condition — the fifth of the eight — and `FINAL-REBRAND` §4.1 records it
as half-covered with no owner. It belongs wherever a price appears in a second currency,
and once in the pricing page's footer. It is one sentence and nobody had written it.

### 6 · One note for whoever writes the banned-string test

The stop-list is enforced as a build-time string check, and two shipped strings will
trip a naive substring version of it. Slot 43 — `Every visit is the same full visit. The
only difference is how many.` — contains `the only`, and it is the sentence the design
lead ruled in. Slot 76.4 contains a denial of instalment payment that must not be
rewritten into the word the ban is aimed at. The check should test **phrases**
(`the only service`, `the only company`, `the first in`) rather than fragments, or it
will be switched off within a week — which is worse than not having it.

### 7 · The desktop-only ruling

`FINAL-REBRAND` §2b narrows the deliverable to desktop. No copy in this file changes
because of it, and I have kept every §10 character budget even where it was justified by
a 360-wide layout — a budget is a discipline about how much a sentence may cost, not a
measurement of a phone.

One consequence for the record, since it is a copy consequence rather than a layout one:
this audience reads at 23:40 in Glendale, on a phone, and the strings most likely to be
read there are the two founders' numbers and the WhatsApp affordance. Whatever happens
to the layout, those three must remain one tap from anywhere. That is not an argument
against the ruling — it is the owner's call and it is recorded as one — it is the part
of it that the copy cannot compensate for on its own.

### 8 · What I did not write

Slots `114–117`, `121` and `122` — the portal first-run screen, the invite flow, the
invitation-received page, the guest report, the three bad-news states and the cancellation
flow — are product surfaces rather than pages on the marketing site, and they are outside
the pages I was given. They are also the strings most likely to be written badly by
whoever ends up with them, because two of them (`121` and `122`) are where a company's
register is actually tested: a moved visit and a cancellation. `FINAL-CONTENT` §10.5 and
§9.9 have good drafts of both, written against the old prices — the arithmetic in the
cancellation flow needs redoing at 160,000 and 200,000, and the words do not.

---

## P. The five sentences this file would be judged on

If everything above were cut to five strings, these are the five, and each one is
checkable by a stranger against something on the same page:

1. **Grave care in Yerevan. Every visit documented.** — the category, the city, and the
   one claim the page settles on the same screen.
2. **Every visit is the same full visit. The only difference is how many.** — the whole
   comparison, made honest by the decision of 26.08.
3. **We started in 2026. We have no reviews to show you and we will not borrow anyone
   else's.** — the only asset on this site an incumbent cannot copy.
4. **Starting small costs you nothing.** — a heading that is the consequence of a sum,
   printed above the sum.
5. **Care is rarely one person's decision, and it should not be one person's inbox.** —
   the differentiator, described as a family rather than as a feature.

Not one of them contains an adjective about us.
