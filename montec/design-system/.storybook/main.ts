import type { StorybookConfig } from '@storybook/react-vite'

const config: StorybookConfig = {
  stories: ['../src/**/*.stories.@(ts|tsx)'],
  addons: ['@storybook/addon-essentials', '@storybook/addon-interactions'],
  framework: {
    name: '@storybook/react-vite',
    options: {},
  },
  docs: {
    autodocs: 'tag',
  },
  async viteFinal(config) {
    // The default Vite build code-splits CSS and loads it through the
    // `crossorigin` modulepreload helper. In sandboxed / file-served contexts
    // that helper throws "Unable to preload CSS for …/preview-*.css" and every
    // story renders as an error page — i.e. `storybook build` produced a static
    // site that could not actually run. Emitting one non-split stylesheet and
    // skipping module preload removes that failure path entirely.
    config.build = {
      ...config.build,
      cssCodeSplit: false,
      modulePreload: false,
    }
    return config
  },
}

export default config
