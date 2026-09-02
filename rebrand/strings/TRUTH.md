# TRUTH — every factual claim these strings make, its source, and whether a stranger can check it today

**Content lead, 02.09.2026.** One row per claim, not per string. The verdict
column is also the **tense instruction**: a rule that is true is written in the
present, an artefact that does not exist yet is not described as one, and
anything with no source is not written at all.

**Verdicts:**
**OK** — a visitor or a bank reviewer could verify it now ·
**RULE** — true as a standing operating rule, no artefact to point at yet;
written as a rule ("a visit is not closed until…"), never as an invitation to
come and look ·
**BLOCKED** — no source; the string is a visible gap and the person who closes
it is named ·
**VERIFY** — a value exists in project documents but nobody has confirmed it
against the primary record; one person, one answer.

Company position, stated once because half the register depends on it:
**MemoryCare LLC was registered in 2026 and has zero paying customers.** The
September pilot is the first client work. Nothing in these files says otherwise
and nothing in them borrows evidence from anyone else.

---

## 1. Company, entity, contact

| # | Claim | Keys | Source | Verdict |
|---|---|---|---|---|
| 1 | The company is a registered Armenian legal entity | `about.p1`, `common.entity.registeredYear` | `PROJECT-MEMORY-FULL` §9 | **OK** |
| 2 | It was registered in 2026 | `home.honesty`, `about.p1`, `meta.about.description` | every source; audit | **OK** — and it is the honesty panel, the strongest paragraph on the site |
| 3 | **The registered legal name** | `common.entity.legalName`, `common.entity.registeredName`, `about.entity.tradingAs`, `footer.legal.entity`, `footer.copyright` | **Supplied after my first pass** — the state-register form is now printed verbatim as `«ՄԵՄՈՐԻՔԵՅՐ» ՍՊԸ` | **VERIFY → Davit.** The blocker in my first pass is closed in the files, and the solution adopted is the right one: the readable rendering carries the locale (`MemoryCare LLC` · `ООО «МемориКейр»`) and the **registry form is quoted verbatim beside it**, so the site matches the certificate exactly without printing Armenian at a reader who cannot read it. **I did not open the certificate myself** — somebody who has must confirm all four strings against it before submission. This is the one exception to one-script-per-locale in the EN and RU files, and it is whitelisted by key: a registered legal name quoted verbatim is a proper noun, in the same class as `֏` |
| 4 | **State registration number** — `999.110.1600788` | `footer.legal.entity` | **supplied after my first pass**; no longer a gap | **VERIFY → Davit.** Was BLOCKED. Must match the certificate digit for digit; a mismatch here is the commonest reason a bank submission is returned |
| 5 | **Taxpayer number (ՀՎՀՀ)** — `08330546` | `footer.legal.entity` | same | **VERIFY → Davit** |
| 6 | **Legal address** — 47 Komitas Ave., apt 9, 0051 Yerevan | `footer.legal.entity` | same; note it is `47`, not the `47/1 building 9` the archive recorded | **VERIFY → the lawyer.** The form now printed differs from `PROJECT-MEMORY-FULL` §1, which is the one that was flagged as unconfirmed — so the new form is probably the corrected one, but the change must be confirmed rather than assumed |
| 7 | Davit Hambardzumyan, CEO, +374 55 315 323 | `common.founder.davit.*` | `PROJECT-MEMORY-FULL` §1; `CLAUDE.md` | **OK** — dial it |
| 8 | Hayk Manukyan, CBDO, +374 93 154 108 | `common.founder.hayk.*` | same | **OK** |
| 9 | info@memorycare.am, active since 11.08.2026 | `common.email` | same | **OK.** `memorycarearmenia@gmail.com` appears nowhere and must not |
| 10 | Both numbers take WhatsApp and Viber | `common.channels`, `form.whatsapp` | `FINAL-CONTENT` §4.1; corporate line with WhatsApp Business since ~12–17.08 | **OK** |
| 11 | **Business hours 09:00–18:00 (UTC+4), Mon–Fri** | `common.hours`, `frozen.hours`, `contacts.hours`, `legal.terms.sequence.2` | three project documents carry it; `FINAL-CONTENT` §13.2 item 2 records it as **not confirmed by the CEO** | **VERIFY → Davit.** Not invented — it stands in three sources — but it sits inside a frozen promise used in six places, so it must be confirmed rather than assumed. One word closes it; if he changes it, `frozen.hours` and `common.hours` change together |
| 12 | The corporate landline | — | number never recorded | **BLOCKED → Hayk.** Not printed. If it exists it belongs above the two mobiles in the footer |

