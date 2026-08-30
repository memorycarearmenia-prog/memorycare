# MemoryCare — design brief for the site and client portal

**All deliverables are in ENGLISH.** The site will later be localised to
Armenian and Russian, but every screen, label and document we produce now
is English.

---

## 1. The business

Memory Care LLC, Yerevan, Armenia. A subscription service for the
professional care of family memorial plots in Yerevan cemeteries. The
client subscribes for a year, our crew visits on a schedule, and after
every visit the client receives a report: before/after photographs, video
and GPS confirmation that the crew was on their specific plot.

**The single most important fact about this business:** we do not sell
cleaning. We sell proof. The report IS the product. A client opens it six
to nine times a year, forwards it to a brother or an aunt, and judges the
whole company by it.

**Stage:** pre-launch. Zero paying customers. First crew day early
September, first paying clients the second week of September, client
portal built by an external developer, ready ~20 September.

## 2. Audiences — two, one site

**Armenian diaspora** — USA, France, Russia, Europe. 35–60. Established.
Cannot travel to Yerevan. Emotional driver: guilt about distance. Reads
on a phone, often late at night, from a different time zone. Pays from
abroad to a company they have never met, so every trust signal counts.

**Local premium segment** — Yerevan, 40–60, above-average income. Could
go themselves; has no time. Rational driver.

