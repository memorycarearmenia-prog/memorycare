# 01 — FINDINGS: the authenticated surface under garik (id 4)

This pass audits only what the **garik** account exposes that david's empty account could not: the
populated objects list, the three visit-report pages (`objects/view/1|2|4/`), the populated packages
screen, and the profile form at user id 4. Everything already reported for the public site and the
empty account still stands and is not repeated here.

Format as before: **defects**, **observations**, **questions**, each with **Where / Evidence /
Expected / Actual**. `Expected` quotes `docs/design-package-v1/FINAL-UX.md` at commit `b15fe1a`
where a clause exists, else is marked **(my judgement)**.

All personal data in the evidence is substituted (see `04-PERSONAL-DATA.md`): the real name, phone,
e-mail, grave GPS coordinates and free-text notes were replaced before anything was written.

---

# A. Defects

## A1 — The visit report has no structure: no masthead, no confirmation, no captions, no GPS on screen
Severity: **major**
Where:    `/{am,ru,en}/account/objects/view/1|2|4/`, all viewports
Evidence: `acct-report-4__am__1440__default-full.png`; `dom/acct-report-4__am.html`. The whole report
          is: a title in an **`<h3>`** ("Հաշվետվություն՝ N4"), a coloured visit-type badge, two bare
          `<img>` (before/after grave photos, `/uploads/images/ba/01/{before,after}.webp`) with **no
          alt, no caption, no "before/after" label and no date**, a `<video>`, and one line of note.
          `measurements.json` → `head.outline` for the report is `["H3: Հաշվետվություն… ", "H3:
          Հասցե", "H3: Կոնտակտներ"]` — the two H3s after it are the footer.
Expected: FINAL-UX §7.5 specifies the report as an ordered document: masthead → visit confirmation →
          **GPS block in full** → image blocks **each with a caption** → notes; §8.2 adds a
          "report being prepared" state and a media-failure state.
Actual:   The product a customer pays for is two unlabelled photos, a video and a line of text. A
          viewer cannot tell which photo is "before", when the visit happened, or where — the very
          things the report exists to prove.

## A2 — Two of the three reports have an empty GPS map (`q=,`)
Severity: **major**
Where:    `/{loc}/account/objects/view/2/` and `/view/4/`
Evidence: Raw mirror, `am/account/objects/view/2/index.html` and `/view/4/`:
          `maps.google.com/maps?q=,` — **empty coordinates** — in both map iframes. By contrast
          `/view/1/` carries real coordinates (shown substituted as `q=40.000000,44.000000` in the
          archive) and the objects list carries them too.
Expected: FINAL-UX §8.3(b): the GPS trace is "the entire reason GPS exists, because it turns a
          failure into proof of effort." A report's location proof must be populated.
Actual:   Report 1's map has coordinates; reports 2 and 4 render `q=,`, i.e. a blank Google Maps
          pointing at nothing. The GPS proof — a core selling point — is missing on two of the three
          visits in this account, and there is no way for the customer to tell it is broken rather
          than simply absent.

## A3 — The visit-type badges fail contrast badly, and they are the report's key signal
Severity: **major**
Where:    objects list and every report, all locales
Evidence: Measured on rendered solid colours (`measurements.json`):
          `Լիարժեք` (Full) — white on `rgb(247,161,157)` = **1.99**;
          `Պրոֆիլակտիկ` (Preventive) — white on `rgb(158,202,225)` = **1.75**; both against a 4.5
          requirement. On the objects list the visit dates are worse still: `16/08/2026` =
          **1.38** (`rgb(204,204,204)` on `rgb(238,238,238)`), the section heading "Այցերի
          հաշվետվություններ" = **1.87**, another date = **1.61**. Seven failing pairs on the objects
          list alone. axe `color-contrast` = 120 nodes across the 18 pages.
Expected: WCAG 2.1 AA 1.4.3.
Actual:   The badge that tells a customer what kind of visit happened, and the date it happened, are
          the least legible text on the site — pale colour on pale colour at under 2:1.

