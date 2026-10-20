<script setup lang="ts">
import type { SideNavGroup } from '../types'

defineProps<{
  groups: SideNavGroup[]
  modelValue: string
}>()

const emit = defineEmits<{ 'update:modelValue': [value: string] }>()
</script>

<template>
  <nav class="ui-sidenav" aria-label="Разделы">
    <div v-for="group in groups" :key="group.label" class="ui-sidenav__group">
      <p class="ui-sidenav__label">{{ group.label }}</p>
      <button
        v-for="item in group.items"
        :key="item.key"
        class="ui-sidenav__link"
        :class="{ 'is-active': item.key === modelValue }"
        type="button"
        :aria-current="item.key === modelValue ? 'page' : undefined"
        @click="emit('update:modelValue', item.key)"
      >
        {{ item.label }}
      </button>
    </div>
  </nav>
</template>

<style scoped>
.ui-sidenav {
  display: grid;
  gap: var(--space-3);
}

.ui-sidenav__label {
  margin: 0 0 6px;
  color: var(--muted);
  font: 10px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.ui-sidenav__link {
  display: block;
  width: 100%;
  padding: 8px 10px;
  border: 0;
  border-radius: var(--radius);
  background: transparent;
  color: var(--muted);
  text-align: left;
  font-size: 13px;
  cursor: pointer;
  transition: background var(--motion-02) var(--ease), color var(--motion-02) var(--ease);
}

.ui-sidenav__link:hover {
  background: var(--fg-soft);
  color: var(--fg);
}

.ui-sidenav__link.is-active {
  background: var(--fg-soft);
  color: var(--fg);
  font-weight: 650;
  box-shadow: inset 2px 0 var(--fg);
}
</style>
