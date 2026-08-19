# Expert #2 — Russian-language web findings (social listening)

Date of research: 2026-08-19
Analyst: Expert #2 (Russian-language internet), MemoryCare social-listening team
Keyword source: `docs/social-listening/keywords-ru.md` (primary); `keywords-en.md`, `keywords-hy.md` for context.

## Method + hard limitation (read first)

- All research was done via web search (17 query rounds across the RU keyword
  sections 1, 2, 4, 5, 6, 7, 8, 9).
- **Every direct page fetch was blocked by this environment's network egress
  proxy** (pikabu.ru, woman.ru, otvet.mail.ru, trustpilot.com, irecommend.ru,
  iwaly.ru, profibank.am, yerkramas.org all returned EGRESS_BLOCKED). Therefore
  **every entry below is verified only through the search engine's result
  snippet/summary**, never by reading the page itself. Summaries are limited to
  what the snippet clearly confirmed; fields the snippet did not show are marked
  "—". No URLs, handles, dates, or quotes are invented.
- Search budget for the session was exhausted mid-task (shared 200-call limit),
  so a few planned follow-ups (Profi.ru review texts, ya-pomnu.ru reviews,
  Luysar deep-dive, Avito/Youla listings) were not completed — listed under
  "Not covered" below.

Field legend per entry: (1) permalink · (2) keyword(s) + file · (3) platform ·
(4) date · (5) language · (6) summary · (7) outcome/sentiment · (8) author
handle · (9) author profile link · (10) classification.

## Totals

| Classification | Count |
|---|---|
| DIRECT (demand/discussion of grave-care services) | 6 |
| ADJACENT (attitudes, guilt, traditions, legal, Yerevan cemeteries) | 12 |
| COMPETITOR-MENTION (RU-space analogs incl. Armenia-local) | 12 |
| **Total recorded findings** | **30** |
| Brand mentions of MemoryCare / memorycare.am found | **0** |

---

## DIRECT

| # | Permalink | Keywords (file) | Platform | Date | Lang | Summary | Outcome / sentiment | Author | Profile | Class |
|---|---|---|---|---|---|---|---|---|---|---|
| D1 | https://www.woman.ru/psycho/socialization/thread/5618632/ | уборка на кладбище; кто ухаживает (keywords-ru §1, §4) | Woman.ru forum | — (not in snippet) | RU | Thread "Уборка на кладбище", 42 replies; per search summary, discusses a cemetery-maintenance service idea for people who cannot visit relatives' graves themselves. | Active discussion; mixed practical interest. Fetch blocked — reply-level sentiment unverified. | — | — | DIRECT |
| D2 | https://profi.ru/raznoe/uhod-za-mogilami/ | услуги по уходу за могилой, отзывы (keywords-ru §1) | Profi.ru marketplace | current listing | RU | 194 specialists offering grave care in Moscow; 40 verified client reviews; from ~3,000 ₽ per visit; 15–30% discount for regular service; providers send before/after photo+video. | Established paid demand; positive review base. | n/a (marketplace) | n/a | DIRECT |
| D3 | https://uslugi.yandex.ru/213-moscow/category?text=уборка+могил+на+кладбище | уборка могилы заказать (keywords-ru §1, §4) | Yandex.Uslugi marketplace | current listing | RU | 144 cleaners in Moscow offering grave cleaning, average rating 4.6, with reviews and prices. | Marketplace-level demand confirmed in RU market. | n/a | n/a | DIRECT |
| D4 | https://otvet.mail.ru/question/200063301 | заброшенная могила кто отвечает (keywords-ru §4) | Otvet.Mail.ru Q&A | — | RU | Q: "Если за могилой не ухаживают, сколько лет её трогать не будут?" How long before administration declares a grave abandoned; per snippet, one participant describes moving away with no one left to care for the grave while on a pension. | Anxiety about abandoned family graves; unresolved need. | — | — | DIRECT |
| D5 | https://memory.jct.md/2026/08/01/uhod-za-mogiloj-na-rasstoyanii/ | уход за могилой удалённо, из-за границы (keywords-ru §2) | Company blog (Memory, Moldova) | 2026-08-01 | RU | How-to article "Уход за могилой на расстоянии: как заказать уборку кладбища из-за границы": clients in Russia, Germany, Israel, USA; workflow = exact sector/plot + landmarks + pre-sent photos; photo report after each visit; payment after confirmation, accepts transfers from abroad. | Fully articulated remote-care playbook aimed at emigrants. | — (company content) | — | DIRECT |
| D6 | https://xn----7sbbeodexmclhnp0as0mxd.xn--p1ai/uborka-mogil-na-armyanskom-kladbishche/ | уход за могилой армянская диаспора (keywords-ru §2) | Service site (Moscow) | current | RU | Dedicated landing page: grave cleaning and improvement specifically at the Armenian cemetery (Vagankovskoye), Moscow — i.e., a service explicitly targeting Armenian family graves in Russia. | Evidence that Armenian-diaspora-specific grave-care demand is already being addressed in Moscow. | n/a | n/a | DIRECT |

