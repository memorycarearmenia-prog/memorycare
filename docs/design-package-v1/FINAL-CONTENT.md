# MemoryCare — Final Content Package

**English master copy. Every string the product needs, ready to paste.**
Content Strategist / UX Writer · v1.0 · 30.08.2026
Supersedes `03-content.md`, `r2-03-content.md` and every copy fragment in
`01`, `02`, `04`, `05` and their round-two memos.

Binding order applied throughout: `DECISIONS.md` and `DECISIONS-2.md` →
`BRIEF.md` → the five round-two memos → the five round-one proposals.
Where two memos disagreed and no owner ruling covered it, I chose, and every
such choice is listed in **§13**.

---

## 0. How to read this file

- Every string has a **stable key** in dot notation: `page.block.slot`.
  Keys are the keys in `content/strings.en.json`. **No literal text lives in a
  component.** `strings.hy.json` and `strings.ru.json` carry the same keys with
  `TODO-TRANSLATION` values.
- `{variable}` is a runtime value. The full allowlist is in §12.4. Any `{…}`
  not on that list is a build failure.
- `(n ch)` is the character count including spaces. Slots with a layout limit
  are all listed, counted and confirmed in **§5**.
- Sentence case for every heading and every button. Never Title Case.
- Strings marked **[OPEN]** are blocked on a person, not on writing. §13.2.

---

## 1. The binding decisions this package implements

| # | Ruling | Where it lands in this file |
|---|---|---|
| 1 | Legal entity is `MemoryCare LLC`, one word | §4.1, footer, About, legal, invoice, meta |
| 2 | Callback **within one business day**; report **within 48 hours** — identical in all six places | §4.4 names the six places, verbatim strings |
| 3 | Refund by **visits**, on the **amount actually paid**, shown as arithmetic | §9.9 cancellation, §6.9.2 Refund Policy |
| 4 | A subscription year is **12 months from signing**; "one visit in each season"; a missed winter visit is **added** to spring | §4.3, §6.3, §6.4, §9.8 |
| 5 | The name on the monument (`DECISIONS-2` §4, "the deceased's name") is **off by default** | §9.10 plot settings, §9.5 report masthead, §9.6 guest view |
| 6 | Optimal is marked **"Our recommendation"**, never "Most chosen" | `tariff.badge.leading`, §6.3 |
| 7 | Product names: **English first, Armenian in parentheses on first mention** on a page, English only thereafter | §4.2 |
| 8 | **95,000 ֏ AMD** appears in the calculator and on the pricing page, worded as mechanics, never as a discount | §6.3.5, §6.3.7 |
| 9 | One functional colour, terracotta, **form validation and payment failure only** | §8.4, §10.5 — the copy rules that go with it |
| 10 | Credit: **60 days, one credit only, the larger of the two, at signature, one credit per plot** | §6.3.5 |
| 11 | **No auto-charge on renewal**; offer goes out 30 days before the client's own anniversary | §11.2.8 |
| 12 | **No third-party analytics, therefore no cookie banner** | there is no cookie-banner string in this file, deliberately |
| 13 | **Past reports stay readable forever, including after cancellation** | §9.9 step 3, §11.2.11 |
| 14 | **Consent checkbox stays** in the request form | `form.consult.consent` |

---

## 2. Voice — the definition a stranger can apply

Five rules. Each is testable on a single sentence by someone who has never read
this project. If a sentence fails one of them, it is not our sentence.

### 2.1 State the fact before the feeling

The reader is deciding, often at one in the morning, whether to give money to
strangers in another country to work at their mother's grave. What settles that
is information: what happens, when, at what cost, and how they will know it was
done. The photographs carry the feeling. The words carry the facts.

> **Right** — "The crew visited on 14 September. The report has the
> photographs, the video and the GPS point recorded at the plot."
> **Wrong** — "We know how much this place means to you. Our devoted team
> treated it with all the love and respect your family deserves."

*Test:* can the reader check the sentence? If not, cut it or replace it with
something they can check.

### 2.2 Say what is true, including when it is not flattering

We have no clients, no history and no reviews. The admission is the asset. A
company that says "we are new, here is our method and here are our guarantees"
is more trustworthy than one claiming a decade. The same rule holds when
something goes wrong: the plain account beats the apology.

> **Right** — "We started in 2026 and we are taking on our first clients now.
> We have no reviews to show you yet and we will not borrow anyone else's."
> **Wrong** — "Trusted by hundreds of Armenian families worldwide."

*Test:* could someone contradict this sentence with one search? If yes, do not
write it. This is also why we never say nobody else in Yerevan does photo
reports — hush.am does, since about 2015, and it is checkable.

### 2.3 Address a person about their family, never a client about an object

Every noun has a warm option and a bureaucratic one. Take the warm one without
becoming sentimental. "Your family's plot", not "the site". "The crew", not
"the service team". No word in this product ever refers to a person who has
died as a category.

> **Right** — "Our crew went to your family's plot at Tokhmakh today and could
> not reach it."
> **Wrong** — "The service provider was unable to access the client's burial
> object at the designated location."

*Test:* read the sentence aloud to someone whose father died last year. If you
would soften it before saying it, rewrite it.

### 2.4 The reader's absence is a fact, not a failing

Nothing we write may make a person feel worse about not being in Yerevan, and
nothing may imply they could have gone themselves. This cuts in both
directions: it wounds the diaspora reader and it insults the local one. One
page serves both audiences; neither is named, neither is ranked.

> **Right** — "Care is rarely one person's decision and it should not be one
> person's inbox."
> **Wrong** — "When was the last time you were able to visit?" / "You can't be
> there, but we can." / "Save your Saturday."

*Test:* would this sentence read as an accusation to a person who has not been
to the cemetery in four years? If yes, delete it, however well it converts.

### 2.5 Bad news gets the facts, the proof, the next step, and a name

When something has gone wrong, the order is: what happened, whose fault it is,
what we are doing, who to call. Never an apology longer than the facts, never
"unfortunately", never "unforeseen circumstances", never a hedge.

> **Right** — "We went to your plot today and could not reach it. The cemetery
> was closed for a funeral. We return on 21 September. This visit does not come
> out of your subscription. Hayk has the crew's account of it — +374 93 154 108."
> **Wrong** — "Unfortunately, due to circumstances beyond our control, your
> scheduled service could not be completed at this time."

*Test:* after reading it, does the reader know the date we return and the name
of a person to call? If not, it is not finished.

### 2.6 The register in one line

Write as a competent professional writing to an adult about their family, in
plain English, with nothing to hide and nothing to sell in this particular
sentence.

---

## 3. The stop-list

Anything on this list is a build failure in `qa/strings.spec.ts`, in every
language.

### 3.1 Words about death and the person who died

`deceased` · `the departed` · `the fallen` · `remains` · `body` ·
`burial object` · `the site` (meaning the grave) · `object` · `unit` ·
`property` (meaning the plot) · `disposal` · `resting place` ·
`final resting place` · `eternal rest` · `passed on` ·
`gone but not forgotten`

**Say instead:** the grave · your family's plot · the plot · the monument ·
your mother / your father / the relationship the client used.

### 3.2 Product vocabulary banned by decision

`monthly` · `bestseller` · `most popular` · `most chosen` · `light visit` ·
`preventive visit` · `basic visit` · `heavy visit` · `2 full + 4 preventive` ·
`tier 1` / `tier 2` in client-facing copy · `QR code` · `memory page` ·
`digital memorial` · `coming soon`

`most chosen` is on this list because we have zero paying customers: it is a
claim about client behaviour that has not happened. The badge string is
`Our recommendation`.

### 3.3 Money words that turn the credit into a discount

`save` · `saving` · `discount` · `deal` · `offer` · `special offer` ·
`only` · `just` · `instead of` · `was / now` · `%` off a price ·
any `line-through` on 160,000 · any badge, colour or larger type on the 95,000.

### 3.4 Marketing register

`amazing` · `incredible` · `revolutionary` · `game-changing` · `seamless` ·
`effortless` · `hassle-free` · `peace of mind delivered` ·
`we've got you covered` · `worry-free` · `state-of-the-art` · `cutting-edge` ·
`best-in-class` · `world-class` · `premium experience` · `unlock` · `empower` ·
`elevate` · `curated` · `bespoke` · `journey` (meaning a process) ·
`solution` (meaning our service) · `leverage`

### 3.5 Guilt constructions — never, in any form

`when was the last time you visited` · `how long has it been` ·
`she would have wanted` · `he deserves better than this` ·
`distance is no excuse` · `you can't be there, but we can` ·
`don't let another year pass` · `while you're away, the grass grows` ·
any first-person door, chip or option that makes the reader say their own
absence out loud · any before/after caption implying neglect by the family
rather than the passage of time.

### 3.6 Claims we never make

- That we are the only ones, the first, that nobody else does this, that no one
  in Yerevan does photo reports. Also banned as strings: `the only` ·
  `the first` · `nobody else` · `unlike other` · `no one in Yerevan` ·
  `since 20` (any year claim).
- **No competitor is ever named on the site, in any language, in any form,
  including in an FAQ answer.** We describe the combination we offer.
- No testimonials, no review counts, no "trusted by N families", no years in
  business, no client numbers, no delivery date we have not agreed.
- The single permitted count is `{n_completed}` in the renewal message — our own
  visits, each with a report the reader can open and verify.

### 3.7 Interface words

Never: `Submit` · `OK` · `Learn more` · `Get started` · `Order` (as a button to
a login) · `Buy now` · `Upgrade` · `Oops` · `Something went wrong` · `Error` ·
`Invalid` · `Failed` · `Required field`.

### 3.8 Punctuation and typography

- **No exclamation marks.** Not one, in any language, in any state.
- **No emoji.** Not in the interface, not in email, not in push, above all not
  in errors.
- No ALL CAPS except the logo tagline as delivered.
- No ellipses for suspense. `Loading…` and `Sending…` only.
- No rhetorical questions as headings.
- Dates are written out: `14 September 2026`. Never `14/09/26` — an American
  and a European reader read that string differently.
- Numbers: `4 full visits`, never `four (4) visits`.

### 3.9 Constructions

- No passive voice that hides who acted. Not "the visit was postponed" —
  "we are moving the visit".
- No "unfortunately", no "we regret to inform you".
- No hedges: "may", "might", "should be able to". Either we commit or we say we
  do not know yet.
- No scolding imperatives: "Don't forget to…", "Make sure you…".
- No "simply", no "just". Nothing about this is simple for the reader.

---

## 4. Canonical facts, formats and names

### 4.1 The company

```
brand.name                MemoryCare
brand.entity              MemoryCare LLC
brand.tagline             HONORING MEMORY, CARING FOR LOVED ONES
brand.city                Yerevan, Armenia
contact.hayk.name         Hayk Manukyan
contact.hayk.role         Chief Business Development Officer
contact.hayk.phone        +374 93 154 108
contact.davit.name        Davit Hambardzumyan
contact.davit.role        Chief Executive Officer
contact.davit.phone       +374 55 315 323
contact.email             info@memorycare.am
contact.channels          Both numbers take WhatsApp and Viber.
company.address           {LEGAL_ADDRESS}      [OPEN]
company.regNumber         {REG_NUMBER}         [OPEN]
```

`MemoryCare` is one word, two capitals, never wrapped, never `Memory Care`,
never `MEMORYCARE`, never `MC`. The tagline carries **no full stop** and never
appears in the header.

### 4.2 Product names

English name first, Armenian in parentheses **on first mention on a page**;
English only thereafter. In the Armenian site the Armenian name is the display
name.

| Key | First mention | Later mentions | Price | Band |
|---|---|---|---|---|
| `product.inspection` | Inspection (Զննում) | Inspection | 20,000 ֏ AMD | one-off |
| `product.express` | Express (Էքսպրես խնամք) | Express | 65,000 ֏ AMD | one-off |
| `product.optimal` | Optimal (Օպտիմալ խնամք) | Optimal | 160,000 ֏ AMD a year | annual |
| `product.maximum` | Maximum (Մաքսիմում խնամք) | Maximum | 200,000 ֏ AMD a year | annual |
| `product.special` | Special (Հատուկ խնամք) | Special | priced after an Inspection | annual |

**[OPEN]** Four of the five Armenian forms come from the repo's project memory,
attached to a superseded price list. The owner or the localiser confirms them
before the Armenian build, including whether `խնամք` stays. Only `Զննում` is
confirmed. Do not guess from the old file.

### 4.3 Prices, surcharges, credit, the subscription year

```
price.inspection      20,000 ֏ AMD
price.express         65,000 ֏ AMD
price.optimal         160,000 ֏ AMD a year
price.maximum         200,000 ֏ AMD a year
surcharge.annual.area        +10,000 ֏ AMD a year for each m² above 16
surcharge.annual.monument    +30,000 ֏ AMD a year for each monument above 2
surcharge.express.area       +2,500 ֏ AMD per m² above 16
surcharge.express.monument   +7,500 ֏ AMD per monument above 2
coverage.base         up to 16 m² and up to 2 monuments
calculator.ceiling    100 m² and 10 monuments
credit.window         60 days
credit.rule           one credit only, the larger of the two, applied when the
                      annual subscription is signed, one credit per plot
year.definition       12 months from the date the subscription is signed
```

**Currency format, without exception:** `160,000 ֏ AMD` — symbol immediately
after the numeral, the letters AMD after a space. In body copy, in tables, in
the calculator, in the portal, in email, on the invoice and in the PDF. Never
`160k`, never the symbol alone, never `AMD 160,000`. Any figure in another
currency is labelled approximate and never appears in a total.

**Visit language:** every visit is a full visit. There is no smaller kind of
visit and copy never implies one. Optimal is "four full visits, one in each
season" inside the client's own twelve months. Maximum is "six full visits
across the year" — never "monthly", never "every two months".

`year.winterRule` (used in Terms, How it works and the visit list):
> **`If the weather never allows a winter visit, that visit is added to spring.
> You receive four full visits whatever the winter does.`** (118 ch)

### 4.4 The two public promises — identical in six places each

**Callback.**
`promise.callback` = **`We reply within one business day, Yerevan time (UTC+4).`** (55 ch)

The six places, all carrying this exact sentence, no softening, no sharpening:
1. `form.consult.intro` — the consultation form
2. `form.consult.success.body` — the in-place confirmation
3. `email.consultAck.body` — the acknowledgement email
4. `footer.hours` — every page footer
5. `contacts.hours.line` — the Contacts page
6. `how.step1.body` — How it works, step 1

**Report.**
`promise.report` = **`The report is in your portal within 48 hours of the visit.`** (58 ch)

The six places:
1. `home.report.body` — Home, the report block
2. `how.step5.body` — How it works, step 5
3. `sample.intro.body` — the sample report page
4. `portal.first.next.3` — the portal first-entry screen
5. `report.state.preparing.body` — the report-being-prepared state
6. `email.reportReady.body` — the report-ready email

Nobody may localise these two numbers differently. They are one string each.

### 4.5 One term per thing

| Canonical | Never |
|---|---|
| Request a consultation (button) | Request a free consultation (that is the form heading), Free consultation, Get started, Contact us |
| Visit report | report summary, visit summary |
| Sample report | report example |
| Our recommendation | Most chosen, bestseller, most popular, leading choice |
| One-off · not a subscription | ONE-OFF · NO SUBSCRIPTION |
| Full visit | deep clean, heavy visit, standard visit |
| Family Circle | family circle in lower case |
| Owner · Family manager · Family member · Guest | account holder, payer, subscriber, manager, member, viewer, link holder |
| Local contact | beneficiary, nominated relative |
| The crew | our team, the service team, operatives, technicians |
| The plot / your family's plot | the site, the object, the grave site |
| Visits (portal tab) | Reports (a report lives inside a visit) |
| Pay by bank transfer | Pay online, while card acquiring is not live |
| MemoryCare LLC | Memory Care LLC, MEMORYCARE, MC |
| `160,000 ֏ AMD` | `֏` alone, `AMD` alone, `160k` |

