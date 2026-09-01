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
  I have left standing, and the two places where the budget itself is wrong are in §M.
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
- Product names in English are a **proposal**, argued in §K. Everything downstream of
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

**`9 legal entity`** — footer legal-entity block, budget 160 ch · 269 ch

> MemoryCare LLC · Company registration number [BLOCKED — no registration number in any source; Davit or the lawyer supplies it] · Komitas Street 47/1, building 9, 0051 Yerevan, Armenia [address unconfirmed — the archive records it as requiring the lawyer's confirmation]

The publishable form, once both facts are confirmed, fits the budget:

| Slot | String | ch | Budget |
|---|---|---|---|
| `9 legal entity (target form)` | MemoryCare LLC · Registration number {REG_NUMBER} · Komitas Street 47/1, building 9, 0051 Yerevan, Armenia | 106 | 160 |

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
ruling. Every other portal reference in this file is written the same way. See §L.

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
took to get there, are in §L. Short version: it ships, at five items, one fewer than
proposed, and the cut item is the reason.

### 11 · The consultation form — slot 40

| Slot | String | ch | Budget |
|---|---|---|---|
| `40 heading` | Request a free consultation | 27 | 44 |
| `40 support` | Three fields, one business day, no payment and no account. | 58 | 90 |

Full form copy — labels, helpers, validation, success, failure — is §I.

### 12 · Footer

Slots 6–12 above. The footer is a bank condition before it is a design element: real
contacts on every page, the legal entity, the registration number, the address. It is
also where the language switcher lives at every width, alongside the header.

---

