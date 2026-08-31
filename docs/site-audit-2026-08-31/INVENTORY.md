# INVENTORY — coverage matrix

Every cell is marked **captured** or **skipped with a reason**. Nothing is omitted silently.

Two framings are captured for every cell: `default-fold` (exactly what the viewport shows) and
`default-full` (the whole page). Where a page fits inside the viewport the two files are
byte-identical, and that is stated rather than hidden.

Total files in `screens/`: **242**. Automated verification (byte size > 2,000 and
per-channel standard deviation > 3.0) passed on every one; the per-file numbers are in
`capture-log.json` and `capture-log-states.json`.

## Axis 1 · Route × locale × viewport, default state

| Route | Path | 360 | 768 | 1024 | 1440 | 1920 |
|---|---|---|---|---|---|---|
| `home` | `/am/page/home/` | fold + full | fold + full | fold + full | fold + full | fold + full |
| `home` | `/ru/page/home/` | fold + full | fold + full | fold + full | fold + full | fold + full |
| `home` | `/en/page/home/` | fold + full | fold + full | fold + full | fold + full | fold + full |
| `contact` | `/am/contact/` | fold + full | fold + full | fold + full | fold + full | fold = full |
| `contact` | `/ru/contact/` | fold + full | fold + full | fold + full | fold + full | fold = full |
| `contact` | `/en/contact/` | fold + full | fold + full | fold + full | fold + full | fold = full |
| `login` | `/am/account/login/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `login` | `/ru/account/login/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `login` | `/en/account/login/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `register` | `/am/account/register/` | fold + full | fold + full | fold + full | fold + full | fold = full |
| `register` | `/ru/account/register/` | fold + full | fold + full | fold + full | fold + full | fold = full |
| `register` | `/en/account/register/` | fold + full | fold + full | fold + full | fold + full | fold = full |
| `reset` | `/am/account/reset/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `reset` | `/ru/account/reset/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `reset` | `/en/account/reset/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `history` | `/am/page/history/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `history` | `/ru/page/history/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `history` | `/en/page/history/` | fold + full | fold + full | fold + full | fold = full | fold = full |
| `mission` | `/am/page/mission/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `mission` | `/ru/page/mission/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `mission` | `/en/page/mission/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `values` | `/am/page/values/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `values` | `/ru/page/values/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `values` | `/en/page/values/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `news` | `/am/publications/news/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `news` | `/ru/publications/news/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `news` | `/en/publications/news/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `notfound` | `/am/zzz-not-found/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `notfound` | `/ru/zzz-not-found/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `notfound` | `/en/zzz-not-found/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `packages-add-1` | `/am/account/packages/add/1/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `packages-add-1` | `/ru/account/packages/add/1/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `packages-add-1` | `/en/account/packages/add/1/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `account-index` | `/am/account/index/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `account-index` | `/ru/account/index/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `account-index` | `/en/account/index/` | **skipped** | **skipped** | **skipped** | fold only | **skipped** |
| `root` | `/` | **skipped** | **skipped** | **skipped** | fold + full | **skipped** |

### Reasons for every skipped cell

- **`mission`, widths 360 / 768 / 1024 / 1920** — Byte-identical to the `history` capture at the same locale and width — the same 404 template. Captured at 1440 only; the other four widths would duplicate `history`.
- **`values`, widths 360 / 768 / 1024 / 1920** — As above.
- **`news`, widths 360 / 768 / 1024 / 1920** — As above.
- **`notfound`, widths 360 / 768 / 1024 / 1920** — As above.
- **`packages-add-1`, widths 360 / 768 / 1024 / 1920** — Captured at 1440 only. Reaching it needs an authenticated session; the mirror holds the session that existed at capture time and cannot be re-authenticated per viewport.
- **`account-index`, widths 360 / 768 / 1024 / 1920** — As above.
- **`root`, widths 360 / 768 / 1024 / 1920** — Captured at 1440 only; it serves the same document as /am/page/home/ (23,287 vs 23,300 bytes).

## Axis 2 · Windows that open on top

| Window | Where it exists | Captured | Note |
|---|---|---|---|
| Mobile menu | `.menu-wrapper.active`, home, 360 and 768 | yes, 3 locales × 2 widths | Full-screen white panel. The language switcher is **not** inside it. |
| Mobile submenu | `nav li.has-children.open`, 360 | yes, 3 locales | 'About us' expanded to History / Mission / Values — all three lead to 404 panels. |
| Desktop nav submenu | hover, 1440 | yes, 3 locales | Opens on hover only; no keyboard or click equivalent. |
| Reviews carousel | `.reviews` Swiper, home | yes, slide 1 and after pressing next | The two captures are visually identical — see FINDINGS #12. |
| Partners carousel | `.partners` Swiper, home | yes, 1440 | Four empty placeholder tiles. |
| Before/after slider | `.beer-slider`, home | yes, at its 50% start position | Only one handle position captured; it is a drag control with no discrete states. |
| Lightbox | Magnific Popup, loaded but unbound | **skipped** | No matching element exists on any route — see the unreached list below. |
| Modal / drawer / bottom sheet / share sheet | — | **skipped** | None exist in the build. |
| Toast / tooltip / popover | — | **skipped** | None exist in the build. |
| Date picker / combobox | — | **skipped** | No such input exists on any route. |
| Confirmation dialog | — | **skipped** | None exist; no destructive action is confirmed. |

## Axis 3 · Interaction states

| State | Captured | Note |
|---|---|---|
| Keyboard focus, first four stops | yes — `home__am__1440__focus-visible-tab1..4.png` | Captured by pressing Tab, not by clicking. |
| Mouse focus | **skipped** | Superseded: clicking a link navigates. Compare with the keyboard captures instead. |
| Hover | yes, on the nav submenu | No other element changes measurably on hover. |
| Disabled | **skipped** | No disabled control exists on any route. |
| Selected | **skipped** | No selectable control exists. |
| Form: empty | yes — contact ×3 locales ×2 widths, register ×2 widths | |
| Form: first field focused | yes | At 1440 the focused capture is **byte-identical** to the empty one: focusing a text field produces no visible change. Evidence for FINDINGS #7. |
| Form: all fields valid | yes — `form-filled` | |
| Form: one field invalid | **skipped** | No client-side validation exists to trigger; see below. |
| Form: after sending | **skipped** | Sending creates a real enquiry; see below. |

## States that were not reached, and how to reach them

Every one of these is a finding in its own right, per the brief.

- **`contact` · form-submitted-success** — Submitting the contact form sends a real enquiry to the business. Not exercised. To reach it: `curl -X POST https://mc.makyan.com/am/contact/ -H 'Content-type: application/json' -d '{"lang":"am","namesurname":"AUDIT","phone":"","email":"audit@example.com","message":"AUDIT"}'` and screenshot `#respct` with class `rsuccess`.
- **`contact` · form-submitted-error** — Same reason. The server returns `{status, message}`; the error branch adds class `rerror` to `#respct`. Same command with a deliberately invalid payload.
- **`login` · invalid-credentials** — Not exercised: it posts to the authentication endpoint. To reach it, sign in with a deliberately wrong password and capture the response rendered into the page.
- **`register` · validation-error** — Not exercised: a successful post creates a real account. There is no client-side validation to trigger — every field is `type="text"` with no `required`, so no browser-native invalid state exists to capture.
- **`reset` · email-sent** — Not exercised: it sends mail to a real address.
- **`*` · loading** — No route has a loading state: every page is server-rendered in one response and the only asynchronous work is form submission.
- **`*` · 500** — Not reachable from outside. To reach it: force a server exception on a staging copy, or ask the developer for the 500 template.
- **`home` · language-switcher-open** — There is no such state — `ՀԱՅ РУС ENG` are three plain links, not a disclosure widget.
- **`*` · lightbox-open** — No lightbox is instantiated. Magnific Popup is loaded (`js/popup.js`, 20,216 bytes) and bound to `.igallery`, `.si`, `.popup-modal`, `.popup-youtube` — none of those selectors match any element on any of the 48 documents.
- **`*` · toast** — No toast or snackbar component exists. Form feedback is written into a static `#respct` div.
- **`*` · tooltip** — No tooltip component exists.
- **`*` · date-picker** — No date input or picker exists on any route.
- **`*` · combobox** — No select or combobox exists on any route.
- **`*` · bottom-sheet / drawer / share-sheet** — None exist. The mobile menu is the only overlay.
- **`*` · plot-switcher** — Does not exist — the plot object model is unbuilt (see GAPS.md).
- **`home` · menu-open at 1024/1440/1920** — `.menu-toggle` is not visible at these widths, so the mobile menu has no open state there. Recorded as a finding: `menu.js` gates its outside-click and submenu behaviour on `innerWidth <= 1300` while the CSS hides the toggle earlier, so between those two widths the submenu logic is live with no way to open the menu.

## Checks that were not run

| Check | Why not | Command for whoever runs it |
|---|---|---|
| Lighthouse against the live origin | This session's sandbox is blocked from `mc.makyan.com` by network policy; Lighthouse was run against a byte-exact local mirror instead, so its network timings are optimistic. | `npx lighthouse https://mc.makyan.com/am/page/home/ --form-factor=mobile --throttling-method=devtools` |
| Real-device rendering | Only Chromium 141 was used. | Repeat on Safari/iOS and Firefox; Armenian shaping differs between engines. |
| Server response headers, TLS, caching | Not captured. | `curl -sSI https://mc.makyan.com/am/page/home/` |
| Guest-report network payload | The route does not exist (see GAPS.md), so there was nothing to inspect. | — |
| Screen-reader walkthrough | Not run — no screen reader in this environment. | NVDA or VoiceOver over the header, the package cards and the contact form. |
| Video recordings | Not produced. The only motion is the Vanta cloud background, the two carousels and the before/after drag; none carries information a still does not. | — |
