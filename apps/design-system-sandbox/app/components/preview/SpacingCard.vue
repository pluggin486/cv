<template>
  <div class="card-spacing">
    <p class="eyebrow">8 / 12 / 20 / 32 / 56 / 96</p>
    <div class="scale">
      <div class="row"><span class="key">02</span><span class="bar" style="width: 8px" /><span class="value">8px</span></div>
      <div class="row"><span class="key">03</span><span class="bar" style="width: 12px" /><span class="value">12px</span></div>
      <div class="row"><span class="key">04</span><span class="bar" style="width: 20px" /><span class="value">20px</span></div>
      <div class="row"><span class="key">05</span><span class="bar" style="width: 32px" /><span class="value">32px</span></div>
      <div class="row"><span class="key">06</span><span class="bar" style="width: 56px" /><span class="value">56px</span></div>
      <div class="row"><span class="key">07</span><span class="bar" style="width: 96px" /><span class="value">96px</span></div>
    </div>
    <div class="layout">
      <div class="box">
        <strong>Плотность</strong>
        <p>8–14px внутри control и таблиц.</p>
      </div>
      <div class="box large">
        <strong>Ритм секции</strong>
        <p>64–96px между смысловыми блоками.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-spacing {
  padding: 20px;
}

.eyebrow {
  margin: 0 0 10px;
  color: var(--accent-strong);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.scale {
  display: grid;
  gap: 8px;
}

.row {
  display: grid;
  grid-template-columns: 36px minmax(0, 1fr) 70px;
  gap: 9px;
  align-items: center;
}

.key {
  color: var(--muted);
  font: 10px var(--font-mono);
}

.bar {
  height: 12px;
  background: var(--fg);
  border-radius: 3px;
}

.value {
  color: var(--muted);
  font: 10px var(--font-mono);
  text-align: right;
}

.layout {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 16px;
  margin-top: 18px;
}

.box {
  min-height: 82px;
  padding: 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
}

.box strong {
  display: block;
  font-size: 12px;
}

.box p {
  margin: 4px 0 0;
  color: var(--muted);
  font-size: 11px;
}

.box.large {
  border-radius: var(--radius-lg);
}
</style>
