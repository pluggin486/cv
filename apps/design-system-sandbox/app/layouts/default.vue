<script setup lang="ts">
const route = useRoute()
const isOverview = computed(() => route.path === '/')
</script>

<template>
  <div class="app-shell">
    <header class="preview-nav">
      <div class="nav-inner">
        <NuxtLink class="wordmark" to="/">ROLFTECH <span>/ CORE</span></NuxtLink>
        <span class="nav-meta">{{ isOverview ? 'ОБЗОР СИСТЕМЫ' : 'ДИЗАЙН-СИСТЕМА' }}</span>
      </div>
    </header>
    <slot />
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.preview-nav {
  border-bottom: 1px solid var(--border);
  background: var(--bg);
}

.nav-inner {
  --page-gutter: clamp(20px, 4vw, 64px);
  width: min(var(--container), calc(100% - (var(--page-gutter) * 2)));
  margin-inline: auto;
  min-height: 68px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-5);
}

.wordmark {
  color: var(--fg);
  font-weight: 650;
  letter-spacing: -0.02em;
  text-decoration: none;
}

.wordmark span {
  color: var(--muted);
  font-weight: 500;
}

.wordmark:hover span {
  color: var(--fg);
}

.nav-meta {
  color: var(--muted);
  font: 11px var(--font-mono);
  letter-spacing: 0.06em;
}
</style>
