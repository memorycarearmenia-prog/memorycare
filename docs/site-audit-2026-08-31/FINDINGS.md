# FINDINGS

Severity-ordered. Every finding names its evidence: a file in `screens/`, a measured number from
`measurements.json` / `capture-log.json`, or a command whose output is quoted.

`Expected` quotes the governing clause. Sources are the design package in
`memorycarearmenia-prog/memorycare` at commit `b15fe1a`:
`docs/design-package-v1/FINAL-UX.md`, `FINAL-CONTENT.md`, `DECISIONS.md`, `LEAD-REVIEW.md`,
and `docs/TARIFF-REDESIGN-2026-08-26.md`. Bank requirements are the eight Ameriabank site
conditions recorded on 11.08.2026.

Findings marked **(28.08)** were already reported in the previous audit
(`docs/site-audit-2026-08-28/`) and are still present.

---

## 1 — The home page states four quantities of proof that do not exist
Severity: blocker
Where:    `/am/page/home/`, `/ru/page/home/`, `/en/page/home/`, every viewport
Evidence: `home__am__1440__default-full.png`, `home__ru__1440__default-full.png`,
          `home__en__1440__default-full.png`. String extraction, `CONTENT.md`:
          `150,000 հաճախորդ` · `55+ ծառայություն` · `250000+ գերեզման` · `15 տարվա փորձ`,
          and the same four in Russian and English.
Expected: "No invented proof of any kind: no testimonials, no counts, no years in business, no
          competitor named, no claim of being the only ones." — audit brief §6. FINAL-UX §1:
          "Never 'Most chosen' — we have zero customers and it would be a claim about behaviour
          that has not happened."
Actual:   The company has no customers, has not run its pilot, and was registered in 2026. The page
          claims 150,000 customers, 250,000+ graves serviced and 15 years of experience. **(28.08)**

## 2 — The testimonials are fabricated, with photographs and star ratings
Severity: blocker
Where:    `/am/page/home/` and both other locales, section `.reviews`
Evidence: `reviews__am__1440__slider-slide1.png`, `reviews__am__1440__slider-slide2.png`.
          Three cards, each a portrait photograph, a name, a five-star graphic and a Lorem Ipsum
          quote. One card is attributed to `(Մեկսիկա)` — Mexico. axe reports
          `aria-prohibited-attr` on `.stars-display[aria-label="Rating"]` ×18 nodes.
Expected: As #1 — no testimonials. The previous audit recorded that the photographs are of real
          public figures under invented names.
Actual:   Fabricated endorsements are presented as genuine customer reviews. Beyond the brief's
          prohibition this is a legal exposure in its own right. **(28.08)**

## 3 — The prices on the site are a superseded line-up, and one of them is a cancelled product
Severity: blocker
Where:    `/{am,ru,en}/page/home/` pricing cards; `/{am,ru,en}/account/packages/add/{1,2,3,4}/`
Evidence: `home__am__1440__default-full.png` (crop at y≈3820–4330), `spot-1440.png`.
          Rendered prices: `80000 ֏` · `40000 ֏` · `180000 ֏` · `240000 ֏`.
Expected: FINAL-UX §1, the locked table: Inspection `20,000 ֏ AMD`, Express `65,000 ֏ AMD`,
          Optimal `160,000 ֏ AMD / year` (4 visits), Maximum `200,000 ֏ AMD / year` (6 visits),
          Special "priced after an Inspection".
Actual:   None of the four ruled prices appears anywhere on the site. `40,000` is the repeat-Express
          price that was **cancelled on 25.08.2026** — "правило «повторный Экспресс в тот же год =
          40 000 AMD» ОТМЕНЕНО". The site is selling a product that no longer exists at a price that
          was withdrawn. **(28.08, and the line-up has moved again since)**

## 4 — Five of the six navigation destinations serve a 404 panel with HTTP 200
Severity: blocker
Where:    `/{am,ru,en}/page/history/`, `/page/mission/`, `/page/values/`, `/publications/news/`,
          and any unknown URL
Evidence: `history__am__1440__default-fold.png`, `spot-1440.png` (mission, values, news, notfound
          in all three locales). Response status measured in the browser:
          `/am/page/history/ → 200`, document title `404`, body 4,345 bytes.
Expected: FINAL-UX §2.1 names the marketing routes that must exist; a nav item must lead to its page.
          A not-found response must carry status 404 so search engines and monitoring see it.
