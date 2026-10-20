<script setup lang="ts">
interface Props {
  variant?: 'pill' | 'tag' | 'dark' | 'plain'
  label: string
}

withDefaults(defineProps<Props>(), {
  variant: 'tag',
})
</script>

<template>
  <span class="ui-status" :class="`ui-status--${variant}`">{{ label }}</span>
</template>

<style scoped>
.ui-status {
  display: inline-flex;
  align-items: center;
  min-height: 26px;
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  font-size: 11px;
  line-height: 1;
  white-space: nowrap;
}

/* В работе — единственный цветной сигнал */
.ui-status--pill {
  background: var(--accent-soft);
  color: var(--accent-strong);
  font-family: var(--font-mono);
}

/* По плану — нейтральный контур */
.ui-status--tag {
  border: 1px solid var(--muted);
  color: var(--muted);
}

/* Готово / активно — инверсия */
.ui-status--dark {
  background: var(--fg);
  color: var(--surface);
  font-family: var(--font-mono);
}

/* Технический текст в таблицах */
.ui-status--plain {
  padding: 0;
  min-height: 0;
  color: var(--accent-strong);
  font-family: var(--font-mono);
  font-size: 12px;
}
</style>
