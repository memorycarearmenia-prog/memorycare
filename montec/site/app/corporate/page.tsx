import type { Metadata } from 'next'
import { Body, Eyebrow, H2, Lead, Plate, Section } from '@/components/Bits'
import { RequestForm } from '@/components/RequestForm'

export const metadata: Metadata = {
  title: 'Corporate gifting',
  description:
    'Personalised Montec pieces for client and partner gifting: initials blind-embossed, boxed as standard, made in Armenia from full-grain Italian calfskin. Enquiries by form.',
}

export default function CorporatePage() {
  return (
    <>
      <Section>
        <Eyebrow>Corporate gifting</Eyebrow>
        <H2 className="mt-6 max-w-[22ch]">The gift is judged before it is opened.</H2>
        <Lead className="mt-7">
          A gift from a bank, an insurer or a firm says something about the sender first. Ours is
          designed to say: this person has taste, and did not delegate it.
        </Lead>

        <div className="mt-20 grid gap-14 md:grid-cols-[1fr_0.9fr] md:gap-20">
          <div>
            <h2 className="font-serif text-[26px]">How a programme works</h2>
            <dl className="mt-8 divide-y divide-paper/[0.07] border-t border-brass/25">
              {[
                ['The piece', 'Usually The Access cardholder or The Capital bifold — small enough to give at scale, good enough that it stays in a pocket for years.'],
                ['Personalisation', "Up to four initials, blind-embossed into the leather. Tone on tone, so it reads as a detail rather than a badge."],
                ['Presentation', 'Rigid matte box, cotton dust bag, and a warm-paper card carrying the batch number. Nothing printed, nothing cellophaned.'],
                ['Lead time', 'Set per programme against the run size — the pieces are cut and finished by hand, so the honest answer depends on the number.'],
                ['Price', 'Quoted per programme. Volume changes the number; it does not change the leather.'],
              ].map(([term, def]) => (
                <div key={term} className="grid grid-cols-[9rem_1fr] gap-5 py-5">
                  <dt className="text-[11px] uppercase tracking-wide2 text-brass">{term}</dt>
                  <dd className="text-[14px] leading-relaxed text-paper/70">{def}</dd>
                </div>
              ))}
            </dl>

            <Body className="mt-10">
              We keep corporate runs small on purpose. A gift that half the room already owns is not
              a gift, and the whole argument of a numbered batch collapses if we print one for
              everybody.
            </Body>
          </div>

          <div>
            <Plate
              src="/products/the-access/emboss.webp"
              alt="Blind-embossed initials on The Access cardholder"
              className="aspect-[4/3]"
            />
            <Plate
              src="/products/the-capital/three-quarter.webp"
              alt="The Capital bifold wallet"
              className="mt-6 aspect-[4/3]"
            />
          </div>
        </div>
      </Section>

      <Section className="!pt-0">
        <div className="rule border-brass/25 pt-16">
          <Eyebrow>Enquiry</Eyebrow>
          <H2 className="mt-6 max-w-[20ch]">Tell us the occasion and the number.</H2>
          <Body className="mt-6">
            We answer every enquiry personally. If the run does not suit us we will say so rather
            than quote you a number we cannot honour.
          </Body>
          <div className="mt-12 max-w-[640px]">
            <RequestForm kind="corporate" />
          </div>
        </div>
      </Section>
    </>
  )
}
