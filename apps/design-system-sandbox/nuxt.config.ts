import { fileURLToPath } from 'node:url'

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  components: {
    dirs: [
      fileURLToPath(new URL('./app/components', import.meta.url)),
      {
        path: fileURLToPath(new URL('../../libs/rolftech-core-ui/src/components', import.meta.url)),
        prefix: 'Ui',
        pathPrefix: false,
      },
    ],
  },
  build: { transpile: ['@rolftech/core-ui'] },
  nitro: {
    preset: 'vercel',
    output: {
      dir: fileURLToPath(new URL('.vercel/output', import.meta.url)),
    },
  },
  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
    head: {
      htmlAttrs: { lang: 'ru' },
      title: 'ROLFTECH Core — дизайн-система',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Песочница дизайн-системы ROLFTECH Core и библиотеки @rolftech/core-ui.' },
      ],
    },
  },
})
