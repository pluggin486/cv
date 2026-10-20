<script setup lang="ts">
import { about, experience, identity as who, metrics, stackStrip } from '~/utils/resume'

definePageMeta({ layout: 'workspace' })
useHead({ title: 'Семён Сергеев — Frontend Developer' })

const currentJob = experience[0]!
</script>

<template>
  <div class="overview">
    <div class="hero">
      <UiEyebrow>КАНДИДАТ · FRONTEND DEVELOPER</UiEyebrow>

      <div class="overview-head">
        <div class="min-width-0">
          <h1>{{ who.name }}</h1>
          <p class="overview-stack mono">{{ who.stackLine }}</p>
        </div>
      </div>

      <div class="overview-summary">
        <div class="summary-item">
          <span>Локация</span>
          <strong>{{ who.location }}</strong>
        </div>
        <div class="summary-item">
          <span>Занятость</span>
          <strong>{{ who.employment }}</strong>
        </div>
        <div class="summary-item">
          <span>Сейчас</span>
          <strong>{{ currentJob.company }} · {{ currentJob.projects[0]!.name }}</strong>
        </div>
      </div>
    </div>

    <div class="marquee" aria-hidden="true">
      <div class="marquee__track mono">
        <span v-for="(item, index) in [...stackStrip, ...stackStrip]" :key="index" class="marquee__item">{{ item }}</span>
      </div>
    </div>

    <UiReveal>
      <section class="overview-about">
        <h2>О себе</h2>
        <p>{{ about }}</p>
      </section>
    </UiReveal>

    <section class="overview-metrics">
      <h2>Доказательства</h2>
      <div class="metrics-grid">
        <UiReveal v-for="(metric, index) in metrics" :key="metric.label" :delay="index * 60">
          <div class="metric">
            <strong><UiCountUp :value="metric.num" :prefix="metric.prefix" :suffix="metric.suffix" /></strong>
            <span>{{ metric.label }}</span>
            <small>{{ metric.note }}</small>
          </div>
        </UiReveal>
      </div>
    </section>

    <section class="overview-actions">
      <UiButton variant="primary" :href="who.telegramHref" target="_blank">
        Telegram {{ who.telegram }}
      </UiButton>
      <UiButton variant="secondary" :href="who.emailHref">Написать email</UiButton>
      <UiButton variant="ghost" href="/experience">
        Опыт работы →
      </UiButton>
    </section>
  </div>
</template>

<style scoped>
.overview {
  display: grid;
  gap: var(--space-5);
}

/* hero с editorial grid-линиями (blueprint) */
.hero {
  position: relative;
  display: grid;
  gap: var(--space-4);
  padding: var(--space-2) 0 0;
}

.hero::before {
  content: '';
  position: absolute;
  inset: 0 calc(-1 * clamp(20px, 3vw, 32px)) -8px;
  background-image: linear-gradient(90deg, var(--border) 1px, transparent 1px);
  background-size: 25% 100%;
  pointer-events: none;
}

.hero > * {
  position: relative;
}

.min-width-0 {
  min-width: 0;
}

.overview-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-3);
}

h1 {
  font-size: clamp(30px, 5vw, 46px);
  line-height: 1.02;
  letter-spacing: -0.035em;
}

.overview-stack {
  margin-top: 8px;
  color: var(--muted);
  font-size: 13px;
}

h2 {
  margin-bottom: var(--space-3);
  font-size: 15px;
  letter-spacing: -0.01em;
}

.overview-summary {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--space-3);
}

.summary-item {
  border-top: 1px solid var(--fg);
  padding-top: var(--space-2);
}

.summary-item span {
  display: block;
  color: var(--muted);
  font-size: 11px;
}

.summary-item strong {
  display: block;
  margin-top: 4px;
  font-size: 14px;
  letter-spacing: -0.01em;
}

/* mono-marquee стека */
.marquee {
  overflow: hidden;
  border-block: 1px solid var(--border);
  padding: 9px 0;
  -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
  mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent);
}

.marquee__track {
  display: flex;
  width: max-content;
  gap: var(--space-4);
  animation: marquee-scroll 36s linear infinite;
}

.marquee:hover .marquee__track {
  animation-play-state: paused;
}

.marquee__item {
  color: var(--muted);
  font-size: 12px;
  white-space: nowrap;
}

.marquee__item::after {
  content: '·';
  margin-left: var(--space-4);
  color: var(--border);
}

@keyframes marquee-scroll {
  to {
    transform: translateX(-50%);
  }
}

.overview-about p {
  max-width: 64ch;
  color: var(--muted);
  font-size: 15px;
  line-height: 1.55;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: var(--space-3);
}

.metric {
  border-top: 1px solid var(--border);
  padding-top: var(--space-2);
  display: grid;
  gap: 3px;
}

.metric strong {
  font-size: 26px;
  letter-spacing: -0.03em;
}

.metric span {
  font-size: 13px;
}

.metric small {
  color: var(--muted);
  font-size: 12px;
  line-height: 1.4;
}

.overview-actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  padding-top: var(--space-2);
  border-top: 1px solid var(--border);
}

@media (prefers-reduced-motion: reduce) {
  .marquee__track {
    animation: none;
  }

  .marquee {
    overflow-x: auto;
  }
}

@media (max-width: 640px) {
  .overview-summary {
    grid-template-columns: 1fr;
  }

  .overview-head {
    flex-direction: column;
    align-items: flex-start;
  }

  .hero::before {
    display: none;
  }
}
</style>
