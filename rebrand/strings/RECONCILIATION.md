# RECONCILIATION — how every conflict between the five decks was ruled

**Content lead, 02.09.2026.** Inputs reconciled: `rebrand/BRIEF.md`,
`docs/content-2026-09-01/EDITORIAL-SYSTEM.md`, `COPY-en.md`, `COPY-ru.md`,
`COPY-hy.md`, `COPY-legal-and-about.md`, `docs/PROMPT-BANK-COMPLIANCE-UIUX.md`,
and the owner decisions relayed by the design lead on 02.09.

Output: `en.json`, `ru.json`, `am.json` — **623 keys, identical in all three,
no key present in one and missing in another.** The three files are generated
from one source table, so parity is structural rather than checked.

A build-time check runs over all three files for every banned string in
`EDITORIAL-SYSTEM.md` §2.1–§2.5 plus one-script-per-locale, currency form,
thousands separator, all-numeric dates, emoji, exclamation marks, straight
quotes and informal address. **It currently reports zero hits.** Six
whitelists exist and each is by key, never by pattern; they are listed in §11.

---

## 1. Product names — ruled, and owner-approved

The English and Russian writers independently rejected the cognate set with the
same three arguments: `Express` promises speed on a line-up whose whole claim is
that every visit is full; `Optimal`/`Maximum` are comparatives and re-import the
quality ladder the owner's 26.08 decision destroyed; `Special` is a promotional
word. The Armenian writer reached the same conclusion about `Էքսպրես խնամք` —
"the quick version of the care" — and solved it structurally instead of by
renaming.

**Shipped set:**

| | AM (am.json) | RU (ru.json) | EN (en.json) |
|---|---|---|---|
| 20,000 ֏ | `Զննում` | `Осмотр` | `Inspection` |
| 65,000 ֏ | `Էքսպրես` | `Разовый визит` | `Single visit` |
| 160,000 ֏/yr | `Օպտիմալ` | `Сезонный уход` | `Four visits a year` |
| 200,000 ֏/yr | `Մաքսիմում` | `Расширенный уход` | `Six visits a year` |
| calculated | `Հատուկ խնամք` | `Особый уход` | `By arrangement` |

**The Armenian diverges from the other two, and that is a deliberate,
owner-approved divergence, not an unresolved conflict.** The mitigation the
Armenian writer proposed is enforced in the string table: `Էքսպրես` never
appears without `մեկ լիարժեք այց` on the line beneath it —
`home.prices.line.single`, `prices.card.single.pitch`,
`prices.card.single.arithmetic`, `prices.calc.chip.single`, `footer.svc.single`.
A build that renders the name without that line has broken the ruling.

One extra argument for `By arrangement` over `Special care`, which nobody in the
three decks made: **`special care` in English is a healthcare term.** It
compounds the exact dementia-care collision the whole English locale is built to
defend against. `By arrangement` names the price mechanism, which is what the
product actually is.

`Inspection` survives in every candidate set and is unchanged.

⚠️ **Downstream, and not ours to fix:** the client contract with the lawyer,
Igor's platform spec, the financial model v6.0 and the design package's
`FINAL-CONTENT.md` all still carry the cognate names against a superseded price
list. Somebody has to reconcile those four documents to this table before the
contract is signed, because the name on the invoice and the name on the card
must be the same word.

**Capitalisation:** sentence case in all three. `Four visits a year`, never
`Four Visits A Year`. Product names are never inflected in the interface; in
running Armenian and Russian body copy the sentence is rebuilt so the token
stays nominative, except in the three card CTAs where Armenian grammar requires
the definite accusative (`Ընտրել Օպտիմալը`) — those are separate keys and the
build must not concatenate a suffix.

---

## 2. `Մեր խորհուրդը`, not `առաջատար` — carried

Already ruled 01.09 on the Armenian writer's evidence and recorded in
`CLAUDE.md`. `առաջատար` means *market leader*, not *our recommendation*: as a
badge next to a price, with zero paying customers, it makes on the Armenian site
exactly the claim the English and Russian sites are forbidden to make, in a word
the English glossary cannot see doing it.

`prices.badge.recommended` = `Our recommendation` · `Наша рекомендация` ·
`Մեր խորհուրդը`.

