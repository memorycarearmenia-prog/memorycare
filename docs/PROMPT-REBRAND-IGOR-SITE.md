# Rebrand the MemoryCare site — additive only

You are rebranding a live, working site. It functions. People built it.
Your task is to make it look and read like the company it belongs to,
**without taking anything away.**

This is not a redesign brief that lets you start over. It is a rebrand
under hard constraints, and the constraints come from the owner.

---

## 0. The owner's constraints — these are law

1. **Nothing may be removed from the functionality.**
2. **Functionality may be added.**
3. **No page may be removed.**
4. **Pages may be added.**
5. **Work exclusively in the brand colours.** No colour outside §2.
6. **Fill everything with real content**, using every available source of
   information about the project. No placeholder text anywhere.
7. **Ask the owner whenever something is unclear.** Do not guess, do not
   fill a gap with a plausible invention, and do not silently pick one
   reading of an ambiguous instruction. §9 lists the questions you should
   expect to have.

If any instruction elsewhere in this document appears to conflict with
these seven, these seven win — **except** where §1 applies, and §1 exists
because the owner's own instruction 6 requires it.

---

## 1. The one carve-out, and it is not a licence

Constraint 1 protects **functionality**. Constraint 3 protects **pages**.
Neither protects **false statements**, and constraint 6 requires real
content, which by definition excludes invented content.

The live site currently carries:

- Four claimed proof figures on the home page — 150,000 customers, 55+
  services, 250,000+ graves serviced, 15 years of experience. **The
  company was registered in 2026 and has zero paying customers.** Every
  one of these is false.
- Three testimonials with photographs, five-star graphics and Lorem Ipsum
  quotes. The photographs are of real public figures under invented names.
- A partners carousel of four empty placeholder tiles.
- `40,000 ֏` for a repeat product. That price was withdrawn by the owner
  on 26.08.2026 and the product it names no longer exists.
- Lorem Ipsum as the English home page `h1` — "WHAT IS LOREM IPSUM?" —
  and the same Lorem Ipsum *translated* into Armenian and Russian.

**The components stay. The false content does not.** A testimonial
carousel is functionality; a fabricated testimonial is a lie. A statistics
band is functionality; an invented number is a lie.

So for each of these you do **one** of the following, and you propose
which and get it approved before building:

- **Repurpose the component with true content** — e.g. the statistics band
  becomes the published visit protocol, which has real numbers: eight
  photographs, four angles before and the same four after, two videos, one
  GPS point. Same component, same layout weight, true.
- **Keep the component and populate it from a real source** where one
  exists.
- **Keep the component in the codebase, unrendered, behind a flag**, with a
  written note saying what real data would populate it and when.

**You may not simply delete them, and you may not leave them as they are.**
This is the single most important judgement in the task, and §9 requires
you to raise it before you start.

---

## 2. Brand — the only palette permitted

From the brandbook of 31.08.2026.

| Name | Hex |
|---|---|
| Dark Olive | `#212212` |
| Olive | `#7C8654` |
| Nude | `#EFE5D5` |
| Ivory white | `#F3F0E9` |
| Sky blue | `#A4D6E8` |

Plus exactly two interface values that are not in the brandbook and exist
for measured reasons:

| Name | Hex | Why |
|---|---|---|
| Deep Olive | `#575E3B` | Links and accent text on light. Nothing in the brandbook can mark a link apart from body text. |
| Error | `#8C3A2E` | Validation only. |

**No other colour appears anywhere.** Not a grey, not a hover tint you
liked, not a success green, not a shadow that is really a blue. If you
need a state you do not have, derive it from a listed value by changing
lightness only — hue and saturation held — and write down the rule and the
resulting measured contrast.

⚠️ Sky blue is **contested**: the brandbook's colour page prints
`#D4ECF9`, every delivered vector and export paints `#A4D6E8`. Use
`#A4D6E8` and make the swap a single token, greppable. Do not resolve it
yourself.

### 2.1 Measured contrast — facts, not preferences

