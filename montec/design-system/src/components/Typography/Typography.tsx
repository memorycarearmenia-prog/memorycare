import React from 'react'

export type TypographyVariant = 'display' | 'h2' | 'lead' | 'eyebrow' | 'body' | 'caption'

export interface TypographyProps extends React.HTMLAttributes<HTMLElement> {
  variant?: TypographyVariant
  /** Render an Armenian-script companion face instead of the Latin default (Brand Guide 05.3). */
  lang?: 'en' | 'hy'
  /** Override the rendered element (defaults chosen per variant: h2→h2, eyebrow/caption→span, others→p). */
  as?: keyof React.JSX.IntrinsicElements
  className?: string
  children?: React.ReactNode
}

const defaultTag: Record<TypographyVariant, keyof React.JSX.IntrinsicElements> = {
  display: 'div',
  h2: 'h2',
  lead: 'p',
  eyebrow: 'span',
  body: 'p',
  caption: 'span',
}

const styleFor = (variant: TypographyVariant, lang: 'en' | 'hy'): React.CSSProperties => {
  const serif = lang === 'hy' ? `'Noto Serif Armenian', 'Cormorant Garamond', serif` : `'Cormorant Garamond', Georgia, serif`
  const sans = lang === 'hy' ? `'Noto Sans Armenian', Inter, sans-serif` : `Inter, -apple-system, system-ui, sans-serif`

  switch (variant) {
    case 'display':
      return { fontFamily: serif, fontWeight: 500, fontSize: 'clamp(64px, 13vw, 150px)', lineHeight: 1, letterSpacing: '0.16em' }
    case 'h2':
      return { fontFamily: serif, fontWeight: 400, fontSize: 44, lineHeight: 1.12 }
    case 'lead':
      return { fontFamily: serif, fontWeight: 300, fontSize: 23, lineHeight: 1.55, maxWidth: '66ch' }
    case 'eyebrow':
      return { fontFamily: sans, fontWeight: 500, fontSize: 11, letterSpacing: '0.42em', textTransform: 'uppercase' }
    case 'body':
      return { fontFamily: sans, fontWeight: 300, fontSize: 16.5, lineHeight: 1.7, maxWidth: '62ch' }
    case 'caption':
      return { fontFamily: sans, fontWeight: 400, fontSize: 13, lineHeight: 1.5 }
  }
}

/**
 * MONTEC's type hierarchy as a single component (Brand Guide Section 05).
 *
 * Pairing rule: never render `lead`/`h2`/`display` (serif) for long body
 * copy, and never render the wordmark or a product name via `body`/`caption`
 * (sans) — the tension between the two faces is the typographic identity.
 */
export function Typography({ variant = 'body', lang = 'en', as, className, style, children, ...rest }: TypographyProps) {
  const Tag = (as ?? defaultTag[variant]) as React.ElementType
  return (
    <Tag className={className} style={{ ...styleFor(variant, lang), ...style }} {...rest}>
      {children}
    </Tag>
  )
}