---

## 2. Products, prices, credit

| # | Claim | Keys | Source | Verdict |
|---|---|---|---|---|
| 13 | Inspection 20,000 ֏ · single visit 65,000 ֏ · four visits 160,000 ֏/yr · six visits 200,000 ֏/yr · fifth by calculator | `prices.card.*.price`, `footer.svc.*`, `home.prices.line.*` | `TARIFF-REDESIGN-2026-08-26` §1, §5 — owner, 26.08 | **OK** |
| 14 | Four visits, one in each season; six visits across the year | `prices.card.optimal.pitch`, `prices.card.maximum.pitch` | same §1.3–1.4 | **OK** |
| 15 | Every visit is a full visit; there is no smaller kind | `prices.sameness`, `home.prices.sameness`, `about.p2` | owner rejection of the light/heavy split, 26.08 | **OK** — and the words for the split appear in no string in any locale, checked |
| 16 | Price is flat within 16 m² and two monuments | `prices.coverage`, `prices.calc.caption.*` | `TARIFF-REDESIGN` §1 | **OK.** Note that `rebrand/BRIEF.md`'s inherited sentence "flat price at any plot size" is **false** and is not written anywhere |
| 17 | +10,000 ֏/yr per m² over 16; +30,000 ֏/yr per monument over two; one-off surcharge is a quarter of the annual | `prices.calc.rate1`, `prices.calc.rate2`, `prices.faq.a3` | `TARIFF-REDESIGN` §2 | **OK** |
| 18 | 160,000 ÷ 16 = 10,000 ֏ per m² per year — an added metre costs what an included one costs | `prices.calc.rate1` | arithmetic | **OK** — self-verifying, and the strongest sentence on the pricing page |
| 19 | Sliders cap at 100 m² and 10 monuments; beyond that, after an inspection | `prices.calc.ceiling` | `TARIFF-REDESIGN` §2 | **OK** |
| 20 | The inspection is credited only on signing an annual subscription, within 60 days, never into a single visit | `prices.credit.rule1`, `.rule3`, `.rule4`, `prices.faq.a4`, `legal.terms.credit.p1` | §1.1, §14 | **OK** — and this is bank condition 4.10.10, a special offer with restrictions, so it is published as terms at the same weight as the offer |
| 21 | A single visit is credited in full into an annual subscription within 60 days | same keys | §1.2 | **OK** |
| 22 | One credit only; the larger of the two; one per plot | `prices.credit.rule1`, `.rule2` | §1.2, §14 | **OK** |
| 23 | **Every route into year one costs 160,000 ֏** | `prices.credit.headline`, `.subline`, `.worked1`–`.worked3` | derived from 13, 20–22 | **OK** — arithmetic, printed above the sum. Never styled as a discount: no `save`, no `only`, no struck-through figure, no badge on the 95,000 |
| 24 | A credited single visit counts as the first visit of the subscription year | `prices.faq.a2`, `legal.terms.year.p1` | §14 | **OK** |
| 25 | No discounted repeat single visit — 65,000 ֏ every time | `prices.credit.rule5`, `prices.faq.a2` | §1.2, §4 | **OK** — and the live site still sells 40,000 ֏, which the audit calls a blocker. That figure appears in these files only as the per-visit arithmetic of the annual product |
| 26 | Paid once, for the year; no instalments, no monthly, no seasonal | `prices.paymentTerm`, `prices.faq.a5`, `legal.terms.what.p1` | §4, owner rejection | **OK** |
| 27 | A Special visit is never priced below a Maximum visit | `prices.special.floor` | §1.5 | **OK as a principle.** The figure ~33,333 is an internal floor and is **not printed**; the check bans it |
| 28 | Special always begins with an inspection | `prices.special.entryRule` | §1.1, §1.5 | **OK** |
| 29 | Prices are the same for clients in Yerevan and abroad | `prices.onePriceList`, `prices.faq.a1` | §1 "единые для местных и диаспоры" | **OK** |
| 30 | **Flowers or a candle as a visible add-on** | `prices.ritual.*` | owner instruction 26.08 §7.5 requires the option on this page; **no source gives either a price** | **BLOCKED → Davit.** The row cannot ship without the number: an add-on with no price, on a page whose whole argument is published prices, would undo the page. "On request" here is exactly the opacity the page is built against |