## ADJACENT

| # | Permalink | Keywords (file) | Platform | Date | Lang | Summary | Outcome / sentiment | Author | Profile | Class |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | https://pikabu.ru/story/ukhod_za_mogilami_rodstvennikov_11580593 | уход за могилой родственника (keywords-ru §2) | Pikabu | 2024-07-07 | RU | Post "Уход за могилами родственников": author holds that family should care for graves with their own hands — weeding, fixing/painting the fence; per search summary, some commenters call grave care "an intimate family matter". | DIY/family-duty ethic; potential resistance to outsourcing. | — (fetch blocked) | — | ADJACENT |
| A2 | https://pikabu.ru/story/tiktokersha_kotoraya_prikhodit_nochyu_na_kladbishcha_i_otmyivaet_mogilyi_11197623 | сатисфайинг видео уборка могилы (keywords-ru §10) | Pikabu | 2024-03-06 | RU | Post about a TikToker who visits cemeteries at night and washes strangers' graves — RU audience engaging with the grave-cleaning content genre. | Viral interest in the cleaning-content genre in RU space. | — | — | ADJACENT |
| A3 | https://otvet.mail.ru/question/40320009 | уборка чужой могилы (keywords-ru §4, §8) | Otvet.Mail.ru | — | RU | Q: "Можно ли убирать чужую могилу?" — etiquette/permissibility of tending someone else's grave. | No prohibition per answers; cultural sensitivity visible. | — | — | ADJACENT |
| A4 | https://otvet.mail.ru/question/238659117 | кто ухаживает (keywords-ru §4) | Otvet.Mail.ru | — | RU | Q: "Зачем некоторые люди ухаживают за чужими могилами на кладбище?" — tradition of maintaining graves of neighbors/acquaintances discussed. | Neutral-curious; norm of communal care exists. | — | — | ADJACENT |
| A5 | https://otvet.mail.ru/question/175814397 | уход за могилой (keywords-ru §1) | Otvet.Mail.ru | — | RU | Q "Уход за могилой." — answers discuss low-maintenance solutions (artificial grass, low clover) for those unable to visit often. | Practical workaround mindset when service unknown/unaffordable. | — | — | ADJACENT |
| A6 | https://otvet.mail.ru/question/204941434 | поминальные традиции (keywords-ru §6, §8) | Otvet.Mail.ru | — | RU | Emigrant who could not attend a relative's funeral in Russia asks about customs — distance-vs-duty conflict firsthand. | Frustration/cultural friction of being abroad at time of loss. | karina_zhevachka | — (per snippet attribution) | ADJACENT |
| A7 | https://otvet.mail.ru/question/237896485 | чувство вины (keywords-ru §8) | Otvet.Mail.ru | — | RU | Q "Чувство вины перед умершим" — guilt toward the deceased discussed. | Emotional driver confirmed verbatim in RU Q&A space. | user_299687271 | — | ADJACENT |
| A8 | https://health.mail.ru/consultation/2387757/ | чувство вины (keywords-ru §8) | Health.Mail.ru consultations | 2017-10-12 | RU | "Чувство вины после смерти мамы" — psychologist consultation thread; experts note such guilt is near-universal and irrational. | Validates guilt as mass phenomenon; needs careful, non-pressuring tone. | — | — | ADJACENT |
| A9 | https://aif.ru/dontknows/eternal/kto_otvechaet_za_mogily_vashih_rodstvennikov_na_kladbishche | заброшенная могила кто отвечает (keywords-ru §4) | AiF (national newspaper) | — | RU | Explainer: one responsible person per plot (usually a relative), legally obliged to maintain it but no sanctions; can delegate via power of attorney or a contract with cemetery administration. | Legal frame for "responsibility for the grave" messaging. | AiF editorial | n/a | ADJACENT |
| A10 | https://annataliya.livejournal.com/893908.html | кладбища Армении, культурный контекст (keywords-ru §5, §6) | LiveJournal | — | RU | Travel-blog post "Один день на армянском кладбище" — RU-language description of Armenian cemetery culture and carved tombstones (incl. the famous wedding-massacre khachkar story). | Warm ethnographic interest from RU readers. | annataliya | https://annataliya.livejournal.com/ | ADJACENT |
| A11 | https://www.armmuseum.ru/funeral-cycle-rites | армянские поминальные традиции, Мерелоц (keywords-ru §6) | Armenian Museum of Moscow (RU-lang) | — | RU | Article on Armenian funeral-cycle rites: graves visited on the second day after major feasts and on Merelots; Ktruk memorial meals on days 7/40/anniversary. | Authoritative RU-language source on visit-timing traditions (useful for visit-scheduling copy). | editorial | n/a | ADJACENT |
| A12 | https://www.openbusiness.ru/biz/business/ukhod-za-mogilami-kak-biznes/ | стартап по уходу за могилами (keywords-ru §7) | OpenBusiness.ru | — | RU | Business-idea guide "Уход за могилами как бизнес": named target clients = busy managers/entrepreneurs and emigrants/remote residents; advises entering only where cemetery bureaus don't already offer it. | Independent confirmation of MemoryCare's exact two personas. | editorial | n/a | ADJACENT |

