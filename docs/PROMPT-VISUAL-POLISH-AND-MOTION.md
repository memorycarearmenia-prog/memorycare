# Visual polish and motion — MemoryCare

You have a working build. This pass makes it feel made rather than assembled,
and gives it motion. You are the art director now, not the implementer, and you
are expected to propose — not to wait for a list.

Read this whole brief before touching anything.

---

## 1. What this product is, before you animate anything

A stranger is deciding whether to trust us with the grave of their mother. Half
of them are abroad and cannot check. They open a report six to nine times a year
and forward it to their family.

So the register is **care and precision, never delight.** Nothing bounces.
Nothing celebrates. Nothing springs. There is no confetti, no easter egg, no
playful micro-interaction, no mascot, no parallax showreel. A motion that would
be charming in a food-delivery app is an insult here.

The test for every animation you add, and you must apply it honestly:
**would this still feel right if the photograph on screen were of my own
mother's grave?** If there is any hesitation, it does not ship.

That does not mean stillness. It means motion that behaves like a document being
laid down, a fact being confirmed, a page being turned by a careful person.
Restraint is not the absence of craft — it is the harder version of it.

---

## 2. What you are given, and what is already decided

The build, the design system, and these motion tokens, which already exist and
which you should use rather than invent:

```
--mc-duration-instant  80ms     --mc-ease-standard    cubic-bezier(.2,0,0,1)
--mc-duration-fast    140ms     --mc-ease-decelerate  cubic-bezier(0,0,0,1)
--mc-duration-base    220ms     --mc-ease-accelerate  cubic-bezier(.3,0,1,1)
--mc-duration-slow    320ms
--mc-motion-distance-sm 4px     --mc-motion-distance-md 8px
```

If you need a value these do not cover, add it to the primitive layer with a
written reason. Do not scatter literals.

Everything in the specification still binds: the palette, the contrast table,
the type floors, the spacing scale, the four radii, the one shadow, one script
per locale, and the content rules. **Motion may not solve a problem by changing
a colour, a size or a word.**

---

## 3. The visual polish pass — do this first

Motion on top of sloppy composition just makes the sloppiness move. Before any
animation, go through the build and fix:

- **Optical alignment.** Where a heading, a rule and a block below it start on
  three different vertical positions. Where a hairline stops short of the text
  above it. Where a bullet is centred on the line box instead of the first line
  of type.
- **Rhythm.** Two blocks with almost-equal gaps that should be equal, or equal
  gaps that should differ because one boundary is stronger than the other.
- **Card rows.** Equal heights, actions aligned across the row, badge reserve
  respected, and the same internal padding everywhere.
- **Type colour.** A page where three greys are doing the work of two. Secondary
  text used where primary belongs, or the reverse.
- **Edges.** Every hairline the same weight and the same token. Every corner the
  same radius as its siblings.
- **Long strings.** A 40-character cemetery name, a long Armenian label, a
  three-line heading. Find what breaks and fix the layout, not the string.
- **The 600–900 range**, where hand-built layouts fall apart.
- **Empty, loading and error states**, which were built early and never revisited
  and always look it.

Take a before-and-after screenshot of every page you touch, at 360 and 1440.

---

## 4. Motion — where it earns its place

Below are the blocks that deserve motion and what the motion should be *about*.
The specific execution is yours. I am naming the intent, not the keyframes —
**if you have a better idea for any of these, use it and say why.**

**The report, arriving.** This is the product. When a report opens, it should
feel like a document being set down, not a page loading: the sheet settles, then
the verification facts resolve, then the photographs. A short, ordered sequence —
not everything at once, not a long cascade. The GPS block is the moment of
proof; it may take a beat of its own. The photographs themselves never animate
beyond a plain fade — no reveal, no wipe, no zoom, no comparison slider. The
image of a grave is evidence, not a transition.

