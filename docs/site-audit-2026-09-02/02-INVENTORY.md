# 02 — INVENTORY: the coverage matrix

Every cell is **captured** or **skipped with a reason**. Nothing is omitted silently.

`screens/` holds **380** PNGs. Verification numbers for every one are in
`capture-log.json`; the route → file index is `manifest.json`.

Legend: `fold + full` — two distinct files. `fold = full` — the page fits the viewport and
the two files are byte-identical (stated, not hidden). `fold + full*` — the full-page file is
**wider than the viewport**, which is a horizontal-overflow finding, not a capture fault.

## Axis 1 · route × locale × viewport, default state

| Route | Path | Auth | 1920 | 1440 | 1280 | 1024 | 360 |
|---|---|---|---|---|---|---|---|
| `home` | `/am/page/home/` | no | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `home` | `/ru/page/home/` | no | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `home` | `/en/page/home/` | no | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `contact` | `/am/contact/` | no | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `contact` | `/ru/contact/` | no | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `contact` | `/en/contact/` | no | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `login` | `/am/account/login/` | no | fold = full | fold = full | fold + full | fold + full | fold + full\* (361px) |
| `login` | `/ru/account/login/` | no | fold = full | fold = full | fold + full | fold + full | fold + full\* (361px) |
| `login` | `/en/account/login/` | no | fold = full | fold = full | fold + full | fold + full | fold + full\* (361px) |
| `register` | `/am/account/register/` | no | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `register` | `/ru/account/register/` | no | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `register` | `/en/account/register/` | no | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `reset` | `/am/account/reset/` | no | fold = full | fold = full | fold + full | fold + full | fold + full\* (361px) |
| `reset` | `/ru/account/reset/` | no | fold = full | fold = full | fold + full | fold + full | fold + full\* (361px) |
| `reset` | `/en/account/reset/` | no | fold = full | fold = full | fold + full | fold + full | fold + full\* (361px) |
| `notfound-tpl` | `/am/page/history/` | no | fold = full | fold = full | fold + full | fold + full | fold + full |
| `notfound-tpl` | `/ru/page/history/` | no | fold = full | fold = full | fold + full | fold + full | fold + full |
| `notfound-tpl` | `/en/page/history/` | no | fold = full | fold = full | fold + full | fold + full | fold + full |
| `acct-dashboard` | `/am/account/index/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-dashboard` | `/ru/account/index/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-dashboard` | `/en/account/index/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-objects` | `/am/account/objects/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-objects` | `/ru/account/objects/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-objects` | `/en/account/objects/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-packages` | `/am/account/mypackages/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (452px) |
| `acct-packages` | `/ru/account/mypackages/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (452px) |
| `acct-packages` | `/en/account/mypackages/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (452px) |
| `acct-profile` | `/am/account/personal-edit/5/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-profile` | `/ru/account/personal-edit/5/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-profile` | `/en/account/personal-edit/5/` | yes | fold = full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-order-1` | `/am/account/packages/add/1/` | yes | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-order-1` | `/ru/account/packages/add/1/` | yes | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `acct-order-1` | `/en/account/packages/add/1/` | yes | fold + full | fold + full | fold + full | fold + full | fold + full\* (361px) |
| `nav-mission` | `/am/page/mission/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-mission` | `/ru/page/mission/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-mission` | `/en/page/mission/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-values` | `/am/page/values/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-values` | `/ru/page/values/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-values` | `/en/page/values/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-news` | `/am/publications/news/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-news` | `/ru/publications/news/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `nav-news` | `/en/publications/news/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `acct-payments` | `/am/account/payments/` | yes | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `acct-payments` | `/ru/account/payments/` | yes | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `acct-payments` | `/en/account/payments/` | yes | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `acct-order-2` | `/am/account/packages/add/2/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-2` | `/ru/account/packages/add/2/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-2` | `/en/account/packages/add/2/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-3` | `/am/account/packages/add/3/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-3` | `/ru/account/packages/add/3/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-3` | `/en/account/packages/add/3/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-4` | `/am/account/packages/add/4/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-4` | `/ru/account/packages/add/4/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `acct-order-4` | `/en/account/packages/add/4/` | yes | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `root` | `/` | no | **skipped** | fold + full | **skipped** | **skipped** | **skipped** |
| `provoked-404` | `/am/no-such-page/` | no | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |
| `acct-packages-add-broken` | `/am/account/packages-add/` | yes | **skipped** | fold = full | **skipped** | **skipped** | **skipped** |

### Why cells are skipped

