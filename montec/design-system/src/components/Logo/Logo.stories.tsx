import type { Meta, StoryObj } from '@storybook/react'
import React from 'react'
import { Logo } from './Logo'
import { Surface } from '../Surface/Surface'

// Logo is the one component whose ground varies per story: the primary lockup
// is near-black and needs a light ground, the reversed lockup is Warm Paper and
// needs a dark one. So the tone is set per story rather than once on the meta —
// each story still carries its own ground and never depends on the storybook
// `backgrounds` parameter to be legible.
const meta: Meta<typeof Logo> = {
  title: 'MONTEC/Logo',
  component: Logo,
  parameters: { layout: 'padded' },
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'reversed', 'monochrome-dark', 'monochrome-light', 'avatar'],
    },
  },
}
export default meta
type Story = StoryObj<typeof Logo>

export const Primary: Story = {
  args: { variant: 'primary', size: 40 },
  decorators: [(S) => <Surface tone="paper"><S /></Surface>],
}

export const Reversed: Story = {
  args: { variant: 'reversed', size: 40 },
  decorators: [(S) => <Surface tone="obsidian"><S /></Surface>],
}

export const Avatar: Story = {
  args: { variant: 'avatar', size: 28 },
  decorators: [(S) => <Surface tone="obsidian"><S /></Surface>],
}

export const AllVariants: Story = {
  render: () => (
    <Surface tone="obsidian">
      <div style={{ display: 'flex', gap: 40, alignItems: 'center', flexWrap: 'wrap' }}>
        <div style={{ background: '#FAF8F3', padding: 24 }}>
          <Logo variant="primary" size={36} />
        </div>
        <div style={{ background: '#0A0A0A', padding: 24 }}>
          <Logo variant="reversed" size={36} />
        </div>
        <div style={{ background: '#0A0A0A', padding: 24 }}>
          <Logo variant="monochrome-light" size={36} />
        </div>
        <div style={{ background: '#FAF8F3', padding: 24 }}>
          <Logo variant="monochrome-dark" size={36} />
        </div>
        <div style={{ background: '#0A0A0A', padding: 24 }}>
          <Logo variant="avatar" size={28} />
        </div>
      </div>
    </Surface>
  ),
}
