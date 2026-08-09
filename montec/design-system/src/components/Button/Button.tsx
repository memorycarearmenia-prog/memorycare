import React from 'react'

export type ButtonVariant = 'primary' | 'secondary' | 'ghost'
export type ButtonSize = 'default' | 'small'

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant
  size?: ButtonSize
}

const base: React.CSSProperties = {
  fontFamily: `Inter, -apple-system, system-ui, sans-serif`,
  fontWeight: 500,
  fontSize: 11,
  letterSpacing: '0.28em',
  textTransform: 'uppercase',
  border: '1px solid transparent',
  cursor: 'pointer',
  transition: 'background-color .2s, color .2s, border-color .2s',
  borderRadius: 2,
}

const sizes: Record<ButtonSize, React.CSSProperties> = {
  default: { padding: '16px 32px' },
  small: { padding: '11px 22px', fontSize: 10 },
}

const variants: Record<ButtonVariant, React.CSSProperties> = {
  // The primary CTA is "REQUEST ACCESS" — an admission, not a sale. No shadow, no glow, no urgency colour.
  primary: { background: '#FAF8F3', color: '#0A0A0A', borderColor: '#FAF8F3' },
  secondary: { background: 'transparent', color: '#B8975A', borderColor: '#B8975A' },
  ghost: { background: 'transparent', color: '#FAF8F3', borderColor: 'transparent' },
}

/**
 * MONTEC's one button component. There is no "sale" or "urgent" variant —
 * per the Old-Money Code ("No discounts, ever"), a button never implies
 * a countdown, a markdown, or an exclamation. Label copy follows the
 * Voice & Tone rules in the Brand Guide: no "Buy now," no "Hurry."
 *
 * Typical usage: `<Button>REQUEST ACCESS</Button>` (primary CTA on a
 * product page) or `<Button variant="secondary">Corporate inquiry</Button>`
 * (the B2B/wholesale secondary CTA).
 */
export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'default', style, children, ...rest }, ref) => (
    <button ref={ref} style={{ ...base, ...sizes[size], ...variants[variant], ...style }} {...rest}>
      {children}
    </button>
  )
)
Button.displayName = 'Button'
