# 05 — VERIFICATION: what I re-checked myself, and what it changed

The archive in this directory arrived already written up (`00`–`04`). I did not take it on trust.
This file records what I re-derived from the raw evidence, what survived, what I am **adding**, and
what must **not** be cited the way it looks like it can be.

The project rule this follows is in `CLAUDE.md`: *when a check passes, ask what it would have said
if the thing were broken.* Every number below was recomputed or re-read from `dom/`, `text/`,
`measurements.json`, `console/` and the screenshots — never from `01-FINDINGS.md`.

---

## 1. Personal data — verified independently, clean

Before anything was copied into the repository I searched the whole extracted archive myself.

| Check | Result |
|---|---|
| Any Armenian mobile pattern (`0XXXXXXXX`, `+374…`) | only `090000002` (the substitute) and `+37410000000` (the site's own published placeholder) |
| Any e-mail | only `garik-user@example.am` (substitute) and `info@memorycare.am` (public) |
| Any coordinate pair in Armenia's range | only `40.000000,44.000000` (substitute), 42 occurrences |
| Substitutions actually present | `SUBSTITUTED NAME 02` 41 files · `SUBSTITUTED NOTE` 16 · substitute phone 40 · substitute e-mail 40 |

No real name, number, address or coordinate is in this directory. The claim in `04-PERSONAL-DATA.md`
holds.

### ⚠️ But the substitution has a hole, and it would matter on a real account

**The cemetery names were not substituted.** `text/acct-objects__am.txt` carries
`Դավթաշենի գերեզմանոց` and `Աբովյանի հիմնական գերեզմանոց` in clear, and the screenshots show them.

The GPS coordinates were replaced precisely because they locate a family's graves — and then the
**named burial ground was left in**, which locates them almost as well. On this seeded account it is
harmless. On a real customer's account, surname plus named cemetery is enough for a stranger to find
the plot, which is the exact disclosure the coordinate substitution exists to prevent.

**Rule for the next pass: the object's cemetery / burial-ground name joins the substitution table.**

---

## 2. Findings I re-derived and confirm

| Finding | How I checked it | Verdict |
|---|---|---|
| **A2** — reports 2 and 4 have `?q=,` | read the `maps.google.com/maps?q=` string out of each of the three report DOMs | **confirmed.** report 1 carries coordinates; 2 and 4 carry `q=,` |
| **A4** — amount in a hidden field on the pay form | `dom/acct-mypackages__am.html`: `name="price" value="40000"` and `value="240000"` inside `<form id="package-pay">` | **confirmed** |
| **A5** — banned vocabulary live | `Լիարժեք` / `Պրոֆիլակտիկ` present in text and legible on screen | **confirmed** |
| **A3** — contrast 1.99 / 1.75 / 1.38 | recomputed WCAG relative luminance from the raw RGB triples, and checked those triples occur in `measurements.json` | **confirmed to the second decimal** |
| **A6/A7/A9** — no `alt`, no `h1`, no `main`, no `<label>` | counted tags per file | **confirmed**: reports carry 14 `<img>`, **0** with `alt`; `h1`=0, `main`=0, `label`=0 on every authenticated route |
| **A1** — report title is an `<h3>` | `<h3>Հաշվետվություն՝ N4`, and the only other `h3`s are the footer's | **confirmed** |

Nothing in `01-FINDINGS.md` had to be withdrawn.

---

## 3. What must NOT be cited from the screenshots

### ⚠️ The blank grey map boxes are a capture artefact, not the defect

On `acct-objects` and every report the map is a **blank grey rectangle** in the PNGs. It is tempting
— and wrong — to point at that as proof of A2.

`console/` shows **`ERR_TUNNEL_CONNECTION_FAILED` on all six pages**: the capture sandbox has no
route to `maps.google.com`, so **no map on any page loaded, including the one whose coordinates are
fine.** The screenshots cannot distinguish a broken map from a blocked one.

**A2 rests on the DOM alone** — the literal string `?q=,` in reports 2 and 4 against real
coordinates in report 1. That evidence is solid. The picture is not evidence, and anyone who
"confirms" the finding from the picture has confirmed nothing.

### ⚠️ The dram sign is correct in the markup — do not report it as wrong

On screen the price reads `40000 Դ`, which looks like the Armenian letter *Da* substituted for the
dram sign. It is not. I read the codepoint: it is **U+058F ARMENIAN DRAM SIGN**, correct.

It *renders* that way because the site resolves everything to `system-ui` (finding A15 of the
02.09 pass) and this capture ran on Linux. On the customer's Windows machine it will look different
again.

This is the third time a dram-sign claim in this project has come from looking at a shape instead of
reading the character, and the first two were both wrong. Cost of the check: one line of Python.

---

## 4. Findings I am ADDING — not in `01-FINDINGS.md`

### A11 (new) — The second Pay button is dead. The 240,000 ֏ package cannot be paid for.
Severity: **major — this is uncollected money**

**Where:** `/{am,ru,en}/account/mypackages/`

**Evidence.** The page renders **two** pay forms and both carry the same DOM id:

```html
<form id="package-pay"> <input type="hidden" name="id" value="14">
  <input type="hidden" name="price" value="40000">  … <button class="npaid">Վճարել</button>
  <p id="pay_res"></p> </form>
<form id="package-pay"> <input type="hidden" name="id" value="11">
  <input type="hidden" name="price" value="240000"> … <button class="npaid">Վճարել</button>
  <p id="pay_res"></p> </form>
```

Two elements share `id="package-pay"`, and two more share `id="pay_res"`. The handler, `js/init.js`
line 504:

```js
const package_pay = document.querySelector('#package-pay');
if (package_pay) { package_pay.addEventListener('submit', async (event) => { event.preventDefault(); … }
```

`querySelector` returns **the first match only**. So the submit listener is attached to the 40,000
form and to nothing else.

**Actual.** The second form has no `action`, no `method`, and its `<button>` has no `type` — so it
defaults to submit. Pressing *Վճարել* on the 240,000 package therefore performs a **native GET to
the current URL**: the page reloads with the fields in the query string, no payment request is made,
and no error is shown. The customer presses Pay, the page blinks, nothing happens. Twice more and
they telephone.

`document.getElementById("pay_res")` has the same defect, so even the first form's response message
can only ever land in the first paragraph.

Verified identical in all three locales (2 forms, 2 buttons, 2 `pay_res` in each).

**Note this compounds A4.** The two questions are different and both are open: A4 asks whether the
server trusts the browser's price; A11 says the more expensive of the two Pay buttons never reaches
the server at all.

### A12 (new) — It is not one withdrawn price. The whole superseded tariff model is live in the account.
Severity: **major**

`01-FINDINGS.md` A5 flags the `40,000 ֏` as withdrawn. That understates it. The screen carries:

| Shown | Composition shown | Status against `CLAUDE.md` |
|---|---|---|
| `Փաթեթ 2` — **40,000 ֏** | Preventive 0 / Full 1 | withdrawn repeat Express (rejected 26.08) |
| `Փաթեթ 4` — **240,000 ֏** | Preventive 8 / Full 4 | **old table** — current Maximum is **200,000 ֏, 6 visits** |
| `Փաթեթ 3` — **180,000 ֏** | Preventive 4 / Full 2 | **old table** — current Optimal is **160,000 ֏, 4 visits** |

`60,000 / 180,000 / 240,000` with a light-visit/heavy-visit split is precisely the pre-26.08
line-up that `CLAUDE.md` records as superseded. **Every price and every visit count on a paying
customer's own billing screen is from the retired product model** — not one stale figure but the
whole of it, including the split the product model forbids by name.

Also: the packages are labelled `Փաթեթ 2 / 3 / 4` — "Package 2" — never `Օպտիմալ` or `Մաքսիմում`.
The customer cannot tell which tariff they bought.

### A13 (new) — The report text is not localized. Armenian appears verbatim in the English report.
Severity: **major**

`text/acct-report-1__en.txt` — the **English** page — renders its body in Armenian, byte-identical
to `acct-report-1__am.txt`. The chrome around it translates correctly (`Report: N1`, `Preventive`,
`My objects`); the report body does not, because it is one stored free-text field served to every
locale.

This is not a placeholder problem that disappears when the Lorem Ipsum is replaced — it is the
shape of the data. **A visit note written by the crew in Armenian will be shown untranslated to a
diaspora customer in Los Angeles**, who is the primary audience and the reason three locales exist.
The report is the product; its only human sentence is the one that cannot be read.

Needs a decision, not just a fix: per-locale note fields, or a stated policy that notes are written
in the customer's language at entry.

---

## 5. Status of the numbers

Everything quoted in `00`–`04` that I tested reproduced. The three additions above are mine and are
evidenced in this file. The two cautions in §3 are limits on how the existing evidence may be used,
not corrections to it.

**Untested and still open**, unchanged from `01-FINDINGS.md` §C: whether the server re-derives the
price (Q2 — needs staging), whether `objects/view/:id/` enforces ownership (Q1 — needs a second
account), and why reports 2 and 4 have no coordinates (Q3 — needs the admin side).