---

## 3. The visit, the protocol, the report

| # | Claim | Keys | Source | Verdict |
|---|---|---|---|---|
| 31 | A visit is not closed until 8 photographs (four angles before, the same four after), 2 videos of 20–40 s and 1 GPS point exist | `home.protocol.*`, `home.method.record.line`, `legal.terms.after.p1`, `about.method3` | `PROJECT-MEMORY-FULL` §8, §11 | **RULE.** True as an operating rule; there is no real report to point at until the September pilot. Written as a rule everywhere, never as "go and look" |
| 32 | The GPS point is recorded on site, at the plot, on the day — it verifies the crew was there, not where the grave is | `home.report.ann.gps`, `report.ann.2`, `home.trust.1.line` | §11 | **RULE.** The verification framing is load-bearing: an unqualified GPS claim is the competitor's claim, and the word `location` never appears near it |
| 33 | Deep cleaning uses steam, wet/dry vacuum, soft brushes and pH-neutral products chosen for the stone | `home.method.equipment.line`, `home.method.chemistry.line`, `how.includes.*` | `TARIFF-REDESIGN` §1.2; `PROJECT-MEMORY-FULL` §11 | **RULE** — demonstrable after the pilot. **The word `Kärcher` appears in no string**, per `CLAUDE.md`; the method is described by what it is |
| 34 | High pressure is used on paths and railings, never on a monument | `home.method.equipment.line`, `how.includes.7`, `legal.limitations.ask.5` | owner clarification 13.08; §11 protocol limits (500 psi granite, 100 psi tuf) | **OK** — a published limit, checkable against the contract |
| 35 | No chlorine and no acid on any of the four stones | `home.method.chemistry.line`, `how.notdo.1`, `legal.limitations.ask.4`, `legal.limitations.stone` | §11 | **OK** |
| 36 | No washing at or below +4…+10 °C or with frost expected within 48 hours | `home.faq.a2`, `how.weather`, `legal.terms.winter.p1` | `TARIFF-REDESIGN` §1.3 | **OK** — a published protocol limit |
| 37 | **The winter visit runs on the days the weather allows; if none comes it is added to spring; four visits either way, as a contract term** | `prices.year.footnote`, `home.faq.a2`, `how.weather`, `legal.terms.winter.p1` | §1.3; `rebrand/BRIEF.md` | **OK provided it is in the contract.** The strings say "a term of the contract" in three places. **The lawyer must confirm the clause is in the client contract before these ship.** If it is not yet a term, the four strings become RULE and the words "term of the contract" come out. → the lawyer, via Hayk |
| 38 | Your plot is looked after by the same assigned crew | `home.method.crew.line`, `how.crew`, `legal.terms.crew.p1`, `prices.card.*.f4` | `TARIFF-REDESIGN` §3.4 | **RULE**, and worded as **assignment** in all three locales, never as a promise of an unchanging roster. 26.08 §3.4 records the unchanged-roster wording as a legal trap as the company grows |
| 39 | Damage is photographed, the coordinator called, and the client within 24 hours | `legal.terms.complaints.p1` | §11 | **RULE** |
| 40 | Construction work requires municipal permission and is outside what we do | `home.notdo.1`, `legal.limitations.construction.*` | §1.1, lawyer 22.08 | **OK**, and it is bank condition 4.10.4 |
| 41 | **The boundary of "minor repair"** | `legal.limitations.construction.blocked` | tasked to the lawyer 22.08, **never delivered** | **BLOCKED → the lawyer.** Until it exists in writing the site names **no repair it will perform**; the inspection quote is described as a separate offer, which is the only formulation true today |
| 42 | There is no cemetery-operator counterparty in Armenia; the client's permission is the legal basis | `legal.limitations.access.p1` | `PROJECT-MEMORY-FULL` §9 | **RULE until the lawyer issues the opinion in writing**, which §9 records as still owed. `legal.limitations.access.blocked` says so on the page. The two mass cases — unregistered inheritance and Soviet-era plots with no title — are named in the lawyer's brief and are not answered here |
| 43 | Yerevan's cemeteries are not usefully mapped | `how.step2.body` | research pass 19.08; `PROJECT-MEMORY-FULL` | **RULE**, and written as the reason the inspection exists — **never as a criticism of anyone** |
| 44 | The first visit of a subscription is a full visit, not a survey | `how.firstVisit` | §1.1 by implication; the light/heavy rejection | **OK** |

