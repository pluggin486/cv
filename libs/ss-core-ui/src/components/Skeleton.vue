<script setup lang="ts">
interface Props {
  width?: string
  height?: string
}

withDefaults(defineProps<Props>(), {
  width: '100%',
  height: '12px',
})
</script>

<template>
  <span class="ui-skeleton" :style="{ width, height }" aria-hidden="true" />
</template>

<style scoped>
.ui-skeleton {
  display: inline-block;
  border-radius: 4px;
  background: var(--fg-soft);
  animation: ui-skeleton-pulse 1.4s var(--ease-standard) infinite;
}

@keyframes ui-skeleton-pulse {
  0%,
  100% {
    opacity: 1;
  }

  50% {
    opacity: 0.45;
  }
}
</style>
