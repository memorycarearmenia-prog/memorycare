import type { MetadataRoute } from 'next'
import { products } from '@/lib/products'

const SITE = 'https://montec.am'

export default function sitemap(): MetadataRoute.Sitemap {
  const staticRoutes = ['', '/collection', '/code', '/corporate', '/about', '/request']
  return [
    ...staticRoutes.map((r) => ({
      url: `${SITE}${r}/`,
      changeFrequency: 'monthly' as const,
      priority: r === '' ? 1 : 0.8,
    })),
    ...products.map((p) => ({
      url: `${SITE}/collection/${p.slug}/`,
      changeFrequency: 'monthly' as const,
      priority: 0.7,
    })),
  ]
}
