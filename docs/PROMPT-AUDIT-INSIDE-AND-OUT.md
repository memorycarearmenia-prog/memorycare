# Audit the site inside and out, and hand back a complete visual record

You have a real browser and you will be given a working login. Your job is
to walk the entire product — the public site **and** everything behind the
login — prove what exists, and hand back an archive that lets someone who
has never opened the site know exactly what it contains and what state it
is in.

You are documenting, not fixing. You will find defects. Record them with
evidence. **Change nothing.**

---

## 0. Before you touch anything

**Credentials.** You will be given a username and password for a real
account. Treat them as secrets:

- Never type them into a page that is not the site's own login form.
- Never write them into a file, a filename, a note, or a commit message.
- Never leave them visible in a screenshot. If a password field shows
  plaintext because you toggled "show password", clear it before capturing.
- If the login form is served over plain HTTP, stop and report it as a
  finding before proceeding.

**The account may contain real personal data** — a real name, a real phone
number, a real address, photographs of a real family's grave. §10 governs
what you may capture and what you must redact. Read it before you log in,
not after.

**Establish the baseline.** Record, before anything else: the exact URL you
were given, the date and time in UTC, your browser and version, your
viewport, and whether you are logged out. Every observation you make is
worthless without knowing which build you were looking at.

---

## 1. What "complete" means

Complete is not "every page". It is:

> **every route × every locale × every viewport × every state**, plus
> **every window that can open on top of them**, plus **every step of every
> flow**, in **both** the logged-out and logged-in condition.

A page you screenshotted once, in English, at 1440, logged out, in its
default state, is roughly two per cent documented.

Build the coverage matrix **first** (§3). Capture against the matrix. A
cell you skip is a cell you **mark as skipped and explain**. It is never a
cell you quietly omit. The single most common failure in this kind of work
is a report that looks complete because the gaps are invisible.

---

## 2. Enumerate from the source, never from memory

Do not derive the page list by clicking around and hoping you saw
everything. Derive it four ways and reconcile them:

1. **`sitemap.xml`** and any `robots.txt` it references.
2. **Every internal link on every page you reach** — crawl breadth-first,
   following only same-origin links, and keep going until the frontier is
   empty. Record the depth at which each route first appeared.
3. **The navigation**, at every viewport, in every locale, logged out
   **and** logged in — the menus differ, and that difference is itself a
   finding.
4. **The client-side router, if there is one.** Read the bundled JS for
   route tables, and read any framework manifest. Routes that exist in the
   code but are unreachable by link are a finding worth having.

Reconcile the four lists. Every route that appears in one and not another
gets a line in the report saying which sources knew about it.

**Then do the same for the authenticated area**, because a crawl of the
public site will not find it.

---

## 3. The coverage matrix

Build it before capturing. It has these axes.

**Axis 1 — route × locale × viewport, default state.**
Locales: every one the switcher offers. Viewports: **1920, 1440, 1280,
1024** as the primary set, plus **360** as a single evidence column.

> The 1024–1300 band is not optional. A known defect lives exactly there
> and it is invisible at 1440. See §9.

**Axis 2 — windows that open on top.** Menus, submenus, dropdowns, modals,
drawers, bottom sheets, lightboxes, tooltips, popovers, toasts, date
pickers, comboboxes, confirmation dialogs, cookie banners, share sheets.
For each: does it exist, how is it opened, what closes it, and what is
behind it.

**Axis 3 — interaction states**, for every interactive element:
`default · hover · focus-visible · active/pressed · disabled · loading ·
error · success · empty · filled · overflowing`.

Focus states matter more than hover. Reach every one with the **keyboard**,
not the mouse, and say what the focus ring looks like — or that there
isn't one.

**Axis 4 — flows, step by step.** Each flow is a sequence of captures, not
one screenshot. Both the happy path and at least one failure path.

**Axis 5 — the logged-out / logged-in split.** Every public route again,
while authenticated. Headers, nav and calls to action commonly change and
nobody ever checks.

---

## 4. Screenshot rules — this is where such work usually goes wrong

**Two framings for every capture, always:**

- `fold` — exactly what the viewport shows, nothing scrolled.
- `full` — the entire page, stitched.

Where the page fits inside the viewport the two files are identical. **Say
that explicitly in the manifest.** Do not silently produce one file, and do
not pretend a short page was cropped.

**Before each capture:**

- Wait for the network to be idle **and** for fonts to have loaded. A
  screenshot taken mid-swap shows the fallback face and misrepresents the
  typography.
- Scroll the full height once, then return to the top, so lazy-loaded
  images and scroll-triggered content have rendered. Then wait again.
