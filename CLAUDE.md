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

- Name: **MEMORY CARE**
- Slogan: «Память, которая не увядает» / «Рядом с родными, сквозь любые расстояния»
- Symbol: Armenian forget-me-not (Անմոռուկ) — 5 velvet-purple petals, 5
  light-lilac inner rays, 12-segment gold sun-crown at center, thin gold
  geo-ring around the outside. Fine line-art style.
- Colors: Midnight Navy `#0A111F` · Antique Gold `#D4AF37` / `#E6CA65` ·
  Celestial Blue `#4A90E2`
- Languages: ARM / ENG / RU switcher — all three must carry real translated
  copy, not decoration. Mobile-first: diaspora traffic is majority mobile.

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
4. Verify the forget-me-not logo mark against the original brand-brief asset
   (5 petals / 5 inner rays / 12-segment crown) rather than a from-scratch
   recreation — ask the user for the original logo file if one exists.
5. Confirm mobile view actually matches the desktop design quality —
   mobile is the primary channel for this audience.
6. Confirm ENG/RU copy is real translated content, not placeholder/duplicate
   Armenian text.
7. Live FX API — nice-to-have, not blocking. Can bundle with the payment/CRM/
   Telegram-bot integration work.

## Things NOT to invent

- Don't invent client testimonials, review counts, or "X families trust us"
  stats — the company is pre-launch (pilot paused, 10 discovery interviews
  done, no live customers yet). Use aspirational/process-trust copy instead
  ("verified visits," "GPS-tagged reports"), not fabricated social proof.
- Don't add pricing tiers, discounts, or visit counts beyond the table above
  without the user confirming it first.
