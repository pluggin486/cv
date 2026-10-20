<script setup lang="ts">
import { projects, projectCategories } from '~/utils/resume'
import type { Project } from '~/utils/resume'

definePageMeta({ layout: 'workspace' })
useHead({ title: 'Проекты — Семён Сергеев' })

const filter = ref('all')

const tabs = projectCategories.map(({ key, label }) => ({ key, label }))

const columns = [
  { key: 'name', label: 'Проект' },
  { key: 'company', label: 'Компания' },
  { key: 'stack', label: 'Стек' },
  { key: 'result', label: 'Ключевой результат' },
]

const filtered = computed<Project[]>(() =>
  filter.value === 'all' ? projects : projects.filter(p => p.category === filter.value),
)
</script>

<template>
  <div class="prj">
    <UiEyebrow>ПРОЕКТЫ / {{ projects.length }}</UiEyebrow>
    <h1>Проекты и результаты</h1>

    <UiTabs v-model="filter" :tabs="tabs" />

    <UiDataTable :columns="columns" :rows="filtered" caption="Портфолио">
      <template #cell-name="{ row }">
        <span class="prj-name">{{ row.name }}</span>
      </template>
      <template #cell-company="{ row }">
        <span class="mono prj-company">{{ row.company }}</span>
      </template>
      <template #cell-stack="{ row }">
        <span class="mono prj-stack">{{ row.stack }}</span>
      </template>
      <template #cell-result="{ row }">
        <span class="prj-result">{{ row.result }}</span>
      </template>
    </UiDataTable>

    <p class="prj-count mono">Показано: {{ filtered.length }} из {{ projects.length }}</p>
  </div>
</template>

<style scoped>
.prj {
  display: grid;
  gap: var(--space-3);
}

h1 {
  font-size: clamp(24px, 4vw, 34px);
  letter-spacing: -0.03em;
  margin-bottom: var(--space-2);
}

.prj :deep(.ui-tabs) {
  margin-bottom: var(--space-2);
}

.prj-name {
  font-weight: 650;
  letter-spacing: -0.01em;
}

.prj-company,
.prj-stack {
  color: var(--muted);
  font-size: 12px;
}

.prj-result {
  color: var(--fg);
  font-size: 13px;
  line-height: 1.45;
}

.prj-count {
  color: var(--muted);
  font-size: 11px;
}
</style>
