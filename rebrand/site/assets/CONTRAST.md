# CONTRAST — every pair this system can produce

**Every ratio on this page was computed, not quoted.** `tools/check-contrast.py`
reads the hex values out of `tokens.source.json`, follows each semantic token
through its aliases, flattens every `rgb(… / α)` against the ground it is
actually painted on, and applies the WCAG 2.1 relative-luminance formula. No
number here was copied from the brief, the brandbook or a previous report.

Reproduce it:

```
python3 tools/check-contrast.py            # the table
python3 tools/check-contrast.py --assert   # exit 1 if a shipped pair fails
```

Thresholds: **4.5** for body text (1.4.3), **3.0** for large text and for
meaningful non-text graphics — borders, focus rings, dividers (1.4.11), and
**no floor** for a disabled control, which 1.4.3 exempts.

Two things about this table that are not true of most contrast tables:

1. **Composited values are flattened first.** `--mc-text-secondary` is Dark
   Olive at 72% alpha. Its ratio is not the ratio of `#212212`; it is the ratio
   of `#5B5949`, which is what a browser paints on Nude. The script does that
   arithmetic. A swatch-level check would have reported 12.93 here and been
   wrong by a factor of two.
2. **The failures are listed too**, with the mechanism that prevents each one
   from reaching a screen. A colour system is only as good as the pairs it
   makes impossible.

---

## Part 1 — the pairs the system ships

