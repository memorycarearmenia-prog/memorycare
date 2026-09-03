# Open questions — 03.09.2026, after the owner's answers

Fifteen questions were put to the owner and answered, plus four that surfaced
while implementing them. **All nineteen answers are in the build.** What is
left below is what genuinely still has no answer.

Nothing in this build is guessed. A sentence that has no fact behind it is
printed as a visible placeholder in square brackets, not invented.

## Still open — the lawyer

| # | What is missing | Where it shows |
|---|---|---|
| 1 | A written opinion on cemetery access rights | `legal.limitations.access.blocked` |
| 2 | The client photograph consent form | `legal.limitations.photo.blocked` — no client photograph is used anywhere until it exists |
| 3 | Retention periods: consultation requests that never became clients, and accounting records | `legal.privacy.retention.blocked` |
| 4 | Whether any age restriction applies to this service | `legal.compliance.ageNote` |
| 5 | Which language version of the terms governs | `legal.governingLanguage` |

## Still open — the bank

| # | What is missing | Where it shows |
|---|---|---|
| 6 | How many business days a refund takes to reach the card. Set by the acquiring terms, not by us. | `legal.refund.how.blocked` |
| 7 | The official colour artwork for Visa, Mastercard, Arca, Google Pay and Apple Pay. The schemes are confirmed and named in the footer already; each row carries its accessible name and gains its mark by dropping a file into `PAYMENT_SCHEMES`. | `build-compliance-pages.py` |

## Still open — content

| # | What is missing | Where it shows |
|---|---|---|
| 8 | `mission`, `values` and `history` are built from strings approved for other pages, so they are true but not written for themselves. They need their own copy in three languages. | those three routes, all locales |

## Held by the owner's own decision

| # | What | Why |
|---|---|---|
| 9 | The comparison FAQ — how we differ from the incumbent. | Held by the owner on 02.09. The condition written against it ("ships the day the liability figure is bound") is now met, since guarantee 2 was settled on 03.09. **It is still held until the owner says otherwise** — a met condition is not permission. |

## Owner actions, outside the code

| # | Action |
|---|---|
| 10 | Update the Ameriabank client form from `hambarcumian@gmail.com` to **info@memorycare.am**. A reviewer compares that field against the domain the acquiring is for. |
| 11 | Enter **memorycare.am** in the state registry's website field, which is empty (`Գրառված չէ`), **before** submitting to the bank. |
| 12 | Ask Mariam to correct the brandbook's colour page to `#A4D6E8`. The owner ruled for the artwork value on 03.09; the twelve delivered files stay as they are. |
| 13 | Ask Mariam whether the **pomegranate** GHEA Mariam draws at U+058F is deliberate — a dingbat parked on the dram codepoint — or a bug. The site no longer uses that font for that character, but anyone else using the font will hit it. |

## Watch this one

**Guarantee 2 has no ceiling.** The owner ruled on 03.09 that we restore
damage our crew causes at our cost, with no cap, and that is what the site
now publishes. A granite monument can cost more than a year's subscription,
and there is no liability policy behind the promise yet. The published
wording is drawn as tightly as the decision allows — we answer for damage we
cause, never for the condition photographed before the work started — but the
exposure is real and it is worth insuring before the pilot.
