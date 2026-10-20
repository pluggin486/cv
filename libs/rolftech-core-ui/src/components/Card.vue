<script setup lang="ts">
interface Props {
  padding?: 'none' | 'md' | 'lg'
  shadow?: 'none' | 'layer' | 'modal'
  radius?: 'md' | 'lg' | 'pill'
}

const props = withDefaults(defineProps<Props>(), {
  padding: 'md',
  shadow: 'none',
  radius: 'lg',
})

const paddingClass = computed(() => (props.padding === 'md' ? 'rt-card--pad-md' : props.padding === 'lg' ? 'rt-card--pad-lg' : ''))
const shadowClass = computed(() => (props.shadow === 'layer' ? 'rt-card--shadow-layer' : props.shadow === 'modal' ? 'rt-card--shadow-modal' : ''))
</script>

<template>
  <div class="rt-card" :class="[`rt-card--radius-${radius}`, paddingClass, shadowClass]">
    <slot />
  </div>
</template>

<style scoped>
.rt-card {
  border: 1px solid var(--border);
  background: var(--surface);
}

.rt-card--radius-md {
  border-radius: var(--radius);
}

.rt-card--radius-lg {
  border-radius: var(--radius-lg);
}

.rt-card--radius-pill {
  border-radius: var(--radius-pill);
}

.rt-card--pad-md {
  padding: var(--space-4);
}

.rt-card--pad-lg {
  padding: var(--space-5);
}

.rt-card--shadow-layer {
  box-shadow: var(--shadow-layer);
}

.rt-card--shadow-modal {
  box-shadow: var(--shadow-modal);
}
</style>