| Scope | Where | Foreground | Background | Ratio | Need | Verdict | Note |
|---|---|---|---|---:|---:|---|---|
| light | page | `text-primary` #212212 | `color-nude` #EFE5D5 | **12.93** | 4.5 | pass | Body copy, every heading. |
| light | page | `text-secondary` #5B5949 | `color-nude` #EFE5D5 | **5.67** | 4.5 | pass | Metadata, captions, helper text. |
| light | page | `text-accent` #575E3B | `color-nude` #EFE5D5 | **5.49** | 4.5 | pass | Links and accent text. |
| light | page | `text-link` #575E3B | `color-nude` #EFE5D5 | **5.49** | 4.5 | pass | Same value; underlined as well as coloured. |
| light | page | `text-link-hover` #212212 | `color-nude` #EFE5D5 | **12.93** | 4.5 | pass | Hover goes darker, not lighter. |
| light | page | `text-error` #8C3A2E | `color-nude` #EFE5D5 | **6.10** | 4.5 | pass | Validation message outside a card. |
| light | page | `text-muted` #7C7868 | `color-nude` #EFE5D5 | **3.55** | n/a | — | DISABLED labels only. 1.4.3 exempts inactive controls. |
| light | page | `border-control` #7C7868 | `color-nude` #EFE5D5 | **3.55** | 3.0 | pass | Input boundary. Non-text, 1.4.11. |
| light | page | `border-focus` #575E3B | `color-nude` #EFE5D5 | **5.49** | 3.0 | pass | Focus ring. Non-text, 1.4.11. |
| light | page | `decor-olive-rule` #7C8654 | `color-nude` #EFE5D5 | **3.12** | 3.0 | pass | A divider that carries meaning. |
| light | object | `text-primary` #212212 | `color-ivory` #F3F0E9 | **14.17** | 4.5 | pass | Card and report-sheet copy. |
| light | object | `text-secondary` #5C5C4E | `color-ivory` #F3F0E9 | **5.96** | 4.5 | pass |  |
| light | object | `text-accent` #575E3B | `color-ivory` #F3F0E9 | **6.01** | 4.5 | pass |  |
| light | object | `text-link-hover` #212212 | `color-ivory` #F3F0E9 | **14.17** | 4.5 | pass |  |
| light | object | `text-error` #8C3A2E | `color-ivory` #F3F0E9 | **6.69** | 4.5 | pass | Field-level error inside a form card. |
| light | object | `text-muted` #7D7D71 | `color-ivory` #F3F0E9 | **3.66** | n/a | — | Disabled only. |
| light | object | `border-control` #7D7D71 | `color-ivory` #F3F0E9 | **3.66** | 3.0 | pass | Input boundary, the usual case. |
| light | object | `border-focus` #575E3B | `color-ivory` #F3F0E9 | **6.01** | 3.0 | pass |  |
| light | object | `decor-olive-rule` #7C8654 | `color-ivory` #F3F0E9 | **3.42** | 3.0 | pass | The rule inside a tariff card. |
| light | primary btn | `text-on-action` #F3F0E9 | `color-dark-olive` #212212 | **14.17** | 4.5 | pass | Ivory label on the Dark Olive fill. |
| light | primary btn hover | `text-on-action` #F3F0E9 | `color-deep-olive` #575E3B | **6.01** | 4.5 | pass | The fill lightens on hover; the label must still hold. |
| light | sky chip | `text-primary` #212212 | `color-sky` #A4D6E8 | **10.26** | 4.5 | pass | Dark Olive on the Sky TINT. This is the only way Sky appears on a light page. |
| light | sky chip | `border-focus` #575E3B | `color-sky` #A4D6E8 | **4.35** | 3.0 | pass | The ring survives on a Sky-tinted chip. |
| light | error panel | `text-primary` #212212 | `wash-error@color-ivory` #EBE1DA | **12.53** | 4.5 | pass | The error-summary panel's own copy. |
| light | error panel | `text-error` #8C3A2E | `wash-error@color-ivory` #EBE1DA | **5.91** | 4.5 | pass | The red heading on its own wash. |
| light | well | `text-primary` #212212 | `ink-a08@color-ivory` #E2E0D8 | **12.20** | 4.5 | pass | Striped table row, calculator readout. |
| dark | band | `color-nude` #EFE5D5 | `color-dark-olive` #212212 | **12.93** | 4.5 | pass | text-primary in the dark scope. |
| dark | band | `color-ivory` #F3F0E9 | `color-dark-olive` #212212 | **14.17** | 4.5 | pass | text-secondary in the dark scope. |
| dark | band | `color-sky` #A4D6E8 | `color-dark-olive` #212212 | **10.26** | 4.5 | pass | text-accent and text-link. THIS is Sky's job. |
| dark | band | `paper-a48` #868579 | `color-dark-olive` #212212 | **4.33** | n/a | — | text-muted, disabled only. |
| dark | band | `paper-a48` #868579 | `color-dark-olive` #212212 | **4.33** | 3.0 | pass | border-control, as a non-text boundary. |
| dark | band | `color-sky` #A4D6E8 | `color-dark-olive` #212212 | **10.26** | 3.0 | pass | border-focus, as a non-text ring. |
| dark | band | `color-olive` #7C8654 | `color-dark-olive` #212212 | **4.14** | 3.0 | pass | decor-olive-rule on dark. Graphic only. |
| dark | raised card | `color-nude` #EFE5D5 | `paper-a06@color-dark-olive` #2E2E1F | **11.03** | 4.5 | pass | Copy on the raised card in the band. |
| dark | raised card | `color-sky` #A4D6E8 | `paper-a06@color-dark-olive` #2E2E1F | **8.75** | 4.5 | pass |  |
| dark | primary btn | `color-dark-olive` #212212 | `color-nude` #EFE5D5 | **12.93** | 4.5 | pass | Dark Olive label on the Nude fill. |
| dark | primary btn hover | `color-dark-olive` #212212 | `color-ivory` #F3F0E9 | **14.17** | 4.5 | pass |  |

Nothing above is marginal. The lowest text ratio in the whole system is **5.49**
(Deep Olive links on Nude), a full point above the 4.5 requirement; the lowest
non-text ratio is **3.12** (an Olive divider on Nude), against 3.0. The tightest
one is worth naming: **an Olive rule on the page ground has 0.12 of headroom.**
It holds, and it is the reason Olive is allowed to be a divider at all — but if
anyone ever proposes nudging Olive lighter, that is the number that breaks
first, before anything anyone would notice by eye.

---

## Part 2 — the pairs the system must never produce