### 4.6 The plot label and the name on the monument

`{plot_label}` renders from the plot record: `{cemetery} · {sector} · {plot}`.
The name on the monument is a separate field with three modes —
`none` (default), `family_name`, `full_name` — set by the Owner on the plot,
plainly worded and reversible. **Default is `none`: the report shows cemetery,
sector and plot, and no name.** Turning the setting off also removes the name
from links already issued. Strings: §9.10.3.

---

## 5. Character limits and compliance

The two limits named in the brief for this package are **H1 ≤ 48** and
**primary button ≤ 22**. The rest are the converged budgets from the round-two
memos (02 §1.1/§4.7, 01 §C, 05 §4.12). Every constrained English string in this
package is listed here with its count. **All fit.** Armenian runs about 25%
longer and Russian about 20%: buttons wrap to two lines with the label centred,
badges wrap rather than ellipsise, and no slot below truncates.

### 5.1 Navigation, ceiling 16

| Key | String | ch | Fits |
|---|---|---|---|
| `nav.how` | How it works | 12 | yes |
| `nav.pricing` | Pricing | 7 | yes |
| `nav.report` | Sample report | 13 | yes |
| `nav.family` | Family Circle | 13 | yes |
| `nav.about` | About | 5 | yes |
| `nav.signin` | Sign in | 7 | yes |

### 5.2 Buttons, ceiling 22 (the primary CTA sits exactly on it)

| Key | String | ch | Fits |
|---|---|---|---|
| `cta.primary` | Request a consultation | 22 | yes |
| `cta.sampleReport` | See a sample report | 19 | yes |
| `cta.openSample` | Open a sample report | 20 | yes |
| `cta.pricing` | See full pricing | 16 | yes |
| `cta.howItWorks` | See how it works | 16 | yes |
| `cta.familyCircle` | See Family Circle | 17 | yes |
| `cta.inspection` | Book an Inspection | 18 | yes |
| `cta.calcConsult` | Use these figures | 17 | yes |
| `cta.openReport` | Open the report | 15 | yes |
| `cta.copyLink` | Copy link | 9 | yes |
| `cta.invite` | Invite someone | 14 | yes |
| `cta.inviteFamily` | Invite your family | 18 | yes |
| `cta.sendInvite` | Send the invitation | 19 | yes |
| `cta.sendAgain` | Send again | 10 | yes |
| `cta.cancelInvite` | Cancel the invitation | 21 | yes |
| `cta.keepAccess` | Keep their access | 17 | yes |
| `cta.bankTransfer` | Pay by bank transfer | 20 | yes |
| `cta.openInvoice` | Open the invoice | 16 | yes |
| `cta.copyBank` | Copy the bank details | 21 | yes |
| `cta.repeatVisit` | Ask for a repeat visit | 22 | yes |
| `cta.tellUs` | Tell us what happened | 21 | yes |
| `cta.tryAgain` | Try again | 9 | yes |
| `cta.save` | Save changes | 12 | yes |
| `cta.signin` | Sign in | 7 | yes |
| `cta.sending` | Sending… | 8 | yes |
| `cta.cancelSub` | Cancel my subscription | 22 | yes |
| `cta.keepSub` | Keep my subscription | 20 | yes |
| `cta.backToReports` | Back to my reports | 18 | yes |
| `cta.showOnMap` | Show on map | 11 | yes |
| `cta.continue` | Continue | 8 | yes |
| `cta.goBack` | Go back | 7 | yes |
| `cta.sendRequest` | Send the request | 16 | yes |
| `cta.addNote` | Add a note | 10 | yes |
| `cta.talkChange` | Talk about changing | 19 | yes |

### 5.3 Headings, H1 ceiling 48, section H2 ceiling 48

| Key | String | ch | Fits |
|---|---|---|---|
| `home.hero.h1` | You will see exactly what was done, and when. | 45 | yes |
| `pricing.h1` | Prices | 6 | yes |
| `how.h1` | How it works | 12 | yes |
| `sample.h1` | A sample report | 15 | yes |
| `family.h1` | Family Circle | 13 | yes |
| `about.h1` | About MemoryCare | 16 | yes |
| `contacts.h1` | Contacts | 8 | yes |
| `guarantees.h1` | Our guarantees | 14 | yes |
| `home.h2.what` | What a subscription covers | 26 | yes |
| `home.h2.report` | The report is the product | 25 | yes |
| `home.h2.family` | One plot, one family, separate accounts | 39 | yes |
| `home.h2.guarantees` | What we commit to in writing | 28 | yes |
| `home.h2.how` | How it works | 12 | yes |
| `home.h2.pricing` | Prices, the same for everyone | 29 | yes |
| `home.h2.founders` | The people you will speak to | 28 | yes |
| `home.h2.closing` | Talk to us before you decide anything | 37 | yes |
| `pricing.fork.heading` | Two ways to start | 17 | yes |

### 5.4 Hero, ceiling: eyebrow 42, standfirst 105, support line 40

| Key | String | ch | Fits |
|---|---|---|---|
| `home.hero.eyebrow` | Yerevan cemeteries · scheduled care | 35 | yes |
| `home.hero.sub` | Scheduled care for a family plot in Yerevan. Photo, video and a GPS point after every visit. | 92 | yes |
| `home.hero.ctaSupport` | No payment now. No account needed. | 34 | yes |
| `home.hero.rail` | Date · Cemetery · GPS confirmed | 31 | yes |

### 5.5 Pricing furniture

| Key | String | ch | Limit | Fits |
|---|---|---|---|---|
| `pricing.band1.heading` | One-off services | 16 | 30 | yes |
| `pricing.band2.heading` | Annual subscriptions | 20 | 30 | yes |
| `pricing.oneoff.eyebrow` | One-off · not a subscription | 28 | 30 | yes |
| `pricing.fork.door1` | I want to know what it needs | 28 | 30 | yes |
| `pricing.fork.door2` | I want it looked after | 22 | 30 | yes |
| `tariff.badge.leading` | Our recommendation | 18 | 18 | yes |
| `tariff.inspection.desc` | One assessment visit. We record the plot's condition. No cleaning. | 66 | 74 | yes |
| `tariff.express.desc` | One full visit: deep cleaning of the plot and every monument. | 61 | 74 | yes |
| `tariff.optimal.desc` | Four full visits, one in each season. Report after every visit. | 63 | 74 | yes |
| `tariff.maximum.desc` | Six full visits across the year. Report after every visit. | 58 | 74 | yes |
| `tariff.special.desc` | Larger plot, more monuments, or several family plots. | 53 | 74 | yes |

`tariff.badge.leading` is the one budget this package raises: 05's badge ceiling
was 14, and the owner's mandated string is 18. The owner string wins; the badge
wraps to two lines in `hy` and `ru` and never ellipsises (02 §4.11).

### 5.6 Feature bullets, ceiling 48

| Key | String | ch | Fits |
|---|---|---|---|
| `tariff.feature.report` | Photo, video and GPS report after every visit | 45 | yes |
| `tariff.feature.portal` | Client portal and Family Circle | 31 | yes |
| `tariff.feature.guarantees` | Covered by the MemoryCare guarantees | 36 | yes |
| `tariff.feature.visits4` | 4 full visits, one in each season | 33 | yes |
| `tariff.feature.visits6` | 6 full visits across the year | 29 | yes |
| `tariff.feature.nocleaning` | No cleaning on this visit | 25 | yes |
| `tariff.feature.credited` | Credited toward an annual subscription | 38 | yes |

### 5.7 Guarantees, title 30 / body 110

| Key | String | ch | Fits |
|---|---|---|---|
| `guarantee.1.title` | Free repeat visit in 7 days | 27 | yes |
| `guarantee.1.body` | Tell us within seven days of a report and we come back and redo the work at our cost. | 85 | yes |
| `guarantee.2.title` | We answer for damage | 20 | yes |
| `guarantee.2.body` | If we damage a monument or the plot, we repair or replace it at our cost. | 73 | yes |
| `guarantee.3.title` | Cancel and get the rest back | 28 | yes |
| `guarantee.3.body` | Cancel at any time and we return the visits you have paid for and not received, pro rata. | 89 | yes |

### 5.8 Status chips, ceiling 24

| Key | String | ch | Fits |
|---|---|---|---|
| `status.completed` | Completed | 9 | yes |
| `status.scheduled` | Scheduled | 9 | yes |
| `status.moved` | Visit moved — weather | 21 | yes |
| `status.noaccess` | Could not reach the plot | 24 | yes |
| `status.preparing` | Report being prepared | 21 | yes |
| `status.revisit` | Repeat visit requested | 22 | yes |
| `status.gps` | GPS confirmed | 13 | yes |

### 5.9 Roles, name 16 / short description 66–70

| Key | String | ch | Fits |
|---|---|---|---|
| `role.owner` | Owner | 5 | yes |
| `role.manager` | Family manager | 14 | yes |
| `role.member` | Family member | 13 | yes |
| `role.guest` | Guest | 5 | yes |
| `role.owner.short` | Pays, changes or cancels the subscription, invites and removes people. | 70 | yes |
| `role.manager.short` | Sees every report, can request extra work. Cannot spend or cancel. | 66 | yes |
| `role.member.short` | Sees every report and every photograph. Cannot order paid work. | 63 | yes |

### 5.10 Progress rail, ceiling 20; verification rail labels, ceiling 12

`progress.1` Payment received (16) · `progress.2` Date confirmed (14) ·
`progress.3` Crew visits (11) · `progress.4` Report ready (12) — all fit.

`rail.label.date` Date (4) · `rail.label.cemetery` Cemetery (8) ·
`rail.label.plot` Plot (4) · `rail.label.crew` Crew (4) ·
`rail.label.arrival` Arrived (7) · `rail.label.departure` Left (4) ·
`rail.label.gps` GPS (3) — all fit.

### 5.11 Meta titles (≤60) and descriptions (≤155)

Counted in §7. Every one fits; every one disambiguates from dementia care.

### 5.12 Email subjects (≤52), push titles (≤40), push bodies (≤110)

Counted in §11. Every one fits.

### 5.13 Errors and validation

Error panel heading ≤40, body ≤140, validation message ≤90. Counted in §8.4 and
§10.5; every one fits. The one message that would have breached 80 characters is
split into two sentences on two lines rather than shortened.

### 5.14 Deliberately long, and permitted

| Key | ch | Rule |
|---|---|---|
| `link.talkFirst` — Actually, I would like to talk to someone first | 47 | tertiary text link, may wrap to three lines |
| `link.guestFeedback` — Something is not right with this report | 39 | tertiary text link on the guest report |
| `report.crewNote` | 120–320 | wraps, never clamped, never truncated |
| `form.consult.optional.placeholder` | 96 | placeholder, wraps |

---

## 6. Marketing site — every block, every string

Routes are `/en/…`, `/hy/…`, `/ru/…` from day one. The guest report is `/r/:shareToken/`.

### 6.0 Global chrome

#### 6.0.1 Header

```
nav.how              How it works
nav.pricing          Pricing
nav.report           Sample report
nav.family           Family Circle
nav.about            About
nav.signin           Sign in
cta.primary          Request a consultation
lang.a11yLabel       Choose site language
lang.hy              Հայերեն
lang.en              English
lang.ru              Русский
header.callA11y      Call MemoryCare on +374 93 154 108
header.menuA11y      Open the menu
header.wordmark      MemoryCare
```

There are three languages. Never build a fourth slot.

#### 6.0.2 Footer — identical on every page (bank requirement)

```
footer.tagline       HONORING MEMORY, CARING FOR LOVED ONES
footer.blurb         Care for family graves in Yerevan cemeteries.
                     Scheduled visits, photo and video reports, GPS confirmation.

footer.contact.h     Contact
footer.contact.hayk  Hayk Manukyan, Chief Business Development Officer
                     +374 93 154 108
footer.contact.davit Davit Hambardzumyan, Chief Executive Officer
                     +374 55 315 323
footer.contact.email info@memorycare.am
footer.contact.chan  We answer on WhatsApp and Viber on both numbers.
footer.hours         We reply within one business day, Yerevan time (UTC+4).

footer.company.h     Company
footer.company.1     MemoryCare LLC, Yerevan, Armenia
footer.company.2     Registered address: {LEGAL_ADDRESS}          [OPEN]
footer.company.3     Company registration number: {REG_NUMBER}    [OPEN]

footer.site.h        Site
footer.site.links    How it works · Pricing · Sample report · Family Circle ·
                     Our guarantees · About · Contacts

footer.legal.h       Legal
footer.legal.links   Privacy Policy · Refund Policy · Terms of Service ·
                     What we cannot do

footer.copyright     © 2026 MemoryCare LLC. All rights reserved.
```

Phone numbers are `tel:` links. WhatsApp is a real `wa.me` link, never text.

#### 6.0.3 The CTA pair, everywhere

```
cta.primary          Request a consultation           (22 ch, the one label site-wide)
cta.support          No payment now. No account needed.
form.consult.heading Request a free consultation      (heading, not a button)
cta.secondary.site   See a sample report
cta.secondary.pay    Pay by bank transfer
```

Never `Learn more`. Never `Register` as a primary action. Never `Order` on a
tariff card leading to a login form.

#### 6.0.4 The mobile action bar

```
bar.call.a11y        Call Hayk on +374 93 154 108
bar.cta              Request a consultation
```

One call icon and one button carrying the site-wide label. The bar hides while
a form field has focus and while the calculator result panel is on screen.

---

### 6.1 Home — `/en/`

#### Block 1 — Hero

```
home.hero.eyebrow    Yerevan cemeteries · scheduled care
home.hero.h1         You will see exactly what was done, and when.
home.hero.sub        Scheduled care for a family plot in Yerevan. Photo, video
                     and a GPS point after every visit.
home.hero.rail       Date · Cemetery · GPS confirmed
home.hero.cta        Request a consultation
home.hero.ctaSupport No payment now. No account needed.
home.hero.secondary  See a sample report
home.hero.figCaption A visit report. Every one carries the date, the plot, the
                     crew, the GPS point and the photographs.
home.hero.placeholder
                     PHOTO · report preview, metadata strip and one plot frame ·
                     3:2 · 1600×1067 · replace after 09.2026 shoot
```

The report preview is cropped by the fold on purpose. What survives the crop is
the metadata strip and the `GPS confirmed` chip, never a cropped photograph.

#### Block 2 — What a subscription covers

```
home.what.h2         What a subscription covers
home.what.1.h        We visit on a schedule
home.what.1.body     Four or six full visits a year, spread across the seasons.
                     Every visit is a full visit — the whole plot and every
                     monument, cleaned, not a look around.
home.what.2.h        We clean properly
home.what.2.body     Steam, pressure washing, vacuum extraction and chemistry
                     chosen for the stone. Granite, basalt and tuff are not
                     treated the same way.
home.what.3.h        We prove it
home.what.3.body     Photographs on arrival and after the work, video, and the
                     GPS point recorded on site. It arrives in your portal and
                     you can forward it to anyone in the family.
```

#### Block 3 — The report is the product

