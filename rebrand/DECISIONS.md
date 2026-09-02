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
