# 01 — FINDINGS

Three separate lists, per §8: **defects** (it is broken), **observations** (it is unusual), and
**questions** (I could not determine this). Nothing has been promoted from the second or third list
to the first to make the report look bigger.

Every finding carries: **Where** (route, locale, viewport, state), **Evidence** (a filename, a
measured number, or a command and its output), **Expected** (quoted from a source where one exists,
or marked as my judgement), and **Actual**.

Sources quoted as *Expected* are the design package in `memorycarearmenia-prog/memorycare` at commit
`b15fe1a` (`docs/design-package-v1/FINAL-UX.md`, `FINAL-CONTENT.md`), the eight Ameriabank site
conditions recorded 11.08.2026, and WCAG 2.1 AA. Where no source exists the line says
**(my judgement)**.

A separate section at the end lists **four corrections to the 31.08 audit** — claims I made then
that this pass proved wrong.

---

# A. Defects

## A1 — A navigation item inside the paid account area is a dead link
Severity: **blocker**
Where:    `/am/account/payments/`, `/ru/…`, `/en/…` — all three locales, all viewports; linked from
          the account sidebar on every authenticated page
Evidence: `acct-payments__am__1440__default-fold.png`. Crawl output: `/am/account/payments/ | 200 |
          | 404 | 1 | 4349 | 0` — HTTP 200, document title `404`, 4,349 bytes, the not-found template.
          The sidebar link is visible in `acct-packages__am__1440__default-fold.png`
          ("Իմ վճարումները" / "Мои платежи" / "My payments").
Expected: A navigation item shown to a signed-in, paying customer leads to its screen. FINAL-UX §2.2
          specifies `/portal/billing/` for payments and invoices.
Actual:   A customer who has paid clicks "My payments" and gets a 404 panel. The server reports the
          failure as success, so nothing monitors it.

## A2 — On a phone the Pay button on "My packages" is off the screen
Severity: **blocker**
Where:    `/{am,ru,en}/account/mypackages/`, 360px
Evidence: `acct-packages__am__360__default-full.png` — the full-page capture is **452px wide against
          a 360px viewport**. Measured layout: the `<form>`, its `button.npaid` and the surrounding
          `<div>` sit at `left: 371px`, i.e. entirely outside the viewport; `document.documentElement
          .scrollWidth` is 452. The same file shows the table row overlapping itself —
          "Պրոֆիլակտիկ - 8" is drawn on top of "Լիարժեք - 4".
Expected: The primary action on a customer's billing screen is reachable on the primary channel
          **(my judgement — no layout source covers this screen, because the specification does not
          have this screen)**.
Actual:   The only way to pay is to scroll the page sideways, on a screen whose row content is
          already illegible from overlap. At 1440 the same screen is fine
          (`acct-packages__am__1440__default-fold.png`), so this is invisible to anyone testing on a
          laptop.

## A3 — Changing the password requires no current password
Severity: **blocker**
Where:    `/{am,ru,en}/account/personal-edit/5/`
Evidence: `acct-profile__am__1440__default-fold.png`; form fields, from the rendered DOM
          (`dom/acct-profile__am.html`): `fullname[text]`, `phone[text]`, `email[text]`,
          `password[password]`, `lang[hidden]`. There is no current-password field and no
          re-authentication step.
Expected: A credential change re-authenticates the user **(my judgement — standard practice; no
          project source covers it)**.
Actual:   Anyone holding a live session can silently change the password, e-mail and phone in one
          submit — that is, a borrowed or stolen session becomes permanent account takeover, and the
          real owner loses the recovery address at the same moment.

## A4 — Every page ships all four account links and picks the right two afterwards
Severity: **major**
Where:    every route, every locale, both states
Evidence: The public documents are **byte-identical logged in and logged out** —
          `/am/page/home/` is 23,169 bytes in both, and the `<header>` markup compares equal. The
          markup always contains all four:
          `<li class='enter'>Մուտք</li> <li class='register'>Գրանցում</li>
          <li class='account'>Անձնական հաշիվ</li> <li class='logout'>Ելք</li>`.
          `js/init.js:94-97` reads them and hides two, but only after `checkSession()` completes a
          `POST /am/account/session/`. Measured live: session round trip **70 ms**, document fetch
          157 ms. No CSS rule sets a default state for those classes.
