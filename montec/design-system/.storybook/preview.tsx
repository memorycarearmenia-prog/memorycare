import type { Preview } from '@storybook/react'
import React from 'react'
import '../src/styles.css'

const preview: Preview = {
  parameters: {
    controls: { matchers: { color: /(background|color)$/i, date: /Date$/i } },
    backgrounds: {
      default: 'obsidian',
      values: [
        { name: 'obsidian', value: '#0A0A0A' },
        { name: 'paper', value: '#FAF8F3' },
      ],
    },
  },
  decorators: [
    (Story) => (
      <div style={{ padding: 32, fontFamily: 'Inter, sans-serif' }}>
        <Story />
      </div>
    ),
  ],
}

export default preview
