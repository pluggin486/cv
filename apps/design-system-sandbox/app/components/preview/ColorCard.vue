<template>
  <div class="card-colors">
    <p class="eyebrow">CORE TOKENS</p>
    <div class="swatches">
      <div class="swatch">
        <div class="sample" style="background: var(--bg)" />
        <div class="info"><strong>Фон</strong><code>--bg</code></div>
      </div>
      <div class="swatch">
        <div class="sample" style="background: var(--surface)" />
        <div class="info"><strong>Поверхность</strong><code>--surface</code></div>
      </div>
      <div class="swatch">
        <div class="sample" style="background: var(--fg)" />
        <div class="info"><strong>Текст</strong><code>--fg</code></div>
      </div>
      <div class="swatch">
        <div class="sample" style="background: var(--muted)" />
        <div class="info"><strong>Вторичный</strong><code>--muted</code></div>
      </div>
      <div class="swatch">
        <div class="sample" style="background: var(--border)" />
        <div class="info"><strong>Граница</strong><code>--border</code></div>
      </div>
      <div class="swatch">
        <div class="sample" style="background: var(--accent)" />
        <div class="info"><strong>Сигнал</strong><code>--accent</code></div>
      </div>
    </div>
    <div class="states" aria-label="Семантические состояния">
      <span class="chip chip-accent">В работе</span>
      <span class="chip chip-dark">Активно</span>
      <span class="chip chip-border">По плану</span>
    </div>
  </div>
</template>

<style scoped>
.card-colors {
  padding: 20px;
}

.eyebrow {
  margin: 0 0 14px;
  color: var(--accent-strong);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.swatches {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--surface);
}

.swatch {
  min-width: 0;
  border-right: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}

.swatch:nth-child(3n) {
  border-right: 0;
}

.sample {
  height: 70px;
  border-bottom: 1px solid var(--border);
}

.info {
  padding: 9px;
}

.info strong {
  display: block;
  font-size: 12px;
}

.info code {
  display: block;
  margin-top: 2px;
  color: var(--muted);
  font-size: 9px;
  overflow-wrap: anywhere;
}

.states {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}

.chip {
  min-height: 28px;
  display: inline-flex;
  align-items: center;
  padding: 4px 9px;
  border-radius: 999px;
  font: 11px var(--font-mono);
}

.chip-accent {
  background: var(--accent-soft);
  color: var(--accent-strong);
}

.chip-dark {
  background: var(--fg);
  color: var(--surface);
}

.chip-border {
  border: 1px solid var(--muted);
  color: var(--muted);
}
</style>
