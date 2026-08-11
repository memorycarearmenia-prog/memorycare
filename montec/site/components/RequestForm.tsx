'use client'

import { useEffect, useRef } from 'react'
import { products, bySlug } from '@/lib/products'

/**
 * Access and corporate enquiries.
 *
 * Deliberately a native form POST, not a fetch: the page is statically
 * exported, and a plain form works with JavaScript disabled, on a slow
 * connection, and in an in-app browser. Nothing here needs to be interactive.
 *
 * Delivery: Netlify Forms picks this up from the `data-netlify` attributes at
 * deploy time and mails submissions on — no backend, no API key in the bundle.
 * To use a different service (Formspree and similar), set
 * NEXT_PUBLIC_FORM_ENDPOINT to its URL and it posts there instead.
 *
 * The piece a visitor arrived from comes in as ?piece=<slug> — read on mount
 * rather than at build time, because this page is one prerendered file shared
 * by every product link. Without JavaScript the select simply starts on "no
 * particular piece yet", which is a true answer rather than a broken one.
 */
export function RequestForm({
  kind = 'access',
  piece,
}: {
  kind?: 'access' | 'corporate'
  piece?: string
}) {
  const select = useRef<HTMLSelectElement>(null)

  useEffect(() => {
    const slug = new URLSearchParams(window.location.search).get('piece')
    const p = slug ? bySlug(slug) : undefined
    if (p && select.current) select.current.value = p.name
  }, [])

  const formName = kind === 'corporate' ? 'montec-corporate' : 'montec-access'
  const endpoint = process.env.NEXT_PUBLIC_FORM_ENDPOINT

  const field =
    'w-full border border-paper/15 bg-transparent px-4 py-3.5 text-[15px] text-paper placeholder:text-paper/30 transition-colors focus:border-brass'
  const label = 'mb-2 block text-[11px] uppercase tracking-wide2 text-paper/45'

  return (
    <form
      name={formName}
      method="POST"
      action={endpoint ?? '/request/received/'}
      data-netlify="true"
      data-netlify-honeypot="company-website"
      className="space-y-7"
    >
      <input type="hidden" name="form-name" value={formName} />
      {/* Honeypot: real people never see it, bots fill it. */}
      <p className="hidden">
        <label>
          Leave this empty <input name="company-website" tabIndex={-1} autoComplete="off" />
        </label>
      </p>

      <div className="grid gap-6 sm:grid-cols-2">
        <div>
          <label className={label} htmlFor="name">
            Name
          </label>
          <input id="name" name="name" required autoComplete="name" className={field} />
        </div>
        <div>
          <label className={label} htmlFor="email">
            Email
          </label>
          <input id="email" name="email" type="email" required autoComplete="email" className={field} />
        </div>
      </div>

      {kind === 'corporate' ? (
        <div className="grid gap-6 sm:grid-cols-2">
          <div>
            <label className={label} htmlFor="organisation">
              Organisation
            </label>
            <input id="organisation" name="organisation" required className={field} />
          </div>
          <div>
            <label className={label} htmlFor="quantity">
              Approximate number of pieces
            </label>
            <input id="quantity" name="quantity" inputMode="numeric" className={field} />
          </div>
        </div>
      ) : (
        <div>
          <label className={label} htmlFor="piece">
            Piece
          </label>
          <select
            id="piece"
            name="piece"
            ref={select}
            defaultValue={piece ?? ''}
            className={field}
          >
            <option value="">No particular piece yet</option>
            {products.map((p) => (
              <option key={p.slug} value={p.name} className="bg-obsidian">
                {p.name} — {p.object}
              </option>
            ))}
          </select>
        </div>
      )}

      <div>
        <label className={label} htmlFor="message">
          Anything we should know
        </label>
        <textarea id="message" name="message" rows={4} className={field} />
      </div>

      <button
        type="submit"
        className="bg-paper px-8 py-4 text-[11px] uppercase tracking-wide2 text-obsidian transition-colors duration-300 hover:bg-brass"
      >
        {kind === 'corporate' ? 'Send enquiry' : 'Request access'}
      </button>

      <p className="text-[12px] leading-relaxed text-paper/35">
        We reply to every request personally, usually within two working days. Your details are used
        for that reply and nothing else.
      </p>
    </form>
  )
}
