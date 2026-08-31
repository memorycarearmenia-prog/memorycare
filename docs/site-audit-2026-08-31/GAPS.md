# GAPS — what the specification names that does not exist

Two kinds of gap are recorded here:

1. **Specified routes and states that are not built.** The written specification for this product is
   `docs/design-package-v1/FINAL-UX.md` in `memorycarearmenia-prog/memorycare` at commit `b15fe1a`.
   It names **45 routes**. The live build serves **14**, and **not one of them is a specified route**
   — the URL shapes do not overlap at all.
2. **States that exist in the build but could not be reached through the interface.** Those are
   listed at the end and each one is a finding in its own right.

---

## 1 · The scale of it

| | Specification | mc.makyan.com |
|---|---|---|
| Marketing routes | 20 (`/en/`, `/en/pricing/`, …) | 6 (`/am/page/home/`, `/am/contact/`, and four that answer 404) |
| Portal routes | 22 (`/portal/…`) | 5 (`/am/account/…`) |
| Public guest routes | 3 (`/r/:shareToken/…`) | 0 |
| Locale prefixes | `/en/` `/hy/` `/ru/` | `/en/` `/am/` `/ru/` |
| Products | 5, named | 4, numbered |
| Routes in common | — | **none** |

The build is not a partial implementation of the specification. It is a different site: a generic
corporate template with a login, a package-order form and a contact form, into which the MemoryCare
name and logo have been dropped. Read the rest of this file with that in mind — almost everything
below is "not started" rather than "incomplete".

---

## 2 · Marketing routes the specification names and the build does not have

