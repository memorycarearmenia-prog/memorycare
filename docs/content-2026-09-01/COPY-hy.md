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

A budget marked **hard** must not be exceeded. Where the Armenian cannot
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
   `Խումբը գնում է հողամաս և գրանցում GPS-կետը` addresses no one and
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
| GPS point | `GPS-կետ` | `գեոպիտակ`, `կոորդինատ` | Armenian attaches suffixes to Latin abbreviations with a hyphen: `GPS-ը`, `GPS-ի`, `GPS-կետը` |
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

**2** · primary button · 22 hard · `Խորհրդատվության հայտ` · 20 ch

  ↳ Not `Անվճար խորհրդատվություն` — 23 ch, over, and "free" belongs to
  the form heading (slot 101), not to every button on the site.
  Not `Կապվել մեզ հետ` (that is `Contact us`, banned).

**3** · sign in · 12 hard · `Մուտք` · 5 ch
**4a** · language label · 4 hard · `ՀԱՅ` · 3 ch
**4b** · language label · 4 hard · `ENG` · 3 ch
**4c** · language label · 4 hard · `РУС` · 3 ch
**5** · skip link · 24 · `Անցնել բովանդակությանը` · 22 ch

**6a** · footer heading · 16 hard · `Ընկերությունը` · 13 ch
**6b** · footer heading · 16 hard · `Ծառայություններ` · 15 ch
**6c** · footer heading · 16 hard · `Իրավական` · 8 ch
**6d** · footer heading · 16 hard · `Կապ` · 3 ch

**7a** · footer service link · 22 · `Զննում — 20,000 ֏` · 17 ch
**7b** · footer service link · 22 · `Էքսպրես — 65,000 ֏` · 18 ch
**7c** · footer service link · 22 · `Օպտիմալ — 160,000 ֏` · 19 ch
**7d** · footer service link · 22 · `Մաքսիմում — 200,000 ֏` · 21 ch

  ↳ The footer links carry the price because they are the only place on a
  legal or a form page where a price appears, and the bank condition is
  "real AMD prices". `AMD` is dropped **here only**, where the string is a
  link label and the full format sits four times over on `/hy/գներ/`.
  If the bank reviewer requires it in every instance, these four go over
  budget by 4 and become a two-line link block — flagged, §11.

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
**11a** · founder role · 24 · `Գործադիր տնօրեն` · 15 ch
**11b** · founder role · 24 · `Բիզնեսի զարգացման տնօրեն` · 24 ch
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

**19** · hero overline · 32 hard · `Խնամք, որը կարելի է ստուգել` · 27 ch
**20** · hero H1 · 48 hard · `Գերեզմանի խնամք Երևանում՝ ամեն այցի ապացույցով` · 46 ch

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

**21** · hero standfirst · 105 hard · `Ոմանք հեռու են, ոմանք ժամանակ չունեն։ Խումբը գնում է, մաքրում ամբողջ հողամասը և ցույց տալիս արածը։` · 98 ch

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

