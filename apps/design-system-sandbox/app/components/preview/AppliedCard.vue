<script setup lang="ts">
const sideSections = [
  { key: 'deals', label: 'Сделки' },
  { key: 'clients', label: 'Клиенты' },
  { key: 'cars', label: 'Автомобили' },
]

const opsSections = [
  { key: 'docs', label: 'Документы' },
  { key: 'tasks', label: 'Задачи' },
]
</script>

<template>
  <div class="card-applied">
    <p class="eyebrow">ONE-WINDOW WORKSPACE</p>
    <div class="shell">
      <div class="bar">
        <strong>ROLF / Сделки</strong>
        <span class="tag">Демо-данные</span>
      </div>
      <div class="workspace">
        <aside class="side">
          <p class="side-label">Продажи</p>
          <button v-for="item in sideSections" :key="item.key" class="side-link" :class="{ active: item.key === 'deals' }" type="button">
            {{ item.label }}
          </button>
          <p class="side-label side-label--gap">Операции</p>
          <button v-for="item in opsSections" :key="item.key" class="side-link" type="button">
            {{ item.label }}
          </button>
        </aside>
        <section class="main">
          <div class="deal-head">
            <div>
              <span class="meta">СДЕЛКА · RT-28419</span>
              <strong>Алексей Морозов</strong>
            </div>
            <span class="pill">Подбор автомобиля</span>
          </div>
          <div class="summary">
            <div class="summary-item"><span>Автомобиль</span><strong>EXEED VX · 2025</strong></div>
            <div class="summary-item"><span>Бюджет</span><strong>3 240 000 ₽</strong></div>
            <div class="summary-item"><span>Ответственный</span><strong>Мария Котова</strong></div>
          </div>
          <table class="table" aria-label="Следующие задачи">
            <thead>
              <tr><th>Задача</th><th>Срок</th><th>Статус</th></tr>
            </thead>
            <tbody>
              <tr><td>Оценить автомобиль</td><td>18 окт</td><td class="status">Готово</td></tr>
              <tr><td>Согласовать кредит</td><td>19 окт</td><td class="status">В работе</td></tr>
              <tr><td>Подготовить договор</td><td>20 окт</td><td>По плану</td></tr>
            </tbody>
          </table>
        </section>
      </div>
    </div>
    <p class="note">Applied UI связывает статус, контекст сделки и следующий шаг в одной рабочей поверхности.</p>
  </div>
</template>

<style scoped>
.card-applied {
  padding: 20px;
}

.eyebrow {
  margin: 0 0 12px;
  color: var(--accent-strong);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.shell {
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--surface);
  overflow: hidden;
}

.bar {
  min-height: 38px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding: 7px 10px;
  border-bottom: 1px solid var(--border);
  font-size: 11px;
}

.tag {
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 3px 6px;
  color: var(--muted);
  font: 9px var(--font-mono);
}

.workspace {
  display: grid;
  grid-template-columns: 90px minmax(0, 1fr);
}

.side {
  padding: 9px;
  border-right: 1px solid var(--border);
  background: color-mix(in oklch, var(--bg) 72%, var(--surface));
}

.side-label {
  margin: 0 0 6px;
  color: var(--muted);
  font: 8px var(--font-mono);
  text-transform: uppercase;
}

.side-label--gap {
  margin-top: 12px;
}

.side-link {
  display: block;
  width: 100%;
  padding: 7px 6px;
  border: 0;
  border-radius: 5px;
  background: transparent;
  color: var(--muted);
  text-align: left;
  font-size: 10px;
  cursor: pointer;
}

.side-link:hover {
  background: var(--fg-soft);
  color: var(--fg);
}

.side-link.active {
  background: var(--fg-soft);
  color: var(--fg);
  font-weight: 650;
  box-shadow: inset 2px 0 var(--fg);
}

.main {
  min-width: 0;
  padding: 12px;
}

.deal-head {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 12px;
}

.meta {
  color: var(--muted);
  font: 8px var(--font-mono);
  letter-spacing: 0.04em;
}

.deal-head strong {
  display: block;
  margin-top: 3px;
  font-size: 13px;
}

.pill {
  padding: 4px 6px;
  background: var(--accent-soft);
  border-radius: 999px;
  color: var(--accent-strong);
  font: 8px var(--font-mono);
  align-self: start;
}

.summary {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 7px;
  margin-bottom: 12px;
}

.summary-item {
  border-top: 1px solid var(--fg);
  padding-top: 5px;
}

.summary-item span {
  display: block;
  color: var(--muted);
  font-size: 8px;
}

.summary-item strong {
  display: block;
  margin-top: 2px;
  font-size: 9px;
}

.table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8px;
}

.table th,
.table td {
  padding: 6px 4px;
  border-bottom: 1px solid var(--border);
  text-align: left;
}

.table th {
  color: var(--muted);
  font: 8px var(--font-mono);
  text-transform: uppercase;
}

.table .status {
  color: var(--accent-strong);
  font-family: var(--font-mono);
}

.note {
  margin: 12px 0 0;
  color: var(--muted);
  font-size: 11px;
}
</style>
