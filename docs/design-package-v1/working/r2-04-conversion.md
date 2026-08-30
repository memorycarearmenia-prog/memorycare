# r2-04 — Conversion & Trust: review of round one

**Author:** Conversion and Trust Strategist
**Date:** 30.08.2026
**Reviewed:** `01-ux-architect.md`, `02-visual-lead.md`, `03-content.md`,
`05-design-system.md`, against `DECISIONS.md` and `BRIEF.md`, and against my own
`04-conversion.md`.

**Standard I judged by, and only this:** does the decision increase or decrease
the number of completed consultation requests and completed payments from a
stranger who has never met us? Where a colleague's answer converts as well as
mine and looks better, I say so and I withdraw mine. Two of my own positions
lose below.

---

# 1. Conflicts

## C1. The hero fold at 360/375 — my demand versus the dark hero and the headline

**The disagreement.** I wrote (04, B1) that the full proof card must be visible
above the fold at 375px. The visual lead (02, §A.2 rhythm) makes the hero a
full-bleed **Anthracite** band with an Ivory report sheet on it. The UX
architect (01, A3.1) puts only the **top 180px** of the report card above the
fold and crops it deliberately. The writer (03, Block 1) supplies an H1 of 57
characters — over the visual lead's hard max of 52 and enough to run to four
lines at 40px on a 360px screen.

**What breaks either way.** Do the arithmetic at 360×640, usable first paint
≈ 560–600px: header 64 + eyebrow 16 + H1 at three lines 132 + subhead at four
lines 104 + primary CTA 48 + the minimum inter-block space 80 = **444px**.
There are 120–160px left. A full report card is 320px minimum. My demand is
arithmetically impossible without deleting either the H1 or the CTA, and
deleting the CTA above the fold costs more requests than a cropped card does.

**Resolution — I withdraw my version.** The UX architect's deliberate crop wins,
and the visual lead's dark hero makes it work *better* than my light one would
have: an Ivory sheet on Anthracite is the highest figure/ground separation
available in this palette, so a 140px sliver still reads unmistakably as a
document rather than as a photograph. I attach three conditions, and they are
the conversion content of the block:

1. **The sliver above the fold must be the metadata, not the image.** The part
   that survives the crop is the sheet header strip — `14 September 2026 ·
   Tokhmakh · Plot 12` and the `GPS confirmed` chip. Proof is the coordinate and
   the date; a cropped photograph proves nothing.
2. **A one-line verification strip sits under the subhead, above the CTA**, in
   `rail` type: `Date · Cemetery · GPS confirmed`. 24px, and it puts proof
   before the ask without costing a fold.
3. **Order at ≤sm is: eyebrow → H1 → subhead → primary CTA → cropped report
   card.** At `lg` the card moves alongside. The CTA is never below the card on
   a phone.

And the H1 must come down to ≤52 characters (see C2).

## C2. The hero H1 — length versus the writer's sentence

**The disagreement.** Writer: *"You will see exactly what was done at the grave,
and when."* (57). Visual lead's budget: 38–46, hard max 52. Design system's
`hero.h1` ref: 62. UX architect: 34–56.

**What breaks.** At 57 characters the H1 takes a fourth line at 360px, which
pushes the CTA to 492px and leaves under 70px of the report card — the crop
stops working and the block loses its only proof element. At the other extreme,
trimming to 40 characters costs the writer's second clause, which is the half
that defuses the diaspora's actual fear ("and when").

**Resolution.** Keep the writer's sentence, cut four characters:
**"You will see exactly what was done, and when."** (44). "At the grave" is
carried by the eyebrow (`Yerevan cemeteries · scheduled care`) and by the report
card directly beneath it, so it is not lost — and the disambiguation from
dementia care that the brief requires is done by the eyebrow, the `<title>` and
the meta description, which is where it belongs anyway. Adopt 52 as the enforced
ceiling in `content-limits.json` (design system currently says 62 — lower it).

## C3. Where Express and Special live on the pricing page

**The disagreement — four different layouts.**

| | Inspection | Express | Optimal | Maximum | Special |
|---|---|---|---|---|---|
| Me (04, A6) | one-off band | one-off band | card row | card row | one line under the calculator |
| UX architect (01, A3.2) | separate card below a divider | *(not placed)* | card row | card row | slim band |
| Visual lead (02, tariff cards) | full-width rule band above | **card row** | card row | card row | ruled row beneath |
| Writer (03, C.3) | one-off band | one-off band | card row | card row | **card in the row** |
| Design system (05, A4.7) | `TariffCard--standalone` above | **card row** | card row | card row | **fifth card, footer position** |

