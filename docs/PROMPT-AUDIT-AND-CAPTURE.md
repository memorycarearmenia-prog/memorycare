> # ⚠️ SUPERSEDED — 01.09.2026
>
> Replaced by `docs/PROMPT-AUDIT-INSIDE-AND-OUT.md`, which adds the
> authenticated area (this one only ever covered the public site), a
> personal-data section for working inside a real account, the 1024–1300px
> band where a known defect lives, and a list of specific findings to
> confirm or refute. Kept for reference.

# Audit the site and produce a complete visual record

Your job is to walk the entire product, prove what exists, and hand back an
archive that lets someone who has never opened the site know exactly what it
contains and what state it is in.

You are documenting, not fixing. If you find defects — and you will — record
them with evidence. Do not change the build.

---

## 1. What "complete" means

Complete is not "every page". It is **every route × every locale × every
viewport × every state**, plus **every window that can open on top of them**.

A page you screenshotted once, in English, at 1440, in its default state, is
about four per cent documented.

Before capturing anything, build the coverage matrix (§3). Capture against the
matrix. A cell you skipped is a cell you must mark as skipped and explain — not
one you quietly omit.

---

## 2. Enumerate from the source, never from memory

Do not list the pages by clicking around and hoping you saw them all. Derive the
list three ways and reconcile:

1. **The router.** Every route the application declares, including dynamic
   segments and the token routes such as the shared-report link.
2. **The specification.** Every route the specification names, whether or not it
   is built. A specified route that does not exist is a finding, and it belongs
   in the record.
3. **The code.** Grep for every component that renders a modal, drawer, sheet,
   toast, tooltip, popover or menu. Each one is a window that must appear in the
   archive, and these are the ones people forget.

Reconcile the three lists. Anything present in one and absent from another is
recorded before you take a single screenshot.

---

## 3. The coverage matrix

Produce `INVENTORY.md` first, as a table, and get it complete before capturing.

**Axes:**

- **Route** — every URL, including the ones behind a token or an account.
- **Locale** — `hy`, `ru`, `en`. Armenian first: it is the widest and the most
  likely to break.
- **Viewport** — `360 · 768 · 1024 · 1440 · 1920`. 360 is the floor and the
  primary channel.
- **State** — default, empty, loading, error, success, and every domain state
  the screen can hold.

**Domain states you must not miss**, because they are the ones a normal pass
never reaches:

- A plot with no visits yet — the first entry after payment.
- A visit report in full, and a report with no photographs.
- The shared report seen by a guest with no account.
- A visit postponed by weather; a visit where the crew could not reach the plot;
  a guarantee re-visit requested.
- Payment by transfer, payment pending, payment declined.
- A subscription being cancelled, with the refund arithmetic on screen.
- An invitation as the recipient sees it, before and after accepting.
- A form with nothing filled, with one field invalid, with everything valid, and
  after sending.
- The calculator at its default, mid-range, and at both slider ceilings.
- 404 and 500.

**Windows that open on top**, each captured open and in every state it has:

modals · drawers · bottom sheets · the share sheet · toasts and their dismissal ·
tooltips · the language switcher open · the mobile menu open · the plot switcher ·
the lightbox with a photograph open · any confirmation dialog · any date picker ·
any combobox with its list open.

**Interaction states** on the components that carry them: default, hover, focus
visible via keyboard, active, disabled, selected, error. Focus states are
captured by tabbing, not by clicking — a mouse focus ring and a keyboard focus
ring are frequently not the same.

---

## 4. Capture rules — this is where audits fail

Follow these exactly. The failures below are not hypothetical; they are what
went wrong in a previous audit of this same product.

- **Full-page screenshots must have their lazy content loaded.** Scroll the page
  to the bottom, wait for network idle, scroll back, then capture. A previous
  audit produced three full-page shots that were almost entirely blank because
  lazy loading never fired, and nobody noticed until much later.
- **Verify each file after writing it.** Check the byte size and that the image
  is not uniform. A blank or near-uniform capture is a failed capture: retake it
  or record it as failed. Never ship one silently.
- **Never mirror, rotate or post-process.** A previous audit shipped two
  screenshots flipped horizontally, and a reader spent time believing the site
  had a right-to-left bug. Capture raw.