## A4 — The pay form carries the amount in a browser-controlled hidden field
Severity: **major**
Where:    `/{loc}/account/mypackages/`
Evidence: `dom/acct-mypackages__am.html`: `<form id="package-pay">` with
          `<input type="hidden" name="id" value="14">` and
          `<input type="hidden" name="price" value="40000">`, and a second with `id=11`,
          `price=240000`. This is the **pay** path, not just the order path (which showed the same
          on david, finding A6 there).
Expected: The amount charged is decided server-side from the package id **(my judgement; and the
          bank's conditions require displayed prices to be authoritative)**.
Actual:   The price the customer is asked to pay sits in a field the browser controls, on the form
          that initiates payment. Whether the server re-derives it before charging was **not tested**
          — testing means submitting a payment (see Questions).

## A5 — A withdrawn price and the banned visit vocabulary are live on a real customer's account
Severity: **major**
Where:    `/{loc}/account/mypackages/` and every report/objects page
Evidence: `text/acct-mypackages__am.txt`: `Փաթեթ 2 · 40000 ֏ · Պրոֆիլակտիկ - 0 · Լիարժեք - 1`;
          `Փաթեթ 4 · 240000 ֏ · Պրոֆիլակտիկ - 8 · Լիարժեք - 4`; `Փաթեթ 3 · 180000 ֏ · Վճարված է`
          (Paid). Vocabulary count on the objects pages: `Լիարժեք` ×4, `Պրոֆիլակտիկ` ×2.
Expected: FINAL-UX §1: every visit is a **full visit**; the words *preventive*, *light*, *heavy*,
          *monthly* "do not exist in any language". The `40,000` repeat-Express price was withdrawn
          25.08.2026.
Actual:   The customer's own dashboard sells "Package 2" at the cancelled `40,000` and breaks every
          package into "Preventive N / Full N" — the exact split the product model forbids. This is
          the same content defect flagged on the public site, now confirmed inside the paid product.

## A6 — The grave photographs and every report image have no alt text
Severity: **major**
Where:    all reports, objects list
Evidence: axe `image-alt` **critical**, 210 nodes across 18 pages. `measurements.json` →
          report images include `/uploads/images/ba/01/before.webp` and `after.webp` with
          `alt: null`. `head.imgsNoAlt` = 14 on each report, 12 on the objects list.
Expected: WCAG 2.1 A 1.1.1.
Actual:   On a page whose entire purpose is a photograph, the photograph has no text alternative — a
          screen-reader user gets nothing from the report at all.

## A7 — The map iframes have no title
Severity: **major**
Where:    objects list and reports
Evidence: axe `frame-title` **serious**, 24 nodes. `measurements.json` → `head.iframes` =
          `["https://maps.google.com/maps?q=… title=NONE", …]`.
Expected: WCAG 2.1 A 4.1.2.
Actual:   Every embedded map is an unnamed frame.

## A8 — On a phone the Pay button is 92px off the screen — same as david, still unfixed
Severity: **major**
Where:    `/{loc}/account/mypackages/`, 360px
Evidence: `acct-mypackages__am__360__default-full.png` is **452px wide against a 360 viewport**.
          Measured: `document.documentElement.scrollWidth` = 452; the `<div>`, `<form>` and
          `button.npaid` all sit 92px past the right edge.
Expected: The primary billing action is reachable on the primary channel **(my judgement)**.
Actual:   Identical to the david finding, on a real customer with three packages to pay. Unchanged.

## A9 — The account area is the least accessible part of the whole site
Severity: **major**
Where:    all authenticated routes
Evidence: Lighthouse desktop accessibility: **objects 48, report-4 48, mypackages 57** — against
          67–81 on public pages and 52–57 on david's account. Same systemic axe failures carry in:
          no `h1` (`page-has-heading-one` 18/18), no `main` (`landmark-one-main` 18/18),
          `user-scalable=no` (`meta-viewport` 18/18), zero `<label>` (`head.labels = 0` everywhere),
          `landmark-unique` 18 nodes (duplicate `.menu-wrapper` landmark).
Expected: WCAG 2.1 AA throughout.
Actual:   The screens a paying customer lives in — their reports and their bill — score in the
          high-40s. The report page at 48 is the lowest score measured anywhere in three audits.

## A10 — The report page ships 1.16 MB, most of it a video that autoplays a demo clip
Severity: **minor**
Where:    `/{loc}/account/objects/view/*/`
Evidence: Lighthouse `total-byte-weight` = 1,157,761 B on report-4 vs 826 KB on the list. The
          `<video>` source is `/uploads/files/video/v.mp4` — the same 2.3 MB demo clip used on the
          public home page (identical path and hash family).
Expected: A per-visit report should carry that visit's own media **(my judgement)**.
Actual:   Every report embeds the site's generic demo video and the generic before/after demo
          photos, so all three "different" visits show the same footage.

---

# B. Observations

## B1 — Adjacent report ids return 503, not a clean 404/403
Where:    `/am/account/objects/view/{3,5,6,10,99}/`
Evidence: Live protocol probe: all five return **HTTP 503**, 807-byte body, no report content, no
          404 template. garik's own reports are ids 1, 2, 4.
Note:     Two things. First, **no cross-user data leaked** — none of the probed ids returned another
          person's report (that is the good news, and it answers the IDOR question at the level I
          can safely test). Second, the server answers a missing or non-permitted object with a
          **503 Service Unavailable**, which is the wrong status: it reads as "the site is down"
          to monitoring and search engines, when the correct answer is 404 (absent) or 403
          (forbidden). The id is sequential and user-supplied in the path, so proper per-object
          authorization still needs the owner check in Question Q1.

