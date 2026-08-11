import { Cta, Eyebrow, H2, Lead, Section } from '@/components/Bits'

export default function NotFound() {
  return (
    <Section className="min-h-[60vh]">
      <Eyebrow>Not found</Eyebrow>
      <H2 className="mt-6 max-w-[20ch]">This page is not part of the batch.</H2>
      <Lead className="mt-7">
        The link may be old, or the piece may have been renamed. The manifest has all thirteen.
      </Lead>
      <div className="mt-12">
        <Cta href="/collection/">See the batch</Cta>
      </div>
    </Section>
  )
}
