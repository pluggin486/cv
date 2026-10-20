<template>
  <div class="card-assets">
    <p class="eyebrow">SOURCE EVIDENCE</p>
    <div class="asset-frame">
      <div class="asset-preview" role="img" aria-label="Место сохранённого preview исходного UI-kit ROLFTECH">
        <span class="asset-preview__meta">rolftech-ui-kit-preview.png</span>
        <span class="asset-preview__note">source preview не передан в архив</span>
      </div>
      <div class="asset-copy">
        <strong>rolftech-ui-kit-preview.png</strong>
        <p>Сохранённый source preview: нейтральная поверхность, красный сигнал и рабочая карточка сделки.</p>
      </div>
    </div>
    <p class="note">
      <span class="meta">ASSET BOUNDARY</span><br>
      Отдельных logo, icon, avatar и font files в source evidence нет. Они не подменяются вымышленными файлами.
    </p>
  </div>
</template>

<style scoped>
.card-assets {
  padding: 20px;
}

.eyebrow {
  margin: 0 0 12px;
  color: var(--accent-strong);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.asset-frame {
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--surface);
  overflow: hidden;
}

.asset-preview {
  height: 160px;
  display: grid;
  place-content: center;
  gap: 6px;
  text-align: center;
  background: var(--fg-soft);
  border-bottom: 1px solid var(--border);
}

.asset-preview__meta {
  font: 10px var(--font-mono);
  color: var(--muted);
}

.asset-preview__note {
  font-size: 11px;
  color: var(--muted);
}

.asset-copy {
  padding: 12px;
}

.asset-copy strong {
  display: block;
  font-size: 12px;
}

.asset-copy p {
  margin: 5px 0 0;
  color: var(--muted);
  font-size: 11px;
  line-height: 1.45;
}

.note {
  margin-top: 12px;
  padding-top: 11px;
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: 11px;
  line-height: 1.45;
}

.meta {
  font: 10px var(--font-mono);
  color: var(--muted);
}
</style>
