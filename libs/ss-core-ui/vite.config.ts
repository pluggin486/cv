import { resolve } from 'node:path'
import { fileURLToPath } from 'node:url'
import vue from '@vitejs/plugin-vue'
import { defineConfig } from 'vite'

const libraryRoot = fileURLToPath(new URL('.', import.meta.url))

export default defineConfig({
  root: libraryRoot,
  plugins: [vue()],
  build: {
    outDir: resolve(libraryRoot, 'dist'),
    emptyOutDir: true,
    cssCodeSplit: false,
    lib: {
      entry: resolve(libraryRoot, 'src/index.ts'),
      formats: ['es'],
      fileName: 'index',
      cssFileName: 'style',
    },
    rollupOptions: {
      external: ['vue'],
    },
  },
})