```
home.report.h2       The report is the product
home.report.body     We do not ask you to trust us. Each visit ends with a
                     record: the date, the plot, the crew who went, the GPS
                     point, photographs of the plot on arrival and after the
                     work, and a short video. The report is in your portal
                     within 48 hours of the visit. It opens on a phone and it
                     can be forwarded by a plain link, so relatives who will
                     never sign in to anything can still see it.
home.report.cta      Open a sample report
```

#### Block 4 — Family Circle

```
home.family.eyebrow  Family Circle
home.family.h2       One plot, one family, separate accounts
home.family.body     Care is rarely one person's decision and it should not be
                     one person's inbox. Invite your brother, your aunt, your
                     cousin. Each of them gets their own access and sees every
                     report. You decide who can order extra work and who can
                     change the subscription — the person who pays keeps that
                     control.
home.family.cta      See Family Circle
```

#### Block 5 — Guarantees (this block replaces testimonials)

```
home.guarantees.h2   What we commit to in writing
guarantee.1.title    Free repeat visit in 7 days
guarantee.1.body     Tell us within seven days of a report and we come back and
                     redo the work at our cost.
guarantee.2.title    We answer for damage
guarantee.2.body     If we damage a monument or the plot, we repair or replace
                     it at our cost.
guarantee.3.title    Cancel and get the rest back
guarantee.3.body     Cancel at any time and we return the visits you have paid
                     for and not received, pro rata.
guarantee.footnote   The full conditions are in our Terms of Service and Refund
                     Policy.
guarantee.cta        Our guarantees
```

Immediately below, at body size or a step above, in a bordered panel — never as
small print:

```
home.honesty.body    We started in 2026 and we are taking on our first clients
                     now. We have no reviews to show you yet and we will not
                     borrow anyone else's. What we can show you is the method,
                     the prices and the guarantees above — and after the first
                     visit, your own report.
```

#### Block 6 — How it works, short

```
home.how.h2          How it works
home.how.1.h         A conversation
home.how.1.body      You tell us where the plot is. We agree the schedule and
                     the product. Nothing is signed on the call.
home.how.2.h         We find the plot and record it
home.how.2.body      On the first visit the crew locates the plot and records
                     its GPS point, and then does the full work — so every
                     later report can be compared with the first.
home.how.3.h         Visits through the year
home.how.3.body      Four or six full visits in the twelve months from the day
                     you sign, one in each season for Optimal.
home.how.4.h         A report after every visit
home.how.4.body      Photographs, video, GPS and a note from the crew, in the
                     portal within 48 hours and shareable by a plain link.
home.how.cta         See how it works
```

#### Block 7 — Pricing teaser (no calculator on Home)

```
home.pricing.h2      Prices, the same for everyone
home.pricing.body    One price list — the same in Yerevan and in Los Angeles.
                     Prices cover a plot of up to 16 m² with up to 2 monuments;
                     anything larger is worked out openly with the calculator
                     on the pricing page.
home.pricing.1       Inspection (Զննում) — 20,000 ֏ AMD, a one-off assessment visit
home.pricing.2       Express (Էքսպրես խնամք) — 65,000 ֏ AMD, one full cleaning visit
home.pricing.3       Optimal (Օպտիմալ խնամք) — 160,000 ֏ AMD a year, four full visits
home.pricing.4       Maximum (Մաքսիմում խնամք) — 200,000 ֏ AMD a year, six full visits
home.pricing.cta     See full pricing
```

#### Block 8 — The people you will speak to

```
home.founders.h2     The people you will speak to
home.founders.body   Two people answer this company's phones, and these are
                     their own numbers.
home.founders.1      Hayk Manukyan · Chief Business Development Officer
                     +374 93 154 108 · WhatsApp, Viber
home.founders.2      Davit Hambardzumyan · Chief Executive Officer
                     +374 55 315 323 · WhatsApp, Viber
home.founders.ph     PHOTO · founder portrait, plain ground · 1:1 · 800×800 ·
                     replace after 09.2026 shoot
```

#### Block 9 — FAQ

```
home.faq.h2          Questions people ask first
home.faq.1.q         How do I know the crew went to my family's plot?
home.faq.1.a         Every report carries the coordinates recorded by the crew's
                     device at the plot, on the day, with the arrival and
                     departure times. The photographs are taken from the same
                     standing positions each visit, so you can compare one
                     report against the next.
home.faq.2.q         Is the price different for someone paying from abroad?
home.faq.2.a         No. One price list — the same in Yerevan and in Los
                     Angeles. Every price is on the pricing page and the
                     calculator works out plots larger than 16 m² before you
                     speak to anyone.
home.faq.3.q         What happens if the weather stops a visit?
home.faq.3.a         We move it and tell you the same day, with the new date.
                     The visit is not lost and your subscription still covers
                     all of its visits. If the weather never allows a winter
                     visit, that visit is added to spring.
home.faq.4.q         Can my family see the reports without an account?
home.faq.4.a         Yes. Every report has a link you can send by WhatsApp or
                     Viber. It opens without an account, shows the report and
                     nothing else — no prices and no sign-up.
home.faq.5.q         What is not included?
home.faq.5.a         Restoration of stone, re-cutting or regilding of lettering,
                     repairs to kerbs and foundations, replacing a monument, and
                     anything needing cemetery administration approval. We can
                     price those separately. The full list is on our
                     "What we cannot do" page.
home.faq.6.q         Can I cancel?
home.faq.6.a         At any time, from the portal, without phoning us. We return
                     the visits you have paid for and not received, worked out
                     on what you actually paid.
```

#### Block 10 — Closing CTA

```
home.closing.h2      Talk to us before you decide anything
home.closing.body    An annual subscription is a real sum and you have never met
                     us. Start with a conversation: we will tell you what the
                     plot needs and what it would cost, and you decide
                     afterwards.
[consultation form component — §8.1]
```

The consultation form never sits on the dark band: the error colour is
illegible on Anthracite (1.57).

---

### 6.2 Guarantees — `/en/guarantees/`

```
guarantees.h1        Our guarantees
guarantees.sub       We have no reviews yet. These are the commitments we make
                     in writing instead, and they are in the Terms of Service.
[guarantee.1 / 2 / 3 — same strings as §6.1 Block 5]

guarantees.detail.1.h  How the repeat visit works
guarantees.detail.1    Tell us within seven days of receiving a report that the
                       work was not right. We agree a date, the crew returns and
                       redoes the work, and you get a new report. You pay
                       nothing for that visit and it does not use one of the
                       visits in your subscription.
guarantees.detail.2.h  What we mean by damage
guarantees.detail.2    If our crew damages a monument, a kerb or the planting,
                       we repair it or replace it at our cost. Damage that was
                       already there when we arrived is photographed and named
                       in the report, and we do not clean over it and call it
                       done.
guarantees.detail.3.h  How a refund is worked out
guarantees.detail.3    We refund the visits you have paid for and not received,
                       in proportion, calculated on the amount you actually
                       paid. Two of four visits taken on a 160,000 ֏ AMD
                       subscription returns 160,000 × 2/4 = 80,000 ֏ AMD. If an
                       Express visit was credited and you paid 95,000 ֏ AMD, the
                       same case returns 95,000 × 2/4 = 47,500 ֏ AMD. You see
                       the arithmetic in the portal before you confirm.
guarantees.limits.h    What the guarantees do not cover
guarantees.limits      They do not cover restoration work we did not do, damage
                       caused by weather or by other people between our visits,
                       or work that the cemetery administration will not permit.
                       Those are listed in full on "What we cannot do".
guarantees.cta         Request a consultation
```

---

### 6.3 Pricing — `/en/pricing/`

#### 6.3.1 Head

```
pricing.h1           Prices
pricing.sub          One price list — the same in Yerevan and in Los Angeles.
pricing.coverage     Prices cover a plot of up to 16 m² with up to 2 monuments.
                     Above that, the calculator below shows the exact figure
                     before you speak to anyone.
```

#### 6.3.2 The fork

```
pricing.fork.heading Two ways to start
pricing.fork.sub     Some people want an assessment first. Some already know
                     what they want done. Both routes are below.
pricing.fork.door1   I want to know what it needs        → the one-off band
pricing.fork.door2   I want it looked after              → the annual band
```

#### 6.3.3 Band 1 — one-off services

```
pricing.band1.heading    One-off services
pricing.oneoff.eyebrow   One-off · not a subscription

tariff.inspection.name   Inspection (Զննում)
tariff.inspection.price  20,000 ֏ AMD, paid once
tariff.inspection.desc   One assessment visit. We record the plot's condition.
                         No cleaning.
tariff.inspection.body   We locate the plot and record it: a written account of
                         its condition, photographs, video, the GPS point, and a
                         list of the work we would recommend with a price
                         against each item. No cleaning is carried out on an
                         Inspection visit.
tariff.inspection.f1     No cleaning on this visit
tariff.inspection.f2     Photo, video and GPS report after every visit
tariff.inspection.f3     Credited toward an annual subscription
tariff.inspection.cta    Request a consultation

tariff.express.name      Express (Էքսպրես խնամք)
tariff.express.price     65,000 ֏ AMD, paid once
tariff.express.desc      One full visit: deep cleaning of the plot and every
                         monument.
tariff.express.body      Steam, pressure washer, vacuum extraction and chemistry
                         matched to the stone, on the whole plot and every
                         monument. Includes the full report and access to the
                         client portal.
tariff.express.f1        Photo, video and GPS report after every visit
tariff.express.f2        Client portal and Family Circle
tariff.express.f3        Credited toward an annual subscription
tariff.express.cta       Request a consultation
```

Both one-off cards carry the same one-line note under the price:

```
tariff.oneoff.creditLine Credited in full toward an annual subscription signed
                         within 60 days.
```

#### 6.3.4 Band 2 — annual subscriptions

```
pricing.band2.heading    Annual subscriptions
pricing.band2.note       Every visit is a full visit — the whole plot and every
                         monument, cleaned. There is no smaller kind of visit.
                         A subscription runs for twelve months from the day you
                         sign it.

tariff.badge.leading     Our recommendation          (on Optimal only)
tariff.optimal.name      Optimal (Օպտիմալ խնամք)
tariff.optimal.price     160,000 ֏ AMD a year
tariff.optimal.desc      Four full visits, one in each season. Report after
                         every visit.
tariff.optimal.f1        4 full visits, one in each season
tariff.optimal.f2        Photo, video and GPS report after every visit
tariff.optimal.f3        Client portal and Family Circle
tariff.optimal.f4        Covered by the MemoryCare guarantees
tariff.optimal.cta       Request a consultation

tariff.maximum.name      Maximum (Մաքսիմում խնամք)
tariff.maximum.price     200,000 ֏ AMD a year
tariff.maximum.desc      Six full visits across the year. Report after every
                         visit.
tariff.maximum.f1        6 full visits across the year
tariff.maximum.f2        Photo, video and GPS report after every visit
tariff.maximum.f3        Client portal and Family Circle
tariff.maximum.f4        Covered by the MemoryCare guarantees
tariff.maximum.cta       Request a consultation
```

#### 6.3.5 The credit block — stated once, under Band 1, always visible

Never a tooltip, never a footnote, never behind a disclosure.

```
pricing.credit.h3        How a one-off payment is credited
pricing.credit.intro     If you have already paid for an Inspection or an
                         Express visit, that amount comes off the price when you
                         sign an annual subscription.
pricing.credit.firstYear An Express visit paid at 65,000 ֏ AMD and an Optimal
                         subscription at 160,000 ֏ AMD means
                         160,000 − 65,000 = 95,000 ֏ AMD for the first year, and
                         160,000 ֏ AMD in each year after that.
pricing.credit.1         The credit applies within 60 days of paying for the
                         one-off service.
pricing.credit.2         One amount is credited, not two. If you paid for both an
                         Inspection and an Express visit, the larger of the two
                         is credited.
pricing.credit.3         The credit is applied when the annual subscription is
                         signed. It does not move between one-off services — an
                         Inspection is not credited towards an Express visit.
pricing.credit.4         One credit for each plot.
pricing.credit.5         Express is 65,000 ֏ AMD every time. There is no reduced
                         repeat price.
```

**The rules that keep this a mechanic and not a discount.** They are enforced in
`qa/prices.spec.ts`, not left to judgement:
1. Always show the subtraction, never the bare result.
2. Always name the mechanism in the same sentence: an amount already paid comes
   off.
3. Always state the second year in the same sentence. This is what stops 95,000
   reading as a price somebody set, and it prevents the renewal conversation a
   year later going badly.
4. None of the words in §3.3 may appear near a price.
5. No strike-through on 160,000, no colour on the 95,000, no badge, no ribbon,
   no larger type. Same type role as the sentence around it.
6. Full currency form every time.
7. 160,000 ֏ AMD is the only price on the Optimal card. The calculator's default
   state is the annual mode showing 160,000.
8. Not in the hero. Not as the Express card's headline price.

#### 6.3.6 The calculator

```
calc.h2              Work out the price for your plot
calc.sub             The price is on the page before you speak to anyone. It
                     does not change depending on where you are calling from.
calc.slider1.label   Plot area
calc.slider1.unit    m²
calc.slider1.helper  If you are not sure, an approximate figure is fine — we
                     measure it on the first visit and confirm the price before
                     any work.
calc.slider1.tick1   16 m² included
calc.slider2.label   Number of monuments
calc.slider2.helper  Headstones and memorial structures on the plot.
calc.slider2.tick1   2 included

calc.result.optimal  Optimal — 4 full visits
calc.result.maximum  Maximum — 6 full visits
calc.result.express  Express — one full visit
calc.result.value    {price} ֏ AMD a year
calc.result.valueOne {price} ֏ AMD, paid once

calc.breakdown.base       Base (up to 16 m², 2 monuments) — {price} ֏ AMD
calc.breakdown.area       {n} m² above 16 — +{price} ֏ AMD
calc.breakdown.monuments  {n} monuments above 2 — +{price} ֏ AMD
calc.breakdown.total      Total — {price} ֏ AMD a year

calc.surcharge.1     Above 16 m²: +10,000 ֏ AMD a year for each additional m².
calc.surcharge.2     Above 2 monuments: +30,000 ֏ AMD a year for each additional
                     monument.
calc.surcharge.3     The same surcharge applies to Optimal and to Maximum.
calc.surcharge.4     For a one-off Express visit: +2,500 ֏ AMD per m² and
                     +7,500 ֏ AMD per monument above the same limits.

calc.fx              ≈ ${amount} · charged in AMD. An approximate conversion at
                     {rate_date}, for orientation only.

calc.credit.label    If you take Optimal within 60 days
calc.credit.value    160,000 − 65,000 = 95,000 ֏ AMD for your first year
calc.credit.note     And 160,000 ֏ AMD in each year after that.

calc.cta             Use these figures
calc.cta.helper      We carry your figures into the request, so the person who
                     calls you is looking at the same number.
calc.included.link   What is included in a full visit?
calc.fineprint       These prices cover the plot as you have configured it. The
                     final figure is confirmed after we have seen the plot.
```

The 95,000 line appears only in the one-off (Express) mode, as a consequence of
a path the visitor chose, recomputed with surcharges. The number changes
instantly with the sliders — no count-up.

Ceiling state (above 100 m² or 10 monuments) — this replaces the result panel,
and it is not an error:

```
calc.ceiling.h       This one we should price together
calc.ceiling.body    A plot this size is outside what a calculator can price
                     honestly. We start with an Inspection — 20,000 ֏ AMD — and
                     give you a written price for the actual work.
calc.ceiling.cta     Book an Inspection
calc.ceiling.alt     Request a consultation
```

