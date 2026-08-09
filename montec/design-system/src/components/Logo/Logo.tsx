import React from 'react'
import { Monogram } from './Monogram'

export type LogoVariant = 'primary' | 'reversed' | 'monochrome-dark' | 'monochrome-light' | 'avatar'

export interface LogoProps {
  /**
   * primary: brass mark + near-black wordmark, for light/paper backgrounds.
   * reversed: brass mark + warm-paper wordmark, for dark/obsidian backgrounds.
   * monochrome-dark / monochrome-light: single-colour rule for one-colour print contexts (Brand Guide 03.5).
   * avatar: circular social-avatar lockup (Brand Guide 03.5 / 11.5) — monogram only, brass ring.
   */
  variant?: LogoVariant
  /** Show the "MONTEC" wordmark next to/under the mark. Ignored for the avatar variant. */
  withWordmark?: boolean
  /** Pixel height of the monogram. Wordmark scales with it. */
  size?: number
  className?: string
}

const markColor: Record<LogoVariant, string> = {
  primary: '#B8975A',
  reversed: '#B8975A',
  'monochrome-dark': '#0A0A0A',
  'monochrome-light': '#FAF8F3',
  avatar: '#B8975A',
}

const wordmarkColor: Record<LogoVariant, string> = {
  primary: '#0A0A0A',
  reversed: '#FAF8F3',
  'monochrome-dark': '#0A0A0A',
  'monochrome-light': '#FAF8F3',
  avatar: '#FAF8F3',
}

/**
 * The full MONTEC lockup: monogram + "MONTEC" wordmark set in Cormorant
 * Garamond with the brand's signature 0.22em tracking.
 *
 * Rules encoded here (Brand Guide Section 03 — do not deviate without
 * updating montec/CLAUDE.md first):
 *  - Only the colourways in `LogoVariant` exist. No gradients, no outlines.
 *  - Clearspace equal to the cap-height of the "M" is the caller's
 *    responsibility (wrap in padding) — this component renders the mark only.
 */
export function Logo({ variant = 'primary', withWordmark = true, size = 32, className }: LogoProps) {
  if (variant === 'avatar') {
    return (
      <div
        className={className}
        style={{
          width: size * 2.2,
          height: size * 2.2,
          borderRadius: '50%',
          border: `1px solid ${markColor.avatar}`,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          background: '#0A0A0A',
        }}
      >
        <Monogram size={size} style={{ color: markColor.avatar }} />
      </div>
    )
  }

  return (
    <div
      className={className}
      style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: size * 0.15 }}
    >
      <Monogram size={size} style={{ color: markColor[variant] }} />
      {withWordmark && (
        <span
          style={{
            fontFamily: `'Cormorant Garamond', Georgia, serif`,
            fontWeight: 500,
            letterSpacing: '0.22em',
            paddingLeft: '0.22em',
            fontSize: size * 0.62,
            color: wordmarkColor[variant],
            lineHeight: 1,
          }}
        >
          MONTEC
        </span>
      )}
    </div>
  )
}