---

## 4. Portal, Family Circle, delivery

| # | Claim | Keys | Source | Verdict |
|---|---|---|---|---|
| 45 | **The report arrives within 48 hours of the visit** | `frozen.report` and every reference to it | `FINAL-UX`; `FINAL-CONTENT` §4.4 | **RULE.** A commitment, not yet demonstrated. The string names **no channel**, deliberately, so it stays true whichever way the platform lands |
| 46 | **We call or write within one business day** | `frozen.callback` | same | **RULE**, same treatment. Never softened to "usually", never sharpened to a shorter number |
| 47 | A report can be sent as a plain link, forwardable, needing no account | `report.linkPreview`, `how.step4.body`, `home.how.step3.line`, `family.guest.can1` | `TARIFF-REDESIGN` §3.3 — owner | **RULE**, and deliverable with an email and a URL on day one. This is the mechanism the present tense rests on |
| 48 | The chat preview carries the mark, "Visit report" and the date — no photograph, no name | `report.linkPreview` | `FINAL-CONTENT` decision; owner privacy decision | **RULE** — a product decision, not yet built |
| 49 | **A client portal exists and reports appear in it** | — | platform target readiness ~20.09.2026, **development contract unsigned** (`PROJECT-MEMORY-FULL` §9) | **Not written as a present-tense screen anywhere.** The portal appears only as *what a subscription includes* and in account-side strings. Three strings that had slipped into "the report appears in your personal account" were rewritten — see RECONCILIATION §7.4 |
| 50 | Family Circle is included in every annual subscription | `home.family.*`, `family.*`, `prices.card.optimal.f3` | `PROJECT-MEMORY-FULL` §8; `CLAUDE.md` | **RULE** as *what a subscription includes* — true, it is a term of the sale. Not shown as a live screen and not illustrated with one |
| 51 | Four roles: Owner, Family manager, Family member, Guest, with those permissions | `family.role.*`, `family.*.can*`, `family.*.cannot*` | `FINAL-CONTENT` §5.9; `PROPOSAL-ux` §7 | **RULE** — the model is decided; the screens are not built |
| 52 | The name on the monument is off by default, and switching it off removes it from links already sent | `legal.privacy.name.p1`, `family.privacy` | `FINAL-CONTENT` decision 5 | **RULE** — a product setting that does not exist yet. Written as a rule, and it is a commitment we will have to honour in code |
| 53 | An invitation is valid for 14 days; removal takes effect at once | `family.privacy` | Russian deck, from the platform spec | **RULE** |
| 54 | A day-before notification, opt-in, routable to someone else | `report.delivery.opt2`, `.opt3`, `legal.terms.after.p2` | `TARIFF-REDESIGN` §3.2 | **RULE**, and described as **opt-in**, never as a default |
| 55 | A relative in Yerevan can meet the crew without joining the circle and never sees a price | `family.yerevanRelative`, `home.faq.a5` | `TARIFF-REDESIGN` §3.2; Russian deck | **RULE** |
| 56 | Reports stay available after a subscription ends | `legal.privacy.retention.reports`, `legal.refund.cancel.p2` | `DECISIONS-2`; `FINAL-SYSTEM` | **RULE**, and it collides with the right to deletion (row 68). The privacy policy must say which wins, in advance |

