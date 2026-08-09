/**
 * MONTEC colour tokens. Source of truth: montec/CLAUDE.md "Visual identity"
 * and montec/docs/planning/Montec_Brand_Book.html Section 04.
 *
 * Ratio guide: Obsidian 70% · Anthracite/Paper 24% · Brass 6%.
 * Brass is the one accent — never introduce a second accent hue here
 * without updating the Brand Book and this file together.
 */
export const colors = {
  // Primary palette
  obsidian: '#0A0A0A',
  brass: '#B8975A',
  brassSoft: '#C9AE7C',
  anthracite: '#2B2B2B',
  anthraciteDeep: '#3A3A3A',
  paper: '#FAF8F3',
  paper2: '#F1ECE2',
  grey: '#8C8C8C',

  // Secondary / tint palette (Brand Guide Section 04.2)
  brassWash: '#EDE5D4', // Brass at 20% over Warm Paper
  obsidianWash: '#CAC8C4', // Obsidian at 20% over Warm Paper
} as const

export type ColorToken = keyof typeof colors

/** The line/hairline rule colour used across dividers, table borders, card outlines. */
export const line = 'rgba(184, 151, 90, 0.28)'
