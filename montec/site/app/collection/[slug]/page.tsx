import type { Metadata } from 'next'
import Link from 'next/link'
import { notFound } from 'next/navigation'
import { Cta, Plate } from '@/components/Bits'
import { products, bySlug, indexOf, nextOf, total, BATCH } from '@/lib/products'

export function generateStaticParams() {
  return products.map((p) => ({ slug: p.slug }))
}

export function generateMetadata({ params }: { params: { slug: string } }): Metadata {
  const p = bySlug(params.slug)
  if (!p) return {}
  return {
    title: `${p.name} — ${p.object}`,
    description: `${p.line} ${p.body}`.slice(0, 155),
    openGraph: {
      title: `${p.name} · Montec`,
      description: p.line,
      images: [{ url: `/products/${p.slug}/three-quarter.webp` }],
    },
  }
}

/** The five fields never change, and never reorder — the brand's own taxonomy. */
const AUDIT_FIELDS = [
  ['External', 'external'],
  ['Architecture', 'architecture'],
  ['Volume', 'volume'],
  ['Hardware', 'hardware'],
  ['Markings', 'markings'],
] as const

export default function ProductPage({ params }: { params: { slug: string } }) {
  const p = bySlug(params.slug)
  if (!p) notFound()

  const n = indexOf(p.slug)
  const next = nextOf(p.slug)

  // Only facts we actually hold. No rating, no review count, no stock claim —
  // the brand is pre-launch and inventing social proof is forbidden. No `offers`
  // either: pieces are released by application and no price is published, so
  // there is nothing truthful to put in one.
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: `Montec ${p.name}`,
    category: p.object,
    description: p.body,
    brand: { '@type': 'Brand', name: 'Montec' },
    material: 'Full-grain vegetable-tanned Italian calfskin',
    image: `/products/${p.slug}/three-quarter.webp`,
  }

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />

      <article className="mx-auto max-w-[1180px] px-6 pb-24 pt-16 md:px-10 md:pt-20">
        <nav className="flex items-center justify-between text-[11px] uppercase tracking-wide2 text-paper/40">
          <span>
            {n} / {total} — {p.object}
          </span>
          <Link href="/collection/" className="hover:text-brass">
            Back to collection
          </Link>
        </nav>

        <div className="mt-12 grid gap-14 md:grid-cols-[1fr_1fr] md:gap-20">
          {/* Left: the piece. Sticky, so it stays with you while THE AUDIT is
              read — the two columns are very different lengths and the piece
              is the thing the words are about. */}
          <div className="md:sticky md:top-24 md:self-start">
            <Plate src={`/products/${p.slug}/three-quarter.webp`} alt={`${p.name} — three-quarter view`} className="aspect-[4/3]" />
            <div className="mt-5 grid grid-cols-3 gap-4">
              <Plate src={`/products/${p.slug}/front.webp`} alt={`${p.name} — front view`} className="aspect-square" />
              <Plate src={`/products/${p.slug}/hardware.webp`} alt={`${p.name} — hardware detail`} className="aspect-square" />
              <Plate src={`/products/${p.slug}/emboss.webp`} alt={`${p.name} — blind-embossed mark`} className="aspect-square" />
            </div>
          </div>

          {/* Right: the argument */}
          <div className="md:pt-4">
            <h1 className="font-serif text-[42px] font-normal leading-[1.05] md:text-[56px]">{p.name}</h1>
            <p className="mt-4 font-serif text-[21px] italic text-brass">{p.line}</p>

            <p className="measure mt-9 text-[16px] leading-[1.75] text-paper/70">{p.body}</p>

            {/* THE AUDIT — identical on all thirteen pages. */}
            <section className="mt-14" aria-labelledby="audit">
              <h2 id="audit" className="eyebrow border-b border-brass/25 pb-3">
                The Audit
              </h2>
              <dl className="divide-y divide-paper/[0.07]">
                {AUDIT_FIELDS.map(([label, key]) => (
                  <div key={key} className="grid grid-cols-[8rem_1fr] gap-5 py-4">
                    <dt className="text-[11px] uppercase tracking-wide2 text-paper/35">{label}</dt>
                    <dd className="text-[14px] leading-relaxed text-paper/75">{p.audit[key]}</dd>
                  </div>
                ))}
              </dl>
            </section>

            <div className="rule mt-14 border-brass/25 pt-9">
              <div className="eyebrow">By request</div>
              <p className="measure mt-4 text-[15px] leading-relaxed text-paper/65">
                We do not publish a price. Ask for this piece and the number comes back with the
                answer — one number, the same for everyone, and it does not move afterwards.
              </p>
              <div className="mt-8">
                <Cta href={`/request/?piece=${p.slug}`}>Request access</Cta>
              </div>
            </div>

            <p className="mt-6 text-[12px] leading-relaxed text-paper/35">
              Batch {BATCH} · Piece {n} of {total} · Made in Armenia. Initials can be blind-embossed
              on request.
            </p>
          </div>
        </div>

        {/* The full reference turnaround — how the house documents each piece. */}
        <section className="mt-28">
          <h2 className="eyebrow border-b border-brass/25 pb-3">Reference sheet</h2>
          <Plate
            src={`/products/${p.slug}/turnaround.webp`}
            alt={`${p.name} — nine-view reference turnaround`}
            className="mt-8 w-full"
          />
        </section>

        {/* Continue the set */}
        <section className="rule mt-24 border-brass/25 pt-10">
          <div className="flex flex-wrap items-end justify-between gap-6">
            <div>
              <div className="eyebrow">Continue the set</div>
              <Link href={`/collection/${next.slug}/`} className="mt-4 block font-serif text-[32px] hover:text-brass">
                {next.name}
              </Link>
              <p className="mt-1 font-serif text-[15px] italic text-paper/45">{next.line}</p>
            </div>
            <Link href="/collection/" className="text-[12px] uppercase tracking-wide2 text-brass hover:text-brass-soft">
              View full collection →
            </Link>
          </div>
        </section>
      </article>
    </>
  )
}
