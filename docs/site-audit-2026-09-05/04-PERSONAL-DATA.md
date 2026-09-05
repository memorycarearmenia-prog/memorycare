# 04 — PERSONAL DATA

## What this archive contains

**No real personal data.** The garik account (user id 4) is a real, populated account whose visit
reports and objects list carry a name, phone, e-mail, **precise GPS coordinates of family graves**,
and free-text notes naming deceased relatives. Every one of those was **substituted at fetch time,
before anything was written to disk** — no unredacted copy was ever created, in `screens/`, `dom/`,
`text/`, `network/`, or any intermediate file.

Substitution over blur, per §10: blurring destroys layout evidence and implies an unredacted
original existed. Replacements keep approximate length so wrapping stays faithful.

| Real value (category) | Replaced with |
|---|---|
| account holder full name | `SUBSTITUTED NAME 02` |
| account holder phone | `090000002` |
| account holder e-mail | `garik-user@example.am` |
| grave GPS coordinates (several, in map iframe `?q=lat,lng`) | `40.000000,44.000000` |
| free-text notes naming deceased relatives | `SUBSTITUTED NOTE` |

**Verification (reproducible):**
```
grep -rl "<real surname>"   archive/   → no matches
grep -rl "<real phone>"     archive/   → no matches
grep -rl "<real e-mail>"    archive/   → no matches
grep -rlE "<real grave coordinates>"                archive/  → no matches
grep -rl "SUBSTITUTED NAME 02" archive/ | wc -l  → 33 pages carry the placeholder
```
All four real-value searches returned nothing; the substituted name appears on the 33 authenticated
pages that carry the account header. `mirror-manifest.json` flags each sanitised page.

## The grave photographs are demo placeholders, not this family's

The before/after images on every report resolve to `/uploads/images/ba/01/before.*` and `after.*` —
the **same files as the public home page's before/after slider** — and the report video is the
public demo clip `/uploads/files/video/v.mp4`. Report bodies are Lorem Ipsum. So the sensitive
category §10 warned about most — real photographs of a real family's grave — **is not present in
this account**. Every `acct-*` and `acct-report-*` file is therefore safe to circulate: it shows the
real layout with placeholder people and demo media. If a genuine customer account is ever audited,
this will not hold, and the substitution must extend to the uploaded image and video files.

## Deliberately not captured

- **No payment card, security code, session token or authorization header** anywhere; no URL
  containing a token. The session cookie was never read or written down.
- **The credentials** (`garik@… (login redacted)` / password) were never written to any file or typed by me —
  the owner signed in himself. They are in the chat transcript, outside this archive: **treat both
  the garik and the earlier david password as disclosed and rotate them.**
- **Another user's report** — the IDOR probe returned only booleans/status (all 503); no other
  account's data was read into the record. See FINDINGS Q1.

## Identifiers kept, and why

Object/report ids (1, 2, 4) and package ids (11, 14) remain — they are the evidence for A2, A4 and
Q1, and identify no person once name/phone/e-mail/GPS are substituted.
