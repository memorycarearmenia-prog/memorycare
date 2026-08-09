import type { Meta, StoryObj } from '@storybook/react'
import React from 'react'
import { colors } from './colors'

const swatchMeta: Record<string, string> = {
  obsidian: 'The ground. Backgrounds, the wordmark, the product\'s soul.',
  brass: 'The single accent. Hardware, rules, emphasis. Use sparingly.',
  brassSoft: 'Hover/active state for brass elements; taglines on dark.',
  anthracite: 'The mid-tone. Panels, dividers, depth without contrast.',
  anthraciteDeep: 'Card fills and panel gradients one step off pure Obsidian.',
  paper: 'Light ground for print & documents. Where prose reads.',
  paper2: 'Secondary paper tone for layered light surfaces.',
  grey: 'Muted captions and de-emphasized text.',
  brassWash: 'Brass at 20% tint — soft backgrounds, hover fills.',
  obsidianWash: 'Obsidian at 20% tint — secondary text on paper, disabled states.',
}

function Palette() {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(180px, 1fr))', gap: 16 }}>
      {Object.entries(colors).map(([name, hex]) => (
        <div key={name} style={{ border: '1px solid rgba(255,255,255,0.08)', borderRadius: 4, overflow: 'hidden' }}>
          <div style={{ height: 88, background: hex }} />
          <div style={{ padding: 12, background: '#141414' }}>
            <div style={{ fontFamily: 'Cormorant Garamond, serif', fontSize: 17, color: '#FAF8F3' }}>{name}</div>
            <div style={{ fontFamily: 'Inter, sans-serif', fontSize: 11, letterSpacing: '0.1em', color: '#B8975A', marginTop: 4 }}>
              {hex}
            </div>
            <div style={{ fontFamily: 'Inter, sans-serif', fontSize: 11, color: '#8C8C8C', marginTop: 6, lineHeight: 1.5 }}>
              {swatchMeta[name] ?? ''}
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}

const meta: Meta = {
  title: 'MONTEC/Tokens/Colors',
  parameters: { layout: 'padded', backgrounds: { default: 'obsidian' } },
}
export default meta
type Story = StoryObj

export const AllColors: Story = { render: () => <Palette /> }