---

## 5. Payment, guarantees, refunds

| # | Claim | Keys | Source | Verdict |
|---|---|---|---|---|
| 57 | Today payment is by bank transfer; card payment opens when the bank enables it; **no date is promised** | `prices.paymentReality`, `prices.faq.a6`, `legal.terms.payment.p1`, `footer.payment.note` | Ameriabank enablement expected early October, `LAWYER-DISCUSSION` §7 computes mid-October from the dependency chain | **OK as written.** No month appears in any string. A date on a public page that the bank then misses is the worst available first broken promise |
| 58 | No surcharge and no different condition for paying by card | `prices.noSurcharge`, `legal.terms.payment.p1` | Ameriabank terms §3.10 | **OK** |
| 59 | Transactions inside Armenia are in AMD only | `legal.terms.payment.p2`, `legal.compliance.currency` | §3.5 | **OK** |
| 60 | We never see or store card numbers; the card is entered on the bank's page | `legal.privacy.collect.cards`, `legal.security.p2` | §4.10.9, §2.2 of the bank brief | **OK** — true of the architecture as specified |
| 61 | We will never ask for your bank account number and may not use it for anything but accepting payment | `legal.security.p3` | §3.13 | **OK** — this is a promise the bank's own terms let us publish, and it is worth more than a padlock icon |
| 62 | Card payment is never accepted against a previously incurred debt | `legal.security.p4` | §3.14 | **OK** |
| 63 | **There is no free or preferential trial** | `legal.compliance.noTrial`, `legal.terms.credit.p2` | §4.10.12 requires the row to be declared, not left blank | **OK.** Declared explicitly, and the credit is stated as a credit and not a trial, because a trial changes which rules apply — including a mandatory email seven days before any charge |
| 64 | Free repeat visit within 7 days, counted **from delivery of the report** | `prices.guarantee.1.remedy`, `legal.terms.guarantees.p1`, `legal.refund.unhappy.p1` | `TARIFF-REDESIGN` §3.1, §7.1 | **RULE — and the contract must be redrafted to match.** §7.1 records that the contract currently counts from the visit date. If the site publishes the client-favourable version and the contract carries the other, the first complaint is a dispute about our own copy. → the lawyer |
| 65 | **We answer for damage we cause** | `prices.guarantee.2.remedy` | `TARIFF-REDESIGN` §3.1, §7.2 records a 500,000 ֏ reserve; `PROJECT-MEMORY-FULL` §9 shows liability and worker insurance **open** | **BLOCKED → the lawyer + Davit.** Guarantee 2 is absent from the site rather than softened. The word "insured" alone is explicitly rejected. This is also the single dependency holding the comparison FAQ (RECONCILIATION §4) |
| 66 | Pro-rata refund on cancellation, on the amount actually paid, rounded up to the nearest 100 ֏, no cap | `legal.refund.*` | `TARIFF-REDESIGN` §3.1; `PROPOSAL-ux` §3.9 | **OK** — the arithmetic is published with three worked examples, which is bank condition 4.10.7 |
| 67 | **Refund turnaround in business days** | `legal.refund.how.blocked` | depends on Ameriabank acquiring terms, not yet in force | **BLOCKED → Davit, from Ameriabank.** The bank reviewer will look for a timeframe here |
| 68 | **The rule for cancelling a one-off before it is carried out** | `legal.refund.oneoff.blocked` | **no owner rule exists** | **BLOCKED → Davit.** The bank will ask, because a one-off single visit is the product a first card payment is most likely to buy. A defensible rule to put to him: full refund before the crew is dispatched; no refund once the visit is performed and the report delivered, with the 7-day repeat applying instead |
| 69 | **How many days after payment the first visit happens** | `legal.terms.sequence.6` | **decided nowhere.** It is the literal subject of bank condition 4.10.6/8, and it is constrained by crew capacity (~60 new clients per crew per month) | **BLOCKED → Davit + Hayk.** It becomes contractual the moment it is published, so it comes from the owner, not from a writer |

