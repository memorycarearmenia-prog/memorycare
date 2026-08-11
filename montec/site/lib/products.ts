/**
 * Batch 001 — the locked 13-piece lineup.
 * Source of truth: montec/CLAUDE.md ("MONTEC Batch 001 — full launch product list").
 *
 * Prices are deliberately absent from this file and from the site. Every piece
 * is released by application and the number is given in the reply — so the
 * interface has no price to render, by construction rather than by omission.
 * The canonical AMD price table lives in montec/CLAUDE.md; if a price ever has
 * to appear here again, that is a business decision to confirm first, not a
 * gap to fill in.
 *
 * THE AUDIT: the brand's fixed 5-field spec taxonomy (EXTERNAL / ARCHITECTURE /
 * VOLUME / HARDWARE / MARKINGS), identical on every product page. Values state
 * only what is actually known — material, construction, use-case, hardware and
 * marking treatment. No invented dimensions or capacities.
 */

export type Group =
  | 'Carry'
  | 'Command center'
  | 'Financial'
  | 'Lifestyle'
  | 'Foundation'

export interface Audit {
  external: string
  architecture: string
  volume: string
  hardware: string
  markings: string
}

export interface Product {
  slug: string
  /** Display name, always upper-case in the interface. */
  name: string
  /** The object it is, in plain words. */
  object: string
  group: Group
  /** The one-line positioning subtitle, set in italic serif on the page. */
  line: string
  body: string
  audit: Audit
}

const LEATHER = '100% full-grain vegetable-tanned Italian leather'
const BRASS = 'Solid Italian brass'
const EMBOSS = 'Blind emboss, tone-on-tone. No ink, no foil.'

