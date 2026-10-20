<script setup lang="ts">
import { languages, skills } from '~/utils/resume'

definePageMeta({ layout: 'workspace' })
useHead({ title: 'Навыки — Семён Сергеев' })
</script>

<template>
  <div class="skl">
    <UiEyebrow>НАВЫКИ / {{ skills.reduce((sum, group) => sum + group.items.length, 0) }}+</UiEyebrow>
    <h1>Стек и инструменты</h1>

    <div class="skl-langs">
      <span class="skl-label mono">Языки</span>
      <div class="skl-lang-row">
        <UiStatus v-for="lang in languages" :key="lang.label" variant="dark" :label="`${lang.label} · ${lang.level}`" />
      </div>
    </div>

    <section v-for="group in skills" :key="group.label" class="skl-group">
      <h2>{{ group.label }}</h2>
      <div class="skl-tags">
        <UiStatus v-for="item in group.items" :key="item" variant="tag" :label="item" />
      </div>
    </section>
  </div>
</template>

<style scoped>
.skl {
  display: grid;
  gap: var(--space-4);
}

h1 {
  font-size: clamp(24px, 4vw, 34px);
  letter-spacing: -0.03em;
  margin-bottom: var(--space-2);
}

.skl-langs {
  display: grid;
  gap: var(--space-2);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--border);
}

.skl-label {
  color: var(--muted);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.skl-lang-row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.skl-group {
  display: grid;
  gap: var(--space-2);
}

.skl-group h2 {
  margin: 0;
  color: var(--muted);
  font: 10px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.skl-tags {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
</style>