#### 6.3.7 Special — one line beneath the calculator, not a card

```
pricing.special.h    Special (Հատուկ խնամք)
pricing.special.body Larger plot, more monuments, or several family plots.
                     Every Special begins with an Inspection, so that we price
                     real work on a plot we have seen rather than a guess.
pricing.special.cta  Book an Inspection
```

#### 6.3.8 Payment reality

```
pay.h2               How to pay
pay.transfer.h       Bank transfer
pay.transfer.body    Our first clients pay by bank transfer. We send an invoice
                     with the full details and confirm in the portal when the
                     payment arrives. Payments from abroad are normal for us and
                     usually take one to three working days.
pay.card.h           Card payment
pay.card.body        Card payment on the site is being set up with our bank and
                     is not live yet. We are not promising a date. We will never
                     ask you for card details by phone or by message.
pay.currency         Every price on this page is in Armenian drams (AMD, ֏). Any
                     figure shown in dollars or euros is an approximate
                     conversion for orientation only — the amount charged is in
                     AMD.
```

Then the guarantees block (§6.1 Block 5), the service-limitations summary
(§6.6.2), and the consultation form.

---

### 6.4 How it works — `/en/how-it-works/`

```
how.h1               How it works
how.sub              From the first conversation to the report that lands on
                     your phone.

how.step1.h          A conversation
how.step1.body       You tell us which cemetery, roughly where the plot is, and
                     who is in the family. We tell you what the visits would
                     involve and what it would cost. Nothing is signed on this
                     call. We reply within one business day, Yerevan time
                     (UTC+4).

how.step2.h          We find the plot and record it
how.step2.body       On the first visit the crew locates the plot and records
                     its GPS point, and then does the full work — so every later
                     report can be compared with the first. The condition of the
                     stone and the planting is written down as we found it.

how.step3.h          The schedule
how.step3.body       Your subscription runs for twelve months from the day you
                     sign it. Optimal is four full visits, one in each season of
                     those twelve months. Maximum is six across the year. We
                     agree the approximate weeks with you and confirm each date
                     in the portal. If the weather never allows a winter visit,
                     that visit is added to spring. You receive four full visits
                     whatever the winter does.

how.step4.h          The visit
how.step4.body       The whole plot and every monument. Steam, pressure washer,
                     vacuum extraction, and chemistry chosen for the stone:
                     granite, basalt and tuff are not treated the same way.
                     Planting is tidied, rubbish is taken away, paths and kerbs
                     are cleaned.

how.step5.h          The report
how.step5.body       The report is in your portal within 48 hours of the visit:
                     photographs on arrival and after the work, video, the GPS
                     point, the date and the crew. You can send it by a plain
                     link to anyone in the family — they do not need an account
                     and they will not be asked to buy anything.

how.step6.h          If something is wrong
how.step6.body       Tell us within seven days and we come back and redo the
                     work at our cost. That is written into our Terms of
                     Service, not offered as a favour.

how.included.h       What a full visit includes
how.included.1       Cleaning of the monument and the base
how.included.2       Cleaning of kerbs, paths and the plot surface
how.included.3       Tidying existing planting
how.included.4       Removing rubbish, leaves and old flowers
how.included.5       Washing down after the work
how.included.6       Photographs on arrival and after the work
how.included.7       Video of the whole plot
how.included.8       GPS point recorded at the plot

how.notincluded.h    What a visit does not include
how.notincluded.1    Restoration or repair of stone
how.notincluded.2    Re-cutting or regilding of lettering
how.notincluded.3    New planting and flowers
how.notincluded.4    Anything needing cemetery administration approval
how.notincluded.link See the full list of what we cannot do

how.cta              Request a consultation
```

---

### 6.5 Sample report — `/en/sample-report/`

```
sample.h1            A sample report
sample.intro.body    This is what arrives after every visit. The report is in
                     your portal within 48 hours of the visit. Nothing here is
                     decorative — each part exists so that you can check the
                     work.

sample.1.h           The header
sample.1.body        Date, cemetery, sector and plot. The first thing you see is
                     a plain confirmation that the visit happened.
sample.2.h           The GPS point
sample.2.body        The coordinates recorded by the crew's device at the plot.
                     It is how you know the crew was at your plot and not at a
                     convenient one nearby.
sample.3.h           What was done
sample.3.body        The work carried out on this visit, item by item.
sample.4.h           Photographs
sample.4.body        The condition on arrival, then the condition after the
                     work, in the same frames, full resolution. You can open any
                     of them and look closely.
sample.5.h           Video
sample.5.body        A short walk around the plot, so that you see it as a whole
                     and not only in the frames we chose.
sample.6.h           The crew's note
sample.6.body        What was done, what we noticed, and anything we think you
                     should know — a cracked kerb, a leaning stone, a tree
                     pressing on the plot.
sample.7.h           What we would recommend
sample.7.body        If we think work is needed beyond the subscription, it is
                     listed with a price at the end, after the report, never
                     alongside the photographs. Nothing happens unless you ask
                     for it.
sample.8.h           The link you send to the family
sample.8.body        Every report has a link you can send by WhatsApp or Viber.
                     It opens without an account and shows the report and
                     nothing else — no prices, no offers, no sign-up.

sample.preview.h     What the link looks like when you send it
sample.preview.body  The preview carries our mark, the words "Visit report" and
                     the date. It never carries a photograph, the cemetery or
                     the plot, because a link forwarded into a group chat is
                     seen by people you did not choose to tell.

sample.name.h        The name on the monument
sample.name.body     A report shows the cemetery, the sector and the plot. The
                     name is not shown unless you switch it on, and you can
                     switch it off again at any time — including on links you
                     have already sent.

sample.placeholder   PHOTO · full report mock, arrival frame · 3:2 · 1600×1067 ·
                     replace after 09.2026 shoot
sample.cta           Request a consultation
```

---

### 6.6 Family Circle — `/en/family-circle/`

```
family.h1            Family Circle
family.sub           A grave belongs to a family, not to one inbox.
family.body          One person usually pays and one person usually chases.
                     Everyone else finds out second-hand. Family Circle is our
                     answer to that: you invite the people who should see the
                     reports, and each of them gets their own access. They do
                     not need to be in Armenia and they do not need to pay
                     anything.

family.roles.h2      Who can do what
role.owner           Owner
role.owner.long      The person who pays. Sees every report. Changes or cancels
                     the subscription. Orders extra work. Invites and removes
                     people. There is one Owner, and ownership can be
                     transferred.
role.manager         Family manager
role.manager.long    Sees every report and the schedule. Can request extra work,
                     which the Owner approves. Can invite family members. Cannot
                     cancel the subscription, cannot change payment details and
                     cannot approve a charge.
role.member          Family member
role.member.long     Sees every report and every photograph, and can ask for a
                     repeat visit under the guarantee. Sees no prices, no
                     invoices and no renewal dates. This is the right role for
                     most relatives.
role.guest           Guest
role.guest.long      Someone who opened a link you sent. Sees that one report
                     and nothing else. No prices, no account, no request to sign
                     up.

family.local.h2      Someone in Yerevan who will meet the crew
family.local.body    If a relative in Yerevan would like to be there, tell us
                     who and we will let them know the day before a visit. They
                     receive the reminder and the reports as plain links. They
                     never receive a price, an invoice or a renewal message, and
                     we ask for their agreement before we write to them.

family.privacy.h2    What the family sees, and what they do not
family.privacy.body  Everyone you invite sees the reports for this plot. Only
                     the Owner sees money. The name on the monument appears in
                     a report only if you switch it on.

family.cta           Request a consultation
```

---

### 6.7 About — `/en/about/`

```
about.h1             About MemoryCare
about.who.h          Who we are
about.who.body       MemoryCare LLC is a company registered in Yerevan, Armenia.
                     We look after family graves in Yerevan cemeteries for
                     families who cannot get there themselves, and for families
                     who do not have the time to do the work properly.
about.what.h         What we do
about.what.body      Scheduled cleaning of graves and monuments, using steam,
                     pressure washing, vacuum extraction and chemistry chosen
                     for the particular stone. After every visit we produce a
                     report with photographs, video and the GPS point of the
                     plot, delivered through a client portal that the whole
                     family can be given access to.
about.now.h          Where we are in 2026
about.now.body       We are at the beginning. The company was founded in 2026
                     and we are taking on our first clients now. We are saying
                     that plainly rather than implying a history we do not have.
                     What we can put in front of you is our method, our prices,
                     our guarantees and, once we have worked for you, your own
                     reports.
about.who2.h         Who to speak to
about.who2.body      Davit Hambardzumyan, Chief Executive Officer —
                     +374 55 315 323
                     Hayk Manukyan, Chief Business Development Officer —
                     +374 93 154 108
                     info@memorycare.am
                     Both numbers take WhatsApp and Viber.
about.details.h      Company details
about.details.body   MemoryCare LLC
                     Registered address: {LEGAL_ADDRESS}          [OPEN]
                     Company registration number: {REG_NUMBER}    [OPEN]
                     Registered in the Republic of Armenia.
```

No mission, no values, no history, no news. Those are what the current site gets
wrong; do not rebuild them.

---

### 6.8 Contacts — `/en/contacts/`

```
contacts.h1          Contacts
contacts.sub         A person answers these numbers. If you are calling from
                     another time zone, leave a message and we will call back at
                     a time that suits you.
contacts.hayk        Hayk Manukyan — Chief Business Development Officer
                     +374 93 154 108 · WhatsApp, Viber
                     Services, prices and starting a subscription.
contacts.davit       Davit Hambardzumyan — Chief Executive Officer
                     +374 55 315 323 · WhatsApp, Viber
                     Anything you would rather raise with the head of the
                     company, including a complaint.
contacts.email       info@memorycare.am — written enquiries, invoices, documents.
contacts.office.h    Office
contacts.office      {LEGAL_ADDRESS}, Yerevan, Armenia       [OPEN]
contacts.hours.h     Working hours
contacts.hours       {WORKING_HOURS}                          [OPEN]
contacts.hours.line  We reply within one business day, Yerevan time (UTC+4).
contacts.map.ph      MAP · office location · placeholder pending the registered
                     address
```

Then the consultation form.

---

### 6.9 Legal pages — framing, plain-language summaries, structure

A lawyer supplies the clauses. Every page carries the same top matter, and every
section opens with one sentence of plain English in normal type before the
clause. Older readers in a second or third language read that sentence and
nothing else, so it must be true on its own.

```
legal.updated        Last updated: {DATE}
legal.entity         This document applies to MemoryCare LLC, Yerevan, Armenia.
legal.help           If anything here is unclear, write to info@memorycare.am
                     and we will explain it in plain language before you commit
                     to anything.
```

#### 6.9.1 Privacy Policy — `/en/legal/privacy/`

```
privacy.h1           Privacy Policy
privacy.intro        What we record about you and your family's plot, why, and
                     what you can ask us to delete.
privacy.s1           Who is responsible for your data — MemoryCare LLC, and how
                     to reach the person responsible.
privacy.s2           What we collect — name, contact details, cemetery and plot
                     details, payment records, portal activity.
privacy.s3.plain     The photographs and video we take at the plot, and the GPS
                     point of the plot, are treated as your family's data. We do
                     not publish them, sell them, or use them in our marketing
                     without asking you first, in writing, for that specific
                     image.
privacy.s4           Why we hold it — performing the service, invoicing, legal
                     duties.
privacy.s5           Who else sees it — the people you invite, our crew, our
                     bank and our payment provider. Nobody else.
privacy.s6.plain     A report shows the cemetery, the sector and the plot. The
                     name on the monument is shown only if the Owner switches it
                     on, and switching it off removes it from links already sent.
privacy.s7           Anyone you invite to Family Circle — what they see and what
                     they do not.
privacy.s8           A person in Yerevan whom you nominate to be told about a
                     visit — what we send them, and the agreement we ask for
                     first.
privacy.s9           How long we keep it, including after a subscription ends.
privacy.s10          Your rights — access, correction, deletion, a copy of your
                     reports.
privacy.s11          Cookies and measurement. Plain sentence: "We do not use
                     third-party analytics or advertising cookies on this site."
privacy.s12          International transfer — our clients are in the USA,
                     France, Russia and elsewhere.
privacy.s13          How to complain.
```

#### 6.9.2 Refund Policy — `/en/legal/refund/`

```
refund.h1            Refund Policy
refund.intro         When you get money back, how much, and how quickly.
refund.plain         You can cancel an annual subscription at any time. We
                     refund the visits you have paid for and not received, in
                     proportion, worked out on the amount you actually paid. You
                     do not need to phone us — it can be done in the portal.
                     Money is returned by the route it arrived.

refund.formula.h     How the amount is calculated
refund.formula       refund = amount you paid × (visits not performed ÷ visits
                     in the plan), rounded up to the nearest 100 ֏ AMD.
refund.example1.h    Example — no credit was applied
refund.example1      You paid 160,000 ֏ AMD for Optimal, four visits. One visit
                     has taken place. 160,000 × 3/4 = 120,000 ֏ AMD is returned.
refund.example2.h    Example — an Express visit was credited
refund.example2      You paid 65,000 ֏ AMD for an Express visit, then signed
                     Optimal within 60 days and paid 95,000 ֏ AMD for the first
                     year. One of the four visits has taken place.
                     95,000 × 3/4 = 71,250, rounded up to 71,300 ֏ AMD.
refund.basis         The basis is visits, not days: you can count the visits
                     yourself. Work already performed has already been paid for.
refund.cap           There is no cap on the refund.

refund.s1            Cancelling an annual subscription — the calculation above,
                     with both worked examples.
refund.s2            One-off services — Inspection and Express, before and after
                     the visit.
refund.s3            A visit we could not complete — what happens if the crew
                     could not reach the plot, or the cemetery was closed.
refund.s4            The seven-day repeat visit — a repeat visit, not a refund,
                     and why.
refund.s5            How long a refund takes and by what route.
refund.s6            Bank transfer refunds and international payments.
refund.s7            How to ask for a refund and who answers.
refund.s8.plain      Cancelling does not delete your reports. They stay readable
                     in the portal, and the links you have already sent to your
                     family go on working.
```

#### 6.9.3 Terms of Service — `/en/legal/terms/`

```
terms.h1             Terms of Service
terms.intro          What we undertake to do, what we need from you, and what
                     happens when something goes wrong.
terms.s1             Who these terms are between.
terms.s2             What is included in each product — Inspection, Express,
                     Optimal, Maximum, Special — with the 16 m² and 2 monument
                     limit stated.
terms.s3             Surcharges above those limits.
terms.s4.plain       A subscription runs for twelve months from the day it is
                     signed. Optimal provides one full visit in each season of
                     those twelve months. If the weather never allows a winter
                     visit, that visit is added to spring; four full visits are
                     provided whatever the winter does.
terms.s5             Scheduling, and what happens when a visit has to move.
terms.s6             The credit for a one-off service: 60 days, one amount, the
                     larger of the two, applied at signature, one credit for each
                     plot.
terms.s7             Your obligations — accurate plot details, and the right to
                     authorise work on that plot.
terms.s8             Reports — what a report contains, when it is delivered, and
                     how long it stays available.
terms.s9             Family Circle — invitations, roles, and what an invited
                     person may do on your behalf.
terms.s10.plain      These guarantees are obligations, not goodwill. They apply
                     whether or not you ask nicely.
terms.s11.plain      Every amount is in Armenian drams (AMD, ֏). Any figure
                     shown in another currency is an approximation for your
                     convenience.
terms.s12.plain      We do not charge a card automatically when a subscription
                     year ends. We write to you 30 days before your renewal date
                     and you decide.
terms.s13            Transfer of ownership of a subscription.
terms.s14            Suspension and termination, by either side.
terms.s15            Liability and its limits.
terms.s16            Governing law and disputes.
terms.s17            Changes to these terms and how we notify you.
```

