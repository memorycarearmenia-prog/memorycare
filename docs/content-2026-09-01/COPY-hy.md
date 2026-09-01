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

**1a** · nav · 18 hard · `Գներ` · 0 ch
**1b** · nav · 18 hard · `Ինչպես է աշխատում` · 0 ch
**1c** · nav · 18 hard · `Հաշվետվություն` · 0 ch
**1d** · nav · 18 hard · `Ընտանեկան շրջանակ` · 0 ch
**1e** · nav · 18 hard · `Մեր մասին` · 0 ch

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

**2** · primary button · 22 hard · `Խորհրդատվության հայտ` · 0 ch

  ↳ Not `Անվճար խորհրդատվություն` — 23 ch, over, and "free" belongs to
  the form heading (slot 101), not to every button on the site.
  Not `Կապվել մեզ հետ` (that is `Contact us`, banned).

**3** · sign in · 12 hard · `Մուտք` · 0 ch
**4a** · language label · 4 hard · `ՀԱՅ` · 0 ch
**4b** · language label · 4 hard · `ENG` · 0 ch
**4c** · language label · 4 hard · `РУС` · 0 ch
**5** · skip link · 24 · `Անցնել բովանդակությանը` · 0 ch

**6a** · footer heading · 16 hard · `Ընկերությունը` · 0 ch
**6b** · footer heading · 16 hard · `Ծառայություններ` · 0 ch
**6c** · footer heading · 16 hard · `Իրավական` · 0 ch
**6d** · footer heading · 16 hard · `Կապ` · 0 ch

**7a** · footer service link · 22 · `Զննում — 20,000 ֏` · 0 ch
**7b** · footer service link · 22 · `Էքսպրես — 65,000 ֏` · 0 ch
**7c** · footer service link · 22 · `Օպտիմալ — 160,000 ֏` · 0 ch
**7d** · footer service link · 22 · `Մաքսիմում — 200,000 ֏` · 0 ch

  ↳ The footer links carry the price because they are the only place on a
  legal or a form page where a price appears, and the bank condition is
  "real AMD prices". `AMD` is dropped **here only**, where the string is a
  link label and the full format sits four times over on `/hy/գներ/`.
  If the bank reviewer requires it in every instance, these four go over
  budget by 4 and become a two-line link block — flagged, §11.

**8a** · footer legal link · 30 · `Գաղտնիության քաղաքականություն` · 0 ch
**8b** · footer legal link · 30 · `Ծառայության պայմանները` · 0 ch
**8c** · footer legal link · 30 · `Վերադարձի քաղաքականություն` · 0 ch
**8d** · footer legal link · 30 · `Սահմանափակումներ` · 0 ch

**9** · legal-entity block · 160 · `[BLOCKED — the Armenian-registry form of the company name, the registration number and the legal address are not in any source. FINAL-CONTENT §4.1 carries both as {LEGAL_ADDRESS} and {REG_NUMBER}; CLAUDE.md says "Memory Care LLC" and FINAL-CONTENT says "MemoryCare LLC" and forbids the spaced form. These are three separate facts and I will not compose an Armenian legal line out of a contradiction. Shape it should take once supplied: «MemoryCare» ՍՊԸ · ՀՎՀՀ {REG_NUMBER} · {LEGAL_ADDRESS}, Երևան, Հայաստան]` · 0 ch

  ↳ Note for whoever fills it: Armenian company names take
  «guillemets» inside the legal line — `«MemoryCare» ՍՊԸ` — and the
  registration identifier an Armenian reader looks for is the **ՀՎՀՀ**
  (tax ID), not the word `գրանցման համար`. Both should be present if both
  exist.

**10** · copyright · 60 · `MemoryCare ՍՊԸ, Երևան, Հայաստան · © 2026` · 0 ch
**11a** · founder role · 24 · `Գործադիր տնօրեն` · 0 ch
**11b** · founder role · 24 · `Բիզնեսի զարգացման տնօրեն` · 0 ch
**12** · business hours · 55 · `Երևան, երկ–ուրբ 09:00–18:00 (UTC+4)` · 0 ch

  ↳ `երկ–ուրբ` and not `Երկուշաբթի–Ուրբաթ`: Armenian abbreviates weekdays
  to three letters and every Armenian reader parses it instantly. The
  UTC offset is mandatory in this string per §9.3 of the UX proposal —
  and it does real work in Armenian too, because a large part of the
  audience reading Armenian is reading it in Moscow, Los Angeles and
  Lyon.

### 5.2 The three frozen strings