- Disable animations only if you also capture the animated state
  separately. A frozen carousel is not the same evidence as a moving one.
- Do not resize the window between the `fold` and the `full` capture of the
  same cell.

**Naming.** One scheme, used everywhere, machine-parseable:

```
<route>__<locale>__<width>__<state>.png
home__en__1440__default-fold.png
home__en__1440__default-full.png
account-reports__ru__1280__empty-full.png
form-request__hy__1024__error-phone-fold.png
```

**Verify every single file** and record the numbers:

- byte size > 2,000
- per-channel standard deviation > 3.0 (a blank or single-colour capture
  fails this and is the classic silent failure)
- dimensions match the requested viewport width

Any file that fails is recaptured. If it fails twice, it goes in the report
as a defect with the reason.

---

## 5. Flows to walk, logged out

For each: capture every step, then deliberately break it and capture that.

1. **The consultation request.** Empty submit. One field at a time. An
   invalid phone. A valid international phone. A very long name. Paste
   emoji. Submit twice quickly. Capture: the empty form, each error, the
   filled form, the loading state, the success state, and what the page
   looks like after.
2. **Language switching**, from every page, in every direction. Does it
   keep you on the same page or throw you to the home page? Does the URL
   change? Does the `lang` attribute change?
3. **The pricing / package selection path**, as far as it goes without an
   account.
4. **Every 404 and error route** you can provoke: a nonexistent path, a
   nonexistent locale, a malformed query string. Record the **HTTP status**
   next to each — a 404 page served with `200` is a real defect.
5. **Search**, if there is one: no results, one result, many, special
   characters.
6. **Cookie/consent**, if present: accept, reject, and what happens on
   reload.

---

## 6. Flows to walk, logged in

Log in and repeat the crawl. Then walk these.

1. **Login itself:** wrong password, wrong username, empty submit, correct
   credentials. Capture each error. Note whether the error distinguishes
   "no such user" from "wrong password" — that is a security finding.
2. **Password reset**, as far as you can take it without a mailbox. Say
   where you stopped.
3. **The account landing page**, first thing after login.
4. **Every screen behind the login**, enumerated the same four ways as §2.
   Orders, subscriptions, reports, invoices, settings, profile, family or
   shared access if it exists, notifications, payment methods.
5. **The empty states.** A new account with no data is the state a first
   real customer sees, and it is the one nobody designs. If the account
   has data, look for a way to see the pre-data view and say so if you
   cannot.
6. **The report view**, if any exists — this is the product. Every part of
   it: metadata, photographs, video, map or coordinates, download, share.
7. **Add / purchase a package**, step by step, and **stop before payment.**
   Do not enter card details. Do not complete a purchase. Capture the last
   screen before money would move and say clearly that you stopped there.
8. **Destructive actions** — cancel, delete, remove. Open the confirmation
   dialog, capture it, and **cancel out.** Never confirm.
9. **Session behaviour:** what happens on a hard reload, on opening a deep
   link in a new tab, after logout, and when you press Back after logout.
   A page that renders from cache after logout is a finding.
10. **Logout**, and then re-verify that every authenticated route now
    redirects rather than rendering.

---

## 7. What to record per page, beyond pictures

For every route, capture the data as files, not as prose:

- **HTTP status, final URL after redirects, and the redirect chain.**
- **The rendered DOM** (`outerHTML` after scripts have run), saved per
  route/locale.
- **All text content**, extracted, so strings can be diffed and searched.
- **`lang` attributes**, `<title>`, meta description, canonical, hreflang,
  Open Graph and any JSON-LD.
- **Every request the page made**: URL, type, size, status, and whether it
  is same-origin or third-party. Name every third-party host and say what
  it is for.
- **Console output**: errors and warnings, verbatim.
- **Computed styles for the type ramp** — for every text element, the
  resolved font-family, size, weight, line-height and colour. This is how
  you catch a font that never loaded and a size below a floor.
- **Measured colour contrast** for every text-on-background pair actually
  present, computed from rendered pixels, with the ratio and a pass/fail
  against 4.5 (text) and 3.0 (non-text graphics and UI boundaries).
- **An automated accessibility pass** (axe or equivalent) per route, saved
  as JSON, plus a manual keyboard walk: tab through the whole page and
  record the focus order, anything unreachable, and anything that traps.
- **Lighthouse or equivalent**, per route, saved as JSON, on the desktop
  profile.

---

## 8. Reporting

Findings are ordered by severity, and every one carries:

- **Where** — route, locale, viewport, state.
- **Evidence** — the exact screenshot filename, or a quoted measurement, or
  a command and its output. Never "it looks wrong".
