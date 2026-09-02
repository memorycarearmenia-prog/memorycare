# What the 02.09 audit overturned in our own work

The audit corrected four claims from the 31.08 archive. I had repeated
three of them as established fact in documents that went to the owner, to
five specialists and into a developer handover. Recorded here so the
record is straight and so nobody rebuilds on them.

## 1. The dram sign does not fall back on the live site

**We said:** ֏ renders at a visibly different weight and size from the
digits beside it, and the live site proves the problem.

**Measured:** wrapping the two runs and measuring them separately gives an
**identical** declared stack, size and weight — both are
`system-ui, -apple-system, "Helvetica Neue", Arial, sans-serif`, 19px,
weight 700, rendered height 22px. The sign is narrower because that is how
the character is drawn. The live site sets everything in `system-ui`, so
the digits and the sign come from the same place.

**Where it went:** `CLAUDE.md`, `build/HANDOVER.md`, the design-system
prompt, the rebrand prompt, and three replies to the owner. Corrected in
all of them.

**What survives:** ֏ is genuinely absent from Montserrat, verified
separately. So the isolated `unicode-range` slice is still required — for
the rebranded site, not because the current one is broken.

## 2. The reviews carousel does advance

**We said:** pressing next produces the same three cards; either it holds
one slide per view with duplicate content, or the control is not wired up.

**Measured:** slide 1 and slide 2 are different files, different hashes,
different sizes. **All six slides carry identical text and only the
photograph changes**, which is what fooled the earlier byte comparison.

This weakened one argument for deleting the carousel. Moot for the rebrand
— the owner has since ruled that nothing may be removed — but the reason
we gave was wrong.

## 3. The testimonial names are placeholders, not invented names

**We said:** photographs of real public figures under invented names,
three of them.

**Measured:** **six** slides, three visible at a time, every one named
`Անուն Ազգանուն` — literally "Name Surname". Countries: Mexico, Russia,
Italy, Germany, France, USA. Photographs at
`/uploads/images/persons/01–07.jpg`, none with an `alt`.

The substantive problem is unchanged and is still a blocker: photographs of
people presented as customers of a company that has none. But "invented
names" was wrong, and it came through two reports without anyone checking.

## 4. Cumulative layout shift is not zero

**We said:** CLS is 0.000, the one thing this build does well.

**Measured:** true on the mobile profile only. **Desktop measures 0.099**,
from `body > div.main` (0.082) and the nav submenu (0.018). We generalised
one profile to the build — and desktop is now the entire scope.

---

## The pattern

Three of the four travelled the same way: stated in one report, repeated in
the next without re-testing, then quoted by me as settled. The fix is not
more caution in prose, it is what this audit did — measure the specific
thing, and say what the measurement cannot decide.

The audit is explicit about that last part too: computed style cannot
identify the physical face that drew a glyph, so it filed the question
open rather than answering it. That is the standard.