#### 6.9.4 What we cannot do — `/en/legal/limitations/`

```
limits.h1            What we cannot do
limits.intro         Some things are outside the service, and some things are
                     outside anyone's control. It is better that you know them
                     now than discover them in a report.
limits.1.h           What is not included in a subscription
limits.1             Restoration of stone, re-cutting or regilding of lettering,
                     repairs to kerbs and foundations, replacing a monument, and
                     any work requiring cemetery administration approval. We can
                     price these separately.
limits.2.h           Damage that was there before we arrived
limits.2             Cracks, subsidence, weathering and old repairs are recorded
                     in the report and not concealed. We are not responsible for
                     them and we will not clean over them and call it done.
limits.3.h           Stone we will not treat aggressively
limits.3             Some surfaces — soft, flaking or previously coated stone —
                     can be harmed by pressure or by chemistry. Where that is the
                     case we clean gently, say so in the report, and explain what
                     we chose not to do.
limits.4.h           Weather and season
limits.4             Frozen ground, heavy rain and snow can make a visit
                     pointless or unsafe. We move the visit and tell you the same
                     day, with a new date. The visit is not lost, and a winter
                     visit that never became possible is added to spring.
limits.5.h           Access
limits.5             Cemetery closures, funerals in progress, construction,
                     blocked paths, or a plot that has been enclosed since we
                     last came. We photograph the obstruction, tell you, and
                     return. That visit does not come out of your subscription.
limits.6.h           Locating a plot
limits.6             If you cannot tell us where the plot is, we search — but on
                     some older cemeteries the records are incomplete and we may
                     not find it. If we do not find it we tell you what we did
                     and refund the Inspection.
limits.7.h           Planting and flowers
limits.7             We tidy and maintain existing planting. New planting and
                     flowers are ordered separately.
limits.8.h           What we will not do
limits.8             We do not carry out religious rites, and we do not act for
                     one family member against another. If there is a
                     disagreement inside a family about a plot, we pause and wait
                     for it to be settled.
```

A three-line summary of §6.9.4 appears on the pricing page with a link to the
full page. A reader who discovers the limits after paying is a refund.

---

### 6.10 404 and 500

```
error.404.h          This page does not exist
error.404.body       The link may be old or mistyped. These are the pages people
                     usually want.
error.404.links      How it works · Pricing · Sample report · Family Circle ·
                     Contacts
error.404.phone      If you were looking for something else, call Hayk on
                     +374 93 154 108.

error.500.h          Something on our side is not working
error.500.body       This is our fault, not yours, and nothing of yours has been
                     lost. Please try again in a few minutes.
error.500.phone      If you need something now, call Hayk on +374 93 154 108.
```

No joke, no illustration, no emoji, no error colour.

---

## 7. Meta titles and descriptions — every page

In English, "memory care" is semantically owned by the dementia-care industry.
**Every title pairs the brand with grave, cemetery or memorial plot care within
the first few words, and every description says what we are not.** Titles ≤60,
descriptions ≤155, all counted and all fitting.

| Route | Key | Title | ch |
|---|---|---|---|
| `/en/` | `meta.home.title` | MemoryCare — grave care in Yerevan cemeteries | 45 |
| `/en/pricing/` | `meta.pricing.title` | Grave care prices in Yerevan \| MemoryCare | 41 |
| `/en/how-it-works/` | `meta.how.title` | How MemoryCare works — grave care in Yerevan | 44 |
| `/en/sample-report/` | `meta.sample.title` | A sample visit report \| MemoryCare, Yerevan | 43 |
| `/en/family-circle/` | `meta.family.title` | Family Circle — shared grave care reports | 41 |
| `/en/guarantees/` | `meta.guarantees.title` | Our guarantees \| MemoryCare grave care, Yerevan | 47 |
| `/en/about/` | `meta.about.title` | About MemoryCare — grave care company, Yerevan | 46 |
| `/en/contacts/` | `meta.contacts.title` | Contact MemoryCare — grave care in Yerevan | 42 |
| `/en/consultation/` | `meta.consult.title` | Request a consultation \| MemoryCare, Yerevan | 44 |
| `/en/legal/privacy/` | `meta.privacy.title` | Privacy Policy \| MemoryCare grave care, Yerevan | 47 |
| `/en/legal/refund/` | `meta.refund.title` | Refund Policy \| MemoryCare grave care, Yerevan | 46 |
| `/en/legal/terms/` | `meta.terms.title` | Terms of Service \| MemoryCare, Yerevan | 38 |
| `/en/legal/limitations/` | `meta.limits.title` | What we cannot do \| MemoryCare grave care | 41 |
| `/r/:shareToken/` | `meta.report.title` | Visit report — {date} | 32 |

Descriptions:

```
meta.home.desc         (138 ch)
Care for family graves in Yerevan cemeteries on a yearly schedule, with photo,
video and GPS reports after every visit. Not dementia care.

meta.pricing.desc      (153 ch)
What memorial plot care costs in Yerevan: an inspection at 20,000 AMD, annual
subscriptions of four or six full visits. Cemetery care, not dementia care.

meta.how.desc          (150 ch)
How care for a family grave in a Yerevan cemetery works: the first visit, the
seasonal schedule, the cleaning method, and the report after each visit.

meta.sample.desc       (155 ch)
See what a MemoryCare report for a Yerevan cemetery plot contains: photographs,
video, GPS confirmation and the crew's note. Grave care, not dementia care.

meta.family.desc       (146 ch)
Invite relatives anywhere to see every visit report for your family's grave in a
Yerevan cemetery. Separate accounts and roles. Not dementia care.

meta.guarantees.desc   (142 ch)
The three written MemoryCare guarantees for grave care in Yerevan: a free repeat
visit in seven days, liability for damage, a pro-rata refund.

meta.about.desc        (149 ch)
MemoryCare LLC is a Yerevan company caring for family graves in Armenian
cemeteries, with photo, video and GPS reports. Not a dementia care provider.

meta.contacts.desc     (137 ch)
Phone, WhatsApp and email for MemoryCare, a Yerevan company caring for family
graves in Armenian cemeteries. Not a dementia care service.

meta.consult.desc      (145 ch)
Ask for a free consultation about care for a family grave in a Yerevan cemetery.
We reply within one business day. Grave care, not dementia care.

meta.privacy.desc      (144 ch)
How MemoryCare LLC handles your data and the photographs, video and GPS records
of your family's grave in a Yerevan cemetery. Not dementia care.

meta.refund.desc       (145 ch)
How to cancel a MemoryCare grave care subscription in Yerevan and how the
pro-rata refund in AMD is calculated. Cemetery care, not dementia care.

meta.terms.desc        (152 ch)
The terms between MemoryCare LLC and clients whose family graves in Yerevan
cemeteries we care for, including the written guarantees. Not dementia care.

meta.limits.desc       (149 ch)
What is not included in MemoryCare grave care in Yerevan: restoration, damage
that was there before, weather, access, older plots. Not dementia care.
```

**Report route:** `noindex, nofollow` on `/r/:shareToken/` and on every portal
route. The report page `<title>` is `Visit report — {date}` and nothing else —
a plot identity in a browser tab is visible over a shoulder and in any screen
share. There is no meta description on those routes.

**Search phrasing note for whoever writes ads and content later:** never bid on
or optimise for the bare brand phrase. Use compound queries — "grave care
Yerevan", "cemetery plot care Armenia", "MemoryCare grave care" — because the
bare phrase returns dementia care.

---

## 8. Forms — labels, placeholders, helpers, validation, consent

Rules for every form in the product:
- Validate on blur, never on keystroke; re-validate on keystroke only once a
  field is already in error.
- The message sits below the field. Colour is never the only signal: the glyph
  and the sentence carry it.
- Never disable the submit button before submission.
- On failure, focus moves to the first field in error and a summary appears at
  the top of the form with `role="alert"`.
- Field values are never lost on a failed submit.
- Every validation message begins with "Please", names the field in real-world
  words, and never says invalid, required, failed or error.

### 8.1 Consultation request — the primary conversion, six placements, one component

```
form.consult.heading      Request a free consultation
form.consult.intro        Tell us where the plot is and how to reach you. We
                          reply within one business day, Yerevan time (UTC+4).

form.consult.name.label   Your name
form.consult.name.err     Please enter your name.

form.consult.contact.label   Phone or email
form.consult.contact.helper  Any country. For a phone number include the country
                             code, for example +374, +1 or +33.
form.consult.contact.err.empty   Please give us one way to reach you.
form.consult.contact.err.format  This does not look like a phone number or an
                                 email address.
form.consult.contact.err.format2 Please check it and try again.
form.consult.contact.err.country Please include the country code, for example
                                 +374, +1 or +33.
form.consult.whatsapp.label      This number is on WhatsApp
                                 (checked by default for non-+374 numbers)

form.consult.place.label   Cemetery or city
form.consult.place.helper  If you are not sure of the cemetery name, the district
                           or the city is enough. "Not sure" is a valid answer.
form.consult.place.err     Please tell us roughly where the plot is.

form.consult.disclosure    Add a note or a family contact
form.consult.optional.label       Anything we should know (optional)
form.consult.optional.placeholder For example: the best hours to call you, or who
                                  else in the family we should speak to.
form.consult.local.name.label     Name of a relative in Yerevan (optional)
form.consult.local.phone.label    Their phone (optional)
form.consult.local.helper         Only if someone in Yerevan would like to meet
                                  the crew. We ask their agreement before we
                                  write to them.

form.consult.consent       I agree to MemoryCare contacting me about this
                           request.
form.consult.consent.link  Privacy Policy
form.consult.consent.err   Please confirm we may contact you.

form.consult.submit        Request a consultation
form.consult.submitting    Sending…
```

Success — replaces the form in place, never navigates away:

```
form.consult.success.h      Thank you. Your request has reached us.
form.consult.success.body   We reply within one business day, Yerevan time
                            (UTC+4). Hayk will write to you on WhatsApp from
                            +374 93 154 108 first, and call only if you prefer.
form.consult.success.calc   You configured: {area} m², {monuments} monuments,
                            {tier} — {price} ֏ AMD a year. The person who calls
                            you will be looking at the same figures.
form.consult.success.cta    See a sample report
form.consult.success.alt    If you would rather not wait, write to us on WhatsApp
                            at +374 93 154 108.
```

Failure:

```
form.consult.fail.h     We could not send your request
form.consult.fail.body  The message did not reach us and nothing you typed has
                        been lost. Please try again. If it fails a second time,
                        write to info@memorycare.am or on WhatsApp at
                        +374 93 154 108 and we will take it from there.
form.consult.fail.cta   Try again
```

### 8.2 Other forms — deltas only

```
form.contact.*        name, phone or email, message (10 characters minimum),
                      consent. Same strings as §8.1 where they repeat.
form.invite.*         §9.7
form.revisit.*        §10.4.3
form.guest.*          §9.6.3
form.cancel.*         §9.9
form.profile.*        §9.10
```

### 8.3 The complete validation set

Every message ≤90 characters; all fit.

```
val.name              Please enter your name.                               (23)
val.contact           Please give us one way to reach you.                  (36)
val.contactFormat     This does not look like a phone number or an email
                      address.                                              (59)
val.contactFormat2    Please check it and try again.                        (30)
val.country           Please include the country code, for example +374,
                      +1 or +33.                                            (61)
val.place             Please tell us roughly where the plot is.             (41)
val.consent           Please confirm we may contact you.                    (34)
val.email             Please enter their email address.                     (33)
val.emailFormat       This does not look like an email address.             (41)
val.duplicate         {email} already has access to this plot.              (40)
val.password          Please use at least 10 characters.                    (34)
val.message           Please tell us what is wrong, in a sentence or two.   (51)
val.fileSize          That photograph is larger than 10 MB. Please send a
                      smaller one.                                          (64)
val.fileType          We can accept JPG, PNG and HEIC photographs.          (44)
val.memberLimit       You have reached the limit of {n} people on this plot.
                      Remove someone, or call us and we will raise it.
val.inviteExpired     This invitation has expired. Ask {owner_name} to send it
                      again.
val.resetExpired      This password link has expired. Reset links last one hour —
                      ask for a new one.
val.sessionExpired    You have been signed out for safety. Sign in again —
                      nothing has been lost.
val.calcCeiling       The calculator goes up to 100 m². For a larger plot we
                      price the work after an Inspection.
```

`val.calcCeiling` is **neutral, never in the error colour**: passing 100 m² is a
normal outcome and a route to Inspection, not a mistake.

### 8.4 Where the error colour is allowed, in words

Two places only, and the copy differs accordingly.

1. **Form validation.** The message is short, begins with "Please", and names
   what to do. The colour appears on the field border, the glyph and the message
   text. Never as a panel fill.
2. **Payment failure** (§10.5). The colour appears on the heading rule and the
   glyph. Never a panel fill, never a button fill, never a modal.

Everything else is neutral, expressed in words and a glyph: a postponed visit, a
blocked plot, a report that will not load, an expired link, an expired
invitation, a repeat-visit request, a cancellation, a session timeout, the
calculator ceiling, 404 and 500. **On any screen showing a photograph of a
grave, the error component renders with no colour at all** — the failure there
is ours, not the reader's, and it is a sentence, not a validation.

---

## 9. The client portal — every screen

Routes: `/portal/…`; the guest report is `/r/:shareToken/`.

### 9.1 Sign in, activation, password

```
auth.signin.h         Sign in
auth.signin.sub       Your reports and your family's plot.
auth.email.label      Email
auth.password.label   Password
auth.forgot.link      I have forgotten my password
auth.signin.cta       Sign in
auth.magic.link       Send me a link instead
auth.magic.sent       If there is an account for {email}, a link is on its way.
                      It works once and lasts one hour.
auth.magic.whatsapp   Send the link by WhatsApp instead
auth.guest.note       Have you been sent a report link? You do not need an
                      account — open the link and it will show you the report.
auth.help             If you cannot get in, call Hayk on +374 93 154 108.

auth.err.credentials  That email and password do not match
auth.err.credentials.body
                      Check them and try again, or ask for a new password.
auth.err.locked       Sign-in is paused for 15 minutes
auth.err.locked.body  There have been several attempts on this account. For
                      safety we have paused sign-in. If you need access sooner,
                      call +374 93 154 108.
auth.err.server       We cannot reach the portal at the moment
auth.err.server.body  This is on our side. Your reports are safe. Try again in a
                      few minutes.

auth.activate.h       Set up your access
auth.activate.body    Your subscription is paid and your plot is registered.
                      Choose a password and the portal is yours.
auth.reset.h          Choose a password
auth.reset.helper     At least 10 characters. A short phrase you will remember
                      is better than a complicated word.
auth.reset.sent       If there is an account for {email}, a reset link is on its
                      way. It is valid for one hour.
auth.reset.done       Your password is changed. You can sign in now.
```

### 9.2 First-entry screen — after payment, before any visit

The moment of maximum doubt. No upsell of any kind on this screen.

