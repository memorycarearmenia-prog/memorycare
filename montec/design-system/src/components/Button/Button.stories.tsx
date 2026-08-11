import type { Meta, StoryObj } from '@storybook/react'
import React from 'react'
import { Button } from './Button'
import { Surface } from '../Surface/Surface'

// Grounded via <Surface>: the primary button is Warm Paper and the ghost
// variant is Warm Paper text, both of which disappear on a white page. See the
// note in Typography.stories.tsx — stories carry their own ground rather than
// depending on the storybook `backgrounds` parameter.
const meta: Meta<typeof Button> = {
  title: 'MONTEC/Button',
  component: Button,
  parameters: { layout: 'padded' },
  argTypes: {
    variant: { control: 'select', options: ['primary', 'secondary', 'ghost'] },
    size: { control: 'radio', options: ['default', 'small'] },
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
