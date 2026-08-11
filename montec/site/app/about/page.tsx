import type { Metadata } from 'next'
import { Body, Cta, Eyebrow, H2, Lead, Plate, Section } from '@/components/Bits'

export const metadata: Metadata = {
  title: 'The house',
  description:
    'Montec is designed in Armenia and made from full-grain vegetable-tanned Italian calfskin by named craftsmen. A young house with a real origin rather than an invented one.',
}

export default function AboutPage() {
  return (
    <>
      <Section>
        <Eyebrow>The house</Eyebrow>
        <H2 className="mt-6 max-w-[24ch]">A young house, with a real origin.</H2>
        <Lead className="mt-7">
          Montec was founded in Yerevan. It does not claim a Tuscan workshop in 1961, because it does
          not have one — and a story you can check is worth more than a story you cannot.
        </Lead>

        <div className="mt-20 grid gap-14 md:grid-cols-2 md:gap-20">
          <div>
            <h2 className="font-serif text-[26px]">Who makes it</h2>
            <Body className="mt-5">
              The pieces are made by two master craftsmen — Artem, and Levon, who works from Kapan in
              Syunik and is becoming the house&rsquo;s primary maker. They are paid per piece, not per
              hour, which is the honest arrangement when the work is this slow.
            </Body>
            <Body className="mt-5">
              Montec sits under FiCorp, which also runs a separate budget-tier leather brand. The two
              share a workshop and nothing else: no shared materials, no shared pricing logic, and
              no shared shortcuts.
            </Body>
          </div>

          <div>
            <h2 className="font-serif text-[26px]">What it is made of</h2>
            <Body className="mt-5">
              Full-grain vegetable-tanned Italian calfskin throughout, with solid Italian brass
              hardware — except on The Capital and The Access, which are deliberately hardware-free
              so there is nothing between the hand and the leather.
            </Body>
            <Body className="mt-5">
              Vegetable tanning is slower and less forgiving than chrome, and it is the only method
              that produces a patina worth waiting for. The leather you receive is the lightest it
              will ever be.
            </Body>
          </div>
        </div>

        <div className="mt-20 grid grid-cols-2 gap-6 md:grid-cols-4">
          <Plate src="/products/the-founder/emboss.webp" alt="The blind-embossed mark on full-grain calfskin" className="aspect-square" />
          <Plate src="/products/the-executive/hardware.webp" alt="Solid Italian brass hardware" className="aspect-square" />
          <Plate src="/products/the-closer/three-quarter.webp" alt="The Closer messenger bag" className="aspect-square" />
          <Plate src="/products/the-capital/front.webp" alt="The Capital bifold wallet" className="aspect-square" />
        </div>
      </Section>

      <Section className="!pt-0">
        <div className="rule border-brass/25 pt-16">
          <H2 className="max-w-[22ch]">Two lines we hold ourselves to.</H2>
          <div className="mt-12 grid gap-10 md:grid-cols-2">
            <blockquote className="border-l border-brass/40 pl-7">
              <p className="font-serif text-[25px] italic leading-snug">
                &ldquo;I am not rich enough to buy cheap things.&rdquo;
              </p>
              <footer className="mt-4 text-[12px] uppercase tracking-wide2 text-paper/40">
                The line for the object — why the price is the price
              </footer>
            </blockquote>
            <blockquote className="border-l border-brass/40 pl-7">
              <p className="font-serif text-[25px] italic leading-snug">
                &ldquo;Craftsmanship and strategy for those who write history.&rdquo;
              </p>
              <footer className="mt-4 text-[12px] uppercase tracking-wide2 text-paper/40">
                The line for the customer — who it is made for
              </footer>
            </blockquote>
          </div>
          <div className="mt-14">
            <Cta href="/collection/" tone="outline">See the batch</Cta>
          </div>
        </div>
      </Section>
    </>
  )
}
