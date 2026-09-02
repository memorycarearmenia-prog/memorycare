# Addendum — build it in Figma first, then export the whole thing as screenshots

This attaches to `PROMPT-REDESIGN-EVERY-SCREEN.md`. That document says
*what* to design. This one says *where* and *what to hand back*.

Two instructions from the owner:

> **1. Create a new Figma project first, and do all of the work there.**
> **2. Then deliver the entire project as screenshots as well.**

---

# Part one — Figma

## 1. Load the skill before you touch the API

Before the first `use_figma` call, load the `figma-use` guidance — the
`/figma-use` skill if your client has it, otherwise the
`skill://figma/figma-use/SKILL.md` resource. Skipping it produces failures
that are genuinely hard to debug, and you will not be the first.

## 2. Create a new file. Do not edit any existing one.

Use `create_new_file`. Name it:

```
MemoryCare — Site rebrand (from 02.09 audit)
```

Set up these pages, in this order, and keep the numbering:

```
00 · Read me
01 · Foundations
02 · Components
03 · Public — 1440
04 · Account — 1440
05 · Windows & states
06 · Before / after
```

`00 · Read me` is a real page, not a courtesy: put on it the date, the
archive you worked from, what a reader is looking at, and the list of
things you could not do. Anyone opening this file in a month should not
have to ask.

## 3. Foundations before screens. No exceptions.

Nothing is drawn until the variables and text styles exist, because
retro-fitting tokens onto finished screens does not happen — people
re-type hexes instead, and then the file and the code disagree forever.

**Colour variables**, one collection, two modes named `Light` and `Dark`.
The dark mode is not a dark theme: it exists because two bands on the page
flip. Three layers:

- **Primitives** — the five brand values plus the two interface values.
  Describe each as "primitive, do not reference from a design".
- **Semantics** — aliased per mode. Name them so misuse is a word that is
  obviously wrong to type: Olive belongs in a `decor` namespace defined as
  *paint that never has a foreground*.
- Set `scopes` explicitly on every variable. The default pollutes every
  picker and nobody ever cleans it up.

**A trick worth using.** Two tokens are *deliberately undefined* in one
mode — Sky blue as type on a light ground, and the error colour on a dark
ground. Figma has no "undefined", so set those to **magenta** in the wrong
mode and say so in the description. When something comes out magenta on
the canvas, the rule caught a mistake in under a minute. This works: it
caught mine.

**Text styles.** Sixteen roles, from the main prompt's ramp. One set —
there is no mobile ramp, the scope is desktop. Put the reason for each
floor in the style description, so the next person does not "improve" a
14px rail down to 12.

## 4. Two font problems in Figma, and neither is your fault

**GHEA Mariam is not among Figma's fonts.** Neither is any Armenian-
capable serif — the only family matching `/armenian/` is `Charm`, which is
Thai. Two ways out:

- **Preferred:** ask the owner to install the four supplied OTFs locally.
  Figma's desktop app picks up local fonts, and then the file shows the
  real face.
- **Otherwise:** use **Source Serif 4** as a stand-in and name it as one
  **in the description of every text style that uses it**, so nobody
  mistakes the file for the specification. The built site uses GHEA
  Mariam.

**Armenian does not render on the Figma canvas at all.** The glyphs are in
the data model — read them back and they are there — but nothing draws.
This is not a font stack you can fix.

The consequence for a three-locale deliverable is real, so handle it
deliberately rather than discovering it at the end:

- Build the Armenian frames with the correct Armenian strings in them
  anyway. The text is real, and it exports and copies correctly.
- **Put a visible note on the Armenian page** saying the canvas does not
  draw these glyphs and that the strings are present and correct.
- **Deliver the Armenian screens as HTML renders instead** — see Part two,
  §3. That is where the Armenian typography can actually be judged.
- Do the same check for Russian before you rely on it, and report what you
  find.

## 5. Build order

1. Foundations — variables, text styles. Validate before continuing.
2. The mark, imported from the supplied SVG, and the medallion as a
   separate component. **The medallion is 29 filled paths with no stroke
   attribute**, so it cannot be drawn with a stroke animation, and it
   stops being legible below **48px**.
3. Components, on `02 · Components`, with variants and every state.
4. Screens, page by page, starting with `home` and `acct-order-1` —
   the first because it carries the argument, the second because it is the
   biggest hole in the product and will teach you what the account area
   needs.
