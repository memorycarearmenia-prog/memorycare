# Owner decisions, round two — binding, 29.08.2026

These are additional to `DECISIONS.md` and override any proposal or memo.

## 1. Pro-rata refund — by visits, on the amount actually paid

```
refund = amount_actually_paid × (visits_not_performed ÷ visits_total)
```
rounded up to the nearest 100 ֏.

- **Base is what the client actually paid, never the list price.** A
  client who paid 95,000 ֏ after an Express credit and has had 1 of 4
  visits receives 95,000 × 3/4 = 71,250 → **71,300 ֏**. Computing from
  160,000 would return 120,000 and we would refund more than we took.
  This is the single most expensive bug the review found; it must reach
  the lawyer and the platform.
- Basis is visits, not days. The client can count visits himself, so the
  number is never disputed. Work already performed is already paid for.
- No cap on the refund. The guarantee only sells if it is unconditional.
- The calculation must be shown in the cancellation flow before
  confirmation, as arithmetic, not as a single figure.

## 2. A subscription year = 12 months from the signing date

- Each client has their own start date; seasons are a promise **inside**
  those twelve months, worded as "one visit in each season".
- The winter visit rule stands: if no suitable weather window occurred,
  the visit is **added** to spring. Four visits are guaranteed regardless.
- Renewal is offered against the client's own anniversary, not a company
  calendar.

## 3. Public service promises — these exact numbers, everywhere

- **Callback: within one business day.** Business hours Yerevan time,
  stated next to the promise so a client in Los Angeles can convert it.
- **Report: within 48 hours of the visit.** Chosen over 24 hours because
  video editing and checking need the margin, and missing this promise on
  the first clients destroys exactly what we are building.
- These two numbers appear identically in all six places they occur.
  Nobody may soften or sharpen them locally.

## 4. The deceased's name in a report — off by default

- A report shows cemetery, sector and plot. The name appears only if the
  client switches it on.
- Reason: the link is forwarded into a family group chat and to people
  without accounts, and part of the audience is in the EU.
- The setting lives on the plot, is worded plainly, and is reversible.
  Turning it off must also remove the name from previously issued links.

## 5. Design-lead rulings on the remaining open items

Taken by the design lead so the work is not blocked. Each is a real
decision the owner may reverse; each is listed in `OPEN-ITEMS.md`.

- **Credit is attached to the plot, not the client.** The object model is
  the plot, Special explicitly allows several family plots, and a credit
  that floats between plots is unarguable to implement and easy to abuse.
- **Optimal is marked "Our recommendation", never "Most chosen".** With
  zero customers, "most chosen" is a claim we cannot support, and it is
  exactly the kind of invented proof we are removing from the old site.
- **No auto-charge on renewal.** A renewal offer goes out 30 days before
  the anniversary; the client acts. Silently charging a card for a
  memorial service a year later is the wrong register for this brand.
- **No third-party analytics at launch**, therefore no cookie consent
  banner over the primary CTA. Server-side request counts only. Revisit
  after the pilot.
- **Past reports stay readable forever, including after cancellation.**
  Access to reports about a family member's grave is not a SaaS feature
  to switch off. Read-only, no new visits, no upsell on those screens.
- **Product names in the English version:** English name first, Armenian
  in parentheses on first mention on the page —
  Inspection (Զննում), Express (Էքսպրես խնամք), Optimal (Օպտիմալ խնամք),
  Maximum (Մաքսիմում խնամք), Special (Հատուկ խնամք). Thereafter English
  only.
- **Consent checkbox stays in the request form.** Part of the audience is
  in the EU and the bank requires a lawful basis. It is one line, not a
  wall of text.

## 6. Corrections to the brief itself

- The brief said "three annual subscriptions". **There are two** —
  Optimal and Maximum. Special is priced by calculator and is never a
  card. This error produced three incompatible pricing layouts in round
  one.
- The credit window is **60 days**. The 30-day figure in the older
  pricing table is stale and must not be used.

## 7. Verified by the design lead — arithmetic the team disputed

Recomputed independently; the reviewer was right in each case:

| Claim | Measured | Verdict |
|---|---|---|
| Anthracite at 70% over Nude | **4.28** | fails 4.5, do not use for text |
| Solid secondary text token on Nude | **4.98** | passes |
| Olive fill with Anthracite label | **3.08** | fails, "Our recommendation" badge must be Deep Olive + Ivory |
| Tagline in Olive on Anthracite | **3.08** | fails, tagline in the dark footer is Nude |
| Error red `#8C3A2E` on Anthracite | **1.57** | invisible — **the request form may never sit on a dark band** |
| Error red on Nude | **6.10** | passes |
| Error red on Ivory | **6.69** | passes |

## 8. Unverified, must be checked before build

This session has no network access. Both items get a safe fallback rule
in the type spec regardless of the answer:

- Does **Cabin** contain ֏ (U+058F)?
- **Gloock does not contain ֏** — two reviewers found this
  independently. Prices set in the display face need a `unicode-range`
  fallback for the currency glyph alone.