| Pair | Ratio | |
|---|---|---|
| Dark Olive on Nude | 12.93 | pass |
| Dark Olive on Ivory | 14.17 | pass |
| Nude / Ivory on Dark Olive | 12.93 / 14.17 | pass |
| Sky blue on Dark Olive | 10.26 | pass |
| Deep Olive on Nude / Ivory | 5.49 / 6.01 | pass |
| Error on Nude / Ivory | 6.10 / 6.69 | pass |
| **Olive on Nude / Ivory / Dark Olive** | **3.12 / 3.42 / 4.14** | **fails as text** |
| **Sky blue on Nude / Ivory** | **1.26 / 1.38** | **invisible** |
| **Deep Olive on Dark Olive** | **2.36** | **never** |
| **Error on Dark Olive** | **2.12** | **invisible** |

Four rules follow and none is negotiable:

1. **Olive never carries text and never receives text.** Fills, rules,
   dividers, decorative panels, the petal bullet.
2. **Sky blue is a dark-ground colour.** On light it may only be a tint
   fill — a chip ground, the seal disc — never type.
3. **No form that shows validation errors may sit inside a dark band.**
4. **Nude is the page ground; Ivory is the objects on it** — cards, the
   report sheet, inputs, the header bar.

Every contrast figure you report must be **computed by you from the hex
values**, not copied. An asserted ratio is a defect.

### 2.2 Type

Display **Ghea Mariam**. Text **Montserrat**. Armenian **Montserrat Arm** —
a separate family, not a subset; name it explicitly in the stack.
Self-host all three.

Floors: body never below 16px; no informational text below 14px anywhere;
uppercase chips, badges and eyebrows never below 14px; every input 16px.
Tabular lining figures wherever a number can change. Opacity is banned for
text — secondary text is its own token.

**The dram sign is a trap and it is already broken on the live site.**
֏ (U+058F) is in neither Ghea Mariam nor Montserrat — verified against
Source Serif 4, Montserrat, Noto Sans and Noto Serif, absent from all
four. The browser silently falls back to whatever system face has it,
which is why the price on the site today renders the sign at a different
weight and size from the digits beside it. **Give it its own element and
its own font stack, scoped `unicode-range: U+058F` and nothing else.** A
face that actually contains the glyph has not yet been sourced — say so
rather than naming one you have not tested.

### 2.3 The mark

Two open hands in Nude cradling a five-petal forget-me-not in Olive, its
centre a woven interlaced medallion in Sky blue. The wordmark is
**single-colour Olive**. The tagline is Sky blue, uppercase, wide
tracking, **no full stop**. Vectors are supplied.

Two facts about the artwork: the medallion is 29 filled paths with no
stroke attribute, so it cannot be drawn with `stroke-dasharray`; and it
stops being legible below **48px**.

The logo currently on the site is the retired 27.08 mark. Replace it.

---

## 3. Every existing page stays — here is what each becomes

Nothing here is deleted. Four of these routes currently serve a 404
template while returning HTTP 200; under constraint 3 they are not
removed, they are **filled**, which is also what constraint 6 requires.

| Route | Today | What it becomes |
|---|---|---|
| `home` | Lorem Ipsum `h1`, fabricated stats and testimonials, a cloud-gradient hero | The real offer, the report as evidence, the five products, the trust material. §4 |
| `contact` | exists | Real contacts — named people, dialable numbers, the legal entity, the address |
| `login` | exists | Rebranded, keyboard-complete, real error copy |
| `register` | exists | **Stays.** Rebranded, and given the consent control it currently lacks |
| `reset` | exists | Rebranded, with an honest description of what the user will receive |
| `history` | 404 template, HTTP 200 | Real: the company's actual short history — registered 2026, the pilot, what has and has not happened yet |
| `mission` | 404 template, HTTP 200 | Real: the evidentiary standard the company sells, stated plainly |
| `values` | 404 template, HTTP 200 | Real: what is done on a visit and, as importantly, what is **not** done |
| `news` | 404 template, HTTP 200 | Real: an honest, dated log — company registration, equipment, the pilot. If there is not enough to fill it, say so and propose the smallest honest version |
| `notfound` | exists | A real 404, and it must return **HTTP 404** |
| `account-index` | exists | The portal landing, rebranded, with a designed empty state |
| `packages-add-1` | exists | The purchase flow, rebranded, carrying the corrected five-product line-up |
| `root` | exists | Locale redirect, verified |

Every route must return the status it renders. A 404 page served with 200
is a defect regardless of how it looks.

---

## 4. What to add

Adding is permitted and these are needed.

### 4.1 Six pages the bank requires

Card acceptance is blocked until these exist, and the reviewing bank
cannot begin until the pages are live — every week they are missing is
added to the review, not spent in parallel with it.

