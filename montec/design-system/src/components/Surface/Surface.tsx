import React from 'react'
import { colors } from '../../tokens/colors'

export type SurfaceTone = 'obsidian' | 'anthracite' | 'paper'

export interface SurfaceProps extends React.HTMLAttributes<HTMLDivElement> {
  /**
   * Which brand ground this surface establishes.
   * 'obsidian' (default) — the near-black ground the brand lives on.
   * 'anthracite' — the mid-tone panel ground, one step off Obsidian.
   * 'paper' — the warm off-white ground used for print and documents.
   */
  tone?: SurfaceTone
  /** Inner padding in px. Pass 0 for a flush surface. */
  padding?: number
  children?: React.ReactNode
}

const grounds: Record<SurfaceTone, { background: string; color: string }> = {
  obsidian: { background: colors.obsidian, color: colors.paper },
  anthracite: { background: colors.anthracite, color: colors.paper },
  paper: { background: colors.paper, color: colors.obsidian },
}

/**
 * The MONTEC root wrapper. Every screen, section, and card sits on a Surface.
 *
 * Why it exists: MONTEC is a dark-first system. `Typography`, `Button`'s
 * paper/ghost variants and `Logo`'s reversed lockup all render in Warm Paper
 * and are **invisible on a white page** — they inherit their legibility from
 * the ground beneath them. Surface is what supplies that ground (and the
 * matching text colour), so components are never left depending on an ambient
 * body style that a host app may not have.
 *
 * Pair the tone with the variant: `tone="obsidian"` with `Logo variant="reversed"`
 * and light Typography; `tone="paper"` with `Logo variant="primary"` and dark text.
 */
export function Surface({ tone = 'obsidian', padding = 32, style, children, ...rest }: SurfaceProps) {
  return (
    <div
      style={{
        ...grounds[tone],
        padding,
        fontFamily: `Inter, -apple-system, system-ui, sans-serif`,
        ...style,
      }}
      {...rest}
    >
      {children}
    </div>
  )
}
