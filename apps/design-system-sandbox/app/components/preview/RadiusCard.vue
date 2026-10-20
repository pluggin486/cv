<template>
  <div class="card-radius">
    <p class="eyebrow">SURFACE HIERARCHY</p>
    <div class="surface-grid">
      <div class="surface r8"><strong>Control</strong><span>radius / 8px</span></div>
      <div class="surface r12"><strong>Card</strong><span>radius / 12px</span></div>
      <div class="surface pill"><strong>Status</strong><span>radius / 999px</span></div>
      <div class="surface r12 shadow"><strong>Dropdown</strong><span>shadow / layer</span></div>
      <div class="surface r12 modal"><strong>Dialog</strong><span>shadow / modal</span></div>
      <div class="surface r8"><strong>Обычная поверхность</strong><span>border + space, no shadow</span></div>
    </div>
    <p class="note">Тень объясняет только отдельный слой. Обычные карточки остаются плоскими и отделены линией.</p>
  </div>
</template>

<style scoped>
.card-radius {
  padding: 20px;
}

.eyebrow {
  margin: 0 0 14px;
  color: var(--accent-strong);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.surface-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
}

.surface {
  min-height: 76px;
  padding: 13px;
  border: 1px solid var(--border);
  background: var(--surface);
}

.surface strong {
  display: block;
  font-size: 12px;
}

.surface span {
  display: block;
  margin-top: 3px;
  color: var(--muted);
  font: 10px var(--font-mono);
}

.r8 {
  border-radius: var(--radius);
}

.r12 {
  border-radius: var(--radius-lg);
}

.pill {
  border-radius: 999px;
}

.shadow {
  box-shadow: var(--shadow-layer);
}

.modal {
  box-shadow: var(--shadow-modal);
}

.note {
  margin: 15px 0 0;
  padding-top: 12px;
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: 11px;
  line-height: 1.5;
}
</style>
