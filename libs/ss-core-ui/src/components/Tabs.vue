<script setup lang="ts">
interface TabItem {
  key: string
  label: string
}

const props = defineProps<{
  tabs: TabItem[]
  modelValue: string
}>()

const emit = defineEmits<{ 'update:modelValue': [value: string] }>()

const select = (key: string) => emit('update:modelValue', key)

const onKeydown = (event: KeyboardEvent, index: number) => {
  const keys = ['ArrowRight', 'ArrowLeft', 'Home', 'End']
  if (!keys.includes(event.key)) return
  event.preventDefault()
  let nextIndex = index
  if (event.key === 'ArrowRight') nextIndex = (index + 1) % props.tabs.length
  if (event.key === 'ArrowLeft') nextIndex = (index - 1 + props.tabs.length) % props.tabs.length
  if (event.key === 'Home') nextIndex = 0
  if (event.key === 'End') nextIndex = props.tabs.length - 1
  const next = props.tabs[nextIndex]
  if (next) emit('update:modelValue', next.key)
}
</script>

<template>
  <div class="ui-tabs" role="tablist">
    <button
      v-for="(tab, index) in tabs"
      :key="tab.key"
      class="ui-tab"
      :class="{ 'is-active': tab.key === modelValue }"
      type="button"
      role="tab"
      :aria-selected="tab.key === modelValue"
      :tabindex="tab.key === modelValue ? 0 : -1"
      @click="select(tab.key)"
      @keydown="onKeydown($event, index)"
    >
      {{ tab.label }}
    </button>
  </div>
</template>

<style scoped>
.ui-tabs {
  display: flex;
  border-bottom: 1px solid var(--border);
}

.ui-tab {
  position: relative;
  min-height: 38px;
  padding: 8px 14px;
  border: 0;
  background: transparent;
  color: var(--muted);
  font-size: 13px;
  cursor: pointer;
  transition: color var(--motion-02) var(--ease-standard);
}

.ui-tab::after {
  content: '';
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 0;
  height: 2px;
  border-radius: 1px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: left center;
  transition: transform var(--motion-03) var(--ease-standard);
}

.ui-tab:hover {
  color: var(--fg);
}

.ui-tab.is-active {
  color: var(--fg);
}

.ui-tab.is-active::after {
  transform: scaleX(1);
}
</style>
