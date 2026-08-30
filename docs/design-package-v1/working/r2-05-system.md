# r2-05 — Design System & Handoff: convergence memo

**Author:** Design System and Handoff Engineer
**Round:** 2 — cross-review of `01-ux-architect.md`, `02-visual-lead.md`,
`03-content.md`, `04-conversion.md` against `DECISIONS.md`, `BRIEF.md` and my own
`05-design-system.md`.
**Date:** 30.08.2026 · Language: English
**Standing:** where I judge against myself I say so explicitly. I concede four of
my own calls below (button radius, the display-face split, shadows, photo ratio)
and I hold three.

Reading convention: **[OWNER]** = a decision only Hayk/Davit can make;
**[DESIGNER]** = the brandbook author; everything else converges in this round.

---

# 1. Conflicts

Fifteen real conflicts. Each: what is disputed, who holds what, what breaks
either way, my resolution and why.

---

## C1 — Functional colour: does red exist?

**Positions.**
- `DECISIONS.md` §2: exactly one muted red, `#8C3A2E`, errors only, no success
  or warning sibling.
- **01** §A8: *"No red. We have no red in the palette and we are not adding one.
  Errors use Deep Olive plus an icon plus explicit text."*
- **02** §B.8: asks the owner for **two** functional colours, recommends the
  former over an all-typographic language.
- **03** §C.9: *"Errors sit on Nude with Anthracite text. Never red."*
- **05** (me): `mc.color.danger.600/100`, `text.danger`, `border.danger`,
  `surface.danger-subtle`, a `button--danger` variant, `Badge--warning`,
  `Toast--success / --warning / --error`.

**What breaks.** With no error colour, a failed payment on a phone at 1 a.m.
is indistinguishable from body text — that is the owner's stated reason and it
is correct: a missed error here is an unfinished payment. With my naming, the
`danger` / `warning` / `success` family invites a seventh colour within a month;
the owner explicitly forbade the family, not just the hues.

**Resolution.** The owner has ruled; 01, 02, 03 and my token names are all
superseded. Canonical:

```css
--mc-color-feedback-error:        #8C3A2E;  /* the sixth colour. The last one. */
--mc-color-feedback-error-subtle: #F6E4E0;  /* 10% of the above over Ivory — a tint, not a hue */
```

Semantic layer: `--mc-text-feedback-error`, `--mc-border-feedback-error`,
`--mc-surface-feedback-error-subtle`. **No token in this system may end in
`-success` or `-warning`** — enforced by a name rule in `lint:tokens` that
rejects those two suffixes outright, so the restriction is visible in the
grammar and not only in a document.

Consequences the four of us must absorb:
- 02's error input (2px Anthracite border + 4px Anthracite bar + Anthracite dot)
  keeps its **form**; the bar, the border and the dot take the error colour.
- 03's rule "never red next to a photograph of a grave" survives as a scope rule:
  the error colour exists **only** in form validation and payment failure. It is
  forbidden on report screens, guest views, bad-news screens and every marketing
  surface. That is the honest reconciliation of 03's instinct with the ruling.
- Success and warning are typographic, exactly as the owner said: a word, a glyph
  and a rule weight. "Moved", "Completed", "Could not access" are words with
  glyphs, never colours.
- My `button--danger` variant is **deleted**. Cancellation is not an error; 01
  §A4.8 is right that it is a calm Deep Olive text link. The error colour never
  fills a button.
- My `Toast` variants collapse to `neutral | error`. Toast on the dark band is
  currently undefined — see §4.

Measured: `#8C3A2E` on Nude = **6.10**, on Ivory = 6.7, on the error tint ≈ 5.6.
White on `#8C3A2E` = 6.84. All pass; error text may sit on page, on card, or in
its own tint panel.

---

## C2 — Button radius: 10px (mine) or 2px (visual lead)

**Positions.** Me: `radius-md` 10px for buttons, 14 for cards, 20 for modals,
"editorial-minimal, not consumer-app". **02** §A.3: `0` for bands, photographs,
the report sheet, dividers; **`2px` for buttons, inputs, cards, badges, modals**;
`999px` only for the slider thumb and the petal bullet; and explicitly *"No
8px/12px/16px 'friendly' radii — they are the wellness-template tell."*

**What breaks.** At 10px the page acquires the exact SaaS-card texture 02's whole
"paper laid on stone" concept is built to avoid, and it fights the 0-radius
report sheet sitting next to it — a 10px card containing a 0px photograph reads
as a mistake. At 2px, nothing breaks: the 48px hit target, the focus ring and
the inner-Ivory ring all work identically.

**Resolution — I concede.** The visual lead owns visual language, their reason is
specific and mine was taste. Canonical radius scale, and the unused steps are
**deleted** rather than left in the file (an unused token gets used):

| Token | Value | Applies to |
|---|---|---|
| `--mc-radius-0` | `0` | bands, photographs, the report sheet, dividers, the plot diagram, the verification rail |
| `--mc-radius-sm` | `2px` | buttons, inputs, cards, tariff cards, badges, modals, sheets, toasts, menus |
| `--mc-radius-full` | `9999px` | slider thumb, petal bullet, avatar circle |

`xs / md / lg / xl / 2xl` are removed from `tokens.json`. One consequence I owe:
the mobile bottom sheet's block-start corners were `xl`; at 2px a sheet no longer
reads as a sheet, so it keeps the 36×4 drag handle and gains a 1px
`border-default` top rule — **[DESIGNER]** may raise the sheet corners to 8px as
a single documented exception; my default is 2.

---

## C3 — Splitting the display face by script

**Positions.** Me §A3.4: `en` Gloock, `hy` Noto Serif Armenian, `ru` **Playfair
Display**, wired per-glyph with `unicode-range`. **02** §A.1: the display face is
*one swappable token*; *"Localisation must not begin until a display face with
Armenian coverage is confirmed. Flagged as blocking."*