Actual:   Four of the five menu entries are dead, and they answer `200 OK`, so they will be indexed
          as real pages. There is no `/404/` route and no `500` template. **(28.08)**

## 5 — Every word of body copy is Lorem Ipsum, in all three languages
Severity: blocker
Where:    all routes, all locales, all viewports
Evidence: `home__am__360__default-full.png`, `home__ru__360__default-full.png`,
          `home__en__360__default-full.png`; `CONTENT.md` flags 25 (am), 26 (ru) and 32 (en)
          placeholder strings on the home page alone. The account dashboard
          (`account-index__am__1440__default-fold.png`) is Lorem Ipsum as well.
Expected: FINAL-CONTENT defines every string with a stable key.
Actual:   A visitor cannot learn what the company does, what is included in a package, or what
          happens after payment. **(28.08)**

## 6 — `<html lang>` is `en` on every page in every locale
Severity: blocker
Where:    all 18 route × locale combinations measured
Evidence: `measurements.json`, `head.lang` — `"en"` for all 18, including
          `/am/page/home/` and `/ru/contact/`.
Expected: Audit brief §6: "`<html lang>` correct on every locale."
Actual:   Screen readers announce Armenian and Russian text with English pronunciation rules, and
          search engines are told every page is English. The `og:locale` meta on the same pages
          correctly says `hy_AM`, so the information exists in the template and is not being used.

## 7 — Pinch-zoom is disabled on every page
Severity: blocker
Where:    all routes, all locales
Evidence: `<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0,
          maximum-scale=1.0, minimum-scale=1.0">` — present in every one of the 48 documents.
          axe: `meta-viewport`, impact **critical**, 18/18 pages.
Expected: WCAG 2.1 AA 1.4.4 Resize Text. The audience is 35–60 and 40–60 year-old buyers.
Actual:   A reader who cannot make out 14px Armenian cannot enlarge it. **(28.08)**

## 8 — The contractor's development site invites search engines to index it
Severity: blocker
Where:    every page; `/robots.txt`
Evidence: `<meta name="ROBOTS" content="INDEX, FOLLOW"/>` in every document.
          `GET /robots.txt` → **200** serving the HTML 404 panel, not a robots file.
          `GET /sitemap.xml` → **200**, same.
Expected: A staging build under a contractor's domain must not be indexable, and the fabricated
          claims in #1 and #2 must not reach a search index under the client's brand.
Actual:   The invented customer counts and testimonials are publicly crawlable. **(28.08)**

## 9 — The registration form takes personal data with no consent, no privacy link and no password confirmation
Severity: blocker
Where:    `/{am,ru,en}/account/register/`, all viewports
Evidence: `register__am__1440__form-empty.png`, `register__am__360__form-empty.png`.
          Fields, from the markup: `fullname`, `phone`, `email`, `password`, `lang` — and nothing
          else. `measurements.json` → `head.labels = 0`; no checkbox, no link to any policy.
Expected: Ameriabank requires a published privacy policy and terms before internet acquiring is
          enabled. The developer task list requires the client-permission checkbox as a separate
          control "с фиксацией даты/IP".
Actual:   Name, phone, e-mail and a password are collected with no stated basis, no policy to
          point at, and no confirmation field. **(28.08)**

## 10 — No form control on the site has a label
Severity: blocker
Where:    `/{loc}/contact/`, `/account/login/`, `/account/register/`, `/account/reset/`
Evidence: `measurements.json` → `head.labels = 0` on all 18 measured pages. Every field is
          `<input type="text">` carrying only a `placeholder`.
          `contact__am__1440__form-empty.png`, `login__am__360__default-fold.png`.
Expected: WCAG 2.1 AA 3.3.2 Labels or Instructions; 1.3.1 Info and Relationships.
Actual:   Placeholder-only fields have no accessible name, and the prompt disappears as soon as
          the user types. The e-mail and phone fields are `type="text"`, so mobile keyboards do not
          adapt and no browser validation applies.

## 11 — 198 images have no alternative text and 126 links have no discernible name
Severity: blocker
Where:    all routes, all locales
Evidence: axe-core 4.10.2 across 18 pages: `image-alt` **critical**, 198 nodes;
          `link-name` **serious**, 126 nodes. Examples: `.back-to-top`,
          `a[href=""] > img[src$="logo.png"]`, `li:nth-child(1) > a[href="#"][target="_blank"]`.
Expected: WCAG 2.1 A 1.1.1 and 2.4.4.
Actual:   The logo link, the back-to-top control and every gallery image are unnamed. **(28.08)**

