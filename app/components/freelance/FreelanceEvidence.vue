<script setup lang="ts">
import type { FreelanceProof } from '~/utils/freelance'

defineProps<{ items: FreelanceProof[] }>()
</script>

<template>
  <section class="freelance-section" aria-labelledby="freelance-proof-title">
    <div class="freelance-section__heading">
      <p class="freelance-eyebrow mono">01 / ДОКАЗАТЕЛЬСТВА</p>
      <h2 id="freelance-proof-title">Опыт в цифрах</h2>
    </div>
    <div class="freelance-proof-grid">
      <article v-for="item in items" :key="item.label" class="freelance-proof-card">
        <strong class="freelance-proof-card__value">{{ item.value }}</strong>
        <span class="freelance-proof-card__label">{{ item.label }}</span>
        <small class="freelance-proof-card__detail">{{ item.detail }}</small>
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

.freelance-proof-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1px;
  overflow: hidden;
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--border);
}

.freelance-proof-card {
  min-height: 142px;
  padding: var(--space-4);
  display: grid;
  align-content: start;
  gap: 7px;
  background: var(--surface);
}

.freelance-proof-card__value {
  font-size: clamp(24px, 4vw, 34px);
  letter-spacing: -0.04em;
}

.freelance-proof-card__label {
  font-size: 13px;
  font-weight: 650;
}

.freelance-proof-card__detail {
  color: var(--muted);
  font-size: 12px;
  line-height: 1.45;
}

@media (max-width: 800px) {
  .freelance-proof-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 420px) {
  .freelance-proof-card {
    min-height: 128px;
    padding: var(--space-3);
  }
}
</style>
