# Make the site satisfy Ameriabank's internet-acquiring terms

For the UI/UX and content designer. This document is the difference
between a site that looks finished and a site the bank will actually
approve for card acceptance.

**Source:** *Ինտերնետ էքվայրինգ ծառայության պայմաններ և սակագներ*,
Ameriabank CJSC. Adopted 05.09.2018 by board decision 03/24/18; **this
edition by decision 06/71/26 of 18.05.2026, in force from 26.05.2026.**
Chapter 4 — *Requirements set for the internet site and mobile
application* — is the operative part, and §4.10 is the list your work is
measured against.

Everything below is read from that document, not from a summary. Earlier
project notes worked from a transcription of a screenshot and were
incomplete: they carried eight conditions. **§4.10 alone has twelve**,
§4.9 adds three more, and five operational clauses elsewhere create
interface obligations nobody had recorded.

---

## 0. Why this is urgent, in one paragraph

Card acceptance is blocked until the bank approves the site. The bank
cannot begin reviewing pages that do not exist, so every week a required
page is missing is added to the review rather than spent in parallel with
it. Card revenue is expected in October. **§5.2 also gives the bank a
standing right to monitor the site's compliance for the whole life of the
relationship** — so this is not a one-time gate you pass and forget.

---

## 1. §4.10 — the twelve items that must be on the site

Each row is a deliverable. Where copy already exists in the project, it is
named. Where it does not, that is your work.

| § | Requirement | What it means here | Status |
|---|---|---|---|
| **4.10.1** | An **"About us"** section with a general description of the merchant and its field of activity | A real About page: Memory Care LLC, Yerevan, registered 2026, what it does | **Copy written** — `COPY-legal-and-about.md` §2 |
| **4.10.2** | **Contact details** — address, phone number(s), e-mail | Real address, real dialable numbers, `info@memorycare.am`. The live site prints `0000, Yerevan` and `+374 10-00-00-00` | **Blocked** — see §4 |
| **4.10.3** | A **full description of the goods or services**, matching the real characteristics of what is advertised | All five products, with exact visit counts and what each visit contains. "Corresponding to real data" is the operative phrase — the description must match what is actually performed | **Copy written** — §3 |
| **4.10.4** | **Legal restrictions**, if any | Construction work on a plot requires municipal permission; cemetery access rules; what we do not and cannot do | **Copy written** — §4, but the "minor repair" boundary is still undefined by the lawyer |
| **4.10.5** | **Real prices and currency — quoting in AMD is mandatory** | Every price in ֏ AMD. Any $ or € figure is secondary, marked approximate, and never the only figure shown | Prices decided; **the FX note appears nowhere on the site** |
| **4.10.6** | **Delivery terms**, including restrictions on delivery outside Armenia | See §2.1 — this needs thought, because the buyer is abroad and the service is performed in Yerevan | **Not written** |
| **4.10.7** | **Return and refund terms** | The pro-rata rule, with worked arithmetic | **Copy written** — §6 |
| **4.10.8** | The **customer-data privacy policy**, and where applicable the site's privacy policy **and the site's cookie policy** | Two documents, not one. The cookie policy is named separately in the clause | Privacy **written**; **cookie policy not written** |
| **4.10.9** | **The site's security capabilities and the rules for using card data** | A section nobody has written. See §2.2 | **Not written** |
| **4.10.10** | **The terms of any special offers that carry restrictions** | Our credit rules are exactly this: the inspection credited only on signing an annual subscription, within 60 days, never into a single visit; one credit only, never both | **Not published as an offer** — see §2.3 |
| **4.10.11** | **Which payment systems' cards are accepted — at minimum the colour trade marks of those systems must be present** | Visa / Mastercard / ArCa marks, **in colour**, in their official form | **Not present** |
| **4.10.12** | If a **free or preferential trial** exists: its terms, dates, the date of the first recurring charge, a statement that failure to cancel results in a charge, the cancellation steps, and the refund procedure | We have no free trial. **State that explicitly in the compliance table** rather than leaving the row blank — and see §2.3, because a credit is not a trial and must not read like one | **N/A — declare it** |

---

## 2. The four that need real design thinking

### 2.1 Delivery terms for a service performed in Armenia and bought from abroad (§4.10.6)

The clause is written for goods. Ours is a service, and the geometry is
unusual: **the payer is typically outside Armenia and the service is
performed inside it.** The site must say, plainly:

- **What is delivered, and where.** The care itself happens at the plot,
  at a named cemetery in Yerevan. That is the delivery location, and it
  does not change with the buyer's country.
- **What the customer receives, and how.** The visit report — eight
  photographs, two videos, one GPS point — delivered digitally, reachable
  from anywhere.
- **When.** Report within 48 hours of the visit. And the one number
  nobody has decided: **how many days after payment the first visit
  happens.** See §4.
- **Geographic restrictions.** We serve Yerevan cemeteries. Name the
  boundary rather than implying we go anywhere.

