# PROPOSAL — Interaction & Motion

MemoryCare rebrand, 01.09.2026. Owner: interaction & motion.
Every duration and every curve in this document is a value to be implemented, not an illustration.

---

## 0. Preflight — what I read, and three conflicts I am resolving in the open

**`docs/rebrand-2026-09-01/BRIEF.md` does not exist.** The directory did not exist either; I created
it to write this file. Nothing at that path, no file of that name anywhere in the repo
(`docs/design-package-v1/BRIEF.md` is a different, older document). So my fact base is:

- `CLAUDE.md` — palette, contrast table, typography, tone, structure, truth constraints.
- `docs/site-audit-2026-08-31/` — `FINDINGS.md`, `INVENTORY.md`, `PERFORMANCE.md`.
- `docs/design-package-v1/FINAL-SYSTEM.md` §5.5–5.7 — the existing motion, focus and hit-area rules
  and the existing motion tokens.
- `docs/design-package-v1/FINAL-UX.md` — routes, Family Circle flow, state tables.
- `docs/PROMPT-VISUAL-POLISH-AND-MOTION.md` — prior art, per instruction.
- `assets/brand/brandbook/page-2-logo.png` — the mark.

If a BRIEF.md lands later and contradicts anything below, it wins; every number here is one line to
change because they are all tokens.

**Conflict 1 — `docs/logo-animation-prompt.md` (03.08.2026) is dead and I am not building it.**
It specifies five concentric rings rotating on a seamless 60-second loop, a breathing flower and
flickering stamens, in `#33373C` / `#5E6A3A` / `#FAFAF7`. The 31.08 brandbook has no rings — the
mark is two hands, five petals and a woven medallion — and all three of those hex values are
retired. `FINAL-SYSTEM` §5.5 independently forbids "a rotating, blooming or pulsing medallion".
That prompt should be marked superseded. My §3 replaces it.

**Conflict 2 — `FINAL-SYSTEM` §5.5 forbids "any animation whatsoever on the sample report", and my
scope asks for a report reveal.** I am not overturning that rule; I am drawing the line it was
missing. See §4.1. Short version: a report a real client opens gets zero motion, forever. The home
page's *depiction* of receiving one is not a report.

**Conflict 3 — `PROPOSAL-art-direction.md` §1.5 and §8 land in my scope.** It was published in
parallel with this document. Its motion section is explicitly "brief", and motion is my scope, so
**this document is authoritative on every duration, curve and behaviour**; §12 reconciles the two
line by line, adopts its one genuinely better idea, and rejects one thing it proposes that its own
governing rules forbid.

**Conflict 4 — prices.** `CLAUDE.md` and `FINAL-UX.md` §1 carry two different locked tariff tables
(60,000 / 180,000 / 240,000 vs 65,000 / 160,000 / 200,000). That is somebody's blocker, not mine.
**This document quotes no price, no visit count and no customer number**, and nothing in my spec
depends on one. Flagging it because audit FINDINGS #3 says the live site matches neither.

---

## 1. Motion philosophy

Motion here is **confirmation, not expression**. A stranger is deciding whether to trust us with
their mother's grave; a good half of them are 4,000 km away and cannot verify anything themselves.
The only legitimate job for movement on this site is to say *this happened, in this order, and it is
now true* — the visual grammar of a document being set down and countersigned, not of an interface
being pleased with itself. Mechanically that resolves to four hard rules. **Short:** state changes
land in 80–140 ms, entrances in 220 ms, and nothing on the marketing site runs longer than 320 ms
except one 1,100 ms line-drawing that plays once per session. **Flat:** every easing curve in the
system has both control points inside the unit square — there is no overshoot, no spring, no bounce,
no `cubic-bezier` with a `y` above 1, anywhere, ever; a curve that overshoots is a curve that says
"delight", and delight is the wrong word for this product. **Small:** the maximum travel of any
animated element is 8 px, and most is 4 px; nothing crosses the screen, nothing slides in from an
edge, nothing scales, nothing lifts. **Still where it matters:** the fold never animates, a
photograph of a grave never does anything but fade in on decode, and a real report, a bad-news
screen and the guest view are completely motionless. The test, applied honestly to every item below:
*would this still feel right if the photograph on screen were of my own mother's grave?* Everything
here passed it or was cut, and §9 lists what was cut.

---

## 2. Tokens

### 2.1 Existing — unchanged, use these

```css
--mc-duration-instant: 80ms;
--mc-duration-fast:    140ms;
--mc-duration-base:    220ms;
--mc-duration-slow:    320ms;
--mc-ease-standard:    cubic-bezier(.2, 0, 0, 1);   /* state changes, both-ended */
--mc-ease-decelerate:  cubic-bezier(0, 0, 0, 1);    /* entrances */
--mc-ease-accelerate:  cubic-bezier(.3, 0, 1, 1);   /* exits */
--mc-motion-distance-sm: 4px;
--mc-motion-distance-md: 8px;
```

### 2.2 Additions — four, each with its reason