**About · a full five-product tariffs page · legal restrictions · an
English privacy policy · a refund and cancellation policy · service
delivery terms.**

Two further conditions are half-met and are one-line fixes: the footer
prints a placeholder address and phone and carries **no registration
number**, and the AMD prices carry **no exchange-rate note** anywhere.

### 4.2 Product and pricing structures

The line-up is five products, decided by the owner 26.08.2026. **All
visits are full visits — the light/heavy distinction was rejected and the
words must not survive anywhere, including as enum values or column names
in the database.**

| Product | Composition | Price |
|---|---|---|
| Զննում — inspection | One orientation visit: locate the plot, full written inventory, photo and video of the condition, a list of the work needed, a quote for minor repair. **No cleaning.** | 20,000 ֏ |
| Էքսպրես — single visit | One full visit: deep cleaning of the whole plot and every monument — steam, professional neutral-pH chemistry, wet/dry vacuum. **No high-pressure washing on a monument.** | 65,000 ֏ |
| Օպտիմալ — flagship | Annual: **4 full visits, one in each season** | 160,000 ֏ / year |
| Մաքսիմում | Annual: **6 full visits** | 200,000 ֏ / year |
| Հատուկ խնամք — special | Non-standard: more visits, a plot over 16 m², more than two monuments, several family plots. Always begins with an inspection. | calculator / consultation |

Credits: the inspection is credited **only on signing an annual
subscription**, within 60 days, and never into a single visit. A single
visit is credited in full into a subscription within 60 days. **One credit
only** — either one or the other, never both; a client who bought both
gets the larger credited.

**There is no discounted repeat single visit.** Always 65,000. Design the
system so the withdrawn 40,000 cannot return: no field for it in the
model, and a build-time check against the literal.

**Add a price calculator** to the tariffs page — an owner decision, not an
option. An open formula, two sliders, the same price for everyone, visible
before anyone has to call. Price is flat within a standard envelope of
**16 m² and two monuments**; beyond it: +10,000 ֏/year per m² over 16 and
+30,000 ֏/year per monument over two (for a single visit: +2,500 and
+7,500 per visit). Sliders cap at 100 m² and 10 monuments. The internal
logic is worth publishing because it *is* the argument: 160,000 ÷ 16 m² =
exactly 10,000 ֏ per m² per year, so an added metre costs precisely what
an included one costs.

### 4.3 Content structures worth adding

- **The visit report as a page.** This is the product; the site currently
  treats it as a feature. A real sample report a stranger can open.
- **The published protocol**, with its numbers.
- **Family Circle** — relatives get their own sub-account by invite, see
  every report, can order one-off services.
- **An honesty panel.** "We started in 2026. We have no reviews to show
  you and we will not borrow anyone else's." The admission is an asset,
  and an incumbent structurally cannot say it.

---

## 5. Content — real, from real sources

Constraint 6. Use every available source: the business archive, the tariff
decision of 26.08, the field protocol, the pilot checklist, the lawyer's
notes, the competitive research, and the real contact details. Quote
rather than paraphrase where a fact is precise.

Facts you may state because they are true today:

- A visit is not closed until the report contains **eight photographs —
  four angles before and the same four after — two videos, and one GPS
  point recorded at the plot on the day.**
- GPS as **verification**, never as location: it answers *was the crew
  standing there*, not *where is the grave*.
- The winter visit runs in a weather window rather than on a date, because
  the protocol limit is temperature. **Four visits are guaranteed
  regardless**: if no window opens, the visit is added to spring. That is a
  contract term, not a failure.
- The company was registered in 2026 and the pilot is its first client
  work.

Things you must never write, in any language: `the only` · `the first` ·
`nobody else` · `unlike others` · `unique` · `since 20xx`. **No competitor
is named or alluded to**, including in an FAQ. An established competitor
has sold four visits a year with photographs in this city since about
2015; a claim to be first is falsifiable in one search by exactly the
person you most need to convince.

**Write each language natively.** Do not write English and translate it.
Armenian and Russian that read as translations of an American landing page
are a failure, and it is the most likely one.

---

## 6. Premium is a discipline, not a decoration

The register is **light premium minimalism**: generous white space, large
type, restrained editorial elegance, warm but professional. Explicitly
**not** funeral cliché — no dominant black, no crosses, no gothic
lettering, no candles. Not guilt, not sentimentality, not corporate
coldness.

