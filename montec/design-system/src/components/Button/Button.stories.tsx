import type { Meta, StoryObj } from '@storybook/react'
import React from 'react'
import { Button } from './Button'

const meta: Meta<typeof Button> = {
  title: 'MONTEC/Button',
  component: Button,
  parameters: { layout: 'centered', backgrounds: { default: 'obsidian' } },
  argTypes: {
    variant: { control: 'select', options: ['primary', 'secondary', 'ghost'] },
    size: { control: 'radio', options: ['default', 'small'] },
  },
}
export default meta
type Story = StoryObj<typeof Button>

export const Primary: Story = { args: { variant: 'primary', children: 'REQUEST ACCESS' } }
export const Secondary: Story = { args: { variant: 'secondary', children: 'Corporate inquiry' } }
export const Ghost: Story = { args: { variant: 'ghost', children: 'View full collection' } }
export const Small: Story = { args: { variant: 'primary', size: 'small', children: 'REQUEST ACCESS' } }

export const AllVariants: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: 16, flexWrap: 'wrap' }}>
      <Button variant="primary">REQUEST ACCESS</Button>
      <Button variant="secondary">Corporate inquiry</Button>
      <Button variant="ghost">View full collection</Button>
    </div>
  ),
}
