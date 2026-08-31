# Review your own work, polish it, and hand over a deployable project

Run this **after** you have built everything the build brief asked for: the
marketing site, the client portal, all three locales, mobile and desktop, the
content, the tokens, the states.

You are now the reviewer of your own work, and you are not a friendly one. The
purpose of this phase is to find what you got wrong while it is still cheap,
and to leave a project a team of programmers can take over without you.

Two rules govern everything below.

**A finding without evidence is not a finding.** Every claim carries a
reproduction: a file and line, a command and its output, a screenshot at a named
viewport and locale, or a measured number. "This looks off" is not admissible.

**You may not grade yourself on effort.** The only question is whether the built
thing matches the specification and works. Nothing else counts.

---

## 1. Freeze, then measure

Before any review agent runs:

1. Commit everything. Tag it `pre-review`.
2. Run a clean-clone build: fresh directory, `install`, `build`, `start`. If it
   does not come up from a clean clone with the committed lockfile, stop and fix
   that first — everything after this depends on it.
3. Capture the baseline: every route × three locales × `360 / 768 / 1024 / 1440
   / 1920`. Save to `review/baseline/`. These screenshots are the evidence base
   for the whole phase.
4. Run every automated gate the build brief specified and record the raw output
   in `review/gates-before.txt`, failures included. Do not fix anything yet.

---

## 2. The review panel — eight agents, run in parallel

Each agent gets: the specification, the running site, the baseline screenshots,
and its own remit below. Each writes one report to `review/01-…md` … `08-…md`
in the format at §3. **No agent fixes anything.** Reviewing and fixing in the
same pass is how a reviewer talks himself out of a finding.

**1 · Specification conformance.** Walk `FINAL-UX`, `FINAL-UI` and
`FINAL-SYSTEM` clause by clause against the build. Every block of every page in
the order specified; every state that must exist; every measurement — section
padding and the adjacency rule, card padding, radii `0/2/8/full`, the spacing
scale, header 56/72, the rail at 14px, breakpoints. Report every divergence,
including ones you think are improvements. An improvement is still a
divergence: record it and let the owner decide.

**2 · Accessibility and contrast.** Recompute every text-on-surface pair the
build actually renders — not the pairs the tokens permit, the ones on screen —
and assert ≥ 4.5. Verify: Olive carries no text anywhere; error red never sits
on Anthracite; no form sits inside a dark band; hit areas ≥ 44×44 including
padding; visible focus on every interactive element; full keyboard operation
including modals, drawers and the lightbox; correct semantics before ARIA;
`prefers-reduced-motion` honoured. Run axe on every route in every locale and
attach the raw report.

**3 · Locale and typography.** The one most likely to be skipped and most likely
to be broken. Check every route in **Armenian first**, then Russian, then
English, at 360 and 1440. Armenian sets taller and wider: look for clipped
buttons, wrapped navigation, broken cards, truncated labels, text overlapping a
rule. Verify the `:lang(hy)` fallback stack actually resolves and that no
Armenian text falls back to a system font unintentionally. Verify **the dram
symbol renders** in its own element and that the `AMD` word form appears
everywhere the bank requires it. Verify no locale silently shows English where a
translation is missing — a placeholder must be visibly marked.

**4 · Content and compliance.** Diff every rendered string against
`FINAL-CONTENT`. Any string in the build that is not in the specification is a
finding — you are not the copywriter. Then run the prohibitions: no invented
proof of any kind, no testimonial component, no rating field, no counts, no
years in business; no QR code or memorial page in any tense; no competitor named
and no claim of exclusivity; `Optimal` marked "Our recommendation" and never
"Most chosen"; the forbidden-word list clean in all three locales; no
exclamation marks, no emoji; currency always with `AMD` in words; the two
service promises — callback within one business day, report within 48 hours —
identical in every one of their occurrences. Verify the legal address and
registration number still render as **visible** placeholders and were not
quietly dropped. Check the eight Ameriabank requirements each have a real place
in the structure.

