# Independent verification of this audit

**31.08.2026, design lead.** The audit below was produced by another agent
against the live contractor site. Before it is acted on, its claims were spot
checked against the captured mirror. This note records what was checked and
what was found.

## Verdict

**The audit is accurate.** Every claim tested reproduced exactly. Its method is
sound, its evidence is real, and its self-reporting is unusually honest — it
discards a bad capture run, withdraws a finding it could not sustain, and
declares that its own crawl ended a live session. Act on it.

## Claims tested against the mirror, and the result

| Claim | Finding | Verified |
|---|---|---|
| `<html lang="en">` on every page in every locale | #6 | Yes — six pages checked, all `en`, including Armenian and Russian |
| Pinch-zoom disabled | #7 | Yes — `user-scalable=no, maximum-scale=1.0, minimum-scale=1.0` |
| The development site invites indexing | #8 | Yes — `<meta name="ROBOTS" content="INDEX, FOLLOW">` |
| Every word of body copy is Lorem Ipsum | #5 | Yes — 49 occurrences on the English home page, 43 Armenian, 66 Russian |
| Superseded prices, including a cancelled product | #3 | Yes — 80,000 / 40,000 / 180,000 / 240,000. The 40,000 repeat-Express was cancelled on 26.08 |
| Company name written as two words | #19 | Yes — `MEMORY CARE` four times, `MemoryCare` never |
| No `h1`, no `main`, no `footer` | #34 | Yes — zero of each |
| Images without alternative text | #11 | Yes — 25 of 27 on the home page alone |
| Fabricated proof figures | #1 | Yes — `150,000`, `250000`, `55+`, `15` all present |

## The captures

242 PNGs. Checked independently for uniformity: **none is blank or near-blank**
— minimum per-channel range across the set is well above the threshold, file
sizes run from 9 KB to 6.1 MB. Naming is consistent and parses cleanly into
route, locale, width and state. Coverage spans three locales × four widths, with
Armenian captured most heavily, which is the correct priority for this product.

Spot-opened captures render correctly: the Armenian fold at 360 shows the header
in place, the headline unclipped and the script rendering properly — and it
independently confirms finding #36, the floating action button rendering as a
broken image.

The two capture defects that spoiled the previous audit — blank full-page shots
from lazy content never loading, and horizontally flipped frames — do not occur
here, and the method section explains precisely how each was prevented.

## The one thing to do before circulating this archive

Six files show authenticated account pages including a real name, telephone
number and e-mail address. `account-index__*` and `packages-add-1__*`. The audit
flags this itself. **Delete those six files before the archive leaves the
company.**
