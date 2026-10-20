<script setup lang="ts">
const fieldValue = ref('Алексей Морозов')
const activeTab = ref('actions')

const tabs = [
  { key: 'actions', label: 'Действия' },
  { key: 'fields', label: 'Поля' },
  { key: 'states', label: 'Состояния' },
]
</script>

<template>
  <div class="card-components">
    <p class="eyebrow">COMPONENT LANGUAGE</p>
    <div class="group">
      <span class="label">Действия</span>
      <div class="actions">
        <UiButton variant="primary">Создать сделку</UiButton>
        <UiButton variant="secondary">Сохранить</UiButton>
        <UiButton variant="ghost">Открыть →</UiButton>
      </div>
    </div>
    <div class="group">
      <span class="label">Состояния</span>
      <div class="states">
        <UiStatus variant="pill" label="В работе" />
        <UiStatus variant="tag" label="По плану" />
      </div>
    </div>
    <div class="group">
      <span class="label">Поле</span>
      <UiInput v-model="fieldValue" label="Клиент" />
    </div>
    <div class="group">
      <span class="label">Tabs</span>
      <UiTabs v-model="activeTab" :tabs="tabs" />
    </div>
  </div>
</template>

<style scoped>
.card-components {
  padding: 20px;
}

.eyebrow {
  margin: 0 0 12px;
  color: var(--accent-strong);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.group {
  padding: 13px 0;
  border-top: 1px solid var(--border);
}

.group:first-of-type {
  border-top: 0;
  padding-top: 0;
}

.label {
  display: block;
  margin-bottom: 9px;
  color: var(--muted);
  font: 10px var(--font-mono);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.states {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
}
</style>
