# Build a modern design system from the MemoryCare brandbook

You are building the design system for MemoryCare from its brandbook. Not a
theme, not a component folder — a system: tokens with a pipeline, components
with contracts, documentation someone can work from, and the tooling that stops
it rotting.

Read the whole brief, then the brandbook, then start.

---

## 1. What "modern" means here, and what it does not

**It means current platform and practice**, not current fashion:

- Tokens in the W3C DTCG format, one source, multiple generated outputs.
- CSS cascade layers so specificity is a decision and not an accident.
- Container queries for components, media queries only for page structure —
  a card should respond to the space it is in, not to the size of the window.
- Logical properties throughout: `inline-start`, `block-end`, `padding-inline`.
  Not because this product needs right-to-left, but because the same discipline
  is what makes a component survive three scripts.
- Fluid type and space with `clamp()`, bounded at both ends, never unbounded.
- `:has()`, `:focus-visible`, `@supports`, `color-mix()` where they remove a
  variant rather than add cleverness.
- Subset variable fonts, self-hosted, with `unicode-range` per script and
  `size-adjust` so a fallback does not shift the layout.
- WCAG 2.2, not 2.1: target size, focus not obscured, dragging alternatives,
  consistent help, redundant entry.
- Every interactive pattern built to the ARIA Authoring Practices, with the
  native element first and ARIA only where the platform has no answer.
- Motion, colour and data preferences all honoured: `prefers-reduced-motion`,
  `prefers-reduced-data`, `prefers-contrast`.
- Versioned releases with a changelog, and a deprecation path that is not
  "we deleted it".

**It does not mean** glassmorphism, gradient meshes, oversized rounded cards,
pill buttons, floating shadows, blurred translucency, neon accents, a purple
hero, an animated blob, or a hero that occupies two screens. None of that is
modern; it is 2021, and it is wrong for this brand specifically.

**The brand's own register is care and precision.** This is a company that
cleans and photographs family graves for people who cannot travel. A system that
looks like a fintech startup has failed regardless of how current its CSS is.

---

## 2. The brandbook is the source — read it before you write a token

`brand/MemoryCare_brandbook.pdf` and `brand/BRAND-NOTES.md`.

It gives you four colours with CMYK, two typefaces, and the mark in its
lock-ups. Everything visual in the system derives from those, and where the
brandbook is silent you extend it in its own logic rather than importing a
convention from elsewhere.

### Colour — what the brandbook gives, and the one thing it does not

| Name | HEX | CMYK |
|---|---|---|
| Olive | `#7C8654` | 52 / 34 / 78 / 12 |
| Nude | `#EFE5D5` | 6 / 8 / 15 / 0 |
| Ivory white | `#F3F0E9` | 3 / 3 / 7 / 0 |
| Anthracite | `#33373C` | 74 / 64 / 57 / 52 |

Measured, and this is the fact the brandbook does not carry: **Olive fails
contrast on every ground** — 3.12 on Nude, 3.42 on Ivory, 3.08 on Anthracite,
3.42 for Ivory on Olive. It is a decorative colour. It never carries text and
never receives text.

So the system adds a fifth, interface-only value: **Deep Olive `#575E3B`** —
the same hue and saturation, lightness 30% instead of 43%. It measures 5.49 on
Nude, 6.01 on Ivory, 6.01 for Ivory on it. It is a working value adopted by the
owner and pending the designer's own; treat it as one token, easy to replace.

And a sixth, the only functional colour: **error `#8C3A2E`**, for form
validation and payment failure. **There is no success token and no warning
token** — those are expressed with words, glyphs and rule weight. Name the error
token so a sibling cannot be added later.

Two consequences that are architectural, not stylistic:

- **Error red on Anthracite measures 1.57 — invisible.** Therefore a form may
  never sit inside a dark band, and that is enforced by the layout primitive,
  not by a note.
- **Nude and Ivory differ by 1.1** and are indistinguishable side by side. Give
  each one fixed job and write it down: Nude is the page ground, Ivory is
  objects — cards, sheets, forms, bars. Nude below, Ivory above, always with a
  hairline between them.

Shades are yours to derive, but each one that carries text arrives with its
measured pairs. A shade nobody measured is a shade nobody may use for type.

### Typography — a single-weight display face is the interesting constraint

**Gloock Regular** for display. Free, on Google Fonts, and it has **one weight**.
That is not a limitation to work around; it is the thing that will make this
system look considered. Hierarchy comes from size, measure, colour, spacing and
tracking — never from weight, because there is no other weight. Gloock is
rationed to a handful of slots and never set below 24px.

**Gill Sans** for text in the brandbook — commercial Monotype, not licensable
for the web here. Use **Cabin**, a humanist sans in the same tradition, and label
it a substitute everywhere: in the token comment, in the docs, in the README.
Swapping to Gill Sans must remain one token.

**Neither face covers Armenian**, and Armenian is the primary market. The
system needs a companion that carries Armenian, Cyrillic and Latin, declared in
every stack — including the display stack, which is the one people forget.