**5 · Flows and dead ends.** Walk every journey end to end, clicking: diaspora
buyer, local buyer, and the Los Angeles son buying for his mother in Yerevan.
Then every portal path: first entry after payment, visit list, report, guest
report at a token URL, invitation as the recipient sees it, payment by transfer,
payment pending, card declined, postponed visit, crew could not reach the plot,
guarantee re-visit, profile, cancellation with the refund arithmetic. Every
screen must be reachable and every screen must offer a way onward. Report every
dead end, every state you cannot reach through the interface, and every action
whose result is not confirmed to the user.

**6 · Data, privacy and correctness.** Verify the guest report view is gated
**server-side** and that no price, plan or upsell reaches the client for a guest
— check the network payload, not the DOM. Verify the deceased's name is off by
default and that turning it off removes it from links already issued. Verify a
report link preview carries no photograph of a burial. Verify past reports stay
readable after cancellation. Then the arithmetic: the refund is computed from
the amount actually paid, by visits, rounded up to the nearest 100 ֏ — test the
95,000 case and assert 71,300, and assert that no code path can compute it from
the list price. Verify the credit rule: one credit only, either Inspection or
Express, never both, 60-day window, only at the moment of signing.

**7 · Performance and robustness.** Lighthouse on every route, mobile profile,
throttled. Report anything under 95 for accessibility or best practices, and any
route whose full load exceeds two seconds. Check image formats, dimensions and
lazy loading; check the fonts are subset and preloaded; check there is no layout
shift on the fold. Then break things deliberately: slow network, offline mid
navigation, a report with no photographs, a plot with no visits, a very long
name, a very long cemetery name, a 4G connection from abroad. Nothing may show a
raw error.

**8 · Handover readiness.** Read the project as a programmer who has never met
you and must own it on Monday. Can they install, run, build and deploy from the
README alone? Is every environment variable documented and is nothing secret
committed? Is the Node version pinned and the lockfile present? Is the structure
navigable and are the names honest? Are the fixtures clearly marked as fixtures
with a single seam to a real API? Is there a test they can run to know they
have not broken anything? List every question they would have to ask you.

---

## 3. Report format — identical for all eight

```
## Finding <n> — <one line, the defect, not the symptom>
Severity: blocker | major | minor
Where:    <file:line> or <route + locale + viewport>
Evidence: <command output, measured number, or screenshot path>
Expected: <the clause, quoted, with its source file and section>
Actual:   <what happens>
Fix:      <the specific change; or "owner decision" and why>
```

Severity has one definition and it is not about how annoying it is:

**Blocker** — ships something false, illegal, inaccessible or broken: an
invented claim, a contrast failure, an unreachable screen, a wrong refund, a
privacy leak, a build that does not come up.
**Major** — a real divergence from the specification that a user would notice.
**Minor** — a divergence a user would not notice but a maintainer would.

---

## 4. Cross-review, then reconcile

**Round two.** Each agent reads the other seven reports and writes a short memo:
which findings it disputes and why, which it thinks are misgraded, what all
eight missed, and where two agents are describing the same defect in different
words. An agent that finds nothing to dispute has not read carefully.

**Reconciliation.** Produce one `review/FINDINGS.md`: every surviving finding,
deduplicated, severity settled, ordered blocker → major → minor. Where two
agents disagreed and the evidence does not settle it, keep both positions and
mark it for the owner.

Then, and only then, start fixing.

---

## 5. Fixing — the rules

Fix in severity order. After each fix, re-run the gate that would have caught it
and re-capture the affected screenshots.

**Fix silently:** anything with an unambiguous specification clause behind it.

**Fix and record in `OPEN-QUESTIONS.md`:** anything where you had to choose
between two defensible readings. State both and your reasoning.

