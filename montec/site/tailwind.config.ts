import type { Config } from 'tailwindcss'
import { colors as ds } from '@montec/design-system'

// Tokens come from the design system package — one source of truth. If a value
// changes there, it changes here, and the Brand Book stays the authority for both.
const config: Config = {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}', './lib/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        obsidian: ds.obsidian,
        brass: { DEFAULT: ds.brass, soft: ds.brassSoft, wash: ds.brassWash },
        anthracite: { DEFAULT: ds.anthracite, deep: ds.anthraciteDeep },
        paper: { DEFAULT: ds.paper, 2: ds.paper2 },
        ash: ds.grey,
      },
      fontFamily: {
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        sans: ['Inter', '-apple-system', 'system-ui', 'sans-serif'],
        'serif-hy': ['"Noto Serif Armenian"', '"Cormorant Garamond"', 'serif'],
        'sans-hy': ['"Noto Sans Armenian"', 'Inter', 'sans-serif'],
      },
      letterSpacing: {
        wordmark: '0.22em',
        eyebrow: '0.42em',
        wide2: '0.28em',
      },
      maxWidth: { measure: '62ch', lead: '66ch' },
      transitionTimingFunction: { quiet: 'cubic-bezier(0.22, 0.61, 0.36, 1)' },
    },
  },
  plugins: [],
}
export default config
