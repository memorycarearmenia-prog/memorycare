# 02 — INVENTORY: coverage of the NEW authenticated surface

This pass documents only what was **new or changed under garik (id 4)** versus the empty david
account already audited: the populated objects list, the three visit reports, the populated
packages screen, and the profile form at the new user id. The full public site and the empty-state
account screens are in the prior two archives and are not re-captured here.

`screens/` holds **180** PNGs. Verification numbers are in `capture-log.json`; the route
index is `manifest.json`. `fold + full*` marks a full-page file **wider than the viewport** — a
horizontal-overflow finding, not a capture fault.

## Route × locale × viewport (default state)

| Route | Path | 1920 | 1440 | 1280 | 1024 | 360 |
|---|---|---|---|---|---|---|
| `acct-objects` | `/am/account/objects/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-objects` | `/ru/account/objects/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-objects` | `/en/account/objects/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-1` | `/am/account/objects/view/1/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-1` | `/ru/account/objects/view/1/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-1` | `/en/account/objects/view/1/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-2` | `/am/account/objects/view/2/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-2` | `/ru/account/objects/view/2/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-2` | `/en/account/objects/view/2/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-4` | `/am/account/objects/view/4/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-4` | `/ru/account/objects/view/4/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-report-4` | `/en/account/objects/view/4/` | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-mypackages` | `/am/account/mypackages/` | fold = full | fold + full | fold + full | fold + full | fold + full\* (452px) |
| `acct-mypackages` | `/ru/account/mypackages/` | fold = full | fold + full | fold + full | fold + full | fold + full\* (452px) |
| `acct-mypackages` | `/en/account/mypackages/` | fold = full | fold + full | fold + full | fold + full | fold + full\* (452px) |
| `acct-profile-4` | `/am/account/personal-edit/4/` | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-profile-4` | `/ru/account/personal-edit/4/` | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-profile-4` | `/en/account/personal-edit/4/` | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |

## Windows / states on the new surface

| Item | Status |
|---|---|
| Visit-report view (`objects/view/:id/`) | **NEW** — captured, 3 reports × 3 locales × 5 viewports |
| Populated objects list with map embeds | **NEW** — captured |
| Package "Paid" state (`Վճարված է`) | **NEW** — visible on `acct-mypackages`, package 3 |
| Package "Pay" state + pay form | captured; form not submitted (creates a payment) |
| Report id 3 (503) | recorded from crawl; a 503, not a report |
| Photo lightbox on report | none — images are bare `<img>`, no zoom |
| Share / guest-report control on report | **absent** — see FINDINGS and GAPS |
| Map iframe | present on list + report 1; **empty `q=,`** on reports 2 and 4 |

## Not captured / not done

- **Payment** — the Pay button (`Վճարել`) posts a real payment; not pressed. Last read-only screen captured.
- **Cross-user report access (IDOR)** — probed at protocol level only (ids 3/5/6/10/99 → 503, no data read). Not captured as screens.
- **Public marketing site, empty-state account, forms submitted** — in the two prior archives; not repeated.
