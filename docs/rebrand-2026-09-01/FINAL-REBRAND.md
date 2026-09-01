# FINAL — the converged rebrand

**01.09.2026. Design lead.** This document has the highest precedence in
the rebrand. Where it differs from any of the five proposals, this one
governs. Where it is silent, the proposal named in §3 governs.

This is not a digest of five documents and it is not a compromise between
them. It is one variant. Where two specialists disagreed I ruled for one
and said why; where both were wrong I said so.

---

## 1. The five, and how they were judged

The strategist's §8 supplied the ranking test, and I applied it as
written rather than inventing my own, because a test authored before the
proposals were read is worth more than one authored after.

| Test | Result |
|---|---|
| 1 · Truth gate (disqualifying) | All five pass **after correction**. Three were written against a superseded price table that I circulated; two revised in place, one was rewritten. No proposal now asserts anything untrue as of today. |
| 2 · Checkability of the first screen | UX wins outright: the fold ends on a report sheet cropped at its metadata strip — a date, a cemetery, a plot number and a GPS chip. |
| 3 · Does the report outweigh everything? | UX moves it to section 2; art direction makes it the heaviest object on the page at 720px wide. Both, independently. Adopted. |
| 4 · Swap test — specificity | Art direction passes hardest: the cradle rule, the year rail and the seal could not belong to a dental practice. Motion passes: nothing on this site moves on its own. |
| 5 · Distance to the form | UX puts the form **on** the page as section 11, not behind a button. Two taps from anywhere. |
| 6 · Measured, not asserted | System recomputed every ratio from the hexes and found two defects in our own prior system. This is the proposal I trust most. |
| 7 · Degradation without photography | Art direction ships **zero images pretending to be photographs**. The page works today, before the September shoot. This is the single most important pass on the list. |
| 8 · Commercial completeness | **Only the strategist raised it, and it is the finding with revenue attached.** See §4.1. |
| 9 · Cost of a token change | System makes the Sky-blue swap one line plus a CI grep. |

**No proposal is discarded.** Each owns its domain; the conflicts are
ruled below.

---

## 2. The one sentence

> **This company will show me, in evidence I can check and forward to my
> family, exactly what was done at our grave and when — on a schedule I do
> not have to manage.**

Adopted verbatim from the strategist. The verb is *show*, the object is
*evidence*, the qualifier is *checkable*. Every element on the site serves
that sentence or it is decoration.

We are not selling grave care. Anyone with a brush and a car can cut
grass, and an incumbent has been selling four visits a year with
photographs since about 2015. We are selling an evidentiary standard that
happens to include grave care.

**The corrected pricing makes this reframe mandatory rather than
optional.** Under the superseded table the argument could have been visit
volume — six and nine against a local four. Optimal is now four full
visits, which is the count the incumbent already advertises. *The volume
differentiator does not exist.* What remains is what a visit is and what
arrives after it. The 26.08 rejection of the light/heavy split is
therefore not a simplification we absorb, it is the positioning asset we
lead with: **every visit is a full visit — the whole plot and every
monument, cleaned, not a look around.**

Never, in any language: `the only` · `the first` · `nobody else` ·
`unlike others` · `unique` · `since 20xx`. No competitor is ever named,
including in an FAQ answer.

---

## 2b. Scope — desktop web only, ruled by the owner 01.09

The deliverable is the **desktop web version**. No mobile screens, no 360
breakpoint, no mobile type ramp, no mobile-specific UX.

What this removes: `PROPOSAL-ux.md` §8 in full (mobile-first specifics,
thumb reach, the sticky-CTA question, what is deliberately different at
360); the 360 column of every table in `PROPOSAL-art-direction.md` §2.3
and §5; the mobile half of the system's responsive architecture; and the
mobile ramp already built in Figma, now marked out of scope rather than
deleted.

What survives unchanged, because none of it was ever about screen width:
every contrast ratio and the four structural colour rules; the truth
constraints; the pricing; the protocol numbers; the whole content round;
and the six routes the bank requires.

Two floors survive too, and they are not mobile concerns even though they
were written next to them: **body text never below 16px** and **no
informational text below 14px anywhere**. The verification rail carries
the actual proof for a 40–60 audience; that is a legibility rule, not a
breakpoint rule.

Recorded plainly: `CLAUDE.md` states diaspora traffic is majority mobile
and the 31.08 audit captured five widths. Narrowing to desktop is the
owner's call and is deliberate.

## 3. Domain ownership

| Domain | Governing document |
|---|---|
| Positioning, claims, tone, what may be said | `PROPOSAL-strategy.md` |
| Visual language, type scale, colour application, photography, grid, report sheet | `PROPOSAL-art-direction.md` |
| IA, page order, flows, tariff presentation, string slots | `PROPOSAL-ux.md` |
| Tokens, components, fonts, a11y, performance, CSS architecture | `PROPOSAL-system.md` |
| Everything that moves | `PROPOSAL-motion.md` |

---

## 4. Rulings on conflicts and open questions

### 4.1 The bank conditions are in scope — and they reorder the work