---

## 6. Privacy, data, cookies

| # | Claim | Keys | Source | Verdict |
|---|---|---|---|---|
| 70 | What the consultation form collects | `legal.privacy.collect.consultation` | the form itself, as specified | **OK** |
| 71 | What we hold about a client | `legal.privacy.collect.client` | platform spec | **RULE** — accurate to what the system is specified to hold |
| 72 | We do not sell data, do not share it with advertisers, do not use plot photographs in marketing without separate written consent | `legal.privacy.notdo.p1`, `legal.limitations.photo.p1` | owner and lawyer decisions | **OK** as a commitment |
| 73 | **Where the data physically lives — provider and country** | `legal.privacy.who2.blocked` | recorded nowhere; the developer contract is unsigned and contains no data-processing agreement | **BLOCKED → Igor via Hayk, and the lawyer.** A privacy policy that cannot name where the photographs are stored is not finished. The processor is described by function, never by name, because naming a processor we have no agreement with is a finding waiting to happen |
| 74 | **Legal basis for any transfer outside Armenia** | same key | the CRM is a US processor and part of the audience is in the EU | **BLOCKED → the lawyer** |
| 75 | **Retention periods** — for requests that never became clients, and for accounting records | `legal.privacy.retention.blocked` | decided by nobody | **BLOCKED → Davit + the accountant** |
| 76 | **The window in which we answer a data request** | `legal.privacy.rights.window` | not committed to | **BLOCKED → Davit / Hayk.** Do not print a number until somebody commits to one |
| 77 | **"Reports stay available" versus the right to deletion** | `legal.privacy.retention.reports` + `legal.privacy.rights.3` | two promises that collide the first time somebody exercises the second | **BLOCKED → the lawyer.** The policy must say which wins, in advance, not in the reply email |
| 78 | **This site sets no advertising and no analytics cookies; language choice and the sign-in session are the only stored items** | `legal.cookies.p2`, `.p3` | **true of the site this team is building** — static HTML, no framework, no third-party script, no embedded map, per `rebrand/BRIEF.md` build conventions | **OK for this build, and it is a commitment the build must keep.** It is why there is **no cookie banner** and no consent mechanism: nothing non-essential is set, so there is nothing to consent to. **If anyone adds measurement, an embedded map or a marketing tag, this page becomes false and a banner becomes necessary.** The consultation form forwards what you typed plus the source page to us; that is a data transfer covered by the privacy policy and the consent line, not a cookie, and `legal.cookies.p4` says so |
| 79 | **The photography-consent form** | `legal.limitations.photo.blocked` | being drafted by the lawyer, three opt-ins in three languages | **BLOCKED → the lawyer.** No client photograph is used anywhere until it exists |
| 80 | **Which language version governs** the legal pages | `legal.governingLanguage` | `LAWYER-DISCUSSION` §7.1 raises it, unanswered | **BLOCKED → the lawyer.** Three operative texts and no rule for divergence is not a formality for a diaspora client reading the English |
| 81 | **Whether any licence must be displayed, and whether an age restriction applies** | `legal.compliance.ageNote` | §4.9.1, §4.9.3 | **BLOCKED → the lawyer** |

