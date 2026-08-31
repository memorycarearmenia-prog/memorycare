# Design lead review — verification of the final package

**29.08.2026.** Written after reading the four converged specifications
against each other and against the owner's rulings. This document has the
highest precedence in the package: where it differs from any other file,
this one governs.

Everything below was checked, not assumed.

---

## 1. Contrast — recomputed independently

Every pair the team specified was recalculated from the hex values rather
than taken on trust. The reviewers were right in every case they raised,
including against themselves.

| Pair | Measured | Verdict |
|---|---|---|
| Anthracite `#33373C` on Nude `#EFE5D5` | 9.61 | pass |
| Anthracite on Ivory `#F3F0E9` | 10.53 | pass |
| Nude on Anthracite | 9.61 | pass |
| Deep Olive `#575E3B` on Nude | 5.49 | pass |
| Deep Olive on Ivory | 6.01 | pass |
| Ivory on Deep Olive | 6.01 | pass |
| White on Deep Olive | 6.84 | pass |
| Error `#8C3A2E` on Nude | 6.10 | pass |
| Error on Ivory | 6.69 | pass |
| Ivory on Error | 6.69 | pass |
| Secondary text token on Nude | 4.98 | pass |
| **Anthracite at 70% opacity over Nude** | **4.28** | **fails — removed from the system** |
| **Olive `#7C8654` on Nude** | **3.12** | **fails — Olive never carries text** |
| **Olive on Ivory** | **3.42** | **fails** |
| **Olive on Anthracite** | **3.08** | **fails** |
| **Ivory on Olive** | **3.42** | **fails — no light label on an Olive fill** |
| **Error red on Anthracite** | **1.57** | **invisible — the request form may never sit on a dark band** |
| **Deep Olive on Anthracite** | **1.75** | **never used** |

Two consequences that were not obvious before the numbers existed: the
"Our recommendation" marker cannot be an Olive fill with a dark label,
and the consultation form cannot live inside a dark section. Both are now
structural rules, not preferences.

## 2. Cross-document conflicts found and ruled on

The four specifications were written in parallel, and two values came out
different. Both are now identical everywhere.

### 2.1 Photograph ratio — ruled 4:3 for reports, 3:2 for marketing

The UX and system documents said 3:2; the UI document said 4:3. The
argument offered for 3:2 was that it is "the native ratio of the camera
the crew will hold".

That premise is wrong, and our own pilot checklist says so. The routine
visit report is photographed **by a crew member on a phone** — the
checklist lists a phone with a good camera plus a spare, a tripod, a phone
holder, a power bank, and geotagging switched on. The professional
photographer with drone and camera is booked for the first three or four
visits only, shoots marketing material, and the checklist states
explicitly that the protocol report is still taken by the crew regardless.

A phone's native still ratio is 4:3. So 4:3 is the no-crop ratio for the
device that actually takes these photographs, and the extra vertical
extent suits an upright monument.

**Ruling.** Report photographs 4:3 at 1600×1200. Comparison pairs are two
stacked 4:3 frames. Marketing section images 3:2 at 1800×1200 — that is
what the camera shoots. Crew and equipment portraits 1:1. Video 16:9.
Link previews 1.91:1.

Applied to all four documents.

### 2.2 Corner radius — ruled 0 / 2 / 8 / full

The UI document had 4px for controls; the system document had 2px and no
overlay radius at all.

**Ruling.** `0` for photographs, the report sheet, bands, rules, the
verification rail and tables. `2px` for buttons, inputs, cards, tariff
cards, badges, chips and toasts — 4px begins to read as a mobile app and
fights the hairline, editorial character the rest of the system is built
on. `8px` for overlays only: modals, drawers, bottom sheets, the lightbox
— an overlay is a different plane and may say so. `full` for the slider
thumb, the petal bullet and avatar discs.

Applied to all four documents.

## 3. Checked and found consistent

- Header height 56 / 72 across all three structural documents.
- Verification rail at 14px, not the 11–12px originally proposed.
- Breakpoints 360 / 600 / 900 / 1200 / 1440 everywhere.
- Report block order: confirmation, then GPS as its own block, then
  photographs grouped `On arrival` before `After the work`, chronological,
  crew note after the images. No before/after slider anywhere, and the
  after-image is never the opening image.
- The 95,000 ֏ first-year figure appears in the calculator and on the
  pricing page in all four documents, worded as arithmetic.
- The two service promises — callback within one business day, report
  within 48 hours — are identical in every occurrence.
- Character limits reconcile: H1 capped at 48 and the longest written is
  45; the primary button is capped at 22 and the agreed label
  `Request a consultation` is exactly 22.
- One error colour only. No success or warning sibling exists in the
  token set, and the naming prevents one being added.

## 4. Corrections to my own brief

Two errors of mine caused work to be redone, and both are recorded so the
same mistake is not repeated from the same source.