**What breaks.** My version ships three different serifs under one brand.
Playfair is a Didone-adjacent transitional with vertical stress; Gloock is a
high-contrast display with a very different rhythm — the Russian site would not
look like the same company as the English one, and a mixed-script line ("Siranush
Hakobyan" inside an English sentence, which happens constantly here) would render
two competing serifs on one line. That is worse than an honest fallback. 02's
version, taken literally, blocks the Armenian site indefinitely on an asset
nobody has committed to buy or draw.

**Resolution — I concede the decision, and keep the mechanism.**
1. The target is **one display face covering Latin + Cyrillic + Armenian**.
   Choosing it is **[DESIGNER] + [OWNER]**, not mine. It is `OPEN-ITEMS` #6 and
   it does not block the English build.
2. Until it exists, `hy` and `ru` headings fall to the **text face at 600**, not
   to a second serif. A heading in the text face reads as a deliberate system;
   a heading in a different serif reads as a broken font.
3. The `unicode-range` machinery stays, as a **safety net, not a design**: every
   declared face carries an explicit range so a missing glyph falls to the next
   family and never to tofu. See §7.
4. If a single covering face proves not to exist for free, the maximum permitted
   split is **two** faces — Gloock for Latin (+ Cyrillic if it has it, unverified,
   §7) and one Armenian companion chosen for a matching axis. Three is refused.

---

## C4 — Shadows: mine (four elevation steps) or none (02)

**Positions.** Me: `elevation-1…4`, card shadow at rest, `elevation-2` on hover
with `translateY(-2px)`, `elevation-4` on modals. **02** §A.3: *"Shadows — none.
There is not one shadow in the system"*; elevation is a ground change plus a
hairline; overlays separate with an Anthracite 60% scrim.

**What breaks.** Shadows on a Nude ground at 4–8% opacity are nearly invisible
anyway and cost a real texture decision; 02 is right that the ground change does
the work, and 01 §D2 independently reached the same conclusion ("shadows read as
SaaS; a 1.1-ratio tonal step reads as paper"). Two of three reviewers agree
against me. But removing shadow leaves three floating layers undefined — see §4
item 6.

**Resolution — I concede.** `elevation-1…4` are deleted. What survives:
`--mc-elevation-0: none` and `--mc-surface-scrim: rgba(51,55,60,0.60)` (02's 60%,
not my 72% — one value, theirs). Every raised object is defined by
**ground change + 1px hairline**. Floating layers get the rules in §4.6.

---

## C5 — Photograph aspect ratio: 3:2 (mine) or 4:3 (01 + 02)

Me: 3:2 for plot photography, "1:1 never". **02** §A.5: report photo **4:3**
(1600×1200), comparison pair 4:5, section image 3:2, crew portrait **1:1**, hero
16:9, OG 1.91:1. **01** §A4.4: report photos 4:3.

**Resolution — I concede, and I correct a self-contradiction.** 02's ratio table
is canonical. My own package shipped `portrait-1x1-team.svg` while my Gallery
spec said "1:1 never" — that rule is withdrawn (1:1 is correct for a crew
portrait, wrong for a plot). Placeholder files rename:
`photo-4x3-plot-arrival.svg`, `photo-4x3-plot-after.svg`, `photo-4x5-compare.svg`,
`photo-3x2-section.svg`, `portrait-1x1-crew.svg`, `video-16x9-report.svg`.

---

## C6 — The pricing row: which products sit together

**Positions.**
- Me §A4.7 and **01** §A3.2 and **02** §A.4: a row of **three** — Express,
  Optimal, Maximum — with Inspection set apart above, Special as a band/footer
  card.
- **03** §C.3: **two bands** — one-off (Inspection + Express), annual (Optimal,
  Maximum, Special).
- **04** §A6: a **fork** at the top ("Do you already know what your plot
  needs?"), then a one-off band (Inspection + Express) and a subscriptions band
  (Optimal + Maximum only); **Special is not a card at all** — one line under
  the calculator.
- **02** §B.3 flags exactly this and asks strategy to rule.

**What breaks.** Putting Express in the annual row states, visually, that a
one-off is a subscription — which contradicts the brief's own reason for setting
Inspection apart and 03's rule 8. Making Special a card adds a fifth thing to
compare, with no price, to serve a minority — 04's argument, and it is right:
the target is a decision in under 60 seconds on a 375px screen.

**Resolution — 04 + 03 win, and my `TariffCard--standalone` is deleted.**

```
Pricing page
  honest-price sentence
  Band 1 · One-off services        Inspection 20,000 | Express 65,000   (2 cards)
  credit rule, four bullets, under the band, always visible (03 §C.4)
  Band 2 · Annual subscriptions    Optimal (marked) | Maximum           (2 cards)
  calculator
  Special — one line beneath the calculator, routed through Inspection
  Guarantees → payment reality → closing CTA → footer
```

Component consequence: `TariffCard` takes `variant: "one-off" | "annual"` and
`emphasis: "leading" | null`. Layout is 1-up below 600, **2-up from 600** — the
3-up grid disappears, which also retires my `--mc-tariff-min-height: 480px` (see
§4.11). 04's fork is a new component I owe (§3).

---

## C7 — How Optimal is marked as the leading choice

**Positions.** Me: 2px Deep Olive border + a Deep Olive badge with an Ivory
label. **02**: no badge at all — the card **inverts to Anthracite**, label "MOST
CHOSEN" in Nude, 24px taller. **03** §C.3: *"a small Olive-filled label with
Anthracite text"*. **04** §B4: *"an Olive top band with Anthracite text carrying
'Most chosen'"*.

**What breaks.** 03's and 04's proposals are **not buildable**: Anthracite on
Olive is 3.08, Ivory on Olive is 3.42, and the brief's own contrast table forbids
both. Two independent reviewers reached for the same forbidden combination, which
tells me the palette's single most likely production mistake is exactly this one
— it must be blocked in code, not in prose.

**Resolution.** **02's inversion is canonical** (Nude on Anthracite = 9.61,
passes, and it needs no badge chip at all). Where a light card is required
instead, the only permitted mark is `Badge--accent`: Deep Olive fill, Ivory
label, 6.01. **An Olive fill with any label is forbidden system-wide**, enforced
by `stylelint-mc-contrast` — this is the rule that pays for the whole linter.

**[OWNER] — a claim, not a design question.** We have **zero paying customers**.
"Most chosen" is a statistic about client behaviour that has not happened, and it
sits in the same class as "trusted by N families", which every one of us has
banned. The brief permits it, so I am not overruling it, but it should be a
conscious owner decision. Safe alternatives that carry the same weight without a
false claim: **"Our recommendation"**, or Armenian **"Առաջատար"** used as the
source and translated as "The leading choice".

---

## C8 — Breakpoints: three incompatible sets

Me: 360 · 480 · 768 · 1024 · 1280 · 1440. **01** §B1: 375 · 600 · 1024 · 1440.
**02** §A.3: 375 · 600 · 900 · 1200 · 1440. **03** §A.1.1: nav collapses **below
900px**.

**What breaks.** Three sets means three grids, three Figma layout modes and three
sets of media queries; every component spec then measures against a width that
does not exist in the other two documents. It is the single cheapest thing to fix
now and the most expensive to fix in October.

**Resolution — one set, 02's, with my QA floor:**

| Name | Min | Columns | Gutter | Margin | Notes |
|---|---|---|---|---|---|
| `base` | **360** | 4 | 16 | 20 | **QA floor** — older diaspora Android. Design frames stay at 375. |
| `sm` | 600 | 8 | 24 | 40 | 2-up tariff cards |
| `md` | 900 | 8 | 24 | 40 | nav expands here (03's rule) |
| `lg` | 1200 | 12 | 24 | auto, max 1200 | verification rail appears |
| `xl` | 1440 | 12 | 32 | auto | more air, no new layout |

360 is a QA gate, not a second design width — that reconciles my objection with
their frames at zero cost. Figma `4 Layout` collection modes become **360 / 900
/ 1440**. Media queries stay min-width only.

---

## C9 — Type: three scales and three different minimum sizes

**Positions.** Me: body 16, "nothing below 13px exists". **01** §B4: body 17/18,
*"nothing below 14px anywhere in the product"*. **02**: body 17 desktop / 16
mobile, `caption` 13, **`eyebrow` 12 (11 on mobile)**, **`rail` 12 (11 on
mobile)**, `legal` 14, body floor 15.

**What breaks.** 02's `rail` at 11px uppercase with +0.08em tracking is the type
that carries the **actual proof** — date, cemetery, plot, crew, coordinates — for
an audience of 40–60 reading on a phone at night. That is the least legible text
in the system carrying the most important content in the product. It also has no
Armenian form: my own rule bans uppercase in Armenian (Armenian caps read as
shouting), and 02's rail is uppercase by definition.

**Resolution.**
- **Informational text floor: 14px** (01's, on merit — the audience decides it).
  13px survives only for genuinely decorative eyebrows.
- `--mc-type-rail`: **14px**, tracking reduced to `0.06em`, tabular, uppercase
  labels in Latin/Cyrillic, **sentence case in Armenian** (`:lang(hy)` branch,
  same mechanism as `overline`). Values are never uppercase in any script.
- `--mc-type-body`: `clamp(1rem, …, 1.0625rem)` — 16 mobile → 17 desktop, which
  satisfies 02, 01 and the iOS-no-zoom rule at once.
- **My `heading-2` was unbuildable**: its `clamp()` minimum is 22px in the display
  face, and 02's optical floor is *Gloock is never set below 24px, ever*. That
  floor is correct — Gloock's hairlines break up. `heading-2` minimum is raised
  to 24px; below `sm`, `heading-3` is the text face at 600, as 02 specified.

---

## C10 — The header logo: four proposals

Me §E4: constructed horizontal lock-up SVG at 36/32px; below 480 the mark plus
live `<span>` in Gloock at **20px**. **01** §B6: constructed lock-up, mono-dark
on light, overriding "Memory in Ivory". **02** §A.6: two tightly-bounded exports,
mark 32/28, and **"the wordmark survives, not the mark"** when space runs out.
**03** §C.1 and **04** §B8: **the mark alone below 900px**, mark + live "MemoryCare"
in Gloock above it.

**What breaks.** 03/04's mark-alone mobile header removes the company name from
the primary channel — for a visitor who arrived from an English search that
returns dementia care, that is the one thing that must never be dropped. 02's
principle ("the name is what survives") is right and directly contradicts them.
My own 20px Gloock breaks 02's 24px optical floor.

**Resolution — the drawn wordmark is not used in the header at all.**

| Element | Rule |
|---|---|
| Composition | mark + **live text** `MemoryCare`, at every width |
| Mark | `mark-mono.svg`, `currentColor`, 32px ≥900 / 28px below |
| Word | display face, **24px minimum** (02's floor), never wraps, never `MC`, never `MEMORYCARE` |
| Two-colour | `Memory` = `--mc-text-primary`, `Care` = `--mc-text-accent` (**Deep Olive**). Not Olive — 3.42 at 24px is unreadable. On the Anthracite footer both halves are Nude. |
| Degradation | below 360 the **mark** drops, the word stays |
| Tagline | never in the header (all four of us agree) |
| Ground | header is Ivory (see C11) |

Live text is selectable, translatable, sharp at any DPR and needs no new asset.
The constructed horizontal lock-up SVGs stay in the package for the footer, OG
images, print and the invoice, where they run at or above their minimum widths.

---

## C11 — Header ground: Ivory or Nude

**02**: Ivory bar. **01** §A3.0: Nude ground, 1px **Olive divider at 20%**.
Me: `surface-page` at 92% + `backdrop-filter: blur(12px)`.

**Resolution.** **Ivory** (02) — it is a sheet, which is exactly what 02's own
Nude/Ivory rule says an object on the ground must be, and both 01 and 02 also
require an Ivory object on Nude to carry a hairline. So: Ivory fill, **permanent**
1px `--mc-border-default` (Anthracite 12%) bottom rule at all widths — not
appearing on scroll, because the 1.1 tonal step without a rule reads as a
printing error, which is 02's own stated failure mode.

Two deletions: **no `backdrop-filter`** (three scripts, old Android, and it buys
nothing over a solid Ivory bar — this also retires my
`prefers-reduced-transparency` rule), and **no Olive at 20% opacity** — 02's rule
is that structural Olive rules are 1px at 100%, and object edges are Anthracite
12%. `alpha.olive.20` is not created.

---

## C12 — The primary CTA string

**04** §A3: *"Request a free consultation"*, one wording only, everywhere.
**05** (me): same. **03** §A.1.3: button `Request a consultation`, heading
`Request a free consultation`. **01** §C1: "Request a free consultation" = 29
chars, *too long* — use "Free consultation". **02** §C: primary label hard max
**24** chars; sticky bar max 16.

**What breaks.** 27–29 characters does not fit any budget any of us wrote, before
Armenian adds 25%. 04 is right that one wording must win; 03/01/02 are right that
it cannot be that one.

**Resolution.** One button label site-wide: **`Request a consultation`** (22).
`Request a free consultation` is the **form heading only**. The sticky mobile bar
uses **`Free consultation`** (17) — a bar, not a sentence. "Free" is carried by
the permanent support line under every instance: *"No payment now. No account
needed."* (04's line, 03's register.)

And a hard requirement that follows: **buttons must survive two lines** with the
label centred (03 §C.2) — at hy +25% a 22-char label is 27–28 characters. My
Button spec has no wrap rule; that is a defect, fixed in §4.

---

## C13 — The consultation form: 4 fields, 7 fields, or 5

**04** §A4: four fields, two required; **explicitly rejects** preferred contact
time, and any consent checkbox beyond a single-line privacy statement.
**03** §A.1.4: name, contact, cemetery, optional note, **consent checkbox**.
**01** §A6.1: the above **plus** a conditional "family member in Yerevan"
disclosure (name + phone), **plus** preferred-contact-time chips.

**Resolution, field by field, with reasons:**

| Field | Verdict | Why |
|---|---|---|
| Name | required | all agree |
| Phone **or** email, one field | required | all agree; international formats, country selector, dial code as text, never a flag alone |
| Cemetery or city, combobox with free entry | required | 04's argument (it changes the quality of the callback) beats the volume cost |
| Optional note, collapsed | optional | 04 and 03 agree |
| Preferred contact time | **cut** | 04 wins: guessed wrong more often than right, and the callback window is stated instead |
| Yerevan family member | **cut from the form**, captured on the onboarding call | 01's own §A2.3 step 2 already captures it there. The split-payer case is a **data-model** requirement (three contact records per plot), not a form requirement. |
| Consent checkbox | **kept** | 04 loses this one. A meaningful share of the audience is resident in France and the rest of the EU; the privacy policy, the bank package and the Armenian data question all need a demonstrable lawful basis. The conversion cost of one checkbox is smaller than one complaint from a French resident. **[OWNER]** may overrule with counsel's sign-off. |

---

## C14 — Error language, icons and illustrations

**03** §C.9: the error component has three slots (what happened / whose fault /
what to do), **must not accept an icon slot**, and the illustration slot "must not
exist". **Me** §A4.2: field errors carry a 16px alert icon.

**What breaks.** Removing the icon from a **field** error leaves colour plus text
as the only signal; WCAG 1.4.1 and my own "colour is never the only carrier" rule
both require a second non-colour signal, and roughly 8% of a male 40–60 audience
is colour-deficient (01 §A6.1 makes the same point).

**Resolution — both, scoped.** Field-level errors keep the 16px glyph (it is a
signal, not decoration). **Page- and screen-level error panels** take 03's shape
exactly: heading, body, action, optional phone line, **no icon, no illustration,
no emoji, no "Oops"** — and that constraint is enforced in code by the component
having no `icon` or `illustration` prop at all, so it cannot be reached for under
deadline.

---

## C15 — Number motion in the calculator

Me: 220ms count-up on the total, snapping under reduced motion. **01** §A7: the
number animates only on `pointerup` — a number counting during a drag is
unreadable. **02** §A.4: *"Numbers change instantly. No count-up animation. A
price that rolls like a slot machine is exactly the wrong register."*

**Resolution — 02, and I concede.** No count-up anywhere. The total updates
instantly; the track fill updates during the drag; tabular figures prevent
jitter, which is what the count-up was compensating for. This also removes a
reduced-motion branch, so the reduced-motion and default paths are identical —
always the better outcome.

---

# 2. Contradictions with the owner decisions

Including mine. `DECISIONS.md` overrides all five proposals.

| # | Ruling | Who contradicts it | Correction |
|---|---|---|---|
| 1 | §1 `MemoryCare LLC`, one word | Nobody in this round. **03** §D.6 asks which spelling is registered — **that question is now answered**; use `MemoryCare LLC` in the footer, offer, invoices, legal pages, bank package and meta. The repo's `CLAUDE.md` ("Memory Care LLC") is stale. | 03 closes its open item 6. My denylist already fails the build on the spaced form and on `MEMORYCARE`. |
| 2 | §2 one functional colour, errors only, no `-success`/`-warning` sibling | **01** ("no red, errors in Deep Olive"), **02** (asks for two), **03** ("never red"), **05** (`danger` + `warning` + `success` families, `button--danger`) | C1. All four texts are superseded. My token family is renamed to `--mc-color-feedback-error` with a lint rule banning the two sibling suffixes; `Toast` collapses to `neutral | error`; `Badge--warning` becomes `Badge--neutral` with a word; `button--danger` is deleted. |
| 3 | §3 show 160,000 − 65,000 = **95,000 ֏** for the first year, in the calculator **and on the pricing page**; never as a discount; not in the hero; not as the Express headline price | **01** §A7 renders it in the calculator ✅ but calls it "a 40% first-year discount" in its own §D5 — internal language that must not reach copy. **03** explains the credit mechanic but **never prints the arithmetic** on the pricing page. **04** likewise. **05** has no string slot and no component for it. | New copy slot `pricing.credit.firstYear` and a calculator result row, both printing the arithmetic as a mechanic. New lint rule: the words `save`, `discount`, `offer`, `%`, `was` and any `text-decoration: line-through` on a price are build failures. Express card headline price stays `65,000 ֏ AMD`. |
| 4 | §4 credit window **60 days** | Nobody. 01 §D4 flags the repo's stale 30-day figure — resolved. | `products.json` carries 60 and is the only source. |
| 5 | §4 scope = site **and** portal | Nobody. | — |
| 6 | §4 Cabin, labelled everywhere as a substitute for Gill Sans | **03** and **04** never label it (not their remit, but the label must appear on their mocks and in exported PDFs too). | `FONTS.md` owns the sentence; it is repeated in `tokens.json` `$description`, in a comment in the built CSS, on Figma page `01 · Foundations`, and in the footer of every exported spec PDF. |
| 7 | §4 neutral branded placeholders labelled with the replacing shot, exact ratio and crop | Nobody contradicts; **02** §A.5 is the fullest version and is canonical. My ratios were wrong — C5. | Placeholder files renamed and re-cut to 02's ratio table; each names ratio, pixel size, subject and source, or it is not shippable. |
| 8 | §4 legal address = visible placeholder + open item | All four comply. | — |
| 9 | §5 verify ֏ (U+058F) in Cabin; if absent, a fallback for the currency glyph only, stated in the type spec | **03** §C.11 raises it and cannot answer it. **05** asserted stacks without a verification path. Nobody can check — no network. | §7: the currency glyph gets its own font binding and a build-time glyph test. |

---

# 3. Components the others need that my spec does not contain

My `components/` shipped 18 specs. The four proposals require **34 more**. Listed
by claimant, with the specification each needs. Anything marked **new** does not
exist in any document as a component contract.

### From 01 (screens and behaviour)

| # | Canonical component | Spec required |
|---|---|---|
| 1 | `VerificationRail` | 02's signature device; see the 02 block below — 01 also depends on it for every visit and report screen. |
| 2 | `GpsVerification` | 1:1 frame, 120px ≥900 / 96px below, radius 0, 1px Olive, Nude fill, bearing rose (3 concentric Olive rules at 20%), cross-hair, solid Olive petal glyph 14px at the true offset; coordinates in `type.rail` below; caption line; `Badge--accent-soft` "GPS confirmed"; `[Show on map]` opens the device map app by `geo:`/Apple Maps URL — **no map tile** (see §4.9). States: `recorded` · `pending` ("Coordinates pending upload", never an empty cell) · `not-recorded`. |
| 3 | `ProgressRail` **new** | 4 dots, horizontal, labelled; states `done · in-progress (ring) · pending`; used on the portal first-entry screen; `aria-current="step"`; label max 20 chars, wraps to two lines at 360. |
| 4 | `PlotCard` **new** | Dashboard row: identity, cemetery, next visit, last-report thumbnail (neutral crop, 4:3), plan name; whole card is one stretched link; min-height 88. |
| 5 | `VisitListRow` + `VisitListGroup` **new** | Scheduled group (dashed Olive inline-start rule) above completed group (solid Deep Olive rule); row 72 min, entire row the target; chevron; status chip. Replaces "the table becomes a stack of report cards" hand-wave in my §B3. |
| 6 | `ShareSheet` **new** | Read-only link field + Copy, WhatsApp, Viber, Email, divider, **"Link is active · Revoke"** with the creation date and a confirm. The revoke affordance must live in the sheet that creates the link. |
| 7 | `RoleSelector` **new** | Three radio-cards with one-line descriptions (never a dropdown — a dropdown hides the consequence), plus plot-scope checkboxes when >1 plot. |
| 8 | `PermissionMatrix` **new** | The one permitted horizontally scrolling table: capability column frozen, scroll-fade affordance, and a screen-reader-equivalent definition list. Amends my §B3 "tables do not exist below `sm`". |
| 9 | `Stepper` (flow) **new** | "Step n of 4", back/next, escape at equal weight; used by cancellation. |
| 10 | `RefundTable` **new** | annual price · visits completed · value consumed · refund · method · timing; tabular figures; a single arithmetic source shared with the calculator. |
| 11 | `SegmentedControl` **new** | tier selector (Optimal/Maximum), calculator mode toggle, language switcher; `aria-pressed`; 44×36 minimum with a 44×44 hit area. |
| 12 | `NumberField` / `Input--numeric` **new** | Paired with every slider. 48 tall, 96 wide, stepper buttons at 44×44, tabular. 01 and 02 both call sliders alone unusable; my calculator mentions it but there is no input variant contract. |
| 13 | `CountrySelect` **new** | Dial code + ISO as text (`+374 AM`), never a flag alone; searchable in three scripts; default by IP, always visibly overridable, never re-guessed. |
| 14 | `Combobox` **new** | Cemetery/city: free text with suggestions, free entry always accepted. My `Select` is a closed listbox and cannot express it. |
| 15 | `Accordion` **new** | Home FAQ (first open), pricing FAQ, legal ToC, "what each role can do". Missing entirely from my package though three documents use it. |
| 16 | `StepStrip` **new** | Numbered 3–4 step strip (home "what a visit is", how-it-works timeline with the Olive rail). |
| 17 | `PortalTabBar` + `PortalSidebar` **new** | 4 tabs, 56 + `env(safe-area-inset-bottom)` below 900; 240px sidebar above. My `Navigation` spec is marketing-header only. |
| 18 | `PlotSwitcher` **new** | Portal header, only when >1 plot. |
| 19 | `ReportShareBar` **new** | The report screen's own sticky bar, 48 tall, **Share only**. Distinct from `StickyCtaBar`, which 02 §B.7 removes entirely on report and guest views. |
| 20 | `GuestReportLayout` **new** | The route, not just the bundle rule: masthead, body, one-line foot, one non-commercial action. |
| 21 | `GuestFeedbackForm` **new** | Three fields (name, phone, message), no consent theatre, no account; the **only** interactive element on `/r/`. |
| 22 | `ErrorPage` (404 / 500) **new** | Calm heading, five real links, phone. No joke, no illustration. |
| 23 | `BankTransferPanel` + invoice template **new** | The path the first paying clients actually use; currently undesigned in every document (04 §D.2 flags it). Wire instructions on screen and as PDF. |
| 24 | `AuthScreens` **new** | Sign in, magic-link interstitial, activation from token, password reset — with 03's lock-out, session-expired and server-error strings. |
| 25 | `NotificationMatrix` **new** | Per-plot event × recipient toggles, plus the local-contact block with the third-party consent checkbox. |
| 26 | `FileUpload` **new** | Guarantee re-visit: up to 3 photos, 10 MB, **HEIC accepted**; states idle/uploading/complete/too-large/wrong-type. |
| 27 | `EmptyState` **new** | Generic: heading, body, one action, **no illustration slot** (03 §C.9). |

### From 02 (the verification rail and the brand furniture)

| # | Component | Spec required |
|---|---|---|
| 28 | `VerificationRail` | Right column, `cols 10–12` (222px) at `lg`+; label/value pairs in `type.rail`; **collapses to a horizontal ruled strip beneath its content below `lg`** — 02 defines only 375 and 1440, so the 600–1199 behaviour is specified here (see §4.8). Every field has a defined empty form; a missing value renders "Pending", never a blank cell. |
| 29 | `Divider--medallion` | The woven-medallion section divider, Olive, used **at most four times** on the home page. The artwork does not exist — §4.13. |
| 30 | `BulletPetal` | The five-petal list glyph, 6px, Olive, 0.6em from the baseline; also the **only permitted loop in the system** as the 14px loading glyph. My Button spec's generic spinner is replaced by it. Artwork does not exist — §4.13. |
| 31 | `PullQuote` | One per page maximum, display face. |
| 32 | `ComparePair` | 2-up at 4:5 with a 1px Nude gutter, headed "Compare", placed **below** the sequential arrival/after images, never as the opening image and never as a drag-slider. |
| 33 | `AvatarRow` | Family Circle: 48px Nude circles, initials in text face 600 at 16 (9.61 on Nude), 1px Ivory-40 ring, −12px overlap, owner ringed in Olive. No photographs of people, no stock avatars. |
| 34 | `DataTable` | Zebra rules (Nude on Ivory), 8% rules, tabular figures; used by the credit table, the refund table and the permission matrix. |

### From 03 (states my components do not have)

- `ReportSheet` needs states my spec omits: **`preparing`** ("The visit is done.
  The report is being prepared."), **`media-partial`** ("Some photographs are
  still uploading. The rest of the report is complete."), `failed`.
- `Toast` needs the copy contract "Link copied." and nothing that must be kept.
- `Tooltip` **new**, tightly restricted: definitions only (GPS point, AMD, full
  visit, pro-rata). It may **never** carry a rule, a price or a surcharge — 03
  §C.4 and §C.5 both refuse a tooltip for those. Tap-to-open on touch,
  dismissible, never hover-only.
- Validation states missing from my Input spec: duplicate invitee, file too
  large, wrong file type, out-of-range calculator entry, expired invitation,
  expired reset link, session expired.

### From 04 (conversion blocks)

| # | Component | Spec required |
|---|---|---|
| 35 | `PricingFork` **new** | Two doors at the top of Pricing ("No, I haven't seen it in years" → Inspection / "Yes — I want it cared for" → the plans). Stacked below 600. |
| 36 | `TrustLadder` **new** | Three ruled steps — Know → Do once → Keep it cared for — with a price on each. |
| 37 | `GuaranteesBlock` **new** | Three items (name, number, remedy) + the honest-limits paragraph + links to the four legal pages. Appears on Home, Pricing and in the portal visit list — one component, three placements. |
| 38 | `TeamBlock` **new** | Two founders: name, role, `tel:` link, `wa.me` link, 1:1 portrait placeholder. |
| 39 | `HonestyPanel` **new** | "We started in 2026, we have no reviews." Bordered panel on Nude, **body size or a step above**, directly under the guarantees — never small print (03 §C.10 is right; styling it as a disclaimer inverts its job). |
| 40 | `PaymentRealityBlock` **new** | Bank transfer now / card payment when the bank enables it, **no date promised**. |
| 41 | `CreditCountdown` **new** | "Your 65,000 ֏ is credited toward an annual subscription until 14 November." A dated fact. **No timer, no red, no scarcity styling** — that register would end the brand. |
| 42 | `ShareThisPage` **new** | 04 §A5/21: "send this to your family" as a legitimate secondary conversion on marketing pages. Needs its own OG rule, distinct from the report OG. |
| 43 | Calculator → form handoff | Not a component but a missing contract: URL state `?tier=&area=&monuments=`, hidden fields on the consultation form, and the configuration **echoed back** in the confirmation ("You configured: 24 m², 3 monuments, Optimal — 270,000 ֏ AMD/year"). 01 §D4 and 04 §A6 both require it; my calculator spec ends at the total. |

---

# 4. What cannot be built as described

Each is a concrete defect with the fix.

1. **Olive fill carrying a label** — 03 §C.3 ("Olive-filled label with Anthracite
   text") and 04 §B4 ("Olive top band with Anthracite text"). Anthracite on Olive
   = 3.08, Ivory on Olive = 3.42. Not buildable. Fix: C7 — inversion, or
   `Badge--accent` (Deep Olive/Ivory, 6.01). Blocked in the linter.

2. **02's secondary-text opacity ladder is arithmetically wrong.** 02 §A.2 states
   "Anthracite 70% secondary text (7.1:1, passes)". Composited over Nude,
   Anthracite at 70% resolves to ≈`#6B6B6A`, which is **4.29 : 1 — it fails.**
   Every "Anthracite 70%" instance in 02 (helper text, captions, rail labels, the
   FX line, placeholder text) is therefore a failing pair. Fix: secondary text is
   the token `--mc-text-secondary` = `#606161` (**4.87** on Nude, 5.34 on Ivory),
   never an opacity. Opacity is banned for text system-wide; the Ivory-on-dark
   ladder (80% ≈ 8.3) is fine but is likewise replaced by a token.

3. **02's `rail` and `eyebrow` at 11–12px** carry the proof data for a 40–60
   audience, and the rail has no Armenian form (uppercase + tracking). Fix: C9 —
   14px, 0.06em, sentence case in `hy`.

4. **My `heading-2` resolves to 22px in the display face**, below the 24px
   optical floor for Gloock. Fix: minimum raised to 24px; below `sm`, headings
   under 24px are the text face at 600.

5. **My `.mc-hit-44::after` does not work.** `inset: 50% 50% 50% 50%` sets all
   four insets, so the declared `width`/`height` are ignored and the element
   collapses to zero — the 44×44 hit area silently does not exist. Fix:

   ```css
   .mc-hit-44 { position: relative; }
   .mc-hit-44::after {
     content: ""; position: absolute; top: 50%; inset-inline-start: 50%;
     width: max(100%, var(--mc-layout-target-min));
     height: max(100%, var(--mc-layout-target-min));
     transform: translate(-50%, -50%);
   }
   ```

6. **Floating layers have no separation once shadows are removed (C4).** Three
   undefined states: (a) a `Select`/`Combobox` menu opening over an Ivory band is
   Ivory on Ivory — invisible, and it violates 02's own "no Ivory on Ivory" rule;
   (b) `Toast` has no dark-band definition, and its "success rule in `olive-700`"
   would sit at 1.75 on Anthracite; (c) the lightbox controls have no ground.
   Fix: floating layers take the **opposite light** of the band beneath them
   (`--mc-surface-float` resolving to Ivory on Nude bands and Nude on Ivory
   bands, via a `.mc-on-ivory` band scope), plus a 1px `--mc-border-strong`
   outline; toasts on the Anthracite band take `surface-inverse-raised` with a
   Nude label; the lightbox uses the scrim.

7. **`.mc-on-dark` remaps `--mc-text-accent` to Nude** (correct), but three
   components address Deep Olive directly rather than through the token — my
   own header word treatment, 02's "Deep Olive small-caps product name" on the
   inverted Optimal card, and 02's active-nav underline. On Anthracite these
   resolve to 1.75. Fix: no component may reference `olive-700` directly; all
   accent colour goes through `--mc-text-accent` / `--mc-border-accent`, which
   the dark scope rewrites. The linter rejects `var(--mc-color-olive-700)`
   outside the semantic layer.

8. **The verification rail has no rule between 600 and 1199**, and the report
   sheet has none between 375 and 1440 (02 designs only two widths). Fix: rail is
   a right column at `lg`+ only; at `base`–`md` it is a horizontal ruled strip
   beneath its content, two rows of label/value pairs, 1px Anthracite-12 rule
   between, values at the inline-end.

9. **The GPS element is specified two incompatible ways.** 01 §A4.4: "tap reveals
   a static map crop with a pin and coordinates". 02: "not a map screenshot and
   not a red pin — a map tile is someone else's brand and a red pin is a delivery
   app". A tile also carries an attribution licence and a third-party request the
   bank's review disliked. Fix: 02 wins — the plot diagram is the artefact; 03's
   `[Show on map]` stays as an **outbound link** to the visitor's own map app with
   the coordinates. No tiles are served by us.

10. **Two fixed bars can occupy the same block-end.** 02 pins the calculator
    result panel as a 96px bar at the bottom on mobile while the sliders are in
    view; the `StickyCtaBar` is 64–72px and also fixed. Together they take ~168px
    of a ~640px viewport. Fix: `StickyCtaBar` is suppressed while the calculator
    result bar is mounted, and both are suppressed while a form field has focus.

11. **`--mc-tariff-min-height: 480px` cannot survive localisation.** A fixed
    minimum with wrapping `hy` content either wastes 120px in English or
    overflows in Armenian. Fix: delete the token; equalise by
    `display: grid; align-items: stretch` on the band, `min-height: 0` on the card.

12. **Strings with no length limit.** `content-limits.json` has no slot for:
    `link.tertiary` (03's `Actually, I would like to talk to someone first` = 46
    chars — a text link permitted to wrap to three lines, but it must be declared),
    `guarantee.title` / `guarantee.body`, `faq.question` / `faq.answer`,
    `legal.paragraph`, `email.subject` (30–52) / `email.preheader`, `push.title` /
    `push.body`, `role.name` / `role.description`, `rail.label` (12) /
    `rail.value` (18), `placeholder.caption`, `report.recommendation.item`,
    `credit.rule.bullet`. All are added. One conflict inside them: the crew note
    is 120–300 in 01 and 220–320 in 02 — canonical **120–320, wrap, no clamp**.

13. **Assets that do not exist.** The woven-medallion divider band (02 §A.0) and
    the five-petal bullet/loading glyph (02 §A.4) are treated as available; they
    are not. Neither is the 16px simplified mark (my `OPEN-ITEMS` #12), the two
    OG images, or the tightly-bounded exports 02 asks for (my `prepare.mjs`
    produces them from the nine 1080² sources, so that one is covered). Fix:
    three pieces of new artwork are owed — medallion divider, petal glyph,
    simplified mark — all derivable from the master, **[DESIGNER]** to draw or
    ratify. Until they land, the divider is a 1px Olive rule and the loading
    affordance is a fading opacity pulse on the label, not a spinner.

14. **Unresolved variables that will ship as literal braces.** `{REPORT_SLA}`,
    `{LEGAL_ADDRESS}`, `{REG_NUMBER}`, `{WORKING_HOURS}`, the Family Circle member
    limit `{n}`, and the callback SLA "within one working day" (04 §D.3 — unconfirmed
    by the founders). Fix: `lint:strings` fails on any `{…}` in a shipped locale
    that is not on the runtime-variable allowlist; the six above are on the
    **blocking** list in `OPEN-ITEMS.md`, and `{LEGAL_ADDRESS}` and `{REG_NUMBER}`
    additionally gate the bank package.

15. **The pro-rata refund has no defined basis** — by visits consumed or by days
    elapsed. 01 §D.1 and 03 §D.2 both escalate it; it changes the number on the
    cancellation screen, in the refund policy and in the bank submission.
    **[OWNER]**. 01 recommends *by visits consumed*; I agree, for its reason — a
    client who has received one of four visits should never be told they consumed
    27% of the year.

16. **"Most chosen" with zero customers** — C7, **[OWNER]**.

17. **The Express credit has no abuse rule** — once per client or once per plot?
    01 designed for once per plot. **[OWNER]**; it belongs in `products.json` and
    in the Terms.

---

# 5. Naming reconciliation

One canonical name per component, token and screen. Left columns are the names as
they appear in each proposal; the right column is what everyone writes from now
on — in code, in Figma, in the string keys and in conversation.

### 5.1 Components

| 01 | 02 | 03 | 04 | 05 (mine) | **Canonical** |
|---|---|---|---|---|---|
| report artefact / report screen | report sheet | report screen | proof card | `ReportCard` | **`ReportSheet`** (the document) |
| — | — | visit row | — | (absent) | **`VisitListRow`** |
| GPS chip | plot diagram + GPS VERIFIED badge | "Recorded on site" | proof element | GPS chip | **`GpsVerification`** (badge string: `GPS confirmed`) |
| — | verification rail | — | — | (absent) | **`VerificationRail`** |
| pricing card | tariff card | product card | tier card | `TariffCard` | **`TariffCard`** (`variant: one-off \| annual`) |
| Inspection strip | Inspection band | one-off band | one-off band | `TariffCard--standalone` | **`PricingBand`** (`--one-off` / `--annual`) |
| calculator | plot calculator | calculator block | calculator | `Calculator` | **`PlotCalculator`** |
| sticky action bar | sticky mobile CTA bar | sticky foot bar | sticky mobile CTA bar | `StickyCtaBar` | **`StickyCtaBar`** (marketing) + **`ReportShareBar`** (report) |
| share sheet | — | sharing block | — | (absent) | **`ShareSheet`** |
| roles table | permission table | "Who can do what" | permission distinction | (absent) | **`PermissionMatrix`** |
| progress rail | — | "What happens next" | dated schedule | (absent) | **`ProgressRail`** |
| first-entry state | — | the doubt screen | first-entry screen | portal empty state | **`FirstEntryScreen`** |
| bad-news states | — | — | conversion assets | `SPEC-status-postponed` etc. | **`StatusScreen--rescheduled / --no-access / --revisit`** |
| language switcher | language switcher | language switcher | — | in `Navigation` | **`LanguageSwitcher`** (a `SegmentedControl` instance) |
| guarantees | — | guarantees | guarantees block | (absent) | **`GuaranteesBlock`** |
| — | — | honesty paragraph | honesty block | (absent) | **`HonestyPanel`** |
| — | — | — | the fork | (absent) | **`PricingFork`** |
| — | — | — | trust ladder | (absent) | **`TrustLadder`** |

### 5.2 Roles and statuses

| 01 | 03 | **Canonical data value** | **Canonical UI string** |
|---|---|---|---|
| Owner | Owner | `owner` | Owner |
| Manager | Family manager | `manager` | Family manager |
| Member | Family member | `member` | Family member |
| Guest (link) | Guest | `guest` | Guest |
| Postponed | Moved | `rescheduled` | **Moved** |
| — | Being prepared | `preparing` | Being prepared |
| Access blocked | Could not access | `no-access` | Could not access the plot |
| Completed | Completed | `completed` | Completed |
| Scheduled | Scheduled | `scheduled` | Scheduled |
| Re-visit requested | Repeat visit | `revisit-requested` | Repeat visit requested |

My spec files rename accordingly: `SPEC-status-postponed.md` →
`SPEC-status-rescheduled.md`.

### 5.3 Tokens

| Appears as | **Canonical token** |
|---|---|
| Deep Olive / `#575E3B` / accent | `--mc-color-olive-700` (L1) → `--mc-text-accent`, `--mc-border-accent`, `--mc-surface-accent-strong` (L2) |
| Olive / `#7C8654` / decorative | `--mc-color-olive-500` → `--mc-border-decorative`, `--mc-surface-accent-solid`. **Never a text or label token.** |
| Nude / page / ground | `--mc-surface-page` |
| Ivory / paper / card / raised | `--mc-surface-raised` |
| "Anthracite 70%" (02) | **deleted** → `--mc-text-secondary` (`#606161`) |
| red / danger / error | `--mc-color-feedback-error` (+ `-subtle`). `danger`, `warning`, `success` are forbidden strings in token names. |
| radius md/lg/xl (mine) | **deleted** → `--mc-radius-0 / -sm / -full` |
| elevation 1–4 (mine) | **deleted** → hairline + ground change; `--mc-surface-scrim` only |
| rail / eyebrow / overline | `--mc-type-rail` (14, tabular) and `--mc-type-overline` (13, decorative) — two different roles, no longer interchangeable |
| body 16 / 17 / 18 | `--mc-type-body` (16→17 clamp), `--mc-type-body-lg` (17→19) |

### 5.4 Screens and routes

01's sitemap is canonical, unchanged, and becomes `layout/ROUTES.md`. Two
clarifications the others need: the guest report lives at **`/r/:shareToken/`**
(short, retypable, not under `/portal`), and Guarantees exists **both** as a page
(`/en/guarantees/`, 01) **and** as a block in three placements (04) — one
component, four surfaces.

---

# 6. The handoff package — updated inventory and ownership

One repository, `memorycare-design-handoff-v1.1/`. **If it is not in this tree it
is not a requirement.** Every file has one owner; the owner is the only person who
may change it, and it is the source of truth for exactly one thing.

| Path | Owner | Source of truth for |
|---|---|---|
| `README.md` | Design system (me) | Order of operations; the "tokens.json wins over Figma" rule |
| `DECISIONS.md` | **Owner (Hayk)** | Binding rulings. Overrides every other file in this tree. |
| `CHANGELOG.md` | Me | What changed per version and what must be re-checked |
| `OPEN-ITEMS.md` | Me (entries owned individually) | Everything unresolved, with an owner and a date |
| `ACCEPTANCE-CHECKLIST.md` | Me | What Igor signs off against |
| `DEVELOPER-DECISIONS.md` | Me | The eleven things that are Igor's call — unchanged |
| `tokens/tokens.json` | Me | **Every value in the product.** No exceptions. |
| `tokens/build/*` | Me (generated) | Nothing — generated, committed, never hand-edited |
| `tokens/CONTRAST-MATRIX.md` | Me | The complete permission list of colour pairs |
| `tokens/stylelint-mc-contrast/` | Me | Machine enforcement of the above + the Olive-label ban |
| `components/00-INDEX.md` | Me | The component list, status, Figma node id |
| `components/SPEC-*.md` (18 existing + 34 from §3) | Me, with the claimant named in each | Anatomy, measurements, state matrix, ARIA, responsive rule, content limits, "do not" list |
| `layout/GRID.md` | Me | The single breakpoint set (C8) |
| `layout/ROUTES.md` | **UX architect (01)** | Every URL, locale variants, meta rules |
| `layout/PAGE-TEMPLATES.md` | **UX architect (01)** | Section order per route, by component name |
| `layout/JOURNEYS.md` | **UX architect (01)** | The three journeys, incl. the split-payer case |
| `portal/PERMISSION-MATRIX.md` | **UX architect (01)**, ratified by **[OWNER]** | Who may do what; the data contract behind Family Circle |
| `portal/NOTIFICATION-MATRIX.md` | **UX architect (01)** | Event × recipient routing, incl. the local contact |
| `visual/ART-DIRECTION.md` | **Visual lead (02)** | The visual concept, section rhythm, Olive's five jobs, the no-shadow rule |
| `visual/PHOTO-BRIEF.md` | **Visual lead (02)** | Ratio table, treatment rules, framing, what the crew must shoot in September |
| `visual/MOTION.md` | **Visual lead (02)** | The six permitted behaviours and the forbidden list |
| `content/strings.en.json` | **Writer (03)** | Every user-facing string. No literal text in any component. |
| `content/strings.hy.json` / `.ru.json` | **Writer (03)** → localiser | Keys present, values `TODO-TRANSLATION` |
| `content/content-limits.json` | Me, populated by **03** and **02** | Grapheme ceilings per slot per locale |
| `content/COPY-RULES.md` | **Writer (03)** | The denylist, the voice principles, the validation tone rules |
| `content/products.json` | **[OWNER]**, maintained by **04** | Prices, surcharge rates, credit rules, the 60-day window, the 95,000 arithmetic. **The only place a price exists.** |
| `conversion/OBJECTION-MAP.md` | **Conversion (04)** | Which block answers which objection, and with what proof |
| `conversion/CTA-PLACEMENT.md` | **Conversion (04)** | Count and placement of every CTA; the "never next to a photograph" rule |
| `conversion/POST-PAYMENT.md` | **Conversion (04)** | The five signals between payment and first visit |
| `brand/LOGO-USAGE.md` | Me | Clear space, minimum sizes, forbidden uses |
| `brand/logo/source/` | **[DESIGNER]** | The nine original 1080² SVGs, untouched |
| `brand/logo/production/` | Me (generated by `prepare.mjs`) | The eleven prepared lock-ups |
| `brand/FONTS.md` | Me | Licences, subsets, `unicode-range`, the Gill Sans substitution label, **and every unverified glyph claim (§7)** |
| `brand/fonts/` | Me | Self-hosted woff2, subset per script, ≤180 KB per locale |
| `brand/favicon/`, `brand/og/` | Me | Icon set; the two OG images |
| `placeholders/` | **Visual lead (02)**, cut by me | Every placeholder, each naming ratio, pixel size, subject and source |
| `qa/contrast.spec.ts` | Me | axe-core over every route, 3 locales, 360 and 1280 |
| `qa/strings.spec.ts` | Me | Denylist, length limits, tagline full stop, unresolved `{}` |
| `qa/meta.spec.ts` | Me | The OG image is never a photograph |
| `qa/glyphs.spec.ts` | Me | **New — §7.** Codepoint coverage of every shipped font file |
| `qa/prices.spec.ts` | Me | **New.** Every price traces to `products.json`; no `line-through`; no `save`/`discount` near a price |
| `qa/VISUAL-BASELINES/` | Me | Reference screenshots at 360 / 900 / 1440 |
| `figma/FIGMA-MAP.md` | Me | node-id → spec → code-file |

Two rules that hold the tree together, unchanged from v1.0 and now more load-bearing
because five people write into it: **Figma is the source of truth for composition,
files are the source of truth for values** — and **a value that is not in
`tokens.json` does not exist**, including a value the design lead is certain about.

---

# 7. Typeface claims — all unverified, and the rule that makes it safe

This session has **no network access**. Every statement below about what a font
file contains is therefore **UNVERIFIED**, including statements I made confidently
in round one. They are recorded in `brand/FONTS.md` with this exact label and are
resolved by a build-time test, not by anybody's memory.

| Claim | Made by | Status |
|---|---|---|
| **Cabin contains ֏ (U+058F), the dram sign** | `DECISIONS.md` §5 asks; 03 §C.11 asks | **UNVERIFIED.** If absent, every price on the site breaks. |
| **Gloock does not cover Cyrillic** | me, §A3.4 | **UNVERIFIED.** I asserted it; I cannot check it. If it does cover Cyrillic, the Russian display problem disappears. |
| Gloock covers Latin + Latin-ext only | me | **UNVERIFIED** |
| Gloock has no Armenian | 02, me, brief | **UNVERIFIED** (very likely true, still untested) |
| Cabin's Cyrillic is "adequate" | 02 §A.1 | **UNVERIFIED** |
| Cabin has no Armenian | brief, me | **UNVERIFIED** |
| Gloock has tabular figures | assumed by 02's `price` in Gloock | **UNVERIFIED** — 03 §C.11 raises it |
| Noto Serif/Sans Armenian ship 400 and 600 | me | **UNVERIFIED** |
| Playfair Display covers Cyrillic | me | **UNVERIFIED** — and moot after C3 |

## The fallback rule — the build is correct whichever way each claim resolves

**R1 — The currency glyph is never bound to a text or display face.**
Every `֏` is emitted by the price formatter inside its own element:

```html
160,000 <span class="mc-currency">֏</span> AMD
```
```css
.mc-currency { font-family: var(--mc-font-currency); }
```
```css
--mc-font-currency: "Noto Sans Armenian", "Noto Sans", "Cabin", system-ui, sans-serif;
```

If Cabin has the glyph, the stack resolves to it visually unchanged. If it does
not, the Armenian face supplies it and prices still render. Either way it is one
line to change and the failure cannot be silent — see R3. This satisfies
`DECISIONS.md` §5's requirement for "a fallback face for the currency glyph only,
stated in the type spec". The word `AMD` (bank requirement) is always printed
next to the symbol, so even a total glyph failure leaves the price legible.

**R2 — Every `@font-face` declares an explicit `unicode-range`.** A codepoint
outside the declared range is never requested from that file, so a missing glyph
falls to the next family in the stack and **never renders as tofu**. Every stack
terminates in `system-ui` and a generic family; no stack can dead-end.

**R3 — `qa/glyphs.spec.ts` turns every unverified claim into a build failure.**
Runs in CI over the actual shipped `woff2` files with `fontkit`, asserting, per
locale stack:

- U+058F (֏) present in the family bound to `--mc-font-currency`;
- U+0531–U+058A + U+FB13–FB17 present in the `hy` stack;
- U+0400–U+04FF present in the `ru` stack;
- U+0030–U+0039 present, and the `tnum` (or default tabular) feature available,
  in whichever family sets prices;
- total per-locale font weight ≤ 180 KB.

A locale does not ship until its assertion passes. This is what makes it safe to
have written a type spec without a network: nothing depends on my recollection.

**R4 — Prices never depend on the display face for correctness.** They may be
*set* in the display face, but the currency glyph is bound by R1 and the figures
must be tabular; if `qa/glyphs.spec.ts` reports that the display face has no
tabular figures, `--mc-type-price` falls back to the text face at 600 — a single
token change, no component edits. (This also resolves 03 §C.11's second worry.)

**R5 — Every mock, PDF and built page carries the substitution label:**
*"Cabin is used as a free substitute for Gill Sans (commercial Monotype). It is
not the brand text face."* — in `FONTS.md`, in the `tokens.json` `$description`,
as a comment in the generated CSS, on Figma page `01 · Foundations`, and in the
footer of every exported spec. Per `DECISIONS.md` §4 and 02's open item 6.

---

# 8. What only the owner can decide

Everything else in this memo converges without escalation.

1. **Pro-rata basis** — by visits consumed or by days elapsed. Blocks the
   cancellation screen, the refund policy page and the bank submission.
   Recommendation: **by visits consumed**.
2. **"Most chosen"** — a behavioural claim with zero customers. Recommendation:
   **"Our recommendation"** until there is data.
3. **The Express credit guard** — once per client or once per plot.
   Recommendation: **once per plot**.
4. **The consent checkbox on the consultation form** — kept (C13) unless counsel
   says otherwise.
5. **Callback SLA** — "within one working day" is written into six surfaces and
   is not yet confirmed by the founders.
6. **Legal address and registration number** — the oldest open item, now on the
   critical path for the footer, About, Contacts and the bank package.
7. **Report SLA** (`{REPORT_SLA}`) — appears in the portal, in emails and in the
   first-entry screen.
8. **[DESIGNER]** — Deep Olive ratified or replaced; a single display face with
   Armenian coverage; the medallion divider and petal glyph artwork; the 16px
   simplified mark; a colour mark that survives a Nude ground.