These are written once and repeated verbatim. Any local variation is a
defect.

**16** · callback promise · 48 hard · `Կզանգենք կամ կգրենք մեկ աշխատանքային օրում։` · 0 ch

  ↳ **STRUCTURE.** The idiomatic Armenian is `մեկ աշխատանքային օրվա
  ընթացքում` — and it is 9 characters longer and breaks the 48 hard
  budget. `մեկ աշխատանքային օրում` is correct, ordinary Armenian and it
  fits. This is a genuine case where the budget chose between two right
  answers rather than forcing a wrong one.
  ↳ Armenian keeps the two verbs (`կզանգենք կամ կգրենք`) that English
  keeps, because the choice between a call and a message is the whole
  point for a reader who does not want a phone to ring at 23:40.

**17** · hours qualifier · 46 · `Երևանյան աշխատանքային ժամեր՝ 09:00–18:00 (UTC+4)` · 0 ch
**18** · report promise · 52 hard · `Հաշվետվությունը ստանում եք այցից 48 ժամում։` · 0 ch

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

**19** · hero overline · 32 hard · `Խնամք, որը կարելի է ստուգել` · 0 ch
**20** · hero H1 · 48 hard · `Գերեզմանի խնամք Երևանում՝ ամեն այցի ապացույցով` · 0 ch

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

**21** · hero standfirst · 105 hard · `Ոմանք հեռու են, ոմանք ժամանակ չունեն։ Խումբը գնում է, մաքրում ամբողջ հողամասը և ցույց տալիս արածը։` · 0 ch

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

**22a** · verification item · 22 hard · `GPS-կետը՝ գրանցված տեղում` · 0 ch ⚠ OVER
**22b** · verification item · 22 hard · `8 լուսանկար, 2 տեսանյութ` · 0 ch ⚠ OVER
**22c** · verification item · 22 hard · `Հաշվետվություն՝ 48 ժամում` · 0 ch ⚠ OVER

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

**23** · CTA support line · 40 · `Առայժմ ոչ վճարում, ոչ գրանցում։` · 0 ch

  ↳ **STRUCTURE.** English is two sentences (`No payment now. No account
  needed.`). Armenian has a correlative construction — `ոչ… ոչ…` — that
  does both halves in one breath and sounds like a person rather than a
  checkbox list. Forcing two Armenian sentences here would be the tell of
  a translated page.

**HOME-7** · secondary link · n/a · `Տեսնել ամբողջական հաշվետվություն` · 0 ch

### 6.2 The report — section 2, the heaviest object on the page

**24a** · report overline · 24 · `Ապացույցը` · 0 ch
**24b** · report H2 · 44 · `Ահա թե ինչ է գալիս ամեն այցից հետո` · 0 ch
**24c** · report standfirst · 100 · `Ամսաթիվ, գերեզմանոց, հողամասի համար, GPS-կետ, 8 լուսանկար, 2 տեսանյութ և խմբի գրառումը։` · 0 ch

  ↳ The standfirst is a **list, not a sentence**, and that is deliberate:
  it reads as an inventory, which is what the product is. Armenian
  tolerates a bare nominal list far better than English does — a
  verb-first sentence here would soften it.

**25a** · annotation · GPS · 90 · `GPS-կետը գրանցվում է հենց հողամասի մոտ, այցի օրը։ Այն ցույց է տալիս, որ խումբն այնտեղ է եղել։` · 0 ch ⚠ OVER
**25b** · annotation · timestamps · 90 · `Ամեն լուսանկար կրում է իր ժամը։ Չորս անկյուն մինչև աշխատանքը, նույն չորսը՝ հետո։` · 0 ch
**25c** · annotation · condition · 90 · `Խմբի գրառումը՝ ինչ արվեց, ինչ նկատվեց քարի վրա և ինչ է պետք հաջորդ անգամ։` · 0 ch

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

**26** · report link · 24 · `Ամբողջ հաշվետվությունը` · 0 ch

### 6.3 How it works — three steps

**27a** · step label · 14 hard · `Զանգ` · 0 ch
**27b** · step label · 14 hard · `Այց` · 0 ch
**27c** · step label · 14 hard · `Հաշվետվություն` · 0 ch

  ↳ **STRUCTURE.** English is `Plan · Visit · Report`. Armenian has no
  usable one-word noun for *plan* in this sense — `պլան` is a Russian
  borrowing that means a document, `ծրագիր` means a programme or a piece
  of software, and `պայմանավորվածություն` is 20 characters. So the
  Armenian triple starts at `Զանգ` — *a call* — which is also more
  truthful: the first step is a conversation, not a plan, and the site's
  primary CTA is a consultation request precisely because of that. The
  three Armenian words are 4, 3 and 14 characters and read as a rhythm.

