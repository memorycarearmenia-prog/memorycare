# MemoryCare — audit of the authenticated surface under garik (id 4)

**Origin:** https://mc.makyan.com  ·  **Captured:** 5 September 2026, ~16:34 UTC (Yerevan +4)
**Browser:** Chrome (Claude in Chrome) for the live/mirror; Chromium 141 headless for capture.
**Account:** garik (user id 4) — a **populated** account, unlike the empty david (id 5) audited before.

## Why this pass exists

The two prior archives covered the public site and the **empty** david account. A populated account
was expected to expose screens the empty one could not. It does: a **visit-report view**
(`account/objects/view/:id/`), a **populated objects list** with map embeds, a **populated packages
screen** including a real **Paid** state. This archive documents that new surface with the same
treatment; it does **not** re-capture the public site or the empty-state screens.

## What is new here (diff against david's 61 routes)

| New / changed | Under david | Under garik |
|---|---|---|
| `/{loc}/account/objects/view/1|2|4/` | did not exist | **3 visit reports** (photos, video, map, note) |
| `/{loc}/account/objects/` | empty (152 chars) | **populated** — 2 cemeteries, 3 report cards |
| `/{loc}/account/mypackages/` | 1 empty form | **3 packages**, Pay + **Paid** states, 2 pay forms |
| `/{loc}/account/personal-edit/N/` | id 5 | id 4 |
| Crawl total | 61 routes | **70 routes** |

## Headline findings (full detail in 01-FINDINGS.md)

- The visit **report — the actual product — has no structure**: two unlabelled photos, a video and a
  line of text. No "before/after" label, no date, no caption, title in an `<h3>`, no `<h1>`, no `main`.
- **Two of the three reports have an empty GPS map** (`?q=,`) — the location proof, a core selling
  point, is broken on reports 2 and 4 while report 1 has it.
- The **visit-type badges** (`Full` / `Preventive`) fail contrast at **1.99** and **1.75**, and the
  dates on the objects list reach **1.38** — the least legible text on the whole site.
- The **pay form** carries the amount in a browser-controlled hidden field (`price=40000`), on the
  real payment path — and the withdrawn `40,000 ֏` tariff and the **banned** "Preventive/Full"
  vocabulary are live on a real customer's dashboard.
- The **account area is the least accessible part of the site**: Lighthouse a11y **48** on the report
  and objects pages, against 67–81 public.
- No cross-user data leak: adjacent report ids return **503** (not another person's report) — but 503
  is the wrong status, and proper per-object authorization still needs the owner check in Q1.

## Personal data

**None real in the archive.** The account's real name, phone, e-mail, grave GPS coordinates and
free-text notes were **substituted before writing**. The grave photos and video are the site's demo
assets, not this family's — so no real grave photographs are present. Full account and verification
in `04-PERSONAL-DATA.md`. The garik and david passwords are in the chat transcript — **rotate both.**

## Files

`01-FINDINGS.md` (defects / observations / questions) · `02-INVENTORY.md` (coverage matrix) ·
`04-PERSONAL-DATA.md` · `screens/` (180 PNGs) · `dom/` `text/` `network/` `console/` `a11y/` `perf/`
(18 route×locale each) · `measurements.json` · `capture-log.json` · `manifest.json` ·
`mirror-manifest.json`.

## Method notes

Same as before: sandbox can't reach the origin, so the site was mirrored through the signed-in
browser (PII substituted before writing), served locally, captured with Playwright at DPR 1,
scrollbars hidden, motion frozen, fonts awaited, scroll returned-and-asserted, both framings.
Every file verified for byte size, per-channel stddev and width — the 18 "failures" are all the 360
full-page width check firing on **real horizontal overflow** (mypackages 452px, reports 361px), a
site defect kept as evidence and marked `fold + full*` in the inventory. No form was submitted, no
payment made, no destructive action taken; the IDOR probe returned booleans only.