**What breaks each way.** Express in the three-card row makes the row read as
"three plans, one of which is cheap" — a 65,000 one-off sitting beside 160,000
and 200,000 annuals is the classic anchor failure: it does not sell Express, it
makes Optimal look expensive, and it invites the reader to compare across a
category boundary. Special as a card adds a fifth option with no price, and a
priceless card in a price comparison is where a hesitant reader stops and leaves
— it reads as "call us for a quote", which is exactly the diaspora fear the
whole calculator exists to kill.

**Resolution — the writer's two-band model, with Special demoted.**

- **Band 1, one-off services** (Inspection 20,000 · Express 65,000), on the
  ground, distinct form, the credit rule stated once beneath the band as a
  property of the band.
- **Band 2, annual subscriptions** — exactly **two** cards, Optimal and Maximum.
  Two options differing on one axis (4 visits vs 6) is a sub-10-second decision.
- **Special** is one ruled line under the calculator, as the visual lead drew it,
  with `Start with an Inspection` as its action.

This is the writer's structure minus his Special card, and it kills the visual
lead's and the design system's three-card row. Design system: `TariffCard` is a
2-up grid at `md`+ and `TariffCard--oneoff` is the band, and there is no fifth
card. This is a component-shape change, so it needs to be made before Igor
builds.

## C4. Marking Optimal as the leading choice

**The disagreement.** Visual lead: Optimal card **inverted to Anthracite**, its
CTA a Nude fill with an Anthracite label, neighbours on Ivory with Deep Olive
CTAs. Design system: 2px Deep Olive border + a Deep Olive/Ivory badge, no
inversion. Me and the UX architect: elevation and space, not size.

**What breaks.** The inversion is the better-looking of the two and I would take
it on aesthetics alone — but it has a specific conversion defect. On a page whose
primary-button language is "Deep Olive fill = the thing to press", inverting the
leading card gives the **leading product the only button that is not Deep Olive**.
The eye at speed picks the strongest of three buttons, and after the inversion
that is one of the two products we did not want chosen. On a 360px stack, where
the cards are read one at a time and the row context is gone, the Nude button
just reads as a secondary.

**Resolution.** Design system's version: Optimal keeps the light card, takes a
**2px Deep Olive border** and a **Deep Olive fill / Ivory label** badge reading
"Most chosen", and is the **only** card in the band with a `primary` CTA —
Maximum's CTA drops to `secondary`. That is three consistent signals (border,
badge, button weight) and none of them costs the button language. If the visual
lead wants the inversion, it is acceptable **only** on the condition that
Maximum's CTA also becomes secondary, so Optimal's Nude button is the only
filled button in the band. Either is fine; the current combination is not.

## C5. Error colour — three proposals contradict the owner outright

Covered in §2 below, because it is a contradiction with `DECISIONS.md` and not a
peer disagreement. It is listed here only so the convergence step does not miss
that it also *is* a conflict between us: visual lead asks for two semantic
colours, UX architect and writer both ban red, the design system ships
terracotta. The owner has ruled; three of five documents must change.

## C6. Shadows, radii and the two type scales

**The disagreement.** Visual lead: **no shadow exists in the system**, radius
`0` or `2px` only, "no 8/12/16 friendly radii — they are the wellness-template
tell". Design system: a four-step elevation ladder, `radius-lg` / `radius-xl` /
`radius-full` on cards, modals, sliders and sheets.

**What breaks.** These are not reconcilable by taste; they produce two different
products. The conversion stake is small but real and runs in the visual lead's
favour: the whole trust argument of this brand is "these are records, not
marketing", and a 16px-radius card with a soft shadow is the visual grammar of a
wellness subscription. There is one place the design system is right — a modal or
a bottom sheet with no shadow and no scrim is invisible against the page, and
the visual lead already conceded this with an Anthracite 60% scrim.

**Resolution.** Adopt the visual lead. `radius-sm: 2px` for buttons, inputs,
cards, badges, modals; `0` for bands, images, the report sheet, dividers;
`radius-full` only for the slider thumb and the petal bullet. Elevation ladder
reduced to two tokens: `elevation-0: none` and `elevation-scrim` for overlays.
The design system keeps the token names so nothing else has to change.

**Type scale.** Three scales were written (02 px tables, 01 px table, 05
`clamp()`). The design system's `clamp()` implementation wins — it is the file
Igor gets — but it must absorb two rules from the visual lead that it currently
breaks: **Gloock is never rendered below 24px** (`mc.type.heading-2` bottoms out
at 22px at 360px, so either raise its floor to 1.5rem or make `heading-2` the
text face below `md`), and **body never below 16px on the site**.

## C7. Is there a calculator on the home page?

Visual lead's rhythm puts the calculator at home §7. UX architect, writer and I
put it on Pricing only.