Write it as delivery terms, not as marketing. The bank is reading it to
check that a cardholder knows what they will get and when.

### 2.2 Security capabilities and card-data rules (§4.10.9)

A short, honest page. What it must cover:

- **The connection is encrypted.** §4.8 obliges us to apply modern
  encryption standards and to hold a certificate proving it.
- **We do not store card numbers.** Payment is handled by the bank's
  payment page; card details are entered there, not with us. Say who
  processes the payment.
- **What we do store** — name, phone, e-mail, the plot, the reports.
- **§3.13 is a promise you can publish:** we may not ask for the
  cardholder's bank account number, and may not use it for anything other
  than accepting payment. Saying so plainly is worth more than a security
  badge.
- **§3.14:** card payment is never accepted against a previously incurred
  debt.

Do not illustrate this with padlock icons and the word "bank-grade".
Write what is true.

### 2.3 The credit rules are a special offer with restrictions (§4.10.10)

Nobody has treated them as one, and the clause is explicit: **if a special
offer carries restrictions, those restrictions must be published.**

The restrictions, exactly:

- The inspection (20,000 ֏) is credited **only on signing an annual
  subscription**, and **only within 60 days**. It is never credited into a
  single visit.
- A single visit (65,000 ֏) is credited in full into an annual
  subscription within 60 days.
- **One credit only.** Either the inspection or the single visit, never
  both. A client who bought both receives the larger.

These go on the tariffs page as terms, in the same visual weight as the
offer itself — not in a footnote, and not only in the legal pages.

**And a warning about the framing.** A credit is not a trial. §4.10.12 and
§3.8 govern free and preferential trial periods, which carry heavy
obligations — including an e-mail to the cardholder **no later than seven
days** before any charge. Do not let the copy drift into language that
makes the credit read like a trial with an automatic charge at the end,
because that changes which rules apply.

### 2.4 The payment-system marks (§4.10.11)

Mandatory, and specifically **in colour**. This lands on your palette
discipline, and the rule that no colour appears outside the brand set does
**not** override a bank requirement.

Handle it properly rather than fighting it:

- Use the official marks in their official colours, at their specified
  minimum sizes, per each scheme's own brand rules.
- Give them their own zone — the footer, and the payment step — on a
  neutral ground where they read as third-party marks rather than as part
  of our palette.
- Do not recolour, outline, flatten to monochrome, or restyle them. That
  breaks both the bank's requirement and the schemes' own rules.
- The current site's `#FF0000` Pay button is a different matter: that is
  our colour, it is off-palette, its label measures 4.00 against a 4.5
  requirement, and it goes.

---

## 3. §4.9 — legal compliance, and the clause that makes fabricated content a legal problem

| § | Requirement | Consequence |
|---|---|---|
| 4.9.1 | The information required by RA law must be present, including any licence that must be displayed | Confirm with the lawyer whether this activity requires a displayed licence |
| **4.9.2** | **All information on the site, including advertising, must comply with RA legislation** | **This is the clause that makes the invented content a legal exposure rather than a matter of taste.** The site currently claims 150,000 customers, 55+ services, 250,000+ graves and 15 years of experience. The company was registered in 2026 and has zero paying customers. It also shows six testimonials named `Անուն Ազգանուն` — "Name Surname" — with photographs of people. Under 4.9.2 this is false advertising on a page submitted to a bank for approval |
| 4.9.3 | Technical and software solutions for the legal requirements of the field, including **age restrictions** | Decide whether any age gate applies and record the answer either way |

**§4.11 — every link on the site must be real, contain real data, and must
not redirect to sites that violate the terms.** The site currently has
**nineteen routes that return HTTP 200 while rendering a 404**, and a
sidebar item shown to paying customers — "My payments" — that leads to a
404. Both are direct breaches of 4.11 and both are yours to fix.

---

## 4. Operational clauses that create interface work

These are not in chapter 4 and nobody had recorded them.

| § | Rule | What it means for the interface |
|---|---|---|
| **3.5** | Where foreign currency is possible, the site must have a **technical solution ensuring that transactions performed inside Armenia are made only in AMD** | A currency rule, not a label. If you display anything but AMD, there must be logic behind it |
| **3.6** | The service may be operated in Armenian; other languages where technically possible. The merchant must comply with RA language legislation | Armenian is not one of three equal options — it is the baseline. Design so it is never the degraded one |
| **3.10** | **No surcharge and no different conditions for card payment** than for any other payment method | The card price equals the bank-transfer price. No "card fee", no discount for paying another way |
| **3.12** | No charge may be made unless the transaction is confirmed, **or** the service has been delivered, **or** the cardholder has consented to recurring charges | An annual subscription paid up front is prepayment and is allowed. **If anything recurs, explicit cardholder consent is a designed interface element**, not a checkbox buried in terms |
| **3.8** | If a preferential or free period is used, the cardholder must be e-mailed **no later than seven days** before the charge, with the cancellation steps | Only if we introduce one. If we ever do, that e-mail is a designed template with a deadline attached |

