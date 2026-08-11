# design-sync notes — @montec/design-system

Repo layout: this is **not** a JS repo at the root. The root holds two unrelated
businesses' documents (Memory Care, MONTEC); the design system is one subpackage
at `montec/design-system/`. Run everything from the repo root, pass
`--node-modules montec/design-system/node_modules` and
`--entry montec/design-system/dist/index.js`. There is no root `package.json` or
lockfile — the only lockfile is the package's own.

## Environment

- **Chromium**: the sandbox can't `playwright install`. A system chromium exists —
  export `DS_CHROMIUM_PATH=/opt/pw-browsers/chromium` for every `package-validate.mjs`
  and `compare.mjs` run, or capture fails at launch.
- **Network egress in capture**: `curl` reaches the internet through `HTTPS_PROXY`,
  but the chromium the harness launches does **not** inherit that proxy. Anything a
  page fetches from an external host during capture will fail. This is why the fonts
  are self-hosted (below) rather than CDN-loaded — see `[ASSETS_BLOCKED]` history.

## Fixes this sync made (both were real defects, not sync workarounds)

- `[GENERAL]` **Static Storybook build produced a non-functional site.** Every story
  in `.design-sync/sb-reference` rendered as an error page — `Unable to preload CSS
  for …/preview-*.css` — so the first compare run returned 15/15 `sb-error` and the
  oracle was useless. Cause: Vite code-splits the preview CSS and loads it through
  the `crossorigin` modulepreload helper, which throws in this serving context.
  Fix: `viteFinal` in `montec/design-system/.storybook/main.ts` sets
  `build.cssCodeSplit: false` + `build.modulePreload: false`, so the CSS ships as one
  plain `<link rel="stylesheet">`. This also repaired the repo's own
  `npm run build-storybook`, which had the same breakage.
- `[GENERAL]` **Brand fonts moved from Google Fonts CDN to self-hosted.** The package
  previously `@import`ed `fonts.googleapis.com` from `src/styles.css`. During capture
  that host is unreachable (above), so **both** panels fell back to the same system
  font — `[ASSETS_BLOCKED]` — which is exactly the failure mode where grades pass
  falsely while real users see something else. Beyond verification, a CDN dependency
  is a poor fit for this brand: typography is load-bearing (the wordmark's 0.22em
  tracking is the signature), so a blocked or slow font host degrades the brand
  silently. Fix: 23 woff2 files in `montec/design-system/src/fonts/` (~600 KB, all
  4 families × latin/latin-ext/cyrillic/cyrillic-ext/armenian/greek/vietnamese
  subsets), generated `src/fonts.css` with 71 `@font-face` rules pointing at them,
  `src/styles.css` imports that instead of the remote URL, and `build:css` copies
  `src/fonts/` → `dist/fonts/`. Verified: 71/71 url() references resolve, 0 remote
  references remain, and validate's `[FONT_REMOTE]` warning is gone.

- `[GENERAL]` **Stories depended on the storybook `backgrounds` addon to be legible.**
  The first honest compare showed every preview rendering light-on-white:
  Typography (all 6 stories), `Button` primary/ghost, `Logo` reversed — all
  invisible. Storybook painted its canvas from `parameters.backgrounds`, the
  preview card did not, so the components lost the ground they silently depended
  on. This would have shipped blank-looking cards to Claude Design and taught the
  design agent nothing about the dark-first contract. Fix: added a real
  **`Surface`** component (obsidian / anthracite / paper grounds, exported from
  the package) and made every story carry its own ground via story-level
  `decorators` — per-story on `Logo`, whose primary lockup needs a *light* ground
  while reversed needs a dark one, so no single global `cfg.provider` could serve
  both. Stories are now self-describing and previews match the reference exactly.
  `Surface` is also what the conventions header instructs the design agent to
  wrap in.
  - Note for next time: story-level `decorators` **do** reach previews — the
    generated wrapper composes `story.decorators` then `meta.decorators`. The
    `.storybook/preview.tsx` global decorator is the one that's lost when the
    decorator bundle fails, and it only added padding.

## Known, accepted

- `! preview decorator bundle failed: No loader is configured for ".woff2"` — the
  decorator bundle in `lib/source-storybook.mjs` uses a hardcoded loader map
  (`.js`, `.json` only), unlike the story-preview compile which already maps
  `.woff2 → dataurl` via `STORY_LOADERS`. Since `.storybook/preview.tsx` imports
  `src/styles.css`, and that chain now reaches woff2 files, the decorator bundle
  fails. **Accepted deliberately**: the decorator contributes only `padding: 32`
  and a wrapper `fontFamily` — pure framing, which the grading rubric says to
  ignore — and component CSS reaches previews through the converter's own css
  path (`styles.css` → `_ds_bundle.css`), not through the decorators. Not
  config-fixable: `cfg.storyImports.loaders` feeds the preview compile and
  `preview-rebuild`, not the decorator bundle.
- `Colors` is excluded via `cfg.titleMap {"Colors": null}`. `src/tokens/Colors.stories.tsx`
  is a palette *showcase*, not a package export — there is no `Colors` component to
  bundle, so it can't be a synced component. The colour tokens themselves still reach
  the design agent as `window.MontecDesignSystem.colors` and through `tokens/`.

- `[REFERENCE_STALE?]` fires whenever the bundle is rebuilt after the reference,
  since it compares mtimes. On this run it was a false positive — the storybook
  panel demonstrably showed the new Surface-grounded stories. Don't ignore it
  blindly: confirm from the sheet that the storybook side shows current design.

## Upload status (2026-08-11)

**Nothing was uploaded.** `DesignSync` could not authorize — this session runs in
claude.ai/code where `/design-login` needs an interactive terminal, and the grant
is issued at session creation, so re-running `/design-sync` here can never fix it.
The tool's own fallback ("provide the project files directly") was taken: the
verified `ds-bundle/` is the deliverable. No Claude Design project exists yet, so
`config.json` has no `projectId` and there is no `_ds_sync.json` anchor remotely —
the next sync is correctly a first sync. To finish: open the project from Claude
Design via "Send to Claude Code Web" (that session gets the grant) and run
`/design-sync` there; everything in `.design-sync/` is committed, so it replays
this run's decisions instead of rediscovering them.

## Re-sync risks — what to watch

- **Fonts are a vendored copy.** `src/fonts/*.woff2` + `src/fonts.css` were generated
  from the Google Fonts css2 API on 2026-08-11 and will not update themselves. If the
  brand adds a weight/family, regenerate both together (the header comment in
  `fonts.css` says how) — a weight added to `tailwind.config.js` or a component
  without a matching `@font-face` fails silently to a fallback face.
- **The storybook `viteFinal` block is load-bearing for the oracle.** If someone
  "cleans up" `main.ts` and drops it, every story goes back to `sb-error` and the
  whole sync is unverifiable. The symptom is unmistakable; the cause is not.
- **Scope is MVP.** Only Logo, Typography, Button are synced components. The Brand
  Guide's product card, THE AUDIT spec table, SKU/pricing table and stationary suite
  are documented but unbuilt — when they land, they arrive as new components with no
  carried grades.
- **Prices in prompts/docs**: 5 of the 13 Batch 001 SKUs are still TBD. Nothing in
  this package hardcodes prices, but README/prompt copy generated from repo docs may
  quote the confirmed 8 — re-check against `montec/CLAUDE.md` if it drifts.
