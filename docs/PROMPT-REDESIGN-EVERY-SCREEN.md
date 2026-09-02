# Redesign every screen in the audit archive, to our brand

You are given a complete audit of a live site — **380 screenshots covering
22 routes × 3 locales × 5 viewports, both framings, public and behind the
login** — plus the rendered DOM, the extracted text, the network and
console logs, the accessibility results and the measurements.

Your task: **produce the rebranded version of every one of those screens
and every window that opens on top of them.** UI, UX and content, all
three, for each.

This is a rebrand of a working product, not a redesign competition. The
site functions. People use it. Respect that and improve it.

---

## 0. The owner's rules

1. **Do not touch the functionality.** Nothing is removed, nothing stops
   working, no feature disappears. Every field, every control, every link
   that exists still exists and still does what it did.
2. **Do not move buttons or windows** — unless leaving them where they are
   genuinely harms usability. §3 defines what counts, and it is a short
   list, not a licence.
3. **You do the UI.** Layout, colour, type, spacing, states, the whole
   visual system.
4. **You do the UX.** Flows, hierarchy, labels, errors, empty states, what
   a person understands and in what order.
5. **You do the content.** Real strings, in three languages, from real
   project sources.
6. **Every piece of data must be true and must match the project.** Not
   plausible, not illustrative — true. If you cannot source a fact, you
   mark it and you do not invent it.

---

## 1. What to redesign — the exact inventory

**22 routes.** Twelve public, ten behind the login.

| Public | Behind the login |
|---|---|
| `home` | `acct-dashboard` |
| `contact` | `acct-objects` |
| `login` | `acct-order-1` … `acct-order-4` |
| `register` | `acct-packages` |
| `reset` | `acct-packages-add-broken` |
| `root` | `acct-payments` |
| `notfound-tpl` | `acct-profile` |
| `provoked-404` | |
| `nav-mission`, `nav-values`, `nav-news` | |
| `carousel-reviews` (the component in two states) | |

**Three locales:** `am`, `ru`, `en` — the site's own codes. Each is a
separate deliverable, written natively, not translated.

**Viewports.** The owner has ruled the **desktop web version** as the
scope, so design at **1440** and specify behaviour across **1024 · 1280 ·
1440 · 1920**. The archive's **360** captures are still evidence you must
read, because two defects only appear there — but you are not producing a
mobile design unless the owner tells you otherwise. If you think that is
wrong, say so; do not decide it silently.

**Both framings.** For each screen, show what the first viewport-height
contains and what the whole page contains. What survives the fold is a
design decision, and on several of these screens it is currently an
accident.

**Windows that open on top.** Menus, submenus, the reviews carousel, and
every dialog you add under §3. There is currently **no modal, no drawer,
no toast and no confirmation dialog anywhere on the site** — that is a
finding, not a design constraint.

---

## 2. Read before designing

- `01-FINDINGS.md` — 16 defects, 9 observations, 5 open questions, and 4
  corrections. **Read section D first**: four claims from the previous
  audit were wrong, and if you design from the old ones you will design
  the wrong fix.
- `02-INVENTORY.md` — what was captured and what was not.
- `03-GAPS.md` — what nobody tested. Do not assume those areas are fine.
- `measurements.json` — the type ramp, contrast pairs and focus order,
  per route. Use the measured values, not your reading of a screenshot.
- `dom/` — the rendered markup. **Read the form markup before you redesign
  a form.** Several forms carry hidden fields that must survive.
- `text/` — the extracted strings, so you can see exactly what is on each
  screen today.

---

## 3. When you may move something — the complete list

Rule 2 says do not rearrange. These are the cases where the current
arrangement demonstrably harms the user, each one measured in the audit.
Fix these. Justify anything else in writing before you do it.

1. **`acct-packages` at narrow widths: the Pay button is off the screen.**
   The form sits at `left: 371px` in a 360px viewport; the document is
   452px wide. The table row also overlaps itself. The only way to pay is
   to scroll sideways. This is the clearest case on the site.
2. **`acct-payments` is a dead link.** A sidebar item shown to paying
   customers 404s. Design the screen it should have led to — payments and
   invoices — and keep the nav item.
3. **`acct-order-1..4`: the order form has no visible field at all.** Six
   hidden inputs and a submit button. A customer subscribes to a year of
   grave care without ever saying which grave. **This is the single
   biggest UX hole in the product.** Design the missing step: which plot,
   which cemetery, and the ability to create a plot when none exists —
   `acct-objects` is empty and offers no way to add one.
4. **Nothing can be cancelled anywhere.** No control, no dialog, in any
   locale. Add the cancellation path and its confirmation dialog. The
   refund is pro-rata and the arithmetic is shown before confirming.
5. **`acct-profile`: the password change has no current-password field.**
   Add it. This is functionality being added, which rule 1 permits and
   rule 2 does not restrict.
6. **The 404 template drops the language switcher** on all 19 routes that
   render it — including four of the six menu items.
