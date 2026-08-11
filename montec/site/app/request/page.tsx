import type { Metadata } from 'next'
import { Body, Eyebrow, H2, Lead, Section } from '@/components/Bits'
import { RequestForm } from '@/components/RequestForm'
import { BATCH, total } from '@/lib/products'

export const metadata: Metadata = {
  title: 'Request access',
  description: `Batch ${BATCH} is released by application. Tell us which of the ${total} pieces you want and we answer personally.`,
}

export default function RequestPage() {
  return (
    <Section>
      <div className="grid gap-16 md:grid-cols-[0.9fr_1fr] md:gap-24">
        <div>
          <Eyebrow>Access</Eyebrow>
          <H2 className="mt-6 max-w-[16ch]">There is no checkout.</H2>
          <Lead className="mt-7">
            You ask, and we answer. It is slower than a cart, and it is the only way a finite batch
            stays finite.
          </Lead>
          <Body className="mt-8">
            Batch {BATCH} holds {total} pieces. Requests are answered in the order they arrive, by a
            person, usually within two working days. If the piece you want is spoken for we will say
            so plainly rather than keep you waiting.
          </Body>
          <Body className="mt-5">
            The price is the price. We do not run sales, and there is no code to ask us for.
          </Body>
        </div>

        <div>
          <RequestForm kind="access" />
        </div>
      </div>
    </Section>
  )
}