```
portal.first.h        Welcome, {first_name}. Everything is set up.
portal.first.body     Your subscription is active and your plot is registered
                      with us. On the first visit the crew locates the plot and
                      records its GPS point, and then does the full work — so
                      every later report can be compared with the first.

portal.first.card.plot         Plot            {cemetery} · {sector} · {plot}
portal.first.card.plan         Subscription    {tier} · {visits_total} full
                                               visits in the year
portal.first.card.paid         Paid            {amount} ֏ AMD on {date}
portal.first.card.year         Your year       {start_date} to {end_date}
portal.first.card.firstVisit   First visit     {date_or_status}
portal.first.card.unscheduled  Being scheduled — we confirm the date here and by
                               email, and we tell you before the crew goes.

progress.1            Payment received
progress.2            Date confirmed
progress.3            Crew visits
progress.4            Report ready

portal.first.next.h   What happens next
portal.first.next.1   We confirm the date of the first visit.
portal.first.next.2   The crew goes, records the plot and does the work.
portal.first.next.3   The report is in your portal within 48 hours of the visit.

portal.first.do.h     Meanwhile
portal.first.do.1     See a sample report — so you know what to expect
portal.first.do.2     Invite your family — they see every report from the first
                      one
portal.first.do.3     Add a note — anything we should know about the plot

portal.first.support  Nothing needs doing from you now. If you have a question,
                      Hayk answers on +374 93 154 108.
```

### 9.3 Dashboard and plots

```
portal.nav.visits     Visits
portal.nav.family     Family Circle
portal.nav.billing    Subscription
portal.nav.profile    Your details

plot.card.next        Next visit {date}
plot.card.nextUnknown Next visit being scheduled
plot.card.lastReport  Last report {date}
plot.switcher.label   Choose a plot
plot.empty.h          No plots yet
plot.empty.body       As soon as a subscription is active, the plot appears here
                      with its visits.
```

### 9.4 Visits list

```
visits.h1             Visits
visits.filter.all     All
visits.filter.done    Completed
visits.filter.sched   Scheduled
visits.filter.moved   Moved

visits.row.completed  {date} · {cemetery} · {plot}
                      Report ready
                      Open the report
visits.row.scheduled  {date} · {cemetery} · {plot}
                      Scheduled
                      Remind me the day before
visits.row.moved      {original_date} → {new_date}
                      Visit moved — weather
                      Why this moved
visits.row.noaccess   {date} · {cemetery} · {plot}
                      Could not reach the plot
                      What happened
visits.row.revisit    {date} · repeat visit for {original_date}
                      Repeat visit requested

visits.year.note      Your subscription year runs {start_date} to {end_date}.
                      Optimal is one full visit in each season of that year.
visits.winter.note    If the weather never allows a winter visit, that visit is
                      added to spring. You receive four full visits whatever the
                      winter does.
visits.guarantees.link Our guarantees
```

### 9.5 Report screen — the canonical block order

The order below is binding. It is the round-two majority (01 final, 02, 05):
the human sentence sits after the images it comments on, and the GPS is its own
block, not a chip.

```
1  report.masthead        Visit report
                          {cemetery} · {sector} · {plot}
                          [name shown only if the plot setting is on]
2  report.confirmation.h  The visit took place
   report.confirmation    {weekday}, {date}
   rail.label.crew        Crew          {crew_names}
   rail.label.arrival     Arrived       {arrival_time}
   rail.label.departure   Left          {departure_time}
   status.completed       Completed
   report.gps.h           Recorded on site
   report.gps.value       {lat}, {lng}
   status.gps             GPS confirmed
   report.gps.helper      These coordinates were recorded by the crew's device at
                          the plot on {date}. It is how you know the crew was at
                          your plot.
   cta.showOnMap          Show on map
3  report.work.h          What was done
   report.work.item       {work_item}
   report.work.more       Show all {n}
4  report.photos.h        Photographs
   report.photos.g1       On arrival
   report.photos.g2       After the work
   report.photos.helper   Tap any photograph to open it full size.
   report.photos.compare  Compare
5  report.video.h         Video from the visit
   report.video.duration  {duration}
   report.video.none      No video was recorded on this visit.
6  report.crewNote.h      Notes from the crew
   report.crewNote        {note_text}                      (120–320 ch, wraps)
   report.crewNote.none   The crew recorded nothing beyond the work carried out.
7  report.recommend.h     Work we would recommend      [Owner and Family manager
                                                        only — removed
                                                        server-side for everyone
                                                        else]
   report.recommend.intro Nothing here happens unless you ask for it. These are
                          observations, not urgent, unless we say so.
   report.recommend.item  {work} — {price} ֏ AMD
   report.recommend.cta   Ask about this
8  report.docs.h          Documents
   report.docs.pdf        Download this report as a PDF
   report.docs.note       The PDF carries no prices, so it is safe to forward.
9  report.actions.h       Actions
   cta.copyLink           Copy link
   report.actions.share   Send this report to the family
   link.revisit           Something is not right with this visit
10 report.next.h          Next visit                    [never in the guest view]
   report.next.value      {date}
   report.next.unknown    Being scheduled
```

Sample crew note, as the register reference for operators (246 ch):

> The stone had a lot of green along the north side, which is normal after a wet
> spring. It came off with steam and no acid. The kerb on the left has an old
> crack — nothing new, and we have photographed it so you can see it against the
> next report.

### 9.6 The guest report — `/r/:shareToken/`

Roughly half of all opens. No prices, no upsell, no account prompt, no
navigation into the marketing site. Prices, the recommended-work figures, the
next-visit date and the subscription name are **removed server-side, not
hidden**.

```
guest.strip           Visit report · MemoryCare
guest.identity        {cemetery} · {sector} · {plot} · {date}
[blocks 2–6 and 8 of §9.5, identical]
guest.foot.1          This report was made by MemoryCare after a visit to the
                      plot on {date}. {owner_first_name} shared it with you.
guest.foot.2          MemoryCare cares for family graves in Yerevan cemeteries.
guest.foot.phone      Questions: +374 93 154 108
guest.foot.about      About MemoryCare            (text link, never a button)
```

#### 9.6.1 The one permitted action

```
link.guestFeedback    Something is not right with this report     (39 ch)
guest.fb.h            Tell us what is wrong
guest.fb.body         We will look at it and come back to you. You do not need
                      an account and nothing here costs anything.
guest.fb.name         Your name
guest.fb.contact      Phone or email
guest.fb.message      What is wrong?
guest.fb.cta          Send the request
guest.fb.sent.h       We have your message
guest.fb.sent.body    Someone will come back to you within one business day, and
                      we have told {owner_first_name} as well.
```

#### 9.6.2 Guest-view states

```
guest.expired.h       This link is no longer active
guest.expired.body    The person who sent it can share it again. Nothing has been
                      deleted — the report still exists.
guest.preparing.h     The visit took place on {date}
guest.preparing.body  The photographs and video are still being prepared.
                      {owner_first_name} will be able to send you the link again
                      when they are ready.
```

No sign-up prompt, no account prompt, no price on either state.

#### 9.6.3 The share sheet

```
share.h               Send this report
share.field.label     Link to this report
cta.copyLink          Copy link
share.copied          Link copied.
share.whatsapp        Send on WhatsApp
share.viber           Send on Viber
share.email           Send by email
share.helper          Anyone with this link can see this report. They will not
                      see prices and will not be asked to sign up.
share.name.note       The name on the monument is {on_or_off} for this plot.
                      Change it in the plot settings.
share.status          Link is active · shared {date}
share.revoke          Stop this link working
share.revoke.confirm.h  Stop this link working?
share.revoke.confirm    Anyone you have already sent it to will no longer be able
                        to open the report. You can share it again at any time.
share.revoked           The link has been stopped.
```

### 9.7 Family Circle in the portal

```
family.portal.h1      Family Circle
family.portal.sub     The people who can see the reports for
                      {cemetery} · {sector} · {plot}.
family.row            {name} · {email} · {role}
family.row.change     Change role
family.row.remove     Remove

family.empty.h        No one else has access yet
family.empty.body     Invite a relative and they will see every report, from the
                      first one. There is nothing for them to pay and no
                      subscription of their own.
family.empty.cta      Invite someone

family.invite.h       Invite someone
family.invite.name    Their name
family.invite.email   Their email
family.invite.role.h  What they can do
family.invite.role.member  Family member — sees every report and every
                           photograph. Cannot order paid work. Right for most
                           relatives.
family.invite.role.manager Family manager — sees every report and can request
                           extra work. Cannot spend or cancel.
family.invite.roles.link   What each role can do
family.invite.cta     Send the invitation
family.invite.helper  They get an email with a link. The invitation is valid for
                      14 days.
family.invite.sent    The invitation is on its way to {email}.
family.invite.pending Invited {date} — not accepted yet.
family.invite.again   Send again
family.invite.cancel  Cancel the invitation

family.remove.h       Remove {name} from the family circle?
family.remove.body    They will no longer be able to open reports for this plot.
                      Reports you have already sent them by link will still open.
                      You can invite them again at any time.
family.remove.confirm Remove {name}
family.remove.cancel  Keep their access

family.role.up.h      Let {name} request extra work?
family.role.up.body   A family manager can request extra work on this plot; you
                      approve anything that costs money. They still cannot cancel
                      the subscription or change payment details.
family.role.up.cta    Make {name} a family manager
```

**A standing content rule for the whole product:** no renewal, price, payment or
upgrade string may ever be addressed to a Family member, a Guest or a local
contact. Only the Owner sees money.

### 9.8 Subscription and payments

```
billing.h1            Subscription and payments
billing.card.plan     {tier} · {visits_total} full visits in the year
billing.card.price    {amount} ֏ AMD a year
billing.card.plot     {cemetery} · {sector} · {plot} · {area} m² ·
                      {monuments} monuments
billing.card.year     Your year: {start_date} to {end_date}
billing.card.renewal  We write to you about renewal on {notice_date}. Nothing is
                      charged automatically.
billing.card.paid     Paid {amount} ֏ AMD on {date}
billing.credit.note   The {amount} ֏ AMD you paid for your Express visit was
                      credited to this subscription.

billing.history.row   {date} · {amount} ֏ AMD · {method} · Invoice
billing.history.empty You have no payments recorded yet.

billing.change.h      Change your subscription
billing.change.body   Moving between Optimal and Maximum changes the number of
                      visits in your year. We work out what you have paid and
                      tell you the difference before anything is charged.
billing.change.cta    Talk about changing
link.cancel           Cancel my subscription
link.transferOwner    Transfer ownership of this plot
```

The renewal figure is visible from day one, so the price in year two is never a
surprise: `billing.card.price` shows 160,000 ֏ AMD even in a year that was paid
at 95,000, with `billing.credit.note` explaining the difference.

### 9.9 Cancellation with the pro-rata refund — completable without a phone call

The arithmetic is shown, not the result alone, and the base is the amount
actually paid.

```
cancel.step1.h        Cancel your subscription
cancel.step1.body     You can cancel at any time. We return the visits you have
                      paid for and not received, worked out on what you actually
                      paid.
cancel.calc.paid      You paid                     {amount_paid} ֏ AMD
cancel.calc.visits    Visits in your plan          {visits_total}
cancel.calc.done      Visits completed             {visits_done}
cancel.calc.left      Visits not performed         {visits_left}
cancel.calc.formula   {amount_paid} × {visits_left}/{visits_total} =
                      {raw_refund} ֏ AMD
cancel.calc.rounding  Rounded up to the nearest 100 ֏ AMD
cancel.calc.refund    We return                    {refund} ֏ AMD
cancel.calc.helper    The refund goes back the way it came — to the account or
                      card you paid from. A transfer abroad usually takes one to
                      three working days.
cancel.step1.cta      Continue
cancel.step1.alt      Keep my subscription

cancel.step2.h        Before you go — is there anything we could have done?
cancel.step2.body     You do not have to answer. If something went wrong with a
                      visit or a report, we would rather fix it than lose you.
cancel.reason.1       The work was not what I expected
cancel.reason.2       The reports were not what I expected
cancel.reason.3       It is too expensive
cancel.reason.4       The plot no longer needs this
cancel.reason.5       Something in the family has changed
cancel.reason.6       Another reason
cancel.step2.free     Anything you want to tell us (optional)
cancel.step2.cta      Cancel my subscription
link.talkFirst        Actually, I would like to talk to someone first

cancel.revisit.offer  You are entitled to a free repeat visit within seven days
                      of a report. If that would settle it, ask for one —
                      cancelling stays available either way.
cancel.revisit.cta    Ask for a repeat visit
cancel.revisit.alt    Continue cancelling

cancel.step3.h        Your subscription is cancelled
cancel.step3.body     We have returned {refund} ֏ AMD to {method}. It usually
                      arrives within one to three working days.
cancel.step3.reports  Your reports stay in the portal and the links you have sent
                      to your family go on working. Nothing is deleted.
cancel.step3.back     If you want to come back, your plot and its GPS point stay
                      on record.
cancel.step3.cta      Back to my reports

cancel.calc.fail.h    We could not work out your refund automatically
cancel.calc.fail.body This is a fault on our side and it does not affect your
                      right to cancel or to the refund. Call Hayk on
                      +374 93 154 108 and we will do it with you.
```

After cancellation the portal is read-only for that plot: reports open, no new
visits, and **no upsell of any kind on those screens** — no "come back" banner,
no offer, no price.

### 9.10 Your details, notifications, plot settings

```
profile.h1            Your details
profile.name          Your name
profile.email         Email
profile.email.helper  Reports and invoices go here.
profile.phone         Phone
profile.phone.helper  Any country. Include the country code.
profile.lang          Preferred language
profile.tz            Time zone
profile.tz.helper     We use this so that we do not call you at four in the
                      morning.
cta.save              Save changes
profile.saved         Your details are saved.
profile.saveFail      We could not save your changes. Nothing has been lost —
                      please try again.

profile.notify.h      Notifications
profile.notify.1      Tell me when a report is ready                (on)
profile.notify.2      Remind me the day before a visit              (off)
profile.notify.3      Tell me before the subscription year ends     (on)
profile.notify.local  Send the reminder to someone else instead
profile.local.name    Their name
profile.local.contact Their phone
profile.local.channel How to reach them: WhatsApp · SMS
profile.local.helper  Useful if a relative in Yerevan will meet the crew. They
                      receive the reminder and the report links, never your
                      prices, invoices or renewal messages.
profile.local.consent This person has agreed to receive messages from us.
profile.local.consent.err  Please confirm they have agreed.

profile.plot.h        Plot settings
profile.plot.identity {cemetery} · {sector} · {plot}
profile.plot.name.h   The name on the monument
profile.plot.name.body  A report shows the cemetery, the sector and the plot. The
                        name is not shown unless you switch it on. Reports are
                        forwarded into family group chats and opened by people
                        without accounts, which is why it is off to begin with.
profile.plot.name.off   Do not show a name                     (default)
profile.plot.name.fam   Show the family name
profile.plot.name.full  Show the full name
profile.plot.name.note  Turning this off also removes the name from links you have
                        already sent.
profile.plot.notes.h    A note for the crew
profile.plot.notes.helper  Anything we should know about the plot — where it is
                           from the gate, a fragile stone, a neighbour who has
                           the key.
```

### 9.11 Ownership transfer

The flow most likely to be used at the worst moment in a family's year. The
register is administrative and calm. No condolence copy: we do not know why the
transfer is happening and guessing is worse than not asking.