**The dram sign `֏` (U+058F) is in none of these faces.** Verified by rendering:
it disappears rather than falling back. The currency symbol gets its own element
and its own stack, and `AMD` in words is always available as the default form.

### The mark

Nine vector lock-ups in `brand/svg/`. Two defects to design around: the colour
mark's hands are Ivory and vanish on the Nude ground, so it belongs on
Anthracite or white only; and every SVG sits in a 1080×1080 square with large
padding, so crop to content before shipping. There is no horizontal lock-up —
construct one and document its geometry.

---

## 3. The system's architecture

**Three token layers, enforced structurally.** Primitive holds every literal and
nothing else. Semantic references primitive only. Component references semantic
only. A component that reads a primitive, or writes a hex, fails the lint. Ship
the lint with the system.

**One source, generated outputs.** `tokens.json` in DTCG → CSS custom
properties, a Sass module, a Tailwind preset if anyone wants one, and TypeScript
types. The types should make illegal states unrepresentable: this product has no
"monthly" plan and no "light visit", so those strings should not compile.

**Scopes are classes, never media queries.** A dark section is a class a
designer applies, not something a visitor's operating system decides. In this
product that is not a preference: an OS setting must never repaint a page
containing a photograph of a grave in colours nobody checked. Write that reason
in the file.

**Components own their layout, pages own their composition.** Container queries
inside components, page structure outside them.

**Everything is keyboard-first.** Build the interaction with the native element,
add ARIA only where nothing native exists, and test every component with the
mouse unplugged.

---

## 4. Non-negotiable measurements

- Contrast ≥ 4.5 for text, verified over **rendered** pairs and not over token
  combinations — a token that passes on two surfaces can fail on a third.
- Type: nothing below 13px; 13px only for a decorative uppercase overline;
  informational text 14px or more; body 16px minimum on mobile.
- Hit areas 44×44 including invisible padding.
- Spacing on one scale, in `rem`, and nothing off it.
- Four radii: `0`, `2px`, `8px` for overlays only, and `9999px`. No others.
- One shadow, for overlays. No card shadow, no hover lift.
- Breakpoints 360 · 600 · 900 · 1200 · 1440, min-width only. 360 is the floor.

---

## 5. What to build

**Foundations** — layout primitives first: a `Section` that knows its own ground
and its neighbour's, a `Stack`, a `Row` with an equal-height mode, a `Grid`, a
`Sheet`, a visually-hidden helper, a skip link.

**Controls** — button in its variants and every state, link, input, textarea,
select, checkbox, radio, switch, a field wrapper that owns label, help and
error, an international phone field, a combobox, a slider paired with a number
field.

**Product components** — this is where the system stops being generic and starts
being MemoryCare: a verification rail that carries the proof facts, a GPS block,
a report sheet, a photograph placeholder that names its ratio and its subject, a
tariff card with a badge reserve so titles align across a row, a price display
with the currency element, a plot calculator, a guarantees block.

**Feedback** — empty, loading and error states as first-class components, a
toast, a modal, a drawer, a lightbox. The error state matters more here than in
most products: it may appear on a screen showing a photograph of a grave, so it
cannot be cheerful and it cannot be flippant.

**Chrome** — header at two heights, footer, language switcher, mobile action bar.

Every component ships: all states, container-query behaviour, keyboard
operation, a visible focus ring, reduced-motion behaviour, a Storybook story per
state, a test, and a written note on when **not** to use it.

---

## 6. What must never exist in this system

No testimonial component and no rating property — the company is pre-launch with
zero customers and invents nothing. No QR-code or memorial-page component. No
`danger` button variant, no success or warning token, no third functional
colour. No before/after slider — a photograph of a grave is evidence, not a
transition. No "bestseller" or "most popular" flag. No component whose only
purpose is decoration.

---

## 7. Gates, all automated

Contrast over rendered pairs · no literals outside the primitive layer · every
spacing value on the scale · type floors measured on rendered output · hit areas
measured, not asserted · axe clean on every story · keyboard walk-through per
component · visual regression at 360 and 1440 · every story rendered in all
three scripts with the longest string · reduced motion honoured · the package
installs and renders from `dist/` in both a React app and a plain HTML page.

Write `ACCEPTANCE.md` with each gate and the command that proves it.

---

## 8. Documentation

A README that gets someone running in five minutes. A conventions document
written for whoever builds screens with this — naming the real class and token
vocabulary, not describing it in the abstract; every name in it verified to
exist in the built artifacts. A page on the brand constraints and why they are
constraints — the Olive rule, the single-weight display face, the dram sign — so
the next person does not undo them out of ignorance. And an `OPEN-QUESTIONS.md`
for everything you could not settle.

---

## 9. Definition of done

Someone who has never met you installs the package, reads the README, builds a
correct MemoryCare screen without asking a question — and a year later, someone
else adds a component to it without breaking the rules, because the rules are in
the lint and not in a person's memory.