---

## 7. Positioning — the claims most likely to be written wrong

| # | Claim | Keys | Verdict |
|---|---|---|---|
| 82 | We combine photo + video + GPS + a portal + a family circle | `home.trust.*`, `home.family.*` | **Written as what we do, never as what others do not.** No string says `the only`, `the first`, `nobody else`, `unique` or `since 20xx`, in any language, and the check enforces it. The 19.08 research pass records an established Yerevan competitor since ~2015 with photo reports; **"nobody in Yerevan does grave care with photo reports" is false and appears nowhere** |
| 83 | No competitor is named or alluded to | — | **OK** — checked across all three files including placeholders, and the comparison block (held) is written so that every question is one a buyer asks unprompted, with `including us` in its own heading |
| 84 | 160,000 ֏ ÷ 4 = 40,000 ֏ a visit | `prices.card.optimal.arithmetic` | **OK** — arithmetic, and it must be published: the premium needs an argument, and the two feature lines above it say what a visit is |
| 85 | We have no reviews and will not borrow anyone else's | `home.honesty` | **OK** — the only asset on this site an incumbent structurally cannot copy. Set at body size inside a border; set small and grey it becomes a disclaimer and does the opposite of its job |
| 86 | "Memory care" in English means dementia care; that is not what we do | `legal.limitations.notus.p2` | **OK** — and it is why every English title is category-first |
| 87 | The report photographs are placeholders until the September shoot | `report.headerLine` | **OK** — said on the page rather than hidden. There is no stock photograph of a stranger's grave anywhere in this string set, and none may be added |

---

## 8. What is blocked, in one list, by owner

**Davit** — business hours confirmation · the flowers and candle price · the
one-off cancellation rule · the days between payment and the first visit (with
Hayk) · the data-request response window. **Closed since the first pass:** the
registration number, the ՀՎՀՀ, the legal address and the registered name are now
in the files and need confirming against the certificate rather than supplying.

**The lawyer** — the confirmed legal address · the boundary of "minor repair" ·
the liability figure and policy for guarantee 2 · the cemetery-access opinion ·
the photography-consent form · the legal basis for transfers outside Armenia ·
retention periods · reports-forever versus deletion · which language governs ·
licence and age restriction · **confirmation that the four-visits-regardless
winter clause is in the client contract** (row 37).

**Hayk** — the corporate landline number, if it exists · routing the lawyer's
items · reading the bank's own document rather than the transcription of a
screenshot of it, before submission.

**Igor, via Hayk** — hosting provider and the country the data sits in.

**Ameriabank, via Davit** — the refund turnaround in business days.

Thirteen still open, four now supplied and awaiting confirmation. Most of the
open ones are one answer from one person who already knows the answer. None of them is a writing task, and every one of them, left open,
becomes a defect found in October by someone who was not on this team.

---

## 8a. The account area — 134 keys added 02.09

The account area is the portal. It is not live, nobody has ruled what the site
may claim about it, and these strings are written so that **no sentence in it
becomes false if the platform slips.**

