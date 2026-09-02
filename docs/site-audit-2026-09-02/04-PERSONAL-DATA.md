# 04 — PERSONAL DATA

## What this archive contains

**No real personal data, anywhere.**

The account used for the authenticated half of this audit belongs to a real person and its pages
display a real name, telephone number and e-mail address in the header block of every screen behind
the login. Those three values were **substituted at the moment the pages were fetched**, before
anything was written to disk, so no unredacted copy of them was ever created — not in `screens/`,
not in `dom/`, not in `text/`, not in `network/`, and not in any intermediate file.

Substitution was chosen over blurring deliberately, per §10: blurring destroys the layout evidence
that these screens exist to provide, and a blur applied after the fact means an unredacted original
existed at some point. The replacements preserve approximate string length so wrapping and
truncation behaviour stay faithful.

| Real value | Replaced throughout with | Length change |
|---|---|---|
| the account holder's full name | `SUBSTITUTED NAME 01` | 19 → 19 characters |
| the account holder's mobile number | `+37400000001` | 12 → 12 characters |
| the account holder's e-mail address | `user@example.am` | 14 → 15 characters |

**Verification.** After extraction, the whole archive was searched for each of the three real
values. All three searches returned nothing. The substituted name appears in **24 files** — the
eight authenticated route templates × three locales — which matches the number of pages that carry
the account header. The commands are reproducible:

```
grep -rl "<the real surname>"  archive/     # → no matches
grep -rl "<the real number>"   archive/     # → no matches
grep -rl "<the real address>"  archive/     # → no matches
grep -rl "SUBSTITUTED NAME 01" archive/ | wc -l   # → 24
```

## Files that show substituted content

Every file whose name begins with `acct-` in `screens/`, and the corresponding entries in `dom/`,
`text/` and `measurements.json`. That is **120 screenshots** and 36 DOM/text pairs. The manifest
marks each of them; `mirror-manifest.json` carries a `sanitised: true` flag per page.

These files are **safe to circulate**. They show the real layout with placeholder content, and the
manifest says so, which is what §10 asks for when redaction would destroy the evidence.

## What was deliberately not captured

- **No payment card, security code, session token or authorization header** appears anywhere. No
  URL containing a token was captured; the session cookie was never read, written down or
  transmitted anywhere.
- **The credentials themselves** were never written to any file, filename, note, log or commit
  message, and were never typed into any form by me — the account owner performed the sign-in
  himself. They do, however, appear in the chat transcript where they were pasted, which is outside
  this archive and outside my control. **They should be treated as disclosed and rotated.**
- **No photographs of a family's grave exist in this account.** `/{loc}/account/objects/`
  ("My objects") is empty — 152 characters of text, all of it header and footer chrome — so the
  category of sensitive data §10 warned about is simply not present. If a real customer's account
  is ever audited, that will not be true, and the substitution approach used here will need to be
  extended to images.

## Identifiers that were kept, and why

Two numeric identifiers remain in the archive:

- **`5`** — the account holder's user id, in the path `/account/personal-edit/5/`.
- **`13`** — an order id, in a hidden field on the packages page.

Both are retained because they are the evidence for finding Q2 (a user id exposed in a URL) and A6
(client-supplied order fields). Neither identifies a person once the name, phone and e-mail are
substituted, and removing them would remove the finding.

## One thing to be aware of before sharing

Nothing in this archive needs redacting before circulation. The only sensitive artefact produced
during this audit lives outside it: the password in the chat transcript.
