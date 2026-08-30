# MemoryCare — design package v1.0

Marketing site and client portal. English. Produced 29.08.2026 by a team
of five specialists working in two rounds — five independent proposals,
then cross-review and convergence — with a design-lead verification pass
on top.

## Precedence — read this order, and it settles every conflict

1. `LEAD-REVIEW.md` — the verification protocol. Highest authority.
   Recomputed contrast, the conflicts found between documents and how they
   were ruled, the money defect, and what could not be verified.
2. `DECISIONS.md` and `DECISIONS-2.md` — the owner's rulings.
3. `FINAL-UX.md` · `FINAL-UI.md` · `FINAL-CONTENT.md` · `FINAL-SYSTEM.md`
   — the four specifications. Peers; each is the source of truth for its
   own domain.
4. `BRIEF.md` — the shared brief. Historical context. Two errors in it are
   corrected in `LEAD-REVIEW.md` §4.

## The four specifications

| File | Source of truth for | Size |
|---|---|---|
| `FINAL-UX.md` | Sitemap, object and role model, journeys, every screen block by block, every state, permission matrix, forms, calculator, cancellation, responsive rules | ~1,600 lines |
| `FINAL-UI.md` | Visual concept, surfaces, type system, grid, spacing, components in every state, page layouts at 360 and 1440, photography direction | ~1,770 lines |
| `FINAL-CONTENT.md` | Every English string with a stable key, voice and stop-list, all states and system messages, meta tags, character counts against limits | ~3,100 lines |
| `FINAL-SYSTEM.md` | Token architecture, full `tokens.json` and CSS, 52 component specifications, Figma file structure, logo production, handoff inventory, acceptance checklist, developer decisions, open items | ~3,400 lines |

## What is settled, and what is not

Settled by the owner: refund by visits on the amount actually paid; a
subscription year is 12 months from signing; callback within one business
day and report within 48 hours; the deceased's name off by default; one
error colour and no more; the 95,000 ֏ first-year figure shown publicly as
arithmetic and never as a discount; legal entity `MemoryCare LLC`.

Open and owned by someone named: see `FINAL-SYSTEM.md` open items — the
legal address, the registration number, whether Cabin carries the ֏ glyph,
and the rest.

## Two things to act on outside the design work

**The refund formula.** A refund computed from the list price returns more
than a credited client ever paid. `LEAD-REVIEW.md` §5. This belongs to the
lawyer and the platform, not to the designer.

**The stale credit window.** The older pricing table in this repository
still says 30 days. It is 60. Three specialists tripped over it
independently.

## Working files

`working/` holds the five round-one proposals and the five cross-review
memos. Kept because they carry the reasoning behind decisions that will
look arbitrary in six months. Not authoritative — superseded by the four
final specifications.
