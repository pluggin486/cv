<script setup lang="ts">
interface Props {
  title: string
  defaultOpen?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  defaultOpen: false,
})

const isOpen = ref(props.defaultOpen)
</script>

<template>
  <details class="ui-accordion" :open="isOpen" @toggle="isOpen = ($event.target as HTMLDetailsElement).open">
    <summary class="ui-accordion__summary">
      <span class="ui-accordion__title">{{ title }}</span>
      <span class="ui-accordion__marker mono" aria-hidden="true">+</span>
    </summary>
    <div class="ui-accordion__content">
      <slot />
    </div>
  </details>
</template>

<style scoped>
.ui-accordion {
  border-top: 1px solid var(--border);
}

.ui-accordion__summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-2);
  min-height: 40px;
  padding: 8px 0;
  cursor: pointer;
  list-style: none;
  user-select: none;
}

.ui-accordion__summary::-webkit-details-marker {
  display: none;
}

.ui-accordion__summary:hover .ui-accordion__title {
  color: var(--fg);
}

.ui-accordion__title {
  color: var(--muted);
  font-size: 12px;
  font-weight: 650;
  letter-spacing: -0.01em;
  transition: color var(--motion-02) var(--ease-standard);
}

.ui-accordion__marker {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  border: 1px solid var(--border);
  border-radius: var(--radius-pill);
  color: var(--muted);
  font-size: 13px;
  transition: transform var(--motion-03) var(--ease-standard), color var(--motion-02) var(--ease-standard), border-color var(--motion-02) var(--ease-standard);
}

.ui-accordion[open] > .ui-accordion__summary .ui-accordion__marker {
  transform: rotate(45deg);
  color: var(--accent-strong);
  border-color: currentColor;
}

.ui-accordion__content {
  padding-bottom: var(--space-3);
  animation: ui-accordion-in var(--motion-04) var(--ease-standard);
}

@keyframes ui-accordion-in {
  from {
    opacity: 0;
    transform: translateY(-4px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