**Resolution — Pricing only.** Two live calculators double the maintenance of
the one component whose arithmetic can embarrass us, and they split the
analytics on the single highest-value interaction on the site, which is the one
number I want to measure cleanly. Home carries the pricing teaser plus the
sentence *"One price list. The same for a client in Yerevan and a client in Los
Angeles."* and a link into `#calculator`. The sentence is what does the
trust work; the sliders only prove it.

## C8. The consultation form has grown from three fields to seven rows

**The disagreement.** The brief says three fields. My version: 3 required + 1
collapsed optional. UX architect: name, contact, cemetery, *local family member*
(disclosure), *preferred contact time* (3 chips), *message*, *consent checkbox*.
Writer: name, contact, cemetery, optional note, *consent checkbox*.

**What breaks.** Every visible row pushes the submit button further down a 360px
screen. At seven rows the button is off-screen on first paint, and a form that
looks long to a person deciding at 1 a.m. is abandoned before it is read. Against
that, the UX architect is right that this is structurally a split-payer business
and the Yerevan-contact capture is worth real money on the call.

**Resolution.**
- Three required fields, visible: name · phone or email · cemetery or city.
- **One** disclosure link, `Add a note or a family contact`, holding the
  free-text note *and* the two Yerevan-contact fields. One tap for the minority
  who need it, zero cost for everyone else.
- **Cut the preferred-contact-time chips.** They are guessed wrong more often
  than right and are answered better in the first ten seconds of the call.
- Consent: see C9.

## C9. The consent checkbox

**The disagreement.** UX architect and writer both make an explicit consent
checkbox **required**. I rejected it.

**What breaks.** A required checkbox on a three-field form is the single most
common submit-blocker in lead forms, and the failure is silent for an older user
who does not connect the red field at the top with the box at the bottom.
Against that: part of this audience is in France and Germany, so GDPR is live,
and the writer is right that a consent record has value.

**Resolution.** Replace the checkbox with a statement directly under the button:
*"By sending this you agree we may contact you about this request. Privacy
policy."* Processing a callback that the person explicitly requested is
performance-of-a-request, not marketing consent; a checkbox is the wrong
instrument and it costs requests. A checkbox is required **only** if we ever add
a marketing-mailing opt-in, and we are not adding one. **This needs a five-minute
legal confirmation before launch** — I have listed it in §5.

## C10. Prices on the report screen

**The disagreement.** I wrote "zero prices, zero upsell in the report block",
absolute (04, C3). The writer (03, C.7) allows prices in the **recommended-work**
block for Owner and Family manager only, after a full-width rule and a change of
ground. The UX architect allows the same. Guest view: all three of us remove it
server-side.

**Resolution — I withdraw my absolute.** The brief itself scopes the ban to the
guest view ("no prices and no upsell" for someone without an account), and a
recommendation list with no prices forces the owner into a phone call to learn
what a repair costs, which loses one-off revenue and adds support load. The
writer's containment is the right shape. I add two conditions: the priced block
is **last**, after every photograph, and it can never appear in the report **PDF**
that gets forwarded — the PDF is the artefact that circulates in a family chat
and it must be price-free like the guest view.

## C11. Count-up on the calculator total

Visual lead: "numbers change instantly, no count-up — a price that rolls like a
slot machine is exactly the wrong register." UX architect: animate on
`pointerup` only. Design system: 220ms count-up.

**Resolution — the visual lead.** Instant. The count-up belongs to gamified
fintech and it is the one animation on this site a 55-year-old will read as a
trick. The design system's `aria-live` announcement on release stays.

## C12. Report block order

Four orders were written. **Adopt the UX architect's** (01, A4.4): masthead →
confirmation (date, status, GPS) → **crew note** → work performed → photographs →
video → recommendations → documents → actions → next visit. It matches the
brief's rule and it puts the one human sentence in the product *before* the
images, which sets the register. Keep the design system's gallery rule inside
block 5: the first image is the plot **after** the visit; before-images are
labelled and start at position 2.

## C13. Header ground and the language switcher

Visual lead: header Ivory. UX architect and design system: header on the page
ground. Minor, but it must be decided once or it will be built twice.
**Resolution: header on the page ground (Nude) with a hairline on scroll** —
it keeps the design system's testable rule ("any full-bleed section is Nude")
intact, and the mobile sticky CTA bar stays Ivory so it reads as a floating
object.

**Language switcher:** design system uses `ARM · ENG · РУС`, writer uses native
names. **Use native script** — `ՀԱՅ · ENG · РУС`. A visitor who reads Armenian
should see their language in their alphabet without a click; that recognition is
worth more than the alignment of three Latin triplets.

---