```
transfer.link         Transfer ownership of this plot
transfer.helper       The Owner is the person who pays and who can change or
                      cancel the subscription. There is one Owner, and it can be
                      changed.

transfer.1.h          Transfer ownership of {cemetery} · {sector} · {plot}
transfer.1.body       The person you choose takes over the subscription: the
                      payments, the schedule, who is in the family circle, and
                      the right to cancel. You keep access to every report unless
                      they remove you.
transfer.1.field      Who should take over?
transfer.1.helper     Choose someone already in the family circle, or enter their
                      email and we will invite them.
transfer.1.note       Anything they should know (optional)
transfer.1.cta        Continue
transfer.1.alt        Keep ownership

transfer.2.h          What changes when {name} takes over
transfer.2.1          {name} becomes the Owner and can change or cancel the
                      subscription.
transfer.2.2          Invoices and payment requests go to {name}.
transfer.2.3          You become a family manager: you see every report and can
                      request extra work, but not change the subscription.
transfer.2.4          The plot, its GPS point and every past report stay exactly
                      as they are.
transfer.2.body       Nothing changes until {name} accepts. We ask them to
                      confirm by email, and we ask you to confirm as well.
transfer.2.cta        Send the request
transfer.2.alt        Go back

transfer.3.h          Waiting for {name} to accept
transfer.3.body       We have written to {email}. The request is open for 14
                      days. Until they accept, nothing has changed and you are
                      still the Owner.
transfer.3.cta        Send again
transfer.3.alt        Cancel the transfer

transfer.declined.h   {name} has not taken over the plot
transfer.declined     They declined the transfer. You are still the Owner and
                      nothing has changed. You can ask someone else, or leave it
                      as it is.

transfer.death.h      If the Owner of a subscription has died
transfer.death.body   Call us on +374 55 315 323 and we will move the
                      subscription to another member of the family. We will ask
                      for a document confirming the death and for proof of your
                      relationship, because we are not able to hand over a
                      family's records on a phone call alone. Care of the plot
                      does not stop while this is settled — the visits continue
                      on the schedule already paid for.
```

**[OWNER]** The last paragraph commits us to continuing service during a
transfer after a death. That is an operational promise as much as a copy
decision, and only the owners can make it.

---

## 10. Every state — empty, loading, error, success, and the bad news

### 10.1 Global state rules

- **Skeletons, not spinners**, for anything with a known shape. Spinners only
  for an action the user just started, and the loading affordance is never the
  brand mark.
- **Photographs never load into a black box.** The placeholder is a brand-colour
  fill with its caption, never grey and never black.
- **Every error names a next step and a human.** "Call Hayk — +374 93 154 108"
  is a valid recovery path and is often the right one for this audience.
- **No error is ever an apology longer than the facts.**
- Loading strings: `Loading your visits…` · `Loading this report…` ·
  `Sending…` · `Working out your refund…`. Nothing else.

### 10.2 Empty states

```
empty.visits.h        No visits yet
empty.visits.body     The first visit has not taken place. When it does, the
                      report will be here — photographs, video and the GPS
                      point. We will write to you the moment it is ready.
empty.visits.cta      See a sample report

empty.family.h        No one else has access yet
empty.family.body     Invite a relative and they will see every report, from the
                      first one. There is nothing for them to pay and no
                      subscription of their own.
empty.family.cta      Invite someone

empty.payments        You have no payments recorded yet.
empty.reports.h       No reports yet
empty.reports.body    A report appears here within 48 hours of each visit.
empty.search.h        Nothing matches that filter
empty.search.body     Change the filter, or choose All.
```

No empty state carries an illustration. The component has no illustration slot.

### 10.3 Loading and error, screen by screen

| Screen | Loading | Error heading | Error body | Action |
|---|---|---|---|---|
| Dashboard | one plot-card skeleton | `We cannot load your plots` | This is on our side. Your subscription is active and nothing has changed. | Try again · phone |
| Visits list | three row skeletons | `We cannot load your visits` | This is a problem on our side, not with your subscription or your reports. | Try again · phone |
| Report | skeleton in document order | `We cannot open this report` | The report exists and nothing has been lost. This is a fault on our side. | Try again · phone |
| Report media | image slots hold their ratio | `Some photographs are still uploading` | The rest of the report is complete. We will tell you when the photographs are there. | Tell me when they are ready |
| Family Circle | two row skeletons | `We cannot load your family circle` | This is on our side. Nobody's access has changed. | Try again |
| Billing | skeleton | `We cannot reach billing` | Nothing has changed on your subscription. | Try again · phone |
| Cancellation | skeleton on the amount only | `We could not work out your refund automatically` | This does not affect your right to cancel or to the refund. | Call Hayk |
| Guest report | skeleton | `This link is no longer active` | The person who sent it can share it again. Nothing has been deleted. | none — no account prompt |
| Marketing pages | text paints first, image slots hold their ratio | media failure shows the labelled placeholder; the page stays complete | — | — |

None of these uses the error colour: they are our failures on screens that
usually show a grave, and they are sentences, not validations.

### 10.4 Success states

```
success.consult       Thank you. Your request has reached us.       (§8.1)
success.invite        The invitation is on its way to {email}.
success.copied        Link copied.
success.saved         Your details are saved.
success.revisit.h     We have your request
success.revisit.body  Hayk will come back to you within one business day to agree
                      a date. The repeat visit is free and it does not use one of
                      the visits in your subscription.
success.payment.h     Payment received
success.payment.body  We have received {amount} ֏ AMD. Your subscription runs to
                      {end_date} and covers {visits_total} full visits.
success.cancel        Your subscription is cancelled                 (§9.9)
success.transfer.h    {plot} is now looked after by {new_owner_name}
```

Success carries no colour. It is a word, a glyph and a rule weight. There is no
success colour in this product and no token that could become one.

### 10.5 The bad-news states

These are designed screens with the same budget as a report — not toasts, not
alert bars, and never in the error colour.

#### 10.5.1 Visit postponed by weather

```
status.moved              Visit moved — weather
moved.h                   We are moving the visit to {plot}
moved.dates               Planned {old_date} → now {new_date}
moved.reason              {weather_reason}. Working in these conditions would not
                          clean the stone properly and it is not safe for the
                          crew.
moved.reassure            The visit is not lost. It stays part of your
                          subscription and the rest of your year does not change.
moved.winter              If the weather never allows a winter visit, that visit
                          is added to spring. You receive four full visits
                          whatever the winter does.
moved.unknownDate         We will confirm a new date by {commit_date}.
moved.cta                 Suggest a different date
moved.alt                 Call Hayk on +374 93 154 108
```

`{weather_reason}`, written by the operator from a fixed set, plainly:
`The ground is frozen` · `Heavy rain is forecast all day` ·
`Snow has covered the plot` · `The wind makes working on the stone unsafe`.
Never "adverse weather conditions", never "circumstances beyond our control".

**Rule: the new date must be present.** "Postponed, we will be in touch" is the
message that loses the client. If a new date is genuinely unknown, we commit to
a date by which we will confirm — never an open end.

#### 10.5.2 The crew could not reach the plot

The hardest screen in the product. The client is abroad and something at their
family's grave is wrong. Facts, proof, next step, a name. The GPS block stays:
it is what turns a failure into proof of effort.

```
status.noaccess           Could not reach the plot
noaccess.h                We went to {plot} on {date} and could not reach it
noaccess.confirmation     The crew arrived at {arrival_time} and recorded their
                          position at the cemetery. The coordinates are below.
noaccess.gps.helper       This is where the crew stood. It is how you know they
                          went.
noaccess.found.h          What we found
noaccess.found            {obstruction_description}
noaccess.photo.caption    The obstruction, photographed on {date}.
noaccess.next.h           What happens now
noaccess.next             We return on {return_date}. {action_taken}
noaccess.notCharged       This visit does not come out of your subscription. Your
                          subscription still covers all {visits_total} visits.
noaccess.human            If you would rather talk to someone, call Hayk on
                          +374 93 154 108 — he has the crew's account of it.
noaccess.cta              Suggest a different date
noaccess.alt              Call Hayk
```

`{obstruction_description}`, operator-written from a fixed set:
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

**Photograph rule:** the obstruction only — a locked gate, a blocked path,
materials. Never a photograph of a neighbouring grave, and no neighbouring
inscription in frame.

#### 10.5.3 The guarantee repeat visit

```
link.revisit              Something is not right with this visit
revisit.h                 Ask for a repeat visit
revisit.body              If this report does not satisfy you, we come back and
                          redo the work within seven days of the visit, at our
                          cost. Tell us what is wrong so that the crew knows what
                          to look at.
revisit.field             What is wrong?
revisit.placeholder       For example: the kerb on the left is still dirty; the
                          stone still has green marks along the base.
revisit.photo             Add a photograph (optional)
revisit.photo.helper      Up to three photographs, 10 MB each. JPG, PNG and HEIC.
revisit.cta               Ask for a repeat visit
revisit.helper            We come back to you within one business day and agree a
                          date with you.

revisit.sent.h            We have your request
revisit.sent.body         Hayk will contact you to agree the date. The repeat
                          visit is free and it does not use one of the visits in
                          your subscription.
revisit.sent.ref          Your reference is {reference}.

revisit.late.h            This visit was more than seven days ago
revisit.late.body         The free repeat visit applies within seven days of a
                          report. Tell us anyway — if it is our mistake we will
                          still put it right.
revisit.late.cta          Tell us what happened

status.revisit            Repeat visit requested
revisit.scheduled         Repeat visit on {date}, for the visit of
                          {original_date}
revisit.notCounted        A repeat visit does not use one of the visits in your
                          subscription.
```

#### 10.5.4 Failed card payment

The one place besides form validation where the error colour appears: on the
heading rule and the glyph, never as a panel fill, never as a button.

```
payfail.h                 The payment did not go through
payfail.body              Your card was not charged. This usually means the bank
                          declined it rather than anything being wrong with your
                          details.
payfail.do.h              What you can do
payfail.do.1              Try again, or use a different card.
payfail.do.2              Pay by bank transfer instead — we will send an invoice.
payfail.do.3              Call Hayk on +374 93 154 108 and we will take it from
                          there.
payfail.cta               Try again
payfail.alt               Pay by bank transfer

payfail.renewal.h         We could not take this year's payment
payfail.renewal.body      Your subscription and your reports are unaffected and
                          nothing has been cancelled. Pay by transfer, or update
                          the payment details, and the schedule continues as it
                          is.
```

#### 10.5.5 Bank transfer pending — the silence between paying and being confirmed

Neutral, never the error colour: nothing has gone wrong.

```
transferpending.h         We are waiting for your transfer
transferpending.body      The invoice is below. A transfer from abroad usually
                          takes one to three working days. When it arrives we
                          confirm it here and by email. Nothing is needed from
                          you in the meantime.
transferpending.cta       Open the invoice
transferpending.alt       Copy the bank details
transferpending.ref       Please quote {payment_reference} so that we can match
                          it.

transferlate.h            We have not received your transfer yet
transferlate.body         It has been {n} working days. Transfers from abroad
                          sometimes take longer, and nothing is wrong with your
                          subscription. If you have the payment reference from
                          your bank, send it to us and we will trace it.
transferlate.cta          Send us the reference
transferlate.alt          Call Hayk on +374 93 154 108

cardnotlive               Card payment on the site is being set up with our bank
                          and is not live yet. We are not promising a date. We
                          will never ask you for card details by phone or by
                          message.
```

---

## 11. System messages and notifications, per channel

### 11.1 Channel rules

| Channel | Rule |
|---|---|
| **Email** | Text-first, one Anthracite header bar, system font stack, no photographs — a report notification renders in a preview pane at somebody's work. Subject states the fact, the first sentence repeats it, the plot is named. No marketing footer, no unsubscribe pressure on transactional mail. Sent in the recipient's chosen language. |
| **Push / in-browser** | Title ≤40, body ≤110. States the fact only. Never carries a name from a monument, never a photograph, never a price. |
| **In-portal** | A neutral toast (`Link copied.`) or an inline panel. A postponed visit, a completed payment and a sent invitation are all neutral and are differentiated by their words, not by colour. |
| **WhatsApp / SMS to the local contact** | Only the day-before reminder and the report link. Never a price, never an invoice, never a renewal message. Sent only after the Owner has confirmed the person agreed. |
| **WhatsApp, first contact from us** | Hayk writes first, from +374 93 154 108, before calling. A US or French recipient will not answer an unannounced Armenian number, and increasingly the carrier will silence it. |

### 11.2 The messages

#### 11.2.1 Consultation received

```
email.consultAck.subject    We have your request — MemoryCare            (33)
email.consultAck.preheader  We reply within one business day, Yerevan time.
email.consultAck.body
{first_name},

We have your request about a plot at {place}.

We reply within one business day, Yerevan time (UTC+4). Hayk will write to you
on WhatsApp from +374 93 154 108 first, and call only if you prefer.

{If a calculator configuration was attached:}
You configured: {area} m², {monuments} monuments, {tier} — {price} ֏ AMD a year.
The person who calls you will be looking at the same figures.

While you wait, this is what a report looks like: {sample_report_url}

MemoryCare · info@memorycare.am · +374 93 154 108
```

WhatsApp, first contact, written by Hayk from the same number:

```
wa.firstContact
Good {morning/afternoon}, {first_name}. This is Hayk from MemoryCare in Yerevan —
you asked us about care for a family plot. Is now a good time to write, or would
you prefer a call? Nothing is being sold in this conversation.
```

#### 11.2.2 Welcome and portal activation

```
email.welcome.subject     Set up your MemoryCare portal access          (36)
email.welcome.preheader   Your subscription is active. Choose a password.
email.welcome.body
{first_name},

Your subscription for {plot} is active. The portal is where your reports appear
and where you can invite the rest of the family.

[Set up your access]

The link works once and lasts seven days. If it has expired, ask for a new one on
the sign-in page or call Hayk on +374 93 154 108.
```

Reminder if not opened in three days: same subject prefixed `Reminder — `, same
body, one added line: `Nothing is wrong; the link is simply still waiting.`

#### 11.2.3 Report ready

```
email.reportReady.subject   Your visit report is ready — {date}        (≤52)
email.reportReady.preheader Photographs, video and the GPS point from {date}.
push.reportReady            Your visit report is ready                  (26)
push.reportReady.body       The report from the visit on {date} is ready. (51)
email.reportReady.body
{first_name},

The crew visited {plot} at {cemetery} on {date}. The report is in your portal
within 48 hours of the visit, and it is there now: photographs on arrival and
after the work, video, and the GPS point recorded at the plot.

[Open the report]

You can send this report to the family with a link — they do not need an account.

MemoryCare · info@memorycare.am · +374 93 154 108
```

#### 11.2.4 Visit tomorrow — opt-in only

```
email.visitTomorrow.subject   A visit to your plot tomorrow, {date}     (≤52)
push.visitTomorrow            A visit tomorrow                          (16)
push.visitTomorrow.body       The crew is due at your plot tomorrow, {date}. (52)
email.visitTomorrow.body
{first_name},

Our crew is due at {plot}, {cemetery}, tomorrow, {date}.

Nothing is needed from you. The report will be in your portal within 48 hours of
the visit.

If you need to move this visit, call +374 93 154 108 or reply to this message.
```

To a local contact, by WhatsApp or SMS, never email-only:

```
wa.localContact.reminder
{recipient_name}, this is MemoryCare. {owner_name} asked us to let you know: our
crew is due at {plot}, {cemetery}, tomorrow, {date}, in the {morning/afternoon}.
You do not have to be there. If you would like to meet them, reply here or call
+374 93 154 108.
```

#### 11.2.5 Visit moved by weather

