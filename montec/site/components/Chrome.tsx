'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { useEffect, useState } from 'react'

const nav = [
  { href: '/collection/', label: 'Collection' },
  { href: '/code/', label: 'The Code' },
  { href: '/corporate/', label: 'Corporate' },
  { href: '/about/', label: 'House' },
]

function Mark({ className = '' }: { className?: string }) {
  return (
    <svg viewBox="0 0 120 80" className={className} aria-hidden="true" fill="none">
      <path d="M14 72 L46 20 L78 72" stroke="currentColor" strokeWidth={16} strokeLinejoin="round" strokeLinecap="round" />
      <path d="M42 72 L74 8 L106 72" stroke="currentColor" strokeWidth={16} strokeLinejoin="round" strokeLinecap="round" />
    </svg>
  )
}

export function Header() {
  const pathname = usePathname()
  const [scrolled, setScrolled] = useState(false)
  const [menu, setMenu] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  // Close on navigation — the overlay would otherwise cover the page it opened.
  useEffect(() => setMenu(false), [pathname])

  useEffect(() => {
    if (!menu) return
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && setMenu(false)
    document.addEventListener('keydown', onKey)
    document.body.style.overflow = 'hidden'
    return () => {
      document.removeEventListener('keydown', onKey)
      document.body.style.overflow = ''
    }
  }, [menu])

  return (
    <header
      className={`sticky top-0 z-50 transition-colors duration-500 ease-quiet ${
        scrolled ? 'bg-obsidian/85 backdrop-blur-md border-b border-brass/15' : 'bg-transparent'
      }`}
    >
      <div className="mx-auto flex max-w-[1180px] items-center justify-between px-6 py-5 md:px-10">
        {/* Primary logo position is top-left — Brand Guide 03.4. */}
        <Link href="/" className="flex items-center gap-3" aria-label="Montec — home">
          <Mark className="h-4 w-6 text-brass" />
          <span className="font-serif text-[17px] font-medium tracking-wordmark pl-[0.22em] text-paper">
            MONTEC
          </span>
        </Link>

        <nav className="hidden items-center gap-9 md:flex">
          {nav.map((item) => {
            const active = pathname.startsWith(item.href)
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`text-[12px] uppercase tracking-wide2 transition-colors duration-300 ${
                  active ? 'text-brass' : 'text-paper/60 hover:text-paper'
                }`}
              >
                {item.label}
              </Link>
            )
          })}
          <Link
            href="/request/"
            className="border border-brass px-5 py-2.5 text-[11px] uppercase tracking-wide2 text-brass transition-colors duration-300 hover:bg-brass hover:text-obsidian"
          >
            Request access
          </Link>
        </nav>

        <div className="flex items-center gap-4 md:hidden">
          <Link
            href="/request/"
            className="border border-brass px-4 py-2 text-[10px] uppercase tracking-wide2 text-brass"
          >
            Access
          </Link>
          <button
            type="button"
            onClick={() => setMenu(true)}
            aria-expanded={menu}
            aria-controls="mobile-nav"
            className="py-2 text-[10px] uppercase tracking-wide2 text-paper/70"
          >
            Menu
          </button>
        </div>
      </div>

      {/* Mobile navigation. The four sections don't fit the bar at 390px, and a
          brand sold by application still has to let people find the batch. */}
      <div
        id="mobile-nav"
        hidden={!menu}
        className="fixed inset-0 z-50 bg-obsidian px-6 pb-14 pt-6 md:hidden"
      >
        <div className="flex items-center justify-between">
          <span className="eyebrow">Batch 001</span>
          <button
            type="button"
            onClick={() => setMenu(false)}
            className="py-2 text-[11px] uppercase tracking-wide2 text-brass"
          >
            Close
          </button>
        </div>

        <nav className="mt-14">
          <ul className="divide-y divide-paper/[0.08] border-y border-brass/25">
            {nav.map((item) => (
              <li key={item.href}>
                <Link
                  href={item.href}
                  className={`block py-5 font-serif text-[30px] ${
                    pathname.startsWith(item.href) ? 'text-brass' : 'text-paper'
                  }`}
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
          <Link
            href="/request/"
            className="mt-10 block border border-brass px-6 py-4 text-center text-[11px] uppercase tracking-wide2 text-brass"
          >
            Request access
          </Link>
        </nav>
      </div>
    </header>
  )
}

export function Footer() {
  return (
    <footer className="mt-32 border-t border-brass/15">
      <div className="mx-auto max-w-[1180px] px-6 py-16 md:px-10">
        <div className="grid gap-12 md:grid-cols-[1.4fr_1fr_1fr]">
          <div>
            <div className="flex items-center gap-3">
              <Mark className="h-4 w-6 text-brass" />
              <span className="font-serif text-[17px] font-medium tracking-wordmark pl-[0.22em]">MONTEC</span>
            </div>
            <p className="mt-5 max-w-[38ch] text-[13px] leading-relaxed text-paper/50">
              Quiet-luxury leather, designed in Armenia from full-grain vegetable-tanned Italian
              calfskin. Released in numbered batches, sold by application.
            </p>
          </div>

          <div>
            <div className="eyebrow mb-4">Batch 001</div>
            <ul className="space-y-2.5 text-[13px] text-paper/60">
              <li><Link href="/collection/" className="hover:text-paper">All thirteen pieces</Link></li>
              <li><Link href="/code/" className="hover:text-paper">The Old-Money Code</Link></li>
              <li><Link href="/corporate/" className="hover:text-paper">Corporate gifting</Link></li>
              <li><Link href="/about/" className="hover:text-paper">The house</Link></li>
            </ul>
          </div>

          <div>
            <div className="eyebrow mb-4">Enquiries</div>
            <ul className="space-y-2.5 text-[13px] text-paper/60">
              <li><Link href="/request/" className="hover:text-paper">Request access</Link></li>
              <li>
                <a href="https://instagram.com/montecleather" className="hover:text-paper" rel="noreferrer noopener" target="_blank">
                  Instagram
                </a>
              </li>
              <li>
                <a href="https://youtube.com/@TheMontec" className="hover:text-paper" rel="noreferrer noopener" target="_blank">
                  YouTube
                </a>
              </li>
            </ul>
          </div>
        </div>

        <div className="rule mt-14 pt-6 text-[11px] uppercase tracking-wide2 text-paper/35">
          <div className="flex flex-wrap items-center justify-between gap-3">
            <span>Made in Armenia</span>
            <span>© {new Date().getFullYear()} Montec · Batch 001</span>
          </div>
        </div>
      </div>
    </footer>
  )
}
