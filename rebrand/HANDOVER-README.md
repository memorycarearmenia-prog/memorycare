# MemoryCare — rebrand handover
### 03.09.2026 · for Igor

Everything here comes from one source. The pages are real HTML that runs,
the screenshots are photographs of those pages taken by a browser, and the
CSS is generated from one token file. Nothing in this archive was drawn by
hand to look like something it isn't.

**Open `01-site/en/index.html` through a local web server, not by
double-clicking it.** The pages use root-relative asset paths (`/assets/…`),
which is correct for production and resolves to your filesystem root over
`file://` — every page then renders unstyled. From inside `01-site/`:

```
python3 -m http.server 8000     →  http://localhost:8000/en/index.html
```

---

## What is in here

| Folder | What it is |
|---|---|
| `01-site/` | **79 HTML pages** — 26 routes × 3 locales, plus the root. Runnable. This is the deliverable; the Figma file is the design record. |
| `01-site-generators/` | The Python that writes those pages from the string files. Re-run them and they reproduce `01-site/` byte for byte. |
| `02-screenshots/` | **870 PNGs.** 26 routes × 3 locales × 5 widths × 2 framings, plus both states of the three two-state account pages. `manifest.json` maps every route to its files. |
| `03-design-system/` | `tokens.source.json` is the only place a value is typed. `build-tokens.py` emits `tokens.css` and `tokens.json` together, so the CSS and the JSON cannot drift. `tools/` holds the checkers. |
| `04-content/` | `en/ru/am.json`, **765 keys each**, verified for parity and for empty values. `TRUTH.md` records what each claim rests on. |
| `05-documents/` | The brief, the owner's decisions, the registry facts, the data contract, the bank compliance mapping, the font notes. |

## Read these three first

1. **`05-documents/DATA-CONTRACT.md`** — the `{token}` slots on the seven
   account pages, what fills them, and the rules that are not optional. Two
   matter most: **the hidden `price` field is deleted and must not come
   back**, and **`visits` must be re-derived on the server** from the chosen
   product, with a mismatch rejected. Both are the same rule — a hidden field
   is browser-controlled and decides money.
2. **`03-design-system/SYSTEM.md`** — how the three token layers work and
   which colours may carry text. Two rules decide most visual questions:
   Olive never carries text and never receives it; Sky blue is a dark-ground
   colour and may only be a tint fill on light.
3. **`05-documents/BRIEF.md`** — the ten measured defects in the current
   build and what each fix is.

## What the screenshots are for

They are not decoration. Each one is a browser capture of the page beside
it in `01-site/`, at a named width, verified for size and pixel variance
before it was kept. If a screenshot and the HTML disagree, the HTML is
right and the screenshot is stale — regenerate with
`02-screenshots/shoot.py`.

Naming: `route__locale__width__framing.png`. `default-fold` is the first
screenful at that width; `default-full` is the whole scrolling page.
`state-populated` / `state-empty` are the second state of a page that has
two.

## Three things to know before you start

**`am` is the URL segment; the language is `hy`.** The build serves `/am/`
and names its files `am.json`, which is fine as a path. But `am` is the ISO
code for **Amharic** — Armenian is `hy`. Every `lang`, `hreflang`,
`Content-Language` and `:lang()` in this build says `hy`. Keep it that way.

**Prices carry a real dram sign.** `֏` is U+058F. It is served by
`mc-dram.woff2`, a 716-byte slice cut from Noto Sans Armenian whose
`unicode-range` is that one character, and **`"MC Dram"` leads every font
stack**. Do not reorder the stacks: GHEA Mariam maps U+058F and draws a
**pomegranate** there, so if it wins the character every price on the site
shows a piece of fruit. This shipped in our own build until 03.09 and was
found by looking at a rendered glyph — reading the font's character map says
the codepoint is present, which is exactly what made it invisible.

**Seven placeholders remain, on purpose.** A sentence with no fact behind it
is printed in square brackets rather than invented. They are all with the
lawyer or the bank, and they are listed with their owners in
`06-OPEN-QUESTIONS.md`. Do not fill them with plausible text.
