<script setup lang="ts">
defineProps<{
  name: string
  role: string
  stack: string
  availability: string
  introduction: string
}>()
</script>

<template>
  <section class="freelance-hero" aria-labelledby="freelance-title">
    <p class="freelance-eyebrow mono">FRONTEND · FREELANCE</p>
    <div class="freelance-hero__body">
      <div>
        <p class="freelance-hero__role">{{ role }}</p>
        <h1 id="freelance-title">{{ name }}</h1>
        <p class="freelance-hero__stack mono">{{ stack }}</p>
      </div>
      <p class="freelance-availability">{{ availability }}</p>
    </div>
    <p class="freelance-hero__intro">{{ introduction }}</p>
  </section>
</template>

<style scoped>
.freelance-hero {
  display: grid;
  gap: var(--space-4);
}

.freelance-eyebrow {
  color: var(--accent-strong);
  font-size: 11px;
  letter-spacing: 0.1em;
}

.freelance-hero__body {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: var(--space-4);
}

.freelance-hero__role {
  margin-bottom: 6px;
  color: var(--muted);
  font-size: 14px;
}

.freelance-hero h1 {
  font-size: clamp(40px, 8vw, 76px);
  line-height: 0.98;
  letter-spacing: -0.055em;
}

.freelance-hero__stack {
  margin-top: var(--space-3);
  color: var(--muted);
  font-size: 13px;
}

.freelance-availability {
  max-width: 250px;
  padding: 10px 13px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  color: var(--muted);
  font-size: 12px;
}

.freelance-hero__intro {
  max-width: 65ch;
  color: var(--muted);
  font-size: clamp(16px, 2vw, 19px);
  line-height: 1.6;
}

@media (max-width: 620px) {
  .freelance-hero__body {
    align-items: flex-start;
    flex-direction: column;
  }

  .freelance-availability {
    max-width: none;
  }
}
</style>