```
email.moved.subject     The visit to your plot is moving — {new_date}   (≤52)
push.moved              Tomorrow's visit is moving                       (26)
push.moved.body         The visit moves to {new_date} because of the weather.
                        Nothing is lost.                                 (72)
email.moved.body
{first_name},

We are moving the visit planned for {old_date}. {weather_reason} — working in
these conditions would not clean the stone properly and it is not safe for the
crew.

The new date is {new_date}.

The visit is not lost. It stays part of your subscription and the rest of your
year does not change. If the weather never allows a winter visit, that visit is
added to spring.

If {new_date} does not suit you, call +374 93 154 108 and we will find another.
```

#### 11.2.6 Could not reach the plot

```
email.noaccess.subject   We could not reach your plot today             (34)
email.noaccess.preheader We went, we were stopped, and we return on {return_date}.
push.noaccess            We could not reach the plot                     (27)
push.noaccess.body       We went, we were stopped, and we return on {return_date}.
                                                                         (56)
email.noaccess.body
{first_name},

Our crew went to {plot} at {cemetery} today, {date}, and could not reach it.

What we found: {obstruction_description}

The crew arrived at {arrival_time} and recorded their position at the cemetery.
We photographed the obstruction so that you can see exactly what we saw.

[See what we found]

What happens now: we return on {return_date}. {action_taken}

This visit does not come out of your subscription.

If you would rather talk to someone, call Hayk on +374 93 154 108 — he has the
crew's account of it.
```

#### 11.2.7 Payment

```
email.paymentReceived.subject   Payment received — {amount} AMD           (≤52)
push.paymentReceived            Payment received                          (16)
push.paymentReceived.body       We have received {amount} ֏ AMD. Your
                                subscription is active.                   (58)
email.paymentReceived.body
{first_name},

We have received {amount} ֏ AMD for {tier}, for {plot} at {cemetery}.

Your subscription runs from {start_date} to {end_date} and covers {visits_total}
full visits. The invoice is in your portal.

[Open the portal]

The first visit is {first_visit_status}.
```

```
email.transferPending.subject   We are waiting for your transfer          (32)
email.transferPending.body
{first_name},

Your invoice for {amount} ֏ AMD is attached and is also in your portal.

A transfer from abroad usually takes one to three working days. When it arrives
we confirm it in the portal and by email. Nothing is needed from you in the
meantime. Please quote {payment_reference} so that we can match it.
```

Day three, from a named person, not from a system address:

```
email.transferDay3.subject   Your transfer has not arrived yet            (33)
email.transferDay3.body
{first_name}, this is Hayk.

Your transfer of {amount} ֏ AMD has not reached us yet. That is normal at three
days for an international payment and nothing is wrong.

If you would like me to trace it, send me the reference your bank gave you, here
or on WhatsApp at +374 93 154 108.
```

Day seven: same subject, the bank details repeated in full, and one line:
`If it is easier to start again, tell me and I will reissue the invoice.`

```
email.paymentFailed.subject   We could not take this year's payment       (37)
email.paymentFailed.body
{first_name},

We tried to take {amount} ֏ AMD for {plot} and the payment did not go through.
Your card was not charged.

Your subscription and your reports are unaffected and nothing has been cancelled.
You can pay by transfer or update the payment details in the portal, and the
schedule continues as it is.

[Open the portal]  ·  Call Hayk on +374 93 154 108
```

#### 11.2.8 Renewal — 30 days before the client's own anniversary, no auto-charge

```
email.renewal.subject   Your subscription renews on {date}                (40)
push.renewal            Your subscription year ends on {date}
email.renewal.body
{first_name},

Your {tier} subscription for {plot} reaches the end of its year on {date}. A new
year is {amount} ֏ AMD for {visits_total} full visits.

We do not charge a card automatically. If you would like another year, tell us
and we will send the invoice. If not, nothing happens and the reports you already
have stay in your portal.

In the past year we visited {n_completed} times and every report is in your
portal.

[Review my subscription]  ·  Call Hayk on +374 93 154 108
```

`{n_completed}` is the only count in this product. It is our own visits, each
with a report the reader can open and check.

A second, shorter notice goes seven days before the date, same facts, no urgency
language, no countdown, no colour.

#### 11.2.9 Family Circle invitation

```
email.invite.subject   You have been added to a family circle             (38)
email.invite.body
{recipient_name},

{owner_name} looks after {plot} at {cemetery} through MemoryCare and would like
you to see the reports.

You will see the photographs, video and details of every visit. There is nothing
to pay and nothing to set up beyond a password.

[Accept the invitation]

If you do not know why you have received this, you can ignore it — the invitation
expires in 14 days and nothing happens.
```

#### 11.2.10 Repeat visit

```
email.revisitAck.subject   We have your request for a repeat visit        (39)
email.revisitAck.body
{first_name},

You told us the report from {date} was not right. We are coming back.

What you told us: "{client_text}"

Hayk will contact you within one business day to agree a date. The repeat visit
is free and it does not use one of the visits in your subscription.
```

```
email.revisitSet.subject   The repeat visit is set for {date}             (≤52)
email.revisitSet.body
{first_name},

The crew returns to {plot} on {date} to redo the work. They have your note about
{short_summary}.

You will get a new report after the visit, in the usual way.
```

#### 11.2.11 Cancellation

```
email.cancelled.subject   Your subscription is cancelled                  (30)
email.cancelled.body
{first_name},

Your {tier} subscription for {plot} is cancelled.

You paid {amount_paid} ֏ AMD and received {visits_done} of {visits_total} visits,
so we are returning {amount_paid} × {visits_left}/{visits_total} =
{refund} ֏ AMD to {method}. It usually arrives within one to three working days.

Your reports stay in the portal and the links you have sent to your family go on
working. Nothing is deleted.

If you want to come back, your plot and its GPS point stay on record.
```

#### 11.2.12 Ownership transfer

```
email.transferRequest.subject   {owner_name} would like you to take over the
                                care of a family plot
email.transferRequest.body
{recipient_name},

{owner_name} looks after {plot} at {cemetery} through MemoryCare and has asked us
to transfer it to you.

If you accept, you become the Owner: the subscription, the visit schedule, the
invoices and the family circle. The reports already made stay where they are.

Nothing is charged to you today. The subscription year ends on {end_date} and we
will write to you before then.

[Accept]   [Decline]

If you are not sure why you received this, speak to {owner_name} first, or call
Hayk on +374 93 154 108. The request expires in 14 days on its own.
```

```
email.transferDone.subject   Ownership of the plot has been transferred   (42)
email.transferDone.body
The transfer is done. {new_owner_name} is now the Owner of the subscription for
{plot}. {old_owner_name} keeps access to every report as a family manager.
```

### 11.3 Notification matrix — who gets what

| Event | Owner | Family manager | Family member | Local contact | Guest |
|---|---|---|---|---|---|
| Report ready | email + push | email + push | email + push | report link by WhatsApp/SMS | — |
| Visit tomorrow (opt-in) | email + push | email + push | opt-in | WhatsApp/SMS | — |
| Visit moved | email + push | email + push | email | WhatsApp/SMS | — |
| Could not reach the plot | email + push | email + push | email | WhatsApp/SMS | — |
| Repeat visit acknowledged / scheduled | email | email | email if they asked | — | email if they asked |
| Payment received / pending / failed | email | — | — | — | — |
| Renewal notice | email | — | — | — | — |
| Cancellation | email | email (fact only, no money) | — | — | — |
| Invitation | — | email | email | — | — |
| Ownership transfer | email | email | — | — | — |

**Hard rule, restated:** no renewal, price, payment, invoice or upgrade message
is ever addressed to a Family member, a local contact or a Guest.

---

## 12. Link preview for a shared report

The link is pasted into a family group chat and forwarded past the family more
often than the family thinks. The preview therefore carries our mark, the words
"Visit report" and the date — nothing else.

```
og:site_name     MemoryCare
og:title         Visit report — {date}                                  (32 ch)
og:description   A record of a MemoryCare visit. Photographs, video and GPS.
                                                                        (59 ch)
og:image         brand/og/report-share.png — the mark and the words "Visit
                 report" on an Anthracite ground, 1200×630, 1.91:1
og:type          article
twitter:card     summary_large_image
<title>          Visit report — {date}
robots           noindex, nofollow  (also as an X-Robots-Tag header)
```

Shorter form where a client truncates:

```
og.short.title       Visit report — {date}
og.short.description MemoryCare · photographs, video and GPS.
```

### 12.1 The rules behind those strings

1. **Never a photograph in the preview.** Not a plot, not a monument, not a
   grave, under any circumstances, including when the client has shared the
   report publicly themselves. The OG image is a static generated asset.
2. **No cemetery, no sector, no plot, no name.** A location in a preview
   identifies the family to everyone in the chat, including people the Owner
   did not choose to tell.
3. **Anthracite ground.** A Nude 1200×630 renders as a near-blank card in a dark
   WhatsApp thread, and the colour mark's hands vanish on Nude.
4. The crawlers of Meta and Viber fetch the URL unauthenticated. That is
   acceptable only because rules 1 and 2 hold.

### 12.2 Sharing a marketing page

Different asset, different strings — never the report OG.

```
og.site.title        MemoryCare — grave care in Yerevan cemeteries
og.site.description  Scheduled care for a family grave in Yerevan, with photo,
                     video and GPS reports after every visit.
og.site.image        brand/og/site-share.png — mark and wordmark on Anthracite,
                     1200×630
share.page.cta       Send this page to your family
```

### 12.3 The report PDF

Same block order as §9.5, A4, and **never any price in any variant** — one file
serves Owner, member and guest, because it is the artefact that circulates in a
family chat. It carries the mark, the plot line under the same name rule as the
screen, and the tagline set from the print asset. It is not deleted when a
subscription is cancelled.

### 12.4 Runtime variable allowlist

`{first_name}` `{owner_name}` `{owner_first_name}` `{new_owner_name}`
`{old_owner_name}` `{recipient_name}` `{name}` `{email}` `{plot}` `{cemetery}`
`{sector}` `{date}` `{old_date}` `{new_date}` `{return_date}` `{start_date}`
`{end_date}` `{notice_date}` `{commit_date}` `{credit_end_date}`
`{arrival_time}` `{departure_time}` `{duration}` `{crew_names}` `{lat}` `{lng}`
`{tier}` `{amount}` `{amount_paid}` `{price}` `{raw_refund}` `{refund}`
`{method}` `{payment_reference}` `{reference}` `{visits_total}` `{visits_done}`
`{visits_left}` `{n}` `{n_completed}` `{area}` `{monuments}` `{work}`
`{work_item}` `{note_text}` `{client_text}` `{short_summary}`
`{obstruction_description}` `{action_taken}` `{weather_reason}` `{place}`
`{rate_date}` `{first_visit_status}` `{date_or_status}` `{on_or_off}`
`{morning/afternoon}` `{sample_report_url}`

Blocking placeholders that are **not** runtime variables and must be resolved
before launch: `{LEGAL_ADDRESS}` `{REG_NUMBER}` `{WORKING_HOURS}` `{DATE}` (on
legal pages). `lint:strings` fails the build on any `{…}` outside the allowlist.

Plural forms: `{n} visits`, `{n} monuments`, `{n} m²`, `{n} working days`,
`{n} people` are authored as ICU messages from the start. Russian has three
forms, Armenian two. Retrofitting them costs more than writing them now.

---

## 13. Convergence — what I decided, and what is still open

### 13.1 Decisions I took during convergence

Each of these was a live disagreement between two or more round-two memos with
no owner ruling covering it. I chose, and I say why.

1. **One button label, `Request a consultation` (22), everywhere — including
   the tariff cards and the mobile action bar.** 05 wanted `Free consultation`
   (17) on the bar and 04 wanted it on the cards, to avoid a two-line wrap.
   With the annual band now two cards rather than three, and the bar a single
   full-width button, the wrap risk is gone at 360px, and one label is worth
   more than 17 characters of tidiness. "Free" lives in the form heading and in
   the permanent support line under every instance.
2. **The crew note sits after the photographs and video, not before them.** I
   argued the other way in round two; 01 conceded its own position, and 02 and
   05 both place it after. Three to one, and the note reads better as commentary
   on images already seen. The first screen is saved from reading as a receipt
   by the GPS block, not by the note.
3. **Photographs run chronologically: "On arrival", then "After the work".**
   05's "first image is the after shot" is struck. A record that opens on the
   clean stone with no reference frame is a marketing image.
4. **Special is one line beneath the calculator, not a card.** A priceless card
   in a row of published prices re-opens the exact fear the calculator exists to
   close.
5. **`tariff.badge.leading` is allowed 18 characters instead of 05's 14.** The
   owner's string is `Our recommendation`; the layout budget yields to the
   owner's string, and the badge wraps rather than ellipsises in `hy`/`ru`.
6. **The guest report keeps exactly one interactive element** — a tertiary text
   link, `Something is not right with this report`. I had argued for a dead
   page; the split-payer case (payer abroad, mother in Yerevan without an
   account) makes a dead page a phone call across eight time zones. It is
   support, never sales, and it is a link, never a button.
7. **The prices in the recommended-work block stay, for Owner and Family manager
   only, last on the page, removed server-side for everyone else, and never in
   the PDF.** 02 wanted an absolute ban; that pushes the price conversation into
   a channel we cannot control.
8. **`val.calcCeiling` and every bad-news state are neutral, never in the error
   colour.** Reaching 100 m² is a normal outcome, and "could not reach the plot"
   is a report of a visit that happened, with GPS proof.
9. **The `og:description` names no cemetery.** My round-one string did; the
   brief says date only, and 01 and 02 are right that the link travels further
   than the family expects.
10. **A three-line summary of "What we cannot do" goes on the pricing page.** A
    reader who discovers the limits after paying is a refund.
11. **No competitor is named anywhere on the site, in any language, including in
    an FAQ answer.** We describe the combination we offer; the reader can search
    for themselves, and we would rather they find us honest than defensive.
12. **The renewal figure is visible from day one** in the portal, even in a year
    paid at 95,000, so 160,000 is never a surprise in month eleven.
13. **`Visits` is the portal tab; a report lives inside a visit.** Two documents
    used `Reports` as a tab name alongside `Plots`.
14. **Hours are never stated as a range** until the CEO confirms them. 04 wrote
    "10:00–19:00" and "10–15 minutes" as commitments; they are not confirmed, so
    the copy carries the window only.

### 13.2 Open items — a person, not a writer, has to answer these

| # | Item | Owner | What it blocks |
|---|---|---|---|
| 1 | `{LEGAL_ADDRESS}` and `{REG_NUMBER}` | Owner | Footer on every page, About, Contacts, invoice, and the Ameriabank package |
| 2 | `{WORKING_HOURS}` | CEO | Contacts page. The one-business-day promise itself is settled and does not wait on this |
| 3 | Armenian display names for Express, Optimal, Maximum and Special | Owner or localiser | The Armenian build. Only `Զննում` is confirmed; the others come from a superseded price list |
| 4 | Does Cabin contain ֏ (U+058F)? | Design system | Every price string. The safe fallback is already specified: the currency glyph is bound to its own font family, so the build is correct either way — but the check must be run |
| 5 | Family Circle member limit `{n}` | Owner | One validation message |
| 6 | The commitment that care continues on the paid schedule while a subscription is transferred after a death | Owners | `transfer.death.body` |
| 7 | Legal review of the consent line and of messaging a local contact who never contacted us | Counsel | `form.consult.consent`, `profile.local.consent` |
| 8 | Armenian and Russian localisation brief | Localiser | The polite form (Вы / Դուք) throughout without exception; the honesty block re-argued rather than translated literally; Armenian uppercase avoided in badges and micro-labels |

Everything else in this package is written, counted and ready to paste.
