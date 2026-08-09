/**
 * MONTEC typography tokens. Source of truth: montec/CLAUDE.md "Visual identity"
 * and montec/docs/planning/Montec_Brand_Book.html Sections 05.1–05.3.
 *
 * Pairing rule: Cormorant Garamond carries emotion and heritage; Inter carries
 * information. Never set long body copy in the serif, and never set the
 * wordmark or a product name in the sans.
 */
export const fontFamilies = {
  serif: `'Cormorant Garamond', Georgia, serif`,
  sans: `Inter, -apple-system, system-ui, sans-serif`,
  /** Armenian companion for the serif — Cormorant Garamond has no Armenian glyphs. */
  serifArmenian: `'Noto Serif Armenian', 'Cormorant Garamond', serif`,
  /** Armenian companion for the sans — Inter has no Armenian glyphs. */
  sansArmenian: `'Noto Sans Armenian', Inter, sans-serif`,
} as const

/**
 * Type hierarchy, matching the Brand Guide's Section 05.2 table exactly.
 * `level` is used as the React component's `variant` prop value.
 */
export const typeScale = [
  { level: 'display', family: 'serif', weight: 500, size: 'clamp(64px, 13vw, 150px)', use: 'Cover wordmark only' },
  { level: 'h2', family: 'serif', weight: 400, size: '44px', use: 'Section headlines' },
  { level: 'lead', family: 'serif', weight: 300, size: '23px', use: 'Positioning lines, pull-quotes' },
  { level: 'eyebrow', family: 'sans', weight: 500, size: '11px', use: 'Section labels, category tags (uppercase, 0.42em tracking)' },
  { level: 'body', family: 'sans', weight: 300, size: '16.5px', use: 'Paragraph copy, 62–66ch max width' },
  { level: 'caption', family: 'sans', weight: 400, size: '13px', use: 'Specs, captions, fine print' },
] as const

export type TypeLevel = (typeof typeScale)[number]['level']
