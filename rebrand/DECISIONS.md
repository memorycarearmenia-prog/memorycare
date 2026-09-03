# Owner decisions — 02.09.2026

Taken by Hayk during the build. Binding on everyone.

## 1. Product names — descriptive, not cognate

| | Inspection | One visit | 4/yr | 6/yr | Non-standard |
|---|---|---|---|---|---|
| **EN** | Inspection | Single visit | Four visits a year | Six visits a year | By arrangement |
| **RU** | Осмотр | Разовый визит | Сезонный уход | Расширенный уход | Особый уход |
| **AM** | Զննում | Էքսպրես | Օպտիմալ | Մաքսիմում | Հատուկ խնամք |

The Russian and English writers independently rejected the cognates with
the same two arguments: *Express* promises speed, which contradicts "every
visit is a full visit"; and *Optimal / Maximum* imply a quality ladder that
stopped existing when the owner rejected the light/heavy split. The count
**is** the pitch.

**The Armenian deliberately diverges**, and the owner has taken that
knowingly. The Armenian writer's objection — that `Էքսպրես խնամք` reads as
*the quick version of the care* — is met by never letting `Էքսպրես` appear
without `մեկ լիարժեք այց` on the line beneath it.

⚠️ The contract, Igor's platform spec and the financial model still carry
the old names. Someone must reconcile them.

## 2. The false content — repurposed, not deleted

- **The statistics band survives**, carrying the **published visit
  protocol** instead: eight photographs, four angles before and the same
  four after, two videos, one GPS point recorded at the plot on the day.
  Same component, same weight on the page, real numbers.
- **The testimonials and the partners strip stay in the codebase behind a
  flag**, not rendered, each with a note saying what real data fills it
  and when. Reversible; deletion is not, and after the pilot there will be
  real testimonials.
- **Two conditions on the flag:** the note must name the real data source,
  and a build check must make it impossible to ship the flag enabled with
  placeholder content. A flagged-off component someone switches on with
  dummy data is how the current site got here.

## 3. Scope — desktop plus correct reflow

Design target 1440. The page must reflow correctly to 360 **with no
horizontal scroll**. This is not a mobile design: no second type ramp, no
mobile-specific components, no separate section order.

The reason is a defect, not a preference. Two measured failures live only
at narrow widths: on `acct-packages` the Pay button sits at `left: 371px`
in a 360px viewport with the document 452px wide, and a table row overlaps
itself. Removing horizontal scroll is a fix.

This widens the earlier desktop-only ruling of 01.09.

## 4. The comparison FAQ — written, held

Written in full, all six items **including** the monument-damage question,
and marked `[HELD]`. It ships the day the lawyer binds a liability figure.

The English writer proposed shipping five by cutting the damage item. The
Russian writer objected that cutting the one item we fail is exactly the
reverse-engineering the rule forbids. The owner sided with the stricter
reading.

---

## 03.09.2026 — nineteen answers from the owner

Fifteen open questions were put to the owner one at a time and answered; four
more surfaced while implementing those and were answered too. Every one is in
the build.

| Question | Ruling |
|---|---|
| Card schemes | Visa, Mastercard, Arca — plus Google Pay and Apple Pay as a **separate wallet group**, because they are payment methods, not schemes. |
| Service delivery term | Զննում **within one working week** of payment; every other service **within 14 working days**, unless another date is agreed. |
| Minor repair | **The boundary is the stone.** Fence, slab, soil, metal — yes. Anything on the monument — no, and not subcontracted either. |
| Guarantee 2 | **Restoration at our cost, no ceiling.** We answer for damage we cause, not for the condition photographed beforehand. |
| Flowers and candle | **On request, at cost, receipt shown.** Not a price-list line, not in the calculator. |
| Order form `p`/`f` | Replaced by **one field, `visits`**. The server must derive the count from the product and reject a mismatch. |
| Data hosting | **Armenia.** A written data-processing agreement with Igor exists. No transfer outside the country. |
| Sky blue | **`#A4D6E8`** — the value the artwork physically contains. Mariam corrects the colour page. The dispute is closed. |
| Armenian text face | **Noto Sans Armenian, permanently.** Not a stand-in. "Montserrat Arm" does not exist. |
| Favicon | Built from our own vector. Full mark at 180 and 512; **the forget-me-not alone at 16 and 32** — the hands and flower merge into a blob at that size. |
| Armenian in Figma | **Only in the HTML build and its screenshots.** Figma renders Armenian and ֏ as empty space, silently. |
| Bank form e-mail | Owner updates it to `info@memorycare.am`. |
| Registry website field | Owner enters `memorycare.am` before submitting to the bank. |
| Cancelling a subscription | **Immediate, refund automatic.** No request, no telephone call. |
| Sample report | **Schematic, no photographs**, until the September pilot shoot. No change needed — the page was already built that way. |
| Cancelling a one-off | **Full refund up to 24 hours** before the agreed date. |
| Later than 24 hours | Refund **less 10,000 ֏ for the trip**, shown as its own line. |
| Data-request window | **30 days.** |
| Liability wording | Filled from guarantee 2 — the last placeholder the owner could close. |
