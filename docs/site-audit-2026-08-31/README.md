# MemoryCare site audit — mc.makyan.com

**Captured 31 August 2026, 20:16–20:50 UTC (Yerevan +04).**

## What this is

A complete visual and technical record of the website the contractor (Igor) is building for
MemoryCare LLC at the temporary address `https://mc.makyan.com`, audited against the written
specification the company issued for it.

The short version, before you open anything else: **the build and the specification have no routes
in common.** The specification names 45 routes; the live site serves 14; none of the 14 is one of
the 45. What exists is a generic corporate template — a landing page, a login, a package-order form
and a contact form — with the MemoryCare logo dropped into it, filled with Lorem Ipsum in three
languages, four superseded prices, and four fabricated proof claims. `GAPS.md` is the longest
document here for that reason.

This is a record, not a repair. Nothing was changed on the site or in any repository.

## Which build

The site carries no version identifier — the asset query strings are `time()` at render, not a
build hash (see FINDINGS #41), so there is nothing to quote as a commit. What identifies this
snapshot instead:

| | |
|---|---|
| Origin audited | `https://mc.makyan.com` |
| Snapshot taken | 2026-08-31T20:16:45Z (`screens/../mirror-manifest.json` → `captured`) |
| Documents captured | 48 (14 routes × 3 locales, plus `/`, `/robots.txt`, `/sitemap.xml`) |
| Assets captured | 51, 5.58 MB |
| Specification audited against | `memorycarearmenia-prog/memorycare`, branch `claude/memorycare-knowledge-pdsctw`, commit **`b15fe1a`** |
| Previous audit compared against | `docs/site-audit-2026-08-28/` in the same repository |

## How to read this

| File | What is in it |
|---|---|
| `INVENTORY.md` | The coverage matrix. Every route × locale × viewport × state cell, marked captured or skipped **with a reason**, plus the checks that were not run and the command to run each one. Read this before disputing a gap. |
| `FINDINGS.md` | 41 defects, severity-ordered — 14 blockers, 22 major, 5 minor. Each one names its evidence file or its measured number, quotes the clause it breaches, and states what actually happens. Findings marked **(28.08)** were reported in the previous audit and are still present. |
| `GAPS.md` | Everything the specification names that does not exist, and every state that could not be reached through the interface. |
| `CONTENT.md` | Every user-facing string, by route and locale, with placeholders, wrong-script strings, superseded prices and invented proof flagged. |
| `ACCESSIBILITY.md` | axe-core per route and locale, the keyboard walk, focus-order problems, and contrast measured on rendered output — including a note on where the naive method gives false failures. |
| `PERFORMANCE.md` | Lighthouse mobile per route, live load timings, where the 4.7 MB goes, and what would remove most of it. |
| `screens/` | 242 PNGs. |
| `sheets/` | The ten contact sheets used to review the captures — the review record, not extra evidence. |
| `capture-log.json`, `capture-log-states.json` | Per-file byte size, dimensions and pixel standard deviation for every capture, plus the states that were skipped and why. |
| `measurements.json` | The raw axe, contrast, typography, hit-area, focus-order and string data behind `ACCESSIBILITY.md` and `CONTENT.md`. |
| `contrast-pixel.json` | Contrast measured from element screenshots, for text over photographs. |
| `lighthouse/` | Five raw Lighthouse JSON reports. |
| `mirror-manifest.json` | What was captured from the live site, with per-document status and byte size. |

## File naming

```
<route-slug>__<locale>__<width>__<state>.png
home__am__360__default-fold.png
contact__ru__1440__form-filled.png
home__en__1440__nav-submenu-hover.png
```

`<locale>` is the site's own code — `am`, `ru`, `en` (the specification calls for `hy`, not `am`;
that divergence is FINDINGS #17). `root__none__…` is the bare `/`.

Two framings are captured for every route cell:

- `default-fold` — exactly what the viewport shows on arrival, nothing more.
- `default-full` — the whole page.

Where a page fits inside the viewport the two files are byte-identical, and `INVENTORY.md` says
`fold = full` rather than pretending they are two observations.

## How the captures were made

The sandbox this audit ran in cannot reach `mc.makyan.com` — outbound access to that host is
blocked by network policy. Rather than settle for viewport screenshots taken through a remote
browser, the site was **mirrored byte-for-byte** through the user's browser (all 48 documents, all
51 assets, absolute URLs rewritten to local paths and nothing else changed), served locally, and
captured with Playwright against Chromium 141. Every rendering decision below was therefore under
direct control:

