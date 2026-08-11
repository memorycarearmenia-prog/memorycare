/** @type {import('next').NextConfig} */
const nextConfig = {
  // Static export: every route ships as pre-rendered HTML. This is the whole
  // reason for Next here — the competitor's moat is search, and a client-only
  // SPA forfeits it.
  output: 'export',
  images: { unoptimized: true },
  trailingSlash: true,
  transpilePackages: ['@montec/design-system'],
}
export default nextConfig