**Ruled: adopted, and it changes the plan.** The strategist is the only
one who noticed that the brief's route list — mine — omits six of
Ameriabank's eight site conditions. A flawless rebrand of the routes I
listed still cannot be submitted to the bank, and the bank sits on the
critical path to card revenue: site ready → bank review → acquiring,
expected early October. The bank cannot begin reviewing pages that do not
exist, so every week not spent on those six is added to the review.

The trade is close to cost-neutral and I am taking it: **delete
`history`, `mission`, `values` and `news` rather than design them** — all
four serve the 404 template under HTTP 200 today, so nothing is lost —
and spend that work on About, a full five-product tariffs route, legal
restrictions, an English privacy policy, a refund policy and
service-delivery terms.

Two conditions are half-covered and both are one-line fixes nobody had
assigned: the footer exists but prints `0000, Yerevan` and
`+374 10-00-00-00` with no registration number, and the AMD prices carry
no FX note anywhere.

### 4.2 The surcharge question — resolved from source, not by vote

The strategist left this open and deliberately avoided writing "flat
whatever the size of the plot". Right instinct; here is the answer, from
`TARIFF-REDESIGN-2026-08-26.md` §2.

Price is flat **within a standard envelope — up to 16 m² and up to two
monuments** — and beyond it there is a published formula, identical for
everyone:

| | Standard | Annual subscription | One-off Express |
|---|---|---|---|
| Area | ≤ 16 m² | +10,000 ֏ / year per m² over 16 | +2,500 ֏ / visit per m² |
| Monuments | ≤ 2 | +30,000 ֏ / year per monument over 2 | +7,500 ֏ / visit per monument |

Sliders cap at 100 m² and 10 monuments; beyond that, consultation, via a
Զննում. Surcharges are identical for Optimal and Maximum. The internal
logic is worth publishing because it is the argument: **160,000 ÷ 16 m² =
exactly 10,000 ֏ per m² per year — an added metre costs precisely what an
included one costs.** The one-off surcharge is the annual figure ÷ 4.
Զննում alone is flat at any size.

So the correct sentence is not "flat whatever the size" but **"the same
formula for everyone, published, and you can see your price before you
call."** That is a stronger claim, and it is true.

### 4.3 The calculator is the site's best motion opportunity

**Ruled for the strategist over my own instinct.** Motion's philosophy —
calm, small, confirmation not expression — is right, and I adopt it whole.
But the strategist landed a better argument than either of us had: the
calculator recomputing **in the open** *is* the transparency argument made
visible. A number that updates as a slider moves, with the arithmetic
shown rather than asserted, is the one place on this site where movement
carries meaning instead of decorating it.

The ruling: the calculator's result animates — the numeral tweens, the
arithmetic line re-renders — within motion's own envelope (≤140 ms, easing
inside the unit square, no travel). It is the **only** number on the site
permitted to change on screen, precisely because the site's defining sin
was inventing numbers. Everything else motion refuses stays refused: no
count-ups, no parallax, no scroll-jacking, no animated hero.

### 4.4 Report animation — the line motion drew is correct

`FINAL-SYSTEM` §5.5 forbids all animation on the sample report, which
collided with the commissioned hero moment. Motion resolved it and I
confirm: **the real report, the sample-report page and the guest view
carry zero motion, forever.** The home page's *depiction* of receiving one
is not a report; it may play its 1,620 ms sequence once. A document of
record does not animate. An illustration of what arriving feels like may.

### 4.5 Four cards vs five

Art direction's band table says "four Ivory cards" — written before the
correction reached it. **UX governs**: entry rail for Զննում, a row of
three, the credit block, then Special as a full-width card carrying the
calculator. Any surviving four-card artefact is a defect.

### 4.6 The "How should I compare grave-care services?" FAQ

**Ruled: build it, under the author's own conditions.** They flagged it as
their most contestable idea and attached the right test — every item must
be a question a reasonable buyer would ask unprompted, none reverse-
engineered from a competitor's weakness, and if the copy lead cannot write
it without a sneer, we cut it. I add one condition: **it ships only if we
clear every item on it at the moment of writing.** A checklist we fail is
an own goal.

Under the corrected pricing its first item must be *what is done on one
visit*, not *how many* — the old ordering would have pointed at a tie.

### 4.7 Olive earns exactly one job

The strategist predicted the visual lead would use Olive as text because
it is *the* brand colour. They did not. Art direction and system both
quarantine it independently — system by putting it in a `decor` namespace
defined as "paint that never has a foreground", so the wrong token is a
word that is wrong to type.

The one place Olive does real work is UX's year rail: a 12×12 filled mark
at 3.12 on Nude, clearing the 3:1 non-text floor with almost no margin,
which is why every mark also carries a 1px Deep Olive outline at 5.49 and
the count is printed as a numeral in the same card. Colour is never the
sole carrier. Correct.

### 4.8 Two prior-system defects — fixed, and worth naming

Found by the system engineer, both silent:

- `FINAL-SYSTEM` §3 binds the modal radius to a token §5.3 deletes. Every
  modal would have rendered square and nobody would have known why. Now
  `--mc-radius-overlay: 8px`.
