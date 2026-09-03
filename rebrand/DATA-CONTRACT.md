# Data contract — what the server fills in

Every string in this build is real, final copy in three languages **except**
the tokens listed here. A token in `{braces}` is a **slot the server fills**,
not unfinished text.

They are confined to the **seven authenticated pages**. **No public page
contains a single one** — verified by grep across all 79 pages. If a `{token}`
ever appears on a public page, that is a bug, not a template.

The tokens survive into the screenshots on purpose. A screenshot showing
`{plot_name}` says *this cell is server data*; a screenshot showing
"Երևանյան գերեզմանատուն, 12/4" would say *this is the copy*, and someone
would ship it as a hard-coded string. Do not "fill them in" to make the
screenshots look finished.

## The slots, by page

| Page | Tokens |
|---|---|
| `account/index.html` | `{fullname}` `{phone}` `{email}` |
| `account/profile.html` | `{fullname}` `{phone}` `{email}` |
| `account/plot-new.html` | `{fullname}` `{phone}` `{email}` |
| `account/plots.html` | + `{plot_name}` `{cemetery}` `{area}` `{monuments}` `{care}` |
| `account/order.html` | + `{customer_id}` `{product_title}` `{p}` `{f}` `{plot_id}` `{location}` `{base}` `{area_surcharge}` `{monument_surcharge}` `{total}` |
| `account/packages.html` | + `{order_id}` `{period}` `{start}` `{start_iso}` `{end}` `{end_iso}` `{done}` `{left}` `{total}` `{paid}` `{result}` `{amount}` |
| `account/payments.html` | + `{date}` `{date_iso}` `{what}` `{amount}` `{loc}` |

`{fullname}` `{phone}` `{email}` appear on all seven because they sit in the
account rail, which is shared.

## Rules that are not optional

**Amounts.** `{base}`, `{area_surcharge}`, `{monument_surcharge}`, `{total}`,
`{amount}` are **display only**. They are rendered into text nodes, never into
a form field, and nothing on the page posts an amount back. The order form's
`<input type="hidden" name="price">` — present on both money forms of the
current site — **is deleted here and must not return.** The server derives the
charge from the product and the plot. Audit A6 / question Q1.

**Paired date tokens.** `{start}`/`{start_iso}`, `{end}`/`{end_iso}`,
`{date}`/`{date_iso}` are the same instant twice: the human form goes in the
text node, the machine form in `<time datetime>`. Locale-format the first;
the second is always `YYYY-MM-DD`. Filling one and not the other produces a
`<time>` element that lies.

**Numeric cells.** Every cell carrying a number has `data-numeric`, which
turns on `tabular-nums` and end-alignment. Amounts are followed by
` ֏ AMD` in the markup, not inside the token — the server sends digits only.

**`{loc}`** is a locale segment in the invoice URL, nothing else. It must
equal the page's own locale. Two endpoints on the current site are hard-coded
to `/am/`, which is how a Russian customer gets Armenian responses at the
moment money moves (audit A5).

**Escaping.** `{fullname}`, `{plot_name}`, `{cemetery}`, `{location}` and
`{what}` carry customer-entered text. HTML-escape at render.

## Two slots that are genuinely undecided

`{p}` and `{f}` on the order form are the preventive/full visit split the
owner **rejected on 26.08** — "all visits are full visits". The words appear
nowhere on any page. What these two fields should carry now that the split is
gone is a data-model decision, not a copy decision, so they are left
server-filled rather than guessed. **Igor: this needs a ruling before the
order form can be wired.**

## Two states per page, one of them inert

Three pages have both a filled and an empty state. Rather than ship two
files per page, **each page renders one state live and keeps the other in an
inert `<template>`** in the same file. Nothing inside a `<template>` is a live
link, a live form or a focusable control, so the page is safe to open as-is.
The server picks one and drops the other.

| Page | Rendered live (and so in the screenshot) | In the `<template>` |
|---|---|---|
| `account/plots.html` | empty — no plot yet | `data-state="populated"` — the table |
| `account/payments.html` | empty — nothing charged | `data-state="populated"` — the table |
| `account/packages.html` | **populated — the orders table** | `data-state="empty"` |

**`packages` is deliberately inverted.** On plots and payments the live state
is what a new customer actually sees on day one. On packages the table is the
screen that has to be reviewable — it is the one carrying the cancel control
the bank requires published, and an empty screenshot would show neither the
control nor the row it belongs to.

`data-state="invalid"` on the login, register, reset, profile, plot-new and
order forms is a different mechanism: it is the error state of a field, not
an empty state of a page.
