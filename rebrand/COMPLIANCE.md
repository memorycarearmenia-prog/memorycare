# COMPLIANCE — Ameriabank internet-acquiring terms, clause by clause

**Source:** *Ինտերնետ էքվայրինգ ծառայության պայմաններ և սակագներ*, Ameriabank
CJSC, edition adopted by board decision 06/71/26 of 18.05.2026, **in force from
26.05.2026**. Clause numbering is the bank's; the mapping is
`docs/PROMPT-BANK-COMPLIANCE-UIUX.md`.

**How to read this.** One row per clause. *Where* is the route and the section
inside it. *String key* is the exact key in `rebrand/strings/{en,ru,am}.json` —
the same key in all three locales, and it is written into an HTML comment beside
its own text on the page, so a reviewer can find any sentence from either end.
Rows marked **N/A** are declared, not omitted. Rows marked **BLOCKED** render on
the page as a visible bracketed gap naming the person who closes it; none of
them has been filled with a plausible value.

Every route below exists in three locales: `/en/…`, `/ru/…`, `/am/…`
(`lang="hy"` — the folder name `am` is a lead instruction, the language code is
not).

---

## 1. §4.10 — the twelve items

| § | Requirement | Where | String key | Status |
|---|---|---|---|---|
| **4.10.1** | "About us" — description of the merchant and its field of activity | `/{loc}/about.html`, opening section; extended at `/{loc}/history.html` | `about.h1`, `about.p1`, `about.why`, `about.p2`, `about.method1`–`.method3`, `common.entity.registeredYear` | **Present** |
| **4.10.2** | Contact details — address, phone(s), e-mail | **Footer, every page, every locale.** Legal strip and Contact column | `footer.legal.entity`, `common.entity.registeredName`, `common.entity.addressLabel`, `common.entity.address`, `common.founder.davit.name/.roleShort/.phone/.tel`, `common.founder.hayk.*`, `common.email`, `common.channels`, `common.hours` | **Present.** Entity, registration number 999.110.1600788, taxpayer number 08330546 and the registered legal address are in one line of every footer |
| **4.10.3** | Full description of the services, matching real characteristics | `/{loc}/legal/terms.html` §"What you are buying" + the five products; `/{loc}/values.html` (what a visit contains); `/{loc}/prices.html` (not this engineer's route) | `legal.terms.what.p1`, `prices.sameness`, `footer.svc.inspection/.single/.four/.six/.special`, `prices.coverage`, `prices.special.definition`, `prices.special.entryRule`, `how.includes.1`–`.8`, `how.firstVisit`, `how.crew` | **Present** |
| **4.10.4** | Legal restrictions, if any | `/{loc}/legal/restrictions.html`, all six sections | `legal.limitations.h1`, `.standfirst`, `.notus.p1/.p2`, `.construction.p1/.p2/.p3`, `.ask.1`–`.6`, `.stone`, `.access.p1/.p2`, `.photo.p1`, `.liability.h2` | **Present**, with three blocked gaps below |
| **4.10.5** | Real prices, quoting in AMD mandatory | Footer Services column on every page; `/{loc}/legal/terms.html`; `/{loc}/legal/refunds.html`; `/{loc}/prices.html` | `footer.svc.*`, `common.currencyLine`, `common.fx.long`, `legal.compliance.currency`, `legal.refund.example1`–`3.paid/.calc` | **Present.** Every figure on these routes is ֏ AMD. No other currency is printed anywhere; `common.fx.long` is the standing note that any converted figure is approximate and that the charge is in drams |
| **4.10.6** | Delivery terms, including restrictions on delivery outside Armenia | `/{loc}/legal/terms.html` §"Where the service is performed" and §"From your request to your first visit" and §"What arrives after every visit" | `legal.terms.where.p1`, `.where.p2`, `prices.onePriceList`, `legal.terms.sequence.1`–`.7`, `legal.terms.after.p1`, `.after.p2`, `frozen.report` (via `legal.terms.sequence.7`) | **Present except one number** — see BLOCKED #4 |
| **4.10.7** | Return and refund terms | `/{loc}/legal/refunds.html`, whole page | `legal.refund.h1`, `.standfirst`, `.rule.p1/.formula/.rounding`, `.visits.p1`, `.base.p1`, `.example1`–`3.*`, `.cancel.p1/.p2`, `.unhappy.p1`, `.how.p1` | **Present.** Formula plus three worked examples with real arithmetic |
| **4.10.8a** | Customer-data privacy policy | `/{loc}/legal/privacy.html`, whole page | `legal.privacy.h1`, `.summary`, `.who.p1`, `.collect.consultation/.client/.cards`, `.who2.staff/.dev/.crm/.bank/.family`, `.retention.reports`, `.name.p1/.p2`, `.notdo.p1`, `.rights.intro/.1`–`.6/.accounting`, `.changes.p1` | **Present**, with three blocked gaps below |
| **4.10.8b** | The site's **cookie policy** — named separately in the clause | `/{loc}/legal/cookies.html` — **a separate document at its own URL**, cross-linked both ways with the privacy policy | `legal.cookies.h1`, `.p1`–`.p6` | **Present.** `legal.cookies.p1` states on the page why it is a separate document. No consent banner, because `legal.cookies.p2` commits that nothing non-essential is set — that commitment binds the build |
| **4.10.9** | Site security capabilities and rules for using card data | `/{loc}/legal/security.html`, whole page | `legal.security.h1`, `.p1`–`.p5`, `legal.privacy.collect.cards`, `legal.terms.payment.p2`, `legal.compliance.currency`, `legal.compliance.noTrial` | **Present** |
| **4.10.10** | Terms of special offers that carry restrictions | `/{loc}/legal/terms.html` §"The credit, and the conditions on it" — full weight, not a footnote. Repeated at the same weight on `/{loc}/prices.html` (other engineer) | `legal.terms.credit.p1`, `prices.credit.rule1`–`.rule5`, `legal.terms.credit.p2` | **Present.** The credit is stated as a credit and explicitly not a trial, so §4.10.12 / §3.8 do not attach |
| **4.10.11** | Which card schemes are accepted — **colour trade marks at minimum** | **Footer, every page**, its own zone (`.mc-paymarks`), on the neutral Ivory object ground, marks rendered as `<img>` in their own colours at each scheme's own minimum size | `footer.payment.heading`, `footer.payment.note`, `prices.noSurcharge` | **BLOCKED — which schemes.** The strip is built and schemes are data (`PAYMENT_SCHEMES` in the generator). It renders a visible bracketed gap until the set is confirmed. **The one permitted palette exception; no hex enters CSS or HTML for it** |
| **4.10.12** | Free or preferential trial: terms, dates, first charge date, non-cancellation warning, cancellation steps, refund procedure | Declared explicitly on `/{loc}/legal/terms.html` §credit and §payment, and on `/{loc}/legal/security.html` | `legal.compliance.noTrial`, `legal.terms.credit.p2` | **N/A — declared.** There is no free or preferential trial. Nothing renews by itself and nothing is charged automatically. Declared in prose rather than left blank, per the clause's own logic |

## 2. §4.9 — legal compliance

| § | Requirement | Where | String key | Status |
|---|---|---|---|---|
| 4.9.1 | Information required by RA law, including any licence that must be displayed | `/{loc}/legal/restrictions.html` §"Limits on what we can promise"; entity identity in every footer and on `/{loc}/about.html` §"Legal identity" | `legal.compliance.ageNote`, `about.entity.tradingAs`, `common.entity.legalName/.regNumber/.taxNumber/.address/.registeredName/.country`, `about.entity.bank`, `legal.entityLine` | **BLOCKED — whether a licence must be displayed.** → the lawyer |
| **4.9.2** | All information, **including advertising**, complies with RA law | Whole site. On these ten routes: no statistic, testimonial, customer count, review count or years-in-business claim appears at all. The honesty panel says so in the company's own words | `home.honesty` (on `/about.html` and `/history.html`) | **Present.** The four invented figures, the six `Անուն Ազգանուն` testimonials and the empty partners strip are not rendered on any route in this set. `.mc-testimonial` / `.mc-partners` remain in `components.css` behind a flag nothing sets |
| 4.9.3 | Technical/software solutions for the field's legal requirements, incl. age restrictions | `/{loc}/legal/restrictions.html` §"Limits on what we can promise" | `legal.compliance.ageNote` | **BLOCKED — whether an age restriction applies.** → the lawyer. Recorded either way, per the clause |
| **4.11** | Every link real, with real data; no redirect to non-compliant sites; no soft 404 | All thirty routes in this set. Link audit in §5 below | — | **Present for this set.** Three of these routes (`history`, `mission`, `values`) are exactly the soft-404s: they now carry real content instead of a 404 template under HTTP 200 |

## 3. Operational clauses that create interface obligations

| § | Rule | Where | String key | Status |
|---|---|---|---|---|
| **3.5** | Transactions inside Armenia in AMD only, enforced technically | `/{loc}/legal/terms.html` §Payment; `/{loc}/legal/security.html`; footer legal strip on every page | `legal.terms.payment.p2`, `legal.compliance.currency`, `common.currencyLine`, `common.fx.long` | **Present as published rule.** No non-AMD figure is rendered anywhere on this site, so there is no conversion path to enforce. If a currency toggle is ever added, this row stops being satisfied by copy alone |
| **3.6** | Armenian is the baseline language; RA language law | Every page in this set exists in `hy`. The language switcher lists **ՀԱՅ first**, in native script, in all three locales | `header.lang.hy`, `header.lang.en`, `header.lang.ru`, `header.lang.label` | **Present.** ⚠️ URL segment is `/am/` per the lead's folder instruction; `lang` and `hreflang` are `hy`. See §6 |
| **3.8** | Preferential/free period ⇒ e-mail 7 days before charge | — | `legal.compliance.noTrial` | **N/A.** No such period exists. If one is introduced, that e-mail becomes a designed template with a deadline |
| **3.10** | No surcharge and no different conditions for card payment | Footer payment zone on **every page**; `/{loc}/legal/terms.html` §Payment | `prices.noSurcharge`, `legal.terms.payment.p1` | **Present.** Nothing anywhere advertises a card fee or an alternative-payment discount |
| **3.12** | No charge without confirmation, delivery, or consent to recurring | `/{loc}/legal/terms.html` §"The subscription year" and §credit | `prices.paymentTerm`, `legal.terms.year.p1`, `legal.terms.credit.p2`, `legal.compliance.noTrial` | **Present.** An annual subscription is prepayment, paid once; nothing recurs, so no recurring-consent interface element is required. If auto-renewal is ever added, §3.12 requires a designed consent control |
| **3.13** | Merchant may not request the cardholder's bank account number, nor use it for anything but accepting payment | `/{loc}/legal/security.html` | `legal.security.p3` | **Present, published as a promise** |
| **3.14** | Card payment never accepted against a previously incurred debt | `/{loc}/legal/security.html` | `legal.security.p4` | **Present** |
| 3.7 / 3.9 / 5.3 | Supporting document for a disputed transaction; three-year record retention; six-month freeze | Not a page in this set — a report-export requirement. See §7 | `legal.terms.after.p1` describes what the report contains today | **Gap — nobody's plan.** See §7 |
| 4.2 / 4.7 / 4.8 | Payment part agreed with the bank; domain-ownership document; encryption certificate | `legal.security.p1` publishes the encryption claim | `legal.security.p1` | **Partly.** 4.7 and 4.2 are not design work; see §7 |
| 5.2 | The bank may monitor compliance for the life of the relationship | — | — | **Standing.** This table is the artefact that answers a re-check; keep it current |

---

## 4. BLOCKED — what renders as a visible gap, and who closes it

Each renders as bracketed text on the live page, marked in the DOM with
`data-blocked="…"` so a build check can find every one. None is filled with a
plausible value.

| # | What is missing | Renders on | String key | `data-blocked` | Who closes it |
|---|---|---|---|---|---|
| 1 | Which card schemes are accepted, and therefore which colour marks §4.10.11 requires | Footer, every page | *(no key — build marker)* | `schemes` | **Davit**, from the acquiring contract |
| 2 | The written boundary of "minor repair" | `legal/restrictions.html` | `legal.limitations.construction.blocked` | `minor-repair-boundary` | **the lawyer** (tasked 22.08, undelivered) |
| 3 | The lawyer's written opinion on cemetery access | `legal/restrictions.html` | `legal.limitations.access.blocked` | `cemetery-access-opinion` | **the lawyer** |
| 4 | Days between payment and the first visit — **required by §4.10.6** | `legal/terms.html`, step 6 of the sequence | `legal.terms.sequence.6` | `sequence` | **Davit + Hayk** |
| 5 | Liability for damage — figure and the policy that binds it | `legal/restrictions.html` | `legal.limitations.liability.blocked` | `liability-figure` | **the lawyer + Davit** |
| 6 | The photography-consent form | `legal/restrictions.html` | `legal.limitations.photo.blocked` | `photo-consent-form` | **the lawyer** |
| 7 | Whether a licence must be displayed / whether an age restriction applies | `legal/restrictions.html` | `legal.compliance.ageNote` | `age-restriction-and-licence` | **the lawyer** |
| 8 | Hosting provider, the country the data sits in, and the legal basis for transfer outside Armenia — **§4.10.8 cannot be finished without it** | `legal/privacy.html` | `legal.privacy.who2.blocked` | `hosting-country-and-transfer-basis` | **Igor via Hayk, and the lawyer** |
| 9 | Retention periods (non-client requests; accounting records) | `legal/privacy.html` | `legal.privacy.retention.blocked` | `retention-periods` | **Davit + the accountant** |
| 10 | The window in which a data request is answered | `legal/privacy.html` | `legal.privacy.rights.window` | `data-request-window` | **Davit / Hayk** |
| 11 | The rule for cancelling a one-off before it is carried out | `legal/refunds.html` | `legal.refund.oneoff.blocked` | `one-off-cancellation-rule` | **Davit** |
| 12 | Refund turnaround in business days — **the reviewer will look for it** | `legal/refunds.html` | `legal.refund.how.blocked` | `refund-turnaround-days` | **Davit, from Ameriabank** |
| 13 | Which language version governs | every legal document, tail strip | `legal.governingLanguage` | `governing-language` | **the lawyer** |
| 14 | Date of publication of the legal documents | every legal document, tail strip | `legal.updatedValue` | `publication-date` | **whoever publishes** — it is the date of the submission, not a decision |
| 15 | Dedicated copy for the three restored routes | `history.html`, `mission.html`, `values.html` | *(no keys exist)* | `route-copy` | **content lead** — see §6 |

The two blockers that were open in `docs/PROMPT-BANK-COMPLIANCE-UIUX.md` §7 and
are now **closed** by `rebrand/LEGAL-FACTS.md`: the registered entity spelling
(«ՄԵՄՈՐԻՔԵՅՐ» ՍՊԸ, printing `MemoryCare LLC` / `ООО «МемориКейр»` per locale,
with the registered Armenian name carried in every locale), and the registration
number, taxpayer number and legal address. All four are in every footer.

---

## 5. §4.11 link audit — the thirty routes in this set

Every `href` emitted by these pages, deduplicated.

**Resolve inside this set (200, real content):**
`/{loc}/about.html` · `/{loc}/history.html` · `/{loc}/mission.html` ·
`/{loc}/values.html` · `/{loc}/legal/restrictions.html` ·
`/{loc}/legal/privacy.html` · `/{loc}/legal/cookies.html` ·
`/{loc}/legal/refunds.html` · `/{loc}/legal/terms.html` ·
`/{loc}/legal/security.html` — for `loc` in `en`, `ru`, `am`. 30 files, all
present, none serving a 404 template.

**Stylesheets:** `/assets/tokens.css`, `/assets/base.css`,
`/assets/components.css`, and `/assets/brand/MemoryCare_logo-mark_color.svg` —
all present.

**Off-site:** `tel:+37455315323`, `tel:+37493154108`,
`https://wa.me/37455315323`, `https://wa.me/37493154108`,
`mailto:info@memorycare.am`. Numbers are the two confirmed mobiles; the e-mail
is live since 11.08.2026.

**Depend on the other two engineers — must exist before submission:**
`/{loc}/` (home) · `/{loc}/prices.html` · `/{loc}/how.html` ·
`/{loc}/report.html` · `/{loc}/family.html` · `/{loc}/contacts.html` ·
`/{loc}/consultation.html` · `/{loc}/account/`. These are linked from the header
and the footer, which appear on every page in this set, so **any one of them
missing is a §4.11 breach on all thirty of these routes as well as on its own.**
The header/footer route names are the assumption; if a filename changes, change
`ROUTES`/`NAV` in the generator and re-run, do not hand-edit thirty files.

**Nothing 200s while rendering a 404 in this set**, and no page in this set
links to a route the site does not intend to serve.

---

## 6. Notes a reviewer will raise, recorded rather than hidden

1. **`/am/` is the URL for Armenian.** `am` is Amharic; `hy` is Armenian. `lang`
   and `hreflang` are correct (`hy`) on all ten Armenian pages. The folder name
   is the lead's instruction and matches `strings/am.json`.
   `strings/RECONCILIATION.md` §12 asks for `/hy/`. One rename in `LOCALES` in
   the generator changes all thirty files and every link.
2. **`history.html`, `mission.html` and `values.html` have no strings of their
   own.** They are built from approved keys written for other pages — every
   sentence on them is a verified string, none is invented — and each carries a
   visible `[BLOCKED — this route has no strings…]` marker naming the content
   lead. Their `<h1>` is an existing approved heading key, and their `<title>` is
   that key composed with `common.brand`.
3. **`footer.copyright` in `am.json` prints `«MemoryCare» ՍՊԸ`**, which is not
   the registered name. Every other Armenian entity string uses
   `«ՄԵՄՈՐԻՔԵՅՐ» ՍՊԸ` correctly, including `footer.legal.entity` in the same
   footer. A reviewer cross-checking against the registry will see both forms on
   one page. One value in `strings/am.json`. → content lead.
4. **The bank holds `hambarcumian@gmail.com` for this company**; every footer
   prints `info@memorycare.am`, on the very domain the acquiring is for
   (`LEGAL-FACTS.md`). Update the bank's record or expect the question. → Davit.
5. **The registry's website field is `Գրառված չէ`** — empty. If the bank
   cross-checks it against the acquiring domain, fill it first. → Davit.
6. **The published address is a residential apartment.** Ruled by the owner and
   correct for §4.10.2; recorded so nobody is surprised it is in the footer of
   every page.
7. **`legal.cookies.p2` is a promise the build must keep.** It says these pages
   set no analytics and no advertising cookies, which is why there is no consent
   banner. Adding measurement, an advertising tag or an embedded map makes that
   page false and makes a banner necessary. This binds the other two engineers
   as much as this one.
8. **`prices.paymentReality` and `footer.payment.note` promise no date** for card
   acceptance. Keep it that way: a month published on a page the bank then misses
   is the worst available first broken promise.

---

## 7. What the bank will ask for that is in nobody's plan

1. **§3.7 — the chargeback supporting document.** For a disputed transaction the
   bank wants a description of what was delivered, the delivery address, date and
   time, the recipient's name and the **last four digits of the card**. Our visit
   report already carries the cemetery and plot, the date, the crew and a GPS
   point taken on site. It does **not** carry the customer's name or the card's
   last four, and there is **no export path** that turns a report into that
   document. Adding two fields and a print/PDF export now costs almost nothing;
   retrofitting it after the first chargeback is expensive. **Owner: the platform
   contractor, via Hayk.** Nobody has been asked.
2. **§3.9 and §5.3 — three-year retention of transaction records, and the bank's
   right to freeze a disputed amount for six months.** Neither appears in the
   privacy policy's retention section, which is itself blocked (#9). The
   accounting-retention carve-out is written (`legal.privacy.rights.accounting`)
   but has no number behind it. **Owner: Davit + the accountant + the lawyer.**
3. **§4.7 — the domain-ownership document**, and **§4.8 — the encryption
   certificate.** `legal.security.p1` publishes the claim that we hold the
   certificate. Somebody must actually hold both documents at submission.
   **Owner: Davit / Igor via Hayk.**
4. **§4.2 — the payment part of the site must be built and operated in a manner
   agreed with the bank.** That conversation has not happened, and the payment
   screens belong to the account-area engineer. It should happen before those
   screens are finalised, not after. **Owner: Davit.**
5. **§5.2 — standing monitoring.** This is not a gate that is passed and
   forgotten. This file is the artefact that answers a re-check; it needs an
   owner after launch. **Owner: Hayk.**
6. **A data-processing agreement with the platform developer.** The developer
   contract is unsigned and contains none. Blocker #8 cannot be closed without
   it, and §4.10.8 cannot be finished with blocker #8 open. **Owner: Hayk + the
   lawyer.**
7. **The client contract must be redrafted to match two things this site now
   publishes**: the seven-day repeat window counted **from delivery of the
   report** rather than from the visit date (`legal.terms.guarantees.p1`,
   `legal.refund.unhappy.p1`), and the four-visits-regardless winter clause
   stated on three pages as *a term of the contract*
   (`legal.terms.winter.p1`, `how.weather`). If the contract says otherwise, the
   first complaint is a dispute about our own copy. **Owner: the lawyer, via
   Hayk.**

---

## 8. How these files are produced

`rebrand/site/_includes/build-compliance-pages.py` reads
`rebrand/strings/{en,ru,am}.json` and writes all thirty routes plus the three
footer includes. It raises on a missing key, so a string that disappears breaks
the build instead of shipping as an empty element. Re-run it after any change;
do not hand-edit the generated files.

```
python3 rebrand/site/_includes/build-compliance-pages.py
cd rebrand/site/assets && sh tools/check-tokens.sh    # clean
```
