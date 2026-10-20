<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary' | 'ghost'
  size?: 'md' | 'sm'
  type?: 'button' | 'submit' | 'reset'
  disabled?: boolean
  loading?: boolean
  block?: boolean
  href?: string
  target?: string
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'secondary',
  size: 'md',
  type: 'button',
  disabled: false,
  loading: false,
  block: false,
  href: undefined,
  target: undefined,
})

const isDisabled = computed(() => props.disabled || props.loading)
const isLink = computed(() => !!props.href && !isDisabled.value)
const rel = computed(() => (props.target === '_blank' ? 'noopener noreferrer' : undefined))
</script>

<template>
  <component
    :is="isLink ? 'a' : 'button'"
    class="ui-btn"
    :class="[`ui-btn--${variant}`, `ui-btn--${size}`, { 'is-block': block, 'is-loading': loading }]"
    :type="isLink ? undefined : type"
    :href="isLink ? href : undefined"
    :target="isLink ? target : undefined"
    :rel="isLink ? rel : undefined"
    :disabled="isLink ? undefined : isDisabled"
    :aria-busy="loading || undefined"
  >
    <span v-if="loading" class="ui-btn__spinner" aria-hidden="true" />
    <span class="ui-btn__label"><slot /></span>
  </component>
</template>

<style scoped>
.ui-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  border-radius: var(--radius);
  font-weight: 650;
  letter-spacing: -0.01em;
  text-decoration: none;
  white-space: nowrap;
  cursor: pointer;
  transition: background var(--motion-02) var(--ease), border-color var(--motion-02) var(--ease), color var(--motion-02) var(--ease), transform var(--motion-02) var(--ease);
}

.ui-btn:active:not(:disabled) {
  transform: translateY(1px);
}

.ui-btn:disabled,
.ui-btn.is-loading {
  opacity: 0.45;
  cursor: not-allowed;
}

.ui-btn--md {
  min-height: 40px;
  padding: 9px 16px;
  font-size: 13px;
}

.ui-btn--sm {
  min-height: 32px;
  padding: 6px 11px;
  font-size: 12px;
}

.is-block {
  width: 100%;
}

/* variant: primary — единственный сильный сигнал */
.ui-btn--primary {
  border: 1px solid var(--accent-strong);
  background: var(--accent-strong);
  color: var(--surface);
}

.ui-btn--primary:hover:not(:disabled) {
  background: color-mix(in oklch, var(--accent-strong) 86%, #000);
  border-color: color-mix(in oklch, var(--accent-strong) 86%, #000);
}

.ui-btn--primary:focus-visible {
  outline-color: var(--accent-strong);
}

/* variant: secondary */
.ui-btn--secondary {
  border: 1px solid var(--muted);
  background: var(--surface);
  color: var(--fg);
}

.ui-btn--secondary:hover:not(:disabled) {
  background: var(--fg-soft);
}

/* variant: ghost */
.ui-btn--ghost {
  border: 1px solid transparent;
  background: transparent;
  color: var(--fg);
}

.ui-btn--ghost:hover:not(:disabled) {
  background: var(--fg-soft);
}

.ui-btn__spinner {
  width: 13px;
  height: 13px;
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  animation: ui-btn-spin 700ms linear infinite;
}

@keyframes ui-btn-spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