```css
/* The medallion line-draw. 1,100ms is the shortest duration at which six
   interlaced strands read as being *drawn* rather than wiped on; below ~900ms
   the eye reads a reveal, above ~1,300ms it reads as a page that is stuck.
   Used by exactly two elements in the product (§3, §4.2) and by nothing else. */
--mc-duration-draw: 1100ms;

/* A pen curve: a real hand accelerates out of the first stroke and eases off
   the last. --mc-ease-standard at 1,100ms reads as sliding to a stop on ice.
   Both control points inside [0,1] — no overshoot, per §1. */
--mc-ease-draw: cubic-bezier(.45, 0, .15, 1);

/* Sequence spacing. 60ms is the existing stagger for sibling reveals and is
   unchanged. 90ms is for the report chain in §4, where the gap between steps
   IS the content — at 60ms the four steps read as one blurry event. */
--mc-stagger-tight: 60ms;   /* = the existing 60ms rule, named */
--mc-stagger-step:  90ms;
```

No other literal ms or cubic-bezier appears anywhere in the codebase. If a fifth is ever needed it
goes here with a written reason, per `FINAL-SYSTEM` §1 layer rules.

### 2.3 Colour, since motion touches it

The medallion is **Sky blue `#D4ECF9`**, which measures **1.02 on Nude** and **1.07 on Ivory** — it
is *invisible* on a light ground. So the drawn medallion only ever animates in the dark lock-up
(Sky blue on Dark Olive, 13.18). On a light ground the site uses the monochrome lock-up and the
medallion draws in **Dark Olive `#212212`** (12.93 on Nude). This is not a motion decision, but the
draw animation is the thing most likely to get someone to paste a Sky-blue mark onto a Nude hero, so
it is written down here as well.

---

## 3. Page level

### 3.1 Entry

**The fold does not animate. At all. In any state.** Header, H1, subhead, primary CTA, the price
block and the hero report preview are painted by the server and are present at first paint with
opacity 1 and no transform. Nothing below waits on JS. This is a hard rule and it protects LCP,
CLS and the audit's one genuinely good result (`PERFORMANCE.md`: CLS 0.000 today — do not regress
it). There is no splash, no preloader, no logo curtain, no `body { opacity: 0 }` that JS removes.

The single exception is the medallion draw (§3.3), which starts *after* the mark has painted in its
final position and which changes no geometry the fold depends on.

### 3.2 Route transitions

The site is server-rendered multi-page. I use the native View Transition API, and only for a
cross-fade:

```css
@view-transition { navigation: auto; }

::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: var(--mc-duration-fast);      /* 140ms */
  animation-timing-function: var(--mc-ease-standard);
}
/* header and footer persist across the navigation rather than cross-fading */
.site-header { view-transition-name: mc-header; }
.site-footer { view-transition-name: mc-footer; }
::view-transition-group(mc-header),
::view-transition-group(mc-footer) { animation: none; }
```

Opacity only — no slide, no shared-element morph, no directional logic. 140 ms is short enough that a
visitor perceives "the page changed" rather than "the page performed". Browsers without the API get
an ordinary navigation, which is the same thing minus 140 ms; nothing is conditional on support.

**Two navigations get no transition at all:**

- **The language switcher.** Switching ARM ⇄ RUS ⇄ ENG changes the script on every glyph on the
  page. Cross-fading Armenian into Cyrillic produces 140 ms of illegible overlap that reads as a
  rendering fault. Locale links carry `data-no-transition` and the handler calls
  `document.startViewTransition` never; they are plain navigations.
- **Any navigation into or out of `/portal/`.** The marketing site and the account are different
  places and should feel like it.

### 3.3 Scroll choreography

**Scroll-triggered, not scroll-linked. There is not one scroll-linked animation on this site, and
no `scroll` event listener anywhere in the codebase.**

Why, since scroll-linked (`animation-timeline: view()`) is now cheap and native: a scroll-linked
reveal hands the animation's speed to the user's finger. Flick the page and the section snaps in at
whatever velocity you threw it — the content becomes a physical toy, which is exactly the register
we are avoiding. It also re-plays every time the element re-enters the viewport, which breaks the
"fires once per element, ever" rule, and it makes the reveal reversible: scroll up a little and the
section starts *un*-arriving. A fact that un-arrives is the opposite of what this product sells.
Scroll-triggered gives the same reveal at a speed we chose, once.

```js
const io = new IntersectionObserver((entries) => {
  // one rAF for the whole batch; no layout reads in this callback, ever
  requestAnimationFrame(() => {
    for (const e of entries) {
      if (!e.isIntersecting) continue;
      e.target.dataset.arrived = '';
      io.unobserve(e.target);          // once. never again.
    }
  });
}, { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });
```

```css
[data-reveal] {
  opacity: 0;
  transform: translateY(var(--mc-motion-distance-md));   /* 8px */
  transition: opacity var(--mc-duration-base) var(--mc-ease-decelerate),
              transform var(--mc-duration-base) var(--mc-ease-decelerate);
}
[data-reveal][data-arrived] { opacity: 1; transform: none; }

/* max three staggered children per section; a fourth arrives with the group */
[data-reveal-group] > :nth-child(1) { transition-delay: 0ms; }
[data-reveal-group] > :nth-child(2) { transition-delay: var(--mc-stagger-tight); }   /*  60ms */
[data-reveal-group] > :nth-child(3) { transition-delay: calc(var(--mc-stagger-tight) * 2); } /* 120ms */
```

Rules around it:

- `-12%` bottom margin, so a section begins arriving when it is meaningfully on screen rather than
  the instant one pixel crosses the edge.
