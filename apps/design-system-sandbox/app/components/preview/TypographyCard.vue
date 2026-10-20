<template>
  <div class="card-typography">
    <p class="eyebrow">TYPE SCALE</p>
    <div class="specimen">
      <span class="label">Display / 620</span>
      <div class="display">Один интерфейс для всей сделки</div>
    </div>
    <div class="specimen">
      <span class="label">Body / 16</span>
      <p class="body">Клиент, автомобиль, документы и задачи остаются в одном рабочем контексте.</p>
    </div>
    <div class="specimen">
      <span class="label">Mono / technical</span>
      <div class="mono">RT-28419 · 3 240 000 ₽ · 18 окт</div>
      <div class="small">ID, даты, цены, статусы</div>
    </div>
  </div>
</template>

<style scoped>
.card-typography {
  padding: 20px;
}

.eyebrow {
  margin: 0 0 10px;
  color: var(--accent-strong);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.specimen {
  border-top: 1px solid var(--border);
  padding: 15px 0;
}

.label {
  display: block;
  margin-bottom: 7px;
  color: var(--muted);
  font: 10px var(--font-mono);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.display {
  font-size: clamp(30px, 6vw, 52px);
  line-height: 1;
  letter-spacing: -0.04em;
  font-weight: 650;
}

.body {
  max-width: 48ch;
  font-size: 16px;
  line-height: 1.5;
}

.mono {
  font: 13px/1.5 var(--font-mono);
  font-variant-numeric: tabular-nums;
}

.small {
  color: var(--muted);
  font-size: 12px;
}
</style>