- **`nav-mission`, `nav-values`, `nav-news`, `acct-payments`, `acct-order-2/3/4` — captured at
  1440 only.** Each renders a template already captured at every viewport: the first four are
  the same 404 panel as `notfound-tpl`, and the order pages differ from `acct-order-1` only in
  the package name and price. Byte sizes in `mirror-manifest.json` confirm the equivalence.
- **`root`, `provoked-404`, `acct-packages-add-broken` — 1440 only, no locale.** `/` serves the
  Armenian home document without redirecting; the other two are evidence of the soft-404
  behaviour, not designed screens.
- **`/{loc}/account/logout/` — not captured at all.** Requesting it ends the session. It is
  documented from its markup and from the incident on 31.08 when a crawl triggered it.

## Axis 2 · windows that open on top

| Window | Exists | How opened | How closed | Captured |
|---|---|---|---|---|
| Mobile menu | yes | `.menu-toggle`, ≤900px only | `.menu-close`, or an outside click ≤1300px | 31.08 archive, 360 and 768 × 3 locales |
| Nav submenu | yes | hover ≥901px; `.open` class ≤1300px | pointer leaves | 31.08 archive, 1440 × 3 locales |
| Reviews carousel | yes | prev/next arrows | n/a | `carousel-reviews__am__1440__slide-1/2.png` |
| Partners carousel | yes | arrows | n/a | 31.08 archive |
| Before/after slider | yes | drag handle | n/a | 31.08 archive, start position only |
| Modal | **no** | — | — | skipped — none exists |
| Drawer / bottom sheet / share sheet | **no** | — | — | skipped — none exists |
| Lightbox | **no** | Magnific Popup is loaded but bound to selectors that match nothing | — | skipped — unreachable |
| Tooltip / popover | **no** | — | — | skipped — none exists |
| Toast / snackbar | **no** | form replies write into a static `div` | — | skipped — none exists |
| Date picker / combobox | **no** | no such input on any route | — | skipped — none exists |
| Confirmation dialog | **no** | no destructive action exists to confirm | — | skipped — none exists |
| Cookie / consent banner | **no** | — | — | skipped — none exists, and there is no privacy policy |

## Axis 3 · interaction states

| State | Captured | Note |
|---|---|---|
| default | yes, every cell above | |
| hover | yes, nav submenu only | No other element changes measurably on hover. |
| focus-visible (keyboard) | yes, 31.08 archive, first four Tab stops | Reached with Tab, never the mouse. Links show a faint ring; **text inputs show nothing** — the empty and focused captures are byte-identical. |
| active / pressed | **skipped** | No `:active` styling is declared on any control. |
| disabled | **skipped** | No disabled control exists on any route. |
| loading | **skipped** | No loading state exists: pages are server-rendered in one response. The only async work is form submission, which was not performed. |
| error | **partly** | Server error *messages* were obtained at protocol level for login (see 01-FINDINGS). Rendered error states were not captured because rendering them requires submitting a form that creates a record. |
| success | **skipped** | Same reason. |
| empty | yes | `acct-objects` is genuinely empty in this account — captured at every viewport. |
| filled | yes, 31.08 archive | Contact and register forms. |
| overflowing | yes | `acct-packages` at 360 overflows by 92px — captured. |

## Axis 4 · flows

| Flow | Walked | Where it stopped |
|---|---|---|
| Login — wrong password, unknown user, empty submit | yes, at protocol level | Two deliberate failures only, to avoid any lockout risk. Messages quoted in 01-FINDINGS. |
| Language switching from five pages | yes | Targets verified for every page type. |
| Package selection, logged out | yes | Ends at the login form. |
| Package order, logged in | yes | **Stopped at the last screen before payment.** The Pay button was never pressed. |
| Provoked 404s and malformed routes | yes | 12 URL shapes, HTTP status recorded for each. |
| Contact form | **not submitted** | Submitting creates a real enquiry. Empty/focused/filled states captured on 31.08. |
| Password reset | **not submitted** | Sends real mail. |
| Registration | **not submitted** | Creates a real account. |
| Destructive actions | **nothing to walk** | No delete, remove or cancel control exists anywhere. |
| Logout and post-logout session behaviour | **not performed** | See 03-GAPS. |
| Search | **does not exist** | No search on any route. |

## Axis 5 · logged-out vs logged-in

Public routes were captured logged-out on 31.08 and logged-in on 02.09. The documents are
**byte-identical** (`/am/page/home/`: 23,169 bytes in both states, `<header>` markup identical).
The header ships all four account links — Login, Register, Personal account, Log out — in every
response, and JavaScript hides two of them after a session POST resolves. See finding 04.

Authenticated-only routes have no logged-out counterpart: they redirect to the login form.
