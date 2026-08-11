# MONTEC — website

The Batch 001 site: thirteen pieces, sold by application. Next.js App Router,
statically exported — the build produces plain HTML/CSS/JS in `out/` with no
server behind it.

```bash
npm install
npm run dev      # http://localhost:3000
npm run build    # static export into out/
```

## How it is put together

| Path | What lives there |
|---|---|
| `lib/products.ts` | Batch 001 — the single source of truth for names, groups and THE AUDIT copy. Carries no prices at all: see below. |
| `app/collection/[slug]/` | The thirteen product pages, generated from that file at build time. |
| `components/EmbossField.tsx` | The hero. The real macro photograph of the embossed mark sits nearly unlit; a soft light follows the pointer and reveals it. |
| `components/Ledger.tsx` | The collection as a manifest — number, name, object — rather than a photo grid. |
| `components/RequestForm.tsx` | Access and corporate enquiries. A native form POST, so it works with JavaScript off. |
| `public/products/<slug>/` | Product photography, sliced from the canonical turnaround grids in `montec/assets/products/`. |
| `app/fonts.css` | Self-hosted Cormorant Garamond, Inter, and the Noto Armenian companions. No external font requests. |

Design tokens (colours, type scale) come from `@montec/design-system` — the
Tailwind config imports them rather than restating hex values, so the site and
the component package cannot drift.

## Brand rules the code enforces

- **No prices anywhere.** Every piece is released by application and the number
  is given in the reply, so `lib/products.ts` holds no price field and the
  product JSON-LD carries no `offers`. The site cannot show a price by
  construction, not by omission. The canonical AMD table lives in
  `montec/CLAUDE.md`; putting any of it back on the site is a business
  decision to confirm first, not a gap to fill.
- No testimonials, review counts or customer numbers anywhere. Montec is
  pre-launch; the product JSON-LD deliberately carries no rating or stock claim.
- THE AUDIT's five fields (External / Architecture / Volume / Hardware /
  Markings) are identical and in the same order on all thirteen pages.
- No cart and no discount anywhere in the interface — the model is REQUEST
  ACCESS, and the Old-Money Code page says why.

## Deploying

`netlify.toml` is set up for Netlify: base `montec/site`, publish `out`. The
two forms use Netlify Forms, which picks them up from the deployed HTML —
submissions appear in the site's Forms tab, and a notification there forwards
them to an inbox.

To use another form service instead (Formspree and similar), set
`NEXT_PUBLIC_FORM_ENDPOINT` to its URL; both forms post there instead.

Any static host works — the export is just files.

## Still open

- Photography for the pieces whose only source is a turnaround render.
- Armenian and Russian copy. The fonts are already loaded and the Tailwind
  `font-serif-hy` / `font-sans-hy` families are wired for it.