- **Anything already inside the viewport at first paint is marked `data-arrived` synchronously
  before the observer is attached.** No fold element ever runs the transition.
- **Sections opt out** with `data-reveal="none"`: the sample report page, every bad-news screen,
  the guest report view, the 404 and 500 pages, error and empty states, and legal pages. On those,
  content is simply present.
- **No-JS is the final state.** The `opacity: 0` rule lives inside a `.js` class set by an inline
  script in `<head>`, so a scraper, a reader mode or a JS failure shows a complete page.

---

## 4. The logo mark

### 4.1 What the mark actually is

From `page-2-logo.png`: two open hands in Nude, five petals in Olive, and at the centre a woven
interlaced medallion drawn as **open line-work** in Sky blue — five or six strands looping over and
under each other with five-fold rotational symmetry. The hands and petals are *filled shapes*. The
medallion is the only stroked element in the mark, and it is the only thing that can honestly be
drawn.

So: **the hands and the petals never animate. Not a fade, not a rise, not a "settling into place".**
They are painted at first paint like everything else on the fold. Only the medallion draws.

### 4.2 Where it plays, how long, how often

**One place as the full mark: the home page hero. Once per browser session.** The medallion path is
reused at 24 px as the pending-action glyph (§7) — that is the same drawing, not a second animation,
and it is the only other place it appears.

- Not the 32 px header logo — at that size the strand overlaps are two pixels wide and the draw is
  visual mush, and it would replay on every page load.
- Not the footer.
- Not a page loader. There is no page loader (§7).
- Not the 404, not the portal, not an email, not the favicon.

```js
const KEY = 'mc.mark.drawn';
const mark = document.querySelector('[data-mark]');
const allowed =
  !sessionStorage.getItem(KEY) &&
  !matchMedia('(prefers-reduced-motion: reduce)').matches &&
  !navigator.connection?.saveData;
if (allowed) { mark.dataset.draw = ''; sessionStorage.setItem(KEY, '1'); }
```

Timing, from the moment the mark paints:

| t | What |
|---|---|
| +200 ms | strand 1 begins |
| +270 ms | strand 2 begins (`--mc-stagger-tight` + 10 ms rounding) |
| +340 / 410 / 480 / 550 ms | strands 3–6 begin, **in the weave's over/under order** so the knot builds as a knot rather than as a wireframe filling in |
| +1,650 ms | last strand completes (`--mc-duration-draw` = 1,100 ms each) |

```css
[data-mark] .strand {
  stroke-dasharray: var(--len);          /* per-path, written at build time */
  stroke-dashoffset: var(--len);
}
[data-mark]:not([data-draw]) .strand { stroke-dashoffset: 0; }   /* the default */

[data-mark][data-draw] .strand {
  animation: mc-draw var(--mc-duration-draw) var(--mc-ease-draw) both;
}
[data-mark][data-draw] .strand:nth-child(1) { animation-delay: 200ms; }
[data-mark][data-draw] .strand:nth-child(2) { animation-delay: 270ms; }
/* …3–6 at 340 / 410 / 480 / 550ms */

@keyframes mc-draw { to { stroke-dashoffset: 0; } }
```

The `--len` values are measured with `getTotalLength()` **once, at build time**, and baked into the
SVG as inline custom properties. Nothing measures geometry at runtime.

**Honesty about the property:** `stroke-dashoffset` is not a compositor property — it repaints. It
is permitted here, as a named exception in §8, because it is six paths inside a single
`contain: paint` box of roughly 180 × 180 CSS px, running once per session, on the fold, at a moment
when the user is not interacting with anything. It changes no geometry, so it cannot cause layout or
CLS. Measured gate: if it costs more than **2 ms per frame** on the reference device (§8), it is
deleted and the mark is static. It is not worth one dropped frame.

**Degradation:**

- No JS → no `data-draw` → `stroke-dashoffset: 0` → the finished mark. This is the default state in
  CSS, so failure means "correct", not "invisible".
- SVG not inlined (CMS fallback) → `<img>` of `02-primary-on-light.png` → static.
- `prefers-reduced-motion: reduce` → not played, no substitute.
- Save-Data / `prefers-reduced-data` → not played.
- Second page view in the same session → not played.

**And it never loops.** There is no idle animation on the mark: no breathing, no rotation, no
shimmer, no stamen flicker. See §9.1.

---

## 5. The report reveal — the hero moment

### 5.1 The line I am drawing

`FINAL-SYSTEM` §5.5 says: no animation whatsoever on the sample report, on a bad-news screen, or on a
guest report view. That rule is right and I am keeping every word of it. What it did not distinguish
is the difference between **the artefact** and **the depiction of receiving the artefact**.

| Surface | Motion |
|---|---|
| `/portal/report/:id` — a real report a real client opens, having been notified that their mother's plot was visited | **Zero. Present on paint. Not one transition, not one fade, not one reveal.** |
| `/sample-report/` — the standalone proof page | **Zero.** The page *is* the artefact. Rule unchanged. |
| Guest report from a family chat link | **Zero.** The quietest page in the product. |
| The home page hero's `ReportPreview` | **The sequence below.** This is a marketing illustration of what arrives, not a report. It carries no real person's grave. |

That is the whole reconciliation, and it is the only place in the product where a sequence exists.