- **Expected** — quote the source that says what it should be, if you have
  one. If you have no source, say so and mark it as your judgement.
- **Actual** — what is there.

Separate **defects** (it is broken) from **observations** (it is unusual)
from **questions** (I could not determine this). Do not inflate the second
two into the first to make the report look substantial.

If you could not test something, it goes in a **Gaps** section with the
reason. An honest gap is worth more than a confident guess.

---

## 9. Re-test these specifically

Known or suspected defects. Confirm or refute each, with evidence:

1. **The navigation between 1024 and 1300px.** The script is believed to
   treat the layout as mobile below 1300 while the CSS shows the desktop
   menu, so clicking a parent nav item may call `preventDefault()` and
   toggle a class instead of navigating. Test at 1024, 1100, 1200, 1280 and
   1300 and say exactly where the behaviour changes.
2. **`user-scalable=no` / `maximum-scale`** in the viewport meta. Check
   every page.
3. **The English home page headline.** It is believed to read "WHAT IS
   LOREM IPSUM?" with Lorem Ipsum body text, and to be *translated* into
   the other locales. Confirm across all three.
4. **Four claimed proof figures** on the home page (customers, services,
   graves, years of experience). The company has no customers. Capture
   them and quote the numbers.
5. **Testimonials** — reportedly three, with photographs, star ratings and
   Lorem Ipsum quotes. Capture and describe.
6. **Prices.** Record every price string on the site, verbatim, with the
   page it is on. A `40,000` price for a repeat product is believed to be
   live and is a withdrawn price.
7. **The dram sign ֏ (U+058F)** wherever a price appears. Report the
   computed `font-family` actually used for that character versus the
   digits next to it, and the rendered size and weight of each. It is
   believed to fall back to a different face.
8. **Routes that render a 404 template with HTTP 200.** Check every route's
   status against what it renders.
9. **The footer** on every page: the legal entity name and its exact
   spelling, the registration number, the address, the phone. Report them
   verbatim, per locale, and flag any that differ between pages.
10. **Any carousel**: does pressing "next" actually change the content?
    Capture slide 1 and slide 2 and compare the files.

---

## 10. Personal data — read before logging in

The account is real. Photographs of a family's grave, a real name, a real
phone number and a real address are personal data, and one of those
categories is sensitive.

- **Redact before saving**, not after: blur or block out personal names,
  phone numbers, email addresses, postal addresses, plot identifiers tied
  to a named person, and any face. Redact in the image file itself, not
  with a CSS overlay that a viewer can remove.
- **Keep an unredacted copy of nothing.**
- **Never capture** a payment card, a security code, a session token, an
  authorization header, or a URL containing one. If a token appears in a
  URL bar, crop it out.
- Where redaction would destroy the evidence, capture the layout with the
  data replaced rather than hidden — and say in the manifest that the
  content is substituted.
- List in the report **every file that contains any personal data**, so
  someone can decide whether the archive may be circulated.

---

## 11. What you hand back

One archive. Structure:

```
audit-<site>-<YYYY-MM-DD>/
  00-README.md            what this is, when captured, which build, how to read it
  01-FINDINGS.md          severity-ordered, each with evidence
  02-INVENTORY.md         the coverage matrix, every cell captured or skipped-with-reason
  03-GAPS.md              what could not be tested and why
  04-PERSONAL-DATA.md     every file containing personal data
  screens/                every PNG, one naming scheme
  dom/                    rendered HTML per route/locale
  text/                   extracted strings per route/locale
  network/                request logs per route
  a11y/                   axe JSON per route
  perf/                   Lighthouse JSON per route
  measurements.json       type ramp, contrast pairs, computed styles
  capture-log.json        every file, with its verification numbers
  manifest.json           route × locale × viewport × state → filename
```

`00-README.md` must state plainly: what is covered, what is not, and what
you were unable to do. A reader should be able to tell within a minute
whether the thing they care about was looked at.

---

## 12. Rules

- **Change nothing.** No form is submitted that creates a real record, no
  purchase is completed, no destructive action is confirmed, no setting is
  saved. If a flow cannot be walked without writing data, stop at the last
  read-only step and say so.
- **Never invent.** If you did not see it, it did not happen. An empty
  section is better than a plausible one.
- **Do not summarise away the numbers.** "Contrast is poor" is useless;
  "`#7C8654` on `#EFE5D5` measures 3.12 against a 4.5 requirement" is a
  finding someone can act on.
- **Quote, do not paraphrase**, when reporting what a page says.
- **Report your own failures.** A capture that would not verify, a page
  that would not load, a flow you could not complete — each is a line in
  the report, not a silence.
