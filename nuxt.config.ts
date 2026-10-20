import { fileURLToPath } from 'node:url'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  components: {
    dirs: [
      fileURLToPath(new URL('./app/components', import.meta.url)),
      {
        path: fileURLToPath(new URL('./libs/rolftech-core-ui/src/components', import.meta.url)),
        prefix: 'Ui',
        pathPrefix: false,
      },
    ],
  },
  build: { transpile: ['@rolftech/core-ui'] },
  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
    head: {
      htmlAttrs: { lang: 'ru' },
      title: 'Семён Сергеев — Frontend Developer',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Семён Сергеев — Frontend Developer. Vue 3 / Nuxt / TypeScript. Визитка на дизайн-системе ROLFTECH Core.' },
        { property: 'og:title', content: 'Семён Сергеев — Frontend Developer' },
        { property: 'og:description', content: 'Vue 3 / Nuxt / TypeScript · 3+ года опыта · UI Kit · виртуализация · −70% CI' },
      ],
      script: [
        {
          innerHTML: "(function(){try{var t=localStorage.getItem('rt-theme');if(t!=='dark'&&t!=='light'){t=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}document.documentElement.dataset.theme=t}catch(e){}})()",
        },
      ],
    },
  },
})
