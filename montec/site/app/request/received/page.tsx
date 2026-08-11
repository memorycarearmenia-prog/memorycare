import type { Metadata } from 'next'
import { Cta, Eyebrow, H2, Lead, Section } from '@/components/Bits'

export const metadata: Metadata = {
  title: 'Request received',
  description: 'Your request has reached us.',
  robots: { index: false, follow: false },
}

export default function ReceivedPage() {
  return (
    <Section className="min-h-[60vh]">
      <Eyebrow>Received</Eyebrow>
      <H2 className="mt-6 max-w-[18ch]">Your request has reached us.</H2>
      <Lead className="mt-7">
        A person will read it and reply, usually within two working days. Nothing further is needed
        from you.
      </Lead>
      <div className="mt-12 flex flex-wrap gap-4">
        <Cta href="/collection/" tone="outline">Back to the batch</Cta>
      </div>
    </Section>
  )
}