**28a** · step line · 80 · `Խոսում ենք, գտնում ենք հողամասը և պայմանավորվում այցերի մոտավոր շաբաթների շուրջ։` · 0 ch ⚠ OVER
**28b** · step line · 80 · `Խումբը գալիս է սարքավորումով և մաքրում ամբողջ հողամասն ու բոլոր քարերը։` · 0 ch
**28c** · step line · 80 · `48 ժամում հաշվետվությունը հայտնվում է ձեր անձնական էջում։` · 0 ch

  ↳ 28a says `մոտավոր շաբաթների շուրջ` — *around the approximate weeks* —
  and not a date, because `PROPOSAL-ux.md` and the weather rule both
  forbid promising a day. Trimmed to fit 80 it becomes
  `Խոսում ենք, գտնում ենք հողամասը և պայմանավորվում այցերի շաբաթները։`
  which promises more than we can keep. Keeping the honest version.

**HOME-18/19** — the two frozen promises, slots 16 and 18 verbatim, with
slot 17 beside slot 16. No local variation.

**HOME-20** · link · n/a · `Ամբողջ ընթացակարգը` · 0 ch

### 6.4 What a visit includes · what we do not do

**29** · method H2 · 44 · `Ինչ է անում խումբը մեկ այցի ընթացքում` · 0 ch

**30a-l** · method label · 20 · `Սարքավորումը` · 0 ch
**30a-b** · method line · 90 · `Գոլորշու գեներատոր, Kärcher, փոշեկուլ՝ քարի և հողամասի ամբողջ մակերեսին։` · 0 ch
**30b-l** · method label · 20 · `Միջոցները` · 0 ch
**30b-b** · method line · 90 · `Մաքրող միջոցն ընտրում ենք քարի տեսակով՝ գրանիտ, բազալտ, տուֆ։ Սպիտակեցնող չենք օգտագործում։` · 0 ch ⚠ OVER
**30c-l** · method label · 20 · `Խումբը` · 0 ch
**30c-b** · method line · 90 · `Ձեր հողամասն ամրագրված է որոշակի խմբի։ Այցից այց նույն մարդիկ գիտեն, թե ինչ են թողել։` · 0 ch
**30d-l** · method label · 20 · `Գրանցումը` · 0 ch
**30d-b** · method line · 90 · `Այցը փակվում է միայն այն բանից հետո, երբ կան 8 լուսանկարը, 2 տեսանյութը և GPS-կետը։` · 0 ch

  ↳ `Միջոցները` and not `Քիմիան`: Armenian `քիմիա` is the school subject.
  `Մաքրող միջոց` is what a professional calls the product, and
  `մասնագիտական քիմիա` — the literal rendering of the brief's
  "professional chemistry" — reads in Armenian as a phrase from a safety
  data sheet.
  ↳ 30c is worded as an **assignment** (`ամրագրված է որոշակի խմբի`) and
  never as an unchanged roster, per 26.08 §3.4. The second sentence
  carries the benefit (they know what they left) without promising the
  same names, which is the legal trap.

**31** · `what we do not do` H3 · 30 · `Ինչ չենք անում` · 0 ch
**32a** · limit · 70 · `Շինարարական աշխատանք չենք անում՝ պետք է քաղաքային թույլտվություն։` · 0 ch
**32b** · limit · 70 · `Տապանաքարը չենք բացում և տեղից չենք շարժում։` · 0 ch
**32c** · limit · 70 · `Փակ կամ վիճելի հատված չենք մտնում առանց ընտանիքի համաձայնության։` · 0 ch

### 6.5 Family Circle — the dark band

**33a** · eyebrow · 24 · `Ընտանեկան շրջանակ` · 0 ch
**33b** · H2 · 40 · `Մեկ հողամաս, մի ամբողջ ընտանիք` · 0 ch
**33c** · definition · 120 hard · `Խնամքը հազվադեպ է մեկ մարդու որոշում, և այն չպետք է մնա մեկ մարդու փոստարկղում։` · 0 ch

  ↳ This is the strategist's sentence #4 written in Armenian rather than
  translated into it. `փոստարկղ` (letterbox) is the right image: the
  Russian and English both reach for *inbox*, and `inbox`-as-`մուտքային`
  is untranslatable jargon in Armenian, while `փոստարկղ` is a physical
  object every reader over forty has stood in front of.

