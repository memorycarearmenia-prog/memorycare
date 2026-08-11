// MONTEC design system — public API.
// Source of truth for brand facts: montec/CLAUDE.md and
// montec/docs/planning/Montec_Brand_Book.html / Montec_Brand_Guide.pdf.

export * from './tokens'
export * from './components/Surface'
export * from './components/Logo'
export * from './components/Typography'
export * from './components/Button'

// Consumers import styles separately: `import '@montec/design-system/styles.css'`
// (built by `npm run build:css` from ./src/styles.css — see package.json "exports").
