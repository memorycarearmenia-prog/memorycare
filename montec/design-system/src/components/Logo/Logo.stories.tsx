import type { Meta, StoryObj } from '@storybook/react'
import React from 'react'
import { Logo } from './Logo'

const meta: Meta<typeof Logo> = {
  title: 'MONTEC/Logo',
  component: Logo,
  parameters: { layout: 'centered' },
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
  parameters: { backgrounds: { default: 'paper' } },
}

export const Reversed: Story = {
  args: { variant: 'reversed', size: 40 },
  parameters: { backgrounds: { default: 'obsidian' } },
}

export const Avatar: Story = {
  args: { variant: 'avatar', size: 28 },
  parameters: { backgrounds: { default: 'obsidian' } },
}

export const AllVariants: Story = {
  render: () => (
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
  ),
}