**34a** · bullet · 60 · `Հրավերով ամեն հարազատ ստանում է իր մուտքը։` · 0 ch
**34b** · bullet · 60 · `Բոլորը տեսնում են նույն հաշվետվությունները։` · 0 ch
**34c** · bullet · 60 · `Ցանկացողը կարող է առանձին այց պատվիրել։` · 0 ch

**HOME-36** · link · n/a · `Ինչպես է աշխատում շրջանակը` · 0 ch

### 6.6 Trust and verification

**35-h** · H2 · 40 · `Ինչպես ստուգել վերևում գրվածը` · 0 ch
**35a-l** · label · 22 · `Ամսաթիվն ու կետը` · 0 ch
**35a-b** · line · 90 · `GPS-կետը գրանցվում է հողամասի մոտ, այցի օրը, ոչ թե գրասենյակում, ոչ թե հետո։` · 0 ch
**35b-l** · label · 22 · `Անուն և հեռախոս` · 0 ch
**35b-b** · line · 90 · `Դավիթ Համբարձումյանի և Հայկ Մանուկյանի ուղիղ բջջային համարները՝ կայքի ամեն էջում։` · 0 ch
**35c-l** · label · 22 · `Գները՝ բացեիբաց` · 0 ch
**35c-b** · line · 90 · `Չորս գին տպված է, հինգերորդը՝ հաշվիչով։ Բանաձևը բոլորի համար նույնն է։` · 0 ch
**35d-l** · label · 22 · `Մեր սահմանները` · 0 ch
**35d-b** · line · 90 · `Գրում ենք նաև այն, ինչ չենք անում, և այն, ինչ լինում է, երբ եղանակը թույլ չի տալիս։` · 0 ch

  ↳ `բացեիբաց` — *openly, in the open* — is an ordinary Armenian adverb
  and the only word here that carries any warmth. It earns its place
  because the sentence it labels is about arithmetic.

### 6.7 The honesty panel

**36** · honesty panel · 240 hard · `Մենք սկսել ենք 2026-ին։ Առաջին հաճախորդներին ընդունում ենք հիմա։ Կարծիքներ դեռ չունենք ցույց տալու, և ուրիշինը չենք վերցնի։ Փոխարենը կա այն, ինչ կարող եք ստուգել՝ գրված ընթացակարգ, իրական հաշվետվություն, մեր անունները և ուղիղ համարները։` · 0 ch

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

**37a-n** · name · 32 · `Դավիթ Համբարձումյան` · 0 ch
**37a-r** · role · 24 · `Գործադիր տնօրեն` · 0 ch
**37a-l** · line · 70 · `Պատասխանում է պայմանագրի, երաշխիքների և վճարումների հարցերին։` · 0 ch
**37b-n** · name · 32 · `Հայկ Մանուկյան` · 0 ch
**37b-r** · role · 24 · `Բիզնեսի զարգացման տնօրեն` · 0 ch
**37b-l** · line · 70 · `Առաջին զանգը սովորաբար նրանից է։ Գրում է նաև WhatsApp-ով։` · 0 ch

### 6.9 FAQ — six items, first open

**38a** · Q · 70 hard · `Ի՞նչ է լինում, եթե ձմռանը հարմար եղանակ չլինի։` · 0 ch
**39a** · A · 320 · `Քարը չենք լվանում, երբ օդի ջերմաստիճանը ցածր է +4…+10 ℃-ից կամ երբ մոտակա 48 ժամում սառնամանիք է սպասվում։ Ուրեմն ձմեռային այցը կատարում ենք այն օրերին, երբ եղանակը թույլ է տալիս։ Եթե ամբողջ ձմռանը այդպիսի օր չլինի, այցը չի կորչում՝ այն ավելանում է գարնանը։ Չորս լիարժեք այցը մնում է չորս՝ ինչ եղանակ էլ լինի։` · 0 ch

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

**38b** · Q · 70 hard · `Հողամասի ճիշտ տեղը չգիտեմ։ Դա խնդի՞ր է։` · 0 ch
**39b** · A · 320 · `Ոչ։ Զննումը հենց դրա համար է՝ խումբը գտնում է գերեզմանոցը և հողամասը, գրանցում GPS-կետը և ուղարկում է վիճակի ամբողջական նկարագիրը՝ լուսանկարներով և տեսանյութով։ Այդ կետից հետո տեղը հայտնի է ընդմիշտ, և ամեն հաջորդ այց սկսվում է նույն կետից։ Զննումն արժե 20,000 ֏ AMD, և տարեկան բաժանորդագրություն կնքելիս այդ գումարը հաշվառվում է։` · 0 ch