These are the reasons the four structural rules exist. Each row is a real
combination someone could type; each is prevented by a specific mechanism, named
in the last column and specified in full in `SYSTEM.md` §5.

| Foreground | Background | Ratio | Rule and why it is forbidden |
|---|---|---|---|
| `color-olive` #7C8654 | `color-nude` #EFE5D5 | **3.12** | Rule 1. Olive as text on the page. |
| `color-olive` #7C8654 | `color-ivory` #F3F0E9 | **3.42** | Rule 1. Olive as text on a card. |
| `color-olive` #7C8654 | `color-dark-olive` #212212 | **4.14** | Rule 1. Olive as text in the dark band — clears AA-large only, which is why the wordmark is allowed to be art and body text is not. |
| `color-olive` #7C8654 | `color-sky` #A4D6E8 | **2.48** | Rule 1. Olive as text on a Sky chip. |
| `color-dark-olive` #212212 | `color-olive` #7C8654 | **4.14** | Rule 1 again, from the other side: Olive never RECEIVES text either. |
| `color-ivory` #F3F0E9 | `color-olive` #7C8654 | **3.42** | Rule 1. A light label on an Olive fill. |
| `color-sky` #A4D6E8 | `color-nude` #EFE5D5 | **1.26** | Rule 2. Sky as type on the page ground. |
| `color-sky` #A4D6E8 | `color-ivory` #F3F0E9 | **1.38** | Rule 2. Sky as type on a card. |
| `color-error` #8C3A2E | `color-dark-olive` #212212 | **2.12** | Rule 3. A validation message inside a dark band. |
| `color-deep-olive` #575E3B | `color-dark-olive` #212212 | **2.36** | Deep Olive is a light-ground colour only. |
| `color-nude` #EFE5D5 | `color-ivory` #F3F0E9 | **1.10** | Rule 4. Ground colour used as an object, or the reverse — the two are 1.10 apart and invisible against each other. |

### Where each is structurally prevented

**Olive as text or behind text — 3.12 / 3.42 / 4.14 / 2.48.**
There is no token that produces it. Olive exists in the semantic layer only as
`--mc-decor-olive-fill` and `--mc-decor-olive-rule`, in a namespace defined as
*paint that never has a foreground*. `color: var(--mc-decor-…)` is a sentence
that reads wrong before it is linted, and `tools/check-tokens.sh` §3 rejects it
anyway — with one whitelisted exception, `li::marker`, which accepts no property
but `color` and is a graphic rather than text at 3.12/3.42.

The 4.14 row deserves a note because it is the one people argue about. Olive on
Dark Olive clears AA-large (3.0) and fails AA (4.5). That is exactly why the
wordmark, set large in Olive on the dark lock-up, is legitimate art and why a
paragraph in the same two colours is not. The system draws the line at the token
layer rather than at a size, because a token cannot be resized by accident.

**Sky as type on light — 1.26 on Nude, 1.38 on Ivory.**
Effectively invisible: a 1.26 ratio is a coloured smear, not text. Prevented by
scope rather than by discipline. `--mc-text-accent-on-dark` is defined **only**
inside `.band--dark`. In `:root` and in `.band--light` it is deliberately
pointed at a custom property that does not exist:

```css
--mc-text-accent-on-dark: var(--mc-__SKY-BLUE-IS-1-POINT-2-6-ON-NUDE--USE-text-accent-OR-decor-sky-tint);
```

An unresolvable `var()` is *invalid at computed-value time*. For an inherited
property such as `color` that means the declaration is dropped and the element
keeps the inherited value — Dark Olive on a light page. So the failure mode of
using Sky as type on light is **legible dark text**, plus a guard name printed
in DevTools that says what went wrong and what to use instead. It is not a
warning nobody reads; it is a value nobody can get.

Sky still appears on light, as `--mc-decor-sky-tint` — a fill. Dark Olive on
that tint measures **10.26**, which is how a Sky chip carries a label. The label
is Dark Olive. Sky is the ground.