- The input border composites to **3.01** against a 3:1 requirement —
  passing by a rounding artefact, and failing outright at 3.30 on Ivory.
  Replaced with solid `#737060` (3.99 / 4.38).

### 4.9 The medallion cannot be stroke-animated

The delivered `MemoryCare_logo-mark_color.svg` is **29 filled paths with
no `stroke` attribute** — the interlace was drawn as filled outlines, not
centrelines. `stroke-dasharray` makes 29 shapes trace their own
perimeters. Motion's mask-with-growing-stroke technique is adopted; the
designer's geometry is not touched. `docs/logo-animation-prompt.md` is
marked superseded — it animates five rotating rings the current mark does
not have.

### 4.10 Public registration is deleted

**Ruled for UX.** An account before a purchase is an empty room, and
today's register form collects personal data with no consent control.
Portal access arrives with the first order.

---

## 5. The page, settled

Twelve sections. Two dark bands, not three, not one. The hero is Nude —
both the visual lead and the UX lead argued this independently and for the
same reason: a dark hero spends the page's scarcest asset on the one
screen where "not funeral-cliché" is strictest.

| # | Section | Ground | Job |
|---|---|---|---|
| 1 | Hero | Nude | The offer + verification in one screen. Ends on the report sheet cropped at its metadata strip |
| 2 | **The report** | Nude, Ivory sheet | The promise becomes evidence. The heaviest object on the page |
| 3 | How it works | Nude | What happens, in what order |
| 4 | What a visit includes / what we do not do | Nude | Answers "why not ask a cousin" |
| 5 | Tariffs | Nude | Five products, the year rail, the credit block, the calculator |
| 6 | **Family Circle** | **Dark Olive** | The differentiator, full-width dark |
| 7 | Trust & verification | Nude | How each claim above is checked |
| 8 | Honesty panel | Nude, bordered | "We started in 2026. We have no reviews yet." |
| 9 | Founders | Nude | Two named people, dialable numbers |
| 10 | FAQ | Nude | Six items, first open |
| 11 | **Consultation form** | Nude, Ivory sheet | The conversion — the form itself |
| 12 | Footer | **Dark Olive** | Bank requirement, contacts, legal entity, registration number |

Dark bands ≈ 21% of page height; cap 25%. Dark Olive at 12.93 against Nude
is materially heavier than the Anthracite it replaces; past 40% it stops
being an anchor and becomes a funeral.

**The form is on the page because the contrast table forbids it on dark**
(error `#8C3A2E` measures 2.12 on Dark Olive — invisible). UX took that
constraint as the answer rather than routing around it, which is the right
move: a page ending in a button that opens a page containing a form loses
conversions at two doors instead of none.

### The two ideas I would keep if I could keep only two

**The cradle rule.** No photograph of a plot, a monument or a report ever
bleeds to the viewport edge; every one sits framed with visible ground on
all four sides. Full-bleed is the modern default and the reference sites
use it — Airbnb full-bleeds a room because it is selling the room. We are
not selling the grave. The frame is the difference between a listing and
something being held and shown to you. It is also the only place the open
hands survive in the interface, as a rule rather than a drawing.

**The year rail.** Twelve cells, one per month, the same component in every
card. Optimal's four marks land one per season. *"Four full visits, one in
each season"* stops being a claim and becomes a picture. Nothing else on
this site can do that, and it only became possible because the owner
rejected the light/heavy split.

### The best sentence found in the work

UX ran the credit arithmetic under the 26.08 rules and found that **every
route into year one costs the same 160,000 ֏** — entering by a 20,000
inspection, by a 65,000 Express, or by buying the subscription outright.
Hence the credit block heading: **"Starting small costs you nothing."**
That removes the only real objection to the trust ladder, with a sum
rather than with reassurance. It is the kind of claim this brand is
allowed to make, because it is arithmetic.

---

## 6. Blocked — these need a person, not a designer

1. **The flowers / candle option** is an explicit owner instruction for the
   tariffs page and **has no price in any source.** Designable, not
   sellable. → Davit.
2. **Guarantee #2 needs a liability figure** from the lawyer. A guarantee
   without a cost attached creates no trust, and `PROJECT-MEMORY-FULL.md`
   §9 still shows liability and worker insurance open. Publish each
   guarantee only once it is actually bound. → lawyer.
3. **What does the site claim about a portal that is not live?** Nobody has
   ruled. The first promise a pilot customer meets must not be a broken
   one. → Hayk + Igor.
4. **Sky blue `#A4D6E8` vs the brandbook's printed `#D4ECF9`.** → Mariam.
   Built as a one-token swap either way.
5. **A favicon crop of the medallion** at 16 / 32 / 180 / 512 — the one
   asset art direction asks Mariam for.
6. **EN and RU product names must actually be written.** Four of five
   Armenian forms are still `[OPEN]` in the prior art and attached to a
   superseded price list.
7. **Downstream documents still on the old line-up:** the financial model
   v6.0, the client contract, Igor's platform spec, and `FINAL-CONTENT.md`,
   which carries a third variant. Not a design task.

---

## 7. Next

Build the converged design in Figma against these rulings, then run the
content team over the same ground.
