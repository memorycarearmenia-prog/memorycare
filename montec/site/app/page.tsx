import Link from 'next/link'
import { EmbossField } from '@/components/EmbossField'
import { Body, Cta, Eyebrow, H2, Lead, Plate, Section } from '@/components/Bits'
import { products, indexOf, BATCH, total } from '@/lib/products'

const featured = ['the-founder', 'the-executive', 'the-closer'].map(
  (s) => products.find((p) => p.slug === s)!
)

export default function Home() {
  return (
    <>
      {/* ── Hero: the mark, revealed by light ─────────────────────────── */}
      <section className="relative flex min-h-[88vh] items-center overflow-hidden">
        <EmbossField src="/products/the-founder/emboss.webp" />

        <div className="relative mx-auto w-full max-w-[1180px] px-6 py-28 md:px-10">
          <Eyebrow>
            Batch {BATCH} · {total} artifacts
          </Eyebrow>

          <h1 className="mt-7 max-w-[16ch] font-serif text-[46px] font-normal leading-[1.04] md:text-[76px]">
            Quiet is the loudest luxury.
          </h1>

          <p className="mt-8 max-w-[46ch] text-[16px] leading-[1.75] text-paper/70">
            Full-grain vegetable-tanned Italian calfskin, cut and finished in Armenia. The mark is
            pressed into the leather and never printed — you find it with light, not colour.
          </p>

          <div className="mt-11 flex flex-wrap items-center gap-4">
            <Cta href="/collection/">See the batch</Cta>
            <Cta href="/request/" tone="outline">
              Request access
            </Cta>
          </div>

          <p className="pointer-hint mt-10 text-[12px] uppercase tracking-wide2 text-paper/35">
            Move across the leather to find the mark
          </p>
        </div>
      </section>

      {/* ── Position ──────────────────────────────────────────────────── */}
      <Section>
        <div className="grid gap-14 md:grid-cols-[1.15fr_1fr] md:gap-20">
          <div>
            <Eyebrow>The idea</Eyebrow>
            <H2 className="mt-6">Earned, not advertised.</H2>
            <Body className="mt-7">
              Montec is for people who have nothing to prove and everything to protect: their time,
              their reputation, their word. The logo is small. The leather is the loudest thing in
              the room, and it never raises its voice.
            </Body>
            <Body className="mt-5">
              We are not affordable luxury. We are <span className="text-brass">earned</span> luxury
              — the world&rsquo;s finest materials, made at home, offered to those who ask.
            </Body>
          </div>

          <div className="self-end">
            <dl className="rule divide-y divide-brass/15 border-brass/25 pt-9">
              {[
                ['Quiet', 'Restraint over spectacle. We remove before we add.'],
                ['Permanent', 'Made to outlast the trend, and probably its owner.'],
                ['Ours', 'Armenian craft, carried with pride at home and abroad.'],
              ].map(([term, def]) => (
                <div key={term} className="grid grid-cols-[7rem_1fr] gap-6 py-5">
                  <dt className="font-serif text-[20px] text-brass">{term}</dt>
                  <dd className="text-[14px] leading-relaxed text-paper/65">{def}</dd>
                </div>
              ))}
            </dl>
          </div>
        </div>
      </Section>

      {/* ── Featured pieces ───────────────────────────────────────────── */}
      <Section className="!pt-0">
        <div className="flex items-end justify-between gap-8">
          <div>
            <Eyebrow>Batch {BATCH}</Eyebrow>
            <H2 className="mt-6">Three of thirteen.</H2>
          </div>
          <Link
            href="/collection/"
            className="hidden shrink-0 text-[12px] uppercase tracking-wide2 text-brass hover:text-brass-soft md:block"
          >
            The full batch →
          </Link>
        </div>

        <div className="mt-14 grid gap-8 md:grid-cols-3">
          {featured.map((p) => (
            <Link key={p.slug} href={`/collection/${p.slug}/`} className="group block">
              <Plate
                src={`/products/${p.slug}/three-quarter.webp`}
                alt={`${p.name} — ${p.object}`}
                className="aspect-[4/3] transition-opacity duration-500 ease-quiet group-hover:opacity-90"
              />
              <div className="mt-5 flex items-baseline justify-between gap-4">
                <span className="font-serif text-[22px]">{p.name}</span>
                <span className="text-[11px] uppercase tracking-wide2 text-paper/35">
                  {indexOf(p.slug)} / {total}
                </span>
              </div>
              <p className="mt-1.5 font-serif text-[15px] italic text-brass/80">{p.line}</p>
              <p className="mt-3 text-[13px] text-paper/50">{p.object}</p>
            </Link>
          ))}
        </div>

        <Link
          href="/collection/"
          className="mt-12 inline-block text-[12px] uppercase tracking-wide2 text-brass md:hidden"
        >
          The full batch →
        </Link>
      </Section>

      {/* ── Material ──────────────────────────────────────────────────── */}
      <Section className="!py-0">
        <div className="rule grid gap-12 py-24 md:grid-cols-2 md:gap-20 md:py-32">
          <div className="order-2 grid grid-cols-2 gap-5 md:order-1">
            <Plate src="/products/the-executive/hardware.webp" alt="Solid Italian brass hardware" className="aspect-square" />
            <Plate src="/products/the-founder/emboss.webp" alt="The blind-embossed Montec mark" className="mt-10 aspect-square" />
          </div>

          <div className="order-1 md:order-2">
            <Eyebrow>Material honesty</Eyebrow>
            <H2 className="mt-6">Italian leather. Armenian hands.</H2>
            <Body className="mt-7">
              Every piece in the batch is full-grain vegetable-tanned Italian calfskin with solid
              Italian brass. Full-grain keeps the surface the animal actually had — the marks, the
              grain, the way it darkens where you hold it.
            </Body>
            <Body className="mt-5">
              Local production is not a compromise here. It is the point: the same class of material
              the European houses use, cut in Yerevan, at a price that reads as confident rather
              than exorbitant.
            </Body>
            <div className="mt-9">
              <Link href="/about/" className="text-[12px] uppercase tracking-wide2 text-brass hover:text-brass-soft">
                Inside the house →
              </Link>
            </div>
          </div>
        </div>
      </Section>

      {/* ── The Code ──────────────────────────────────────────────────── */}
      <Section>
        <Eyebrow>The Old-Money Code</Eyebrow>
        <H2 className="mt-6 max-w-[20ch]">Six rules. Break one and it becomes ordinary.</H2>

        <ol className="mt-14 grid gap-px bg-brass/15 md:grid-cols-3">
          {[
            ['No logos, loud', 'The mark is a whisper. Recognition is for insiders, not passers-by.'],
            ['No discounts, ever', 'A markdown confesses the first price was a lie.'],
            ['By application', 'You are admitted, not sold to.'],
            ['Numbered batches', 'Limited, dated, finite. An early piece stays early.'],
            ['Material honesty', 'Full-grain, vegetable-tanned. Nothing corrected, nothing hidden.'],
            ['Made at home', 'Italian leather, Armenian hands.'],
          ].map(([title, text], i) => (
            <li key={title} className="bg-obsidian p-8">
              <div className="font-serif text-[19px] text-brass">{String(i + 1).padStart(2, '0')}</div>
              <h3 className="mt-4 font-serif text-[21px]">{title}</h3>
              <p className="mt-2.5 text-[14px] leading-relaxed text-paper/60">{text}</p>
            </li>
          ))}
        </ol>

        <div className="mt-12">
          <Link href="/code/" className="text-[12px] uppercase tracking-wide2 text-brass hover:text-brass-soft">
            Read the code in full →
          </Link>
        </div>
      </Section>

      {/* ── Corporate ─────────────────────────────────────────────────── */}
      <Section className="!pt-0">
        <div className="rule grid gap-12 border-brass/25 pt-24 md:grid-cols-[1fr_0.85fr] md:gap-20">
          <div>
            <Eyebrow>Corporate gifting</Eyebrow>
            <H2 className="mt-6">A gift that makes the giver look as good as the brand.</H2>
            <Body className="mt-7">
              Banks, insurers, law firms and funds buy gifts that have to signal taste. A
              personalised piece from Batch {BATCH} — the recipient&rsquo;s initials blind-embossed,
              boxed the way we box everything — does that without a logo in sight.
            </Body>
            <div className="mt-9">
              <Cta href="/corporate/" tone="outline">
                Corporate enquiries
              </Cta>
            </div>
          </div>
          <Plate
            src="/products/the-access/front.webp"
            alt="The Access cardholder, the piece most often chosen for corporate programmes"
            className="aspect-[4/3] self-center"
          />
        </div>
      </Section>

      {/* ── Access ────────────────────────────────────────────────────── */}
      <Section className="!pt-0">
        <div className="relative overflow-hidden border border-brass/20 px-8 py-20 text-center md:px-16 md:py-28">
          <Eyebrow>Access</Eyebrow>
          <H2 className="mx-auto mt-6 max-w-[18ch]">There is no checkout. You ask, and we answer.</H2>
          <Lead className="mx-auto mt-7 text-center">
            Batch {BATCH} is finite. Pieces are released to people who request them, in the order
            the requests arrive. The price is not published — it comes back with the answer, and it
            is the same number for everyone who asks.
          </Lead>
          <div className="mt-11">
            <Cta href="/request/">Request access</Cta>
          </div>
        </div>
      </Section>
    </>
  )
}