Source: FINAL-UX §2.1. `/` is specified to redirect to `/en/`; it does not (FINDINGS #18).

| Specified route | Purpose | In the build |
|---|---|---|
| `/en/` `/hy/` `/ru/` | Home | Only as `/{loc}/page/home/`, with placeholder content |
| `/{loc}/pricing/` | Two bands, calculator, guarantees | **absent** — prices sit on the home page as four numbered cards |
| `/{loc}/how-it-works/` | How it works | **absent** |
| `/{loc}/sample-report/` | The product demo — the thing being sold | **absent** |
| `/{loc}/family-circle/` | The stated differentiator vs Tending | **absent** |
| `/{loc}/guarantees/` | The three named guarantees, in full | **absent** |
| `/{loc}/about/` | About the company — an Ameriabank requirement | **absent**; `/page/history/`, `/page/mission/`, `/page/values/` all answer 404 |
| `/{loc}/contacts/` | Contacts | Exists as `/{loc}/contact/` |
| `/{loc}/consultation/` + modal twin | The primary conversion target | **absent** — the site's main call to action leads to a login form |
| `/{loc}/consultation/thank-you/` | Confirmation | **absent** |
| `/{loc}/pay/` | Payment options | **absent** |
| `/{loc}/pay/bank-transfer/` | Invoice and wire instructions | **absent** |
| `/{loc}/pay/thank-you/` | Payment initiated / awaiting transfer | **absent** |
| `/{loc}/legal/` | Index of the four documents | **absent** |
| `/{loc}/legal/privacy/` | Privacy policy — bank requirement | **absent** |
| `/{loc}/legal/refund/` | Refund policy, where the pro-rata rule lives — bank requirement | **absent** |
| `/{loc}/legal/terms/` | Terms of service — bank requirement | **absent** |
| `/{loc}/legal/limitations/` | Service limitations — bank requirement | **absent** |
| `/{loc}/404/` | Designed not-found page | **absent**; a 404 panel is served with HTTP 200 |
| `/{loc}/500/` | Designed server-error page | **absent / unreachable** |
| `/sitemap.xml` | | **absent** — returns the 404 panel with HTTP 200 |
| `/robots.txt` | | **absent** — returns the 404 panel with HTTP 200 |

The eight stable anchors the specification reserves for navigation, footer, calculator and
advertising — `#inspection` `#express` `#optimal` `#maximum` `#special` `#calculator` `#guarantees`
`#faq` — do not exist. The home page uses `#trust`, `#pricing`, `#how`, `#faq`, `#gallery`,
`#contact`, of which only `#faq` overlaps.

The specified primary navigation is five items: Pricing · How it works · Sample report ·
Family Circle · About. The build's navigation is Home · About us (History / Mission / Values) ·
News · Login · Register · Contact — six items, four of which are dead.

## 3 · Portal routes the specification names and the build does not have

Source: FINAL-UX §2.2. The build has `/{loc}/account/{login,register,reset,index,logout}/` and
`/{loc}/account/packages/add/{1..4}/`. Everything below is absent.

`/portal/login/check-email/` · `/portal/activate/:token/` · `/portal/plots/:plotId/` ·
`/portal/plots/:plotId/visits/` · `/portal/plots/:plotId/documents/` ·
`/portal/plots/:plotId/settings/` · `/portal/visits/:visitId/` · `/portal/visits/:visitId/revisit/` ·
`/portal/family/` · `/portal/family/invite/` · `/portal/family/:memberId/` ·
`/portal/invite/:token/` · `/portal/orders/new/` · `/portal/orders/:orderId/` · `/portal/billing/` ·
`/portal/billing/change/` · `/portal/billing/transfer/` · `/portal/billing/cancel/` ·
`/portal/profile/` · `/portal/profile/notifications/` · `/portal/support/`

The object model behind them is absent too. FINAL-UX §3.1 makes **the Plot** the central object;
the build has no plot, no visit, and no report. The account dashboard
(`account-index__am__1440__default-fold.png`) has a sidebar reading "My objects / My packages /
My payments / My personal data" and a body of Lorem Ipsum.

## 4 · Public guest routes — the entire sharing product

Source: FINAL-UX §2.3 and §13.

`/r/:shareToken/` · `/r/:shareToken/expired/` · `/r/:shareToken/tell-us/` — **none exist.**

The brief asks for the guest report to be checked for price, plan and upsell leakage "and check the
network payload, not just the screen". There is no route, no token, and no payload to inspect. The
check could not be run and is recorded in `INVENTORY.md` as not run rather than as passing.

## 5 · Domain states the brief lists, none of which the build can hold

Every one of these is specified in FINAL-UX §8. None is reachable, because the screens they belong
to do not exist.

| State | Specified at | In the build |
|---|---|---|
| A plot with no visits yet — first entry after payment | §7.1, §8.2 "never a blank list" | no plot object |
| A visit report in full | §7.5 | no report screen |
| A report with no photographs | §8.2 "Report, being prepared" | — |
| The shared report seen by a guest with no account | §13.3 | no guest route |
| Visit postponed by weather | §8.3(a) `rescheduled` — "The new date must be present" | — |
| Crew could not reach the plot | §8.3(b) `no-access` — the GPS block in full | — |
| Guarantee re-visit requested | §8.3(c) — "We will return within 7 days at no cost." | — |
| Payment by transfer | §8.2 "Bank transfer — `Awaiting payment`" | no payment route at all |
| Payment pending | §8.2 | — |
| Payment declined | §8.2 "The payment did not go through. Your card was not charged." | — |
| Subscription being cancelled, refund arithmetic on screen | §12 | no billing route |
| Invitation as the recipient sees it, before and after accepting | §8.2 "Invitation accept" | no Family Circle |
| Calculator at default, mid-range and both slider ceilings | §11.1–§11.3 | **no calculator exists** |
| The 95,000 first-year line | §11.4, four permitted places | appears nowhere; the number 95,000 does not occur on the site |
| 404 | §8.1 — "plus five real links and a phone number" | a bare panel, HTTP 200, no links |
| 500 | §8.1 — "Something on our side is not working. Your data is safe." | unreachable |

## 6 · Two specified pieces of arithmetic that have nowhere to live

**The refund formula.** FINAL-UX §12.1:

```
refund = amount_actually_paid × (visits_not_performed ÷ visits_total)
         rounded UP to the nearest 100 ֏, in the client's favour
```

with the accompanying rule that "the base is what the client actually paid, never the list price",
and the worked example `95,000 × 3/4 = 71,250 → 71,300 ֏ AMD`. LEAD-REVIEW records that computing
from the list price would return 120,000 against 95,000 actually received. There is no cancellation
screen, so nothing implements it — and nothing implements the wrong version either. This is a gap,
not yet a defect.

**The credit and the first-year line.** FINAL-UX §1 and §11.4: one already-paid one-off is credited
in full within 60 days, producing `160,000 − 65,000 = 95,000 ֏ AMD for the first year, and
160,000 ֏ AMD in each year after that`, shown in exactly four places and nowhere else. None of the
four places exists.

## 7 · Windows the specification names that the build has no equivalent for

Modal (consultation) · share sheet · confirmation dialog · date picker · combobox · plot switcher ·
lightbox · toast · tooltip. The build's only overlay is the mobile menu, plus two Swiper carousels
and a before/after drag handle. Magnific Popup is loaded on every page (`js/popup.js`, 20,216 bytes,
plus `css/popup.css`) and bound to `.igallery`, `.si`, `.popup-modal` and `.popup-youtube` — none of
which matches any element on any of the 48 documents. It is dead weight on every page load.

## 8 · Checks from the brief that could not be run because the subject does not exist

| Check | Status |
|---|---|
| Prices 20,000 · 65,000 · 160,000 · 200,000 and the 95,000 first-year figure | **run — all five absent.** See FINDINGS #3 and #13 |
| The two promises identical everywhere they appear | **run — both absent everywhere.** FINDINGS #13 |
| No QR code and no memorial page, in any tense | **run — passes.** No occurrence of QR, `QR-код`, memorial page or `հիշատակի էջ` in any of the 48 documents |
| No competitor named, no "only ones" claim | **run — passes.** No competitor name occurs |
| Guest report shows no price, plan or upsell; check the network payload | **not run** — no guest route exists |
| Calculator at default, mid-range and both ceilings | **not run** — no calculator exists |
| Legal address and registration number present as visible placeholders | **run — partially fails.** The address and phone are placeholders but are not marked as such; the registration number is absent entirely. FINDINGS #14 |
| Dram sign renders; `AMD` in words where the bank requires it | **run — split.** The sign renders (verified at 4× magnification); the letters `AMD` appear nowhere. FINDINGS #21 |

## 9 · States that exist in the build but were not reached

These are listed in full in `INVENTORY.md` with the command to reach each one. In summary:

- **Form submitted, success and error**, on all four forms — reaching them sends a real enquiry,
  creates a real account, or sends real mail. Not exercised deliberately.
- **Invalid-field state** — cannot be triggered at all: every input is `type="text"` with no
  `required` attribute and there is no client-side validation, so no browser-native invalid state
  exists. That absence is itself FINDINGS #10.
- **500** — not reachable from outside.
- **Mobile menu between the CSS breakpoint and 1300px** — the toggle is hidden while the script
  still treats the layout as mobile. FINDINGS #28.