## COMPETITOR-MENTION

| # | Permalink | Keywords (file) | Platform | Date | Lang | Summary | Outcome / sentiment | Author | Profile | Class |
|---|---|---|---|---|---|---|---|---|---|---|
| C1 | https://profibank.am/ru/uhod-za-nadgrobiem-i-mogilami-v-erevane | уход за могилой Ереван (keywords-ru §4) | Profibank.am directory (Armenia) | current | RU | **Yerevan-local**: listing "Уход за надгробием и могилами в Ереване" — cleaning, gravel filling, repair/construction, flower/wreath delivery; one-time or regular year-round; phone +374 96 666 700. Directory also lists **Luysar** — professional monument/grave/cemetery cleaning across Armenia. | Existing local supply, but only directory-level presence; no visible reviews or verification features. | n/a | n/a | COMPETITOR-MENTION |
| C2 | https://iwaly.ru/ | платформа ухода за захоронениями (keywords-ru §7) | iWALY (RU platform + iOS/Android app) | current | RU | Cloud "family burial archive" + remote ordering of cleaning/flowers/photo with verified contractors, before/after photo reports, works across Russia and CIS; celebrity-grave feature. Closest RU functional analog to MemoryCare's portal model. | Mature product; no GPS verification or family sub-accounts advertised in snippets. | n/a | n/a | COMPETITOR-MENTION |
| C3 | https://irecommend.ru/content/kompyuternaya-programma-mobilnoe-prilozhenie-iwaly-arkhiv-zakhoronenii-i-servis-po-ukhodu-za | приложение для ухода за могилой (keywords-ru §3, §7) | iRecommend.ru review site | — | RU | User review of the iWALY app: praised as fast/convenient "for people who cannot visit their relatives' graves"; before/after photos sent; ordering via mobile app appreciated. | Positive; validates app+photo-report UX in RU market. | — (fetch blocked) | — | COMPETITOR-MENTION |
| C4 | https://yandex.ru/maps/org/iwaly_delikatny_servis/240830598616/reviews/?page=2 | отзывы (keywords-ru §7) | Yandex Maps reviews | — | RU | Review page for "Iwaly — Деликатный сервис" (multiple pages of reviews exist). | Reviews present; content not readable via snippet. | various | n/a | COMPETITOR-MENTION |
| C5 | https://www.trustpilot.com/review/tending.app (also https://fr.trustpilot.com/review/tending.app) | Tending.app (keywords-ru §7) | Trustpilot | — | EN/FR | Trustpilot review pages for Tending — the named world analog: cleaning/leveling/restoration of granite, marble, bronze; management via mobile app; invite relatives to share access; before/after photo documentation each visit. | Tending already markets family-shared app access — closest feature overlap with MemoryCare's "family circle"; review texts unread (fetch blocked). | various | n/a | COMPETITOR-MENTION |
| C6 | http://gravecare.cc.ua/ (+ /experience.html) | GraveCareUkraine (keywords-ru §7) | GraveCareUkraine site | operating since 2008 (site 2010) | RU/UA | Grave search, cleaning, permanent care across Ukraine (Kyiv, Poltava, Odesa, etc.); positions itself for clients abroad who cannot supervise work in person; publishes work examples/reviews. | Long-running named analog; diaspora-oriented pitch. | n/a | n/a | COMPETITOR-MENTION |
| C7 | https://gravecare.md/ru/ | уход за могилами (keywords-ru §7 analogs) | gravecare.md (Moldova) | current | RU | "Уход за могилами в Кишиневе" — RU-language Moldovan remote grave-care service (grave search by name/year, photo confirmation, pay-after-photo-report). | Same emigrant-focused model in another post-Soviet small market — closest structural analog to Armenia's situation. | n/a | n/a | COMPETITOR-MENTION |
| C8 | https://yerkramas.org/article/201900/distancionnyj-uxod-za-mogilami-v-minske--belarusi-uborka-i-restavraciya | уход за могилой для диаспоры (keywords-ru §2, §7) | Yerkramas.org — Armenian diaspora newspaper (Russia), RU-lang | — | RU | Article/advertorial "Дистанционный уход за могилами в Минске, Беларуси" (service Verim.by) published on an Armenian-diaspora outlet. | Proof that RU-language Armenian diaspora media already carry remote-grave-care advertorials — a ready channel. | editorial | n/a | COMPETITOR-MENTION |
| C9 | https://ok.ru/group/70000052159572 | (platforms note §11) | Odnoklassniki group | current | RU | Group "Уборка могил в Минске Verim.by", 448 members; Minsk + region, remote service for clients in other cities and abroad. | Small but active social-network presence of a BY analog. | Verim.by | n/a | COMPETITOR-MENTION |
| C10 | https://vk.ru/@uborkamogil-sohranite-pamyat-o-blizkih-pochemu-nuzhno-uhazhivat-za-mogil | (platforms note §11) | VK article (community @uborkamogil, УММ ПЛЮС+, Belarus) | — | RU | VK longread "Почему нужно ухаживать за могилой?" from a Belarusian grave-cleaning company community — content marketing on VK for this niche. | VK used for niche content marketing; community indexed publicly. | @uborkamogil | https://vk.com/uborkamogil | COMPETITOR-MENTION |
| C11 | https://ritualcentr.ru/uhod-za-mogiloy/ | сколько стоит уборка могилы, фото отчёт (keywords-ru §1, §3, §4) | Moscow ritual service | current | RU | "Уход за могилой в Москве — уборка 5 000 ₽, фотоотчёт" — photo report is in the headline offer itself. | Photo report = table stakes in RU pricing pages. | n/a | n/a | COMPETITOR-MENTION |
| C12 | https://ya-pomnu.ru/ | вечный уход за могилой (keywords-ru §10) | "Светлая Память" (all-Russia service) | current | RU | Nationwide RU service: grave care, burial search, flower/wreath laying. | Nationwide aggregator model exists in RU. | n/a | n/a | COMPETITOR-MENTION |