## 12 — The English slider caption fails contrast against its photograph
Severity: blocker
Where:    `/en/page/home/`, 1440, the carousel above the footer
Evidence: `home__en__1440__default-full.png` (crop y≈5550–6504). Measured from the rendered
          element screenshot, not from tokens: the 18px white caption returns **3.20** against the
          median background luminance and **2.36** against its brighter regions; the 65px heading
          returns **3.02** median, **2.36** over bright regions.
Expected: WCAG 2.1 AA 1.4.3 — 4.5:1 for body text, 3:1 for large text.
Actual:   3.20 against a required 4.5 for the caption; the heading is at the threshold on average
          and below it over the bright part of the image. Both sit on an unscrimmed photograph, so
          the ratio changes as the carousel advances.

## 13 — Neither of the two service promises appears anywhere on the site
Severity: blocker
Where:    all routes, all locales
Evidence: String search across all 18 measured pages: no match for "one business day",
          "48", "рабочего дня", "48 часов", "48 ժամ", or any variant.
Expected: FINAL-UX §1: "Two public service promises, identical in all six places they appear, and
          nobody may soften or sharpen them locally: `We call or write within one business day.` …
          `Your report arrives within 48 hours of the visit.`"
Actual:   Absent. There is nothing to compare across pages because there is nothing to compare.

## 14 — The address and phone are placeholders that read as real, and the registration number is missing
Severity: blocker
Where:    footer on every page, all locales
Evidence: `home__en__1440__default-full.png` (footer crop): `0000, Yerevan, Republic of Armenia`,
          `+374 10-00-00-00`, `info@memorycare.am`.
Expected: Ameriabank requires a real legal address and registration number on the site. The design
          package requires both to appear "as visible TO BE CONFIRMED markers".
Actual:   The placeholders are formatted as though they were real details — a visitor reads
          `+374 10-00-00-00` as a phone number rather than as a gap. The company registration
          number does not appear at all, in any form. **(28.08)**

---

## 15 — Changing locale on an account URL silently drops the visitor into Armenian
Severity: major
Where:    `/ru/account/index/`, `/en/account/index/`, `/{ru,en}/account/packages/add/{1..4}/`
Evidence: Measured with `fetch(..., {redirect:'follow'})` in the browser:
          `/en/account/index/ → 200`, final URL `/am/account/login/`. Same for every `ru` and `en`
          account route.
Expected: FINAL-UX §2: "Language is switched manually and persists in a cookie; a shared link is
          never silently redirected to another locale."
Actual:   An English or Russian speaker who follows an account link is redirected into an Armenian
          sign-in page and loses their language.

## 16 — Signing out happens on a GET, so anything that follows links can end a session
Severity: major
Where:    `/{loc}/account/logout/`
Evidence: `<a href="/am/account/logout/">` in the header of every authenticated page. During this
          audit an automated link crawl reached that URL and terminated the live session — that
          is the finding demonstrating itself.
Expected: A state-changing action must not be reachable by GET. Any prefetcher, crawler, antivirus
          link-scanner or chat-app preview will sign the user out.
Actual:   Sign-out is an ordinary link.

## 17 — The locale codes are `am`, not the specified `hy`
Severity: major
Where:    every URL
Evidence: Routes are `/am/…`, `/ru/…`, `/en/…`. The same documents carry
          `<meta property="og:locale" content="hy_AM">`.
Expected: FINAL-UX §2: "Locale is in the URL from day one — `/en/`, `/hy/`, `/ru/`". `hy` is the
          ISO 639-1 code for Armenian; `am` is Amharic.
Actual:   Every Armenian URL is labelled Amharic. The template already knows the right value.

## 18 — `/` serves Armenian without redirecting, so there is no canonical home
Severity: major
Where:    `/`
Evidence: `root__none__1440__default-fold.png`; `GET /` → 200, 23,287 bytes, Armenian content,
          no redirect. `/am/page/home/` → 200, 23,300 bytes.
Expected: FINAL-UX §2: "`/` redirects to `/en/`."
Actual:   Two URLs serve near-identical documents with no canonical link between them, and neither
          page carries `<link rel="canonical">` or any `hreflang` alternate.

## 19 — The company name is written as two words in the footer and the page title
Severity: major
Where:    every page, all locales
Evidence: `<title>MEMORY CARE LLC</title>`; footer `© 2026 MEMORY CARE LLC`
          (`home__en__1440__default-full.png`, footer crop).