# 2. Contradictions with the owner decisions

**Ranked by cost of leaving it unfixed.**

### 2.1 Error colour — three documents contradict `DECISIONS.md §2` head-on

- **UX architect, A8:** *"No red. We have no red in the palette and we are not
  adding one. Errors use Deep Olive plus an icon plus explicit text."*
- **Writer, C.9:** *"Errors sit on Nude with Anthracite text. Never red."*
- **Visual lead, inputs + B.8:** error is a 2px Anthracite border and an
  Anthracite bar; then asks the owner to approve **two** semantic colours.
- **Design system:** ships `#8C3A2E` correctly — and is the only one that does.

The owner ruled: one muted terracotta `#8C3A2E`, errors only, and the reasoning
he gave is a conversion reasoning — *a missed error is an unfinished payment*.
All three must change. Deep Olive as the error colour is actively harmful: Deep
Olive is also our link colour and our primary button fill, so an error field and
a call-to-action would be the same colour on the same screen.

The visual lead's request for two semantic colours is **answered and closed** —
no second colour. Postponement and no-access states are carried by `nude-600`
grounds, glyph and wording, exactly as he designed them.

### 2.2 Sibling token names the owner explicitly forbade

`DECISIONS.md §2`: the token name must make the restriction obvious, with **no
sibling `-success` / `-warning`**. The design system ships `mc.color.danger.*`,
plus `Badge--warning`, `Badge--danger`, `Toast--success`, `Toast--warning`,
`Toast--error` and a **`Button--danger` variant** (`bg danger-600, fg white`).

- Rename the colour tokens to `--mc-color-feedback-error` / `-error-subtle`.
- **Delete the `danger` button variant.** Terracotta is for validation and
  payment failure only; a destructive-action button in it is a third use the
  owner did not authorise — and the UX architect is right that "Cancel
  subscription" should be a calm Deep Olive text link, not a red button.
- Badge and toast variants keep their *behaviour* but lose the colour-family
  names: `Badge--neutral` (nude-600 ground) for postponed and no-access,
  `Toast--confirm` (Olive rule) for success. Nothing green, nothing amber — the
  design system already complies visually; only the naming contradicts.

### 2.3 The 95,000 figure is missing from four documents out of five, including mine

`DECISIONS.md §3` requires it in the **calculator and on the pricing page**.

- **UX architect** has it — in the calculator's one-off mode only. Compliant as
  far as it goes; the pricing-page half is missing.
- **Writer's pricing copy** states the credit in words ("comes off the
  subscription price") but never shows the number. That is under-delivering an
  explicit owner instruction.
- **Visual lead** and **design system**: absent.
- **Mine:** absent. I wrote the credit mechanics in full and never printed the
  result. That is my own contradiction with the ruling and I am correcting it in
  §4 below.

### 2.4 The dram sign in a display face — `DECISIONS.md §5`, unanswered and worse than stated

The owner asked whether **Cabin** contains ֏ (U+058F). Nobody checked (no
network), and the writer flagged it (03, C.11). But the design system has created
a second, larger version of the same problem that nobody noticed:
**`mc.type.price` is set in the display face**, and **Gloock is Latin and
Latin-ext only** — it certainly does not contain ֏. So on the current spec every
price on the site renders the numerals in Gloock and the dram sign in an
unpredictable system fallback, at 40px, side by side. That is visible on the most
scrutinised number on the site.

**Answer, and it costs one line:** bind U+058F to a face that certainly has it,
independently of locale:

```css
@font-face { font-family:"MC Dram"; src:url("/fonts/noto-sans-armenian-400.woff2") format("woff2");
  font-weight:400; font-display:swap; unicode-range:U+058F; }
```

…and put `"MC Dram"` first in **both** `--mc-font-display` and `--mc-font-text`.
This resolves the owner's open item without needing to verify Cabin at all, and
it also fixes Gloock. Additionally: **set the currency glyph and the letters
`AMD` in the text face at `type.body`** even when the numerals are Gloock — the
writer's format `160,000 ֏ AMD` is a numeral plus a label, and the label was
never display type.

### 2.5 Legal entity name — closed, but one document still asks

`DECISIONS.md §1`: **MemoryCare LLC**. The writer's open item 6 still asks which
spelling is registered. It is answered; the design system's denylist already
fails the build on `Memory Care`. Nothing to do but close the item.

### 2.6 Credit window — closed, but one document still asks

`DECISIONS.md §4`: **60 days**, one credit only, larger of the two, fires at
signature. The UX architect's open item 4 (30 vs 60) is answered: 60. The
writer's copy is already correct. The UX architect's own recommendation of
**once per plot** is not in `DECISIONS.md` and should be — see §5.

