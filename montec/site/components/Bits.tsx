import Link from 'next/link'
import { formatAmount } from '@/lib/products'

/**
 * A price, with the dram sign set in Noto Sans Armenian — neither Cormorant
 * Garamond nor Inter carries a glyph for ֏, and letting the browser pick a
 * fallback mid-number renders the sign inconsistently from machine to machine.
 */
export function Price({ price }: { price: number | null }) {
  if (price === null) return <>Price on request</>
  return (
    <>
      {formatAmount(price)}
      <span className="font-sans-hy"> ֏</span>
    </>
  )
}

export function Eyebrow({ children }: { children: React.ReactNode }) {
  return <div className="eyebrow">{children}</div>
}

export function Section({
  children,
  className = '',
}: {
  children: React.ReactNode
  className?: string
}) {
  return (
    <section className={`mx-auto max-w-[1180px] px-6 py-24 md:px-10 md:py-32 ${className}`}>
      {children}
    </section>
  )
}

export function H2({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <h2 className={`font-serif text-[34px] font-normal leading-[1.12] md:text-[44px] ${className}`}>
      {children}
    </h2>
  )
}

export function Lead({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return (
    <p className={`max-w-lead font-serif text-[21px] font-light leading-[1.55] text-paper/85 md:text-[23px] ${className}`}>
      {children}
    </p>
  )
}

export function Body({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  return <p className={`measure text-[16px] leading-[1.7] text-paper/70 ${className}`}>{children}</p>
}

/** The one CTA shape. No urgency, no gradient, no shadow — Old-Money Code 01. */
export function Cta({
  href,
  children,
  tone = 'solid',
}: {
  href: string
  children: React.ReactNode
  tone?: 'solid' | 'outline'
}) {
  const base =
    'inline-block px-8 py-4 text-[11px] uppercase tracking-wide2 transition-colors duration-300 ease-quiet'
  const skin =
    tone === 'solid'
      ? 'bg-paper text-obsidian hover:bg-brass'
      : 'border border-brass text-brass hover:bg-brass hover:text-obsidian'
  return (
    <Link href={href} className={`${base} ${skin}`}>
      {children}
    </Link>
  )
}

/**
 * Product photography is studio-shot on white. Rather than fight that, the
 * shots are mounted as warm-paper plates on the near-black ground — specimen
 * cards, which is also how the brand's own reference sheets are organised.
 */
export function Plate({
  src,
  alt,
  className = '',
}: {
  src: string
  alt: string
  className?: string
}) {
  return (
    <div className={`overflow-hidden bg-paper ${className}`}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={src} alt={alt} loading="lazy" className="h-full w-full object-cover" />
    </div>
  )
}
