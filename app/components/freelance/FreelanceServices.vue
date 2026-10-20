<script setup lang="ts">
import type { FreelanceService } from '~/utils/freelance'

defineProps<{ items: FreelanceService[] }>()
</script>

<template>
  <section class="freelance-section" aria-labelledby="freelance-services-title">
    <div class="freelance-section__heading">
      <p class="freelance-eyebrow mono">02 / ЧЕМ ПОМОГУ</p>
      <h2 id="freelance-services-title">Задачи, которые беру</h2>
    </div>
    <div class="freelance-services-grid">
      <article v-for="(item, index) in items" :key="item.title" class="freelance-service-card">
        <p class="freelance-service-card__index mono">0{{ index + 1 }}</p>
        <div class="freelance-service-card__body">
          <h3>{{ item.title }}</h3>
          <p class="freelance-service-card__stack mono">{{ item.stack }}</p>
          <p class="freelance-service-card__description">{{ item.description }}</p>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.freelance-section {
  display: grid;
  gap: var(--space-4);
}

.freelance-section__heading {
  display: grid;
  gap: 8px;
}

.freelance-eyebrow {
  color: var(--accent-strong);
  font-size: 10px;
  letter-spacing: 0.1em;
}

.freelance-section h2 {
  font-size: clamp(24px, 4vw, 34px);
  letter-spacing: -0.035em;
}

.freelance-services-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--space-2);
}

.freelance-service-card {
  display: grid;
  grid-template-columns: 36px minmax(0, 1fr);
  gap: var(--space-2);
  min-height: 190px;
  padding: var(--space-4);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--surface);
}

.freelance-service-card__index {
  color: var(--accent-strong);
  font-size: 11px;
}

.freelance-service-card__body {
  display: grid;
  align-content: start;
  gap: 10px;
}

.freelance-service-card h3 {
  font-size: 17px;
  letter-spacing: -0.02em;
}

.freelance-service-card__stack {
  color: var(--muted);
  font-size: 11px;
}

.freelance-service-card__description {
  max-width: 48ch;
  color: var(--muted);
  font-size: 13px;
  line-height: 1.55;
}

@media (max-width: 680px) {
  .freelance-services-grid {
    grid-template-columns: 1fr;
  }

  .freelance-service-card {
    min-height: unset;
  }
}
</style>