**22a** · verification item · 22 hard · `GPS-կետը՝ գրանցված տեղում` · 25 ch ⚠ OVER
**22b** · verification item · 22 hard · `8 լուսանկար, 2 տեսանյութ` · 24 ch ⚠ OVER
**22c** · verification item · 22 hard · `Հաշվետվություն՝ 48 ժամում` · 25 ch ⚠ OVER

  ↳ **All three breach 22 hard and I am not shortening them.** This is
  the verification strip — the checkable substance on the first screen,
  the thing test 2 of the ranking criteria measures. The alternatives
  that fit 22 are `GPS-կետ` (7, says nothing — hush.am also says GPS,
  and unqualified GPS is on the strategy's indefensible list),
  `Լուսանկար, տեսանյութ` (20, drops the numbers, and the numbers *are*
  the protocol), and `48 ժամում` (9, dangling). Each of those trades the
  argument for four characters. **Proposal in §11.1: raise slot 22 to 26
  characters in all three locales.** The word `հաշվետվություն` is 14
  characters long in Armenian and appears in most of the strip-sized
  slots on this site; a 22-character ceiling was set against English and
  cannot survive contact with the noun.

**23** · CTA support line · 40 · `Առայժմ ոչ վճարում, ոչ գրանցում։` · 31 ch

  ↳ **STRUCTURE.** English is two sentences (`No payment now. No account
  needed.`). Armenian has a correlative construction — `ոչ… ոչ…` — that
  does both halves in one breath and sounds like a person rather than a
  checkbox list. Forcing two Armenian sentences here would be the tell of
  a translated page.

**HOME-7** · secondary link · n/a · `Տեսնել ամբողջական հաշվետվություն` · 32 ch

### 6.2 The report — section 2, the heaviest object on the page

**24a** · report overline · 24 · `Ապացույցը` · 9 ch
**24b** · report H2 · 44 · `Ահա թե ինչ է գալիս ամեն այցից հետո` · 34 ch
**24c** · report standfirst · 100 · `Ամսաթիվ, գերեզմանոց, հողամասի համար, GPS-կետ, 8 լուսանկար, 2 տեսանյութ և խմբի գրառումը։` · 87 ch

  ↳ The standfirst is a **list, not a sentence**, and that is deliberate:
  it reads as an inventory, which is what the product is. Armenian
  tolerates a bare nominal list far better than English does — a
  verb-first sentence here would soften it.

**25a** · annotation · GPS · 90 · `GPS-կետը գրանցվում է հենց հողամասի մոտ, այցի օրը։ Այն ապացուցում է, որ խումբն այնտեղ է եղել։` · 92 ch ⚠ OVER
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

**26** · report link · 24 · `Ամբողջ հաշվետվությունը` · 22 ch

### 6.3 How it works — three steps

**27a** · step label · 14 hard · `Զանգ` · 4 ch
**27b** · step label · 14 hard · `Այց` · 3 ch
**27c** · step label · 14 hard · `Հաշվետվություն` · 14 ch

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

**29** · method H2 · 44 · `Ինչ է անում խումբը մեկ այցի ընթացքում` · 37 ch

**30a-l** · method label · 20 · `Սարքավորումը` · 12 ch
**30a-b** · method line · 90 · `Գոլորշու գեներատոր, Kärcher, փոշեկուլ՝ քարի և հողամասի ամբողջ մակերեսին։` · 72 ch
**30b-l** · method label · 20 · `Միջոցները` · 9 ch
**30b-b** · method line · 90 · `Միջոցն ընտրում ենք քարի տեսակով՝ գրանիտ, բազալտ, տուֆ։ Սպիտակեցնող չենք օգտագործում։` · 84 ch
**30c-l** · method label · 20 · `Խումբը` · 6 ch
**30c-b** · method line · 90 · `Ձեր հողամասն ամրագրված է որոշակի խմբի։ Այցից այց նույն մարդիկ գիտեն, թե ինչ են թողել։` · 85 ch
**30d-l** · method label · 20 · `Գրանցումը` · 9 ch
**30d-b** · method line · 90 · `Այցը փակվում է միայն այն բանից հետո, երբ կան 8 լուսանկարը, 2 տեսանյութը և GPS-կետը։` · 83 ch

  ↳ `Միջոցները` and not `Քիմիան`: Armenian `քիմիա` is the school subject.
  `Մաքրող միջոց` is what a professional calls the product, and
  `մասնագիտական քիմիա` — the literal rendering of the brief's
  "professional chemistry" — reads in Armenian as a phrase from a safety
  data sheet.
  ↳ 30c is worded as an **assignment** (`ամրագրված է որոշակի խմբի`) and
  never as an unchanged roster, per 26.08 §3.4. The second sentence
  carries the benefit (they know what they left) without promising the
  same names, which is the legal trap.

**31** · `what we do not do` H3 · 30 · `Ինչ չենք անում` · 14 ch
**32a** · limit · 70 · `Շինարարական աշխատանք չենք անում՝ պետք է քաղաքային թույլտվություն։` · 65 ch
**32b** · limit · 70 · `Տապանաքարը չենք բացում և տեղից չենք շարժում։` · 44 ch
**32c** · limit · 70 · `Փակ կամ վիճելի հատված չենք մտնում առանց ընտանիքի համաձայնության։` · 64 ch

### 6.5 Family Circle — the dark band

**33a** · eyebrow · 24 · `Ընտանեկան շրջանակ` · 17 ch
**33b** · H2 · 40 · `Մեկ հողամաս, մի ամբողջ ընտանիք` · 30 ch
**33c** · definition · 120 hard · `Խնամքը հազվադեպ է մեկ մարդու որոշում, և այն չպետք է մնա մեկ մարդու փոստարկղում։` · 79 ch

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

**35-h** · H2 · 40 · `Ինչպես ստուգել վերևում գրվածը` · 29 ch
**35a-l** · label · 22 · `Ամսաթիվն ու կետը` · 16 ch
**35a-b** · line · 90 · `GPS-կետը գրանցվում է հողամասի մոտ, այցի օրը, ոչ թե գրասենյակում, ոչ թե հետո։` · 76 ch
**35b-l** · label · 22 · `Անուն և հեռախոս` · 15 ch
**35b-b** · line · 90 · `Դավիթ Համբարձումյանի և Հայկ Մանուկյանի ուղիղ բջջային համարները՝ կայքի ամեն էջում։` · 81 ch
**35c-l** · label · 22 · `Գները՝ բացեիբաց` · 15 ch
**35c-b** · line · 90 · `Չորս գին տպված է, հինգերորդը՝ հաշվիչով։ Բանաձևը բոլորի համար նույնն է։` · 70 ch
**35d-l** · label · 22 · `Մեր սահմանները` · 14 ch
**35d-b** · line · 90 · `Գրում ենք նաև այն, ինչ չենք անում, և այն, ինչ լինում է, երբ եղանակը թույլ չի տալիս։` · 83 ch

  ↳ `բացեիբաց` — *openly, in the open* — is an ordinary Armenian adverb
  and the only word here that carries any warmth. It earns its place
  because the sentence it labels is about arithmetic.

### 6.7 The honesty panel

**36** · honesty panel · 240 hard · `Մենք սկսել ենք 2026-ին։ Առաջին հաճախորդներին ընդունում ենք հիմա։ Կարծիքներ դեռ չունենք ցույց տալու, և ուրիշինը չենք վերցնի։ Փոխարենը կա այն, ինչ կարող եք ստուգել՝ գրված ընթացակարգ, իրական հաշվետվություն, մեր անունները և ուղիղ համարները։` · 236 ch

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
**39b** · A · 320 · `Ոչ։ Զննումը հենց դրա համար է՝ խումբը գտնում է գերեզմանոցը և հողամասը, գրանցում GPS-կետը և ուղարկում վիճակի նկարագիրը՝ լուսանկարներով և տեսանյութով։ Այդ կետից հետո տեղը հայտնի է ընդմիշտ, և ամեն հաջորդ այց սկսվում է նույն կետից։ Զննումն արժե 20,000 ֏ AMD, և տարեկան բաժանորդագրություն կնքելիս այդ գումարը հաշվառվում է։` · 316 ch

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

**40a** · form heading · 44 · `Խոսենք՝ առանց պարտավորության` · 28 ch
**40b** · support line · 90 · `Պատմեք գերեզմանոցի մասին, մենք կասենք՝ ինչ կանենք և որքան կարժենա։` · 66 ch

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
**42** · one-price-list line · 60 hard · `Մեկ գնացուցակ՝ նույնը Երևանում և Լոս Անջելեսում։` · 48 ch

  ↳ Los Angeles is named because the suspicion it answers is specific: a
  diaspora buyer's first thought is that a foreign card pays a foreign
  price. Naming the city answers it faster than any sentence about
  fairness, and it names no persona — a Yerevan reader reads it as a
  statement about the company, not about themselves.

**43** · the sameness line · 70 hard · `Ամեն այց նույն լիարժեք այցն է։ Տարբերությունը միայն քանակն է։` · 61 ch

### 7.1 The Զննում rail

**44a** · name · 22 hard · `Զննում` · 6 ch
**44b** · description · 90 hard · `Մեկ այց՝ գտնում ենք հողամասը, նկարագրում վիճակը և գնանշում աշխատանքը։ Առանց մաքրման։` · 84 ch
**44c** · CTA · 20 · `Պատվիրել զննում` · 15 ch

  ↳ 44b fits 90 at 84, but only because both of its load-bearing clauses
  are as short as Armenian allows. `Առանց մաքրման` is the one thing `PROPOSAL-strategy.md` §6e
  says this card must state plainly, because with the light/heavy
  vocabulary gone there is nothing else stopping a reader assuming the
  Զննում includes cleaning; `գնանշում աշխատանքը` — the priced quote — is
  what the same paragraph calls the strongest thing about the product.
  Neither may be cut to make room for anything else in this slot.

**45** · one-off chip · 26 hard · `Մեկանգամյա` · 10 ch

  ↳ **STRUCTURE and a loss.** English fits `One-off · not a subscription`
  in 26. Armenian needs `Մեկանգամյա՝ ոչ բաժանորդագրություն` — 33 — and
  there is no shorter Armenian for *subscription*. I have written the
  half that carries the new information and dropped the half that denies
  the other thing, because in Armenian the denial is the weaker half:
  `Մեկանգամյա` already excludes a subscription to any reader. If the chip
  can hold 33 characters the fuller string is better; §11.3.

### 7.2 The three cards

**46a** · product name · 22 hard · `Էքսպրես` · 7 ch
**46b** · product name · 22 hard · `Օպտիմալ` · 7 ch
**46c** · product name · 22 hard · `Մաքսիմում` · 9 ch
**46d** · product name · 22 hard · `Զննում` · 6 ch
**46e** · product name · 22 hard · `Հատուկ խնամք` · 12 ch

**47a** · unit chip · 12 hard · `Մեկանգամյա` · 10 ch
**47b** · unit chip · 12 hard · `Տարեկան` · 7 ch

  ↳ **⚠ Conflict to resolve, not mine to rule.** `PROPOSAL-ux.md` §3.3
  and the art direction specify these chips as 14px **uppercase**;
  `FINAL-CONTENT` §3.8 bans ALL CAPS in every language except the logo
  tagline. In Armenian the ban should win on typographic grounds as well
  as editorial ones: Armenian majuscules are much wider than the
  lowercase (`ՄԵԿԱՆԳԱՄՅԱ` against `Մեկանգամյա`), they lose the
  descenders that make Armenian readable at small sizes, and Ghea Mariam
  has not been checked for a designed uppercase at 14px. **Recommend
  sentence case with wide tracking** for the Armenian locale, which reads
  as a chip without shouting. §11.4.

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

**51** · year-rail footnote · 120 hard · `Ձմեռային այցը կատարվում է այն օրերին, երբ եղանակը թույլ է տալիս։ Եթե այդպիսի օր չլինի, այցն ավելանում է գարնանը՝ չորս այց՝ միևնույն է։` · 134 ch ⚠ OVER

  ↳ 20 over 120 hard. The English is `The winter visit runs in a
  suitable weather window. If none opens, it is added to spring — four
  visits either way.` Armenian pays for three things English gets free:
  the *weather window* idiom does not exist and must be spelled out as a
  clause (§6.9), `ավելանում է գարնանը` needs its subject, and `միևնույն
  է` is the only natural Armenian for *either way*. The shortest honest
  version is `Ձմեռային այցը կատարվում է եղանակի թույլ տված օրերին։ Եթե
  այդպիսի օր չլինի, այցն ավելանում է գարնանը։` (110) — but it drops
  *four visits either way*, which is the guarantee and the reason the
  footnote exists. §11.5.

**52a** · arithmetic · 44 hard · `65,000 ֏ AMD · մեկ լիարժեք այց` · 30 ch
**52b** · arithmetic · 44 hard · `160,000 ֏ AMD/տարի · 4 այց · 40,000 ֏ այցը` · 42 ch
**52c** · arithmetic · 44 hard · `200,000 ֏ AMD/տարի · 6 այց · ≈33,300 ֏ այցը` · 43 ch

  ↳ `AMD` is written once per line, on the annual figure, and dropped
  from the per-visit figure. Writing it twice puts 52b and 52c at 48 and
  breaks a hard budget on the site's most important numbers. This is the
  concrete cost of the `֏ AMD` rule and it is why I contest it in §12.1.

**53** · feature lines · 54 hard each · four per card, same slot count in
all three so the rows align:

**53a1** · Express · 54 hard · `Ամբողջ հողամասը և բոլոր տապանաքարերը` · 36 ch
**53a2** · Express · 54 hard · `8 լուսանկար, 2 տեսանյութ, GPS-կետ` · 33 ch
**53a3** · Express · 54 hard · `Հաշվետվությունը՝ 48 ժամում, անձնական էջում` · 42 ch
**53a4** · Express · 54 hard · `Ձեր հողամասն ամրագրված է որոշակի խմբի` · 37 ch
**53b1** · Optimal · 54 hard · `Չորս անգամ՝ գարուն, ամառ, աշուն, ձմեռ` · 37 ch
**53b2** · Optimal · 54 hard · `Ամեն այցը՝ ամբողջ հողամասը և բոլոր քարերը` · 41 ch
**53b3** · Optimal · 54 hard · `Ընտանեկան շրջանակ՝ առանց լրավճարի` · 33 ch
**53b4** · Optimal · 54 hard · `Ձեր հողամասն ամրագրված է որոշակի խմբի` · 37 ch
**53c1** · Maximum · 54 hard · `Վեց անգամ՝ տարվա ընթացքում հավասար` · 34 ch
**53c2** · Maximum · 54 hard · `Ամեն այցը՝ ամբողջ հողամասը և բոլոր քարերը` · 41 ch
**53c3** · Maximum · 54 hard · `Ընտանեկան շրջանակ՝ առանց լրավճարի` · 33 ch
**53c4** · Maximum · 54 hard · `Ձեր հողամասն ամրագրված է որոշակի խմբի` · 37 ch

**54a** · credit line · Express · 60 hard · `60 օրվա ընթացքում ամբողջ 65,000-ը հաշվառվում է բաժանորդագրության մեջ։` · 69 ch ⚠ OVER
**54b** · credit line · Optimal · 60 hard · `Զննումի կամ Էքսպրեսի գումարը հաշվառվում է այստեղ։` · 49 ch
**54c** · credit line · Maximum · 60 hard · `Զննումի կամ Էքսպրեսի գումարը հաշվառվում է այստեղ։` · 49 ch

  ↳ `հաշվառվում է` — *is credited/accounted into* — and never
  `զեղչվում է`. `Զեղչ` is a discount, and `FINAL-CONTENT` §3.3 bans the
  discount register outright: this is money the client has already paid
  being carried forward, not a price being reduced. Armenian has the
  exact accounting verb and it should be used everywhere the credit is
  mentioned.

**55a** · card CTA · 20 hard · `Ընտրել Էքսպրեսը` · 15 ch
**55b** · card CTA · 20 hard · `Ընտրել Օպտիմալը` · 15 ch
**55c** · card CTA · 20 hard · `Ընտրել Մաքսիմումը` · 17 ch

  ↳ Definite accusative `-ը` on each name — `Ընտրել Օպտիմալ` is
  ungrammatical Armenian. See the declension note in §3: the build must
  not treat product names as invariant tokens.

**56** · recommendation badge · 22 hard · `Մեր խորհուրդը` · 13 ch

  ↳ Ruled in §4. Not `առաջատար`.

### 7.3 The credit block

**57a** · headline · 34 hard · `Փոքրից սկսելը ձեզ ոչինչ չարժե։` · 30 ch
**57b** · subline · 90 hard · `Ինչպես էլ սկսեք, առաջին տարին 160,000 ֏ AMD է և չորս լիարժեք այց։` · 65 ch

  ↳ The Armenian is a little better than the English here, and it is
  worth saying why: `ձեզ ոչինչ չարժե` uses the same verb (`արժենալ`,
  to cost) that every price on the page uses, so the headline is
  literally in the currency of the section rather than in a metaphor.

**58a** · worked line · 80 · `Ուղիղ Օպտիմալ՝ 160,000 = 160,000 ֏ AMD · 4 լիարժեք այց` · 54 ch
**58b** · worked line · 80 · `Զննում, ապա Օպտիմալ՝ 20,000 + 140,000 = 160,000 ֏ AMD · 4 այց և զննում` · 70 ch
**58c** · worked line · 80 · `Էքսպրես, ապա Օպտիմալ՝ 65,000 + 95,000 = 160,000 ֏ AMD · Էքսպրեսն առաջին այցն է` · 78 ch

**59a** · credit bullet · 80 · `Մեկ հողամասին՝ մեկ հաշվառում, բաժանորդագրությունը կնքելու պահին։` · 64 ch
**59b** · credit bullet · 80 · `Մեկ գումար։ Եթե երկուսն էլ վճարել եք, հաշվառվում է մեծը՝ 65,000-ը։` · 66 ch
**59c** · credit bullet · 80 · `Այցից 60 օր։ Անձնական էջում գրված է, թե որ օրն է այդ ժամկետը լրանում։` · 69 ch
**59d** · credit bullet · 80 · `Կրկնվող Էքսպրեսն էժան չէ։ Երկրորդն էլ 65,000 ֏ AMD է։` · 53 ch

**60** · credit-expiry line, portal · 46 · `Հաշվառումը հասանելի է մինչև 14 հոկտեմբերի 2026` · 46 ch

  ↳ A plain date, never a countdown. Armenian date order is
  day–month–year and the month is lower case and in the genitive
  (`հոկտեմբերի`), which is the form a reader expects on a document. Never
  `14.10.2026` — the same argument the English stop-list makes about
  `14/09/26`.

### 7.4 Special and the calculator

**61a** · name · 22 hard · `Հատուկ խնամք` · 12 ch
**61b** · definition · 110 hard · `16 մ²-ից մեծ հողամասի, երկուսից ավելի քարի, ավելի հաճախակի այցերի կամ մի քանի ընտանեկան հողամասի համար։` · 103 ch
**61c** · price-floor line · 60 · `Հատուկ խնամքի այցը երբեք Մաքսիմումի այցից էժան չէ։` · 50 ch
**61d** · entry rule · 110 hard · `Հատուկ խնամքը միշտ սկսվում է Զննումից. գինը դնում ենք հողամասը տեսնելուց հետո, ոչ թե դրանից առաջ։` · 97 ch

  ↳ 61d uses the Armenian **միջակետ** `.` in the middle — its correct
  function, joining two clauses where English would use a colon or a
  dash. This is the mark most often replaced by a full stop in translated
  Armenian, and getting it right is most of what makes a paragraph read
  as written rather than converted.

**62a** · Special CTA · 26 hard · `Սկսել Զննումից` · 14 ch
**62b** · Special CTA · 26 hard · `Խորհրդատվության հայտ` · 20 ch

**63a** · calculator heading · 40 · `Հաշվեք ձեր գինը հենց հիմա` · 25 ch
**63b** · open-formula line · 80 hard · `Բոլորի համար նույն բանաձևը։ Հեռախոսով ոչինչ չի որոշվում։` · 56 ch

**64a** · base chip · 22 hard · `Օպտիմալ (4 այց)` · 15 ch
**64b** · base chip · 22 hard · `Մաքսիմում (6 այց)` · 17 ch
**64c** · base chip · 22 hard · `Էքսպրես (1 այց)` · 15 ch

**65a** · slider label · 20 · `Հողամասի մակերեսը` · 17 ch
**65b** · slider label · 20 · `Տապանաքարերի թիվը` · 17 ch
**65c** · included caption · 28 hard · `Մինչև 16 մ² ներառված է` · 22 ch
**65d** · included caption · 28 hard · `Մինչև 2 քար ներառված է` · 22 ch

**66a** · result row label · 24 hard · `Հիմքը` · 5 ch
**66b** · result row label · 24 hard · `Մակերեսը` · 8 ch
**66c** · result row label · 24 hard · `Տապանաքարերը` · 12 ch
**66d** · result row label · 24 hard · `Ընդամենը՝ տարեկան` · 17 ch

**67** · default state · 50 hard · `Ստանդարտ հողամաս՝ 160,000 ֏ AMD։ Հավելավճար չկա։` · 48 ch
**68** · ceiling state · 90 hard · `Սրանից մեծի գինը դնում ենք առանձին՝ Զննումից հետո, երբ խումբը տեսել է հողամասը։` · 79 ch
**69a** · rate explanation · 110 · `160,000 ֏ ÷ 16 մ² = 10,000 ֏ քառակուսի մետրի համար՝ տարեկան։ Ավելացած մետրն արժե ճիշտ այնքան, որքան ներառվածը։` · 110 ch
**69b** · rate explanation · 110 · `Մեկանգամյա այցի հավելավճարը տարեկանի քառորդն է՝ մեկ այց չորսի փոխարեն։` · 70 ch
**70a** · aria-valuetext · 30 · `24 քառակուսի մետր` · 17 ch
**70b** · aria-valuetext · 30 · `3 տապանաքար` · 11 ch

  ↳ `aria-valuetext` is read aloud, so it spells `քառակուսի մետր` in
  full rather than `մ²`, which a screen reader would render as
  `մ երկու`. Same reason the English spells `square metres`.

**71** · ritual row · n/a · `[BLOCKED — flowers and a candle are an explicit owner instruction of 26.08 §7.5 for this page, and no source gives either a price. FINAL-REBRAND §6.1 and PROPOSAL-ux §12.1 both record it as blocking. Armenian strings drafted and held: heading «Ավելացնել ցանկացած այցի», items «Ծաղիկներ» / «Մոմ», line «Դնում ենք այցի ընթացքում և ցույց տալիս լուսանկարում։» — the price field stays empty until Davit sets it.]` · 407 ch

**72** · payment term · 40 hard · `Վճարվում է մեկ անգամ՝ տարվա համար։` · 34 ch

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
**76e-A** · A · 300 · `Տարեկան բաժանորդագրություն կնքելու պահին, եթե այցից անցել է 60 օրից պակաս։ Հաշվառվում է մեկ գումար՝ երկուսից մեծը։ Զննումի 20,000-ը Էքսպրեսի մեջ չի հաշվառվում. այն հաշվառվում է միայն բաժանորդագրության մեջ։` · 205 ch

**76f** · Q · 70 · `Կարո՞ղ եմ վճարել մաս-մաս։` · 25 ch
**76f-A** · A · 300 · `Ոչ։ Բաժանորդագրությունը վճարվում է մեկ անգամ՝ ամբողջ տարվա համար։ Ամսական և սեզոնային վճարում չենք առաջարկում, և դա մեր որոշումն է, ոչ թե ժամանակավոր վիճակ։ Եթե տարեկան գումարը հիմա հարմար չէ, սկսեք Զննումից կամ Էքսպրեսից՝ վճարածը հետո հաշվառվում է։` · 249 ch

  ↳ The last sentence turns a refusal into the trust ladder, which is the
  only honest way to publish this one. The owner rejected instalments and
  the client council recorded it as the remaining friction for the older
  local buyer; this is that buyer's answer.

---

## 8. How it works — `/hy/ինչպես-է-աշխատում/`

**77a** · H1 · 40 · `Ինչպես է աշխատում` · 17 ch
**77b** · standfirst · 100 · `Առաջին զանգից մինչև այն հաշվետվությունը, որը բացում եք ձեր հեռախոսում։` · 70 ch

**78** · timeline, four steps — number label 14, heading 30, body 220:

**78a-n** · step number · 14 · `Քայլ 1` · 6 ch
**78a-h** · step heading · 30 · `Խոսակցություն` · 13 ch
**78a-b** · step body · 220 · `Ասում եք՝ որ գերեզմանոցը, մոտավորապես որտեղ է հողամասը և ով կա ընտանիքում։ Մենք ասում ենք՝ ինչ կներառի այցը և որքան կարժենա։ Այս զանգին ոչինչ չի ստորագրվում։ Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 201 ch

**78b-n** · step number · 14 · `Քայլ 2` · 6 ch
**78b-h** · step heading · 30 · `Գտնում և գրանցում ենք` · 21 ch
**78b-b** · step body · 220 · `Առաջին այցին խումբը գտնում է հողամասը և գրանցում նրա GPS-կետը, ապա անում է ամբողջ աշխատանքը։ Քարի ու տնկիների վիճակը գրվում է այնպես, ինչպես գտել ենք, որպեսզի ամեն հաջորդ հաշվետվություն համեմատելի լինի առաջինի հետ։` · 214 ch

**78c-n** · step number · 14 · `Քայլ 3` · 6 ch
**78c-h** · step heading · 30 · `Այցերի տարին` · 12 ch
**78c-b** · step body · 220 · `Բաժանորդագրությունը գործում է 12 ամիս՝ կնքելու օրվանից։ Օպտիմալը չորս լիարժեք այց է՝ մեկը յուրաքանչյուր եղանակին։ Մաքսիմումը՝ վեց այց տարվա ընթացքում։ Մոտավոր շաբաթները պայմանավորվում ենք ձեզ հետ, ամեն ամսաթիվը հաստատում ենք անձնական էջում։` · 240 ch ⚠ OVER

**78d-n** · step number · 14 · `Քայլ 4` · 6 ch
**78d-h** · step heading · 30 · `Այցը և հաշվետվությունը` · 22 ch
**78d-b** · step body · 220 · `Ամբողջ հողամասը և բոլոր տապանաքարերը։ Այցից 48 ժամում անձնական էջում հայտնվում է հաշվետվությունը՝ լուսանկարներ գալու պահին և աշխատանքից հետո, տեսանյութ, GPS-կետ, ամսաթիվ և խմբի անունը։ Կարող եք ուղարկել սովորական հղումով՝ ընտանիքին գրանցում պետք չէ։` · 249 ch ⚠ OVER

**79** · what a full visit includes, eight items, 60 each:

**79a** · included item · 60 · `Տապանաքարի և պատվանդանի մաքրում` · 31 ch
**79b** · included item · 60 · `Եզրաքարերի, արահետների և հողամասի մակերեսի մաքրում` · 50 ch
**79c** · included item · 60 · `Առկա տնկիների կարգի բերում` · 26 ch
**79d** · included item · 60 · `Աղբի, տերևների և հին ծաղիկների հեռացում` · 39 ch
**79e** · included item · 60 · `Աշխատանքից հետո ամբողջ մակերեսի ողողում` · 39 ch
**79f** · included item · 60 · `Լուսանկարներ գալու պահին և աշխատանքից հետո` · 42 ch
**79g** · included item · 60 · `Ամբողջ հողամասի տեսանյութ` · 25 ch
**79h** · included item · 60 · `GPS-կետ՝ գրանցված հողամասի մոտ` · 30 ch

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
  than cut it. §11.6.
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

**83** · assigned crew · 60 hard · `Ձեր հողամասն ամրագրված է որոշակի խմբի։` · 38 ch
**84** · first visit · 220 · `Առաջին այցը սովորական այց չէ միայն այն պատճառով, որ դրանից է սկսվում ամեն ինչ՝ GPS-կետը, վիճակի նկարագիրը, համեմատության ելակետը։ Աշխատանքի ծավալով այն նույնն է, ինչ մյուսները՝ ամբողջ հողամասը և բոլոր քարերը։` · 208 ch

  ↳ Never described as a survey. Only Զննում is a survey, and in Armenian
  that distinction is carried by one word — `զննում` versus `այց` — so it
  is easy to keep and easy to break. A line that called this
  `առաջին զննումը` would collapse two products into one.

---

## 9. Sample report — `/hy/հաշվետվություն/`

**85a** · H1 · 40 · `Հաշվետվության նմուշ` · 19 ch
**85b** · one-line header · 90 · `Ահա թե ինչ է գալիս ամեն այցից հետո։ Այստեղ ոչինչ դեկորատիվ չէ։` · 62 ch

**86a** · block label · 22 hard · `Հաստատում` · 9 ch
**86b** · block label · 22 hard · `GPS-կետ` · 7 ch
**86c** · block label · 22 hard · `Գալու պահին` · 11 ch
**86d** · block label · 22 hard · `Աշխատանքից հետո` · 15 ch
**86e** · block label · 22 hard · `Խմբի գրառումը` · 13 ch
**86f** · block label · 22 hard · `Հաջորդ այցը` · 11 ch

  ↳ `Գալու պահին` / `Աշխատանքից հետո` and not `Մինչև` / `Հետո`. The
  bare pair is the before/after slider's vocabulary, and the design
  package forbids that component precisely because the pair invites a
  judgement about the family. `Գալու պահին` — *at the moment of arrival*
  — describes when the photograph was taken, not what state anything was
  in, and it is chronological rather than evaluative.

**87a** · annotation · 130 · `Առաջին տողը պարզ հաստատում է՝ ամսաթիվ, գերեզմանոց, հատված, հողամաս։ Այցը եղել է, և ահա երբ։` · 91 ch
**87b** · annotation · 130 · `GPS-կետը գրանցվում է հողամասի մոտ, այցի օրը։ Այն պատասխանում է մեկ հարցի՝ խումբը կանգնա՞ծ է եղել այնտեղ։` · 104 ch
**87c** · annotation · 130 · `Չորս անկյուն գալու պահին և նույն չորս անկյունը աշխատանքից հետո՝ ութ լուսանկար, նույն կետերից, որ համեմատելի լինեն։` · 114 ch
**87d** · annotation · 130 · `Երկու տեսանյութ՝ 20-40 վայրկյան։ Խմբի գրառումը վերջում՝ ինչ արվեց և ինչ է պետք հաջորդ անգամ։` · 92 ch

  ↳ 87b is the site's second GPS-as-verification string and it is the
  sharper of the two: Armenian can put the whole question inside the
  sentence with `՞` on the participle — `կանգնա՞ծ է եղել` — and no
  English construction is that compact. **↳ STRUCTURE:** do not
  back-translate; English needs a separate clause to ask it.

**88** · link-preview explainer · 200 · `Հաշվետվությունը կարող եք ուղարկել հղումով՝ WhatsApp-ով կամ Viber-ով։ Ստացողին գրանցում պետք չէ։ Զրույցի նախադիտման մեջ ոչ լուսանկար կա, ոչ անուն՝ միայն ամսաթիվը և գերեզմանոցը, որովհետև այդ էկրանը մերը չէ։` · 204 ch ⚠ OVER

  ↳ The last clause — *because that screen is not ours* — is the whole
  privacy argument in five words and it is the reason the rule exists. An
  Armenian family group chat is exactly where this link lands.

**89a** · delivery question · 80 · `Ինչպե՞ս ուղարկենք հաշվետվությունները, և ուզո՞ւմ եք իմանալ այցից առաջ։` · 69 ch
**89b** · checkbox · 56 hard · `Ուղարկեք հղումով, որ կարողանամ փոխանցել ընտանիքին` · 49 ch
**89c** · checkbox · 56 hard · `Զանգահարեք կամ գրեք այցից մեկ օր առաջ` · 37 ch
**89d** · checkbox · 56 hard · `Այցից առաջ տեղեկացրեք ուրիշին՝ Երևանում` · 39 ch

  ↳ 89b is default on, 89c default off, per 26.08 §3.5. The Armenian for
  89c is written as an instruction from the reader to us
  (`Զանգահարեք…`), not as a description of a setting, because a
  checkbox that reads as a description is ambiguous about which state is
  which.

---

## 10. About, Contacts, 404, 500, and the form

### 10.1 About — `/hy/մեր-մասին/`

**96a** · opening paragraph · 400 · `MemoryCare-ը Երևանում գրանցված ընկերություն է, որը խնամում է ընտանեկան գերեզմանները քաղաքի գերեզմանոցներում և ամեն այցից հետո ուղարկում է հաշվետվություն՝ լուսանկարներով, տեսանյութով և հողամասի մոտ գրանցված GPS-կետով։ Աշխատում ենք բաժանորդագրությամբ՝ տարվա մեջ չորս կամ վեց լիարժեք այց, և առանձին այցերով։ Ամեն այց լիարժեք է. ամբողջ հողամասը և բոլոր տապանաքարերը, ոչ թե շրջայց։` · 376 ch

**96b** · opening paragraph · 400 · `Ընկերությունը հիմնադրվել է 2026 թվականին, և առաջին հաճախորդներին ընդունում ենք հիմա։ Կարծիքներ դեռ չունենք ցույց տալու։ Ունենք գրված ընթացակարգ, տպված գներ, ուղիղ հեռախոսահամարներ և երաշխիքներ, որոնք գումար են արժենում մեզ, ոչ թե ձեզ։ Այս էջում գրված ամեն թիվ կարող եք ստուգել՝ կամ հաշվետվության մեջ, կամ պայմանագրում։` · 318 ch

**97** · why it exists · 300 · `Երևանում գերեզման խնամելը դժվար չէ։ Դժվարը իմանալն է, որ դա իսկապես արվել է։ Ընկերությունը սկսվեց այդ հարցից՝ ոչ թե «ո՞վ կմաքրի», այլ «ինչպե՞ս իմանամ»։ Դրա համար ամեն այցի հետևում կանգնած է գրված ընթացակարգ՝ 8 լուսանկար, 2 տեսանյութ, մեկ GPS-կետ, և առանց դրանց այցը փակված չի համարվում։` · 286 ch

  ↳ **STRUCTURE, and the paragraph I would keep if I could keep one.**
  The Armenian is built on a contrast Armenian makes naturally with two
  short clauses (`Դժվար չէ… Դժվարը… է`) and English cannot do without
  extra words. It also states the company's reason as a question a person
  actually asks, in quotation marks, in the reader's own voice — which is
  as close to a story as this brand is allowed to come, and it contains
  no adjective at all.

**98a** · method item · 120 · `Սարքավորումը՝ գոլորշու գեներատոր, Kärcher, փոշեկուլ։ Ոչ մետաղյա խոզանակ, ոչ սպիտակեցնող։` · 88 ch
**98b** · method item · 120 · `Միջոցն ընտրվում է քարով՝ գրանիտը, բազալտը և տուֆը նույն կերպ չեն մշակվում։` · 74 ch
**98c** · method item · 120 · `Ամեն այց փակվում է գրանցումով՝ 8 լուսանկար, 2 տեսանյութ, GPS-կետ։ Առանց դրանց այցը փակված չէ։` · 93 ch

**About · legal block** — `[BLOCKED — same three missing facts as slot 9. The About page is one of the eight Ameriabank conditions and it cannot be submitted without the entity name, the ՀՎՀՀ and the legal address.]`

### 10.2 Contacts — `/hy/կապ/`

**99** · hours block · 120 · `Երևան, երկուշաբթի–ուրբաթ 09:00–18:00 (UTC+4)։ Երկու համարն էլ ընդունում են WhatsApp և Viber։` · 92 ch
**100** · map placeholder · 60 · `Քարտեզը կավելացվի հասցեն հաստատվելուց հետո` · 42 ch

  ↳ Visibly a placeholder, per FINDINGS #14 — it must not be styled to
  look like a map that failed to load.

### 10.3 The consultation form

**101a** · heading · 44 · `Անվճար խորհրդատվություն` · 23 ch
**101b** · support line · 90 · `Երեք դաշտ։ Ոչ վճարում, ոչ գրանցում։ Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 79 ch

**102a** · field label · 24 hard · `Անուն` · 5 ch
**102b** · field label · 24 hard · `Հեռախոս կամ էլփոստ` · 18 ch
**102c** · field label · 24 hard · `Գերեզմանոց կամ քաղաք` · 20 ch
**102d** · field label · 24 hard · `Ավելացնել նշում` · 15 ch
**102e** · field label · 24 hard · `Համաձայնություն` · 15 ch

**103a** · helper · 70 · `Ինչպես ձեզ դիմել։ Ազգանունը պարտադիր չէ։` · 40 ch
**103b** · helper · 70 · `Գրեք այնպես, ինչպես հարմար է։ Կհասկանանք։` · 41 ch
**103c** · helper · 70 · `Եթե չգիտեք, ընտրեք «Չգիտեմ»՝ դա նորմալ պատասխան է։` · 50 ch

  ↳ 103c matters more in Armenian than in English. A diaspora reader who
  has not been to the cemetery in nine years will not type a guess into a
  form in a language they read better than they write; `Չգիտեմ` must be
  offered as a real, unembarrassing option, and the helper says so in as
  many words.

**104** · note disclosure prompt · 140 · `Օրինակ՝ ո՞ր ժամերին է հարմար զանգել, ո՞վ է Երևանում ընտանիքից, ինչ գիտեք հողամասի մասին։ Պարտադիր չէ։` · 101 ch
**105** · consent line · 110 hard · `Համաձայն եմ, որ տվյալներս օգտագործվեն այս դիմումին պատասխանելու համար։ Գաղտնիության քաղաքականություն։` · 101 ch

**106a** · error · 70 hard · `Գրեք ձեր անունը՝ 2-60 նիշ։` · 26 ch
**106b** · error · 70 hard · `Հեռախոսահամարը կամ էլփոստը դատարկ է։` · 36 ch
**106c** · error · 70 hard · `Այս էլփոստը թերի է թվում։ Ստուգեք @-ից հետո մասը։` · 49 ch
**106d** · error · 70 hard · `Այս համարը երկրի ծածկագրին չի համապատասխանում։` · 46 ch
**106e** · error · 70 hard · `Համարը կարճ է թվում։ Ստուգեք նիշերի քանակը։` · 43 ch
**106f** · error · 70 hard · `Ընտրեք գերեզմանոցը կամ քաղաքը, կամ նշեք «Չգիտեմ»։` · 49 ch
**106g** · error · 70 hard · `Նշումը 500 նիշից երկար է։ Կարճացրեք կամ զանգեք մեզ։` · 51 ch
**106h** · error · 70 hard · `Առանց համաձայնության չենք կարող պահել տվյալները։` · 48 ch
**106i** · error · 70 hard · `Այս դաշտը դեռ լրացված չէ։` · 25 ch

  ↳ No `Սխալ`, no `Անվավեր`, no `Պարտադիր դաշտ` — the Armenian
  equivalents of the banned interface words, and all three are the
  default output of every Armenian form library. Each message says what
  to do next. `106i` replaces `Required field` and is the one string most
  likely to be silently reintroduced by a framework.

**107** · error summary heading · 60 · `Երկու բան դեռ լրացված չէ` · 24 ch

  ↳ **STRUCTURE.** Armenian numerals agree with nothing, so this string
  can be templated as `{n} բան դեռ լրացված չէ` with no plural forms at
  all — where English needs `1 thing` / `2 things` and Russian needs
  three forms. Worth telling the build: the Armenian locale needs no
  plural rules on this string.

**108a** · submit · 22 hard · `Ուղարկել հայտը` · 14 ch
**108b** · sending · 14 hard · `Ուղարկվում է…` · 13 ch

**109a** · success heading · 40 · `Շնորհակալություն, {name}։` · 25 ch
**109b** · promise echo · 16-18 · `Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 43 ch
**109c** · who will call · 110 · `Հայկը սովորաբար առաջինը գրում է WhatsApp-ով՝ +374 93 154 108, և զանգում է, եթե այդպես եք նախընտրում։` · 100 ch
**109d** · next action · 24 · `Տեսնել հաշվետվություն` · 21 ch
**109e** · next action · 24 · `Ինչպես է աշխատում` · 17 ch

  ↳ 109b breaches its 16-18 budget by design: it is slot 16, frozen, and
  frozen strings do not get a shorter local variant. The budget in
  `PROPOSAL-ux.md` §10 for 109 appears to describe a label, not the
  promise; flagged in §11.7 rather than solved by rewriting a frozen
  string.

**110a** · server failure · 130 · `Չհաջողվեց ուղարկել։ Ձեր գրածը տեղում է՝ փորձեք նորից։ Կամ գրեք ուղիղ՝ +374 93 154 108, info@memorycare.am։` · 106 ch
**110b** · retry label · 20 · `Փորձել նորից` · 12 ch

  ↳ No `Ինչ-որ բան սխալ գնաց`. The Armenian says what failed, that
  nothing was lost, and gives two humans to reach. This is the most
  important error on the site per §4.5 of the UX proposal.

**111a** · thank-you question · 40 · `Ինչպե՞ս իմացաք մեր մասին։` · 25 ch
**111b-g** · thank-you options · 24 each — `Որոնողական համակարգ` (19) · `Facebook կամ Instagram` (22) · `Ընկեր կամ հարազատ` (17) · `YouTube` (7) · `Գերեզմանոցում տեսա` (18) · `Այլ` (3)
**112** · country search placeholder · 40 · `Գտնել երկիրը կամ ծածկագիրը` · 26 ch
**113** · WhatsApp checkbox · 44 · `Այս համարը WhatsApp-ում է` · 25 ch

### 10.4 404 and 500

**119a** · 404 heading · 30 · `Այս էջը չկա` · 11 ch
**119b** · 404 line · 90 · `Հասցեն սխալ է կամ էջը տեղափոխվել է։ Ահա այն, ինչ ամենից հաճախ են փնտրում։` · 73 ch
**119c** · link · 22 · `Գլխավոր` · 7 ch
**119d** · link · 22 · `Գներ` · 4 ch
**119e** · link · 22 · `Ինչպես է աշխատում` · 17 ch
**119f** · link · 22 · `Հաշվետվության նմուշ` · 19 ch
**119g** · link · 22 · `Կապ` · 3 ch
**119h** · phone line · 40 · `Կամ զանգեք՝ +374 55 315 323` · 27 ch

  ↳ `Այս էջը չկա` — *this page does not exist* — and not `Էջը չի
  գտնվել`, which is the passive that hides who is at fault, and not
  `Ուպս`. Armenian 404 pages default to both.

**120a** · 500 heading · 30 · `Խնդիրը մեր կողմում է` · 20 ch
**120b** · 500 line · 90 hard · `Մեր կողմում ինչ-որ բան չի աշխատում։ Ձեր տվյալները տեղում են։` · 60 ch

### 10.5 Meta titles and descriptions

Category first, brand last, in every route. The Armenian has no
dementia-care collision to defend against, but the category-first rule
holds anyway because it is also how an Armenian reader scans a SERP.

**13a** · title · home · 60 hard · `Գերեզմանի խնամք Երևանում՝ ֆոտո, տեսանյութ, GPS | MemoryCare` · 59 ch
**14a** · description · home · 155 hard · `Ընտանեկան գերեզմանի պրոֆեսիոնալ խնամք Երևանի գերեզմանոցներում։ Ամեն այցից հետո՝ 8 լուսանկար, 2 տեսանյութ, GPS-կետ։ Չորս լիարժեք այց՝ 160,000 ֏ AMD տարեկան։` · 155 ch
**13b** · title · pricing · 60 hard · `Գերեզմանի խնամքի գները Երևանում | MemoryCare` · 44 ch
**14b** · description · pricing · 155 hard · `Չորս տպված գին և բաց բանաձև՝ Զննում 20,000, Էքսպրես 65,000, Օպտիմալ 160,000, Մաքսիմում 200,000 ֏ AMD։ Հաշվիչը մեծ հողամասերի համար՝ էջում։` · 138 ch
**13c** · title · how-it-works · 60 hard · `Ինչպես է աշխատում գերեզմանի խնամքը | MemoryCare` · 47 ch
**14c** · description · how · 155 hard · `Զանգից մինչև հաշվետվություն՝ քայլ առ քայլ։ Ինչ է ներառում լիարժեք այցը, ինչ չենք անում և ինչ է լինում, երբ ձմռանը եղանակը թույլ չի տալիս։` · 137 ch
**13d** · title · sample report · 60 hard · `Այցի հաշվետվության նմուշ՝ Երևան | MemoryCare` · 44 ch
**14d** · description · sample · 155 hard · `Իրական հաշվետվության կառուցվածքը՝ ամսաթիվ, GPS-կետ, 8 լուսանկար գալու պահին և աշխատանքից հետո, 2 տեսանյութ և խմբի գրառումը։` · 123 ch
**13e** · title · about · 60 hard · `Մեր մասին՝ գերեզմանի խնամք Երևանում | MemoryCare` · 48 ch
**14e** · description · about · 155 hard · `Ով ենք մենք, ինչ ընթացակարգով ենք աշխատում և ինչ երաշխիք ենք տալիս։ Ընկերությունը գրանցված է Երևանում 2026 թվականին։` · 116 ch
**13f** · title · contacts · 60 hard · `Կապ՝ MemoryCare, Երևան` · 22 ch
**14f** · description · contacts · 155 hard · `Ուղիղ համարներ, WhatsApp և Viber, աշխատանքային ժամեր երևանյան ժամանակով (UTC+4)։ Պատասխանում ենք մեկ աշխատանքային օրում։` · 120 ch
**13g** · title · 404 · 60 hard · `Էջը չկա | MemoryCare` · 20 ch
**14g** · description · 404 · 155 hard · `Այս հասցեով էջ չկա։ Անցեք գլխավոր էջ, գների էջ կամ զանգեք ուղիղ։` · 64 ch

**15a** · OG title · 60 · `Գերեզմանի խնամք Երևանում՝ ամեն այցի ապացույցով` · 46 ch
**15b** · OG description · 110 · `8 լուսանկար, 2 տեսանյութ և GPS-կետ՝ գրանցված հողամասի մոտ։ Հաշվետվությունը՝ 48 ժամում։` · 86 ch

  ↳ `ֆոտո` appears in the home title and nowhere else on the site. It is
  there because it is what people type into an Armenian search box;
  `լուսանկար` is the correct word and is used in every human-facing
  string. A title tag is not copy, it is a query surface, and the two
  should not be held to the same rule.

---

## 11. Where the budget cannot hold good Armenian

Twelve slots. In each case I have written the Armenian the sentence
needs and am proposing the component change rather than the cut. The
overage figures are computed, not estimated, and appear against each
string above.

| # | Slot | Budget | Armenian | Proposal |
|---|---|---|---|---|
| 11.1 | **22a-c** verification strip | 22 hard | 24, 25, 25 | **Raise to 26 in all three locales.** `հաշվետվություն` is 14 characters and this slot is the checkable substance on the first screen. Every string that fits 22 drops either a protocol number or the qualifier that makes GPS mean verification rather than location |
| 11.2 | **25a** GPS annotation | 90 | 92 | Raise to 96, or accept 2 over on a soft budget. The overage is the second clause, which is what turns *we record GPS* into *the crew was standing there* |
| 11.3 | **45** one-off chip | 26 hard | 33 for the full form | Either raise to 34 or accept `Մեկանգամյա` alone (10) and lose the denial. I have shipped the short form; the long one is better if the chip can hold it |
| 11.4 | **47a/b** unit chips | uppercase | — | Not a length problem: **the uppercase instruction collides with the ALL-CAPS ban** and with Armenian majuscule metrics. Recommend sentence case with tracking in the Armenian locale. §12.4 |
| 11.5 | **51** year-rail footnote | 120 hard | 134 | **Raise to 140.** The cut that fits 120 removes *four visits either way*, which is the guarantee the footnote exists to state |
| 11.6 | **54a** Express credit line | 60 hard | 69 | **Raise to 72.** Armenian needs the subject of `հաշվառվում է` and the 60-day window in the same clause; splitting them across two lines breaks the card grid |
| 11.7 | **74a** guarantee remedy | 120 | 138 | **Raise to 145.** The overage is `հաշվետվությունն ստանալու օրվանից` — the clause that makes the seven days run from report delivery rather than from the visit, per 26.08 §7.1 |
| 11.8 | **78c-b, 78d-b** timeline bodies | 220 | 240, 249 | Raise to 255. Both carry a list of report contents that cannot be shortened without dropping a protocol item |
| 11.9 | **81** weather paragraph | 420 hard | 599 | **Raise to 610.** The overage is the clause explaining *why* the temperature limit exists, plus the clause saying the visit is not substituted with something else. Without the first, the limit reads as an excuse; without the second, an Armenian reader assumes a swap |
| 11.10 | **88** link-preview explainer | 200 | 204 | Raise to 210, or drop `Ստացողին գրանցում պետք չէ։` — which is the sentence the whole feature exists for |
| 11.11 | **109b** promise echo | 16-18 | 42 | Not solvable and should not be. This slot holds frozen string 16. The budget appears to have been written for a label. Correct the budget |
| 11.12 | **7a-d** footer service links | 22 | 17-21, fits | Fits **only because `AMD` is dropped** in these four link labels. If the bank reviewer requires the full format in every price instance, all four go to 21-25 and the block needs two lines. §12.1 |

**The systemic finding underneath all twelve.** The budgets in
`PROPOSAL-ux.md` §10 were set against English and the file says so —
`EN × 1.30` is the build target. That multiplier is right on average and
wrong exactly where it matters, because Armenian's long words are not
distributed evenly: they cluster in the **nouns this business cannot
avoid**. `հաշվետվություն` (14), `բաժանորդագրություն` (18),
`խորհրդատվություն` (16) and `պատասխանատվություն` (18) are the four most
frequently required nouns on the site, and each is 1.6-2.2× its English
counterpart, not 1.3×. Every over-budget slot above contains one of
those four words. **Recommendation: apply ×1.3 generally and ×2.0 to any
slot whose Armenian must contain one of those four nouns** — which is a
rule the build can check mechanically.

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
   52c are 44 hard and contain two prices each. Writing `AMD` twice puts
   both at 48. I solved it by writing `AMD` once per line, which is
   already a deviation from "without exception" — made visible here
   rather than done quietly.
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

§11.4. Not a disagreement with a person, a collision between two
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
3. **The verification strip cannot be 22 characters** (§11.1). If the
   component is widened for Armenian it should be widened for all three,
   because the Russian `отчёт в течение 48 часов` has the same problem
   and will arrive at the same place a week from now.