- **Freeze motion.** Disable animations and transitions for the capture run, or
  wait for them to settle. Half-finished animations make useless evidence.
- **Deterministic data.** Same fixtures, same dates, same names, every run. Two
  screenshots that differ only because a date changed are noise.
- **No scrollbars in the frame** and a fixed device pixel ratio — pick one and
  state it.
- **Both framings for every page**: the fold exactly as the viewport shows it,
  and the full page. The fold is where the argument about what a visitor sees
  gets settled.
- **Armenian is captured at the same completeness as English.** If you run out
  of time, cut a viewport, never a locale.

**File naming**, one convention, no exceptions:

```
<route-slug>__<locale>__<width>__<state>.png
pricing__hy__360__default.png
report__en__1440__share-sheet-open.png
form__ru__360__error-phone.png
```

---

## 5. What you produce

An archive, `MemoryCare-site-audit-<date>/`:

```
README.md            what this is, when it was captured, against which build
                     (commit hash), and how to read the rest
INVENTORY.md         the coverage matrix, every cell marked captured or skipped
                     with a reason
FINDINGS.md          every defect, severity-ordered, in the format below
CONTENT.md           every user-facing string found on screen, by route and
                     locale, with any string that has no key in the content
                     specification flagged
ACCESSIBILITY.md     the axe report per route and locale, keyboard walk-through
                     notes, focus order problems, and the contrast pairs you
                     measured on rendered output
PERFORMANCE.md       Lighthouse per route on the mobile profile, load times,
                     bundle size, and where the time goes
GAPS.md              every route and state the specification names that does not
                     exist, and every state you could not reach through the
                     interface
screens/             every capture, named as above
recordings/          short captures of anything that only makes sense in motion:
                     the report opening, the calculator responding, a toast
```

**Finding format**, identical throughout:

```
## <n> — <the defect in one line>
Severity: blocker | major | minor
Where:    <route + locale + viewport>, or <file:line>
Evidence: <screenshot filename, measured number, or command output>
Expected: <the clause, quoted, with its source>
Actual:   <what happens>
```

Severity: **blocker** ships something false, illegal, inaccessible or broken —
an invented claim, a contrast failure, an unreachable screen, a privacy leak.
**Major** — a divergence a user would notice. **Minor** — one only a maintainer
would.

---

## 6. What to check while you are in there

You are capturing anyway, so check these against the specification as you go:

- Contrast on **rendered** pairs, not on token combinations. Measure from the
  screenshots or the computed styles.
- Type floors: nothing under 13px, informational text 14px or more, body 16px on
  mobile.
- Hit areas 44×44 including invisible padding.
- **One script per locale.** The English version contains no Armenian and no
  Cyrillic; the Russian contains no Armenian. The only crossings allowed are the
  dram sign and untranslatable proper nouns.
- The dram sign renders, and `AMD` appears in words wherever the bank requires
  it.
- Prices: 20,000 · 65,000 · 160,000 · 200,000 and the 95,000 first-year figure.
- The two promises — callback within one business day, report within 48 hours —
  identical everywhere they appear.
- No invented proof of any kind: no testimonials, no counts, no years in
  business, no competitor named, no claim of being the only ones.
- No QR code and no memorial page, in any tense.
- The guest report shows no price, no plan and no upsell — and check the network
  payload, not just the screen.
- Legal address and registration number still present as visible placeholders.
- `<html lang>` correct on every locale.

---

## 7. What must not happen

Do not fix anything. Do not edit content. Do not re-run a capture until it looks
better. Do not omit a state because it was hard to reach — record that it was
hard to reach, that is itself a finding. Do not present a screenshot you have
not looked at. Do not mark a check as passing because you did not run it: an
unrun check goes in `INVENTORY.md` as skipped, with the command someone else
should run.

---

## 8. Definition of done

Someone opens the archive, reads `README.md`, and can answer without opening the
site: which pages exist, what each looks like on a phone and on a desktop in all
three languages, which windows can open on top of them, which states have been
seen, what is broken, and what is missing entirely.

And every screenshot in the archive is one you have actually looked at.