---

## 5. The report is also chargeback evidence — design it that way

This is the most useful thing in the document and it is not in chapter 4.

**§3.7** sets out what a transaction's supporting document must contain
for delivered goods: a description, the delivery address, the date and
time, the recipient's name, a signature, and the last four digits of the
card. **§5.3** lets the bank freeze a disputed amount for up to six
months. **§3.9** requires transaction records to be kept for three years.

Our visit report already carries most of that — the cemetery and plot, the
date, the crew, a GPS point taken on site, photographs and video. **Add
the customer's name and the last four digits of the card**, and the report
stops being only a product feature and becomes the document that defends a
disputed transaction.

Design it so a report can be exported as that document. It costs almost
nothing now and is very expensive to retrofit after the first chargeback.

---

## 6. What the pages are, and where each requirement lands

| Page | Carries |
|---|---|
| **About** | 4.10.1, and the entity's legal identity |
| **Tariffs** | 4.10.3, 4.10.5, 4.10.10, 3.10 |
| **Service delivery terms** | 4.10.6, and the first-visit interval |
| **Refund and cancellation** | 4.10.7, with worked arithmetic |
| **Privacy policy** | 4.10.8, first part |
| **Cookie policy** | 4.10.8, second part — **a separate document** |
| **Security and card data** | 4.10.9, 3.13, 3.14 |
| **Legal restrictions** | 4.10.4, 4.9.1, 4.9.3 |
| **Every footer** | 4.10.2 — address, phones, e-mail, legal entity, registration number — and the 4.10.11 payment marks |
| **The payment step** | 4.10.11 again, 3.12 consent if anything recurs |
| **Every page** | 4.11 — no dead links, no soft 404s |

An English privacy policy is required by the project's own record of the
bank's expectations; the terms themselves require the site to comply with
RA language law (§3.6). **Produce all of these in all three locales** and
let the lawyer rule on which language governs.

---

## 7. Blocked — a designer cannot close these

Do not invent any of them, and do not write around them.

1. **The exact registered spelling of the legal entity.** Three project
   sources give two answers — `Memory Care LLC` and `MemoryCare LLC`.
   Whatever the site prints must match the certificate exactly; a mismatch
   between the site and the registry is a common reason a submission comes
   back. **Nobody has opened the certificate.** → the owner.
2. **The registration number.** It appears in no project document, and
   4.10.2 puts it in every footer. → the owner.
3. **The confirmed legal address.** Recorded as `0051, Komitas 47/1,
   bldg 9, Yerevan` but flagged as needing the lawyer's confirmation.
4. **How many days after payment the first visit happens.** Required by
   4.10.6, decided nowhere, and contractual the moment it is published.
   → the owner.
5. **The boundary of "minor repair"** (4.10.4). Tasked to the lawyer on
   22.08 and never delivered. Until it exists in writing, the site may not
   name a single repair it will perform.
6. **Where customer data and the photographs are stored** — provider and
   country. Recorded nowhere, and 4.10.8 cannot be written without it. The
   developer contract is unsigned and there is no data-processing
   agreement. → the owner and the lawyer.
7. **Whether any licence must be displayed** (4.9.1) and whether any age
   restriction applies (4.9.3). → the lawyer.
8. **The domain-ownership document** (4.7) and the **encryption
   certificate** (4.8). Not design work, but the bank will ask.
9. **§4.2 — the payment part of the site must be built and operated in a
   manner agreed with the bank.** Somebody must have that conversation
   before the payment screens are finalised.

---

## 8. Deliver

1. Every page in §6, in all three locales, as real copy — not outlines.
2. **A compliance table**: every clause cited in this document, the page
   and section that satisfies it, and the exact string. A bank reviewer
   should be able to follow it in one pass. Include the rows that are
   **N/A**, marked as such — 4.10.12 among them.
3. A **link audit** proving §4.11: every link, its target, its HTTP
   status, and confirmation that no route returns 200 while rendering a
   404.
4. The **footer block** as a single component, identical on every page and
   in every locale, carrying 4.10.2 and the payment marks.
5. **`BLOCKED.md`** — the §7 items, each with the named person who closes
   it, and what cannot ship until they do.

## 9. How this will be judged

1. **Is every one of the twelve §4.10 items present?** A missing one is a
   returned submission.
2. **Is every price in AMD**, with any other currency clearly secondary
   and marked approximate?
3. **Are the payment-system marks present, in colour, unmodified?**
4. **Is the cookie policy a separate document** from the privacy policy?
5. **Does any claim on the site fail §4.9.2** — is anything advertised
   that is not true today?
6. **Does every link resolve, and does every not-found route return 404?**
7. **Is the footer identical on every page and in every locale?**
8. **Are the §7 blockers still marked blocked**, rather than quietly
   filled with something plausible?
