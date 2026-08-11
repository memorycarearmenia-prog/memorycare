import type { Metadata } from 'next'
import { Eyebrow, H2, Lead, Section } from '@/components/Bits'
import { Ledger } from '@/components/Ledger'
import { BATCH, total } from '@/lib/products'

export const metadata: Metadata = {
  title: `Batch ${BATCH} — all ${total} pieces`,
  description: `The complete Batch ${BATCH} manifest: ${total} numbered pieces in full-grain vegetable-tanned Italian calfskin, made in Armenia. Sold by application.`,
}

export default function CollectionPage() {
  return (
    <Section>
      <Eyebrow>Batch {BATCH}</Eyebrow>
      <H2 className="mt-6 max-w-[20ch]">The manifest.</H2>
      <Lead className="mt-7">
        Thirteen artifacts, numbered in the order they were designed. The batch is finite: when a
        piece is gone from it, it is gone from it.
      </Lead>

      <div className="mt-16">
        <Ledger />
      </div>
    </Section>
  )
}