export const products: Product[] = [
  {
    slug: 'the-founder',
    name: 'The Founder',
    object: 'Weekender',
    group: 'Carry',
    line: 'Scale and strategy.',
    body: 'The flagship. A vessel for those who write history rather than participate in it — sized for the trip that decides something, built to be the oldest thing you still carry in twenty years.',
    audit: {
      external: LEATHER,
      architecture: 'Structured weekender body, reinforced base, twin rolled handles',
      volume: 'Two to four days away, carried by hand or on the shoulder',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-executive',
    name: 'The Executive',
    object: 'Briefcase',
    group: 'Carry',
    line: 'The control center.',
    body: 'The briefcase the rest of the batch attaches to. Its MONTEC RAIL™ dock accepts The Unit, so the case adapts to the day instead of the day adapting to the case.',
    audit: {
      external: LEATHER,
      architecture: 'MONTEC RAIL™ integrated framework for modular expansion',
      volume: 'Documents, laptop and the docked Unit',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-unit',
    name: 'The Unit',
    object: 'Laptop module',
    group: 'Carry',
    line: 'Removable, and never an afterthought.',
    body: 'A laptop case that docks into The Executive via MONTEC RAIL™ and detaches to travel alone. The half of the system that makes the other half modular.',
    audit: {
      external: LEATHER,
      architecture: 'MONTEC RAIL™ dock interface; carries independently when detached',
      volume: 'One laptop and its cable',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-closer',
    name: 'The Closer',
    object: 'Messenger bag',
    group: 'Carry',
    line: 'The negotiation weapon.',
    body: 'Fast, bold, decisive — the piece for the meeting that ends in a handshake. Single strap, single motion, nothing between you and the document you came to sign.',
    audit: {
      external: LEATHER,
      architecture: 'Single-strap messenger body with flap closure',
      volume: 'Documents, tablet, the essentials of a working day',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-arena',
    name: 'The Arena',
    object: 'Desk mat',
    group: 'Command center',
    line: 'The battlefield.',
    body: 'The leather foundation of the desk. It defines the boundaries of your influence over the workspace — everything that matters happens inside its edges.',
    audit: {
      external: LEATHER,
      architecture: 'Single-panel mat, edge-finished by hand',
      volume: 'Full working width of a desk',
      hardware: 'None — a single uninterrupted surface',
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-brief',
    name: 'The Brief',
    object: "Men's clutch",
    group: 'Command center',
    line: 'What matters most, on the move.',
    body: 'The operational brief: phone, keys, cards, and nothing you will not use today. Carried in the hand, which is its own kind of statement.',
    audit: {
      external: LEATHER,
      architecture: 'Zip-closed clutch with internal division',
      volume: 'Phone, keys, cards, a folded document',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-capital',
    name: 'The Capital',
    object: 'Bifold wallet',
    group: 'Financial',
    line: 'Daily resources.',
    body: 'The classic, executed perfectly. A foundation for the daily flow of trade — and the piece most likely to outlast every other thing in your pocket.',
    audit: {
      external: LEATHER,
      architecture: 'Bifold, hand-skived edges, no lining bulk',
      volume: 'Notes and cards, carried flat',
      hardware: 'None — a deliberately hardware-free build',
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-treasury',
    name: 'The Treasury',
    object: 'Long wallet',
    group: 'Financial',
    line: 'Order in money.',
    body: 'Respect for larger assets. Notes lie flat and unfolded, documents keep their shape, and nothing is bent to fit a pocket that was never the point.',
    audit: {
      external: LEATHER,
      architecture: 'Long-format, full-width note compartment',
      volume: 'Unfolded notes, cards, travel documents',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-access',
    name: 'The Access',
    object: 'Cardholder',
    group: 'Financial',
    line: 'The universal pass.',
    body: 'The entry piece, and the first Montec most people own. Minimalist, zero friction — the whole system in the smallest object it makes.',
    audit: {
      external: LEATHER,
      architecture: 'Slim cardholder, hand-skived edges',
      volume: 'Cards and a folded note',
      hardware: 'None — a deliberately hardware-free build',
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-voyager',
    name: 'The Voyager',
    object: 'Dopp kit',
    group: 'Lifestyle',
    line: 'Ritual, at any coordinate.',
    body: 'Standards do not travel well unless you bring them. Personal comfort and routine, kept intact in whichever city the week ends in.',
    audit: {
      external: LEATHER,
      architecture: 'Zip-top kit, structured base',
      volume: 'A full travel routine',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-vision',
    name: 'The Vision',
    object: 'Glasses case',
    group: 'Lifestyle',
    line: 'Focus protection.',
    body: 'Armour for the lenses through which you read a room and a balance sheet. Small, rigid, and quietly serious about its one job.',
    audit: {
      external: LEATHER,
      architecture: 'Rigid shell, soft-lined interior',
      volume: 'One pair of frames',
      hardware: 'None — a single closed form',
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-backbone',
    name: 'The Backbone',
    object: 'Belt, brown',
    group: 'Foundation',
    line: 'Character under load.',
    body: 'The spine. It carries weight without complaint and takes on the shape of the person wearing it — which is the entire argument for vegetable tanning.',
    audit: {
      external: LEATHER,
      architecture: 'Single-ply strap, hand-finished edge',
      volume: 'Made to a measured waist',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
  {
    slug: 'the-standard',
    name: 'The Standard',
    object: 'Belt, black',
    group: 'Foundation',
    line: 'Discipline and flawless protocol.',
    body: 'The benchmark. Black, exact, and unremarkable in the way that only a correct thing can be — which is the highest compliment this brand pays an object.',
    audit: {
      external: LEATHER,
      architecture: 'Single-ply strap, hand-finished edge',
      volume: 'Made to a measured waist',
      hardware: BRASS,
      markings: EMBOSS,
    },
  },
]

export const BATCH = '001'
export const total = products.length

export function bySlug(slug: string) {
  return products.find((p) => p.slug === slug)
}

/** "01" … "13" — the piece's position in the batch. Real sequence, not decoration. */
export function indexOf(slug: string) {
  return String(products.findIndex((p) => p.slug === slug) + 1).padStart(2, '0')
}

export function nextOf(slug: string) {
  const i = products.findIndex((p) => p.slug === slug)
  return products[(i + 1) % products.length]
}