**Do not fix — record only:** anything that changes an owner decision, a price,
a promise, a product rule or a piece of content. You may not resolve a
specification conflict by rewriting the specification.

Never "fix" a finding by deleting the test that found it, loosening a
threshold, or hiding an element. If a gate is wrong, say so in writing with the
evidence and leave it failing.

---

## 6. Polish — the things that always rot

After the findings are closed, go over the build once more for the defects that
no gate catches and every real design review finds:

- Cards in a row of unequal height; actions not aligned across a row; a card
  without a badge whose title sits lower than its neighbour's.
- Optical alignment: a heading and the block beneath it starting on different
  vertical rhythms; a rule that does not run to the same edge as the text above.
- Values off the spacing scale that crept in during fixing — re-run the lint.
- Inconsistent capitalisation in labels; two words for the same thing across two
  screens; a button label that differs by one word from the specified one.
- Empty, loading and error states that were built early and never revisited.
- Focus order that jumps, and focus rings clipped by `overflow: hidden`.
- Long-string behaviour: what a 40-character cemetery name does to every card.
- Layer and file hygiene: dead code, unused tokens, commented-out blocks,
  `TODO` without an owner, console output left in.

Re-run the full gate suite and save `review/gates-after.txt`.

---

## 7. Deploy readiness

The project is not done until a programmer can deploy it without you.

- Clean clone → install → build → start, on the pinned Node version, with the
  committed lockfile. Document the exact commands.
- Every environment variable listed in `.env.example` with a description and a
  safe default. **No secret is committed.** Grep the history, not just the tree.
- The site is set to **NOINDEX until it is on the real domain.** Do not ship a
  staging build that search engines can index — that mistake is already in this
  project's history and is one of the things being fixed.
- `robots.txt` and `sitemap.xml` exist and are correct for the target domain,
  and are only permissive once the real domain is live.
- 404 and 500 pages exist, in all three locales, and are styled.
- No third-party analytics and therefore no consent banner — this was an owner
  decision. If you added anything that sets a cookie, remove it or raise it.
- Error handling: no stack trace, no raw message, no `Something went wrong 🙁`
  reaches a user — and remember which screen this is: a photograph of a grave.
- A CI workflow that runs the gate suite on every push.
- Build output verified: bundle size reported, no source maps leaking to
  production unless deliberate, images optimised.

---

## 8. What you hand over

```
README.md              install, run, build, deploy, the substitution note
                       about Gill Sans, and the three open items
ARCHITECTURE.md        routes, data shapes, where the API seam is
CONTENT.md             how strings are keyed and how a translator adds a locale
ACCEPTANCE.md          every gate with the command that proves it, and its
                       current status
DEPLOY.md              environment, hosting, domain, DNS, the NOINDEX rule
DEVELOPER-DECISIONS.md what is deliberately the implementing team's call
OPEN-QUESTIONS.md      every unresolved item, with an owner and a recommendation
review/                FINDINGS.md, the eight reports, the memos, gates-before
                       and gates-after, and the screenshot baselines
```

`README.md` must answer, in its first screen: what this is, how to run it, how
to deploy it, and what is deliberately unfinished.

---

## 9. The final report to the owner

One page, in plain language, no jargon:

- What was built, route by route, and what was not.
- What the review found, by severity, and what was fixed.
- What is deliberately left open and who owns each item — including the legal
  address, the registration number, the Gill Sans licence and the Armenian
  typeface question.
- What could not be verified in this environment and how someone should verify
  it.
- The honest risk list: what will most likely break first in production, and
  why.

Do not write that the project is finished if a blocker is open. Say what is
open, plainly, and let the owner decide.

---

## 10. Definition of done

A programmer who has never spoken to you clones the repository, runs three
commands, sees the site, deploys it to a staging URL, opens it on a phone in
Armenian, and finds nothing to ask you about.

Every gate green. Every finding closed or recorded with an owner. Nothing
invented. Nothing hidden.