Two rules that carry most of the character:

- **No text is ever set over a photograph.** Labels are typographic and
  sit outside the frame. This also structurally removes a contrast failure
  the current build has.
- **No photograph of a plot, a monument or a report bleeds to the edge of
  the viewport.** Each sits framed with visible ground on all four sides.
  Full-bleed is the register of advertising; an inset frame is the
  register of something being held and shown to you.

**Real photographs do not exist yet** — the shoot has not happened. Ship
**nothing that pretends to be a photograph**. No stock, no grey rectangles
labelled "image". Build the page so it works without them and improves
when they arrive.

Motion is calm and small: ~120ms for state changes, ~220ms for entrances,
a 320ms ceiling, transform and opacity only, a complete
`prefers-reduced-motion` path, and nothing that moves on its own. **One
exception, deliberate:** the calculator recomputes visibly as the sliders
move, because arithmetic in the open is the transparency argument made
visible. It is the only number on the site permitted to change on screen.

---

## 7. Defects to fix while you are in there

Confirmed by audit. None of these removes functionality.

1. **The navigation is unopenable between 1024 and 1300px** — the script
   treats the layout as mobile below 1300 while the CSS shows the desktop
   menu, so clicking a parent item toggles a class instead of navigating.
   That band is the most common laptop width there is. One breakpoint set,
   shared by CSS and script.
2. **`user-scalable=no`** disables pinch-zoom at every width. Remove it.
3. **Submenus open on hover only**, with no keyboard or click path. Add
   `aria-expanded`, click, Enter and Escape.
4. **The mobile menu omits the language switcher.**
5. **Focus states are removed and not replaced.** Add real ones.
6. **Four routes render a 404 template with HTTP 200.**
7. **Body text runs at 15px in 225 places, 14px in 132, and 12px in one.**
8. **The footer** prints a placeholder address and phone and no
   registration number.

---

## 8. Deliverables

1. The rebranded site, every existing route plus the added ones.
2. A **token layer** — CSS custom properties and a generated machine-
   readable file from one source, so they cannot drift.
3. A **computed contrast table** covering every text-on-background pair
   the build actually produces.
4. A **route table**: every route, its HTTP status, what changed, and what
   was added.
5. A **content source map**: every non-trivial string, and the document it
   came from.
6. **`QUESTIONS.md`** — everything you asked the owner and what was
   decided.
7. **`NOT-GIVEN.md`** — every gap you refused to fill, and who must close
   it.

---

## 9. Ask the owner about these before you start

Constraint 7 is an instruction, not a courtesy. At minimum, raise:

1. **The fabricated content.** §1. For each of the four items — the
   statistics band, the testimonials, the partners strip, the withdrawn
   40,000 price — propose repurpose, populate, or flag-off, and get each
   approved. Do not begin until this is settled.
2. **The registered spelling of the legal entity.** Three project sources
   give two answers — `Memory Care LLC` and `MemoryCare LLC`. Whatever the
   site prints must match the certificate exactly, and nobody has opened
   it. Also ask for the **registration number**, which appears in no
   project document, and confirmation of the **legal address**.
3. **How many days after payment the first visit happens.** Required by
   the bank and decided nowhere. It becomes contractual on publication.
4. **The boundary of "minor repair."** Construction work needs municipal
   permission. Until the boundary exists in writing, the site may not name
   a single repair that will be performed.
5. **Product names in English and Russian.** Four of five have never been
   written down.
6. **What the site may say about the client portal**, which is not live
   yet. The first promise a real customer meets must not be a broken one.
7. **Whether any guarantee may be published.** A guarantee with no
   liability figure behind it creates no trust; the insurance is open.
8. **Sky blue**, if the designer has ruled since this brief was written.

Ask early, ask in one batch where you can, and never substitute a guess
for an answer.

---

## 10. How this will be judged

1. **Was anything removed?** A missing page or a lost feature fails the
   task outright. The one carve-out in §1 must have been approved in
   writing first.
2. **Is every colour on the page in §2?** One stray hex fails.
3. **Is every claim true today?** Not "true after the pilot" — today.
4. **Is every contrast ratio computed rather than asserted?**
5. **Does every route return the status it renders?**
6. **Does the site work with no photographs at all?**
7. **Were the §9 questions asked before building, not after?**
