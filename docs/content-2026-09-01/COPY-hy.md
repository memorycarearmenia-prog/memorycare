# COPY — hy · the Armenian site, written natively

**01.09.2026 · Armenian copywriter.** Every string below is written in
Armenian first. Nothing here is a translation of an English line, and in
several places the Armenian deliberately refuses the English structure —
each of those is flagged inline with **↳ STRUCTURE**.

Governing documents, in precedence order: `FINAL-REBRAND.md` →
`PROPOSAL-strategy.md` (§7 register) → `PROPOSAL-ux.md` §2 and §10 (slots
and budgets) → `rebrand-2026-09-01/BRIEF.md` (facts) →
`site-audit-2026-08-31/`. Where I disagree with a ruling I have complied
and argued in §12, not deviated.

**Scope note.** `FINAL-REBRAND.md` §2b (added 01.09) narrows the build to
desktop web. That removes the 360px argument for tight budgets but not the
budgets themselves — the character ceilings in `PROPOSAL-ux.md` §10 are
component contracts, so I have held to them and flagged every breach.

---

## 0. How to read this file

Every measured string is one line, in this shape:

> `**slot** · what it is · budget · ` ``the string`` ` · N ch`

`N` is the **Unicode code-point count**, computed mechanically, not
estimated. Two things about counting Armenian:

- **`ու` is two code points** (`ո` + `ւ`), and so is `և` **not** — `և`
  (U+0587) is one. Armenian code-point counts are therefore honest counts
  of letters as they are drawn, which is what a width budget wants.
- Armenian punctuation counts too: `։` `՝` `՞` are each one character.

A budget marked **†** is the **desktop re-derived** number from
`EDITORIAL-SYSTEM.md` §3.4 rather than the original `PROPOSAL-ux.md` §10
figure; where §3.4 left a slot alone, the §10 number stands and carries no
dagger. A budget marked **hard** must not be exceeded — in any language,
per `EDITORIAL-SYSTEM.md` §3.1 Ruling A, which overrides the earlier
`EN × 1.30` sentence in this folder's brief. Where the Armenian cannot
be good inside a hard budget I have written the good Armenian, marked it
**⚠ OVER**, and proposed the component change in §11. I have not mutilated
a sentence to make a number.

Blocked strings are marked `[BLOCKED — reason]` and left empty.

---

## 1. Register — the decisions, stated

Armenian carries distinctions English does not, and a site about graves
gets them wrong in one of two directions: the funeral-parlour register
(`հավերժ հիշատակ`, `սգո`, `անմոռաց`) or the ministry register
(`իրականացվում է`, `սույն ծառայության շրջանակներում`, `տրամադրվում է`).
Both are failures here. The first is the cliché the brand forbids; the
second is what most Armenian institutional websites sound like, and it
reads as an office that will not answer the phone.

**What I chose, and it is a single choice made six ways:**

1. **Eastern Armenian, standard (reformed) orthography.** The company is
   in Yerevan and files in Eastern Armenian; the Russian-, European- and
   Yerevan-resident readers all read it natively. Western-Armenian
   readers in Los Angeles and Beirut read Eastern Armenian without
   difficulty in print, and the alternative — a second Armenian locale —
   is not funded and would fragment one brand into two. **Flagged, not
   hidden:** a Western-Armenian reader will notice `եմ գնում` where they
   say `կը երթամ`. That is a known, accepted cost and it is the right
   trade at this size.

2. **`Դուք`, always, and used sparingly.** Never `դու`. But Armenian
   lets a sentence be polite without addressing anyone, and I have taken
   that road wherever the sentence is a fact rather than a promise:
   `Խումբը գնում է հողամաս և գրանցում GPS կետը` addresses no one and
   sounds like a company that keeps records. `Դուք` is reserved for the
   two promises, the form, the guarantees and the error states — the
   places where somebody is speaking to somebody.

3. **Finite verbs, not nominalisations.** The single tell of translated
   Armenian is the string of verbal nouns: `մաքրման աշխատանքների
   իրականացում`. Native Armenian says `մաքրում ենք`. Almost every line
   in this file has a working verb in it, and where a line is a label it
   is a plain noun, not a noun-phrase tower.

4. **Armenian punctuation, correctly.** `։` (վերջակետ) ends sentences —
   not `.`, which in Armenian is the միջակետ and does the work of a
   semicolon. `՝` (բութ) carries the pause the English em-dash carries,
   and it is the most Armenian mark on the page; it appears a lot below
   and that is deliberate. `՞` sits **over the stressed vowel inside the
   word**, never at the end of the line: `Կարո՞ղ եմ վճարել`, never
   `Կարող եմ վճարել?`. No `!` anywhere, per the stop-list and because
   Armenian `՜` would be worse.

5. **No diminutives, no possessive warmth-signals.** Armenian can make a
   sentence tender with one suffix, and every one of them here would read
   as a stranger touching your arm. `Ձեր հարազատի գերեզմանը` — plain
   possessive, nothing more.

6. **The dead person is not a subject.** Armenian has a whole shelf of
   words for the deceased (`հանգուցյալ`, `ննջեցյալ`, `սգո`). None
   appears in this file. The nouns are `գերեզման`, `հողամաս`,
   `տապանաքար`, and where a person is named it is by the reader's own
   relationship: `ձեր հոր`, `ձեր մոր`.

**In one line:** a competent Armenian professional writing to an adult
about their family — the register of a good notary or a good surveyor,
not of a priest and not of a call centre.

---

## 2. Terminology — one word per thing, fixed

This table is the Armenian half of `FINAL-CONTENT` §4.5 and it binds the
whole locale. Where the obvious dictionary word is wrong, the reason is
given.

`EDITORIAL-SYSTEM.md` §1.1 proposes its own Armenian forms and gives W-HY
one round to contest a term on meaning or grammar. **Four rows below
differ from it** — `հողամաս`, `գերեզմանոց`, `խումբ`, `անձնական էջ` — and
each is argued in **§15.2** rather than substituted silently. Everything
else in that table I have adopted, including `հաշվանցում` for the credit,
which is better than the word I had drafted.

| Thing | Armenian | Never | Why |
|---|---|---|---|
| grave | `գերեզման` | `շիրիմ`, `հանգստարան` | `շիրիմ` is elevated/poetic; `հանգստարան` is the euphemism the stop-list bans |
| the family plot | `հողամաս` / `ընտանեկան հողամաս` | `օբյեկտ`, `տարածք` | `օբյեկտ` is the bureaucratic register we refuse |
| cemetery | `գերեզմանոց` | `գերեզմանատուն` | plain and standard |
| headstone / monument | **`տապանաքար`** | **`հուշարձան`** | `հուշարձան` is a *public* monument — a statue in a square. A translator reaches for it and it is wrong every time |
| the base / kerbing | `պատվանդան` / `եզրաքար` | | |
| visit | **`այց`** | `այցելություն` | both are correct; `այց` is four characters shorter and every card budget needs those four. Used consistently so the shortness reads as a decision |
| full visit | `լիարժեք այց` | `խորը մաքրում`, `ծանր այց`, `թեթև այց` | the last two are banned by the 26.08 decision in every language |
| inspection (the product) | `Զննում` | | confirmed name, §3 |
| report | `հաշվետվություն` | `զեկույց`, `ամփոփում` | `զեկույց` is a presentation given at a meeting |
| the portal | `անձնական էջ` | `պորտալ`, `անձնական կաբինետ` | `պորտալ` is untranslated jargon; `կաբինետ` is a Russian calque |
| the crew | `խումբ` | `թիմ`, `մասնագետներ`, `աշխատակիցներ` | `թիմ` is a sports team; `խումբ` is what a work crew is called |
| subscription | `բաժանորդագրություն` | `փաթեթ` (as the product word) | `փաթեթ` survives only in prose about what is inside a subscription |
| Family Circle | `Ընտանեկան շրջանակ` | lower case, `ընտանեկան խումբ` | it is a product name; capital `Ը` |
| GPS point | `GPS կետ` | `գեոպիտակ`, `կոորդինատ` | Armenian attaches suffixes to Latin abbreviations with a hyphen: `GPS-ը`, `GPS-ի`, `GPS կետը` |
| guarantee | `երաշխիք` | `գարանտիա` | |
| consultation | `խորհրդատվություն` | `կոնսուլտացիա` | |
| Merelots | `Մեռելոց` | | the day after each major feast; a working day, which is the point |

**Latin permitted on the Armenian site, exhaustively:** `MemoryCare`,
`GPS`, `Kärcher`, `AMD`, `WhatsApp`, `Viber`, `UTC+4`, `℃`, `մ²`'s
superscript, e-mail addresses and URLs, and the switcher labels `ENG` /
`РУС`. Nothing else. The switcher is deliberately exempt from
one-script-per-locale: it is the control a lost reader uses to leave, and
a reader who cannot read Armenian must be able to find it.

**⚠ The `֏ AMD` problem, complied with and contested.** `FINAL-CONTENT`
§4.3 freezes the currency format as `160,000 ֏ AMD` "without exception".
I have written it that way everywhere. In Armenian it is wrong twice: the
native word is `դրամ`, `AMD` is an export label that an Armenian reader
reads as *this page was written for someone else*, and the string is 13
characters long inside 44-character arithmetic budgets. Argument and
proposal in §12.1.

---

## 3. Product names — the four `[OPEN]` forms, settled

`FINAL-CONTENT` §4.2 marks four of five Armenian names `[OPEN]`, carrying
`խնամք` as a suffix, and attached to a superseded price list. Here is my
ruling on each. Budget for slot 46 is **22 ch, hard**.

| Product | Prior form | **Settled** | ch | Ruling |
|---|---|---|---|---|
| Inspection | `Զննում` | **`Զննում`** | 6 | Confirmed already. Keep. It is exact — `զննել` is to examine and inventory, which is precisely what is bought and it does *not* imply cleaning |
| Express | `Էքսպրես խնամք` | **`Էքսպրես`** | 7 | `խնամք` dropped |
| Optimal | `Օպտիմալ խնամք` | **`Օպտիմալ`** | 7 | `խնամք` dropped |
| Maximum | `Մաքսիմում խնամք` | **`Մաքսիմում`** | 9 | `խնամք` dropped |
| Special | `Հատուկ խնամք` | **`Հատուկ խնամք`** | 12 | `խնամք` **kept** — `Հատուկ` alone is a bare adjective and cannot stand as a name in Armenian |

**Why `խնամք` is dropped from three of five, and why that is not
tidying.** Three reasons, in order of weight.

1. The three cards in the row exist to be compared on one axis. Three
   names that all end in the same word make the eye work to find the
   part that differs, which is the opposite of what the row is for.
2. `Էքսպրես խնամք` is bad Armenian. `Էքսպրես` in Armenian usage attaches
   to *speed* — express delivery, express dry-cleaning — so
   `էքսպրես խնամք` reads as *the quick version of the care*, which is
   the exact meaning the 26.08 decision spent a whole ruling destroying.
   Stripped to a bare label, `Էքսպրես` is a product name and stops
   making a claim about the work.
3. `Հատուկ խնամք` keeps its noun because it needs one, and the
   asymmetry is useful rather than untidy: four short borrowed labels
   and one Armenian phrase, and the Armenian phrase is the one that is
   not a package.

**↳ FLAG for the owner, one real risk.** `Էքսպրես` still carries speed as
its first association even alone, and the product's whole argument is that
it is a *full* visit. My mitigation is structural rather than a rename:
**the word `Էքսպրես` never appears without `մեկ լիարժեք այց` in the line
immediately beneath it** — in the card, in the footer link's title
attribute, in the FAQ, in the calculator chip. It is enforced below. If
the owner will reopen the name, the Armenian that says the product
correctly is `Մեկ այց`; I am not proposing it unasked, because product
names are the owner's, not mine.

**Declension.** These names take Armenian case endings and must not be
frozen as English nouns: `Օպտիմալը`, `Օպտիմալի`, `Օպտիմալով`,
`Զննումից հետո`, `Էքսպրեսի գինը`, `Մաքսիմումով`. The build must not
concatenate `{product} + ի` blindly — `Հատուկ խնամք` inflects on its
second word (`Հատուկ խնամքի`), the other four on their last letter. Four
of five end in a consonant and take `-ի`; there is no exception in this
set, but the rule belongs in the string table rather than in code.

---

## 4. The badge — `առաջատար` is wrong, and here is what replaces it

`FINAL-REBRAND.md` and the brief both instruct: `Our recommendation`,
never a bestseller word, Armenian `առաջատար`. **I am not writing
`առաջատար`, and this is the one ruling I am asking to have changed rather
than merely arguing about in §12.**

`առաջատար` means *leading, front-running, the one out in front*. In
Armenian commercial usage it is what a company calls itself when it
claims market position — `առաջատար ընկերություն`, `ոլորտի առաջատար`. It
is not a synonym for "recommended"; it is a synonym for the thing the
stop-list bans. On a card, next to a price, with zero paying customers, it
asserts exactly what `most chosen` asserts, and it does so in a word the
brief's English glossary cannot see is doing it. `FINAL-CONTENT` §4.5
already bans **`leading choice`** in English — `առաջատար` is that string.

**Settled: `Մեր խորհուրդը`** — *our recommendation*, literally and only.
It is ours, it is advice, it claims nothing about anyone else's behaviour,
and it is 13 characters against a 22 hard budget.