### 5.2 The sequence

The intent: a visitor should feel the *shape* of receiving verified proof — facts landing in an
order, the GPS confirmation as the beat that changes the page from a claim into evidence, and only
then the photograph, which does not perform.

The sheet does not fly in. **The report sheet is present at first paint**, with its masthead, its
rules and every box at final size — the rail slot, the GPS block and the image frame all have their
final geometry from markup (`width`/`height` on the image, `aspect-ratio` and `min-height` on the
slots). Everything below is opacity and ≤4 px of travel inside boxes that never change size.
**CLS contribution: 0.000.**

t₀ = the hero's paint + 320 ms. Not `load`, not `DOMContentLoaded`, not an IntersectionObserver
(the preview is above the fold; observing it would just fire immediately with extra latency).

| t (ms) | Step | Motion | Duration / curve |
|---|---|---|---|
| 0 | rail item 1 — **date** | opacity 0→1, `translateY(4px→0)` | 220 `--mc-ease-decelerate` |
| 90 | rail item 2 — **cemetery** | same | 220 decelerate |
| 180 | rail item 3 — **plot** | same | 220 decelerate |
| 450 | **coordinate pair** | opacity 0→1 only, no travel — a number does not slide | 220 decelerate |
| 590 | **`GPS confirmed` tick** | a two-segment stroke path drawing, `stroke-dashoffset` | 180 `--mc-ease-draw` |
| 1,100 | **the photograph** | opacity 0→1, **linear**, no transform, no scale, no wipe, no crossfade from a blur | 200 linear |
| 1,400 | caption — crew, arrival time | opacity 0→1, `translateY(4px→0)` | 220 decelerate |

Ends at ~1,620 ms. Runs **once**. Never on scroll-back, never on resize, never again in the session.

Three details that carry the whole thing:

1. **The 270 ms gap before the GPS block** (180 → 450) is the longest pause in the product. It is the
   difference between a list appearing and a fact being confirmed. Do not close it.
2. **The tick draws, it does not pop.** 180 ms, two segments, `--mc-ease-draw`, in Deep Olive
   `#575E3B` on the light sheet (6.01 on Ivory) or Sky blue on a dark ground (13.18). No scale, no
   bounce, no green, no checkmark that springs.
3. **The photograph waits for its own bytes.** If the image has not decoded by t+1,100, the step
   holds and fires on `img.decode()`. An empty frame at the moment of proof is worse than a late
   one.

```js
const img = sheet.querySelector('[data-report-photo]');
img.decode()
   .catch(() => {})                       // decode failure must not stall the chain
   .then(() => { img.dataset.arrived = ''; });
```

If JS never runs, every element is in its arrived state and the preview is complete and correct.

---

## 6. Micro-interactions

