<script setup lang="ts">
interface Props {
  modelValue?: string
  label?: string
  placeholder?: string
  error?: string
  hint?: string
  disabled?: boolean
  readonly?: boolean
  id?: string
  name?: string
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: '',
  label: '',
  placeholder: '',
  error: '',
  hint: '',
  disabled: false,
  readonly: false,
  id: undefined,
  name: undefined,
})

const emit = defineEmits<{ 'update:modelValue': [value: string] }>()

const inputId = useId()
const fieldId = computed(() => props.id ?? inputId)
</script>

<template>
  <div class="ui-field" :class="{ 'has-error': !!error }">
    <label v-if="label" class="ui-field__label" :for="fieldId">{{ label }}</label>
    <input
      :id="fieldId"
      class="ui-input"
      :class="{ 'is-disabled': disabled }"
      :value="modelValue"
      :placeholder="placeholder"
      :disabled="disabled"
      :readonly="readonly"
      :name="name"
      :aria-invalid="!!error || undefined"
      :aria-describedby="error ? `${fieldId}-error` : hint ? `${fieldId}-hint` : undefined"
      @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    >
    <p v-if="error" :id="`${fieldId}-error`" class="ui-field__message ui-field__message--error" role="alert">
      {{ error }}
    </p>
    <p v-else-if="hint" :id="`${fieldId}-hint`" class="ui-field__message">
      {{ hint }}
    </p>
  </div>
</template>

<style scoped>
.ui-field {
  display: grid;
  gap: 6px;
}

.ui-field__label {
  color: var(--muted);
  font-size: 12px;
}

.ui-input {
  min-height: 40px;
  padding: 8px 12px;
  border: 1px solid var(--muted);
  border-radius: var(--radius);
  background: var(--surface);
  color: var(--fg);
  font: inherit;
  font-size: 13px;
  transition: border-color var(--motion-02) var(--ease), box-shadow var(--motion-02) var(--ease);
}

.ui-input::placeholder {
  color: var(--muted);
}

.ui-input:focus {
  outline: none;
  border-color: var(--fg);
  box-shadow: 0 0 0 1px var(--fg);
}

.ui-input.is-disabled {
  background: var(--fg-soft);
  border-color: var(--border);
  color: var(--muted);
  cursor: not-allowed;
}

.has-error .ui-input {
  border-color: var(--accent-strong);
}

.has-error .ui-input:focus {
  border-color: var(--accent-strong);
  box-shadow: 0 0 0 1px var(--accent-strong);
}

.ui-field__message {
  margin: 0;
  color: var(--muted);
  font-size: 12px;
}

.ui-field__message--error {
  color: var(--accent-strong);
}
</style>