- **Device pixel ratio fixed at 1**, stated here once and true of every file.
- **Scrollbars hidden** (`--hide-scrollbars`), so no frame contains one.
- **Motion frozen** — animation and transition durations forced to zero, `prefers-reduced-motion:
  reduce`, AOS entry animations neutralised, and `Math.random` seeded so the Vanta cloud field is
  identical in every capture and between runs.
- **Lazy content forced** — every page is scrolled to the bottom in 600px steps, the network is
  allowed to go idle, and the scroll position is then returned to zero **and asserted to be zero**
  before the shutter. See the note below on why that assertion exists.
- **Deterministic data** — a static mirror, so the same fixtures, dates and names in every run.
- **No post-processing of any kind.** No crop, no rotation, no mirroring, no colour adjustment.
  The three crops referenced in `FINDINGS.md` (`/tmp/en_hero.png` and friends) were working views
  and are not part of the archive; every file in `screens/` is a raw capture.

## Verification

Two passes, both of which mattered:

**Automated.** Every file is checked for byte size and for per-channel standard deviation. A blank
or near-uniform image fails. All 242 pass; the numbers are in the capture logs.

**Visual.** Every capture was looked at. Folds and interaction states were reviewed in the ten
labelled contact sheets in `sheets/`, at roughly 300px per tile — enough to see layout, emptiness,
truncation and mirroring; full-page captures of the home page and anything a sheet raised a
question about were then opened at full size, and specific regions were cropped and magnified where
a measurement had to be confirmed (the pricing cards, the English footer carousel, the dram sign at
4×). That is the honest description of the review: not 242 individual full-size inspections, but no
file unseen.

**The first capture run was discarded.** Its fold screenshots were taken while the page was still
scrolled near the bottom — `window.scrollTo(0,0)` was being animated by the site's
`scroll-behavior`, and the shutter fired before it landed. The home page at 360 came out with no
header and a headline cut in half, which looked exactly like a site defect and was not. The freeze
stylesheet now goes in before the scroll rather than after it, and the return to the top is
asserted in a loop rather than assumed. Both capture passes were re-run from scratch. This is
recorded because the previous audit shipped three blank full-page shots and two horizontally
flipped screenshots, and the lesson is the same one: a capture you have not verified is not
evidence.

**One finding was withdrawn during review.** A first pass at contrast, computed from resolved
styles, reported white-on-white text on the English home page at a ratio of 1.0. Opening the
screenshot showed dark text on a light panel: the method cannot see a background image and had
silently fallen back to white. Contrast over photographs is now measured from element screenshots
instead, and the numbers in `ACCESSIBILITY.md` come from that. A second apparent finding — an
off-by-one between the pricing cards and the package-order pages — was also checked and withdrawn:
the card links are consistent, the package IDs are simply not in display order.

## Two things to know before you circulate this

**The archive contains personal data.** The browser session used to mirror the site was signed in,
so `account-index__*` and `packages-add-1__*` show the authenticated account pages including the
account holder's name, telephone number and e-mail address. Six files. Remove them before sharing
the archive outside the company.

**One live session was ended during the audit.** An automated link crawl followed
`/am/account/logout/`, which is an ordinary GET link, and signed the account out. That is
FINDINGS #16, and it is the finding demonstrating itself.

## What is not here

- **`recordings/`** — empty, deliberately. The only motion in the build is the decorative cloud
  background, two carousels and a drag handle; none carries information a still does not, and one
  of the carousels does not move at all (FINDINGS #23).
- **Real-network Lighthouse.** The scores in `PERFORMANCE.md` come from the local mirror and are
  optimistic. The command to get real ones is in that file and in `INVENTORY.md`.
- **Submitted-form states.** Sending the contact form creates a real enquiry, registering creates a
  real account, and password reset sends real mail. None was exercised. `INVENTORY.md` lists each
  one with the command to reach it.
- **A screen-reader walkthrough**, and any browser other than Chromium.

## How the archive is delivered

The complete archive is 78 MB, above the per-file transfer limit, so it arrives as six ordinary
zips. Extract all six into the same folder and the archive is whole:

```
MemoryCare-site-audit-2026-08-31-docs.zip           the seven documents, sheets/, the JSON logs
MemoryCare-site-audit-2026-08-31-screens-01of05.zip  screens/  (92 files)
MemoryCare-site-audit-2026-08-31-screens-02of05.zip  screens/  (13 files, the tall full-page captures)
MemoryCare-site-audit-2026-08-31-screens-03of05.zip  screens/  (12 files)
MemoryCare-site-audit-2026-08-31-screens-04of05.zip  screens/  (77 files)
MemoryCare-site-audit-2026-08-31-screens-05of05.zip  screens/  (48 files)
```

Each is a normal zip that Windows Explorer opens directly; they are not split-archive parts. The
five screens zips together contain all 242 captures and nothing else.