5. Windows and states.
6. The before/after page, last.

Work in small steps and screenshot after each. A `use_figma` call that
tries to do everything at once fails in ways that take longer to unpick
than they took to write.

## 6. Rules that cost me time, so they should not cost you any

- **Auto-layout frames arrive with a white fill.** A frame that only
  organises children must have its fill cleared, or you get pale
  rectangles behind your text and it will not be obvious why.
- **Cards in a row are equal height, always.** Fix the row to its tallest
  child, set every card to fill it, and push the button to the foot with a
  **growing spacer** — not with hand-tuned padding, which stops working
  the moment a translator writes a longer sentence.
- **A card without a badge reserves the badge's height.** Otherwise the
  titles in a row sit at different heights and the row reads as an
  accident.
- `layoutSizing*` and `*AxisSizingMode` are different enums. Append to the
  parent **before** setting `FILL` or `HUG`.
- Position new top-level frames away from `(0,0)`; things pile up there.
- Name every layer. Thirteen frames called "Frame" is what an unfinished
  file looks like, and it is what a reviewer sees first.

## 7. Every screen carries its evidence

On the `06 · Before / after` page, pair each redesigned screen with the
archive capture it replaces, and label the pair with the archive filename
— `home__en__1440__default-full.png` and so on. A reviewer must be able to
see what changed without opening two windows.

Annotate on the canvas, next to the screen, anything that moved, with the
number of the §3 item in the main prompt that authorised it. An
unannotated move is an unauthorised one.

---

# Part two — the screenshots

The Figma file is the design record. The screenshots are what most people
will actually look at, and the only thing that survives someone losing
access to the file.

## 1. Export every screen

For every **route × locale**, at **1440**:

- the **fold** — the first viewport height
- the **full** page

Plus every window and every state on `05 · Windows & states`, and every
component variant on `02 · Components`.

**Match the archive's naming exactly**, so the before and after sort side
by side in a directory listing:

```
<route>__<locale>__<width>__<state>.png

home__en__1440__default-fold.png
home__en__1440__default-full.png
acct-order-1__ru__1440__default-full.png
acct-packages__am__1440__cancel-dialog-fold.png
```

Export at **2×** for legibility. State the scale in the manifest rather
than leaving someone to infer it from the pixel dimensions.

## 2. Verify every file, and publish the numbers

The same three checks the audit used, because they catch the failure that
otherwise goes unnoticed — a capture that is blank, or a single flat
colour, and looks like a file until someone opens it:

- byte size > 2,000
- per-channel standard deviation > 3.0
- width equals the requested width × the export scale

Any file that fails is re-exported. If it fails twice it is **reported**,
not quietly dropped. Publish the numbers per file in `capture-log.json`.

## 3. The Armenian screens go out as HTML renders

Because the Figma canvas will not draw them (Part one §4), the Armenian
locale is delivered as **rendered HTML screenshots** built on the token
file, at the same widths and with the same naming. Say plainly in the
manifest which files came from Figma and which from HTML, and why.

Do the same for Russian if your own check shows it does not render.

## 4. What the screenshot bundle contains

```
figma-export-<YYYY-MM-DD>/
  00-README.md          what this is, the Figma link, the export scale,
                        which files came from Figma and which from HTML
  manifest.json         route × locale × width × state → filename
  capture-log.json      every file with its three verification numbers
  screens/              every export
  before-after/         each pair, side by side, named for the archive file
  components/           every variant of every component
  windows/              every dialog, menu and state
```

---

# What to hand back, in total

1. **The Figma file**, shared and linked, with `00 · Read me` filled in.
2. **The screenshot bundle** above.
3. Everything the main prompt's §7 asks for — the change lists, the
   strings with their sources, the computed contrast tables, the token
   file, `NOT-GIVEN.md` and `QUESTIONS.md`.

## How this part will be judged

1. **Is it a new file?** Nothing in an existing project was touched.
2. **Do the foundations exist and is every fill bound to a variable?**
   A hard-coded hex on a frame fails.
3. **Does every screen have both framings, in all three locales?**
4. **Does every exported file pass its three checks, with numbers
   published?**
5. **Is every before/after pair labelled with its archive filename?**
6. **Is the Armenian handled honestly** — real strings in Figma, a note on
   the canvas, and HTML renders in the bundle — rather than left as empty
   frames nobody mentions?