7. **Submenus open on hover only**, with no keyboard or click path.
8. **Focus states are removed and not replaced.**
9. **No `h1` exists on any page**, and there are 17 distinct font sizes.
   The document outline is not a visual choice.
10. **Contrast failures**: `#888` on `#F5F5F5` = 3.25 and on `#EDEDED` =
    3.03 across the account area; white on `#FF0000` = 4.00 on the Pay
    button, which is also the only red on a site whose palette has none.

Everything else stays where it is. A control you dislike is not a control
that harms the user.

---

## 4. Brand — the only palette permitted

| Name | Hex |
|---|---|
| Dark Olive | `#212212` |
| Olive | `#7C8654` |
| Nude | `#EFE5D5` |
| Ivory white | `#F3F0E9` |
| Sky blue | `#A4D6E8` |

Plus exactly two interface values, and no third:

| Name | Hex | For |
|---|---|---|
| Deep Olive | `#575E3B` | links and accent text on light |
| Error | `#8C3A2E` | validation only |

⚠️ Sky blue is contested — the brandbook's colour page prints `#D4ECF9`,
every delivered export paints `#A4D6E8`. Use `#A4D6E8`; make the swap one
token; do not resolve it yourself.

**No other colour appears anywhere**, including the `#FF0000` Pay button.

### 4.1 Measured contrast — facts

| Pair | Ratio | |
|---|---|---|
| Dark Olive on Nude / Ivory | 12.93 / 14.17 | pass |
| Nude / Ivory on Dark Olive | 12.93 / 14.17 | pass |
| Sky blue on Dark Olive | 10.26 | pass |
| Deep Olive on Nude / Ivory | 5.49 / 6.01 | pass |
| Error on Nude / Ivory | 6.10 / 6.69 | pass |
| **Olive on Nude / Ivory / Dark Olive** | **3.12 / 3.42 / 4.14** | **fails as text** |
| **Sky blue on Nude / Ivory** | **1.26 / 1.38** | **invisible** |
| **Error on Dark Olive** | **2.12** | **invisible** |

Four rules, none negotiable:

1. **Olive never carries text and never receives text.** Fills, rules,
   dividers, decorative panels.
2. **Sky blue is a dark-ground colour.** On light it is a tint fill only —
   a chip ground, a seal disc — never type.
3. **No form that shows validation errors may sit in a dark band.**
4. **Nude is the page ground; Ivory is the objects on it** — cards,
   sheets, inputs, the header bar.

Every ratio you report must be **computed by you**. An asserted number is
a defect.

### 4.2 Type

**Display: GHEA Mariam** — note the capitals; that is the real family
name. **Text: Montserrat.** **Armenian text: Montserrat Arm**, a separate
family, not a subset.

**֏ (U+058F) is present in GHEA Mariam**, verified by reading the font's
cmap, in all four styles. Prices are set in the display face, so **a price
renders the dram sign natively with no fallback.** ֏ inside Montserrat
text — the arithmetic line, the rail, body copy — still needs an isolated
`unicode-range: U+058F` slice, and that slice points at GHEA Mariam.

Floors: body never below 16px; no informational text below 14px anywhere;
uppercase chips and badges never below 14px; every input 16px. Tabular
lining figures wherever a number can change.

The site today resolves **every** text element to `system-ui` and
downloads an unused webfont twice per page. That goes.

### 4.3 The mark

Two open hands in Nude cradling a five-petal forget-me-not in Olive, its
centre a woven medallion in Sky blue. Wordmark **single-colour Olive**.
Tagline Sky blue, uppercase, wide tracking, **no full stop**. The
medallion stops being legible below **48px**. The logo currently on the
site is the retired 27.08 mark — replace it.

---

## 5. Content — true, and from real sources

### 5.1 The pricing, as decided by the owner 26.08.2026

**All visits are full visits.** The light/heavy distinction was rejected;
those words must not appear anywhere, including in a table column.

| Product | Composition | Price |
|---|---|---|
| Զննում | One orientation visit: locate the plot, full written inventory, photo and video of the condition, a list of the work needed, a quote for minor repair. **No cleaning.** | 20,000 ֏ |
| Էքսպրես | One full visit: deep cleaning of the whole plot and every monument — steam, professional neutral-pH chemistry, wet/dry vacuum. **No high-pressure washing on a monument.** | 65,000 ֏ |
| Օպտիմալ | Annual: **4 full visits, one in each season** | 160,000 ֏ / year |
| Մաքսիմում | Annual: **6 full visits** | 200,000 ֏ / year |
| Հատուկ խնամք | Non-standard; always begins with an inspection | calculator |

Credits: the inspection is credited **only on signing an annual
subscription**, within 60 days, never into a single visit. A single visit
is credited in full within 60 days. **One credit only** — either, never
both. **There is no discounted repeat.**

**The site currently shows `40,000 ֏`.** That price was withdrawn by the
owner and the product it names does not exist. It must not appear on any
screen you produce.

