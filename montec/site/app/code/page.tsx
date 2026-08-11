import type { Metadata } from 'next'
import { Cta, Eyebrow, H2, Lead, Section } from '@/components/Bits'

export const metadata: Metadata = {
  title: 'The Old-Money Code',
  description:
    'Six disciplines that keep Montec a luxury house: no loud logos, no discounts ever, sold by application, numbered batches, material honesty, made at home.',
}

const rules = [
  ['No logos, loud', 'The mark is a whisper, never a billboard. It is blind-embossed into the leather — tone on tone, no ink, no foil — so it is legible to someone who knows what they are looking at and invisible to everyone else. Recognition is for insiders, not passers-by.'],
  ['No discounts, ever', 'The price is the price, in every season and every conversation. A markdown is a confession that the first price was a lie, and a house that discounts once is negotiating forever.'],
  ['By application', 'There is no checkout on this site. You request a piece and we answer — which makes the purchase an acceptance rather than a transaction, and keeps the scarcity real rather than announced.'],
  ['Numbered batches', 'Production is released in finite, dated batches. Batch 001 holds thirteen artifacts. Owning an early piece means something, and it goes on meaning it.'],
  ['Material honesty', 'Full-grain, vegetable-tanned, nothing corrected. We photograph the grain and the marks rather than retouching them, because the surface is the argument.'],
  ['Made at home', 'Italian leather, Armenian hands. Local production is not a cost compromise we hope you overlook — it is the reason the brand exists at all.'],
]

export default function CodePage() {
  return (
    <>
      <Section>
        <Eyebrow>The Old-Money Code</Eyebrow>
        <H2 className="mt-6 max-w-[22ch]">Six rules. Break one and it becomes ordinary.</H2>
        <Lead className="mt-7">
          Everything else about this house is a matter of taste and can be argued. These six are not.
        </Lead>

        <ol className="mt-20 space-y-px">
          {rules.map(([title, text], i) => (
            <li key={title} className="grid gap-6 border-t border-brass/20 py-10 md:grid-cols-[5rem_18rem_1fr] md:gap-10">
              <span className="font-serif text-[22px] text-brass">{String(i + 1).padStart(2, '0')}</span>
              <h2 className="font-serif text-[26px] leading-tight">{title}</h2>
              <p className="text-[15px] leading-[1.75] text-paper/65">{text}</p>
            </li>
          ))}
        </ol>
      </Section>

      <Section className="!pt-0">
        <div className="border border-brass/20 px-8 py-16 text-center md:px-16">
          <H2 className="mx-auto max-w-[20ch]">If that reads like a house you want to buy from —</H2>
          <div className="mt-9">
            <Cta href="/request/">Request access</Cta>
          </div>
        </div>
      </Section>
    </>
  )
}
