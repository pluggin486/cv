<script setup lang="ts">
defineProps<{
  title: string
  copy: string
}>()
</script>

<template>
  <div class="screen-page">
    <h1 class="screen-page__title">{{ title }}</h1>
    <p class="screen-page__copy">{{ copy }}</p>
    <div class="screen-page__frame">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.screen-page {
  width: min(var(--container), calc(100% - 40px));
  margin-inline: auto;
  padding: var(--space-4) 0 var(--space-6);
  flex: 1;
}

.screen-page__title {
  margin: 0 0 8px;
  font-size: 20px;
  letter-spacing: -0.02em;
}

.screen-page__copy {
  margin: 0;
  color: var(--muted);
  font-size: 13px;
}

.screen-page__frame {
  margin-top: var(--space-4);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: var(--surface);
}
</style>