Price is flat within **16 m² and two monuments**; beyond that a published
formula, the same for everyone: +10,000 ֏/year per m² over 16, +30,000
֏/year per monument over two. The tariffs page carries a **calculator with
two sliders** that shows its arithmetic.

### 5.2 What is true and worth saying

- A visit does not close until the report holds **eight photographs — four
  angles before and the same four after — two videos, and one GPS point
  recorded at the plot on the day.**
- GPS is **verification**, not location: it answers *was the crew standing
  there*.
- The winter visit runs in a weather window, not on a date, because the
  limit is temperature. **Four visits are guaranteed regardless** — a
  missed winter visit is added to spring. A contract term, not a failure.
- The company was registered in **2026**. The pilot is its first client
  work.

### 5.3 What is on the screens now and must not survive

- **Lorem Ipsum as the English `h1`** — "WHAT IS LOREM IPSUM?" — and the
  same Lorem Ipsum *translated* into Armenian and Russian.
- **Four invented figures**: 150,000 customers, 55+ services, 250,000+
  graves, 15 years of experience. The company has **zero** paying
  customers.
- **Six testimonial slides**, every one named `Անուն Ազգանուն` — literally
  "Name Surname" — with photographs of people, five-star graphics and
  Lorem Ipsum quotes, from Mexico, Russia, Italy, Germany, France and the
  USA.
- **A partners strip of empty placeholder tiles.**

Rule 1 protects functionality, not false statements, and rule 6 requires
true data. **The components stay; the false content does not.** For each,
propose one of: repurpose with true content — the statistics band becomes
the published protocol, whose numbers are real; populate from a real
source; or keep in the codebase behind a flag with a note saying what real
data would fill it. **Get each approved before building.**

### 5.4 Never

`the only` · `the first` · `nobody else` · `unlike others` · `unique` ·
`since 20xx`, in any language. **No competitor named or alluded to.** No
guilt — never "when did you last visit". No "peace of mind". No words put
in a dead person's mouth. No QR code or digital memorial page.

**Write each language natively.** Armenian and Russian that read as
translations of an American landing page are a failure, and the most
likely one.

---

## 6. Screens that need real thought

- **`home`** — the report is the product and the site treats it as a
  feature. What survives the fold should be something checkable: a date, a
  cemetery, a plot, a GPS confirmation.
- **`acct-dashboard`** — the first thing a customer sees after paying.
  Design its **empty state** as carefully as its full one; that is what
  the first real customer meets.
- **`acct-objects`** — empty, with no way to add anything. It is supposed
  to hold the plots.
- **`acct-order-*`** — four order screens with no visible field. §3.3.
- **`notfound-tpl`** — 19 routes render it. It must return **404**, keep
  the language switcher, and help someone who is lost.
- **`nav-mission`, `nav-values`, `nav-news`** — currently the 404
  template. The owner has ruled that pages are not removed, so these get
  **real content**: the company's actual short history, the evidentiary
  standard it sells, and what is done on a visit and what is not.
- **`carousel-reviews`** — it **does** advance; all six slides carry
  identical text and only the photograph changes. Whatever replaces it,
  the mechanism works and need not be rebuilt.

---

## 7. Deliver

For every route × locale:

1. **The redesigned screen**, as a rendered page you can look at, at 1440,
   both framings, plus notes on 1024 / 1280 / 1920.
2. **A before/after pairing** naming the archive file you worked from.
3. **A change list**: what changed, and for anything that moved, which
   §3 item authorised it.
4. **The strings**, in all three languages, each with its source document.
5. **A computed contrast table** for every pair the screen actually
   produces.

Plus, once for the whole set:

6. **The token file**, and a note of any value you derived and by what
   rule.
7. **`NOT-GIVEN.md`** — every fact you could not source, and who must
   supply it.
8. **`QUESTIONS.md`** — what you asked the owner and what was decided.

---

## 8. How this will be judged

1. **Did anything stop working?** A lost field, control or link fails the
   task.
2. **Did anything move without a §3 justification?**
3. **Is every claim on every screen true today?** Not after the pilot —
   today.
4. **Is every colour in §4?** One stray hex fails.
5. **Is every contrast ratio computed rather than asserted?**
6. **Does each locale read as written rather than translated?**
7. **Are the empty states designed?** They are what the first real
   customer sees.

---

## 9. Ask the owner before you start

1. **The false content** — §5.3, item by item. Do not begin until settled.
2. **Mobile.** The scope is desktop, but two defects live only at 360 and
   the archive covers it. Confirm.
3. **The legal entity's registered spelling**, its **registration
   number** — which appears in no project document — and the confirmed
   address. The footer needs all three.
4. **How many days after payment the first visit happens.** Required by
   the bank, decided nowhere, contractual once published.
5. **Product names in English and Russian.** Four of five have never been
   written down.
6. **What may be said about the client portal**, which is not live yet.
7. **Whether any guarantee may be published** — the liability figure is
   still open, and a guarantee without one creates no trust.