Expected: The server knows who is asking and renders the correct header **(my judgement)**.
Actual:   Every page load shows a logged-out visitor "Personal account" and "Log out" for ~70 ms,
          and a logged-in visitor "Login" and "Register". If JavaScript is blocked or the session
          POST fails, the wrong state is what stays on screen. It also means the header cannot be
          cached per user and the site cannot work without JS.

## A5 — Two endpoints are hard-coded to the Armenian locale
Severity: **major**
Where:    every locale; `js/init.js`
Evidence: `fetch('/am/account/session/', …)` at line 790 and
          `fetch('/am/account/mypackages/pay/', …)` at line 512. Extracted from the live bundle:
          hard-coded `/am/` endpoints = `["/am/account/mypackages/pay/", "/am/account/session/"]`.
Expected: FINAL-UX §2: locale is in the URL from day one and is preserved.
Actual:   A Russian or English customer pressing **Pay** posts to the Armenian endpoint, and every
          page in every locale checks the session against `/am/`. Whatever the server returns —
          messages, redirects, error text — comes back in the wrong language at the moment money
          moves.

## A6 — The price is a hidden field supplied by the browser, on both money forms
Severity: **major**
Where:    `/{loc}/account/packages/add/{1,2,3,4}/` and `/{loc}/account/mypackages/`
Evidence: `dom/acct-order-1__am.html`:
          `<input type="hidden" name="price" value="180000">` alongside `cid=5`, `p=4`, `f=2`.
          `dom/acct-packages__am.html`: `<input type="hidden" name="id" value="13">`,
          `<input type="hidden" name="price" value="240000">`.