Expected: The project's standing rule: the name is always written `MemoryCare`, one word; the legal
          entity is `MemoryCare LLC`. It is described as the one element that never changes.
Actual:   `MEMORY CARE LLC`, two words, on every page. **(28.08)**

## 20 — The packages have no names, only numbers
Severity: major
Where:    home pricing cards and all four order pages, all locales
Evidence: `home__am__1440__default-full.png` — `Փաթեթ 1` · `Փաթեթ 2` · `Փաթեթ 3` · `Փաթեթ 4`;
          `Пакет 1..4`; `Package 1..4`.
Expected: FINAL-UX §1 names five products; the brief of 06.08 fixes the Armenian names
          `Էքսպրես խնամք` / `Օպտիմալ խնամք` / `Մաքսիմում խնամք` and `Զննում`.
Actual:   Numbered placeholders. Card 3 is visually highlighted, but nothing says why, and the
          package contents are Lorem Ipsum bullet fragments. **(28.08)**

## 21 — Prices are written without thousands separators and without the letters AMD
Severity: major
Where:    pricing cards and order pages, all locales
Evidence: Rendered text `80000 ֏`; markup `80000 &#1423;`.
Expected: FINAL-UX §1: "Currency is always written with both the symbol and the letters:
          `160,000 ֏ AMD`." The bank requires prices and currency to be stated explicitly.
Actual:   `80000 ֏`. The dram sign itself does render — verified at 4× magnification — but it comes
          from a fallback face (`.m_price` computes to `system-ui, -apple-system, "Helvetica Neue",
          Arial`, not the loaded Plus Jakarta Sans) and sits visibly smaller and lighter than the
          digits beside it.

## 22 — The "Partners" section is four empty placeholder tiles
Severity: major
Where:    `/{loc}/page/home/`
Evidence: `partners__am__1440__default-fold.png` — four grey tiles bearing a generic mark.
Expected: As #1 — no invented proof; and a section with nothing in it should not ship.
Actual:   An empty credibility block under the heading `ԳՈՐԾԸՆԿԵՐՆԵՐ` / `Партнёры` / `Partners`.
          **(28.08)**

## 23 — The reviews carousel does not advance
Severity: major
Where:    `/am/page/home/`, `.reviews`
Evidence: `reviews__am__1440__slider-slide1.png` (185,958 B) and
          `reviews__am__1440__slider-slide2.png` (185,951 B), captured before and after clicking
          `.reviews .swiper-button-next` with a 700 ms settle. The two images are visually
          identical.
Expected: A carousel with next/previous controls advances when they are pressed.
Actual:   Pressing next produces the same three cards. Either the slider holds one slide per view
          with duplicate content, or the control is not wired to it.

## 24 — Focusing a text field produces no visible change
Severity: major
Where:    `/{loc}/contact/` at 1440; the same styling applies to login, register and reset
Evidence: `contact__am__1440__form-empty.png` and
          `contact__am__1440__form-focus-first-field.png` are **byte-identical** (92,651 B), as are
          the Russian (95,982 B) and English (93,780 B) pairs. The focus capture was taken after
          `page.focus()` on `input[name="namesurname"]`.
Expected: WCAG 2.1 AA 2.4.7 Focus Visible.
Actual:   No focus ring, no border change, no shadow. A keyboard user filling the form cannot tell
          which field they are in. (Navigation links *do* show a faint focus box — see
          `home__am__1440__focus-visible-tab1..4.png` — so the site is inconsistent, not uniformly
          unfocusable.)

## 25 — Touch targets on the primary channel are far below 44×44
Severity: major
Where:    360, all routes
Evidence: Measured at 360 from the rendered layout (`measurements.json` → `typography360.hits`):
          hamburger `.menu-toggle` **28 × 27**; language links `ՀԱՅ` **33.2 × 22.5**,
          `РУС` **28.7 × 22.5**, `ENG` **32.3 × 22.5**; carousel arrows **27 × 44**;
          the order button `.sp.btn` **205.2 × 30.9**; footer phone link **129.3 × 16**;
          "Forgot your password?" **147.5 × 19.5**.
Expected: Audit brief §6: "Hit areas 44×44 including invisible padding."
Actual:   The three language links sit side by side at 22.5px tall with a few pixels between them —
          the control most likely to be needed by a diaspora visitor is the hardest to hit.

## 26 — Body text on mobile is 14–15px, and one string is 12px
Severity: major
Where:    360, all routes
Evidence: `measurements.json` → `typography360.small`: 225 elements at 15px, 132 at 14px, 24 at
          13px, and `.ctry` (the testimonial country line) at **12px**.