## B2 — There is a real "Paid" state, and it renders differently from "Pay"
Where:    `/{loc}/account/mypackages/`
Evidence: `text/acct-mypackages__am.txt`: package 3 shows `Վճարված է` (Paid) with no button, while
          packages 2 and 4 show a `Վճарել` (Pay) button. This is a genuine domain state david's
          empty account could not show.
Note:     Recorded as an observation, not a defect — it works. Worth having in the record because
          the empty-account audit could not confirm the paid path renders at all.

## B3 — The before/after photos and the report video are shared demo assets, not this customer's
Where:    all reports
Evidence: Report images resolve to `/uploads/images/ba/01/before.{jpg,webp}` and `after.*` — the
          same directory as the public home page's before/after slider — and the video is
          `/uploads/files/video/v.mp4`, the public demo clip. Report bodies are Lorem Ipsum.
Note:     This is why `04-PERSONAL-DATA.md` can state there are **no real grave photographs** in this
          account: the media is seeded demo content. If a real customer's report ever carries their
          own photos, the substitution approach must extend to the image files themselves.

## B4 — This looks like a seeded test account, not a live customer
Where:    whole account
Evidence: Phone is a sequential test number, report bodies Lorem Ipsum, notes like "SUBSTITUTED NOTE"
          (was a short test string), demo media throughout.
Note:     The PII was substituted anyway — the discipline is cheap and I cannot be certain — but the
          findings above are about the *build*, and hold regardless of whether the data is real.

---

# C. Questions

## Q1 — Does `objects/view/:id/` enforce that the object belongs to the requester?
The safe probe proved no data *leaked* for ids 3/5/6/10/99 (all 503). It did **not** prove the
control is correct — a 503 could be a crash on someone else's object rather than a deliberate 403.
**To answer it** on a staging copy, or by the owner: create a second account, note one of its object
ids, then request that id while signed in as garik and confirm the response is 403/404 and contains
none of the other account's data.

## Q2 — Does the server re-derive the price on the pay path, or trust the hidden field?
Not tested — pressing Pay initiates a real payment (A4). **To answer it:** on staging, POST to
`/am/account/mypackages/pay/` with `price` altered and confirm the charge uses the server's amount.

## Q3 — Why do reports 2 and 4 have empty GPS while report 1 does not?
Established that they differ (A2); the cause — data-entry gap, a broken save, or a template bug — is
not visible from the front end. **To answer it:** check how the coordinate field is populated when a
report is created in the admin/CMS.