Expected: The amount is decided by the server from the product identifier **(my judgement —
          standard practice; the bank's conditions also require that displayed prices be real)**.
Actual:   Both the order form and the pay form carry the amount in a field the client controls.
          Whether the server re-derives it was **not tested** — testing would mean submitting an
          order (see 03-GAPS). Until it is, this is an open exposure on the payment path.

## A7 — The order form has no field for what is being ordered
Severity: **major**
Where:    `/{loc}/account/packages/add/{1..4}/`, all viewports
Evidence: `acct-order-1__am__1440__default-fold.png`; `dom/acct-order-1__am.html` — the form
          `#package-order` contains **six hidden inputs and a submit button, and no visible input at
          all**. `/{loc}/account/objects/` ("My objects") is empty on this account and offers no way
          to create one: `text/acct-objects__am.txt` is 152 characters, all of it header and footer
          chrome.
Expected: FINAL-UX §3.1 makes the Plot the central object; §7.8 specifies ordering against a
          chosen plot.
Actual:   A customer subscribes to a year of grave care without ever saying which grave. There is no
          plot object, no cemetery, no address, no area, no monument count, no date.

## A8 — There is no way to cancel anything
Severity: **major**
Where:    the whole authenticated area
Evidence: A grep of every authenticated document for delete / remove / cancel / ջնջ / отмен / удал /
          չեղարկ returns **nothing**. No confirmation dialog exists either.
Expected: Ameriabank's conditions require published refund and cancellation terms; FINAL-UX §12
          specifies `/portal/billing/cancel/` with the pro-rata refund on screen.
Actual:   A subscription product with no cancellation path and no refund policy. §6.8 of the audit
          brief asked me to open a confirmation dialog and cancel out of it; there was none to open.

## A9 — The 404 template drops the language switcher
Severity: **major**
Where:    all 19 routes that render the not-found panel, all locales
Evidence: Language-switcher targets extracted per page: `/am/page/home/` → three links;
          `/am/contact/` → three; `/am/account/mypackages/` → three; **`/am/page/history/` → `[]`**.
          `notfound-tpl__am__1440__default-fold.png` shows the header without `ՀԱՅ РУС ENG`.
Expected: FINAL-UX §5.3 places the switcher in the header utility slot on every viewport — and by
          implication every page.
Actual:   A visitor who lands on any of the 19 not-found routes — which includes four of the six
          menu items — cannot change language without navigating away first.

## A10 — Nineteen routes answer 200 while rendering a 404
Severity: **major**
Where:    listed below, all locales
Evidence: Live status probes, 02.09:
          `/robots.txt` 200 · `/sitemap.xml` 200 · `/am/no-such-page/` 200 · `/zz/` 200 ·
          `/api/` 200 · `/am/account/` 200 · `/am/account/packages-add/` 200 ·
          `/{loc}/page/history/`, `/mission/`, `/values/`, `/publications/news/` 200 ·
          `/{loc}/account/payments/` 200. Full list in `mirror-manifest.json` → `rendersNotFound`.
          By contrast an unknown **locale** does return a real 404: `/xx/page/home/` → **404**,
          22 bytes, no template; `/AM/page/home/` → **404** (the locale is case-sensitive).
Expected: A not-found response carries status 404 **(my judgement, and standard HTTP)**.
Actual:   Search engines, uptime monitors and the browser's own history all record these as working
          pages. The site is inconsistent with itself: an unknown path is a soft 404, an unknown
          locale is a hard 404 with an empty body and no styling.

## A11 — `robots.txt` and `sitemap.xml` do not exist, and the site invites indexing
Severity: **major**
Where:    site-wide
Evidence: `GET /robots.txt` → 200, 4,339 bytes of HTML 404 panel. `GET /sitemap.xml` → 200, same.
          `<meta name="ROBOTS" content="INDEX, FOLLOW"/>` on 36/36 measured pages
          (`measurements.json` → `head.robots`).
Expected: A contractor's staging build is not indexable **(my judgement)**.
Actual:   Nothing prevents indexing, and there is no sitemap for the four-way route reconciliation
          §2 asked for — the crawl and the navigation were the only usable sources.

## A12 — Pinch-zoom is disabled on every page
Severity: **major**
Where:    36/36 measured pages, all locales
Evidence: One distinct viewport meta value across the whole site:
          `width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0,
          minimum-scale=1.0`. axe `meta-viewport` on every page.
Expected: WCAG 2.1 AA 1.4.4 Resize Text.
Actual:   Unchanged since 28.08 and 31.08. With body text at 14–15px on a 360px screen, the reader
          has no recourse.

## A13 — The account area is markedly less accessible than the public site
Severity: **major**
Where:    all authenticated routes
Evidence: Lighthouse desktop accessibility: public pages 67–81, **account pages 52–57**
          (`perf/acct-dashboard-am.json` 52, `perf/acct-packages-am.json` 57,
          `perf/acct-order-1-am.json` 57). Two axe rules fire **only** behind the login:
          `label` (**critical**, `input[name="fullname"]`) and `landmark-unique` (`.menu-wrapper`).
          Three contrast failures on the dashboard alone:
          `rgb(136,136,136)` on `rgb(245,245,245)` = **3.25**; on `rgb(237,237,237)` = **3.03** at
          both 16px and 20px — all against a 4.5 requirement.
Expected: WCAG 2.1 AA throughout, not only on the marketing pages.
Actual:   The part of the product a paying customer actually lives in is the least accessible part
          of it.

## A14 — The Pay button's label fails contrast, and it is the only red on the site
Severity: **minor**
Where:    `/{loc}/account/mypackages/`
Evidence: Measured from computed styles: white on `rgb(255, 0, 0)` at 13.33px = **4.00** against a
          4.5 requirement. Visible in `acct-packages__am__1440__default-fold.png`.
Expected: WCAG 2.1 AA 1.4.3; and the brand palette contains no red.
Actual:   Pure `#FF0000`, off-palette, marginally sub-threshold, on the one control that takes money.

## A15 — The webfont is downloaded twice per page and applied to nothing
Severity: **minor**
Where:    every page
Evidence: A `<link>` in the HTML **and** `@import url('https://fonts.googleapis.com/css2?family=
          Plus+Jakarta+Sans…')` at the top of `css/style.css` — two requests for the same
          stylesheet. Across all 36 measured pages the resolved font families are **`system-ui` (335
          text variants) and `Arial` (21)**. Plus Jakarta Sans appears zero times.
          `css/style.css` contains exactly three `font-family` declarations, the only substantive one
          being `system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif`.
Expected: A font that is paid for in bytes is used **(my judgement)**.
Actual:   Every visitor downloads a variable font in two weights of italic and roman across 200–800,
          twice, and reads the page in their operating system's default face.

## A16 — Seventeen distinct font sizes and no `h1` anywhere
Severity: **minor**
Where:    site-wide
Evidence: Distinct rendered sizes across 36 pages: 12, 13, 13.33, 14, 15, 16, 17, 18, 18.72, 19, 20,
          25, 28, 30, 35, 38, 65px. `measurements.json` → `head.h1` is `[]` on all 36; axe
          `page-has-heading-one` and `landmark-one-main` each fire on all 36.
Expected: WCAG 2.1 A 1.3.1 for the outline; a type scale **(my judgement)** for the rest.
Actual:   No document outline on any page, and a size ramp with four "heading" steps inside 10px.

---

# B. Observations

## B1 — The `og:url` meta reflects the query string, and escapes it correctly
Where:    every page
Evidence: `/am/page/home/?x=%22onmouseover%3D1` →
          `<meta property="og:url" content="https://mc.makyan.com/am/page/home/?x=&#34;onmouseover%3D1">`
          `/am/page/home/?x=%3C%2Ftitle%3E` → `…?x=&lt;%2Ftitle&gt;`
Note:     I probed this expecting reflected XSS and did not find it — quotes and angle brackets are
          entity-escaped. **Tested and refuted.** What remains is cosmetic: any tracking parameter
          ends up in the Open Graph URL, so a shared `?utm_source=…` link advertises itself.

## B2 — Login does not leak which accounts exist
Where:    `POST /am/account/login/`
Evidence: Unknown address → `{"status":"error","message":"Մուտքագրված տվյալները սխալ են"}`.
          Known address, wrong password → **the identical message**. Empty submit →
          `{"status":"error","message":"Լրացրեք պարտադիր դաշտերը"}`.
Note:     §6.1 asked whether the error distinguishes "no such user" from "wrong password". It does
          not. **Tested and clean** — this is done correctly. Two attempts only, deliberately, to
          avoid any lockout risk.

## B3 — Language switching preserves the page
Where:    all page types except the 404 template
Evidence: `/am/contact/` → `РУС` points at `/ru/contact/`; `/am/account/mypackages/` → `/ru/account/
          mypackages/`; `/am/account/login/` → `/ru/account/login/`.
Note:     §5.2 asked whether switching throws you to the home page. It does not, on any page that
          has a switcher. The exception is A9.

## B4 — Security headers are mostly present; there is no CSP
Where:    every response
Evidence: `strict-transport-security: max-age=15552000; includeSubDomains` · `x-frame-options:
          SAMEORIGIN` · `x-content-type-options: nosniff` · `server: LiteSpeed` ·
          `content-security-policy: null`.
Note:     Three of the four are right. The missing one matters more than usual here: six third-party
          origins execute on every page, two of them unpinned (`jquery-latest.min.js`,
          `vanta@latest`), on a site intended to take card payments.

## B5 — The site's CMS login sits at a guessable path
Where:    `/admin/`
Evidence: `GET /admin/` → **200**, 1,341 bytes, title `Մուտք կայքի կառավարման`
          ("Login to site management").
Note:     I did not attempt to authenticate against it. Recorded because it is publicly reachable
          and unadvertised. `/.git/config` correctly returns **403**.

## B6 — A trailing slash is optional and produces a second URL for the same page
Where:    every route
Evidence: `/am/page/home` → 200, 23,299 bytes, **no redirect**. `/am/page/home/` → 200, 23,300
          bytes. No `<link rel="canonical">` on any of the 36 measured pages, and no `hreflang`.
Note:     Two indexable URLs per page, three locales, no canonical to reconcile them.

## B7 — Every page load spends an extra round trip deciding who you are
Where:    every route
Evidence: `POST /am/account/session/` fires on load from `js/init.js:790`; measured live at 70 ms;
          returns `{"loggedIn":true,"user":{"id":5,"email":"…","fullname":"…"}}` with
          `content-type: application/json`.
Note:     Related to A4. The endpoint returns the account holder's name and e-mail to any request
          carrying the session cookie. See Q3.

## B8 — The home page's entire performance cost is one decorative background
Where:    `/{loc}/page/home/`, desktop profile
Evidence: Lighthouse desktop: performance **46–48**, total blocking time **22.4–36.9 s**,
          main-thread work 44.8 s of which **40,596 ms is attributed to
          `vanta@latest/dist/vanta.clouds.min.js`**. The other pages score 98 with 0 ms blocking.
Note:     **Measurement caveat, stated because it changes the size of the number:** this ran
          headless with software WebGL — the console logged "Automatic fallback to software WebGL".
          On a real GPU the figure will be far lower. The attribution is unambiguous even if the
          magnitude is not: one animated sky, plus the 601 KB of `three.js` it needs, is the whole
          story of this page's cost.

## B9 — The account pages carry the banned visit vocabulary
Where:    `/{loc}/account/mypackages/`, `/{loc}/account/packages/add/{1..4}/`
Evidence: `text/acct-packages__am.txt`: `Փաթեթ 4 · 240000 ֏ · Պրոֆիլակտիկ - 8 · Լիարժեք - 4 ·
          25/08/2026`. `text/acct-order-1__am.txt`: `6 այցելություն · 2 լիարժեք այցելություն ·
          4 պրոֆիլակտիկ այցելություն · պայման 5 … պայման 10`.
Expected: FINAL-UX §1: "Every visit is a **full visit**. The words *light*, *preventive*, *heavy*,
          *monthly*, *bestseller*, *most popular*, *tier 1*, *basic*, *premium* do not exist in any
          language."
Note:     Recorded as an observation rather than a defect only because it is the same content
          problem already raised as a blocker in the 31.08 archive; what is new is that it also
          reaches the screens a paying customer sees after purchase, and that package contents there
          read "condition 5 … condition 10".

---

# C. Questions — things I could not determine

## Q1 — Does the server re-derive the price, or trust the hidden field?
Determining this requires submitting an order, which creates a real record. Not done.
**To answer it:** on a staging copy, `POST /am/account/packages/add/1/` with `price` altered and
compare the stored order. Until then A6 stands as an exposure of unknown depth.

## Q2 — Is `/account/personal-edit/5/` protected against reading another user's record?
The user id is in the path. Testing it means requesting another person's personal data, which I will
not do. **To answer it:** the owner should request `/am/account/personal-edit/1/` while signed in as
user 5 and confirm it returns 403 or 404 rather than another person's name, phone and e-mail.

## Q3 — Is the session endpoint CSRF-protected, and does it allow cross-origin reads?
`POST /am/account/session/` takes no CSRF token and returns the account holder's name and e-mail.
A cross-origin page could issue the POST; whether it can *read* the reply depends on the
`Access-Control-Allow-Origin` header, which I did not capture. **To answer it:**
`curl -sSI -X POST https://mc.makyan.com/am/account/session/ -H 'Origin: https://example.com'`.

## Q4 — Which physical font actually draws the dram sign?
See correction C3 below. Computed styles give the declared stack, not the resolved face, and this
capture ran on Linux where `system-ui` resolves differently than on the client's Windows machine.
**To answer it:** on a Windows machine, DevTools → Rendered Fonts on `.m_price`.

## Q5 — What happens after logout, and on Back?
Not tested — see 03-GAPS.

---

# D. Corrections to the 31.08 audit

Four claims in the previous archive are wrong. Each was re-tested here.

## C1 — The reviews carousel **does** advance
**31.08 said:** "Pressing next produces the same three cards… either the slider holds one slide per
view with duplicate content, or the control is not wired to it."
**Actually:** it advances correctly. `carousel-reviews__am__1440__slide-1.png` (sha256 `3cea17d1…`,
159,908 B) and `…slide-2.png` (sha256 `4151aff5…`, 149,121 B) are **different files**. The earlier
comparison was fooled because all six slides carry identical text — only the photograph changes.
The previous byte-size comparison used full-viewport captures where the difference was swamped.

## C2 — The testimonials are not "invented names" — they are placeholders, and there are six
**31.08 said:** "Three cards, each a portrait photograph, a name, a five-star graphic and a Lorem
Ipsum quote… photographs are of real public figures under invented names."
**Actually:** there are **six** slides, three visible at a time, and every one is named
`Անուն Ազգանուն` — literally "Name Surname". Countries: Mexico, Russia, Italy, Germany, France, USA.
Photographs `/uploads/images/persons/01–07.jpg`, none with an `alt`. The substantive problem stands
and is unchanged — real people's photographs presented as customers of a company with no customers —
but the claim about invented names was wrong, and I repeated it from the 28.08 report without
checking.

## C3 — The dram sign is not, demonstrably, a fallback face
**31.08 said:** "it comes from a fallback face (`.m_price` computes to `system-ui, …`)… and sits
visibly smaller and lighter than the digits."
**Actually:** wrapping the two runs and measuring them separately gives an **identical** declared
stack, size and weight for both — digits and `֏` are both
`system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif`, 19px, weight 700, rendered height
22px for each. The glyph is narrower (15px against ~14px per digit) because that is how the
character is drawn, not because a different face served it. Computed style cannot identify the
resolved physical face, so the original claim was not supported by the evidence I had. See Q4.

## C4 — Cumulative layout shift is not zero
**31.08 said:** "CLS is genuinely 0.000 — the layout does not shift. That is the one thing this
build does well."
**Actually:** that was true only of the mobile profile. On the desktop profile the same page measures
**CLS 0.099**, contributed by `body > div.main` (0.082) and the nav submenu (0.018). The earlier
sentence generalised one profile's result to the whole build.
