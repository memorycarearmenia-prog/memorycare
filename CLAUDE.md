# Memory Care — website project context

This file is auto-loaded by Claude Code at the start of every session in this
repo. It is the source of truth for brand, pricing, and copy facts. If a file
in this repo (old component, old copy) disagrees with this file, **this file
wins** — flag the mismatch to the user instead of trusting the stale code.

## What this business is

Memory Care LLC (Armenia) — a premium subscription service for cleaning,
monitoring, and light repair of family graves/memorial plots, with verified
photo/video reporting. Plus an add-on: a QR code on the headstone linking to
a digital memory page (gallery + biography + family-only guestbook).

**Primary audience:** Armenian diaspora (US, France, Russia, Europe) — the
core emotional driver is relieving the "guilt of distance." Secondary:
local premium segment in Yerevan.

**Tone:** premium, warm, dignified. NOT somber/funeral-cliché, NOT generic
corporate. Think "quiet trust and craftsmanship," not "grief industry."

## Brand identity (do not deviate without the user's explicit sign-off)

- Name: **MemoryCare** (one word, mixed case — "Memory" + "Care", per the
  live logo asset). Do NOT use "MEMORY CARE" (two words, all caps) —
  that was an earlier/incorrect assumption, corrected by the user
  2026-08-01.
- Slogan (EN, confirmed live copy): "Love Knows No Borders. Care Knows No
  Distance." RU/ARM equivalents: «Память, которая не увядает» / «Рядом с
  родными, сквозь любые расстояния» — reconfirm these are still the
  intended RU/ARM taglines next time it comes up, since the EN one now in
  use on the live site doesn't match either 1:1.
- Symbol: Armenian forget-me-not (Անմոռուկ) line-art flower cradled by two
  open hands. The flower has 5 petals with fine radiating stamens (dot-
  tipped). Behind the flower, a layered swirl of overlapping thin rings
  (spirograph-like arcs), rendered in mixed tones — grey, dark anthracite,
  and olive — not a solid gold sun-crown. See attached reference asset
  (user-provided, 2026-08-01) for exact geometry — do not recreate from
  the old "12-segment gold sun-crown + gold geo-ring" description.
- Colors (corrected by user 2026-08-01 — **do not revert to the old
  Midnight Navy / Antique Gold / Celestial Blue scheme, ever**):
  - **Olive green** — primary accent (buttons, active nav state, "most
    chosen" badge, checkmarks, highlighted headline word)
  - **Light anthracite** — primary text color and dark card/surface fills
    (e.g. the highlighted pricing card uses a near-black anthracite
    background)
  - **Imperfect white** (warm off-white, not pure `#FFFFFF`) — page
    background
  - Exact hex values aren't pinned down yet — pull them from the live
    site's CSS (see below) rather than eyeballing from screenshots when
    precision matters.
- Languages: live site (see below) actually ships a 4-way switcher —
  ARM / ENG / РУС / FRA — one more than the "ARM/ENG/RU" scope stated
  elsewhere in this file. Flagged, not yet reconciled — confirm with the
  user whether FRA is in scope going forward before assuming it everywhere.
  All languages must carry real translated copy, not decoration.
  Mobile-first: diaspora traffic is majority mobile.

**Live reference site:** a version of this site is already deployed at
`memorycarearmenia.netlify.app` (user shared screenshots 2026-08-01) — it
is NOT present in this repo (repo currently only has this CLAUDE.md +
README). It already implements: the corrected name/colors/logo above, the
4-language switcher, hero, pricing cards (matching the locked pricing
table below), a before/after slider, and a "Family stories" section
referencing the 10 completed discovery interviews. Ask the user where
that codebase lives before assuming this repo is the only source — future
work (including the survey one-pager) should match that live site's
actual look, not a from-scratch reinterpretation of the brand.

## Pricing — locked, do not change without explicit instruction

| Tariff | AMD | Visits/yr | Notes |
|---|---|---|---|
| Экспресс (разовый) | 80,000 ֏ | 1 (single heavy visit) | entry/trial |
| Оптимальный | 180,000 ֏ | 6 (2 heavy + 4 light) | **bestseller — mark visually** |
| Максимум | 240,000 ֏ | 12 (4 heavy + 8 light) | premium tier |

Plot-size rule: base covers up to 16 m². Over that: +$20/m² (local
clients) or +$30/m² (diaspora clients).

Currency calculator: AMD/USD/EUR/RUB, interactive (not a static table).
Static reference rates are fine for now (mark "ориентировочно" /
approximate); live FX API is a later upgrade, not required for launch.

## Site sections (already scoped, keep unless user changes it)

1. Hero — emotional offer + GPS/verified-reporting visual
2. Тарифы — 3 tariffs above + multi-currency calculator
3. Галерея «До/После» — before/after slider(s), each with a date + GPS tag
4. Как это работает — subscribe → visits → photo report → (optional) QR memory page
5. Блок доверия — verification, regularity, transparency (diaspora trust signals)
6. Language switcher ARM/ENG/RU
7. Clear CTA to subscribe

## Known open TODOs (do not consider the site launch-ready until closed)

1. Real geo-tagged before/after photos — currently placeholders.
2. Real phone number — currently a placeholder `+374 10 00 00 00`.
3. Professional email on the `memorycare.am` domain (e.g. `info@memorycare.am`)
   — currently a Gmail address, which undercuts the premium positioning.
4. ~~Verify the forget-me-not logo mark against the original brand-brief
   asset~~ — done 2026-08-01, user provided the real logo; description
   above now reflects it. Still worth getting the actual logo file(s)
   (SVG/PNG, all color variants) into the repo rather than relying on a
   text description.
5. Confirm mobile view actually matches the desktop design quality —
   mobile is the primary channel for this audience.
6. Confirm ENG/RU/ARM/FRA copy is real translated content, not
   placeholder/duplicate text — ENG looks real per the live-site
   screenshots (2026-08-01); RU/ARM/FRA not yet verified.
7. Live FX API — nice-to-have, not blocking. Can bundle with the payment/CRM/
   Telegram-bot integration work.

## Things NOT to invent

- Don't invent client testimonials, review counts, or "X families trust us"
  stats — the company is pre-launch (pilot paused, 10 discovery interviews
  done, no live customers yet). Use aspirational/process-trust copy instead
  ("verified visits," "GPS-tagged reports"), not fabricated social proof.
- Don't add pricing tiers, discounts, or visit counts beyond the table above
  without the user confirming it first.