**Error red inside a dark band — 2.12.**
The same guard, in the other direction, and it is the one place where I disagree
with how this was written down before. The previous token pass carried the
comment *"Deliberately NOT defined here"* over an empty space in `.band--dark`.
That does not work: **custom properties inherit.** Not redeclaring
`--mc-text-feedback-error` in the dark scope left the `:root` value visible to
every descendant, so an error message inside a dark band would have rendered in
`#8C3A2E` at 2.12 — precisely the outcome the comment believed it had prevented.

Here the dark scope redeclares all three error tokens as guards:

```css
--mc-text-error:        var(--mc-__ERROR-RED-IS-INVISIBLE-ON-DARK-OLIVE-2-POINT-1-2--MOVE-THIS-FORM-OUT-OF-THE-BAND);
--mc-border-error:      var(--mc-__ERROR-RED-IS-INVISIBLE-…);
--mc-surface-error-wash:var(--mc-__ERROR-WASH-IS-A-LIGHT-GROUND-VALUE--…);
```

`color` falls back to inherited Nude (12.93), `border-color` to `currentColor`,
`background-color` to `transparent`. The message is readable, visibly wrong, and
`components.css` §6 adds a dashed outline around any `.mc-form-error` that finds
itself inside `.band--dark`, so it is caught in a screenshot as well as in a
lint.

**Deep Olive on the dark band — 2.36.** Same class of problem, no separate
guard needed: `--mc-text-accent` is redeclared in `.band--dark` as Sky, so the
token that would carry Deep Olive there simply holds a different value. Deep
Olive is never named directly outside the token file.

**Nude and Ivory against each other — 1.10.** These two are 1.10 apart, which is
to say indistinguishable. The failure they cause is not unreadable text; it is a
card that silently stops looking like a card. Prevented by the semantic split —
`--mc-surface-ground` and `--mc-surface-object`, never the primitives — and by
`tools/check-tokens.sh` §6, which rejects `var(--mc-color-nude)` and
`var(--mc-color-ivory)` in component code outside a short, named whitelist.

---

## Part 3 — corrections

**The brief's numbers are right.** I recomputed all fifteen ratios quoted in
`rebrand/BRIEF.md` from the hex values and every one agrees to the second
decimal: 12.93 · 14.17 · 12.93 · 14.17 · 10.26 · 5.49 · 6.01 · 6.10 · 6.69 ·
3.12 · 3.42 · 4.14 · 1.26 · 1.38 · 2.12. Nothing to correct.

**`CLAUDE.md`'s contrast table is not.** It is computed against `#D4ECF9`, the
brandbook colour page's Sky, rather than `#A4D6E8`, the Sky every delivered file
actually paints and the one the brief adopts. Three of its rows are therefore
wrong for the artwork that exists:

| Pair | `CLAUDE.md` (`#D4ECF9`) | Working value (`#A4D6E8`) | Effect of the difference |
|---|---|---|---|
| Sky on Dark Olive | 13.18 | **10.26** | Both pass; no consequence. |
| Sky on Nude | 1.02 | **1.26** | Both invisible; no consequence. |
| Sky on Ivory | 1.07 | **1.38** | Both invisible; no consequence. |
| Olive on Sky | 3.18 | **2.48** | **This one matters.** Against the printed hex, an Olive rule on a Sky panel clears the 3.0 a meaningful graphic needs. Against the real artwork it does not. Nobody should draw an Olive divider inside a Sky-tinted panel, and on the strength of `CLAUDE.md`'s table somebody would have. |

The system does not depend on any of these — Sky never carries type on light,
and no component puts Olive on Sky — but the table should be recomputed when the
`#D4ECF9` / `#A4D6E8` question goes back to Mariam.

**One number in the earlier token pass was optimistic.** Its `--mc-border-strong`
comment records that the alpha version of the control border "measured 3.01
against a 3:1 requirement", and it therefore introduced a solid `#737060` to get
to 3.99. 3.01 is a pass by 0.01, which is a rounding artefact rather than a
margin. The replacement here is Dark Olive at 56% — `#7C7868` on Nude,
`#7D7D71` on Ivory — measuring **3.55** and **3.66**, with real headroom and
without adding a colour to the palette.