`EDITORIAL-SYSTEM.md` §2.7 item 1 still instructs the build engineer to
**whitelist `առաջատար` on `tariff.badge.leading`**. That instruction is now
wrong and must be struck: the word is banned everywhere with no exception, and
the key it whitelists does not exist in this string set. The banned-string check
shipped with these files bans `առաջատար` unconditionally.

---

## 3. The editor's slot register versus the UX budgets

**Ruling A stands: `hard` beats `× 1.30`.** `rebrand/BRIEF.md` inherits the
sentence "the English budget × 1.30 is the build target", which contradicts the
document it points at. On a hard slot the Armenian and Russian ceilings are the
same number as the English and the writer shortens; `× 1.30` is the *component's*
build target on soft slots only — how much room the engineer leaves, not how
much the writer spends.

**Scope, per the owner's 02.09 decision: desktop budgets, and nothing may
overflow down to 360.** So `EDITORIAL-SYSTEM.md` §3.4's desktop re-derivation
governs wherever it names a slot, and §3.3's number governs everywhere else —
but a re-derived budget is now a *typographic* ceiling, not a licence to depend
on a wide container. Six strings in this set only fit because the container is
wide, and each is named below so the build can check them at 360 first:

| Key | Depends on | What breaks at 360 |
|---|---|---|
| `home.hero.standfirst` | full-width hero | wraps to 4–5 lines; check the fold |
| `home.honesty` | full-width bordered panel at body size | must not be set smaller to fit — Ruling E |
| `prices.rail.description` | full-width entry rail | two clauses, neither cuttable |
| `prices.rail.chip` | full-width rail, 14px uppercase | AM is 33 ch; wraps |
| `how.weather` | full-width band | the longest string on the site |
| `prices.calc.rate1` | result panel at 42% of a full-width card | arithmetic, tabular figures |

**Four Kind-1 budget growths the lead must approve, unchanged from §3.5:** slots
1 (nav), 53, 54 and 55 — the in-card feature lines, credit line and button. A
three-up card row at 1200 gives each card roughly the width a full-bleed card
had at 360, so desktop gives these nothing back. Deciding it now is free;
deciding it at QA costs a design round.

**Five Armenian breaches that survive re-derivation, each ruled:**

| Slot | Budget | AM | Ruling |
|---|---|---|---|
| 81 weather paragraph | 420 hard | ~600 | **Raise to 610.** The budget is a rule about order — limit, window, added-to-spring — and the Armenian keeps that order exactly. The overage is the clause explaining *why* the temperature limit exists. Without it the limit reads as an excuse. The English and Russian carry the same clause and are also over; the English deck's 379-character version is the one that lost the argument, not the budget. |
| 54a credit line | 68 hard | 70 | **Raise to 72.** The alternative buys two characters by dropping `ամբողջ` (*in full*), the word the rule turns on. |
| 74a guarantee remedy | 120 | 138 | **Raise to 145.** The overage is the clause making the seven days run from report delivery, not the visit date. That clause is the guarantee. |
| 25a GPS annotation | 90 | 92 | **Raise to 96.** Slot 24 was re-derived and slot 25 sits in the same component; 25 was missed. |
| 88 link-preview | 200 | 204 | **Raise to 210.** The four characters are `Ստացողին գրանցում պետք չէ։` — the sentence the feature exists for. |

**Russian: nine breaches, all paragraphs, none of them labels.** The Russian
writer's own systemic finding is correct and is adopted as a rule for the
build: **reserve slack in paragraphs, not in chips.** Of sixty-plus hard slots
Russian breached none; every failure was a body paragraph where English uses one
word (`GPS-verified`) and Russian needs a prepositional group. Rulings: take the
writer's supplied short forms at `home.hero.ctaSupport` (23-alt),
`how.overclean` (82-alt), `how.crew` (83-alt) and `contacts.hours` (99-alt) —
all four are in the shipped files. Grow the component at `prices.credit.worked2`
(two columns, description and sum — it is arithmetic and should read as
arithmetic), `how.step1.body` (raise to 300), `report.linkPreview` (split into
two paragraphs), `family.privacy` (four bullets of 80, not one paragraph of 330)
and `how.weather` (see above).