Governing rules for the whole table: **`:focus-visible` only**, 2 px ring, 2 px offset, Deep Olive
(Nude inside `.mc-on-dark`), and **the ring has `transition: none` — it appears and disappears at
0 ms, always** (audit FINDINGS #24: today focusing a field produces a byte-identical screenshot).
Every control has a ≥44×44 hit area via `.mc-hit-44` (FINDINGS #25). `touch-action: manipulation` on
every interactive element. No control anywhere gets a `transform`, a `scale` or a `box-shadow` lift.

### 6.1 The pressed state, because touch is the primary channel

Hover is a desktop luxury; the majority of this audience is on a phone. So:

```css
@media (hover: hover) and (pointer: fine) {
  .mc-button:hover { background-color: var(--mc-button-bg-hover); }
}
.mc-button {
  transition: background-color var(--mc-duration-fast) var(--mc-ease-standard),
              border-color     var(--mc-duration-fast) var(--mc-ease-standard);
}
/* pressed: ground steps one value, in fast, out at normal speed */
.mc-button:active,
.mc-button[data-pressed] {
  background-color: var(--mc-button-bg-active);
  transition-duration: var(--mc-duration-instant);           /* 80ms in */
}
```

A 40 ms tap would otherwise show no feedback at all, so `pointerdown` sets `data-pressed` and it is
**held for a minimum of 120 ms** before `pointerup` can clear it. Release returns over 140 ms. No
ripple, no scale, no haptic-mimicking wobble — just a ground that darkens under the thumb and comes
back. `-webkit-tap-highlight-color: transparent`, since we are supplying our own.

### 6.2 The table

| Control | Default → hover | Pressed / active | Focus | Notes |
|---|---|---|---|---|
| **Primary button** (Dark Olive fill, Ivory label) | fill lightens one step, 140 standard | fill darkens one step, 80 in / 140 out | inner Ivory ring, instant | width is locked to the widest label of all its states so a swap to "Sending…" never reflows |
| **Secondary button** (Deep Olive hairline) | border 1→2 px via `inset box-shadow`, never `border-width` | ground → `alpha-deepolive-08`, 80 ms | 2 px Deep Olive ring, instant | |
| **Text link** | underline colour → Deep Olive, 140 standard | 80 ms | ring, instant | underline is permanent, never animated in |
| **Text input** | border colour, 140 standard | — | `box-shadow: inset 0 0 0 2px` in 140 ms — **height never changes** | real `<label>` above the field, so there is no floating-label animation to build (FINDINGS #10) |
| **Validation message** | opacity 0→1, 140 standard | — | — | the message slot has a reserved `min-height: 20px` from markup. **No shake, ever.** Error border colour transitions over 140 ms to `#8C3A2E` |
| **Submit blocked** | — | — | focus jumps to the first invalid field **instantly** | `scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'center' })`, `scroll-margin-top` set so the sticky header never covers it |
| **Tariff card** | border 1→2 px inset Deep Olive + ground Ivory→Nude, 140 standard | 80 ms ground step | 2 px ring on the card, instant | **no lift, no scale, no shadow.** The "leading choice" marker on Optimal is static — it never pulses, glows or animates in |
| **Language switcher** | segment colour 140 standard | 80 ms | ring per segment | three links, not a disclosure — no open/close animation exists. **No sliding underline** (§9). Each segment gets 44×44 (FINDINGS #25) and the switcher is **inside the mobile menu** as well as the header (FINDINGS #27) |
| **Mobile menu — open** | scrim opacity 0→1, 140 standard; panel opacity 0→1 + `translateY(-8px→0)`, 220 decelerate | — | focus moves to the close button | **not** a slide-in drawer: a full-width surface travelling 360 px reads as an app, and it is the largest moving area on the site. 8 px and a fade. `inert` on everything behind it, focus trapped, `overflow: hidden` + `scrollbar-gutter: stable` on `<html>` so nothing reflows |
| **Mobile menu — close** | opacity 1→0, 140 `--mc-ease-accelerate`, **no translate** | — | focus returns to the toggle | exits are faster and simpler than entrances; leaving is not an event |
| **Accordion / disclosure** | see below | — | ring on the summary row | |
| **Chevron** | `rotate(0 → 90deg)`, 220 standard | — | — | the chevron is not the brand mark; rotating it is fine |
| **Family Circle — invite** | see below | — | — | |
| **Toast** ("Link copied") | opacity 0→1 + `translateY(4px→0)`, 140 standard; hold 4,000 ms; exit opacity 140 accelerate | — | not focusable | `role="status"`, bottom-centre above the safe-area inset, never over the action bar |
| **Sticky mobile action bar** | opacity + `translateY(8px→0)`, 220 decelerate, driven by a **sentinel IntersectionObserver**, never by scroll position | — | — | suppressed while any form field has focus and while the calculator result bar is mounted (existing rule) |

**Accordion**, in detail — the existing spec animates `height`, which triggers layout on every frame:

```css
.mc-disclosure__panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows var(--mc-duration-base) var(--mc-ease-standard),
              opacity           var(--mc-duration-fast) var(--mc-ease-standard);
  opacity: 0;
  contain: layout paint;
}
.mc-disclosure[open] .mc-disclosure__panel { grid-template-rows: 1fr; opacity: 1; }
.mc-disclosure__panel > * { min-height: 0; overflow: hidden; }

@supports (interpolate-size: allow-keywords) {
  :root { interpolate-size: allow-keywords; }   /* height: 0 → auto natively */
}
```

Still a layout-affecting animation — that is unavoidable for a disclosure — but `contain: layout
paint` bounds the recalculation to the panel's own subtree instead of the document.

**Family Circle invite**, in detail. `FINAL-SYSTEM` forbids any transition on the Family Circle
avatars; kept.

1. Submit → button label swaps to "Sending" and the 24 px arc appears **after 400 ms** of pending
   (§7). Button width is pre-locked, so nothing moves.
2. Success → the form cross-fades to the confirmation, 220 ms opacity, in the same box.
3. At +150 ms the new roster row arrives: opacity 0→1 + `translateY(4px→0)`, 220 decelerate. The
   row's initial-disc has no transition of its own; it arrives as part of the row.
4. `aria-live="polite"` carries "Invitation sent to {contact}. It is valid for 14 days." regardless
   of any of the above.

---

## 7. Loading, skeletons, empty, error

**There is no page-level loading state on the marketing site.** Every route is one server-rendered
response (`INVENTORY.md` confirms this is already true of the build). No splash, no preloader, no
progress bar, no route-change spinner.

| State | Spec |
|---|---|
| **Pending action < 200 ms** | nothing. No spinner, no skeleton. A flash of loading UI is worse than the wait it replaces |
| **Pending action ≥ 200 ms** | skeleton blocks appear, then are **held for a minimum of 400 ms** even if the response lands sooner, so they never flash |
| **Skeleton** | flat `surface-sunken` blocks at the content's final geometry. **No shimmer, no pulse, no gradient sweep, no animation of any kind.** A skeleton settles; it does not perform |
| **Skeleton → content** | opacity cross-fade, 140 ms `--mc-ease-standard`, in the identical box. Zero layout shift |
| **In-control pending glyph** | **the medallion, drawn once and then held still.** 24 px, 1.5 px stroke, Deep Olive on light / Sky blue on dark, one strand-ordered draw over `--mc-duration-draw` (1,100 ms), then **static at full stroke** for as long as the wait continues. Appears only after 400 ms pending, `aria-busy="true"`, always beside a word ("Sending", "Loading"), which is what actually communicates that work is in progress. **The mark never rotates and never pulses.** See §12 |
| **Empty state** | no motion at all. Present on paint. An empty Family Circle roster or an unstarted visit list is not an event |
| **Error state — form** | inline message fades in over 140 ms into reserved space; the field border transitions to `#8C3A2E` over 140 ms. No shake, no bounce, no scroll animation beyond §6.2 |
| **Error state — page (404, 500)** | **zero motion.** No reveal, no illustration animation, no view transition into them. `data-reveal="none"` on the whole document |
| **Bad-news screens** (visit postponed, crew could not reach the plot) | **zero motion**, and they are explicitly excluded from the section-reveal system. A person reading one is disappointed; anything moving on that screen is the company being pleased with itself |
| **Image loading** | `opacity: 0 → 1`, 200 ms linear, on `decode()`. Intrinsic `width`/`height` always present. No blur-up, no LQIP fade, no colour-block placeholder that morphs |
| **Offline / failed fetch** | plain text, a retry button, no animation |

One more, since `#8C3A2E` is invisible on Dark Olive (2.12): **no error state may ever be rendered
inside a dark band**, so no error animation is ever specified on a dark ground. That rule is from
`CLAUDE.md`; repeating it because error states are where it gets broken.

---

## 8. `prefers-reduced-motion: reduce` — the complete parallel spec

The existing system-level implementation crushes every duration to 1 ms globally. That is a blunt
instrument: it also destroys the opacity cross-fades that reduced-motion users have no problem with,
and it makes state feedback (a button ground darkening under a thumb) snap in a way that reads as a
rendering glitch rather than as a response. **I replace it with an explicit set.** The principle:
*remove travel and remove sequence; keep colour, keep feedback, keep cross-fades.*

```css
@media (prefers-reduced-motion: reduce) {
  :root {
    --mc-motion-distance-sm: 0px;
    --mc-motion-distance-md: 0px;
    --mc-duration-draw: 0ms;
    --mc-stagger-tight: 0ms;
    --mc-stagger-step:  0ms;
  }
  html { scroll-behavior: auto; }
  ::view-transition-group(*) { animation: none !important; }
}
```

| Behaviour | Default | Under `reduce` |
|---|---|---|
| Fold | already still | **untouched** — already still |
| Section entrance | opacity + 8 px rise, 220 ms, staggered 60 ms | **cross-fade**: opacity only, 140 ms linear, **no stagger** — all siblings together |
| Route transition | 140 ms cross-fade | **removed.** Plain navigation |
| **Logo medallion draw** | 1,100 ms × 6 strands | **removed entirely.** The mark is present, complete, static. No substitute, no fade-in — there is nothing to replace, the mark was always going to be there |
| **Report sequence** | 7 steps over 1,620 ms | **removed as a sequence.** Every element present at paint. **Not** replaced by a simultaneous cross-fade: the sequence's whole meaning was its ordering, and seven things fading in at once is noise, not a reduced version of an order |
| GPS tick draw | 180 ms stroke draw | **removed.** Tick present |
| Photograph | 200 ms decode fade | **survives, untouched.** An opacity change on a static image is not a vestibular trigger, and removing it produces a visible pop-in |
| Button hover / press | colour, 140 / 80 ms | **survives, untouched.** This is feedback. Removing it makes the product feel broken, which is not an accessibility improvement |
| Input focus ring | instant | **survives, untouched** — it was already instant |
| Input focus border | inset shadow, 140 ms | **survives, untouched** (colour only, no travel) |
| Validation message | 140 ms fade into reserved space | **survives, untouched** |
| Scroll-to-invalid-field | `behavior: 'smooth'` | **`behavior: 'auto'`** — instant jump |
| Tariff card hover | border + ground, 140 ms | **survives, untouched** |
| Mobile menu open | scrim fade + panel 8 px rise, 220 ms | **cross-fade only**: scrim and panel opacity 0→1, 140 ms. No translate |
| Mobile menu close | 140 ms opacity | **survives** at 140 ms |
| Accordion | `0fr → 1fr` over 220 ms | **snaps open**; the panel content cross-fades over 140 ms so the change is still legible |
| Chevron rotation | 220 ms rotate | **removed.** The chevron swaps orientation instantly |
| Toast | rise + fade | **fade only**, 140 ms in, 140 ms out. Hold unchanged at 4,000 ms |
| Sticky action bar | 8 px rise, 220 ms | **cross-fade**, 140 ms, no translate |
| Pending glyph | medallion draws over 1,100 ms, then holds | **drawn state immediately**, no draw. The word ("Sending") does the work — the existing rule, kept, with a better glyph |
| Skeleton | already motionless | **untouched** |
| Empty / error / bad-news | already motionless | **untouched** |

**No information is lost anywhere in that column.** Every state that exists by default still exists,
is still reachable, and is still legible; every removal is a removal of *travel* or *timing*, never
of a fact. Verification is part of the QA gate: the whole product is walked once with the OS setting
on, and every row above is confirmed by capture, at 360 and 1440, in all three locales.

Two adjacent preferences, handled at the same time:

- **`prefers-reduced-data` / `navigator.connection.saveData`** — the medallion draw does not play
  (it costs paint on the exact devices that flag this). Everything else is unchanged; motion here is
  CSS, not bytes.
- **`prefers-contrast: more`** — no motion consequence, but the focus ring goes to 3 px. Noted so it
  is not forgotten in the same pass.

---

## 9. Performance budget

**Reference device for every number below:** a mid-range 2022 Android (Snapdragon 6-class), Chrome,
DevTools 4× CPU throttle, "Fast 4G". Not a laptop.

### 9.1 What may be animated

**Allowed without argument:** `opacity`, `transform` (`translate` and `rotate` only — never
`scale`).

**Allowed as named exceptions**, because a system with no shadows and no transforms has to express
state changes through colour, and these are paint-only on single controls at ≤140 ms:

| Property | Where | Bound |
|---|---|---|
| `background-color`, `border-color`, `color` | buttons, links, cards, inputs | paint area ≤ one control |
| `box-shadow` (inset ring only) | input focus, secondary button border | never an outer/blur shadow |
| `stroke-dashoffset` | the hero medallion (6 paths, once per session), the 24 px pending glyph (same paths, once per pending action), the GPS tick (2 segments, once) | `contain: paint`; **≤2 ms/frame or it is deleted** |
| `grid-template-rows` (`0fr → 1fr`) | accordions only | `contain: layout paint` on the panel |

**Forbidden to animate, absolutely:** `width`, `height`, `top`/`right`/`bottom`/`left`, `margin`,
`padding`, `font-size`, `border-width`, `filter`, `backdrop-filter` (none exists anyway),
`background-image`, and anything on the `<body>` or a layout container. If a block must change size,
its space is reserved in markup.

### 9.2 Targets

| Metric | Target | Note |
|---|---|---|
| **CLS** | **0.000 on the fold**, ≤0.02 whole page, in all three locales at 360 and 1440 | today's build measures 0.000 (`PERFORMANCE.md`) — motion must not cost that. Every animated element has its final box from markup |
| **INP** (p75) | **≤150 ms** | tighter than Google's 200 ms "good", because our controls do almost nothing: a tap changes a colour. If a control exceeds it, something is doing work it shouldn't |
| **LCP** | ≤2.5 s at 360 on Fast 4G, all three locales | **no animation may start before LCP.** The report sequence starts at hero-paint + 320 ms, the medallion at +200 ms, both after the LCP element has painted |
| Frame rate | 60 fps floor, ≤3 dropped frames across any single sequence | profiled on the reference device, not on a workstation |
| Long tasks caused by motion code | **zero above 50 ms** | |
| Motion JS | **≤2.5 KB gzipped, no library** | see 9.4 |

### 9.3 Keeping it off the main thread

- Every animation except the four named exceptions runs on `opacity`/`transform` and is composited.
- **Zero `scroll` event listeners in the codebase.** All scroll-position knowledge comes from
  `IntersectionObserver` sentinels (section reveals, the action bar). Nothing polls, nothing throttles.
- **No forced reflow in any observer callback.** No `getBoundingClientRect`, `offsetTop`,
  `getComputedStyle` or `getTotalLength` inside an IO or rAF handler. Path lengths are baked at build
  time (§4.2). Reveal batches are applied inside one `requestAnimationFrame`, writes only.
- `will-change` is set **only** on the mobile-menu panel and the toast, only for the life of the
  transition, and removed on `transitionend`. It is never a blanket rule; a permanent
  `will-change: transform` is a permanent compositor layer and, on this audience's devices, memory
  we do not have.
- `contain: paint` on the mark, `contain: layout paint` on accordion panels.
- No `requestAnimationFrame` loop runs anywhere, ever. There is no continuously running animation in
  this product — every animation has an end.

### 9.4 What this replaces

The audit found jQuery (`jquery-latest.min.js`, frozen since 2014), Vanta.js at `@latest`, three.js
r134 and Swiper 11 loaded from four CDNs with no SRI (`FINDINGS.md` #32), on a 4.8–5.9 MB page
(#31). **A WebGL cloud background is not motion design, it is a 600 KB decoration on a page about a
grave.** All four go. The complete motion layer specified in this document is: one
`IntersectionObserver`, one `sessionStorage` check, one `img.decode()`, one pointer-press helper —
under 2.5 KB gzipped, no dependency, no CDN, no third-party code executing on a site that will take
card payments. **GSAP, Framer Motion, AOS, Lottie and Rive are all refused**; nothing here needs
them, and every one of them is a bigger runtime than the whole feature.

---

## 10. What I refuse to animate, and why

1. **The mark's idle loop.** `docs/logo-animation-prompt.md` specifies a seamless 60-second cycle:
   five rings rotating at 60/30/20/15 s, the flower breathing 100→102 %, the hands rising ±2 px,
   stamens flickering. It is careful work and it is dead three times over — the rings do not exist in
   the 31.08 mark, its colours are retired, and `FINAL-SYSTEM` §5.5 already forbids a rotating,
   blooming or pulsing medallion. Beyond governance: a logo that breathes forever is the company
   performing sincerity at someone who came here about their mother's grave. It also holds a
   compositor layer alive on a mid-range phone for the entire visit. The mark draws once and is then
   still.
2. **Any motion on a real report, a bad-news screen or a guest report view.** §5.1.
3. **A before/after comparison slider, wipe or drag handle.** The build has one (`.beer-slider`). It
   turns a photograph of a grave into a toy, and motion is exactly how it sneaks back in.
4. **Parallax, scroll-jacking, pinned sequences, scroll-linked timelines.** §3.3.
5. **Count-up or rolling numerals on any price or total.** A price is a fact, not a slot machine.
6. **Auto-advancing carousels.** The reviews carousel is fabricated content that must be deleted
   outright (FINDINGS #2) and the partners carousel is four empty tiles (#22); the correct fix for
   both is removal, not repair. If a gallery ever ships, it advances only on a press.
7. **Hover-zoom or Ken Burns on a photograph.** Evidence does not drift.
8. **Skeleton shimmer.** A loading state that entertains.
9. **Card lift, scale or shadow on hover or press.** The system has one shadow and it is not for
   this.
10. **Spring physics, bounce, elastic, overshoot.** No curve in this system has a control point
    outside the unit square. This is enforceable by grep.
11. **A sliding underline on the language switcher.** They are three navigation links; the page
    reloads. An indicator that animates to a position the user is already leaving is decoration
    pretending to be feedback.
12. **A success animation on payment.** Paying for a year of grave care is not a win. It gets a
    receipt: still, complete, immediate.
13. **A page-load splash or preloader.** §3.1.
14. **Cursor followers, magnetic buttons, text scramble, typewriter reveals, animated gradients,
    particles, falling petals, confetti.**
15. **Sound.** None, anywhere, under any condition.
16. **Any animation whose removal under `prefers-reduced-motion` would lose information.** If a
    change is only legible because it moved, the design is wrong, not the motion.

---

## 11. Acceptance gates

Motion ships only when all nine pass, measured, at 360 and 1440, in ARM / RUS / ENG:

1. CLS **0.000** on the fold; ≤0.02 whole page.
2. INP p75 ≤150 ms on the reference device.
3. LCP ≤2.5 s; **no animation begins before LCP** (verified in a performance trace, not by reading
   the code).
4. Every animated element has its final geometry in markup — verified by disabling JS and confirming
   an identical layout.
5. With JS disabled, every page is complete, every state is the arrived state, nothing is invisible.
6. Every one of the 26 rows in §8 confirmed under the OS reduced-motion setting, by capture.
7. Focus ring visible on **every** control, appearing at 0 ms (closes FINDINGS #24), and every
   control ≥44×44 (closes #25).
8. Language switcher present and operable inside the open mobile menu (closes #27).
9. No `scroll` listener, no `will-change` outside the two permitted elements, no `cubic-bezier` with
   a control point outside `[0,1]`, no animation library — all four checkable by grep in CI.

One thing outside my scope that motion must not be used to paper over: `user-scalable=no` is on
every page today (FINDINGS #7) and 200 % zoom must work on every route. If a reveal breaks at 200 %
zoom, the reveal is wrong.

---

---

## 12. Reconciliation with `PROPOSAL-art-direction.md`

We agree completely on register, on the forbidden list, and on the two biggest calls: the mark never
spins, and nothing animates on a report photograph, a status screen or a guest view. Six divergences,
resolved:

| Item | Art direction §8 / §1.5 | Resolved | Why |
|---|---|---|---|
| **Loading glyph** | the medallion **drawn** rather than a generic arc, 1.5 px, Deep Olive / Sky blue, 900 ms | **Adopted**, at `--mc-duration-draw` (1,100 ms) rather than 900 ms so it shares one token with the hero draw | It is the better idea and I have taken it. It reads as a seal being made, it is recognisably ours at 24 px, and it retires the generic arc in `FINAL-SYSTEM` §5.5 |
| **…then a 1,200 ms opacity pulse 1 → 0.55 → 1** | proposed | **Rejected.** The drawn seal holds still; the accompanying word carries the wait | This is precisely the "pulsing medallion" that the same document's governing spec (`FINAL-SYSTEM` §5.5) forbids, and a brand mark breathing at 0.55 opacity while someone waits is the mark performing patience at them. A word that says "Sending" is not ambiguous |
| **Section entrance** | 320 ms `cubic-bezier(.2,.7,.2,1)` | **220 ms `--mc-ease-decelerate`** | The 320 ms/`.2,.7,.2,1` pair is a fifth curve and a fifth timing that exist in no token layer. `--mc-motion-enter` already means exactly this. One system, not two |
| **Link and button hover: "underline draws from the inline start", 160 ms** | proposed | **Rejected.** Underline is permanent; hover changes its **colour** at 140 ms | A drawing underline animates `width` or `background-size`, both of which are on the forbidden list in §9.1, and at 160 ms × three scripts it reads as a wipe. It also fails RTL-neutrality of intent for no gain |
| **Accordion 240 ms; overlays scrim 160 ms / sheet 240 ms** | proposed | **220 ms expand; scrim 140 ms, panel 220 ms** | Same behaviours, snapped to the existing four durations. 160 and 240 are new literals with no reason attached |
| **Reduced motion: "everything to opacity at ≤100 ms"** | proposed | **The 26-row table in §8** | "Reduce everything to 100 ms" still leaves a seven-step report sequence firing in 700 ms, which is worse than either removing it or keeping it. Reduced motion needs a per-behaviour answer, and §8 is it |

Everything else in `PROPOSAL-art-direction.md` — the empty, error and failed-image frames in §1.4,
the no-black-box rule, the form-submitted panel rather than a toast or a checkmark animation — is
adopted verbatim and is reflected in §6 and §7 above.

---

*Numbers in this document are tokens, not opinions. If the register is wrong, the fix is one edit to
§2 and everything follows.*