---

## Not accessible / not covered

- **Egress-blocked for direct reading** (entries above are snippet-verified only):
  pikabu.ru, woman.ru, otvet.mail.ru, health.mail.ru, trustpilot.com,
  irecommend.ru, iwaly.ru, profibank.am, yerkramas.org. Reply-level content,
  exact dates, and author handles on these are therefore mostly unrecorded.
- **Login-walled / unindexed — content NOT guessed:** VK private/closed groups,
  Telegram channels and chats (RU-Armenian diaspora chats), Facebook groups,
  Instagram, Avito/Youla listing interiors (no listing pages surfaced in
  accessible search results), Yandex Zen full articles (dzen.ru titles surfaced,
  e.g. "Уборка могил и захоронений. Честный обзор…" https://dzen.ru/a/X9KKFEDbwAn8suuQ —
  content unverified, deliberately not summarized).
- **Not completed due to exhausted search budget:** Profi.ru individual review
  texts; ya-pomnu.ru reviews; Luysar (Armenia) dedicated search; Verim.by site;
  forum.hayastan.com (first query returned no hits from that domain);
  Yerevan-cemetery Google/Yandex Maps reviews.

## Self-verification notes (what was corrected/removed)

1. Removed a planned entry for the Dzen article "Уборка могил и захоронений.
   Честный обзор…" — only the title was confirmed; content never loaded. Moved
   to Not accessible.