**Two floors are not negotiable and no budget may be met by breaking them:**
body text never below 16px, no informational text below 14px. A string that
fits only because it was set smaller has not fitted.

---

## 4. The comparison FAQ — HELD, not shipped

The English deck cut the damage question and shipped five items. The Russian
deck recommended holding the whole block until the liability figure exists. The
Armenian deck shipped it as one of its six home FAQ items, damage question
included.

**Ruled with the Russian writer, and confirmed by the owner: the block is
written in full and held.**

The reasoning, because it is the one place where the more cautious deck was also
the more rigorous one. The design lead's condition was that the block ships only
if we clear *every* item at the moment of writing. Cutting the item we fail does
not satisfy that condition — it satisfies it by editing the test, which is
precisely the reverse-engineering the rule exists to forbid. A buyer standing in
front of two tabs asks what happens if the monument is damaged; a checklist that
omits it is not a buyer's list, it is a list of our strengths wearing a buyer's
clothes. And the omission is visible to exactly the reader the block is aimed at.

Written, keyed and **not rendered**, under the namespace `held.compare.*` —
six questions including the damage question, plus
`held.compare.note` = `[HELD — ships the day the liability figure is bound by
the lawyer]`. The namespace is called `held` so no builder ships it by
accident. One dependency, one paragraph of work, and it goes live.

**Consequence for the home FAQ.** The Armenian had spent one of six items on the
comparison question. With the block held, that item is replaced. See §5.

---

## 5. The FAQ sets — one fixed meaning set, three native answers

`EDITORIAL-SYSTEM.md` §6.4 item 3 is adopted: the questions are one meaning set,
identical across the three locales; the answers are written natively and diverge
structurally. Three writers each choosing "the questions my reader asks"
produces three FAQs, and one locale then loses the diaspora question while
another loses the local one.

**Home, six items** (`home.faq.q1`–`q6`): where the plot is · winter · the crew
cannot reach the plot · family access without paying · someone from the family
present at the visit · what happens after you request a consultation.

Changes from the decks, and why:
- **Prices-abroad moves to the pricing FAQ.** The English deck's argument wins:
  the home page answers the suspicion where it forms, in the tariff strip
  (`home.prices.onePriceList`), and the full question and answer live where a
  reader thinking about price is already standing. The Russian deck carried it
  on both pages; printing one question twice is worse than either placement.
- **The card-payment question leaves the home FAQ.** The Armenian deck had it
  and correctly marked its own answer `[BLOCKED]`. It is answered honestly on
  the pricing FAQ (`prices.faq.a6`) and in the terms, where "bank transfer now,
  cards when the bank enables them, no date" is a full answer rather than a
  blocked one.
- **"Can someone from the family be there?"** is promoted from the Russian deck.
  It is the only question in the three decks that serves the local buyer and the
  diaspora buyer with one answer, and it makes the Yerevan relative — a real
  product feature nobody else slotted — visible on the home page.
- **"What happens after I request a consultation?"** is kept from the English
  deck. It is the question a reader has with their hand on the button, and it is
  the one place the callback promise reads as an answer rather than a claim.

**Pricing, six items** (`prices.faq.q1`–`q6`): prices abroad · is a repeat
single visit cheaper · does a larger plot cost more · what is credited and
within what window · instalments · how and when you pay.

Winter leaves the pricing FAQ — the home FAQ and `how.weather` and
`prices.year.footnote` and `legal.terms.winter.p1` already carry it, and a fourth
printing was a duplicate rather than a coverage gain. The freed slot goes to the
credit rules, which are **bank condition 4.10.10** and had no FAQ anywhere.

---

## 6. Terminology drift — the six the brief named, plus the ones it missed

Canonical forms, applied everywhere and checkable by grep:

