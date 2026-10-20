<script setup lang="ts">
import { education, experience } from '~/utils/resume'

definePageMeta({ layout: 'workspace' })
useHead({ title: 'Опыт работы — Семён Сергеев' })
</script>

<template>
  <div class="xp">
    <UiEyebrow>ОПЫТ РАБОТЫ / 2023 — 2026</UiEyebrow>
    <h1>4 компании · 15 проектов</h1>

    <UiReveal v-for="(job, jobIndex) in experience" :key="job.company" :delay="Math.min(jobIndex * 60, 180)">
      <article class="xp-item">
        <div class="xp-meta">
          <span class="xp-period mono">{{ job.period }}</span>
          <UiStatus v-if="job.current" variant="pill" label="Сейчас" />
        </div>
        <div class="xp-body">
          <header class="xp-head">
            <div>
              <h2>{{ job.company }}</h2>
              <p class="xp-role">{{ job.role }}</p>
              <p v-if="job.location" class="xp-location">{{ job.location }}</p>
            </div>
          </header>

          <div v-for="project in job.projects" :key="project.name" class="xp-project">
            <h3>{{ project.name }}</h3>
            <p class="xp-stack mono">{{ project.stack }}</p>
            <UiAccordion
              v-if="!job.current"
              :title="`Детали · ${project.bullets.length}`"
            >
              <ul>
                <li v-for="bullet in project.bullets" :key="bullet">{{ bullet }}</li>
              </ul>
            </UiAccordion>
            <ul v-else>
              <li v-for="bullet in project.bullets" :key="bullet">{{ bullet }}</li>
            </ul>
          </div>
        </div>
      </article>
    </UiReveal>

    <section class="xp-education">
      <h2>Образование</h2>
      <div class="edu-grid">
        <span class="mono edu-period">{{ education.period }}</span>
        <div>
          <strong>{{ education.school }}</strong>
          <p class="edu-program">{{ education.program }}</p>
          <p class="edu-note">{{ education.note }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.xp {
  display: grid;
  gap: var(--space-4);
}

h1 {
  font-size: clamp(24px, 4vw, 34px);
  letter-spacing: -0.03em;
  margin-bottom: var(--space-2);
}

.xp-item {
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: var(--space-4);
  padding: var(--space-4) 0;
  border-top: 1px solid var(--border);
}

.xp-meta {
  display: grid;
  gap: var(--space-2);
  align-content: start;
  justify-items: start;
}

.xp-period {
  color: var(--muted);
  font-size: 12px;
}

.xp-head h2 {
  font-size: 18px;
  letter-spacing: -0.02em;
}

.xp-role {
  margin-top: 3px;
  color: var(--muted);
  font-size: 13px;
}

.xp-location {
  margin-top: 2px;
  color: var(--muted);
  font-size: 12px;
}

.xp-project {
  margin-top: var(--space-4);
}

.xp-project h3 {
  font-size: 14px;
  letter-spacing: -0.01em;
}

.xp-stack {
  margin: 4px 0 8px;
  color: var(--muted);
  font-size: 11px;
}

.xp-project ul {
  display: grid;
  gap: 6px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.xp-project li {
  position: relative;
  padding-left: 14px;
  color: var(--fg);
  font-size: 13px;
  line-height: 1.5;
}

.xp-project li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  width: 5px;
  height: 5px;
  border-radius: 1px;
  background: var(--accent);
}

.xp-education {
  padding-top: var(--space-4);
  border-top: 1px solid var(--fg);
}

.xp-education h2 {
  font-size: 15px;
  letter-spacing: -0.01em;
  margin-bottom: var(--space-3);
}

.edu-grid {
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: var(--space-4);
}

.edu-period {
  color: var(--muted);
  font-size: 12px;
}

.edu-program {
  margin-top: 3px;
  color: var(--muted);
  font-size: 13px;
}

.edu-note {
  margin-top: 3px;
  color: var(--muted);
  font-size: 12px;
}

@media (max-width: 640px) {
  .xp-item,
  .edu-grid {
    grid-template-columns: 1fr;
    gap: var(--space-2);
  }
}
</style>