2. Removed forumhouse.ru as a source — two targeted queries returned zero
   forumhouse threads; nothing recorded (no fabrication).
3. Verified there are **0 findable mentions of MemoryCare / memorycare.am /
   Мемори Кэр** in RU-language search (§9 brand keywords): all "MemoryCare"
   results are US dementia-care organizations (memorycare.org, memorycare.com).
   Recorded as zero, not as absence of the site.
4. Downgraded profibank.am from "competitor company" to "directory listing that
   also names Luysar" after the follow-up site query showed profibank.am is a
   general Armenian business directory.
5. Re-checked all 30 permalinks against the original search outputs — every URL,
   date, handle, and member-count above appears verbatim in a search result;
   fields not present in snippets are marked "—".

## Patterns (3–5)

1. **Photo/video before-after reports are already the industry standard** across
   the entire RU-speaking market (Moscow, Minsk, Kyiv, Chișinău, marketplaces).
   MemoryCare's photo report alone will not differentiate for RU-speaking
   diaspora; GPS verification + client portal + family sub-accounts is the
   actual gap — none of the RU analogs surfaced advertise GPS or family-circle
   accounts (Tending's shared app access is the nearest overlap).
2. **The two MemoryCare personas are independently confirmed** by RU market
   literature and service copy: every analog pitches (a) emigrants/those abroad
   and (b) busy professionals — exactly the diaspora + local-premium split, and
   RU business guides name them as the canonical client base.
3. **Armenia is a supply vacuum in the RU-language internet.** For "уход за
   могилой Ереван" the only local results are one directory listing with a phone
   number and a mention of Luysar — no reviews, no content, no verification
   offer. Meanwhile Moscow services already run landing pages for the Armenian
   cemetery at Vagankovskoye. RU-language SEO for Yerevan grave care is
   essentially uncontested.
4. **Cultural ambivalence about outsourcing:** Pikabu/Otvet threads show a
   strong "family must do it with their own hands / intimate family matter"
   ethic alongside widespread guilt threads about not visiting. Messaging should
   frame the service as enabling the family's duty (verification, family
   access, presence at Merelots-relevant dates), never as replacing it —
   consistent with the no-guilt-pressure brand rule.
5. **Diaspora RU media is a proven channel:** the Armenian diaspora newspaper
   Yerkramas (RU) already publishes remote-grave-care advertorials for a
   Belarusian service — indicating both audience receptivity and an open,
   low-cost placement route for MemoryCare.