### 2.7 Photography placeholders

`DECISIONS.md §4` requires each placeholder to be labelled with the shot that
replaces it, plus exact ratio and crop. The visual lead's §A.5 is the best
compliance in the set and should be adopted verbatim by everyone; the design
system's `surface.media-placeholder` token currently has no labelling contract
attached to it and needs one.

---

# 3. Where a colleague's decision will cost us requests or payments

Specific mechanism, specific step, specific audience, specific alternative
behaviour.

**3.1 — Required consent checkbox (01 A6.1, 03 A.1.4).**
*Step:* the last row of the consultation form. *Audience:* both, worst for local
40–60. *Mechanism:* the user fills three fields, presses the button, nothing
appears to happen except a message at the top of a form they have already
scrolled past; on a 360px screen the invalid checkbox is off-screen. *What they
do instead:* press again, then leave. See C9 for the fix.

**3.2 — Express inside the three-card row (02, 05).**
*Step:* the pricing comparison, first ten seconds. *Audience:* local premium, who
skims and decides fast. *Mechanism:* a 65,000 one-off placed beside a 160,000
annual is read as the cheap plan; the reader either picks it (we lose the annual)
or reads 160,000 as 2.5× the "normal" price and stalls. *What they do instead:*
buy Express and never convert, or leave to "think about it". See C3.

**3.3 — Special as a priceless card (03 C.3, 05 A4.7).**
*Step:* same screen. *Audience:* diaspora. *Mechanism:* a card reading "priced
individually" in a row of published prices re-opens the exact fear the calculator
exists to close — *there is a price they will not show me*. *What they do
instead:* they stop trusting the other prices on the page.

**3.4 — Optimal inverted with a Nude button (02).**
*Step:* choosing between two plans. *Mechanism:* the leading product ends up with
the visually weakest button on the page. See C4.

**3.5 — Deep Olive as the error colour (01 A8, 03 C.9).**
*Step:* form validation, and — much worse — the payment-failure screen.
*Mechanism:* the error indicator is the same colour as every link and every
primary button on the page, so it does not read as an interruption. *What they
do instead:* on the form they resubmit blind; on a failed payment they assume it
went through. The owner's own reasoning, verbatim: *a missed error in this
product is an unfinished payment.*

**3.6 — The 640px-tall calculator result panel pinned to the bottom of the
viewport at 375 (02, calculator).**
*Step:* the price reveal. *Mechanism:* a 96px pinned bar plus a 72px sticky CTA
bar plus the iOS chrome leaves under 300px of slider area on a small phone; the
user drags the thumb and cannot see the tick labels and the total simultaneously.
*Fix:* the result sits **immediately below** the two sliders, not pinned, and
the sticky CTA bar suppresses itself inside the calculator section — the
calculator has its own contextual CTA and does not need the global one.

**3.7 — Magic-link-primary login (01, `/portal/login/`).**
*Step:* first portal entry, days after payment. *Audience:* diaspora, especially
the Russia segment. *Mechanism:* the magic link lands in spam or is delayed by a
corporate filter; the client has paid 160,000 ֏ and cannot get in, which is the
worst possible moment to be locked out. *Fix:* magic link **plus** a password set
during activation, both offered on the same screen, and a `Send it again` that
also offers WhatsApp delivery of the link. Keep the phone number on the login
screen.

**3.8 — A cropped hero image with no CTA above it (my own original spec).**
Already withdrawn in C1.

**3.9 — `Request a consultation` at 25 characters as a card CTA (03 C.2).**
*Mechanism:* it wraps to two lines inside a 2-up tariff card at `md`, and the
writer's own solution is to let the button grow. A two-line button inside a card
row breaks card-height equalisation and reads as a layout fault. *Fix:* the
**card** CTA is `Free consultation` (17); the **section-level and sticky** CTA is
`Request a free consultation`. One label per context, held constant across the
site — my A3 rule about a single site-wide label is hereby softened to two
labels, both containing the word "consultation", because the wrap costs more
than the split.