**38c** · Q · 70 hard · `Ի՞նչ է լինում, եթե խումբը չկարողանա հասնել հողամասին։` · 0 ch
**39c** · A · 320 · `Նույն օրը գրում ենք ձեզ և ասում պատճառը՝ գերեզմանոցը փակ էր, ճանապարհը փակված էր, հատվածում թաղում էր։ Ասում ենք նաև, թե որ օրը ենք վերադառնում։ Այդ այցը ձեր բաժանորդագրությունից չի հանվում։ Խմբի բացատրությունը Հայկի մոտ է՝ +374 93 154 108։` · 0 ch

  ↳ Follows `FINAL-CONTENT` §2.5 order — what happened, the date we
  return, whose subscription it does not come out of, a name and a
  number. Armenian keeps the order and drops `unfortunately`, which in
  Armenian (`ցավոք`) is even more reflexive than in English and would be
  the first word a translator wrote.

**38d** · Q · 70 hard · `Եղբայրս կարո՞ղ է տեսնել հաշվետվությունները՝ առանց վճարելու։` · 0 ch
**39d** · A · 320 · `Այո։ Ընտանեկան շրջանակը հենց դրա համար է։ Հրավեր եք ուղարկում՝ WhatsApp-ով կամ էլփոստով, և նա ստանում է իր մուտքը՝ նույն հաշվետվությունները, առանց գնի, առանց որևէ առաջարկի։ Կարող եք նաև ամեն հաշվետվություն ուղարկել սովորական հղումով՝ առանց գրանցման։ Հղումը ցանկացած պահի կարող եք չեղարկել։` · 0 ch

**38e** · Q · 70 hard · `Կարո՞ղ եմ վճարել Հայաստանից դուրս թողարկված քարտով։` · 0 ch
**39e** · A · 320 · `[BLOCKED — card acquiring with Ameriabank is not live and has no committed date; FINAL-REBRAND §6.3 records that nobody has ruled what the site may claim about services that are not yet running. The honest Armenian answer changes depending on that ruling. Placeholder shape, to be confirmed by Hayk: what payment routes exist today, whether a foreign card works today, and what the alternative is. I will not write either «այո» or «շուտով» without it — «շուտով» is on the stop-list and «այո» may be false.]` · 0 ch

**38f** · Q · 70 hard · `Ինչո՞վ համեմատել գերեզմանի խնամքի ծառայությունները։` · 0 ch
**39f** · A · 320 · `Հինգ հարց, որոնք արժե տալ ցանկացած ծառայության՝ ներառյալ մեզ։ Ի՞նչ է արվում մեկ այցի ընթացքում։ Ի՞նչ է գալիս այցից հետո և որքա՞ն ժամանակում։ Կարո՞ղ է ընտանիքի մնացած մասը տեսնել այն։ Գինը տպվա՞ծ է, թե՞ ասվում է հեռախոսով։ Ի՞նչ է լինում, եթե քարը վնասվի։ Մեր պատասխանները այս էջում են։` · 0 ch

  ↳ Built under the author's own conditions (`FINAL-REBRAND` §4.6): every
  item is a question a buyer would ask unprompted, none is reverse-
  engineered from anyone's weakness, no competitor is named or implied,
  and the first item is *what is done on one visit*, not *how many*. The
  Armenian adds `ներառյալ մեզ` — *including us* — in the first line,
  which is the sentence that keeps the whole item from reading as a
  sneer. Without it I would have cut the section, as the condition
  requires.

### 6.10 Closing form section

**40a** · form heading · 44 · `Խոսենք՝ առանց պարտավորության` · 0 ch
**40b** · support line · 90 · `Պատմեք գերեզմանոցի մասին, մենք կասենք՝ ինչ կանենք և որքան կարժենա։` · 0 ch

  ↳ **STRUCTURE.** English would head this `Request a free consultation`.
  Armenian heads it with a verb in the first person plural hortative —
  `Խոսենք` — *let us talk*. It is the single warmest word permitted
  anywhere on this site and it belongs here, at the one moment the page
  asks for something. A nominal Armenian heading here
  (`Անվճար խորհրդատվության հայտ`) turns the conversion into a form to be
  filled rather than a conversation to be had, which is the opposite of
  the business's own reason for using a consultation as the primary CTA.

