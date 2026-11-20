import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { legacyArchive, legacyArchiveBuild } from './scripts/legacyArchive.ts';
import { astryxStylex } from '@astryxdesign/build/vite';

export default defineConfig({
  plugins: [
    legacyArchive(),
    legacyArchiveBuild(),
    ...astryxStylex({
      stylexOptions: {
        dev: process.env.NODE_ENV === 'development',
        runtimeInjection: false,
        propertyValidationMode: 'throw',
        treeshakeCompensation: true,
        unstable_moduleResolution: {
          type: 'commonJS',
          rootDir: process.cwd(),
        },
      },
    }),
    react(),
  ],
  appType: 'spa',
  resolve: {
    alias: {
      '@astryxdesign/core': new URL('./node_modules/@astryxdesign/core/src', import.meta.url).pathname,
    },
  },
  optimizeDeps: {
    exclude: ['@astryxdesign/core', '@astryxdesign/theme-neutral'],
  },
  server: { host: '127.0.0.1' },
});