Expected: Audit brief §6: "nothing under 13px, informational text 14px or more, body 16px on
          mobile."
Actual:   The 12px string breaks the floor outright; the bulk of the page body sits at 15px against
          a 16px requirement — with zoom disabled (#7), the reader has no recourse.

## 27 — The language switcher disappears when the mobile menu is open
Severity: major
Where:    360 and 768, menu open
Evidence: `home__am__360__menu-open.png`, `home__ru__360__menu-open.png`,
          `home__en__360__menu-open.png` — the panel lists six nav items and no language control,
          while the closed header (`home__am__360__default-fold.png`) does show `ՀԱՅ РУС ENG`.
Expected: FINAL-UX §5.3 puts the language switcher in the utility slot on every viewport.
Actual:   Opening the menu hides the only way to change language, on the viewport where the menu is
          the primary navigation.

## 28 — The mobile menu is live between 1024 and 1300px with no way to open it
Severity: major
Where:    widths where `.menu-toggle` is hidden but `menu.js` still treats the layout as mobile
Evidence: `js/menu.js` gates outside-click closing and submenu toggling on `window.innerWidth <=
          1300`. At 1024 the capture run found `.menu-toggle` not visible and skipped the
          `menu-open` state (recorded in `capture-log-states.json` → `skipped`).
Expected: One breakpoint set, shared by CSS and script — FINAL-UX §5.1: "Breakpoints — one set, for
          everyone."
Actual:   Between the CSS breakpoint and 1300px, clicking a parent nav item calls
          `preventDefault()` and toggles a class instead of navigating, on a layout that shows the
          desktop menu.

## 29 — The contact form sits far below the fold at 360, behind an empty screen
Severity: major
Where:    `/{loc}/contact/`, 360
Evidence: `contact__am__360__default-fold.png` — opening hours and one paragraph, then blank to the
          bottom of the viewport. `contact__am__360__default-full.png` is 1,721px tall; the first
          field appears well past the fold. At 768 the fields appear only at the very bottom of a
          1,839px page.
Expected: FINAL-UX §5.7 fixes what must be above the fold at 360 for every route.
Actual:   On the primary channel, the page whose only purpose is the form opens with no form and a
          screen of empty white.

## 30 — The photography is from the wrong business
Severity: major
Where:    `/{loc}/page/home/`, the carousel above the footer
Evidence: `home__en__1440__default-full.png`, crop y≈5550–6220: a stock photograph of a nurse in
          scrubs with a stethoscope, carrying the caption "What is Lorem Ipsum?".
Expected: FINAL-UI's photography direction; the brand is explicitly "NOT funeral-cliché" but it is
          also not a clinic.
Actual:   Medical stock imagery on a memorial-plot care site. Other slides do show cemetery
          imagery, so the set is mixed rather than uniformly wrong.

## 31 — The home page weighs 4.8–5.9 MB
Severity: major
Where:    `/{loc}/page/home/`
Evidence: Lighthouse mobile profile against the byte-exact mirror: total byte weight
          **4,772,362 B** (am), **4,771,932 B** (ru), **5,867,020 B** (en). Live measurement of the
          same-origin asset set for the Armenian home page: **3,746 KB** over 29 requests, plus
          five third-party files.
Expected: The primary channel is a 360px phone, and a large part of the audience is on mobile data
          abroad.
Actual:   Roughly 5 MB for a page whose entire text content is placeholder. The contact page, by
          contrast, is 820 KB. **(28.08 raised image weight)**

## 32 — Third-party scripts are pulled from four CDNs, two of them unpinned
Severity: major
Where:    every page
Evidence: `https://code.jquery.com/jquery-latest.min.js`,
          `https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.clouds.min.js`,
          `https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js`,
          `https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.{css,js}`,
          `https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans…`
Expected: A site that will take card payments should not execute code it does not pin.
Actual:   `jquery-latest.min.js` has been frozen by the jQuery CDN since 2014 and is not the latest
          anything; `vanta@latest` resolves at request time, so the site's behaviour can change
          without a deploy. There is no Subresource Integrity attribute on any of them.

## 33 — A Google Maps iframe is embedded with no title and no consent step
Severity: major
Where:    `/{loc}/contact/`
Evidence: axe `frame-title` **serious**, 3 nodes; the iframe `src` is a `google.com/maps/embed`
          URL. `measurements.json` → `head.iframes` shows `title=NONE`.
Expected: WCAG 2.1 A 4.1.2 for the missing name. For consent: the site has no privacy policy at all
          (#9), so a third-party embed that sets cookies has nothing to disclose against.
Actual:   Unnamed frame, no consent, no policy.

## 34 — There is no `h1`, no `main` and no `footer` element on any page
Severity: major
Where:    all 18 measured route × locale combinations
Evidence: `measurements.json` → `head.h1 = []` and
          `landmarks = {header: 1, nav: 1, main: 0, footer: 0}` on all 18.
          axe: `page-has-heading-one` 17 pages, `landmark-one-main` 17 pages, `region` 142 nodes.
Expected: WCAG 2.1 A 1.3.1; the visible footer should be a `<footer>`.
Actual:   A visually complete page with no document outline. **(28.08 raised the missing h1)**

## 35 — Titles and descriptions are the contractor's placeholders, or empty
Severity: major
Where:    all routes, all locales
Evidence: `measurements.json` → `head.title` / `head.description`:
          `/am/contact/` → title `Հետադարձ կապի վերնագիր` ("Contact page heading"),
          description `Հետադարձ կապի նկարագրություն` ("Contact page description");
          `/ru/contact/` → `Заголовок контакта`; `/en/contact/` → `Title of contacts`;
          login, register and reset → title `""` on all three locales.
          Every page also carries `<meta name="author" content="MAKYAN SYSTEMS">` and
          `<meta name="keywords" content="Ինֆորմացիոն էջերի բանալի բառեր">` ("keywords for
          information pages").
Expected: FINAL-CONTENT specifies the meta title and description per route and locale.
Actual:   The contractor's own scaffolding text is the live metadata, and three route families have
          no title at all. **(28.08)**

---

## 36 — A floating action button renders as a broken image
Severity: minor
Where:    bottom-right of every page, every viewport
Evidence: Visible in `home__am__360__default-fold.png`, `contact__am__360__default-fold.png`,
          `history__am__360__default-fold.png` and every other fold capture — a rounded tile
          showing the browser's broken-image glyph.
Expected: An element that ships should render.
Actual:   A permanently broken 40×40 control, which is also below the 44×44 minimum.

## 37 — `aria-label` is applied to elements that cannot take it
Severity: minor
Where:    `.stars-display` inside the reviews carousel
Evidence: axe `aria-prohibited-attr`, **serious**, 18 nodes, e.g.
          `div[aria-label="1 / 6"] > .ttexts > .stars-display[aria-label="Rating"]`.
Expected: WCAG 2.1 A 4.1.2.
Actual:   A generic `div` with no role carries `aria-label`, so the label is discarded and the
          rating is announced as nothing.

## 38 — The 404 panel's own message fails contrast
Severity: minor
Where:    `/{loc}/page/history/` and every other 404 panel
Evidence: Computed from rendered styles: `.nothing`, 16px, `rgb(187,187,187)` on
          `rgb(255,255,255)` — **1.92** against a required 4.5. axe `color-contrast` confirms.
Actual:   `Ոչինչ գտնված չէ` / `Ничего не найдено` / `Nothing found!` is barely legible.

## 39 — The testimonial country line fails contrast and breaks the type floor at once
Severity: minor
Where:    `/{loc}/page/home/`, `.ctry`
Evidence: 12px, `rgb(204,204,204)` on `rgb(248,248,248)` — **1.51** against a required 4.5.
Actual:   Both the smallest text on the site and the least legible.

## 40 — No canonical URL and no `hreflang` alternates
Severity: minor
Where:    all pages
Evidence: `measurements.json` → `canonical: null`, `hreflang: []` on all 18.
Expected: Three locales of the same document need reciprocal `hreflang` and a canonical.
Actual:   Absent, which compounds #18.

## 41 — Stylesheets and scripts carry a fresh timestamp on every render, defeating browser caching
Severity: major
Where:    every page, every locale
Evidence: Two documents fetched seconds apart during the same mirror run reference
          `css/style.css?1788207401` and `css/style.css?1788207403` — the query string is
          `time()` at render, not a build stamp. It moves by the number of seconds between requests.
          The same applies to `js/init.js`.
Expected: A cache-busting query must change when the file changes, not when the page is served.
Actual:   Every page view re-downloads `style.css` (50 KB), `init.js` (27 KB) and the rest of the
          local CSS and JS, because the URL is never the same twice. A returning visitor gets no
          benefit from the cache at all. It also means the build carries no version identifier —
          there is no way to tell from the outside which deploy is live.