| Concept | AM | RU | EN |
|---|---|---|---|
| the visit | `այց` · full: `լիարժեք այց` | `визит` · `полный визит` | `visit` · `full visit` |
| the report | `հաշվետվություն` | `отчёт` | `report` |
| the plot | `հողամաս` | `участок` | `plot` |
| the grave (reader's word) | `գերեզման` | `могила` | `grave` |
| the monument | `տապանաքար` | `памятник` | `monument` |
| the crew | `խումբ` | `бригада` | `crew` |
| the subscription | `բաժանորդագրություն` | `подписка` | `subscription` |
| the credit | `հաշվանցում` / `հաշվանցվում է` | `зачёт` / `засчитывается` | `credit` / `credited` |
| the portal | `անձնական էջ` | `личный кабинет` | `client portal` |
| the cemetery | `գերեզմանոց` | `кладбище` | `cemetery` |
| the GPS point | `GPS կետ` | `GPS-точка` | `GPS point` |
| Family Circle | `Ընտանեկան շրջանակ` | `Семейный круг` | `Family Circle` |

**Four contests by the Armenian writer, all upheld**, because the editor's own
§1 grants one round on meaning or grammar and all four arguments are about
meaning:

- **`հողամաս`, not `տեղամաս`.** `տեղամաս` means an administrative *precinct* —
  the second half of `ընտրատեղամաս` and `ոստիկանական տեղամաս`. It is not used
  for a parcel of land. This is an error, not a preference.
- **`գերեզմանոց`, not `գերեզմանատուն`.** The standard Eastern Armenian form and
  the one on municipal signage. The word appears in the report metadata on every
  visit; the standard form is the safer one.
- **`խումբ`, not `բրիգադ`.** `բրիգադ` is a Russian loan, and the editor's own
  §1.4b warns that the Armenian will inherit the company's Russian operational
  vocabulary without noticing. This is that vector, in the noun that appears in
  every report. Note that Russian keeps `бригада`: the loan argument is
  Armenian-specific and does not cross.
- **`անձնական էջ`, not `անձնական հաշիվ`.** `հաշիվ` also means *invoice*. On a
  site with invoices, a payment page and refund arithmetic, `ձեր անձնական հաշիվը`
  two components from `հաշիվ-ապրանքագիր` is a real ambiguity in the exact place
  a reader is deciding whether to trust us with money.

**`отчёт`, never `фотоотчёт`** — carried from the editor. The whole positioning
rests on the report being photo *and* video *and* a GPS point, and `фотоотчёт`
names one third of it. The Russian source documents use it throughout, which is
why it needed a ruling rather than a preference.

**The plot / the grave split** is the one deliberate two-word case, and the
Russian writer's rule governs all three locales: the reader's word (`могила` /
`grave` / `գերեզման`) lives in the descriptor, the `h1`, the `<title>`, the
meta description and the first paragraph, where the SEO and the euphemism rules
both require it; the working word (`участок` / `plot` / `հողամաս`) lives
everywhere we talk about the work, the price, the area, the crew and the report
— about ninety per cent of strings. **They never appear in the same sentence**,
with one deliberate exception: `report.ann.2`, where the contrast *is* the
point — the GPS point answers "was the crew there", not "where is the grave".

**`weather window` is not translated as a term.** Armenian has no such idiom and
`եղանակային պատուհան` parses as meteorology, so the Armenian says *on the days
the weather allows* and attaches the temperature. That is not a hedge — it
carries a number — and it is what a builder in Yerevan actually says. The
English and Russian follow the Armenian here rather than the other way round;
the English "suitable weather window" survives only in `prices.year.footnote`
where the space is a single line.

---

## 7. Six more conflicts nobody listed, ruled

**7.1 `Kärcher` — removed from all three locales.** The Russian deck wrote
`аппарат Kärcher на низком давлении` at two slots and the Armenian named
`Kärcher` at two more. `CLAUDE.md` is unambiguous: never write Kärcher as
shorthand for the method, because the word names both our neutral-pH chemistry
and a pressure washer, and high-pressure washing is forbidden on monuments —
above 500 psi on polished granite, above 100 psi on tuf. Copy that lists
"Kärcher" beside "deep cleaning" reads as pressure-washing a grave. The method
is now described by what it is: steam, neutral-pH products chosen for the stone,
wet/dry vacuum, with the pressure limit stated as a rule
(`home.method.equipment.line`, `how.includes.7`,
`legal.limitations.ask.5`). The Russian writer's own §15.5 asked for this to be
settled with operations rather than in copy; it is settled here, in the safer
direction.

**7.2 Thousands separator: comma, in all three locales.** The Russian deck used
a non-breaking space (`160 000`), which is typographically correct Russian and
Armenian and which I am overruling. The editor's reason is decisive and it is
not aesthetic: a space-grouped `40 000` is invisible to the build check unless
every surface normalises four Unicode space characters correctly, and the one
price this site must never print again is a space-grouped one. One typographic
compromise, applied consistently, buys a check that actually fires. The check
shipped with these files normalises U+00A0, U+2009 and U+202F before matching
and flags any space-grouped number.

**7.3 Currency: `160,000 ֏ AMD` in price fields; `֏` alone in the second half of
an arithmetic line.** The Armenian writer's contest is partly upheld. `֏ AMD` is
four characters that land on two 44-hard arithmetic budgets which §3.4
deliberately did not widen — and those two strings are the ones that turn a
premium price into a sum a reader can check. So: `AMD` is written once per line,
on the annual figure, and dropped from the per-visit figure, in all three
locales, so `prices.card.optimal.arithmetic` and
`prices.card.maximum.arithmetic` fit. The bank condition (4.10.5, prices quoted
in AMD) is satisfied by the price fields, the footer currency line and the FX
note. What I did **not** grant is `դրամ` in general Armenian prose — it appears
in no shipped string — because one word for the currency across three locales is
worth more than the idiom. `֏` appears in all three files: it is a currency
sign, not Armenian copy.

**7.4 The portal is never described as a screen you can go and look at.** The
editor's §6.3 ruling is adopted in full, and it required rewriting three strings
that had slipped: the Armenian `28c` and `53a3` and the Russian `78.4c` all said
the report *appears in your personal account*. The report now **arrives**, as a
link you can forward, in every locale — `home.how.step3.line`,
`how.step4.body`, `prices.card.single.f3`, `frozen.report`. The portal appears
only as *what a subscription includes* and in the account-side strings
(`empty.*`, `legal.refund.cancel.p1`), which are true as terms of sale. The
frozen report promise names no channel, so it survives either ruling on the
platform, and the flip when the portal is live is a data change on a named key
set, not a copy round.

**7.5 Two documents each froze a different version of the same promise.**
`PROPOSAL-ux.md` slot 18 froze *"Your report arrives within 48 hours of the
visit."*; `FINAL-CONTENT` §4.4 froze *"The report is in your portal within 48
hours of the visit."* The UX string wins, for the reason in 7.4 and because
`FINAL-REBRAND` §3 gives UX the string slots. `FINAL-CONTENT` §4.4 should be
struck rather than left for whoever writes the emails to find. Nine frozen
strings — `frozen.callback`, `frozen.hours`, `frozen.report` × three locales —
and every other occurrence on the site references those keys rather than
repeating the text, so byte-identity is structural.

**7.6 `Plan · Visit · Report` becomes `Call · Visit · Report`.** The Russian and
Armenian writers arrived at this independently and for the same reason: neither
language has a usable one-word noun for *plan* in this sense, and the first step
is not a plan, it is a conversation. It is also more truthful in English, where
the primary CTA is a consultation request precisely because of that. Changed in
all three (`home.how.step1.label`).

---

## 8. The false content — repurposed, per the owner

- **The statistics band becomes the published protocol.** `home.protocol.*` —
  eight photographs, four angles before and the same four after, two videos of
  20–40 seconds, one GPS point recorded at the plot on the day, the crew's note,
  and the closing line *until all of it exists, the visit is not closed.* Six
  strings, three locales, all true today as an operating rule. The Armenian
  writer's structural note is kept: the heading states the condition and the
  closing line inverts it, which is how a specification reads and how an
  advertisement does not.
- **No testimonial strings and no partner strings are written.** The components
  stay in the codebase behind a flag. What would fill them: the testimonial
  component needs a named client who has received a real report and given
  written consent under the photography-consent form the lawyer is drafting —
  earliest is after the September pilot, and not before that form exists. The
  partners strip needs a signed counterparty; there is none, and an empty strip
  under a heading is the same claim with the evidence removed.
- **The withdrawn `40,000 ֏` price appears nowhere as a price.** It appears once
  per locale as the per-visit arithmetic of the annual product
  (`prices.card.optimal.arithmetic`) and once inside `prices.faq.a2` in
  Armenian, which is correct and required. The check bans it everywhere else and
  whitelists those keys by name.

---

## 9. Locale-specific structure — where a language was given its own sentence

Not a list of translations that came out long. These are places where the
sentence itself is different because the language required it.

- **`home.hero.standfirst`.** English names both reasons in the second person
  without accusing anyone. Armenian cannot: `Հեռու եք ապրում կամ ժամանակ չեք
  գտնում` puts the reader's absence in the second person and lands as an
  accusation. The Armenian moves to the third person indefinite — *some are far
  away, some have no time* — so both reasons are named, neither is ranked, and
  the reader recognises themselves rather than being told which one they are.
  Russian keeps the second person but leads with the outcome and puts both
  reasons in one trailing clause of equal weight.
- **`home.hero.overline` and `home.hero.h1`.** The English overline carries the
  category and the city because `memory care` in English is the dementia-care
  industry's term and the reader has already been shown Alzheimer's services.
  There is no such collision in Armenian, so the Armenian overline is freed for
  the proposition (`Խնամք, որը կարելի է ստուգել`) and the `h1` carries the
  category. **Do not back-translate the Armenian overline; it will look like a
  mistake.**
- **`home.family.line`.** *One person's inbox* has no Armenian or Russian
  equivalent — `inbox` as `մուտքային` is untranslatable jargon and the literal
  Russian gives *почтовый ящик*, which means the thing in the entrance hall.
  Armenian uses `փոստարկղ`, a physical object every reader over forty has stood
  in front of; Russian says *переписка одного человека*. The image changes; the
  observation does not.
- **`home.honesty`.** Re-argued in each language, not translated. The English
  admits three things and offers a substitute; the Armenian puts the substitute
  in an emphatic `Փոխարենը` clause, which stops the paragraph sounding
  apologetic — and an apologetic version of this paragraph inverts its whole
  function. The Russian ends on an instruction (*проверять нас нужно по отчёту*)
  that the English does not have.
- **`home.hero.ctaSupport`.** English is two sentences. Armenian uses the
  correlative `ոչ… ոչ…` and does both halves in one breath; forcing two Armenian
  sentences here is the tell of a translated page.
- **`prices.caption.one` / `.many`.** Armenian does not pluralise a noun after a
  numeral, so one string serves all three cards. **A build that pluralises the
  Armenian caption is a bug.**
- **`home.closing.h2`.** Armenian heads the form with a first-person-plural
  hortative — `Խոսենք` — the one warm word permitted anywhere on the site, at
  the one moment the page asks for something. A nominal Armenian heading turns a
  conversation into a form to be filled, which is the opposite of the reason a
  consultation is the primary CTA.
- **`report.ann.2`.** Armenian puts the whole question inside the sentence with
  `՞` on the participle — `կանգնա՞ծ է եղել` — and no English construction is
  that compact. English needs a separate clause.
- **Armenian punctuation is Armenian.** `։` ends sentences, `՝` carries the
  em-dash pause, `՞` sits over the stressed vowel inside the word, `.` is the
  միջակետ and does semicolon duty inside lists. The build check flags an
  Armenian sentence ending in a Latin full stop, with the list items in
  `legal.privacy.rights.*` whitelisted because there the միջակետ is correct.
- **Polite address throughout:** Russian `Вы`/`Ваш` capitalised in direct
  address, Armenian `Դուք`/`Ձեր`, and Armenian uses the impersonal wherever the
  sentence is a fact rather than a promise. `ты` and `դու` are build failures.

---

## 10. Rulings against the source documents, listed so they can be overturned

1. `EDITORIAL-SYSTEM.md` §2.7 item 1 — the `առաջատար` whitelist — is struck (§2).
2. `EDITORIAL-SYSTEM.md` §1.1 — four Armenian terms replaced on the writer's
   contest (§6).
3. `FINAL-CONTENT` §4.4 — the portal-naming report promise — is dead (§7.5).
4. `FINAL-CONTENT` §4.2 — English name first, Armenian in parentheses — is dead;
   one script per locale, enforced by check.
5. `rebrand/BRIEF.md`'s inherited `× 1.30` sentence loses to `hard` (§3).
6. `rebrand/BRIEF.md` names `Kärcher` in the Express row; `CLAUDE.md` forbids the
   word. `CLAUDE.md` wins (§7.1).
7. The Russian deck's space thousands separator loses to the comma (§7.2).
8. The English deck's five-item comparison FAQ loses to holding the block (§4).
9. The Russian deck's duplicate prices-abroad question on the home page is
   removed (§5).
10. `COPY-legal-and-about.md` writes the entity as `Memory Care LLC` in prose
    and `MemoryCare LLC` in the compliance discussion. Resolved to a single key
    (§11 of TRUTH.md).

---

## 11. The six whitelists in the banned-string check

Each is by key, never by pattern. A whitelist by pattern is a ban switched off.

1. `the only` on `home.prices.sameness` and `prices.sameness` — the ruled-in
   sameness sentence.
2. `40,000` on `prices.card.optimal.arithmetic` (three locales) and
   `prices.faq.a2` (am) — the required per-visit arithmetic.
3. `80,000` / `180,000` on `legal.refund.example2.calc`,
   `legal.refund.example3.calc` and `legal.refund.example3.paid` — refund
   arithmetic results, not product prices.
4. `отзыв` on `home.honesty` — the panel that says we have none.
5. Native-script language labels `ՀԱՅ` / `ENG` / `РУС` in every locale — the
   switcher is the control a lost reader uses to leave, and rendering those
   labels in the host script would be consistent and useless.
6. Latin full stop on `legal.privacy.rights.1`–`.5` (am) — the միջակետ is the
   correct Armenian list separator.

---

## 12. Notes for the build

- **File naming.** The Armenian file is `am.json` as instructed. `am` is
  Amharic. The `lang` attribute must be `hy`, the `hreflang` must be `hy`, and
  the URL segment should be `hy` — the live site currently tells every crawler
  its Armenian pages are Ethiopian. The filename is a lead instruction; the
  markup is not negotiable.
- **Fonts.** Do not write or spec anything that depends on Montserrat covering
  Armenian: the file has 1,312 glyphs, Latin and Cyrillic only, no Armenian and
  no `֏`, and no family called "Montserrat Armenian" exists on Google Fonts. The
  brandbook's typography page is wrong about this and it is a question for the
  designer. Two consequences for these strings: **the Armenian text face is
  currently unresolved**, and **`֏` inside any Montserrat run — every price
  mentioned in English or Russian body copy, the footer currency line, the FX
  note, the arithmetic lines — needs the isolated `unicode-range: U+058F` slice
  pointing at GHEA Mariam**, which we own and which does contain the glyph.
  Prices set in the display face render `֏` natively. Also unverified: whether
  the Armenian text face covers `և` (U+0587), which appears in roughly a third
  of the Armenian strings and has no acceptable fallback — `եւ` is a spelling
  error in reformed orthography.
- **Armenian typesetting:** `hyphens: none`, ragged right, never justified.
  Armenian words in these strings run to 18 characters and justified Armenian
  produces rivers.
- **Placeholders** are `{name}`, `{date}`, `{contact}`, `{place}`, `{area}`,
  `{monuments}`, `{plan}`, `{total}`, `{amount}`, `{plot}`, `{n}`,
  `{n_completed}`, `{paid}`, `{done}`, `{left}`, and `{result}`. They are
  identical across the three files.
- **`{date}` always renders written out** — `14 September 2026` ·
  `14 сентября 2026 г.` · `2026 թ. սեպտեմբերի 14`. Any all-numeric date is a
  build failure; an American and a European reader read `14/09/26` as two
  different days and half this audience is American.
- **Blocked strings render as visible gaps** — `[registration number — to be
  confirmed]`, not a plausible value. Nothing in square brackets may be replaced
  with something that looks real. `+374 10-00-00-00` on the live site is what
  that looks like when it goes wrong.
- **`held.compare.*` is not rendered.** See §4.
- **Phone numbers:** display `+374 55 315 323`, `tel:` href `+37455315323`,
  `wa.me` `37455315323`. Never split across a line break. No trunk zero, no
  brackets, no hyphens — a diaspora reader who dials a trunk `0` from abroad
  gets nothing.