**3.10 — Suppressing the sticky CTA bar only after "the hero leaves the
viewport" (02, 05) versus `scrollY > 480` (01).**
*Mechanism:* the visual lead's dark hero at `lg` can be 900px tall; a user who
scrolls 500px has no visible CTA at all for two screens. *Fix:* the bar appears
at `scrollY > 320` on all breakpoints where it exists, and hides on
`focus-within` of any form (design system's rule, which is correct).

---

# 4. The 95,000 figure — exact specification

The owner approved it, requires it in two places, and forbade it from reading as
a discount. This is that specification.

## 4.1 Where it appears — four places, and nowhere else

**(a) Pricing page, inside the credit block beneath the one-off band.**
As a worked example, in body type, at the same size as the sentences around it:

> **How the credit works.** If you have already paid for an Inspection or an
> Express visit, that amount comes off the price when you sign an annual
> subscription within 60 days.
>
> Worked example: an Express visit is 65,000 ֏ AMD. If you then sign Optimal,
> the first year is 160,000 − 65,000 = **95,000 ֏ AMD**, and 160,000 ֏ AMD in
> each year after that.

**(b) Calculator, one-off (Express) mode only, as the third result row.**
It appears only after the visitor has switched the calculator into Express mode —
i.e. it is a consequence of a path they chose, never the calculator's default
state. Recomputed with surcharges, so a 24 m² plot shows its own arithmetic.

**(c) Portal, after a one-off has been paid**, on the plot overview:
*"Your 65,000 ֏ AMD is credited toward an annual subscription until
14 November 2026."* A stated fact with a date. No countdown, no colour change as
the date approaches, no reminder styled as urgency.

**(d) The written quote sent after the consultation call** (see §5 — this
document does not yet exist and must). Same arithmetic, same sentence.

**Nowhere else. Explicitly not:** the hero, the Optimal card, the Express card's
price line, any badge, any meta description, any ad headline, the sticky bar, or
the footer.

## 4.2 How it is worded so it reads as mechanics

Six rules, all enforceable in the string linter:

1. **Always show the subtraction, never only the result.** `160,000 − 65,000 =
   95,000 ֏ AMD`. Arithmetic reads as a rule; a bare 95,000 reads as a price
   somebody set for you.
2. **Always name the mechanism in the same sentence** — "an amount you have
   already paid comes off". The money is not given away; it is transferred.
3. **Always state the second year in the same sentence** — "and 160,000 ֏ AMD in
   each year after that". This is the single most important guard: it converts
   95,000 from a price into a one-time consequence.
4. **Never these words:** `save`, `saving`, `discount`, `off` used alone, `deal`,
   `offer`, `special`, `only`, `just`, `instead of`, `was/now`, `%`. Add all of
   them to the design system's denylist alongside `bestseller` and `monthly`.
5. **No visual discount grammar.** No strike-through on 160,000 anywhere, ever.
   No colour on the 95,000, no larger type, no badge, no ribbon, no red
   (terracotta is errors only, and a discount tag in the error colour would be a
   double violation). The 95,000 is set in the same type role as the sentence
   containing it.
6. **Full currency form every time** — `95,000 ֏ AMD`, per the writer's §0.5.

## 4.3 What must be true elsewhere, or the figure devalues the 160,000

These are load-bearing. Each one, if broken, turns the mechanic into a discount.

1. **160,000 ֏ AMD is the only price on the Optimal card.** No second figure, no
   "from", no footnote-with-a-number on the card.
2. **The calculator's default state is subscription mode showing 160,000.** The
   first number a visitor sees for Optimal is always 160,000.
3. **No screen shows 95,000 and 160,000 as two options for the same product** in
   the same visual weight. They are a sequence, not a choice.
4. **The Express card's headline price stays 65,000**, as the owner required.
   Express is a product, not a lead-in.
5. **One credit per plot, once.** The UX architect is right that this is
   unguarded (01, D5). Without the rule, a client can Inspection + Express +
   subscribe and argue for both, and a second plot invites the same argument
   again. State on the page: *one credit, one plot, once.*
6. **Renewal is at 160,000 and the client sees that number before year two.**
   The portal's plan card shows `160,000 ֏ AMD / year · renews 14 September 2027`
   from day one. If the first renewal notice is the first time a client sees
   160,000, we will lose that renewal and deserve to.
7. **Pro-rata refunds are computed on the amount actually paid, not on the list
   price.** Nobody caught this: a client who paid 95,000 for the first year and
   cancels after one visit, refunded on a 160,000 basis, receives 120,000 —
   more than they paid. It must be stated in the Refund Policy and implemented
   in `/portal/billing/cancel/`, and it is the reason the credit must be
   recorded against the subscription as a payment, not as a price change.

---

# 5. Gaps — moments in the journey nobody designed

Ordered by revenue at risk. Items 1–4 are the ones I would fix first; between
them they cover everything that happens after the button is pressed, which is
where the money actually is and which none of the five documents specifies.

**G1 — The call itself. Completely undesigned.**
Five documents specify the form that produces a call and none specifies the
call. Needed, and it is a one-page document, not a project:
the **first sixty seconds** (who is speaking, why we are calling, that nothing is
being sold on this call, the promised 10–15 minutes); the **five things we must
learn** (which cemetery, roughly where, area and monuments, who is in Yerevan,
who else in the family decides); the **five things we must say** (what a full
visit is, that the price is the same for everyone, the three guarantees, the
credit rule, how payment works); and the **one thing we must never do** — quote a
different number from the one the calculator showed them. The calculator
configuration must be visible to the caller in the lead record, or the whole
"one price list" argument dies on the first call.

**G2 — The unknown +374 number. This is a real and large leak.**
A US or French recipient receiving an unannounced call from an unknown Armenian
number at an odd hour will not answer it, and a growing share will have it
silenced by the carrier as suspected fraud. Nobody addressed this. **Fix:
WhatsApp first, always.** The confirmation screen and the confirmation email both
say, verbatim: *"Hayk will write to you on WhatsApp from +374 93 154 108 first,
and call only if you prefer."* The number is then a recognised name, not an
unknown international caller. Then a designed **no-answer ladder**: WhatsApp
message → one call at a time appropriate to their timezone (which we can derive
from the country code, and the form already captures it) → one email with the
written quote → stop. Three touches over five days, then the lead rests.

**G3 — The written quote. The missing artefact of the family decision.**
My own objection map named "I need to ask my brother" as the #1 loss cause, and
then nobody — including me — designed the thing that gets forwarded to the
brother. After the call the client should receive a one-page document: the plot
as described, the plan, the price in AMD with the arithmetic, the credit if any,
the three guarantees, the two named humans with numbers, and the payment
instructions. PDF, brand-set, English/Armenian/Russian. It is the highest-value
missing deliverable in this project and it costs one template.

**G4 — The bank-transfer silence.**
The client wires money from Los Angeles. It arrives in one to five days. During
that window there is no screen, no message and no state anywhere in any of the
five documents. Needed: an `Awaiting payment` state on `/en/pay/thank-you/` and
in the portal (*"We have not seen it yet. International transfers usually take
2–5 working days. Nothing is wrong."*), a **day-3 proactive message** from a
named human, and a **day-7** message with the bank details repeated. The absence
of this is where the first refund request of this company will come from.

**G5 — The account-creation bridge.**
The UX architect flagged it (01, D6) and nobody wrote it: the consultation has no
registration, payment is by transfer, and then a portal exists. The welcome email
with the activation token needs an owner, a template and a spec for what happens
when it is not opened for three days.

**G6 — Renewal. Not designed by anyone, in any document.**
Year two is the entire economics of a subscription business and no one has
specified whether it auto-renews, what notice is given, at what price, or what
the notice looks like. Minimum: auto-renew off or on is an **owner decision**;
a notice at 30 days and at 7 days; the price stated; a one-tap "renew" and an
equally visible "do not renew"; and — because this is memorial care — a rule for
what happens if the payer has died, which connects to the UX architect's
ownership-transfer proposal (01, D7). That proposal is correct and should be
adopted.

**G7 — The guest → client path, deliberately closed, and what replaces it.**
Roughly half of all report opens are guests, and every one of us correctly
forbids any CTA there. That is right and I would not change it — but it means our
largest audience is a dead end by design, and nobody wrote down what we do
instead. The answer is not a button on the report; it is (a) the guest footer's
single plain line saying what MemoryCare is with a `tel:` link, (b) the **owner**
being asked on the call whether there is a second family plot — multi-plot
expansion is why the UX architect's plot-first object model (01, D1) is
commercially correct and should be adopted, and (c) nothing else. Write the
decision down so nobody "optimises" the guest view in month four.

**G8 — Analytics. Not specified anywhere.**
We cannot improve what we do not count, and this site launches with zero traffic
history. A minimum event list, agreed before build: `report_sample_opened`,
`calculator_interacted`, `calculator_ceiling_reached`, `form_started`,
`form_field_error` (by field — this is how we will find the phone-field failures),
`consultation_submitted`, `call_connected`, `quote_sent`, `payment_confirmed`,
`portal_first_login`, `report_shared`, `guest_report_opened`. Plus the two
timings I asked for in 04 A7: payment→first report, and first login→first report.

**G9 — Weekend and holiday reality.**
"Within one working day" is promised on six surfaces. Nobody defined what a
Friday-night submission from Glendale means, nor Armenian public holidays.
Either the confirmation computes and states the actual day ("Hayk will write to
you on Monday"), or the promise breaks in its first week.

**G10 — The report SLA.**
The writer flagged `{REPORT_SLA}` as unknown. It appears in the portal
first-entry screen, in the postponement copy and in the guarantee. It is an
operations decision and it blocks four strings.

**G11 — Third-party consent for the Yerevan local contact.**
The UX architect raised it (01, D10) and it is the only genuine legal exposure in
the design: we will message a 72-year-old who never contacted us. His checkbox is
the minimum. Needs the same five-minute legal read as C9.

---

# 6. Ranking — what protects a completed request

The convergence step will have to cut something. This is the order in which
things may be cut, worst first to cut. Ranked by measured contribution to a
**completed consultation request** and, below the line, to a **completed
payment**.

## Tier 1 — cutting or weakening these directly costs requests

| # | Screen / block | Why it ranks here |
|---|---|---|
| 1 | **Consultation form** (3 fields, international phone, in-place confirmation, failure fallback to WhatsApp) | It *is* the conversion. Every other item on this list only delivers traffic to it. A rejected US phone number is a client lost silently and permanently. |
| 2 | **Hero: eyebrow, H1, subhead, CTA, cropped proof card** | The eight seconds that decide whether anything below is read. |
| 3 | **Sample report — the real, explorable component** | The product demo. Opening it is the micro-conversion that best predicts a request. Ranked above pricing because a person who has not seen the proof does not care what it costs. |
| 4 | **Guarantees block** (three items, named, numeric, with the honest limit) | Our entire substitute for reviews. The panel confirmed it is what closes the sale. Must appear on Home, Pricing and its own page. |
| 5 | **The two bands on Pricing + the "one price list" sentence** | Structure carries more weight than any copy here; the sentence is the highest-leverage line on the site for the diaspora. |
| 6 | **Calculator** | Turns the sentence in #5 from a claim into a demonstration. Also the only place the 95,000 lives outside the pricing text. |
| 7 | **Founders block on Home** (two names, roles, real mobile numbers) | A published founder's mobile outweighs 72 anonymous reviews and costs nothing. Currently on Home only in the UX architect's plan — keep it there. |
| 8 | **Sticky mobile CTA bar + `tel:` everywhere** | For the 55-year-old local buyer the phone *is* the primary CTA. |
| 9 | **Post-submit confirmation** (what happens, when, in their timezone, WhatsApp fallback, both numbers) | Prevents the duplicate submission and the "nobody will answer at 1 a.m." abandonment. |

## Tier 2 — cutting these costs payments rather than requests

| # | Screen / block | Why |
|---|---|---|
| 10 | **The call script and WhatsApp-first rule (G1, G2)** | Requests we do not convert are requests we did not need. Cheapest fix in this document. |
| 11 | **The written quote (G3)** | The artefact of the family decision. |
| 12 | **Bank-transfer path + `Awaiting payment` states (G4)** | Every first client passes through it. |
| 13 | **Credit block and the 95,000 worked example** | Removes "why pay a year up front" and de-risks the ladder from both ends. |
| 14 | **Portal first-entry screen** (dated schedule, progress rail, report preview, two humans, no upsell) | The highest-risk two weeks in the product; where refund requests are born. |
| 15 | **Payment reality copy** (transfer now, cards not live, no date promised) | Honesty here prevents an abandoned checkout at the last step. |
| 16 | **Report screen + share sheet + guest view** | Produces the forwarding that is our only organic growth. |

## Tier 3 — real value, but survivable if something must give

17 Family Circle marketing page (the portal feature ships regardless) ·
18 How it works page · 19 Home FAQ · 20 About page (bank requirement — cuttable
in *depth*, not in existence) · 21 Method/equipment block · 22 Bad-news screens
(week-one necessity, but week one, not launch day) · 23 Contacts page ·
24 Cancellation self-serve flow (bank requirement; can ship as a two-step) ·
25 Legal pages (mandatory for acquiring, invisible to conversion).

## What may never be cut regardless of position

- Contacts in every footer, all four legal links, prices in AMD with `֏` **and**
  the letters — bank conditions, and without them card acquiring never opens.
- No CTA, no price and no upsell on the guest report view, and no photograph in
  a link preview.
- No invented testimonial, count, or year.
- The terracotta error colour — the owner's ruling, and it is a payment
  mechanism, not a decoration.

---

# 7. What I need the owner to decide personally

1. **Auto-renew: on or off** — and the renewal notice schedule (G6). Nothing in
   year two exists without this.
2. **Pro-rata basis: by visits consumed or by days elapsed** (01, D1) — and
   confirmation that the basis is the amount **actually paid**, not the list
   price (§4.3.7).
3. **One credit per plot, once** — to be written into `DECISIONS.md` as the
   guard on the 95,000.
4. **"Within one working day"** — confirmed as achievable by the CEO, including
   Fridays and Armenian public holidays, or softened before launch (G9).
5. **Report SLA** in hours (G10).
6. **A five-minute legal read** on two points: the consent statement replacing
   the checkbox (C9), and messaging the Yerevan local contact who never
   contacted us (G11).
7. **Legal address and registration number** — still the oldest open item and
   now on the critical path for the bank package.

