import React from 'react'

export interface MonogramProps extends React.SVGAttributes<SVGSVGElement> {
  /** Pixel size of the square icon. Defaults to 32. */
  size?: number
  /**
   * 'brand' renders the two brass/monochrome peaks in currentColor (default).
   * Colour itself is controlled via the `color` CSS property / `className`.
   */
  title?: string
}

/**
 * The MONTEC monogram: two overlapping chevron peaks forming a stylized
 * mountain / "M" silhouette — the "Mont" half of the name made visible.
 * Traced from montec/assets/brand/logo/logo-gold-on-black.png.
 *
 * Usage rule (montec/CLAUDE.md, Brand Guide 03.6): never fill this mark
 * with a gradient or multiple colours — it renders in exactly one colour
 * via `currentColor`, matching the blind-emboss / single-colourway rule.
 */
export function Monogram({ size = 32, title = 'Montec', ...rest }: MonogramProps) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 120 80"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      role="img"
      aria-label={title}
      {...rest}
    >
      <title>{title}</title>
      {/* Left peak — shorter, appears first */}
      <path
        d="M14 72 L46 20 L78 72"
        stroke="currentColor"
        strokeWidth={16}
        strokeLinejoin="round"
        strokeLinecap="round"
        fill="none"
      />
      {/* Right peak — taller, overlaps the left peak's right leg to form the valley */}
      <path
        d="M42 72 L74 8 L106 72"
        stroke="currentColor"
        strokeWidth={16}
        strokeLinejoin="round"
        strokeLinecap="round"
        fill="none"
      />
    </svg>
  )
}
