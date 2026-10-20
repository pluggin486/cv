<script setup lang="ts">
import FreelanceEvidence from '~/components/freelance/FreelanceEvidence.vue'
import FreelanceHero from '~/components/freelance/FreelanceHero.vue'
import FreelanceServices from '~/components/freelance/FreelanceServices.vue'
import { freelanceProfile, freelanceProof, freelanceServices } from '~/utils/freelance'

definePageMeta({ layout: false })

useHead({
  title: 'Семён Сергеев — Vue / Nuxt разработчик',
  meta: [
    {
      name: 'description',
      content: 'Портфолио frontend-разработчика: Vue 2/3, Nuxt 3, TypeScript, UI Kit и виртуализация списков.',
    },
    { property: 'og:title', content: 'Семён Сергеев — Vue / Nuxt разработчик' },
    {
      property: 'og:description',
      content: 'Примеры задач и подтверждённые результаты коммерческой frontend-разработки.',
    },
  ],
})
</script>

<template>
  <main class="freelance-page">
    <div class="freelance-page__shell">
      <header class="freelance-topline">
        <span class="freelance-topline__brand">SS <span class="freelance-topline__divider">/</span> ПОРТФОЛИО</span>
        <span class="freelance-topline__note mono">VUE · NUXT · TYPESCRIPT</span>
      </header>

      <FreelanceHero
        :name="freelanceProfile.name"
        :role="freelanceProfile.role"
        :stack="freelanceProfile.stack"
        :availability="freelanceProfile.availability"
        :introduction="freelanceProfile.introduction"
      />

      <FreelanceEvidence :items="freelanceProof" />
      <FreelanceServices :items="freelanceServices" />

      <footer class="freelance-footer">
        <span>Ставка и сроки — после оценки объёма задачи.</span>
        <span class="mono">SS / 2026</span>
      </footer>
    </div>
  </main>
</template>

<style scoped>
.freelance-page {
  min-height: 100vh;
  padding: clamp(20px, 5vw, 68px) 20px;
  background:
    radial-gradient(ellipse at 10% 0%, color-mix(in oklch, var(--accent-soft) 45%, transparent), transparent 34rem),
    var(--bg);
}

.freelance-page__shell {
  width: min(1040px, 100%);
  margin-inline: auto;
  display: grid;
  gap: clamp(46px, 8vw, 88px);
}

.freelance-topline,
.freelance-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--space-3);
}

.freelance-topline {
  padding-bottom: 13px;
  border-bottom: 1px solid var(--border);
  color: var(--muted);
  font-size: 11px;
}

.freelance-topline__brand {
  color: var(--fg);
  font-weight: 750;
  letter-spacing: 0.04em;
}

.freelance-topline__divider {
  margin-inline: 4px;
  color: var(--accent-strong);
}

.freelance-topline__note {
  font-size: 9px;
  letter-spacing: 0.08em;
}

.freelance-footer {
  padding-top: 16px;
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: 11px;
}

@media (max-width: 520px) {
  .freelance-page {
    padding-inline: 15px;
  }

  .freelance-topline__note {
    display: none;
  }

  .freelance-footer {
    align-items: flex-start;
    flex-direction: column;
  }
}
</style>