| # | Claim | Keys | Verdict |
|---|---|---|---|
| 88 | A report arrives within 48 hours of each visit, as a link you can open and forward | `empty.reports` (**revised**) | **RULE.** The old value said a report "appears here", which promises this screen. It now names the mechanism that is real on day one — the link — and works as the empty state whether or not the list behind it is live. This was the single place where a first pilot customer would have met a broken promise in the first sentence |
| 89 | You can add a plot yourself, and you can instead tell us on the phone | `empty.plots` (**revised**), `account.plots.callInstead`, `account.plots.add.cta` | **OK.** See RECONCILIATION §13 for the ruling. Both routes are real: the owner authorised self-service and the engineer built it, and the phone has always worked |
| 90 | A plot is one grave, and every visit, report and invoice belongs to one | `account.plots.standfirst`, `account.plots.empty.text`, `account.dashboard.standfirst` | **OK** — a definition of our own data model, checkable against the site |
| 91 | Nothing on the order page is charged, and the amount is set by us, not by the page | `account.order.standfirst`, `account.order.serverPrice` | **OK**, and it is the copy half of the fix for the audit finding that the price travelled in a hidden field. The string says the page cannot change the amount **and neither can anything sent from it** — if the server does not in fact re-derive the price, this string is false and the server is wrong, not the string. → Igor must confirm the server re-derives |
| 92 | An order cannot be placed without saying which grave it is for | `account.order.noplot` | **OK** — the copy half of the fix for the audit's worst finding, that a customer could subscribe to a year of grave care without naming a grave |
| 93 | The current password is required to change a password | `account.profile.password.why` | **OK** — the copy half of the account-takeover fix. The string says why, which is what stops the field being removed again as friction |
| 94 | The password-reset answer is the same whether or not the address is known | `account.reset.note` | **OK** — and it must stay true in the implementation, or the string is a lie that teaches an attacker to ignore it |
| 95 | Cancellation arithmetic, worked, from the amount actually paid | `account.cancel.*` plus the ratified `legal.refund.*` | **OK.** The dialog reuses the ratified refund strings unchanged: 160,000 × 2 ÷ 4 = 80,000, computed on what left the customer's account and never on the list price, rounded up to the nearest 100 ֏ in their favour, no cap. `account.cancel.example` introduces it and adds nothing to it. Nothing here is softened into reassurance and no consoling sentence sits between the sum and the confirm button |
| 96 | Registering costs nothing and orders nothing | `account.register.standfirst` | **OK** |
| 97 | Nothing here is checked against a registry; the first visit records the rest | `account.plotnew.standfirst`, `account.plotnew.help.location` | **OK** — true, and it is what makes *I do not know where it is* a normal answer rather than a failed field |

**Not blocked, but owed by somebody:**
`account.order.serverPrice` and `account.reset.note` are the two strings in this
set whose truth depends on server behaviour rather than on copy. Both are worth
keeping and both should be on the release checklist with a name against them.

---

## 9. Two claims in the brief I could not support

1. **`rebrand/BRIEF.md`, Products table, Express row: "steam, professional
   neutral-pH chemistry, wet/dry vacuum" is right, but the same brief's
   composition text elsewhere in the project names `Kärcher`.** `CLAUDE.md` says
   the word must never be written, because it names both our chemistry and a
   pressure washer, and high-pressure washing is forbidden on monuments. Two
   documents in the required-reading set disagree. I ruled for `CLAUDE.md` and
   the word appears in no string. If operations think the shipped wording is
   inaccurate, `home.method.equipment.line` and `how.includes.7` should be
   rewritten **with them**, not in copy.

2. **`rebrand/BRIEF.md` inherits "Flat price at any plot size for the standard
   products" from the older pricing section.** It is contradicted by the same
   brief's own surcharge paragraph and by `TARIFF-REDESIGN` §2. A writer reading
   it in good faith would publish a false claim. The correct sentence — flat
   within 16 m² and two monuments, one published formula beyond — is at
   `prices.coverage`, and the false one appears nowhere. That line should be
   struck from the brief before the next round reads it.

Two smaller ones, for completeness: the brief's contrast figure for Sky blue on
Dark Olive (10.26) differs from `CLAUDE.md`'s (13.18) — not a content matter,
but somebody should reconcile it before the design system is built; and the
brief's structural claim that Family Circle has no world analogue is written in
these strings only as what we do, never as a comparison, for the reason in
row 82.
