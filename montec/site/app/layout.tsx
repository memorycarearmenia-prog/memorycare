import type { Metadata } from 'next'
import './globals.css'
import { Header, Footer } from '@/components/Chrome'

const SITE = 'https://montec.am'

export const metadata: Metadata = {
  metadataBase: new URL(SITE),
  title: {
    default: 'Montec — quiet-luxury leather, made in Armenia',
    template: '%s · Montec',
  },
  description:
    'Full-grain vegetable-tanned Italian leather, made in Armenia. Batch 001: thirteen numbered pieces, released by application. No discounts, ever.',
  openGraph: {
    type: 'website',
    siteName: 'Montec',
    title: 'Montec — quiet-luxury leather, made in Armenia',
    description:
      'Batch 001: thirteen numbered pieces in full-grain Italian leather. Sold by application.',
    locale: 'en',
  },
  robots: { index: true, follow: true },
}

/** Organization + brand facts for search engines. Only claims that are true. */
const orgJsonLd = {
  '@context': 'https://schema.org',
  '@type': 'Organization',
  name: 'Montec',
  url: SITE,
  description:
    'Quiet-luxury leather accessories designed in Armenia from full-grain vegetable-tanned Italian leather, released in numbered batches.',
  foundingLocation: { '@type': 'Place', name: 'Yerevan, Armenia' },
  sameAs: ['https://instagram.com/montecleather', 'https://youtube.com/@TheMontec'],
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(orgJsonLd) }}
        />
        <a
          href="#main"
          className="sr-only focus:not-sr-only focus:absolute focus:left-6 focus:top-5 focus:z-[60] focus:border focus:border-brass focus:bg-obsidian focus:px-4 focus:py-2 focus:text-[11px] focus:uppercase focus:tracking-wide2 focus:text-brass"
        >
          Skip to content
        </a>
        <Header />
        <main id="main">{children}</main>
        <Footer />
      </body>
    </html>
  )
}
