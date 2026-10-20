<script setup lang="ts">
defineProps<{
  title: string
  description: string
  actionLabel?: string
}>()

const emit = defineEmits<{ action: [] }>()
</script>

<template>
  <div class="deal-empty">
    <p class="deal-empty__title">{{ title }}</p>
    <p class="deal-empty__description">{{ description }}</p>
    <UiButton v-if="actionLabel" variant="ghost" size="sm" @click="emit('action')">
      {{ actionLabel }}
    </UiButton>
  </div>
</template>

<style scoped>
.deal-empty {
  display: grid;
  justify-items: start;
  gap: var(--space-2);
  padding: var(--space-6) var(--space-4);
  border-top: 1px solid var(--border);
}

.deal-empty__title {
  font-size: 15px;
  font-weight: 650;
  letter-spacing: -0.01em;
}

.deal-empty__description {
  max-width: 44ch;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.5;
}
</style>