**Scroll-revealed sections.** The marketing pages want a quiet arrival: a small
rise and fade as a section enters, staggered by no more than a few tens of
milliseconds between siblings. It should be almost subliminal. If a visitor
notices the animation rather than the content, it is too much. Never animate the
first screen on load — the fold must be present instantly.

**The calculator.** The one place a number changing is genuinely informative.
When a slider moves, the surcharge lines and the total should update in a way
that shows *which* number changed. Do not count up digit by digit — that is a
gimmick and the specification already forbids it. Consider instead a brief
emphasis on the changed line, and a total that transitions rather than snaps.

**Tariff cards.** Hover and focus states that acknowledge without lifting. No
shadow, no scale, no float — those belong to a different product. A border, a
ground, a rule: something that says *selected* rather than *fun*.

**The form.** The highest-stakes interaction we have. Focus should be immediate
and unmistakable. Validation appears without jumping the layout — reserve the
space. The transition from filled form to sent state should feel like a receipt,
calm and final. This is where a person who has hesitated for weeks finally acts;
do not make it feel light.

**The share sheet and the copied toast.** Small, fast, obviously reversible.

**Navigation and the mobile action bar.** The header on scroll, the sticky action
bar appearing and retreating. These must never fight the content or steal the
fold. If the action bar covers the calculator, it hides while the calculator is
in view — that rule already exists; make the transition invisible.

**The bad-news screens** — visit postponed, crew could not reach the plot. These
get the *least* motion in the product. A person reading them is disappointed.
Anything decorative here reads as the company being pleased with itself. Plain,
immediate, still.

**The guest report.** Someone arrived from a family chat with no account and no
context. Nothing here may look like marketing. The quietest page in the product.

---

## 5. Where motion is forbidden

- On or around a photograph of a burial, beyond a plain opacity fade.
- Any before/after slider, wipe or comparison animation. Already forbidden, and
  motion is exactly how it sneaks back in.
- Anything that delays the first screen, the price, or the request form.
- Anything that moves a target the user is reaching for.
- Anything that fires on scroll more than once for the same element.
- Loading states that entertain. A skeleton settles; it does not shimmer like a
  game.
- Sound. There is none, anywhere.

---

## 6. Technical rules

- **Transform and opacity only.** No animation of `width`, `height`, `top`,
  `left`, `margin` or anything else that triggers layout. If a block must change
  size, reserve the space.
- **No cumulative layout shift.** Measure it; the target is zero on the fold.
- **`prefers-reduced-motion: reduce` removes movement, not information.** Every
  state must still be reachable and every change still legible — replace motion
  with an instant change, never with nothing. Test the whole product under it.
- **Nothing animates before it is visible.** Use an intersection observer, not a
  timer, and unobserve after the first run.
- **Focus is never animated away.** A focus ring appears instantly.
- **60fps on a mid-range Android**, not on your machine. Profile it.
- Respect the existing durations. As a rule of thumb here: state changes at 80–140ms,
  entrances at 220ms, the report sequence up to 320ms per step, and nothing in
  this product needs longer.

---

## 7. What to deliver

1. The polished build.
2. `MOTION.md` — every animation you added: what it is, where, which tokens,
   why it earns its place, and what happens under reduced motion. Anything you
   proposed that is not in §4 gets a sentence of argument.
3. Before-and-after screenshots for every page you touched, 360 and 1440.
4. A short screen recording of the report opening and of the calculator
   responding — the two sequences most worth reviewing as motion rather than as
   stills.
5. The gates from the build brief, re-run: contrast, type floors, hit areas,
   locale purity, axe, Lighthouse. Motion must not have cost any of them.

---

## 8. How I will judge it

I will open the site on a phone, in Armenian, and scroll it once. Then I will
open a report.

If I notice the animation, it is too much. If the page feels dead, it is too
little. If it feels like a careful person is showing me something they did
properly — that is the target, and it is worth iterating three or four times to
reach it.

Show me your first pass on one page — the home page — before applying the
system everywhere. It is cheaper to argue about the register once than to undo
it eleven times.
