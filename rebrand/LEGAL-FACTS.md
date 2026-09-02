# Verified legal facts — from the official documents, 02.09.2026

Two independent official sources, read directly:

- **State registry extract**, `ՊԵՏԱԿԱՆ ՄԻԱՍՆԱԿԱՆ ԳՐԱՆՑԱՄԱՏՅԱՆԻՑ ՔԱՂՎԱԾՔ`,
  issued 2026-08-05 14:29, verification code `RB4E-CA76-23D4-FFB2`
  (checkable at verify.e-gov.am).
- **Ameriabank client information form** for legal entities,
  `11RBD/12CIB FO 72-01-02, Ed. 14`.

They agree on every company fact.

---

## The registered name — and it is neither of the two we were arguing about

> ### «ՄԵՄՈՐԻՔԵՅՐ» ՍՊԸ

Registered in **Armenian letters**. `ՄԵՄՈՐԻՔԵՅՐ` is the Armenian rendering
of *MemoryCare* — **one word**, no space. `ՍՊԸ` is
`Սահմանափակ պատասխանատվությամբ ընկերություն` — a limited liability
company.

**There is no registered Latin spelling at all.** Ameriabank's own form
prints the Armenian name in both its Armenian and its English column,
because that is the only name the registry holds.

So the long-running argument — `Memory Care LLC` versus `MemoryCare LLC` —
had a false premise. **Neither is the registered name.** The audit's
FINDINGS #19 was closer than this repository was: the one-word form is
right, and the two-word `Memory Care LLC` that stood in `CLAUDE.md` and in
`PROJECT-MEMORY-FULL.md` §1 was wrong.

**RULED by the owner, 02.09.2026:**

| Locale | Prints |
|---|---|
| **hy** | `«ՄԵՄՈՐԻՔԵՅՐ» ՍՊԸ` — the registered name, verbatim |
| **en** | `MemoryCare LLC` |
| **ru** | `ООО «МемориКейр»` |

Because neither the English nor the Russian form is what the registry
holds, **every locale also carries the registered Armenian name in full**
via `common.entity.registeredName` — "registered in the state register as
«ՄԵՄՈՐԻՔԵՅՐ» ՍՊԸ". That is what a bank reviewer cross-checks, and it costs
one line.

Note on the Russian: written with guillemets, `ООО «МемориКейр»`, per
Russian legal convention and mirroring the Armenian registered form, which
also uses them. The owner wrote it without; if the bare form is wanted it
is one value in `ru.json`.

## Identifiers

| | |
|---|---|
| **Registration number** | **999.110.1600788** |
| **TIN / ՀՎՀՀ** | **08330546** |
| Unique identifier (ՁԿԴ) | 56882100 |
| Registration date | **2026-08-05** |
| Term | indefinite (`Անժամկետ`) |
| Status | no dissolution or cessation recorded |
| Country | Armenia |
| Charter capital | 5,000 ֏ |
| Economic activity code | **96.09.0** — other personal service activities n.e.c. |
| Registry website field | **`Գրառված չէ`** — not recorded |

## Two addresses, and they are different

The registry and the bank form both distinguish them, and we had the wrong
one on file.

| | |
|---|---|
| **Legal address** | Հայաստան, Երևան, Արաբկիր, Կոմիտասի Պ., **Շ 47**, Բն. 9, **0051** |
| **Business address** | Հայաստան, Երևան, Արաբկիր, Կոմիտասի Պ., **Շ 47/1**, Բն. 9 |

In Latin: **Komitas Ave. 47, apt 9, 0051, Arabkir, Yerevan, Armenia**
(legal) and **Komitas Ave. 47/1, apt 9** (business).

This repository recorded `0051, Komitas 47/1, bldg 9` — that is the
**business** address, not the legal one, and it was carried as though it
were the registered address.

⚠️ Both are **apartments**. Publishing a residential address on a public
website is a real choice, not a formality — it is already public in the
registry, but putting it in the footer of every page is a different level
of exposure. The bank requires an address (§4.10.2); it does not require
it to be a home. → owner.

## Contacts, and a mismatch worth fixing before submission

| | |
|---|---|
| Phone on file with the bank | **+374 55 315 323** |
| E-mail on file with the bank | **hambarcumian@gmail.com** |
| E-mail the site will print | `info@memorycare.am` |

⚠️ **The bank holds a Gmail address for this company.** The site will
print a domain address on the same domain the acquiring is for. A reviewer
comparing the two will see a mismatch. Update the bank's record, or expect
the question. → owner.

## Director and owner

**ԴԱՎԻԹ ՀԱՄԲԱՐՁՈՒՄՅԱՆ** — sole executive and **100 % shareholder**.

That is all of it that belongs in this repository. The source documents
also contain his passport number, public services number, date of birth
and residential address. **None of that is recorded here, must not appear
in any deliverable, and must not be committed anywhere.** The PDFs
themselves are deliberately not added to the repository for the same
reason.

---

## What this closes

| Blocker | Status |
|---|---|
| Exact registered spelling of the entity | **closed** — `«ՄԵՄՈՐԻՔԵՅՐ» ՍՊԸ` |
| Registration number | **closed** — 999.110.1600788 |
| TIN | **closed** — 08330546 |
| Confirmed legal address | **closed** — Komitas 47, apt 9, 0051 |
| What the EN and RU footers print | **closed** — see the table above |
| Which address the site publishes | **closed** — the **legal** one, ruled by the owner |

## What it opens

1. The Gmail-versus-domain mismatch on the bank's record. The bank holds
   `hambarcumian@gmail.com`; the site will print `info@memorycare.am` on
   the very domain the acquiring is for.
2. The registry's website field is empty (`Գրառված չէ`). If the bank
   cross-checks it against the acquiring domain, fill it in first.
3. The published address is an apartment. The owner has ruled to publish
   the legal one, which is what the bank needs — recorded here only so
   nobody is surprised later that a home address is in the footer of every
   page.