- I wrote "three annual subscriptions". There are **two**, Optimal and
  Maximum. Special is priced by calculator and is never a card. This one
  sentence produced three incompatible pricing layouts in round one.
- The credit window is **60 days**. The 30-day figure still sitting in the
  older pricing table in the repository is stale and must be corrected at
  source; three separate specialists tripped over it.

## 5. The money defect

Two specialists found the same hole independently, from different
directions, which is why it is stated here rather than buried in a spec.

Because the first-year price with an Express credit is 95,000 ֏ while the
list price is 160,000 ֏, a refund computed from the list price returns
more than the client ever paid. A client who paid 95,000 and had one of
four visits would be refunded 120,000.

The agreed formula:

```
refund = amount_actually_paid × (visits_not_performed ÷ visits_total)
```

rounded up to the nearest 100 ֏, shown as arithmetic in the cancellation
flow before confirmation.

This is not a design matter. It belongs in the contract and in the
platform, and it needs to reach the lawyer.

## 6. Unverified — must be checked before build

This session has no outbound network access, so neither claim could be
confirmed. Both have a fallback that makes the build safe either way.

- **Does Cabin contain ֏ (U+058F)?** Unknown.
- **Gloock does not contain ֏.** Reported independently by two reviewers;
  treat as true until disproved.

The currency symbol is therefore specified as its own element with its own
font stack, so a missing glyph degrades to a substitute face for that one
character instead of breaking the price.

## 7. Decisions I took as design lead

Recorded so they can be reversed by name. Each is listed in the open items
with the reasoning above:

- Photograph ratios, §2.1.
- Radius scale, §2.2.
- Credit attaches to the plot, not the client.
- Optimal is marked "Our recommendation", never "Most chosen" — with zero
  customers the second is a claim we cannot support.
- No auto-charge on renewal; an offer 30 days before the anniversary.
- No third-party analytics at launch, therefore no consent banner over the
  primary call to action.
- Past reports stay readable after cancellation, read-only.
- ~~Product names in English with the Armenian in parentheses on first
  mention.~~ **Reversed by the owner 31.08.2026 — the English version carries
  no Armenian script at all.** See `DECISIONS-2` §5.
- The consent checkbox stays in the request form.

---

## 8. Polish pass on the Figma file, 30.08.2026

A second review of the built file against §4.2 of `FINAL-UI.md` found that the
canvas had been built to values I had normalised by eye rather than to the
scale the specification declares. The file has been corrected; the
specification did not change. Recorded here because the divergence was real
and someone will otherwise wonder why the frames moved.

### What was wrong in the file

| Property | Specification | Was built | Now |
|---|---|---|---|
| Section padding, light band | 72 / 72 · 128 / 128 | 32 / 40 · 80 / 88 | as specified |
| Section padding, Anthracite band | 80 / 80 · 144 / 144 | 44 / 44 · 88 / 88 | as specified |
| Card padding | 20 · 32 | 18 · 32 | as specified |
| Report sheet padding | 20 · 40 | 18 · 28 | as specified |
| Body text, mobile | never below 16 | 15 in cards | 16 |
| Uppercase chips and badges | 14 informational floor | 12 and 13 mixed | 14 everywhere |

Values 44, 36, 28, 22, 18, 15, 10, 9 and 6 were all off the declared
4 · 8 · 12 · 16 · 24 · 32 · 40 · 48 · 64 · 72 · 80 · 96 · 128 · 144 · 160
scale. 126 padding values were snapped. Nothing off-scale remains on any page;
this is now verifiable by script rather than by eye.

### One rule the specification did not state, now fixed

§4.2 gives a section's own padding but does not say what happens where two
light sections meet. Applied literally it produces 144px between every pair on
mobile and 256px on desktop.

**The rule, as built:** a light section that follows another light section
opens at **0** and relies on the bottom padding of the section above. A light
section that is first after the header, or that follows an Anthracite band,
opens at its full **72 / 128**. Anthracite bands always carry their full
**80 / 144** on both edges, because they need to separate from what is around
them on both sides.

### Two structural rules discovered while building, added to the system

**Cards in a row are equal height, always.** Where two or more cards sit side
by side — the annual tariffs, the calculator panels, the three how-it-works
cards — the row is a fixed height equal to its tallest child and every child
fills it. The button in a card is pushed to the foot by a growing spacer, not
by hand-tuned padding, so the alignment survives a text change.

**A card without a badge reserves the badge's height.** The Optimal card
carries the "Our recommendation" badge and Maximum does not. Without a
reserve, the two card titles sit at different heights and the row reads as an
accident. The reserve is the badge height plus the gap that follows it — 46px
as built.

### Also corrected

The validation message on the home page sat under the wrong field: it explains
the phone format and was placed after "Cemetery or city". It now sits directly
under the phone field, and that field carries the error stroke.

Thirteen sections were named "Frame". All layers are now named.
