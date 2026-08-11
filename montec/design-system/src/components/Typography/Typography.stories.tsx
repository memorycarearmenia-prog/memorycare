import type { Meta, StoryObj } from '@storybook/react'
import React from 'react'
import { Typography } from './Typography'
import { Surface } from '../Surface/Surface'

// Every story establishes its own ground via <Surface>. Typography renders in
// Warm Paper and is invisible on a white page, so a story that relied on the
// storybook `backgrounds` parameter alone would look correct in storybook and
// broken everywhere else the story is rendered (preview cards, docs, design
// tools). Grounding the story makes it self-describing.
const meta: Meta<typeof Typography> = {
  title: 'MONTEC/Typography',
  component: Typography,
  parameters: { layout: 'padded' },
  argTypes: {
    variant: { control: 'select', options: ['display', 'h2', 'lead', 'eyebrow', 'body', 'caption'] },
    lang: { control: 'radio', options: ['en', 'hy'] },
  },
  decorators: [
    (Story) => (
      <Surface tone="obsidian">
        <Story />
      </Surface>
    ),
  ],
}
export default meta
type Story = StoryObj<typeof Typography>

export const H2: Story = { args: { variant: 'h2', children: 'Quiet is the loudest luxury.' } }
export const Lead: Story = { args: { variant: 'lead', children: '"I am not rich enough to buy cheap things."' } }
export const Eyebrow: Story = { args: { variant: 'eyebrow', children: 'The Old-Money Code' } }
export const Body: Story = {
  args: {
    variant: 'body',
    children:
      'Montec belongs to the "old money" tradition of luxury: value carried quietly, legible only to those who know what they are looking at.',
  },
}
export const ArmenianLead: Story = {
  args: { variant: 'lead', lang: 'hy', children: 'Խնամքը, որը կարևոր է' },
}

export const FullHierarchy: Story = {
  render: () => (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
      <Typography variant="eyebrow">The Old-Money Code</Typography>
      <Typography variant="h2">Quiet is the loudest luxury.</Typography>
      <Typography variant="lead">Craftsmanship and strategy for those who write history.</Typography>
      <Typography variant="body">
        Montec is quiet-luxury leather for people who have nothing to prove and everything to protect: their
        time, their reputation, their word.
      </Typography>
      <Typography variant="caption">Batch 001 · Piece 07 / 13 · Made in Armenia</Typography>
    </div>
  ),
}
