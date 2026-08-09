/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{ts,tsx}', './.storybook/**/*.{ts,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Primary palette — locked, see montec/CLAUDE.md "Visual identity"
        obsidian: '#0A0A0A',
        brass: {
          DEFAULT: '#B8975A',
          soft: '#C9AE7C',
          wash: '#EDE5D4', // 20% tint on Warm Paper
        },
        anthracite: {
          DEFAULT: '#2B2B2B',
          deep: '#3A3A3A',
        },
        paper: {
          DEFAULT: '#FAF8F3',
          2: '#F1ECE2',
        },
        'obsidian-wash': '#CAC8C4', // 20% tint on Warm Paper
        montgrey: '#8C8C8C',
      },
      fontFamily: {
        // Display/serif: headlines, wordmark, product names, pull-quotes — never body copy
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        // Text/sans: body, captions, interface, specs
        sans: ['Inter', '-apple-system', 'system-ui', 'sans-serif'],
        // Armenian companions (Section 05.3 of the Brand Guide) — Latin faces above have no Armenian glyphs
        'serif-hy': ['"Noto Serif Armenian"', '"Cormorant Garamond"', 'serif'],
        'sans-hy': ['"Noto Sans Armenian"', 'Inter', 'sans-serif'],
      },
      letterSpacing: {
        wordmark: '0.22em',
        eyebrow: '0.42em',
      },
      fontSize: {
        display: ['clamp(4rem, 13vw, 9.375rem)', { lineHeight: '1', fontWeight: '500' }],
        'h2-serif': ['2.75rem', { lineHeight: '1.12', fontWeight: '400' }],
        lead: ['1.4375rem', { lineHeight: '1.55', fontWeight: '300' }],
        eyebrow: ['0.6875rem', { lineHeight: '1', letterSpacing: '0.42em', fontWeight: '500' }],
        body: ['1.03125rem', { lineHeight: '1.7', fontWeight: '300' }],
        caption: ['0.8125rem', { lineHeight: '1.5', fontWeight: '400' }],
      },
      boxShadow: {
        card: '0 18px 40px rgba(0,0,0,0.45)',
      },
    },
  },
  // Brass is the one accent — 6% of visual weight per the Brand Guide's ratio guide.
  // Never introduce a second accent hue without updating montec/CLAUDE.md first.
  plugins: [],
}