Do **not** split the site into a diaspora version and a local version.
One page serves both. Do not write diaspora-only copy ("across the
miles", "cheaper than flying yourself"). Lead with the outcome, then name
both reasons naturally.

**Mobile-first is not a preference, it is the primary channel.**

## 3. Tone

Light premium minimalism. Air, large typography, restrained editorial
elegance. Warm but professional.

Explicitly NOT: funeral cliché (no dominant black, crosses, gothic
lettering, candles, black borders around photos), not guilt-pressure, not
sentimental, not cold corporate.

Reference feel: tending.app, headspace.com, stripe.com, airbnb.com.

## 4. Brand — official, from the designer's brandbook

### Colour

| Name | HEX | CMYK | Role |
|---|---|---|---|
| Olive | `#7C8654` | 52/34/78/12 | Decorative fills, petals, tagline, dividers. **Never carries text.** |
| Nude | `#EFE5D5` | 6/8/15/0 | Light surface |
| Ivory white | `#F3F0E9` | 3/3/7/0 | Light text on dark; secondary light surface |
| Anthracite | `#33373C` | 74/64/57/52 | Dark surface, body text |
| **Deep Olive** | `#575E3B` | ~7/0/37/63 | **Interface only.** Links, accent text, primary button fill |

Deep Olive is a working value adopted by the owner: same 72° hue and 23%
saturation as Olive, lightness 30% instead of 43%. It exists because
Olive fails contrast everywhere.

**Measured contrast — this is not negotiable, the audience is 40–60 and
reads on a phone:**

| Pair | Ratio | AA 4.5 |
|---|---|---|
| Anthracite on Nude | 9.61 | pass |
| Anthracite on Ivory | 10.53 | pass |
| Nude on Anthracite | 9.61 | pass |
| Deep Olive on Nude | 5.49 | pass |
| Deep Olive on Ivory | 6.01 | pass |
| Ivory on Deep Olive | 6.01 | pass |
| White on Deep Olive | 6.84 | pass |
| **Olive on Nude** | 3.12 | FAIL |
| **Olive on Ivory** | 3.42 | FAIL |
| **Olive on Anthracite** | 3.08 | FAIL |
| **Ivory on Olive** | 3.42 | FAIL |
| Deep Olive on Anthracite | 1.75 | never use |

**Usage split. Do not invent a sixth colour.**
- Light ground (Nude / Ivory): body text Anthracite; links and accent
  text Deep Olive; primary button = Deep Olive fill, Ivory label.
- Dark ground (Anthracite): text Nude or Ivory; primary button = Nude
  fill, Anthracite label (9.61).
- Olive: fills, petals, tagline, dividers, decorative panels only.

Nude and Ivory differ by only 1.1 — near identical to the eye. Assign
each a fixed job and write it down.

### Type

- **Display: Gloock Regular.** Google Fonts, free, available in Figma.
  Single weight only — plan the hierarchy around that constraint.
- **Text: Gill Sans in the brandbook, but it is commercial Monotype and
  cannot be used in the web or in Figma.** Owner decided: substitute a
  free humanist grotesque of similar character. Design-lead pick:
  **Cabin** — its design brief is explicitly a humanist sans in the
  Gill Sans / Johnston tradition, and it is on Google Fonts. Alternate
  candidate: **Lato**. Every mock and document must label this as a
  substitute for Gill Sans, not as the brand face.

### Logo

Five-petal forget-me-not (Անմոռուկ), woven interlaced medallion at the
centre, held between two open hands. Wordmark "MemoryCare" —
**two-colour**: "Memory" in Ivory white, "Care" in Olive. Tagline below
in Olive small caps: `HONORING MEMORY, CARING FOR LOVED ONES` — **no full
stop**.

Vector available: 9 SVGs — primary logo (vertical lock-up), logo mark,
wordmark, each in color / dark / light.

Two known defects, work around them:
1. The colour mark's hands are Ivory on a Nude ground — they vanish.
   The colour version goes on Anthracite or pure white only.
2. Every SVG sits in a 1080×1080 square with large asymmetric padding.
   Specs must state crop or use a tightly-bounded export.
3. **There is no horizontal lock-up.** For a site header this matters —
   propose how the header handles it.

Name is always **MemoryCare**, one word, two capitals. Never
"Memory Care", "MEMORYCARE", "MC". Legal entity: MemoryCare LLC.

## 5. Products — the approved lineup (26.08.2026)

All prices AMD, identical for local and diaspora clients. Tiers 1–4 cover
a plot **up to 16 m² and up to 2 monuments**.

| Product | Price | What it is |
|---|---|---|
| **Զննում / Inspection** | 20,000 ֏ | One assessment visit: we locate the plot, full written record of its condition, photo and video report, list of recommended work with prices. **No cleaning is performed.** |
| **Express** | 65,000 ֏ | One full visit: deep cleaning of the whole plot and monuments — steam, pressure washer, vacuum, professional chemistry. Report, portal access. |
| **Optimal** | 160,000 ֏/yr | **4 full visits, one per season.** The leading choice. |
| **Maximum** | 200,000 ֏/yr | **6 full visits.** |
| **Special** | by calculator | Non-standard cases: more visits, larger plot, more monuments, several family plots. **Entry is always through Inspection.** |

**Rules that must be visible in the UI:**
- There is no such thing as a "light" or "preventive" visit any more.
  Every visit is a full visit. Never write "2 full + 4 preventive".
- Never use the word "monthly" for any tier.
- Never use the word "bestseller". Mark Optimal as the leading choice
  visually or with wording like "most chosen".
- Inspection is shown **apart** from the three annual subscriptions — it
  is a one-off, and must read as one.
- Currency in words as well as the symbol: "AMD" / "֏". Bank requirement.

**Credit mechanics — implement exactly:**
- On signing an annual subscription the client is credited **one** of the
  one-off services already paid for: **either Inspection (20,000) or
  Express (65,000). Not both.** A client who did both gets the larger.
- Window: **60 days** from paying for the one-off.
- The credit only fires **at the moment the annual subscription is
  signed**. There is no credit between one-off products: Inspection does
  not credit into Express.
- No discounted repeat Express. The price is always 65,000.

**Plot calculator — a required block:**
- Two sliders: plot area and number of monuments.
- Annual surcharge: **+10,000 ֏/year per m² above 16** and
  **+30,000 ֏/year per monument above 2.** Flat, same for Optimal and
  Maximum.
- One-off Express surcharge: **+2,500 ֏/m²** and **+7,500 ֏/monument.**
- Slider ceiling: 100 m² and 10 monuments; beyond that the calculator
  offers a consultation and routes to Inspection.
- The price must be visible before any phone call. This removes the
  diaspora fear of "a different price for the American".

**MemoryCare Guarantees — a required public block:**
- Free repeat visit within 7 days if the client is unhappy with a report.
- Liability for damage.
- Pro-rata refund on cancelling a subscription.

We have no reviews and no history. Guarantees are the only currency of
trust we have, and the customer panel confirmed they are what closed
the sale.

## 6. The primary action is a consultation request, not a payment

The annual sum is large enough that the decision happens after a
conversation. Primary CTA everywhere: **request a free consultation** —
three fields, name, phone or email, cemetery or city. No registration.

"Pay online" is a secondary button, and card acquiring is not live yet,
so the first clients pay by bank transfer. Both paths must exist.

Phone fields must accept **international formats** — clients hold US and
French numbers.

## 7. Site structure

1. Home — proof on the first screen (a report with GPS), then how it
   works, family circle, trust, footer with contacts.
2. Pricing — five products, Inspection set apart, calculator, guarantees.
3. How it works — subscribe, visits, photo/video/GPS report.
4. Sample report — the actual product, give it real weight.
5. Family Circle — relatives get their own sub-accounts by invitation,
   see all reports, can order one-off services. This is our only true
   differentiator and it is currently absent from the live site.
6. About the company — a bank requirement, and diaspora clients check it.
7. Contacts.
8. Four legal pages: privacy policy, refund policy, terms of service,
   service limitations.

**Bank requirements (Ameriabank, hard condition for card acceptance) —
every one of these needs a place in the structure:** About section,
contacts in every footer, full service descriptions, legal restrictions,
real prices in AMD, English privacy policy, refund policy, terms of
service.

## 8. Client portal — in scope

Screens: first entry after payment (no visits yet — the moment of
maximum doubt, "what did I pay for"), visit list, report screen, family
circle and invitation, payment, profile.

Portal rules that must be designed, not left to the developer:
- **Permission matrix for Family Circle** — who views reports, who orders
  one-off services, who changes the subscription, who invites others.
  Do not give everyone identical access; the whole value is in the
  distinction.
- **Report sharing by plain link** into WhatsApp or Viber, with no login.
  Part of the older audience will never open a portal.
- **Guest view of a report** for someone without an account — roughly
  half of all opens. **No prices and no upsell:** selling next to a photo
  of a grave is the single worst thing this brand can do.
- **Link preview rule:** a photograph of a burial must never appear in
  the OG preview. Mark, "Visit report", date only. The link is opened in
  a family group chat.
- **Report block order:** start with a calm confirmation that the visit
  happened — date, plot, status — photographs below. Before/after side by
  side as the opening image reads as cleaning-product advertising and is
  the wrong register.
- **Bad news screens:** visit postponed by weather, crew could not access
  the plot, client requests the guarantee re-visit. Nobody designs these
  and we will meet them in week one.
- **Empty, loading and error states** on every screen. An error on a
  screen showing a photograph of a grave cannot say "Something went
  wrong 🙁".
- **Cancellation with pro-rata refund** must be completable without
  phoning us. The bank requires it too.
- Visit reminder the day before is **opt-in** and can be directed to a
  different person — a relative in Yerevan who will meet the crew.

## 9. Content rules — hard constraints

- **Invent nothing.** No testimonials, no review counts, no "trusted by N
  families", no years-in-business, no client numbers. The company is
  pre-launch with zero paying customers. The live site currently carries
  fabricated figures and stock-photo testimonials with a recognisable
  actor's face — that is exactly what we are replacing.
- Use process trust instead: verified visits, GPS-tagged reports, named
  guarantees, described equipment and method.
- **Never mention a QR code on the headstone or a digital memory page.**
  That is Year-2 scope and does not exist. Not even as "coming soon".
- Do not promise a delivery date we have not agreed.
- Photography: no real before/after images exist yet. Use neutral
  placeholders in brand colours, each labelled with what will go there
  after the September shoot, and the exact aspect ratio and crop.
- Legal address: not yet supplied. Use a clearly-marked placeholder and
  list it as an open item for the developer.

**Real contacts, use these:**
Hayk Manukyan, CBDO — +374 93 154 108
Davit Hambardzumyan, CEO — +374 55 315 323
info@memorycare.am
Domain will be memorycare.am. The current site lives on the contractor's
domain mc.makyan.com, which is temporary.

## 10. Competitive position — be accurate

hush.am has operated in Yerevan since about 2015: a burial-records
database, GPS grave location, a one-year package of four visits with
before/after photo reports, an app on Google Play, roughly 72 reviews, a
US phone number aimed at the Los Angeles diaspora.

So: **never claim that nobody does grave care with photo reports in
Yerevan.** That is false and checkable. Our position is the full
combination — photo + video + GPS + portal + family circle — plus
verification rigour and a premium brand. No competitor combines all five.

In English, "memory care" is semantically owned by the dementia-care
industry. Any headline or meta description must disambiguate: pair the
name with what we actually do.

## 11. What the current site gets wrong — do not repeat

Menu built as a corporate brochure: History, Mission, Values, News. Five
of those pages return 404. A person deciding at 1 a.m. whether to trust
us with their mother's grave will not read our mission.

Hero sells nothing: a heading, a paragraph and two buttons, "Learn more"
and "Register". A picture of our own emblem occupies the hero.

"Order" on a tariff jumps straight to a login form with no explanation.

Fabricated statistics and stock-photo testimonials.

Nothing about the product itself: no report example, no GPS, no team, no
equipment, no family circle.

No sign of a real company for someone paying from abroad: placeholder
phone, placeholder address, dead social links, no legal pages.
