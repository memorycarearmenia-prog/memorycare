# 03 — GAPS: what was not tested, and why

An honest gap is worth more than a confident guess. Everything below is something the brief asked
for that this pass did not deliver, with the reason and, where possible, the command or step that
would close it.

---

## 1. Anything that writes data

§12 forbids creating records; §5 and §6 ask for error and success states that only appear after a
write. Those two pull in opposite directions, and I resolved every conflict in favour of §12.

| Not done | Why | How to close it |
|---|---|---|
| Contact form submitted | Creates a real enquiry to the business | On a staging copy: `POST /am/contact/` with `{"lang":"am","namesurname":"AUDIT","phone":"","email":"audit@example.com","message":"AUDIT"}`, then capture `#respct` with class `rsuccess` and again with `rerror` |
| Registration submitted | Creates a real account | Same, against `/am/account/register/` on staging |
| Password reset submitted | Sends real mail to a real address | Same, against `/am/account/reset/` |
| Package order submitted | Creates a real order and is the last step before money | Staging only — and this is also how to answer Q1 about the client-supplied price |
| Payment | §6.7 says stop before money moves | **Deliberately stopped.** The Pay button on `/{loc}/account/mypackages/` was never pressed. The last read-only screen is captured as `acct-packages__{loc}__{w}__default-fold.png` |
| Password / profile change | Would change the owner's live credentials | Staging only |

**Consequence for the record:** no rendered error state, no rendered success state, and no loading
state appears in `screens/`. The login error *messages* were obtained at protocol level instead
(observation B2), which answers the security question §6.1 actually cared about without touching the
UI. The other three forms have no client-side validation at all, so there is no browser-native
invalid state to capture even in principle — that absence is itself finding A-level material and is
recorded in the 31.08 archive.

## 2. Logout and post-logout session behaviour

§6.9 and §6.10 ask what happens on hard reload, on a deep link in a new tab, after logout, and on
Back after logout — and then to re-verify that authenticated routes redirect.

**Not performed.** Requesting `/am/account/logout/` ends the session, and the account owner had
already been asked to sign in twice during this session. Doing it a third time to satisfy a
checklist item was not a good trade without asking first.

This is a real gap, not a dismissal: a page that renders from cache after logout is exactly the kind
of defect this section exists to catch, and I have not ruled it out.

**How to close it**, in order, taking about two minutes:

1. Signed in, open `/am/account/mypackages/` in a new tab — confirm it renders (deep link works).
2. Hard-reload it (Ctrl+F5) — confirm it still renders.
3. Visit `/am/account/logout/`.
4. Press Back. **If the account page renders from cache, that is the finding.** Check the response
   headers on the authenticated pages for `Cache-Control: no-store`.
5. Request `/am/account/index/`, `/am/account/mypackages/`, `/am/account/personal-edit/5/` — each
   must redirect to the login form, not render.

One thing is already known from 31.08: logout is a plain `GET` link, so a crawler, prefetcher or
link-scanner can end a session by following it. That incident is documented in the previous archive.

## 3. The four-way route enumeration is three-way

§2 asks for `sitemap.xml`, a crawl, the navigation, and a client-side router table.

- **`sitemap.xml` and `robots.txt` do not exist** — both return the HTML 404 panel with status 200
  (finding A11). That source contributed nothing.
- **No client-side router exists.** The site is server-rendered; `js/init.js` contains form handlers
  and a session check, not a route table. There is no framework manifest. §2's fourth source is
  therefore not applicable rather than skipped — but it also means **no route can be discovered from
  code**, so any page not linked from another page is invisible to this audit.
- The reconciliation that remains is crawl × navigation, and the two agree: 61 routes, maximum
  discovery depth 3.

**What this cannot rule out:** an unlinked authenticated route. If the developer has built a screen
that nothing links to yet, nothing here would find it. Ask him for the URL patterns directly.

## 4. Typography in the screenshots is not what a Windows visitor sees

The whole site resolves to `system-ui` (finding A15). `system-ui` is not a font — it is whatever the
operating system provides.

- **Captures were made on Linux/Chromium**, where `system-ui` resolves through fontconfig against the
  299 faces installed in the container (DejaVu Sans and similar).
- **The client's own machine is Windows**, where it resolves to Segoe UI.
- **An Armenian visitor on Android** gets something else again.

Letterforms, metrics and line-breaking in `screens/` are therefore representative of layout, not of
typography. Every measured *size*, *weight*, *colour* and *contrast* number in this archive is
unaffected, because those are computed values. Anything about how the letters *look* — including
correction C3 about the dram sign — needs re-checking on the target platform.

## 5. Lighthouse ran against a local mirror, not the origin

This session's sandbox cannot reach `mc.makyan.com`; the site was mirrored through the browser and
served locally. Byte weights, request counts, asset dimensions and unused-code figures are real —
they come from the same files. **Timings and scores are not**, because `server-response-time` reads
0 ms against a local static server.

To get real numbers, from a machine that can reach the origin:

```
npx lighthouse https://mc.makyan.com/am/page/home/ --preset=desktop \
  --throttling-method=devtools --output=html --output-path=./lh-home-am.html
```

Two further mirror artefacts, identified and excluded from the findings rather than reported as
defects:

- **`Error fetching session: SyntaxError: Unexpected token '<'`** on all 36 pages. The static mirror
  answers the session POST with 501 and an HTML body. **Checked against the live origin:** it returns
  `200` with `content-type: application/json` and a valid body. Not a production defect.
- **`ERR_TUNNEL_CONNECTION_FAILED`** for `fonts.googleapis.com` on all 36 pages, and the Google Maps
  iframe on the contact page. The container's egress is blocked. The webfont's absence changes
  nothing visually, because it is applied to no element (A15) — but the request itself is real, and
  is what exposed the duplicate `@import`.

## 6. Not attempted at all

| Item | Reason |
|---|---|
| Screen-reader walkthrough | No screen reader in this environment. The structural failures (no `h1`, no `main`, missing labels, wrong `lang`) are what one would hit; the experience itself was not heard. |
| Browsers other than Chromium 141 | Not available. Armenian shaping differs between engines. |
| Real devices | Emulated viewports only; no touch, no real DPR variation. |
| `/admin/` authentication | Deliberately not attempted (observation B5). |
| IDOR on `/account/personal-edit/{id}/` | Would expose a third party's personal data to me. Question Q2 gives the owner the exact check. |
| CSRF behaviour of the session endpoint | Needs response headers I did not capture. Question Q3 gives the command. |
| Response headers per route | Captured for the session endpoint only. `curl -sSI` per route would complete it. |
| Video / motion capture | The only motion is the Vanta sky, two carousels and a drag handle. The carousel is documented with two stills (correction C1); the rest carries no information a still lacks. |
| Field performance data | The site has no analytics and no real users. |

## 7. Where the previous archive is still the better source

This pass concentrated on what was new: the authenticated area, the 1280 column, the 1024–1300
navigation band, and re-testing §9. For the logged-out marketing site — the mobile menu open state,
submenu states, keyboard focus captures, filled-form states, and the full string inventory per route
and locale — the 31.08 archive remains the more complete record, and its four incorrect claims are
corrected in `01-FINDINGS.md` section D.
