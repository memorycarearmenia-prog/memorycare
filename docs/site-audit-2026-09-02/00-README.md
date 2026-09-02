# MemoryCare — full site audit, public and authenticated

**Origin:** `https://mc.makyan.com`
**Captured:** 2 September 2026, 09:20–10:05 UTC (Yerevan, UTC+4)
**Browser:** Chromium 141 headless for capture and measurement; Chrome 151 on Windows 10 for the
live probes and the mirror
**Baseline state:** logged out at 09:20:56Z, signed in by the account owner at 09:24Z
**Build identifier:** none exists — the asset query strings are `time()` at render, not a build
hash, so there is nothing to quote as a version. The site is byte-for-byte unchanged from the
31.08 capture on every public route.

---

## Can I tell in a minute whether the thing I care about was looked at?

| | |
|---|---|
| **Public marketing site** | Yes — 6 route families × 3 locales × 5 viewports, both framings |
| **Everything behind the login** | Yes — 9 authenticated routes × 3 locales, 5 viewports for the main 5 |
| **Every locale** | Yes — `am`, `ru`, `en`, at equal completeness |
| **1024–1300 navigation band** | Yes — tested at ten widths, answered precisely (finding A-section, §9.1) |
| **Forms submitted** | **No** — nothing that writes data was submitted. See `03-GAPS.md` §1 |
| **Payment** | **No** — deliberately stopped at the last screen before money moves |
| **Logout / post-logout session** | **No** — see `03-GAPS.md` §2, with the two-minute procedure to close it |
| **Screen reader** | **No** — structural failures recorded, experience not heard |
| **Real personal data in the archive** | **None** — substituted before writing. See `04-PERSONAL-DATA.md` |

---

## What is here

| File | What it is |
|---|---|
| `00-README.md` | This file |
| `01-FINDINGS.md` | 16 defects, 9 observations, 5 open questions — and **4 corrections to the 31.08 audit** |
| `02-INVENTORY.md` | The coverage matrix, all five axes, every cell captured or skipped-with-reason |
| `03-GAPS.md` | Everything not tested, why, and how to close it |
| `04-PERSONAL-DATA.md` | What was substituted, how it was verified, what is safe to circulate |
| `screens/` | **380 PNGs** |
| `dom/` | Rendered `outerHTML` after scripts, 36 route × locale files |
| `text/` | Extracted visible strings, 36 files, diffable |
| `network/` | Request log per route: URL, type, method, failures |
| `console/` | Console output per route, verbatim |
| `a11y/` | axe-core 4.10.2 violations per route, JSON |
| `perf/` | Lighthouse desktop profile, 8 routes, raw JSON |
| `measurements.json` | Head metadata, type ramp, contrast pairs, focus order, per route |
| `capture-log.json` | Every file with byte size, dimensions, stddev, pass/fail |
| `manifest.json` | route × locale × viewport × state → filename |
| `mirror-manifest.json` | Per-route HTTP status, final URL, redirect flag, byte size, sanitised flag |

## Naming

```
<route>__<locale>__<width>__<state>.png
home__en__1440__default-fold.png
home__en__1440__default-full.png
acct-packages__ru__360__default-full.png
carousel-reviews__am__1440__slide-2.png
```

`<locale>` is the site's own code — `am`, `ru`, `en`. The specification calls for `hy`; that
divergence is a finding in the 31.08 archive. `root__none__…` is the bare `/`.

**Both framings exist for every cell.** Where a page fits inside the viewport the two files are
byte-identical — that happens in **50 cells** and `02-INVENTORY.md` marks each as `fold = full`
rather than pretending they are two observations.

## Verification, and what the numbers mean

Every file was checked for byte size > 2,000, per-channel standard deviation > 3.0, and width equal
to the requested viewport.

- **378 captures, 0 blank or uniform failures, 0 fold captures failing verification.**
- **30 files failed the width check.** All 30 are `full` captures at 360, and every one is a
  **site defect, not a capture fault**: the full-page screenshot is as wide as the document, so a
  361px file means the page scrolls sideways by 1px and a 452px file means it scrolls sideways by
  92px. `acct-packages` is the 452px case and it puts the Pay button off-screen — finding A2. The
  check was written to catch mis-sized captures and caught a bug instead; the files are kept as
  evidence and flagged in the inventory with `fold + full*`.

## How the captures were made

The sandbox cannot reach `mc.makyan.com`, so the site was mirrored through the signed-in browser —
59 documents and 51 assets, absolute URLs rewritten to local paths, **and the account holder's name,
phone and e-mail substituted before anything was written to disk** — then served locally and
captured with Playwright.

- Device pixel ratio fixed at **1**.
- Scrollbars hidden, so no frame contains one.
- Fonts awaited (`document.fonts.ready` plus a `status === 'loaded'` wait) before every shutter.
- Full height scrolled in 600px steps, network allowed to idle, then the scroll position returned to
  zero **and asserted to be zero** in a loop before capture.
- No resize between the `fold` and `full` capture of the same cell.
- Motion frozen for the matrix; `Math.random` seeded so the animated sky is identical between runs.
  The one thing that only makes sense in motion — the reviews carousel — was captured separately in
  two states, and that is how correction C1 was found.
- **No post-processing of any kind.** No crop, rotation, mirroring or colour adjustment. Every file
  in `screens/` is a raw capture.

## Three things worth knowing before you read the findings

**1. Four claims in the 31.08 audit were wrong, and are corrected here.** The reviews carousel does
advance; the testimonial names are the placeholder "Անուն Ազգանուն" rather than invented real names,
and there are six of them not three; the dram sign is not demonstrably a fallback face; and CLS is
0.099 on desktop, not the 0.000 I generalised from the mobile profile. `01-FINDINGS.md` section D
sets out each one with the evidence that overturned it.

**2. The typography in these screenshots is not what a Windows visitor sees.** The site resolves
every text element to `system-ui`, which is not a font but a pointer to whatever the operating
system provides. Captures ran on Linux. Layout, sizes, weights, colours and contrast ratios are all
computed values and are unaffected; letterforms and line-breaking are not representative.
`03-GAPS.md` §4.

**3. Two console errors on every page are artefacts of the local mirror, not defects.** Both were
checked against the live origin and excluded. `03-GAPS.md` §5.

## The short version

The public site is unchanged from 31.08 — same Lorem Ipsum, same four invented proof figures, same
withdrawn `40,000 ֏` price, same `user-scalable=no`. What is new is what the login hides.

Behind it: a sidebar item that 404s, a Pay button that sits 92px off the screen on a phone, a
password change that needs no current password, an order form with no field for what is being
ordered, an amount travelling in a hidden field on both money forms, two endpoints hard-coded to the
Armenian locale, and no way to cancel anything at all. The account area also scores 52–57 on
accessibility against 81 for the public pages.

Three things are done correctly and are worth saying out loud: login does not leak which accounts
exist, the language switcher preserves your page, and the `og:url` reflection is properly escaped.
Each was probed expecting a problem and did not have one.
