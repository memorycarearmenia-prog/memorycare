# What is blocked, and who unblocks it

Everything on this list was found during the rebrand and **cannot be
solved by a designer or a writer.** Each item names the one person who
can close it. Nothing here was invented or guessed around — where a fact
was missing, the copy says so rather than filling the gap.

Ordered by what holds up money.

---

## A. Holds up the bank, and therefore card revenue in October

The path is: site ready → Ameriabank review → acquiring enabled. The bank
**cannot begin reviewing pages that do not exist**, so every week these
stay open is added to the review, not spent in parallel with it.

| # | What is missing | Who | Why it blocks |
|---|---|---|---|
| A1 | **The entity's exact registered spelling.** Three sources give two answers: `Memory Care LLC` (two words) in `CLAUDE.md` and the archive §1; a hedge — "MemoryCare LLC / Memory Care" — in archive §3; and `MemoryCare LLC` (one word) per the 31.08 audit, which calls the live site's two-word form a defect. **Nobody has opened the certificate.** | **Davit**, certificate in hand | A mismatch between the site and the registry is among the most common reasons a submission is returned |
| A2 | **The registration number.** It appears nowhere in this repository. | Davit | Required in the footer of every page |
| A3 | **The legal address, confirmed.** `0051, Komitas 47/1, bldg 9, Yerevan` is recorded but flagged as needing the lawyer's confirmation. The live site prints `0000, Yerevan`. | Lawyer | Same |
| A4 | **How many days after payment the first visit happens.** Decided nowhere. The tariff redesign notes the operational ceiling (~60 new clients per crew per month) and says the promise must respect it, but no number was ever set. It becomes contractual on publication. | **Davit** | Bank condition 8 |
| A5 | **The boundary of "minor repair".** Tasked to the lawyer 22.08, never delivered. Construction work requires municipal permission. Until it exists the site may not name a single repair we will perform. | Lawyer | Bank condition on service descriptions; also a real liability |
| A6 | **A refund rule for a cancelled one-off.** The pro-rata formula is meaningless at one visit — and the Express is exactly what a first card payment buys, so the bank will ask. | Davit + lawyer | Bank condition on refund policy |
| A7 | **Where the photographs are stored.** Hosting provider and country recorded nowhere. HubSpot is a US processor with no stated basis. The developer contract is unsigned and there is no DPA, though he will hold client data, deceased-person data and grave coordinates. | Igor + lawyer | The English privacy policy cannot be written without it |
| A8 | **"Reports stay available forever" collides with the right to deletion.** Two promises from different documents that meet the first time someone exercises the second. | Lawyer | Privacy policy |
| A9 | **Cookies and tracking.** Four CDNs, an unconsented Maps iframe, UTM capture into HubSpot, an EU-resident audience — and a prior ruling of "no third-party analytics, therefore no cookie banner" that the HubSpot capture contradicts. | Decide, then lawyer | Privacy policy |
| A10 | **Nobody in this round read the bank's own document.** Everything is built on a transcription of a screenshot. | Hayk | Open it and check line by line before submitting |

Seven further things the bank will ask for that are in nobody's plan: the
accepted public offer with its logged checkbox, a delivery-method
statement, a named chargeback contact with a response time, card-scheme
marks, an HTTPS and security statement, site-to-registry consistency, and
identical contacts on every page and in every locale.

---

## B. Holds up the copy

| # | What is missing | Who |
|---|---|---|
| B1 | **The product names.** Both the Russian and the English writer independently rejected the cognate set and proposed descriptive names, with the same three arguments: *Express* promises speed, which contradicts "every visit is a full visit"; *Optimal* and *Maximum* imply a quality ladder that does not exist now that all visits are identical; and the visit count **is** the pitch. Two independent native writers converging is strong signal — but renaming diverges the locales and touches the contract, Igor's spec and the financial model. | **Davit** |
| B2 | **The liability figure behind guarantee 2** ("if we damage the monument, we repair it at our cost"). Until it is bound by insurance the guarantee is not published — and the comparison FAQ is held with it, because the checklist would otherwise invite the reader to test the one item we fail. | Lawyer + insurer |
| B3 | **The price of the flowers / candle option.** An explicit owner instruction for the tariffs page, with no price in any source. Designable, not sellable. | Davit |
| B4 | **What the site says about a portal that is not live.** Nobody has ruled. Two prior documents froze two *different* sentences for the same promise, and one of them contains the word "portal" in six places across three languages — promising a screen that will not exist when the first pilot customer looks for it. Proposed: the frozen promise names no channel, delivery is described by its mechanism (a forwardable link, real on day one), the portal is future tense until it is live, and "coming soon" is banned. | Hayk + Igor |

---

## C. Holds up the design

| # | What is missing | Who |
|---|---|---|
| C1 | **Sky blue: `#A4D6E8` or `#D4ECF9`?** The brandbook's colour page prints one and every delivered vector, PNG, JPG and PDF paints the other — and the book's own logo page renders `#A4D6E8`. Built as a one-token swap either way. | **Mariam** |
| C2 | **A font that actually contains ֏ (U+058F).** Verified this session: the dram sign renders in *none* of Source Serif 4, Montserrat, Noto Sans or Noto Serif. The live site already shows it falling back to a system face at a different weight and size from the digits beside it. Until a face is sourced, **no price on this site is typeset.** Montserrat Arm is the likely carrier and is unverified. | Whoever owns fonts |
| C3 | **Favicon and app-icon crops of the medallion** at 16 / 32 / 180 / 512. | Mariam |
| C4 | **Clear-space, minimum-size and misuse pages.** Absent from the brandbook. We now have the first real number for one of them: the medallion still reads at **48px** and closes up below, because the interlace is drawn as filled outlines rather than centrelines. | Mariam |

---

## D. Not blocking, but someone must reconcile

The 26.08 pricing decision was never carried into: the financial model
v6.0, the client contract with the lawyer, Igor's platform spec, and
`FINAL-CONTENT.md` in the earlier design package — which carries a third
price variant of its own. This round corrected `CLAUDE.md` at source;
the rest are not design documents and are not ours to change.

Two audit findings must not be lost now that mobile is out of scope,
because neither is a mobile finding: the nav is unopenable between
**1024 and 1300px** (the most common laptop widths), and pinch-to-zoom is
disabled at every width.