Rejected alternatives, for the record: `Մեր առաջարկը` (`առաջարկ` is a
commercial *offer* — the stop-list's money register), `Խորհուրդ ենք
տալիս` (a verb phrase does not sit in a badge), `Ընտրված` (chosen — by
whom).

---

## 5. Global strings — every page

### 5.1 Header, nav, footer

**1a** · nav · 18 hard · `Գներ` · 4 ch
**1b** · nav · 18 hard · `Ինչպես է աշխատում` · 17 ch
**1c** · nav · 18 hard · `Հաշվետվություն` · 14 ch
**1d** · nav · 18 hard · `Ընտանեկան շրջանակ` · 17 ch
**1e** · nav · 18 hard · `Մեր մասին` · 9 ch

  ↳ **STRUCTURE.** English nav item 3 is `Sample report`; Armenian
  `Հաշվետվության նմուշ` is 19 and breaches an 18 hard budget for no gain.
  Armenian solves it the way Armenian solves most naming: the nav item
  names **the thing** (`Հաշվետվություն`) and the page's own `h1` names
  the sample (`Հաշվետվության նմուշ`, slot 85). A reader arriving on the
  page is told immediately it is a sample; a reader in the nav is told
  what lives there. Nothing is lost and the budget holds.

  ↳ `Գներ` over `Սակագներ`: the strategy's whole pricing argument is that
  the prices are *published*, and `Գներ` says prices. `Սակագներ` says
  tariff schedule — the word a utility company uses.

**2** · primary button · 24 hard † · `Խորհրդատվության հայտ` · 20 ch

  ↳ Not `Անվճար խորհրդատվություն` — 23 ch, over, and "free" belongs to
  the form heading (slot 101), not to every button on the site.
  Not `Կապվել մեզ հետ` (that is `Contact us`, banned).

**3** · sign in · 14 hard † · `Մուտք` · 5 ch
**4a** · language label · 4 hard · `ՀԱՅ` · 3 ch
**4b** · language label · 4 hard · `ENG` · 3 ch
**4c** · language label · 4 hard · `РУС` · 3 ch
**5** · skip link · 31 † · `Անցնել բովանդակությանը` · 22 ch

**6a** · footer heading · 22 hard † · `Ընկերությունը` · 13 ch
**6b** · footer heading · 22 hard † · `Ծառայություններ` · 15 ch
**6c** · footer heading · 22 hard † · `Իրավական` · 8 ch
**6d** · footer heading · 22 hard † · `Կապ` · 3 ch

**7a** · footer service link · 28 † · `Զննում — 20,000 ֏ AMD` · 21 ch
**7b** · footer service link · 28 † · `Էքսպրես — 65,000 ֏ AMD` · 22 ch
**7c** · footer service link · 28 † · `Օպտիմալ — 160,000 ֏ AMD` · 23 ch
**7d** · footer service link · 28 † · `Մաքսիմում — 200,000 ֏ AMD` · 25 ch

  ↳ The footer links carry the price because they are the only place on a
  legal page or a form page where a price appears, and the bank condition
  is "real AMD prices" in every footer. Against the original 22 the full
  `֏ AMD` format did not fit and I had dropped `AMD`; at 28 † it fits, so
  the four labels carry the canonical format and `EDITORIAL-SYSTEM.md`
  §4.3 is satisfied without an exception. This is the only place in this
  file where the re-derivation removed a compliance risk rather than a
  writing one.

**8a** · footer legal link · 30 · `Գաղտնիության քաղաքականություն` · 29 ch
**8b** · footer legal link · 30 · `Ծառայության պայմանները` · 22 ch
**8c** · footer legal link · 30 · `Վերադարձի քաղաքականություն` · 26 ch
**8d** · footer legal link · 30 · `Սահմանափակումներ` · 16 ch

**9** · legal-entity block · n/a · `[BLOCKED — the Armenian-registry form of the company name, the registration number and the legal address are not in any source. FINAL-CONTENT §4.1 carries both as {LEGAL_ADDRESS} and {REG_NUMBER}; CLAUDE.md says "Memory Care LLC" and FINAL-CONTENT says "MemoryCare LLC" and forbids the spaced form. These are three separate facts and I will not compose an Armenian legal line out of a contradiction. Shape it should take once supplied: «MemoryCare» ՍՊԸ · ՀՎՀՀ {REG_NUMBER} · {LEGAL_ADDRESS}, Երևան, Հայաստան]` · 508 ch

  ↳ Note for whoever fills it: Armenian company names take
  «guillemets» inside the legal line — `«MemoryCare» ՍՊԸ` — and the
  registration identifier an Armenian reader looks for is the **ՀՎՀՀ**
  (tax ID), not the word `գրանցման համար`. Both should be present if both
  exist.

**10** · copyright · 60 · `MemoryCare ՍՊԸ, Երևան, Հայաստան · © 2026` · 40 ch
**11a** · founder role · 30 † · `Գործադիր տնօրեն` · 15 ch
**11b** · founder role · 30 † · `Բիզնեսի զարգացման տնօրեն` · 24 ch
**12** · business hours · 55 · `Երևան, երկ–ուրբ 09:00–18:00 (UTC+4)` · 35 ch

  ↳ `երկ–ուրբ` and not `Երկուշաբթի–Ուրբաթ`: Armenian abbreviates weekdays
  to three letters and every Armenian reader parses it instantly. The
  UTC offset is mandatory in this string per §9.3 of the UX proposal —
  and it does real work in Armenian too, because a large part of the
  audience reading Armenian is reading it in Moscow, Los Angeles and
  Lyon.

### 5.2 The three frozen strings

These are written once and repeated verbatim. Any local variation is a
defect.

**16** · callback promise · 48 hard · `Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 43 ch

  ↳ **STRUCTURE.** The idiomatic Armenian is `մեկ աշխատանքային օրվա
  ընթացքում` — and it is 9 characters longer and breaks the 48 hard
  budget. `մեկ աշխատանքային օրում` is correct, ordinary Armenian and it
  fits. This is a genuine case where the budget chose between two right
  answers rather than forcing a wrong one.
  ↳ Armenian keeps the two verbs (`կզանգենք կամ կգրենք`) that English
  keeps, because the choice between a call and a message is the whole
  point for a reader who does not want a phone to ring at 23:40.

**17** · hours qualifier · 46 · `Երևանյան ժամեր՝ 09:00–18:00 (UTC+4)` · 35 ch
**18** · report promise · 52 hard · `Հաշվետվությունը ստանում եք այցից 48 ժամում։` · 43 ch

  ↳ `48 ժամում` rather than `48 ժամվա ընթացքում`, for the same reason as
  slot 16 and consistently with it. The two promises must sound like one
  hand wrote them, and in Armenian that means both take the short
  locative.
  ↳ Present tense `ստանում եք`, not future `կստանաք`. Armenian present
  used for a standing commitment reads as *this is how it works*; the
  future reads as *this is what we intend to do*. That difference is the
  entire trust argument of the site, and Armenian marks it in one letter.

---

## 6. Home — `/hy/`

Twelve sections, per `FINAL-REBRAND.md` §5.

### 6.1 Hero

**19** · hero overline · 44 hard † · `Խնամք, որը կարելի է ստուգել` · 27 ch
**20** · hero H1 · 56 hard † · `Գերեզմանի խնամք Երևանում՝ ամեն այցի ապացույցով` · 46 ch

  ↳ The `h1` carries the category and the city, per the strategy's SEO
  rule. In Armenian this costs nothing — the dementia-care collision is
  an **English-only** problem (`memory care` is not a term in Armenian at
  all), so the Armenian overline is freed from disambiguation duty and
  can carry the proposition instead. **↳ STRUCTURE:** the English overline
  and the Armenian overline do different jobs on purpose. Do not
  back-translate this line into English; it will look like a mistake.
  ↳ `ապացույց` (proof/evidence) is the load-bearing word of the whole
  locale and it appears here first. It is a plain, legal-register word in
  Armenian — what you bring to an argument, not what you feel.

**21** · hero standfirst · 150 hard † · `Ոմանք հեռու են, ոմանք ժամանակ չունեն։ Խումբը գնում է, մաքրում ամբողջ հողամասը և ցույց տալիս արածը։` · 98 ch

  ↳ **STRUCTURE, and the most important line in the file.** English can
  name the two reasons in the second person without accusing anybody.
  Armenian cannot: `Հեռու եք ապրում կամ ժամանակ չեք գտնում` puts the
  reader's absence in the second person and it lands as an accusation —
  precisely the failure `PROPOSAL-strategy.md` §7 and `FINAL-CONTENT`
  §2.4 forbid. So the Armenian shifts to the **third person indefinite**:
  `Ոմանք… ոմանք…` — *some are far away, some have no time*. Both reasons
  named, neither ranked, no persona addressed, and the reader is invited
  to recognise themselves rather than told which one they are.
  ↳ The second half is three verbs in a row — `գնում է, մաքրում… և ցույց
  տալիս` — because the brief's one sentence has one verb, **show**, and
  Armenian puts a verb where English would put an abstract noun.

**22a** · verification item · 30 hard † · `GPS կետը՝ գրանցված տեղում` · 25 ch
**22b** · verification item · 30 hard † · `8 լուսանկար, 2 տեսանյութ` · 24 ch
**22c** · verification item · 30 hard † · `Հաշվետվություն՝ 48 ժամում` · 25 ch

  ↳ **These three were the first casualty of the original 22 hard, and
  the desktop re-derivation to 30 saves all of them.** Worth recording
  what 22 would have cost, because it is the clearest illustration of the
  Armenian problem: the only strings that fit 22 are `GPS կետ` (7, which
  says nothing — an unqualified GPS claim is on the strategy's
  indefensible list), `Լուսանկար, տեսանյութ` (20, which drops the
  numbers, and the numbers *are* the protocol) and `48 ժամում` (9,
  dangling). Each trades the argument for four characters, on the one
  strip that carries the checkable substance on the first screen — the
  thing test 2 of the ranking criteria measures. `հաշվետվություն` is 14
  characters and appears in most strip-sized slots on this site.

**23** · CTA support line · 40 · `Առայժմ ոչ վճարում, ոչ գրանցում։` · 31 ch

  ↳ **STRUCTURE.** English is two sentences (`No payment now. No account
  needed.`). Armenian has a correlative construction — `ոչ… ոչ…` — that
  does both halves in one breath and sounds like a person rather than a
  checkbox list. Forcing two Armenian sentences here would be the tell of
  a translated page.

**HOME-7** · secondary link · n/a · `Տեսնել ամբողջական հաշվետվություն` · 32 ch

### 6.2 The report — section 2, the heaviest object on the page

**24a** · report overline · 31 † · `Ապացույցը` · 9 ch
**24b** · report H2 · 57 † · `Ահա թե ինչ է գալիս ամեն այցից հետո` · 34 ch
**24c** · report standfirst · 140 † · `Ամսաթիվ, գերեզմանոց, հողամասի համար, GPS կետ, 8 լուսանկար, 2 տեսանյութ և խմբի գրառումը։` · 87 ch

  ↳ The standfirst is a **list, not a sentence**, and that is deliberate:
  it reads as an inventory, which is what the product is. Armenian
  tolerates a bare nominal list far better than English does — a
  verb-first sentence here would soften it.

**25a** · annotation · GPS · 90 · `GPS կետը գրանցվում է հենց հողամասի մոտ, այցի օրը։ Այն ապացուցում է, որ խումբն այնտեղ է եղել։` · 92 ch ⚠ OVER
**25b** · annotation · timestamps · 90 · `Ամեն լուսանկար կրում է իր ժամը։ Չորս անկյուն մինչև աշխատանքը, նույն չորսը՝ հետո։` · 80 ch
**25c** · annotation · condition · 90 · `Խմբի գրառումը՝ ինչ արվեց, ինչ նկատվեց քարի վրա և ինչ է պետք հաջորդ անգամ։` · 73 ch

  ↳ **25a is the GPS-as-verification string and it is the one sentence
  on the site that must not be trimmed.** `PROPOSAL-strategy.md` §2.2
  requires the point be said as *verification*, never as *location*, and
  Armenian needs both clauses to do that: the first says where and when
  it is recorded, the second says what it therefore proves. Cut the
  second clause and the line becomes `we have GPS`, which is the
  competitor's claim. It is 6 over a soft 90; the annotation is a side
  callout with room. If a hard ceiling is imposed, the sentence that
  survives is the second one, not the first.
  ↳ `հենց` — an Armenian particle with no clean English equivalent,
  meaning *right there, precisely there*. It is doing the work that
  English does with italics on *at the plot*.

**26** · report link · 31 † · `Ամբողջ հաշվետվությունը` · 22 ch

### 6.3 How it works — three steps

**27a** · step label · 20 hard † · `Զանգ` · 4 ch
**27b** · step label · 20 hard † · `Այց` · 3 ch
**27c** · step label · 20 hard † · `Հաշվետվություն` · 14 ch

  ↳ **STRUCTURE.** English is `Plan · Visit · Report`. Armenian has no
  usable one-word noun for *plan* in this sense — `պլան` is a Russian
  borrowing that means a document, `ծրագիր` means a programme or a piece
  of software, and `պայմանավորվածություն` is 20 characters. So the
  Armenian triple starts at `Զանգ` — *a call* — which is also more
  truthful: the first step is a conversation, not a plan, and the site's
  primary CTA is a consultation request precisely because of that. The
  three Armenian words are 4, 3 and 14 characters and read as a rhythm.

**28a** · step line · 80 · `Խոսում ենք, գտնում ենք հողամասը և պայմանավորվում այցերի մոտավոր շաբաթների շուրջ։` · 80 ch
**28b** · step line · 80 · `Խումբը գալիս է սարքավորումով և մաքրում ամբողջ հողամասն ու բոլոր քարերը։` · 71 ch
**28c** · step line · 80 · `48 ժամում հաշվետվությունը հայտնվում է ձեր անձնական էջում։` · 57 ch

  ↳ 28a says `մոտավոր շաբաթների շուրջ` — *around the approximate weeks* —
  and not a date, because `PROPOSAL-ux.md` and the weather rule both
  forbid promising a day. It lands on exactly 80 with the hedge intact,
  which is luck rather than skill; the shorter version that drops
  `մոտավոր` promises more than we can keep and must not be substituted
  if the string is ever re-edited.

**HOME-18/19** — the two frozen promises, slots 16 and 18 verbatim, with
slot 17 beside slot 16. No local variation.

**HOME-20** · link · n/a · `Ամբողջ ընթացակարգը` · 18 ch

### 6.4 What a visit includes · what we do not do

**29** · method H2 · 57 † · `Ինչ է անում խումբը մեկ այցի ընթացքում` · 37 ch

**30a-l** · method label · 28 † · `Սարքավորումը` · 12 ch
**30a-b** · method line · 120 † · `Գոլորշու գեներատոր, Kärcher, փոշեկուլ՝ քարի և հողամասի ամբողջ մակերեսին։` · 72 ch
**30b-l** · method label · 28 † · `Միջոցները` · 9 ch
**30b-b** · method line · 120 † · `Միջոցն ընտրում ենք քարի տեսակով՝ գրանիտ, բազալտ, տուֆ։ Սպիտակեցնող չենք օգտագործում։` · 84 ch
**30c-l** · method label · 28 † · `Խումբը` · 6 ch
**30c-b** · method line · 120 † · `Ձեր հողամասն ամրագրված է որոշակի խմբի։ Այցից այց նույն մարդիկ գիտեն, թե ինչ են թողել։` · 85 ch
**30d-l** · method label · 28 † · `Գրանցումը` · 9 ch
**30d-b** · method line · 120 † · `Այցը փակվում է միայն այն բանից հետո, երբ կան 8 լուսանկարը, 2 տեսանյութը և GPS կետը։` · 83 ch

  ↳ `Միջոցները` and not `Քիմիան`: Armenian `քիմիա` is the school subject.
  `Մաքրող միջոց` is what a professional calls the product, and
  `մասնագիտական քիմիա` — the literal rendering of the brief's
  "professional chemistry" — reads in Armenian as a phrase from a safety
  data sheet.
  ↳ 30c is worded as an **assignment** (`ամրագրված է որոշակի խմբի`) and
  never as an unchanged roster, per 26.08 §3.4. The second sentence
  carries the benefit (they know what they left) without promising the
  same names, which is the legal trap.

**31** · `what we do not do` H3 · 39 † · `Ինչ չենք անում` · 14 ch
**32a** · limit · 70 · `Շինարարական աշխատանք չենք անում՝ պետք է քաղաքային թույլտվություն։` · 65 ch
**32b** · limit · 70 · `Տապանաքարը չենք բացում և տեղից չենք շարժում։` · 44 ch
**32c** · limit · 70 · `Փակ կամ վիճելի հատված չենք մտնում առանց ընտանիքի համաձայնության։` · 64 ch

### 6.5 Family Circle — the dark band

**33a** · eyebrow · 31 † · `Ընտանեկան շրջանակ` · 17 ch
**33b** · H2 · 52 † · `Մեկ հողամաս, մի ամբողջ ընտանիք` · 30 ch
**33c** · definition · 160 hard † · `Խնամքը հազվադեպ է մեկ մարդու որոշում, և այն չպետք է մնա մեկ մարդու փոստարկղում։` · 79 ch

  ↳ This is the strategist's sentence #4 written in Armenian rather than
  translated into it. `փոստարկղ` (letterbox) is the right image: the
  Russian and English both reach for *inbox*, and `inbox`-as-`մուտքային`
  is untranslatable jargon in Armenian, while `փոստարկղ` is a physical
  object every reader over forty has stood in front of.

**34a** · bullet · 60 · `Հրավերով ամեն հարազատ ստանում է իր մուտքը։` · 42 ch
**34b** · bullet · 60 · `Բոլորը տեսնում են նույն հաշվետվությունները։` · 43 ch
**34c** · bullet · 60 · `Ցանկացողը կարող է առանձին այց պատվիրել։` · 39 ch

**HOME-36** · link · n/a · `Ինչպես է աշխատում շրջանակը` · 26 ch

### 6.6 Trust and verification

**35-h** · H2 · 52 † · `Ինչպես ստուգել վերևում գրվածը` · 29 ch
**35a-l** · label · 30 † · `Ամսաթիվն ու կետը` · 16 ch
**35a-b** · line · 120 † · `GPS կետը գրանցվում է հողամասի մոտ, այցի օրը, ոչ թե գրասենյակում, ոչ թե հետո։` · 76 ch
**35b-l** · label · 30 † · `Անուն և հեռախոս` · 15 ch
**35b-b** · line · 120 † · `Դավիթ Համբարձումյանի և Հայկ Մանուկյանի ուղիղ բջջային համարները՝ կայքի ամեն էջում։` · 81 ch
**35c-l** · label · 30 † · `Գները՝ բացեիբաց` · 15 ch
**35c-b** · line · 120 † · `Չորս գին տպված է, հինգերորդը՝ հաշվիչով։ Բանաձևը բոլորի համար նույնն է։` · 70 ch
**35d-l** · label · 30 † · `Մեր սահմանները` · 14 ch
**35d-b** · line · 120 † · `Գրում ենք նաև այն, ինչ չենք անում, և այն, ինչ լինում է, երբ եղանակը թույլ չի տալիս։` · 83 ch

  ↳ `բացեիբաց` — *openly, in the open* — is an ordinary Armenian adverb
  and the only word here that carries any warmth. It earns its place
  because the sentence it labels is about arithmetic.

### 6.7 The honesty panel

**36** · honesty panel · 320 hard † · `Մենք սկսել ենք 2026-ին։ Առաջին հաճախորդներին ընդունում ենք հիմա։ Կարծիքներ դեռ չունենք ցույց տալու, և ուրիշինը չենք վերցնի։ Փոխարենը կա այն, ինչ կարող եք ստուգել՝ գրված ընթացակարգ, իրական հաշվետվություն, մեր անունները և ուղիղ համարները։` · 236 ch

  ↳ **STRUCTURE.** The English admits three things and then offers a
  substitute. Armenian puts the substitute in a `Փոխարենը` clause, which
  is stronger than the English `instead` because `փոխարենը` at the head
  of a sentence is emphatic — it means *here is what stands in its
  place*, and it stops the paragraph from sounding apologetic. An
  apologetic version of this paragraph is worthless; it must sound like a
  company stating its position.
  ↳ `Կարծիքներ դեռ չունենք ցույց տալու` and not `Կարծիքներ չկան` — the
  first says we have none *yet*, the second sounds like nobody has an
  opinion of us.
  ↳ Set at body size. In Armenian more than in English this paragraph
  dies if it is grey and small: at 14px in a muted colour it reads as
  legal boilerplate, which is exactly the register it must not have.

### 6.8 Founders

**37a-n** · name · 32 · `Դավիթ Համբարձումյան` · 19 ch
**37a-r** · role · 24 · `Գործադիր տնօրեն` · 15 ch
**37a-l** · line · 70 · `Պատասխանում է պայմանագրի, երաշխիքների և վճարումների հարցերին։` · 61 ch
**37b-n** · name · 32 · `Հայկ Մանուկյան` · 14 ch
**37b-r** · role · 24 · `Բիզնեսի զարգացման տնօրեն` · 24 ch
**37b-l** · line · 70 · `Առաջին զանգը սովորաբար նրանից է։ Գրում է նաև WhatsApp-ով։` · 57 ch

### 6.9 FAQ — six items, first open

**38a** · Q · 70 hard · `Ի՞նչ է լինում, եթե ձմռանը հարմար եղանակ չլինի։` · 46 ch
**39a** · A · 320 · `Քարը չենք լվանում, երբ օդի ջերմաստիճանը ցածր է +4…+10 ℃-ից կամ երբ մոտակա 48 ժամում սառնամանիք է սպասվում։ Ուրեմն ձմեռային այցը կատարում ենք այն օրերին, երբ եղանակը թույլ է տալիս։ Եթե ամբողջ ձմռանը այդպիսի օր չլինի, այցը չի կորչում՝ այն ավելանում է գարնանը։ Չորս լիարժեք այցը մնում է չորս՝ ինչ եղանակ էլ լինի։` · 309 ch

  ↳ **STRUCTURE, and worth reading before the English version is
  written.** English says *weather window*. Armenian has no such idiom;
  `եղանակային պատուհան` is a calque that a reader will parse as a
  meteorology term and distrust. The Armenian says instead
  `այն օրերին, երբ եղանակը թույլ է տալիս` — *on the days the weather
  allows* — which is what a builder in Yerevan actually says, and it
  needs no explanation. The guarantee then lands in one clause:
  `այցը չի կորչում՝ այն ավելանում է գարնանը` — *the visit is not lost, it
  is added to spring*. `չի կորչում` is the reader's own fear, named and
  answered in two words.
  ↳ The temperature is written as the protocol states it, with the
  degree sign. Numbers are the point of this answer.

**38b** · Q · 70 hard · `Հողամասի ճիշտ տեղը չգիտեմ։ Դա խնդի՞ր է։` · 39 ch
**39b** · A · 320 · `Ոչ։ Զննումը հենց դրա համար է՝ խումբը գտնում է գերեզմանոցը և հողամասը, գրանցում GPS կետը և ուղարկում վիճակի նկարագիրը՝ լուսանկարներով և տեսանյութով։ Այդ կետից հետո տեղը հայտնի է ընդմիշտ, և ամեն հաջորդ այց սկսվում է նույն կետից։ Զննումն արժե 20,000 ֏ AMD, և տարեկան բաժանորդագրություն կնքելիս այդ գումարը հաշվանցվում է։` · 317 ch

**38c** · Q · 70 hard · `Ի՞նչ է լինում, եթե խումբը չկարողանա հասնել հողամասին։` · 53 ch
**39c** · A · 320 · `Նույն օրը գրում ենք ձեզ և ասում պատճառը՝ գերեզմանոցը փակ էր, ճանապարհը փակված էր, հատվածում թաղում էր։ Ասում ենք նաև, թե որ օրը ենք վերադառնում։ Այդ այցը ձեր բաժանորդագրությունից չի հանվում։ Խմբի բացատրությունը Հայկի մոտ է՝ +374 93 154 108։` · 240 ch

  ↳ Follows `FINAL-CONTENT` §2.5 order — what happened, the date we
  return, whose subscription it does not come out of, a name and a
  number. Armenian keeps the order and drops `unfortunately`, which in
  Armenian (`ցավոք`) is even more reflexive than in English and would be
  the first word a translator wrote.

**38d** · Q · 70 hard · `Եղբայրս կարո՞ղ է տեսնել հաշվետվությունները՝ առանց վճարելու։` · 59 ch
**39d** · A · 320 · `Այո։ Ընտանեկան շրջանակը հենց դրա համար է։ Հրավեր եք ուղարկում՝ WhatsApp-ով կամ էլփոստով, և նա ստանում է իր մուտքը՝ նույն հաշվետվությունները, առանց գնի, առանց որևէ առաջարկի։ Կարող եք նաև ամեն հաշվետվություն ուղարկել սովորական հղումով՝ առանց գրանցման։ Հղումը ցանկացած պահի կարող եք չեղարկել։` · 289 ch

**38e** · Q · 70 hard · `Կարո՞ղ եմ վճարել Հայաստանից դուրս թողարկված քարտով։` · 51 ch
**39e** · A · n/a · `[BLOCKED — card acquiring with Ameriabank is not live and has no committed date; FINAL-REBRAND §6.3 records that nobody has ruled what the site may claim about services that are not yet running. The honest Armenian answer changes depending on that ruling. Placeholder shape, to be confirmed by Hayk: what payment routes exist today, whether a foreign card works today, and what the alternative is. I will not write either «այո» or «շուտով» without it — «շուտով» is on the stop-list and «այո» may be false.]` · 506 ch

**38f** · Q · 70 hard · `Ինչո՞վ համեմատել գերեզմանի խնամքի ծառայությունները։` · 51 ch
**39f** · A · 320 · `Հինգ հարց, որոնք արժե տալ ցանկացած ծառայության՝ ներառյալ մեզ։ Ի՞նչ է արվում մեկ այցի ընթացքում։ Ի՞նչ է գալիս այցից հետո և որքա՞ն ժամանակում։ Կարո՞ղ է ընտանիքի մնացած մասը տեսնել այն։ Գինը տպվա՞ծ է, թե՞ ասվում է հեռախոսով։ Ի՞նչ է լինում, եթե քարը վնասվի։ Մեր պատասխանները այս էջում են։` · 284 ch

  ↳ Built under the author's own conditions (`FINAL-REBRAND` §4.6): every
  item is a question a buyer would ask unprompted, none is reverse-
  engineered from anyone's weakness, no competitor is named or implied,
  and the first item is *what is done on one visit*, not *how many*. The
  Armenian adds `ներառյալ մեզ` — *including us* — in the first line,
  which is the sentence that keeps the whole item from reading as a
  sneer. Without it I would have cut the section, as the condition
  requires.

### 6.10 Closing form section

**40a** · form heading · 57 † · `Խոսենք՝ առանց պարտավորության` · 28 ch
**40b** · support line · 120 † · `Պատմեք գերեզմանոցի մասին, մենք կասենք՝ ինչ կանենք և որքան կարժենա։` · 66 ch

  ↳ **STRUCTURE.** English would head this `Request a free consultation`.
  Armenian heads it with a verb in the first person plural hortative —
  `Խոսենք` — *let us talk*. It is the single warmest word permitted
  anywhere on this site and it belongs here, at the one moment the page
  asks for something. A nominal Armenian heading here
  (`Անվճար խորհրդատվության հայտ`) turns the conversion into a form to be
  filled rather than a conversation to be had, which is the opposite of
  the business's own reason for using a consultation as the primary CTA.

### 6.11 The tariff strip on the home page

Four named products as four priced lines plus the Special line, per
`PROPOSAL-ux.md` §2.2 §5. The cards, the credit block and the calculator
live on `/hy/գներ/`.

**HOME-30a** · the sameness line · 70 hard · `Ամեն այց նույն լիարժեք այցն է։ Տարբերությունը միայն քանակն է։` · 61 ch

  ↳ This is slot 43 repeated verbatim on the home page. It is the line
  that replaces the volume argument the corrected pricing killed, and it
  must be one string in the system, not two.

**HOME-30b** · line · n/a · `Զննում — 20,000 ֏ AMD · մեկ այց, առանց մաքրման` · 46 ch
**HOME-30c** · line · n/a · `Էքսպրես — 65,000 ֏ AMD · մեկ լիարժեք այց` · 40 ch
**HOME-30d** · line · n/a · `Օպտիմալ — 160,000 ֏ AMD / տարի · 4 լիարժեք այց` · 46 ch
**HOME-30e** · line · n/a · `Մաքսիմում — 200,000 ֏ AMD / տարի · 6 լիարժեք այց` · 48 ch
**HOME-30f** · line · n/a · `Հատուկ խնամք — հաշվիչով, զննումից հետո` · 38 ch

  ↳ `Էքսպրես` carries `մեկ լիարժեք այց` on the same line, as ruled in §3.
  This is the enforcement point, not a stylistic choice: the word must
  never stand alone.

---

## 7. Prices — `/hy/գներ/`

**41a** · H1 · 40 · `Գերեզմանի խնամքի գները Երևանում` · 31 ch
**41b** · subhead · 90 · `Չորս գին տպված է այս էջում։ Հինգերորդը հաշվում եք ինքներդ՝ նույն բանաձևով։` · 74 ch
**42** · one-price-list line · 90 hard † · `Մեկ գնացուցակ՝ նույնը Երևանում և Լոս Անջելեսում։` · 48 ch

  ↳ Los Angeles is named because the suspicion it answers is specific: a
  diaspora buyer's first thought is that a foreign card pays a foreign
  price. Naming the city answers it faster than any sentence about
  fairness, and it names no persona — a Yerevan reader reads it as a
  statement about the company, not about themselves.

**43** · the sameness line · 100 hard † · `Ամեն այց նույն լիարժեք այցն է։ Տարբերությունը միայն քանակն է։` · 61 ch

### 7.1 The Զննում rail

**44a** · name · 28 † · `Զննում` · 6 ch
**44b** · description · 130 hard † · `Մեկ այց՝ գտնում ենք հողամասը, նկարագրում վիճակը և գնանշում աշխատանքը։ Առանց մաքրման։` · 84 ch
**44c** · CTA · 24 † · `Պատվիրել զննում` · 15 ch

  ↳ 44b sat at 84 against the original 90 hard and now has room at 130 †,
  which matters because both of its clauses are load-bearing and neither
  may be traded. `Առանց մաքրման` is the one thing `PROPOSAL-strategy.md` §6e
  says this card must state plainly, because with the light/heavy
  vocabulary gone there is nothing else stopping a reader assuming the
  Զննում includes cleaning; `գնանշում աշխատանքը` — the priced quote — is
  what the same paragraph calls the strongest thing about the product.
  Neither may be cut to make room for anything else in this slot.

**45** · one-off chip · 34 hard † · `Մեկանգամյա՝ ոչ բաժանորդագրություն` · 33 ch

  ↳ **STRUCTURE, and a loss recovered.** English fits
  `One-off · not a subscription` in 26. Armenian needs 33, because there
  is no shorter Armenian for *subscription* — `բաժանորդագրություն` is 18
  characters and has no accepted short form. Against the original 26 hard
  I had cut it to `Մեկանգամյա` (10) and lost the denial; the desktop
  re-derivation to 34 hard gives it back. Worth recording as the clearest
  single case in this file of a budget set against English costing the
  Armenian a whole clause.

### 7.2 The three cards

**46a** · product name · 22 hard · `Էքսպրես` · 7 ch
**46b** · product name · 22 hard · `Օպտիմալ` · 7 ch
**46c** · product name · 22 hard · `Մաքսիմում` · 9 ch
**46d** · product name · 22 hard · `Զննում` · 6 ch
**46e** · product name · 22 hard · `Հատուկ խնամք` · 12 ch

**47a** · unit chip · 16 hard · `Մեկանգամյա` · 10 ch
**47b** · unit chip · 16 hard · `Տարեկան` · 7 ch

  ↳ **⚠ Conflict to resolve, not mine to rule.** `PROPOSAL-ux.md` §3.3
  and the art direction specify these chips as 14px **uppercase**;
  `FINAL-CONTENT` §3.8 bans ALL CAPS in every language except the logo
  tagline. In Armenian the ban should win on typographic grounds as well
  as editorial ones: Armenian majuscules are much wider than the
  lowercase (`ՄԵԿԱՆԳԱՄՅԱ` against `Մեկանգամյա`), they lose the
  descenders that make Armenian readable at small sizes, and Ghea Mariam
  has not been checked for a designed uppercase at 14px. **Recommend
  sentence case with wide tracking** for the Armenian locale, which reads
  as a chip without shouting. §12.4.

**48** · visit-count caption · 20 hard · `լիարժեք այց տարեկան` · 19 ch

  ↳ **STRUCTURE.** Armenian does not pluralise a noun after a numeral:
  `4 այց`, not `4 այցեր`. The caption is therefore invariant across
  Express (1), Optimal (4) and Maximum (6) — one string, three cards,
  where English needs `full visit` and `full visits`. A build that
  pluralises this string in Armenian is a bug.

**49a** · pitch · Express · 56 hard · `Մեկ լիարժեք այց՝ ամբողջ հողամասը և բոլոր քարերը։` · 48 ch
**49b** · pitch · Optimal · 56 hard · `Չորս լիարժեք այց՝ մեկը յուրաքանչյուր եղանակին։` · 46 ch
**49c** · pitch · Maximum · 56 hard · `Վեց լիարժեք այց՝ տարվա ընթացքում հավասար բաշխված։` · 49 ch

  ↳ 49b is the fixed sentence the product sells on. `յուրաքանչյուր
  եղանակին` and not `ամեն սեզոնին`: `սեզոն` in Armenian is a sports
  season or a tourist season; `եղանակ` is the season of the year and is
  also the word for *weather*, which quietly ties this line to the winter
  rule three components below it. That pun is invisible and useful.
  ↳ 49c says `հավասար բաշխված` — evenly distributed — and never
  `ամսական` or anything implying a month. `Ամսական` is banned.

**50a** · season label · 10 hard · `Գարուն` · 6 ch
**50b** · season label · 10 hard · `Ամառ` · 4 ch
**50c** · season label · 10 hard · `Աշուն` · 5 ch
**50d** · season label · 10 hard · `Ձմեռ` · 4 ch

**51** · year-rail footnote · 170 hard † · `Ձմեռային այցը կատարվում է այն օրերին, երբ եղանակը թույլ է տալիս։ Եթե այդպիսի օր չլինի, այցն ավելանում է գարնանը՝ չորս այց՝ միևնույն է։` · 134 ch

  ↳ 20 over 120 hard. The English is `The winter visit runs in a
  suitable weather window. If none opens, it is added to spring — four
  visits either way.` Armenian pays for three things English gets free:
  the *weather window* idiom does not exist and must be spelled out as a
  clause (§6.9), `ավելանում է գարնանը` needs its subject, and `միևնույն
  է` is the only natural Armenian for *either way*. The shortest honest
  version is `Ձմեռային այցը կատարվում է եղանակի թույլ տված օրերին։ Եթե
  այդպիսի օր չլինի, այցն ավելանում է գարնանը։` (110) — but it drops
  *four visits either way*, which is the guarantee and the reason the
  footnote exists. At 170 † the whole sentence fits and the question is
  closed; recorded because at 120 it was not.

**52a** · arithmetic · 44 hard · `65,000 ֏ AMD · մեկ լիարժեք այց` · 30 ch
**52b** · arithmetic · 44 hard · `160,000 ֏ AMD/տարի · 4 այց · 40,000 ֏ այցը` · 42 ch
**52c** · arithmetic · 44 hard · `200,000 ֏ AMD/տարի · 6 այց · ≈33,300 ֏ այցը` · 43 ch

  ↳ `AMD` is written once per line, on the annual figure, and dropped
  from the per-visit figure. Writing it twice puts 52b and 52c at 48 and
  breaks a hard budget on the site's most important numbers. This is the
  concrete cost of the `֏ AMD` rule and it is why I contest it in §12.1.

**53** · feature lines · 54 hard each · four per card, same slot count in
all three so the rows align:

**53a1** · Express · 60 hard † · `Ամբողջ հողամասը և բոլոր տապանաքարերը` · 36 ch
**53a2** · Express · 60 hard † · `8 լուսանկար, 2 տեսանյութ, GPS կետ` · 33 ch
**53a3** · Express · 60 hard † · `Հաշվետվությունը՝ 48 ժամում, անձնական էջում` · 42 ch
**53a4** · Express · 60 hard † · `Ձեր հողամասն ամրագրված է որոշակի խմբի` · 37 ch
**53b1** · Optimal · 60 hard † · `Չորս անգամ՝ գարուն, ամառ, աշուն, ձմեռ` · 37 ch
**53b2** · Optimal · 60 hard † · `Ամեն այցը՝ ամբողջ հողամասը և բոլոր քարերը` · 41 ch
**53b3** · Optimal · 60 hard † · `Ընտանեկան շրջանակ՝ առանց լրավճարի` · 33 ch
**53b4** · Optimal · 60 hard † · `Ձեր հողամասն ամրագրված է որոշակի խմբի` · 37 ch
**53c1** · Maximum · 60 hard † · `Վեց անգամ՝ տարվա ընթացքում հավասար` · 34 ch
**53c2** · Maximum · 60 hard † · `Ամեն այցը՝ ամբողջ հողամասը և բոլոր քարերը` · 41 ch
**53c3** · Maximum · 60 hard † · `Ընտանեկան շրջանակ՝ առանց լրավճարի` · 33 ch
**53c4** · Maximum · 60 hard † · `Ձեր հողամասն ամրագրված է որոշակի խմբի` · 37 ch

**54a** · credit line · Express · 68 hard † · `60 օրվա ընթացքում ամբողջ 65,000-ը հաշվանցվում է բաժանորդագրության մեջ։` · 70 ch ⚠ OVER
**54b** · credit line · Optimal · 68 hard † · `Զննումի կամ Էքսպրեսի գումարը հաշվանցվում է այստեղ։` · 50 ch
**54c** · credit line · Maximum · 68 hard † · `Զննումի կամ Էքսպրեսի գումարը հաշվանցվում է այստեղ։` · 50 ch

  ↳ `հաշվանցվում է` — *is credited/accounted into* — and never
  `զեղչվում է`. `Զեղչ` is a discount, and `FINAL-CONTENT` §3.3 bans the
  discount register outright: this is money the client has already paid
  being carried forward, not a price being reduced. Armenian has the
  exact accounting verb and it should be used everywhere the credit is
  mentioned.

**55a** · card CTA · 24 hard † · `Ընտրել Էքսպրեսը` · 15 ch
**55b** · card CTA · 24 hard † · `Ընտրել Օպտիմալը` · 15 ch
**55c** · card CTA · 24 hard † · `Ընտրել Մաքսիմումը` · 17 ch

  ↳ Definite accusative `-ը` on each name — `Ընտրել Օպտիմալ` is
  ungrammatical Armenian. See the declension note in §3: the build must
  not treat product names as invariant tokens.

**56** · recommendation badge · 28 hard † · `Մեր խորհուրդը` · 13 ch

  ↳ Ruled in §4. Not `առաջատար`.

### 7.3 The credit block

**57a** · headline · 48 hard † · `Փոքրից սկսելը ձեզ ոչինչ չարժե։` · 30 ch
**57b** · subline · 130 hard † · `Ինչպես էլ սկսեք, առաջին տարին 160,000 ֏ AMD է և չորս լիարժեք այց։` · 65 ch

  ↳ The Armenian is a little better than the English here, and it is
  worth saying why: `ձեզ ոչինչ չարժե` uses the same verb (`արժենալ`,
  to cost) that every price on the page uses, so the headline is
  literally in the currency of the section rather than in a metaphor.

**58a** · worked line · 80 · `Ուղիղ Օպտիմալ՝ 160,000 = 160,000 ֏ AMD · 4 լիարժեք այց` · 54 ch
**58b** · worked line · 80 · `Զննում, ապա Օպտիմալ՝ 20,000 + 140,000 = 160,000 ֏ AMD · 4 այց և զննում` · 70 ch
**58c** · worked line · 80 · `Էքսպրես, ապա Օպտիմալ՝ 65,000 + 95,000 = 160,000 ֏ AMD · Էքսպրեսն առաջին այցն է` · 78 ch

**59a** · credit bullet · 80 · `Մեկ հողամասին՝ մեկ հաշվանցում, բաժանորդագրությունը կնքելու պահին։` · 65 ch
**59b** · credit bullet · 80 · `Մեկ գումար։ Եթե երկուսն էլ վճարել եք, հաշվանցվում է մեծը՝ 65,000-ը։` · 67 ch
**59c** · credit bullet · 80 · `Այցից 60 օր։ Անձնական էջում գրված է, թե որ օրն է այդ ժամկետը լրանում։` · 69 ch
**59d** · credit bullet · 80 · `Կրկնվող Էքսպրեսն էժան չէ։ Երկրորդն էլ 65,000 ֏ AMD է։` · 53 ch

**60** · credit-expiry line, portal · 46 · `Հաշվանցումը՝ մինչև 2026 թ. հոկտեմբերի 14` · 40 ch

  ↳ A plain date, never a countdown. Armenian date order is
  day–month–year and the month is lower case and in the genitive
  (`հոկտեմբերի`), which is the form a reader expects on a document. Never
  `14.10.2026` — the same argument the English stop-list makes about
  `14/09/26`.

### 7.4 Special and the calculator

**61a** · name · 28 hard † · `Հատուկ խնամք` · 12 ch
**61b** · definition · 150 hard † · `16 մ²-ից մեծ հողամասի, երկուսից ավելի քարի, ավելի հաճախակի այցերի կամ մի քանի ընտանեկան հողամասի համար։` · 103 ch
**61c** · price-floor line · 78 † · `Հատուկ խնամքի այցը երբեք Մաքսիմումի այցից էժան չէ։` · 50 ch
**61d** · entry rule · 150 hard † · `Հատուկ խնամքը միշտ սկսվում է Զննումից. գինը դնում ենք հողամասը տեսնելուց հետո, ոչ թե դրանից առաջ։` · 97 ch

  ↳ 61d uses the Armenian **միջակետ** `.` in the middle — its correct
  function, joining two clauses where English would use a colon or a
  dash. This is the mark most often replaced by a full stop in translated
  Armenian, and getting it right is most of what makes a paragraph read
  as written rather than converted.

**62a** · Special CTA · 32 hard † · `Սկսել Զննումից` · 14 ch
**62b** · Special CTA · 32 hard † · `Խորհրդատվության հայտ` · 20 ch

**63a** · calculator heading · 52 † · `Հաշվեք ձեր գինը հենց հիմա` · 25 ch
**63b** · open-formula line · 110 hard † · `Բոլորի համար նույն բանաձևը։ Հեռախոսով ոչինչ չի որոշվում։` · 56 ch

**64a** · base chip · 28 hard † · `Օպտիմալ (4 այց)` · 15 ch
**64b** · base chip · 28 hard † · `Մաքսիմում (6 այց)` · 17 ch
**64c** · base chip · 28 hard † · `Էքսպրես (1 այց)` · 15 ch

**65a** · slider label · 26 † · `Հողամասի մակերեսը` · 17 ch
**65b** · slider label · 34 hard † · `Տապանաքարերի թիվը` · 17 ch
**65c** · included caption · 34 hard † · `Մինչև 16 մ² ներառված է` · 22 ch
**65d** · included caption · 34 hard † · `Մինչև 2 քար ներառված է` · 22 ch

**66a** · result row label · 32 hard † · `Հիմքը` · 5 ch
**66b** · result row label · 32 hard † · `Մակերեսը` · 8 ch
**66c** · result row label · 32 hard † · `Տապանաքարերը` · 12 ch
**66d** · result row label · 32 hard † · `Ընդամենը՝ տարեկան` · 17 ch

**67** · default state · 65 hard † · `Ստանդարտ հողամաս՝ 160,000 ֏ AMD։ Հավելավճար չկա։` · 48 ch
**68** · ceiling state · 110 hard † · `Սրանից մեծի գինը դնում ենք առանձին՝ Զննումից հետո, երբ խումբը տեսել է հողամասը։` · 79 ch
**69a** · rate explanation · 110 · `160,000 ֏ ÷ 16 մ² = 10,000 ֏ քառակուսի մետրի համար՝ տարեկան։ Ավելացած մետրն արժե ճիշտ այնքան, որքան ներառվածը։` · 110 ch
**69b** · rate explanation · 110 · `Մեկանգամյա այցի հավելավճարը տարեկանի քառորդն է՝ մեկ այց չորսի փոխարեն։` · 70 ch
**70a** · aria-valuetext · 30 · `24 քառակուսի մետր` · 17 ch
**70b** · aria-valuetext · 30 · `3 տապանաքար` · 11 ch

  ↳ `aria-valuetext` is read aloud, so it spells `քառակուսի մետր` in
  full rather than `մ²`, which a screen reader would render as
  `մ երկու`. Same reason the English spells `square metres`.

**71** · ritual row · n/a · `[BLOCKED — flowers and a candle are an explicit owner instruction of 26.08 §7.5 for this page, and no source gives either a price. FINAL-REBRAND §6.1 and PROPOSAL-ux §12.1 both record it as blocking. Armenian strings drafted and held: heading «Ավելացնել ցանկացած այցի», items «Ծաղիկներ» / «Մոմ», line «Դնում ենք այցի ընթացքում և ցույց տալիս լուսանկարում։» — the price field stays empty until Davit sets it.]` · 407 ch

**72** · payment term · 50 hard † · `Վճարվում է մեկ անգամ՝ տարվա համար։` · 34 ch

  ↳ Stated plainly and not apologised for, per §3.8 of the UX proposal.
  Armenian resists the temptation better than English does: there is no
  natural Armenian softener here that is not on the stop-list.

### 7.5 Guarantees

**73a** · guarantee name · 30 · `Կրկնակի այց՝ 7 օրվա ընթացքում` · 29 ch
**74a** · remedy · 120 · `Եթե հաշվետվությունը ձեզ չբավարարի, գրեք 7 օրվա ընթացքում՝ հաշվետվությունն ստանալու օրվանից։ Վերադառնում ենք և անում ենք նորից՝ մեր հաշվին։` · 138 ch ⚠ OVER

  ↳ The seven days run **from the delivery of the report**, not from the
  visit (26.08 §7.1), and the Armenian says so explicitly because
  `7 օրվա ընթացքում` alone would be read against the visit date. That
  clause is why the line is over budget; it is the substance of the
  guarantee.

**73b** · guarantee name · 30 · `Պատասխանատվություն վնասի համար` · 30 ch
**74b** · remedy · n/a · `[BLOCKED — 26.08 §7.2 requires this stated as a figure with a policy reference, and PROJECT-MEMORY-FULL §9 still shows liability and worker insurance open. FINAL-REBRAND §6.2 assigns it to the lawyer. The Armenian word «ապահովագրված» alone is explicitly not acceptable, and a guarantee we cannot honour is worse than none.]` · 323 ch

**73c** · guarantee name · 30 · `Համաչափ վերադարձ` · 16 ch
**74c** · remedy · 120 · `Չեղարկելիս վերադարձնում ենք չկատարված այցերի բաժինը՝ հաշված ձեր իրական վճարած գումարից, կլորացված հօգուտ ձեզ։` · 109 ch

  ↳ `հօգուտ ձեզ` — *rounded in your favour* — is the clause that makes
  this a guarantee rather than a policy, and it is short enough in
  Armenian to keep.

**75** · payment-reality line · n/a · `[BLOCKED — depends on the same unruled question as slot 39e: what the site may say today about card payment. FINAL-REBRAND §6.3. Shape once ruled: which routes work now, no date promised for the ones that do not.]` · 213 ch

### 7.6 Pricing FAQ

**76a** · Q · 70 · `Գները տարբերվո՞ւմ են արտերկրի հաճախորդների համար։` · 49 ch
**76a-A** · A · 300 · `Ոչ։ Գնացուցակը մեկն է՝ նույնը Երևանում ապրողի և Լոս Անջելեսում ապրողի համար։ Հեռավորության համար հավելավճար չկա, և արժույթի փոխարկումից բացի ուրիշ տարբերություն չկա։ Ցանկացած գումար դոլարով կամ եվրոյով մոտավոր է. հաշիվը միշտ դրամով է։` · 234 ch

**76b** · Q · 70 · `Երկրորդ Էքսպրեսն ավելի է՞ժան է։` · 31 ch
**76b-A** · A · 300 · `Ոչ։ Էքսպրեսը միշտ 65,000 ֏ AMD է՝ և առաջինը, և երրորդը։ Կրկնվող այցի համար էժան գին չկա, որովհետև դա կնվազեցներ այն, ինչ բաժանորդագրություն վերցրածն արդեն վճարել է։ Եթե այցերը հաճախակի են պետք, բաժանորդագրությունն ավելի էժան է՝ Օպտիմալում մեկ այցն արժե 40,000 ֏։` · 262 ch

**76c** · Q · 70 · `Ի՞նչ է լինում, եթե ձմռանը հարմար օր չլինի։` · 42 ch
**76c-A** · A · 300 · `Այցը չի կորչում. այն ավելանում է գարնանը, և գարնանը լինում է երկու այց։ Չորս լիարժեք այցը մնում է չորս։ Սա պայմանագրի կետ է, ոչ թե բացառություն, և գրված է նաև ծառայության պայմաններում։` · 184 ch

**76d** · Q · 70 · `Ի՞նչ է ներառված 16 մ²-ի մեջ։` · 28 ch
**76d-A** · A · 300 · `Մինչև 16 մ² հողամաս և մինչև 2 տապանաքար՝ սա ստանդարտ ծավալն է, և ներսում գինը չի փոխվում։ Դրանից դուրս գործում է բացված բանաձևը՝ 10,000 ֏ տարեկան ամեն ավելորդ մետրի, 30,000 ֏ տարեկան ամեն ավելորդ քարի համար։ Հաշվիչը այս էջում է։` · 228 ch

**76e** · Q · 70 · `Ե՞րբ է հաշվառվում Զննումի կամ Էքսպրեսի գումարը։` · 47 ch
**76e-A** · A · 300 · `Տարեկան բաժանորդագրություն կնքելու պահին, եթե այցից անցել է 60 օրից պակաս։ Հաշվառվում է մեկ գումար՝ երկուսից մեծը։ Զննումի 20,000-ը Էքսպրեսի մեջ չի հաշվառվում. այն հաշվանցվում է միայն բաժանորդագրության մեջ։` · 206 ch

**76f** · Q · 70 · `Կարո՞ղ եմ վճարել մաս-մաս։` · 25 ch
**76f-A** · A · 300 · `Ոչ։ Բաժանորդագրությունը վճարվում է մեկ անգամ՝ ամբողջ տարվա համար։ Ամսական և սեզոնային վճարում չենք առաջարկում, և դա մեր որոշումն է, ոչ թե ժամանակավոր վիճակ։ Եթե տարեկան գումարը հիմա հարմար չէ, սկսեք Զննումից կամ Էքսպրեսից՝ վճարածը հետո հաշվանցվում է։` · 250 ch

  ↳ The last sentence turns a refusal into the trust ladder, which is the
  only honest way to publish this one. The owner rejected instalments and
  the client council recorded it as the remaining friction for the older
  local buyer; this is that buyer's answer.

---

## 8. How it works — `/hy/ինչպես-է-աշխատում/`

**77a** · H1 · 40 · `Ինչպես է աշխատում` · 17 ch
**77b** · standfirst · 100 · `Առաջին զանգից մինչև այն հաշվետվությունը, որը բացում եք ձեր հեռախոսում։` · 70 ch

**78** · timeline, four steps — number label 14, heading 30, body 220:

**78a-n** · step number · 20 † · `Քայլ 1` · 6 ch
**78a-h** · step heading · 39 † · `Խոսակցություն` · 13 ch
**78a-b** · step body · 286 † · `Ասում եք՝ որ գերեզմանոցը, մոտավորապես որտեղ է հողամասը և ով կա ընտանիքում։ Մենք ասում ենք՝ ինչ կներառի այցը և որքան կարժենա։ Այս զանգին ոչինչ չի ստորագրվում։ Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 201 ch

**78b-n** · step number · 20 † · `Քայլ 2` · 6 ch
**78b-h** · step heading · 39 † · `Գտնում և գրանցում ենք` · 21 ch
**78b-b** · step body · 286 † · `Առաջին այցին խումբը գտնում է հողամասը և գրանցում նրա GPS կետը, ապա անում է ամբողջ աշխատանքը։ Քարի ու տնկիների վիճակը գրվում է այնպես, ինչպես գտել ենք, որպեսզի ամեն հաջորդ հաշվետվություն համեմատելի լինի առաջինի հետ։` · 214 ch

**78c-n** · step number · 20 † · `Քայլ 3` · 6 ch
**78c-h** · step heading · 39 † · `Այցերի տարին` · 12 ch
**78c-b** · step body · 286 † · `Բաժանորդագրությունը գործում է 12 ամիս՝ կնքելու օրվանից։ Օպտիմալը չորս լիարժեք այց է՝ մեկը յուրաքանչյուր եղանակին։ Մաքսիմումը՝ վեց այց տարվա ընթացքում։ Մոտավոր շաբաթները պայմանավորվում ենք ձեզ հետ, ամեն ամսաթիվը հաստատում ենք անձնական էջում։` · 240 ch

**78d-n** · step number · 20 † · `Քայլ 4` · 6 ch
**78d-h** · step heading · 39 † · `Այցը և հաշվետվությունը` · 22 ch
**78d-b** · step body · 286 † · `Ամբողջ հողամասը և բոլոր տապանաքարերը։ Այցից 48 ժամում անձնական էջում հայտնվում է հաշվետվությունը՝ լուսանկարներ գալու պահին և աշխատանքից հետո, տեսանյութ, GPS կետ, ամսաթիվ և խմբի անունը։ Կարող եք ուղարկել սովորական հղումով՝ ընտանիքին գրանցում պետք չէ։` · 249 ch

**79** · what a full visit includes, eight items, 60 each:

**79a** · included item · 78 † · `Տապանաքարի և պատվանդանի մաքրում` · 31 ch
**79b** · included item · 78 † · `Եզրաքարերի, արահետների և հողամասի մակերեսի մաքրում` · 50 ch
**79c** · included item · 78 † · `Առկա տնկիների կարգի բերում` · 26 ch
**79d** · included item · 78 † · `Աղբի, տերևների և հին ծաղիկների հեռացում` · 39 ch
**79e** · included item · 78 † · `Աշխատանքից հետո ամբողջ մակերեսի ողողում` · 39 ch
**79f** · included item · 78 † · `Լուսանկարներ գալու պահին և աշխատանքից հետո` · 42 ch
**79g** · included item · 78 † · `Ամբողջ հողամասի տեսանյութ` · 25 ch
**79h** · included item · 78 † · `GPS կետ՝ գրանցված հողամասի մոտ` · 30 ch

**80** · what we do not do, four items, 70 each:

**80a** · limit · 70 · `Քարի վերականգնում կամ նորոգում` · 30 ch
**80b** · limit · 70 · `Տառերի վերափորագրում կամ ոսկեզօծում` · 35 ch
**80c** · limit · 70 · `Նոր տնկիներ և ծաղիկների տնկում` · 30 ch
**80d** · limit · 70 · `Այն, ինչ պահանջում է քաղաքապետարանի կամ վարչության թույլտվություն` · 65 ch
**80-link** · link · n/a · `Ամբողջ ցանկը՝ սահմանափակումների էջում` · 37 ch

**81** · weather and access · 420 hard · `Քարը չենք լվանում, երբ օդի ջերմաստիճանը ցածր է +4…+10 ℃-ից կամ երբ մոտակա 48 ժամում սառնամանիք է սպասվում։ Սառը քարի վրա ջուրը սառչում է ծակոտիների մեջ և պատռում մակերեսը՝ վնասը երևում է ոչ թե նույն օրը, այլ երկու տարի հետո։ Դրա համար ձմեռային այցի օրը նախապես չենք խոստանում. այն կատարում ենք այն օրերին, երբ եղանակը թույլ է տալիս, և ամսաթիվը հաստատում ենք անձնական էջում մի քանի օր առաջ։ Եթե ամբողջ ձմռանը այդպիսի օր չլինի, այցը չի կորչում և չի փոխարինվում ուրիշ բանով՝ այն ավելանում է գարնանը, և գարնանը լինում է երկու այց։ Չորս լիարժեք այցը մնում է չորս՝ ինչ եղանակ էլ լինի։ Սա պայմանագրի կետ է։` · 599 ch ⚠ OVER

  ↳ The order the brief requires — temperature limit, then the window,
  then the added-to-spring guarantee — is kept exactly. The Armenian adds
  one clause the English brief does not have: **why** the temperature
  limit exists (water freezing in the pores and splitting the surface).
  It is there because without it the limit reads as an excuse, and with
  it the paragraph reads as the one thing on the site nobody would invent
  — which is the strategist's own argument for publishing it. That clause
  is most of the overage; my recommendation is to raise the budget rather
  than cut it. §11.1.
  ↳ `չի կորչում և չի փոխարինվում ուրիշ բանով` — *is not lost and is not
  substituted with something else* — answers the second fear, which the
  English does not address: an Armenian reader assumes a missed service
  gets swapped for a lesser one.

**82** · over-cleaning line · 130 · `Այն քարը, որին գոլորշի պետք չէ, գոլորշով չենք մշակում։ Չափից ուժեղ մաքրումը փչացնում է քարը, և դա անդառնալի է։` · 110 ch

  ↳ **STRUCTURE.** English puts the object last; Armenian fronts it
  (`Այն քարը, որին…`) because the sentence is a promise about restraint
  and Armenian marks restraint by naming the thing you are not doing
  first. This also reads as the local buyer's own knowledge being
  acknowledged — Yerevan readers have seen stone ruined by wire brushes
  and bleach, and this line is written for them without saying so.

**83** · assigned crew · 75 hard † · `Ձեր հողամասն ամրագրված է որոշակի խմբի։` · 38 ch
**84** · first visit · 220 · `Առաջին այցը սովորական այց չէ միայն այն պատճառով, որ դրանից է սկսվում ամեն ինչ՝ GPS կետը, վիճակի նկարագիրը, համեմատության ելակետը։ Աշխատանքի ծավալով այն նույնն է, ինչ մյուսները՝ ամբողջ հողամասը և բոլոր քարերը։` · 208 ch

  ↳ Never described as a survey. Only Զննում is a survey, and in Armenian
  that distinction is carried by one word — `զննում` versus `այց` — so it
  is easy to keep and easy to break. A line that called this
  `առաջին զննումը` would collapse two products into one.

---

## 9. Sample report — `/hy/հաշվետվություն/`

**85a** · H1 · 40 · `Հաշվետվության նմուշ` · 19 ch
**85b** · one-line header · 90 · `Ահա թե ինչ է գալիս ամեն այցից հետո։ Այստեղ ոչինչ դեկորատիվ չէ։` · 62 ch

**86a** · block label · 30 hard † · `Հաստատում` · 9 ch
**86b** · block label · 30 hard † · `GPS կետ` · 7 ch
**86c** · block label · 30 hard † · `Գալու պահին` · 11 ch
**86d** · block label · 30 hard † · `Աշխատանքից հետո` · 15 ch
**86e** · block label · 30 hard † · `Խմբի գրառումը` · 13 ch
**86f** · block label · 30 hard † · `Հաջորդ այցը` · 11 ch

  ↳ `Գալու պահին` / `Աշխատանքից հետո` and not `Մինչև` / `Հետո`. The
  bare pair is the before/after slider's vocabulary, and the design
  package forbids that component precisely because the pair invites a
  judgement about the family. `Գալու պահին` — *at the moment of arrival*
  — describes when the photograph was taken, not what state anything was
  in, and it is chronological rather than evaluative.

**87a** · annotation · 130 · `Առաջին տողը պարզ հաստատում է՝ ամսաթիվ, գերեզմանոց, հատված, հողամաս։ Այցը եղել է, և ահա երբ։` · 91 ch
**87b** · annotation · 130 · `GPS կետը գրանցվում է հողամասի մոտ, այցի օրը։ Այն պատասխանում է մեկ հարցի՝ խումբը կանգնա՞ծ է եղել այնտեղ։` · 104 ch
**87c** · annotation · 130 · `Չորս անկյուն գալու պահին և նույն չորս անկյունը աշխատանքից հետո՝ ութ լուսանկար, նույն կետերից, որ համեմատելի լինեն։` · 114 ch
**87d** · annotation · 130 · `Երկու տեսանյութ՝ 20–40 վայրկյան։ Խմբի գրառումը վերջում՝ ինչ արվեց և ինչ է պետք հաջորդ անգամ։` · 92 ch

  ↳ 87b is the site's second GPS-as-verification string and it is the
  sharper of the two: Armenian can put the whole question inside the
  sentence with `՞` on the participle — `կանգնա՞ծ է եղել` — and no
  English construction is that compact. **↳ STRUCTURE:** do not
  back-translate; English needs a separate clause to ask it.

**88** · link-preview explainer · 200 · `Հաշվետվությունը կարող եք ուղարկել հղումով՝ WhatsApp-ով կամ Viber-ով։ Ստացողին գրանցում պետք չէ։ Զրույցի նախադիտման մեջ ոչ լուսանկար կա, ոչ անուն՝ միայն ամսաթիվը և գերեզմանոցը, որովհետև այդ էկրանը մերը չէ։` · 204 ch ⚠ OVER

  ↳ The last clause — *because that screen is not ours* — is the whole
  privacy argument in five words and it is the reason the rule exists. An
  Armenian family group chat is exactly where this link lands.

**89a** · delivery question · 104 † · `Ինչպե՞ս ուղարկենք հաշվետվությունները, և ուզո՞ւմ եք իմանալ այցից առաջ։` · 69 ch
**89b** · checkbox · 75 hard † · `Ուղարկեք հղումով, որ կարողանամ փոխանցել ընտանիքին` · 49 ch
**89c** · checkbox · 75 hard † · `Զանգահարեք կամ գրեք այցից մեկ օր առաջ` · 37 ch
**89d** · checkbox · 75 hard † · `Այցից առաջ տեղեկացրեք ուրիշին՝ Երևանում` · 39 ch

  ↳ 89b is default on, 89c default off, per 26.08 §3.5. The Armenian for
  89c is written as an instruction from the reader to us
  (`Զանգահարեք…`), not as a description of a setting, because a
  checkbox that reads as a description is ambiguous about which state is
  which.

---

## 10. About, Contacts, 404, 500, and the form

### 10.1 About — `/hy/մեր-մասին/`

**96a** · opening paragraph · 400 · `MemoryCare-ը Երևանում գրանցված ընկերություն է, որը խնամում է ընտանեկան գերեզմանները քաղաքի գերեզմանոցներում և ամեն այցից հետո ուղարկում է հաշվետվություն՝ լուսանկարներով, տեսանյութով և հողամասի մոտ գրանցված GPS կետով։ Աշխատում ենք բաժանորդագրությամբ՝ տարվա մեջ չորս կամ վեց լիարժեք այց, և առանձին այցերով։ Ամեն այց լիարժեք է. ամբողջ հողամասը և բոլոր տապանաքարերը, ոչ թե շրջայց։` · 376 ch

**96b** · opening paragraph · 400 · `Ընկերությունը հիմնադրվել է 2026 թվականին, և առաջին հաճախորդներին ընդունում ենք հիմա։ Կարծիքներ դեռ չունենք ցույց տալու։ Ունենք գրված ընթացակարգ, տպված գներ, ուղիղ հեռախոսահամարներ և երաշխիքներ, որոնք գումար են արժենում մեզ, ոչ թե ձեզ։ Այս էջում գրված ամեն թիվ կարող եք ստուգել՝ կամ հաշվետվության մեջ, կամ պայմանագրում։` · 318 ch

**97** · why it exists · 300 · `Երևանում գերեզման խնամելը դժվար չէ։ Դժվարը իմանալն է, որ դա իսկապես արվել է։ Ընկերությունը սկսվեց այդ հարցից՝ ոչ թե «ո՞վ կմաքրի», այլ «ինչպե՞ս իմանամ»։ Դրա համար ամեն այցի հետևում կանգնած է գրված ընթացակարգ՝ 8 լուսանկար, 2 տեսանյութ, մեկ GPS կետ, և առանց դրանց այցը փակված չի համարվում։` · 286 ch

  ↳ **STRUCTURE, and the paragraph I would keep if I could keep one.**
  The Armenian is built on a contrast Armenian makes naturally with two
  short clauses (`Դժվար չէ… Դժվարը… է`) and English cannot do without
  extra words. It also states the company's reason as a question a person
  actually asks, in quotation marks, in the reader's own voice — which is
  as close to a story as this brand is allowed to come, and it contains
  no adjective at all.

**98a** · method item · 120 · `Սարքավորումը՝ գոլորշու գեներատոր, Kärcher, փոշեկուլ։ Ոչ մետաղյա խոզանակ, ոչ սպիտակեցնող։` · 88 ch
**98b** · method item · 120 · `Միջոցն ընտրվում է քարով՝ գրանիտը, բազալտը և տուֆը նույն կերպ չեն մշակվում։` · 74 ch
**98c** · method item · 120 · `Ամեն այց փակվում է գրանցումով՝ 8 լուսանկար, 2 տեսանյութ, GPS կետ։ Առանց դրանց այցը փակված չէ։` · 93 ch

**About · legal block** — `[BLOCKED — same three missing facts as slot 9. The About page is one of the eight Ameriabank conditions and it cannot be submitted without the entity name, the ՀՎՀՀ and the legal address.]`

### 10.2 Contacts — `/hy/կապ/`

**99** · hours block · 120 · `Երևան, երկուշաբթի–ուրբաթ 09:00–18:00 (UTC+4)։ Երկու համարն էլ ընդունում են WhatsApp և Viber։` · 92 ch
**100** · map placeholder · 78 † · `Քարտեզը կավելացվի հասցեն հաստատվելուց հետո` · 42 ch

  ↳ Visibly a placeholder, per FINDINGS #14 — it must not be styled to
  look like a map that failed to load.

### 10.3 The consultation form

**101a** · heading · 44 · `Անվճար խորհրդատվություն` · 23 ch
**101b** · support line · 90 · `Երեք դաշտ։ Ոչ վճարում, ոչ գրանցում։ Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 79 ch

**102a** · field label · 32 hard † · `Անուն` · 5 ch
**102b** · field label · 32 hard † · `Հեռախոս կամ էլփոստ` · 18 ch
**102c** · field label · 32 hard † · `Գերեզմանոց կամ քաղաք` · 20 ch
**102d** · field label · 32 hard † · `Ավելացնել նշում` · 15 ch
**102e** · field label · 32 hard † · `Համաձայնություն` · 15 ch

**103a** · helper · 91 † · `Ինչպես ձեզ դիմել։ Ազգանունը պարտադիր չէ։` · 40 ch
**103b** · helper · 91 † · `Գրեք այնպես, ինչպես հարմար է։ Կհասկանանք։` · 41 ch
**103c** · helper · 91 † · `Եթե չգիտեք, ընտրեք «Չգիտեմ»՝ դա նորմալ պատասխան է։` · 50 ch

  ↳ 103c matters more in Armenian than in English. A diaspora reader who
  has not been to the cemetery in nine years will not type a guess into a
  form in a language they read better than they write; `Չգիտեմ` must be
  offered as a real, unembarrassing option, and the helper says so in as
  many words.

**104** · note disclosure prompt · 140 · `Օրինակ՝ ո՞ր ժամերին է հարմար զանգել, ո՞վ է Երևանում ընտանիքից, ինչ գիտեք հողամասի մասին։ Պարտադիր չէ։` · 101 ch
**105** · consent line · 160 hard † · `Համաձայն եմ, որ տվյալներս օգտագործվեն այս դիմումին պատասխանելու համար։ Գաղտնիության քաղաքականություն։` · 101 ch

**106a** · error · 90 hard † · `Գրեք ձեր անունը՝ 2-60 նիշ։` · 26 ch
**106b** · error · 90 hard † · `Հեռախոսահամարը կամ էլփոստը դատարկ է։` · 36 ch
**106c** · error · 90 hard † · `Այս էլփոստը թերի է թվում։ Ստուգեք @-ից հետո մասը։` · 49 ch
**106d** · error · 90 hard † · `Այս համարը երկրի ծածկագրին չի համապատասխանում։` · 46 ch
**106e** · error · 90 hard † · `Համարը կարճ է թվում։ Ստուգեք նիշերի քանակը։` · 43 ch
**106f** · error · 90 hard † · `Ընտրեք գերեզմանոցը կամ քաղաքը, կամ նշեք «Չգիտեմ»։` · 49 ch
**106g** · error · 90 hard † · `Նշումը 500 նիշից երկար է։ Կարճացրեք կամ զանգեք մեզ։` · 51 ch
**106h** · error · 90 hard † · `Առանց համաձայնության չենք կարող պահել տվյալները։` · 48 ch
**106i** · error · 90 hard † · `Այս դաշտը դեռ լրացված չէ։` · 25 ch

  ↳ No `Սխալ`, no `Անվավեր`, no `Պարտադիր դաշտ` — the Armenian
  equivalents of the banned interface words, and all three are the
  default output of every Armenian form library. Each message says what
  to do next. `106i` replaces `Required field` and is the one string most
  likely to be silently reintroduced by a framework.

**107** · error summary heading · 78 † · `Երկու բան դեռ լրացված չէ` · 24 ch

  ↳ **STRUCTURE.** Armenian numerals agree with nothing, so this string
  can be templated as `{n} բան դեռ լրացված չէ` with no plural forms at
  all — where English needs `1 thing` / `2 things` and Russian needs
  three forms. Worth telling the build: the Armenian locale needs no
  plural rules on this string.

**108a** · submit · 26 hard † · `Ուղարկել հայտը` · 14 ch
**108b** · sending · 18 hard † · `Ուղարկվում է…` · 13 ch

**109a** · success heading · 52 † · `Շնորհակալություն, {name}։` · 25 ch
**109b** · promise echo · frozen † · `Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 43 ch
**109c** · who will call · 143 † · `Հայկը սովորաբար առաջինը գրում է WhatsApp-ով՝ +374 93 154 108, և զանգում է, եթե այդպես եք նախընտրում։` · 100 ch
**109d** · next action · 31 † · `Տեսնել հաշվետվություն` · 21 ch
**109e** · next action · 31 † · `Ինչպես է աշխատում` · 17 ch

  ↳ 109b breaches its 16-18 budget by design: it is slot 16, frozen, and
  frozen strings do not get a shorter local variant. The budget in
  `PROPOSAL-ux.md` §10 for 109 appears to describe a label, not the
  promise; `EDITORIAL-SYSTEM.md` §3.4 marks 109's second value `frozen`,
  which settles it — flagged here rather than solved by rewriting a frozen
  string.

**110a** · server failure · 169 † · `Չհաջողվեց ուղարկել։ Ձեր գրածը տեղում է՝ փորձեք նորից։ Կամ գրեք ուղիղ՝ +374 93 154 108, info@memorycare.am։` · 106 ch
**110b** · retry label · 26 † · `Փորձել նորից` · 12 ch

  ↳ No `Ինչ-որ բան սխալ գնաց`. The Armenian says what failed, that
  nothing was lost, and gives two humans to reach. This is the most
  important error on the site per §4.5 of the UX proposal.

**111a** · thank-you question · 40 · `Ինչպե՞ս իմացաք մեր մասին։` · 25 ch
**111b-g** · thank-you options · 24 each — `Որոնողական համակարգ` (19) · `Facebook կամ Instagram` (22) · `Ընկեր կամ հարազատ` (17) · `YouTube` (7) · `Գերեզմանոցում տեսա` (18) · `Այլ` (3)
**112** · country search placeholder · 40 · `Գտնել երկիրը կամ ծածկագիրը` · 26 ch
**113** · WhatsApp checkbox · 44 · `Այս համարը WhatsApp-ում է` · 25 ch

### 10.4 404 and 500

**119a** · 404 heading · 39 † · `Այս էջը չկա` · 11 ch
**119b** · 404 line · 117 † · `Հասցեն սխալ է կամ էջը տեղափոխվել է։ Ահա այն, ինչ ամենից հաճախ են փնտրում։` · 73 ch
**119c** · link · 30 † · `Գլխավոր` · 7 ch
**119d** · link · 52 † · `Գներ` · 4 ch
**119e** · link · 52 † · `Ինչպես է աշխատում` · 17 ch
**119f** · link · 52 † · `Հաշվետվության նմուշ` · 19 ch
**119g** · link · 52 † · `Կապ` · 3 ch
**119h** · phone line · 52 † · `Կամ զանգեք՝ +374 55 315 323` · 27 ch

  ↳ `Այս էջը չկա` — *this page does not exist* — and not `Էջը չի
  գտնվել`, which is the passive that hides who is at fault, and not
  `Ուպս`. Armenian 404 pages default to both.

**120a** · 500 heading · 39 † · `Խնդիրը մեր կողմում է` · 20 ch
**120b** · 500 line · 110 hard † · `Մեր կողմում ինչ-որ բան չի աշխատում։ Ձեր տվյալները տեղում են։` · 60 ch

### 10.5 Meta titles and descriptions

Category first, brand last, in every route. The Armenian has no
dementia-care collision to defend against, but the category-first rule
holds anyway because it is also how an Armenian reader scans a SERP.

**13a** · title · home · 60 hard · `Գերեզմանի խնամք Երևանում՝ ֆոտո, տեսանյութ, GPS` · 46 ch
**14a** · description · home · 155 hard · `Ընտանեկան գերեզմանի պրոֆեսիոնալ խնամք Երևանի գերեզմանոցներում։ Ամեն այցից հետո՝ 8 լուսանկար, 2 տեսանյութ, GPS կետ։ Չորս լիարժեք այց՝ 160,000 ֏ AMD տարեկան։` · 155 ch
**13b** · title · pricing · 60 hard · `Գերեզմանի խնամքի գները Երևանում` · 31 ch
**14b** · description · pricing · 155 hard · `Չորս տպված գին և բաց բանաձև՝ Զննում 20,000, Էքսպրես 65,000, Օպտիմալ 160,000, Մաքսիմում 200,000 ֏ AMD։ Հաշվիչը մեծ հողամասերի համար՝ էջում։` · 138 ch
**13c** · title · how-it-works · 60 hard · `Ինչպես է աշխատում գերեզմանի խնամքը` · 34 ch
**14c** · description · how · 155 hard · `Զանգից մինչև հաշվետվություն՝ քայլ առ քայլ։ Ինչ է ներառում լիարժեք այցը, ինչ չենք անում և ինչ է լինում, երբ ձմռանը եղանակը թույլ չի տալիս։` · 137 ch
**13d** · title · sample report · 60 hard · `Այցի հաշվետվության նմուշ՝ Երևան` · 31 ch
**14d** · description · sample · 155 hard · `Իրական հաշվետվության կառուցվածքը՝ ամսաթիվ, GPS կետ, 8 լուսանկար գալու պահին և աշխատանքից հետո, 2 տեսանյութ և խմբի գրառումը։` · 123 ch
**13e** · title · about · 60 hard · `Մեր մասին՝ գերեզմանի խնամք Երևանում` · 35 ch
**14e** · description · about · 155 hard · `Ով ենք մենք, ինչ ընթացակարգով ենք աշխատում և ինչ երաշխիք ենք տալիս։ Ընկերությունը գրանցված է Երևանում 2026 թվականին։` · 116 ch
**13f** · title · contacts · 60 hard · `Կապ՝ գերեզմանի խնամք Երևանում` · 29 ch
**14f** · description · contacts · 155 hard · `Ուղիղ համարներ, WhatsApp և Viber, աշխատանքային ժամեր երևանյան ժամանակով (UTC+4)։ Պատասխանում ենք մեկ աշխատանքային օրում։` · 120 ch
**13g** · title · 404 · 60 hard · `Այս էջը չկա՝ գերեզմանի խնամք Երևանում` · 37 ch
**14g** · description · 404 · 155 hard · `Այս հասցեով էջ չկա։ Անցեք գլխավոր էջ, գների էջ կամ զանգեք ուղիղ։` · 64 ch

**15a** · OG title · 60 · `Գերեզմանի խնամք Երևանում՝ ամեն այցի ապացույցով` · 46 ch
**15b** · OG description · 110 · `8 լուսանկար, 2 տեսանյութ և GPS կետ՝ գրանցված հողամասի մոտ։ Հաշվետվությունը՝ 48 ժամում։` · 86 ch

  ↳ `ֆոտո` appears in the home title and nowhere else on the site. It is
  there because it is what people type into an Armenian search box;
  `լուսանկար` is the correct word and is used in every human-facing
  string. A title tag is not copy, it is a query surface, and the two
  should not be held to the same rule.

---

## 11. Budgets — measured against the re-derived numbers

`EDITORIAL-SYSTEM.md` §3.4 re-derives most of `PROPOSAL-ux.md` §10 for a
desktop-only build, and §3.1 Ruling A settles that a **hard** budget is a
ceiling in every language. Both landed after most of this file was
drafted. I have re-measured every string against the **re-derived**
number where one exists and the §10 number where none does.

**The re-derivation clears most of what I was going to argue about.**
Slots 22, 44, 45, 47, 51, 78, 36, 105 and 106 all had Armenian I was
prepared to defend over budget, and every one of them now fits — slot 45
recovers the full `Մեկանգամյա՝ ոչ բաժանորդագրություն` I had been forced
to cut in half. That
is the largest single improvement to the Armenian in this round and it
came from someone else's document; it is worth saying so plainly.

**What still does not fit, after re-derivation.** Five, and each is a
different kind of problem.

| # | Slot | Budget in force | Armenian | Kind | What I propose |
|---|---|---|---|---|---|
| 11.1 | **81** weather paragraph | 420 hard, **deliberately not re-derived** (§3.4: a content-order rule, not a width) | 599 | Content, not layout | **Raise to 610.** The budget is a rule about *order* — temperature, then window, then the added-to-spring guarantee — and the Armenian keeps that order exactly. The overage is two clauses English does not need: *why* the temperature limit exists, and that the visit is not substituted with a lesser one. Cut the first and the limit reads as an excuse; cut the second and an Armenian reader assumes a swap, because that is what happens to a missed service here |
| 11.2 | **54a** Express credit line | 68 hard † (was 60) | 70 | Two characters | Raise to 72, or accept `60 օրում 65,000-ը հաշվանցվում է բաժանորդագրության մեջ։` (58) — which buys the fit by dropping `ամբողջ`, *in full*, the word the rule turns on, and by shortening the window to the locative used in the frozen promises. I would rather have the two characters. §3.5 already flags 54 as a surviving A |
| 11.3 | **74a** guarantee remedy | 120, not re-derived | 138 | Legal substance | Raise to 145. The overage is `հաշվետվությունն ստանալու օրվանից` — the clause making the seven days run from report delivery, not from the visit (26.08 §7.1). W-LEG owns the final wording; the length is not negotiable downward |
| 11.4 | **25a** GPS annotation | 90, not re-derived | 92 | Two characters | Raise to 96, or accept 2 over on a soft budget. Slot 24 was re-derived and slot 25 sits in the same component; I think 25 was simply missed and should follow 24 |
| 11.5 | **88** link-preview explainer | 200, not re-derived | 204 | Four characters | Raise to 210, or drop `Ստացողին գրանցում պետք չէ։` — the sentence the whole feature exists for |

**Three notes on budgets that fit but should not be assumed safe.**

- **53, 54, 55 — the in-card slots.** §3.5 is right that these are the
  ones people will assume the scope change fixed. It did not: a card in
  a three-up row at 1200 is about as wide as a full-bleed card was at
  360. All twelve of my feature lines fit 60, but with 2-6 characters of
  margin, and every one of them contains `այց` rather than
  `այցելություն` — which is §1.4a's ruling doing exactly the work it was
  adopted for. **If `այցելություն` is ever restored, these twelve strings
  break together.**
- **46 — product names.** Comfortable at 6-12 characters against 22
  **because** `խնամք` is dropped from three of five (§3). With `խնամք`
  restored the longest is `Մաքսիմում խնամք` at 15, which still fits —
  so the budget is not the argument for dropping it and I have not used
  it as one.
- **1 — nav, 18 hard, and §3.5 is right that desktop makes it worse.**
  My five items are 5, 17, 14, 17 and 9. Two sit two characters under
  the ceiling. This is why nav item 3 is `Հաշվետվություն` and not
  `Հաշվետվության նմուշ` (19), argued at slot 1c.

**The systemic finding, restated now that it can be checked.** Armenian's
length problem is not evenly distributed; it lives in four nouns this
business cannot avoid: `հաշվետվություն` (14), `բաժանորդագրություն` (18),
`խորհրդատվություն` (16) and `պատասխանատվություն` (18), each 1.6-2.2× its
English counterpart rather than 1.3×. Four of the five surviving
breaches above contain one of them. **A useful rule for the register:
apply ×1.3 generally and ×2.0 to any slot whose Armenian must contain
one of those four nouns.** It is mechanically checkable and it would have
predicted all five.

---

## 12. Where I disagree with a ruling

### 12.1 `֏ AMD` on the Armenian site

`FINAL-CONTENT` §4.3 freezes `160,000 ֏ AMD`, "without exception, in body
copy, in tables, in the calculator, in the portal, in email, on the
invoice and in the PDF". I have complied everywhere above. I think it is
wrong for this locale, for three reasons and with a proposal that keeps
what the rule is actually for.

1. **It is not what the currency is called in Armenian.** An Armenian
   reader knows the sign `֏` and the word `դրամ`. `AMD` is an ISO code
   used at borders and by banks. Appending it to a price on an Armenian
   page reads the way `160,000 ֏ AMD` would read to a Londoner as
   `£160,000 GBP` — not wrong, but visibly addressed to a foreigner. On
   the locale whose whole job is to not sound translated, that is a cost.
2. **It is 4 characters, and they land on hard budgets.** Slots 52b and
   52c are 44 hard, are explicitly **not** re-derived for desktop
   (`EDITORIAL-SYSTEM.md` §3.4 keeps in-card captions at their §10
   numbers), and contain two prices each. Writing `AMD` twice puts both
   over. I have written `AMD` once per line and closed the space in
   `֏ AMD/տարի`, which is already two deviations from "no exceptions" —
   made visible here rather than done quietly. **This is a request for a
   ruling, not a fait accompli:** if the editor holds the format, slots
   52b and 52c need 48 hard and that is a design change, because they are
   the two strings on the site that prove the price is arithmetic rather
   than a number.
3. **The rule's real purpose is served without it.** The purpose is the
   bank's condition that the currency be stated. That condition is met by
   the price furniture on `/hy/գներ/`, the footer, the invoice and the
   payment page.

**Proposal:** keep `֏ AMD` in every price *field* — cards, calculator,
invoice, payment, footer, schema, email — and allow `֏` alone, or the
word `դրամ`, in **running Armenian prose** on the Armenian locale only.
If the ruling stands unchanged, nothing above breaks; the four flagged
budgets do.

### 12.2 `առաջատար`

Set out in full in §4. Summarised here because it is a direct instruction
in three documents: `առաջատար` is not the Armenian for *our
recommendation*, it is the Armenian for *market leader*, and it makes on
the Armenian site precisely the claim the English site is forbidden from
making. `Մեր խորհուրդը` is what the English says. I have written that,
and this section is the notice rather than a silent substitution.

### 12.3 One script per locale, and the switcher

The rule reads in both directions in some documents. To be explicit about
what I have done: the Armenian site carries the Latin set listed in §2 and
nothing else, **and the language switcher carries `ENG` and `РУС` in
their own scripts**. A reader who has landed on the Armenian page from a
US search and cannot read Armenian must be able to recognise the way out.
Rendering those two labels in Armenian letters would be consistent and
useless.

### 12.4 The uppercase chips

Not a disagreement with a person, a collision between two
documents. It needs one ruling, and my recommendation is that the
ALL-CAPS ban wins in Armenian for typographic reasons independent of the
editorial ones.

---

## 13. What I could not verify, and what is blocked

**Blocked, with the string left empty above:**

- **9** legal-entity block, and the About legal block — entity name in
  Armenian, ՀՎՀՀ, legal address. Three separate missing facts, and
  `CLAUDE.md` and `FINAL-CONTENT` disagree on the entity name itself
  (`Memory Care LLC` against `MemoryCare LLC`). Bank condition.
- **39e** and **75** — what the site may say today about card payment.
  Unruled per `FINAL-REBRAND` §6.3. I will not write `շուտով` (banned) or
  `այո` (possibly false).
- **71** ritual row price — flowers and a candle. Owner instruction with
  no price in any source. Armenian strings drafted and held.
- **74b** liability guarantee — needs the figure and the policy
  reference from the lawyer.

**Unverified, and it affects the Armenian more than the other two
locales:**

- **Font coverage.** `Montserrat Arm` and `Ghea Mariam` are stated to
  cover Armenian, but this file uses characters beyond the basic
  alphabet: `։` U+0589, `՝` U+055D, `՞` U+055E, `և` U+0587, `֏` U+058F
  and `℃`. **`և` is the one to check first** — it is a single-code-point
  ligature that appears in roughly a third of the strings above and there
  is no acceptable fallback: writing `եւ` instead is a spelling error in
  reformed orthography. `֏` is already known to fall back (FINDINGS #21).
  A locale that renders `և` in a substitute face will look broken to
  every Armenian reader on every line.
- **Hyphenation and justification.** Armenian words in this file run to
  18 characters. No hyphenation dictionary is specified. Recommend
  `hyphens: none` and ragged-right for `hy`, and no justified text
  anywhere — justified Armenian at 18-character words produces rivers
  that make a premium page look like a photocopy.
- **Sorting and search.** The cemetery combobox (slot 3 of the form) must
  match Armenian input on Armenian names; I have assumed it does.

**Deliberately not written, because it is outside the scope I was
given:** `/hy/ընտանեկան-շրջանակ/` slots 90-95, the portal (114-118), the
bad-news and cancellation states (121-122), and the transactional email
subjects (123). The home page's Family Circle section (33-36) and the
report-sharing explainer (88) are written above and should be the source
the standalone page is written from, not the other way round — the
definition in slot 33c is the sentence that product sells on and it must
not be re-drafted in a second place.

---

## 14. Three things to hand to whoever writes the English and Russian

Not a review of their work — three findings from the Armenian that the
other two locales will hit.

1. **`Plan · Visit · Report` does not survive contact with Armenian**
   (slot 27), and the replacement — `Զանգ · Այց · Հաշվետվություն` — is
   more truthful than the original in all three languages. The first step
   is a phone call, and the site's primary CTA is a consultation request
   precisely because of that. Worth changing in English too.
2. **`Weather window` has no idiom in Armenian** (slots 51, 81, 39a) and
   the Armenian spells it out as *the days the weather allows*. That
   phrase is clearer than the English one and it is what the operations
   people actually say. The English is not obliged to follow, but should
   know it is the more figurative of the two.
3. **`֏ AMD` costs Armenian two hard budgets and Russian will hit the
   same wall** (§12.1). Slots 52b and 52c are the arithmetic lines — the
   strings that turn a premium price into a sum a reader can check — and
   they are the two in-card captions the desktop re-derivation
   deliberately did not widen. Russian's `160,000 ֏ AMD в год · 4 визита`
   has the same shape and will arrive at the same place. Worth resolving
   once, for all three, before three writers each invent a private
   abbreviation.

---

## 15. Reconciliation with `EDITORIAL-SYSTEM.md`

The editorial system landed while this file was being drafted. §1 of it
grants W-HY **one round to contest a term in writing, with a reason about
meaning or grammar and not about taste.** This is that round. Everything
not listed here I have adopted and applied above.

### 15.1 Adopted without argument

- **`այց`, not `այցելություն`** (§1.4a). Confirmed, and the editor's
  reasoning is right for a reason they could not check: `այց` is not a
  clipped or informal form of `այցելություն`, it is the ordinary noun,
  and it takes every case ending the slots need without difficulty —
  `այցից`, `այցի`, `այցով`, `4 այց`. There is no grammatical problem in
  any of the constructions used above, so the budget argument stands
  unopposed. Twelve feature lines depend on it.
- **`հաշվանցում` / `հաշվանցվում է`** for the credit. Better than the
  `հաշվառվում է` I had drafted: `հաշվառել` is *to register or record*,
  `հաշվանցել` is *to set one payment off against another*, which is
  exactly the operation. Applied throughout — slots 54, 59, 60, 39b,
  76e.
- **`տապանաքար`**, **`հաշվետվություն`**, **`բաժանորդագրություն`**,
  **`Զննում`**, **`Ընտանեկան շրջանակ`**, **`երաշխիք`**, **`հաշվիչ`**,
  **`խորհրդատվություն`** — identical to my own table at §2, arrived at
  independently, which is a good sign for both.
- **No `փաթեթ`.** The live site's `Փաթեթ 1..4` is the failure being
  removed, and the editor is right that it is the word an Armenian writer
  reaches for by reflex.
- **`֏` in its own element**, phone-number format, no exclamation marks,
  Armenian quotation marks `« »`, the all-numeric date ban, seasons named
  and never dated, `20–40` with an en dash. All applied.
- **Meta titles: the brand leaves the Armenian `<title>`** (§3.6b).
  Adopted — slots 13a-g above now end at the category and the city. The
  argument is stronger than the editor states it: an Armenian searcher
  will never type `MemoryCare`, and 12 characters of unindexable brand
  in a 60-character ceiling is 20% of the title spent on nothing.
- **Armenian dates as `2026 թ. հոկտեմբերի 14`** (§4.4). Applied at slot
  60.

### 15.2 Contested — four terms, on meaning, not taste

**a. `հողամաս`, not `տեղամաս`, for the plot. This one is an error, not a
preference.** `տեղամաս` in Armenian means a *precinct* — an
administrative district. It is the second half of `ընտրատեղամաս`
(electoral precinct) and `ոստիկանական տեղամաս` (police precinct), and
that is the association every Armenian reader has. It is not used for a
parcel of land. The word for a parcel of land, including in Armenian
cadastral and cemetery-administration usage, is **`հողամաս`**. Writing
`ձեր ընտանիքի տեղամասը` on a page about a grave will read to a Yerevan
buyer as though the copy was machine-produced. **Recommend: `հողամաս`,
with `գերեզման` for the grave itself, exactly as the editor's table
structures it.** Everything above uses `հողամաս`.

**b. `գերեզմանոց`, not `գերեզմանատուն`, for the cemetery.**
`գերեզմանոց` is the standard Eastern Armenian term, it is what the
Yerevan cemeteries are called in their own names, and it is what appears
on municipal signage and in the addresses a client will read.
`գերեզմանատուն` is a real word and is not wrong, but it is the older,
more colloquial variant, and on a site whose Armenian must not read as
approximate, the standard form is the safer one. This one I hold
loosely; the ruling matters more than which way it goes, because the
word appears in the report metadata strip on every visit.

**c. `խումբ`, not `բրիգադ`, for the crew — and I acknowledge this is the
closest call of the four.** `բրիգադ` is precise, it is genuinely what
Armenian trades call a work crew, and I can see why it was chosen: it is
the workmanlike register the English `the crew` is reaching for. Two
arguments against it. First, it is a Russian loan (*бригада*), and the
one drift the editor's own §1.4b warns about is Armenian inheriting the
company's Russian operational vocabulary without noticing — this is that
vector, in the noun that appears in every report. Second, its
contemporary Armenian associations are a construction site and, in
colloquial use, something less flattering; neither is the register of a
premium service that photographs graves. **`խումբ`** is native, neutral,
and shorter, and the editor's own ban on `թիմ` (a sports team) points
the same direction. Everything above uses `խումբ`. If the editor holds
`բրիգադ` I will not argue twice — but it should be a decision taken
knowing it is a loan.

**d. `անձնական էջ`, not `անձնական հաշիվ`, for the portal — weakest of
the four, raised because of one collision.** `հաշիվ` means *account* and
also *bill / invoice*. This site has invoices, a payment page and a
refund arithmetic, and `ձեր անձնական հաշիվը` sitting two components away
from `հաշիվ-ապրանքագիր` is a genuine ambiguity in a place where the
reader is deciding whether to trust us with money. `անձնական էջ` has no
second meaning. I have used `անձնական էջ` above; if the editor prefers
`անձնական հաշիվ` the change is mechanical and I will make it.

**e. `եղանակային պատուհան` — partial contest, and a compromise that
gives the editor what the rule is for.** The editor bans `if conditions
allow` / `при благоприятной погоде` and mandates the term. The ban is
right: a vague hedge in place of a rule is exactly the evasion this site
must not commit. But the Armenian calque is opaque — a reader meets
`եղանակային պատուհան` and parses it as meteorology, not as a term of
our contract. **Proposal: keep `եղանակային պատուհան` as the named term
wherever a term is what is needed** — the Terms document, the schedule
label in the portal — **and in the two places where the rule is
explained to a buyer (slots 51 and 81) state it as what it is**, with
the temperature attached: `+4…+10 ℃-ից ցածր չենք լվանում. ձմեռային այցը
կատարվում է եղանակի թույլ տված օրերին`. That is not a hedge — it carries
a number — and it is what the crew actually says. Slots 51 and 81 above
are written that way; the term itself is available and unbanned.

### 15.3 One conflict the editor's own rules create

**`16 մ²` or `16 m²`.** §4.3 says *"never `m2` or `кв.м` or `քմ`"* and
writes the unit as `m²` — a Latin `m`. §4.5's permitted-Latin list covers
proper nouns and technical initialisms and does not reach a unit
abbreviation. The Armenian unit is **`մ²`**, and `16 m²` on the Armenian
page is a Latin word-fragment in a locale that carries none. I have
written `մ²` throughout, including in the calculator and slot 76d, and
`քառակուսի մետր` spelled out in the two `aria-valuetext` strings, where
a screen reader would otherwise say `մ երկու`. **This needs one line of
ruling**, because it appears in the calculator, the Special card, the
pricing FAQ and the surcharge formula — four surfaces, one character.

### 15.4 Slot 50 — the Armenian month initials, solved

`EDITORIAL-SYSTEM.md` §3.4 raises a new flag: desktop-only means the year
rail carries **month initials, not season names**, and Armenian month
initials had not been looked at. They do not work, and here is why in one
line.

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Month | Հունվար | Փետրվար | Մարտ | Ապրիլ | Մայիս | Հունիս | Հուլիս | Օգոստոս | Սեպտեմբեր | Հոկտեմբեր | Նոյեմբեր | Դեկտեմբեր |
| Initial | Հ | Փ | Մ | Ա | Մ | Հ | Հ | Օ | Ս | Հ | Ն | Դ |

**Four months begin with `Հ` and two with `Մ`.** A twelve-cell rail
labelled with single Armenian initials reads `Հ Փ Մ Ա Մ Հ Հ Օ Ս Հ Ն Դ` —
six of twelve cells ambiguous, and the rail's whole job is to let a
reader see *one mark in each season*. Single initials are not available
in Armenian, and no ruling can make them available.

**Settled: three-letter lower-case abbreviations, which are the
conventional Armenian forms and are unambiguous.**

**50 (revised)** · year-rail month labels ×12 · 3 ch each — `հնվ` · `փտվ` · `մրտ` · `ապր` · `մյս` · `հնս` · `հլս` · `օգս` · `սեպ` · `հոկ` · `նոյ` · `դեկ`

  ↳ Two-letter forms (`Հն Փտ Մր Ապ Մյ Հս Հլ Օգ Սպ Հկ Նմ Դկ`) are also
  unambiguous and are the fallback if a 12-cell rail cannot hold three
  characters per cell. **Single letters are not a fallback, they are a
  defect.** If neither fits, the Armenian rail keeps the four season
  labels the mobile design used — `Գարուն · Ամառ · Աշուն · Ձմեռ`, slot
  50 as originally written above — and that is the better degradation,
  because the season is the unit Optimal is sold in and the month is not.
  ↳ Lower case is correct: Armenian month names are lower case except at
  the start of a sentence, and the live site's `Փաթեթ`-style
  capitalisation of everything is part of what is being removed.

### 15.5 The four unslotted strings, in Armenian

`EDITORIAL-SYSTEM.md` §3.7 finds strings that are mandated somewhere and
slotted nowhere. Three of them appear on pages in my scope, so here they
are rather than a note saying somebody should write them.

**NEW-1** · header descriptor, beside the logo, every page · `Գերեզմանի խնամք Երևանում` · 0 ch

  ↳ Mandated by `PROPOSAL-strategy.md` §5.4 and the content brief; it has
  no slot. In English it is a defence against the dementia-care
  collision. **In Armenian there is no collision and it does different
  work:** it is the only place on a page above the fold that says the
  category and the city together in a header a search engine reads first,
  and it lets the `h1` spend its 56 characters on the proposition. Keep
  it in Armenian for that reason, not the English one.

**NEW-2** · FX note, wherever a non-AMD figure appears · `Հաշիվը միշտ դրամով է։ Այլ արժույթով գումարը մոտավոր է։` · 0 ch

  ↳ Ameriabank condition 5, named by `FINAL-REBRAND` §4.1 as an
  unassigned one-liner. `EDITORIAL-SYSTEM.md` §4.3 requires it beside
  every foreign figure. Note that this is the one string on the Armenian
  site where **`դրամ` is the right word and `AMD` would be wrong** — the
  sentence is about which currency the client is charged in, and an
  Armenian reader is charged in `դրամ`. See §12.1.

**NEW-3** · the published protocol block, home page, after the report
section · heading + five lines:

**NEW-3h** · heading · `Ինչ պետք է լինի, որ այցը փակվի` · 0 ch
**NEW-3a** · line · `8 լուսանկար՝ չորս անկյուն մինչև աշխատանքը, նույն չորսը՝ հետո` · 0 ch
**NEW-3b** · line · `2 տեսանյութ՝ 20–40 վայրկյան, ամբողջ հողամասը` · 0 ch
**NEW-3c** · line · `1 GPS կետ՝ գրանցված հողամասի մոտ, այցի օրը` · 0 ch
**NEW-3d** · line · `Խմբի գրառումը՝ ինչ արվեց, ինչ է պետք հաջորդ անգամ` · 0 ch
**NEW-3e** · closing line · `Քանի դեռ այս ամենը չկա, այցը փակված չէ։` · 0 ch

  ↳ §3.7 is right that this is the highest-ratio trust device on the
  site and that it is currently spread thinly across slots 25 and 79
  with no block of its own. It costs nothing — it is an internal rule
  that already exists — and no competitor publishes one.
  ↳ **STRUCTURE.** The heading is not *our protocol* or *how we work*;
  it is `Ինչ պետք է լինի, որ այցը փակվի` — *what must exist before a
  visit is closed*. Armenian puts the condition first and the
  consequence second, and the closing line inverts it
  (`Քանի դեռ… չկա, այցը փակված չէ` — *as long as this does not exist,
  the visit is not closed*). The two together are the same rule stated
  from both ends, which is how a specification reads and how an
  advertisement does not.

**NEW-4** · the comparison FAQ item. Already written above as slots 38f
and 39f — `EDITORIAL-SYSTEM.md` §3.7 notes that `FINAL-REBRAND` §4.6
rules it in and that slots 38 and 76 are full at six items each. **On the
Armenian home page I have spent one of the six on it** rather than adding
a seventh, and moved *do prices differ abroad* to the pricing FAQ (76a),
where a reader asking about price is already standing. The home FAQ's six
are therefore: winter · finding the plot · the crew cannot reach it ·
family access without paying · foreign card · how to compare. That
allocation is a proposal, not a ruling; if the lead wants a seventh item
the Armenian is written and fits.
