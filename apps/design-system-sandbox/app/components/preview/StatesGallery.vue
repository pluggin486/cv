<script setup lang="ts">
const client = ref('Алексей Морозов')
const budget = ref('3 240 000')
const owner = ref('')
const loading = ref(false)

const runLoading = () => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
  }, 1400)
}

const galleryTabs = [
  { key: 'queue', label: 'Очередь' },
  { key: 'empty', label: 'Пустое состояние' },
  { key: 'loading', label: 'Скелетон' },
]
const galleryTab = ref('queue')

const columns = [
  { key: 'name', label: 'Задача' },
  { key: 'due', label: 'Срок', mono: true },
  { key: 'status', label: 'Статус' },
]

const rows = [
  { name: 'Оценить автомобиль', due: '18 окт', status: 'Готово' },
  { name: 'Согласовать кредит', due: '19 окт', status: 'В работе' },
]
</script>

<template>
  <section class="gallery" aria-label="Полный набор состояний UI-kit">
    <UiEyebrow>UI-KIT / ALL STATES</UiEyebrow>

    <div class="group">
      <span class="label">Actions / default · disabled · loading</span>
      <div class="row">
        <UiButton variant="primary">Создать сделку</UiButton>
        <UiButton variant="secondary">Сохранить</UiButton>
        <UiButton variant="ghost">Открыть →</UiButton>
      </div>
      <div class="row">
        <UiButton variant="primary" disabled>Создать сделку</UiButton>
        <UiButton variant="secondary" disabled>Сохранить</UiButton>
        <UiButton variant="primary" size="sm">Small</UiButton>
        <UiButton variant="secondary" size="sm">Small</UiButton>
      </div>
      <div class="row">
        <UiButton variant="primary" :loading="loading" @click="runLoading">
          {{ loading ? 'Сохраняем…' : 'Сохранить с индикатором' }}
        </UiButton>
      </div>
    </div>

    <div class="group">
      <span class="label">Statuses / pill · tag · dark · plain</span>
      <div class="row">
        <UiStatus variant="pill" label="В работе" />
        <UiStatus variant="tag" label="По плану" />
        <UiStatus variant="dark" label="Готово" />
        <span class="mono plain-demo">RT-28419 · plain</span>
      </div>
    </div>

    <div class="group group--fields">
      <span class="label">Fields / default · hint · error · disabled</span>
      <UiInput v-model="client" label="Клиент" hint="Имя, как в договоре." />
      <UiInput v-model="budget" label="Бюджет" hint="Формат — рубли, табличные цифры." />
      <UiInput v-model="owner" label="Ответственный" error="Укажите ответственного менеджера." />
      <UiInput model-value="RT-28419" label="ID сделки" disabled />
    </div>

    <div class="group">
      <span class="label">Tabs + DataTable / данные и пустое состояние</span>
      <UiTabs v-model="galleryTab" :tabs="galleryTabs" />
      <UiDataTable
        v-if="galleryTab === 'queue'"
        :columns="columns"
        :rows="rows"
        caption="Следующие задачи"
      >
        <template #cell-status="{ value }">
          <UiStatus :variant="(value as string) === 'Готово' ? 'dark' : 'pill'" :label="value as string" />
        </template>
      </UiDataTable>
      <UiDataTable
        v-else-if="galleryTab === 'empty'"
        :columns="columns"
        :rows="[]"
        caption="Следующие задачи"
        empty-label="Задач нет — очередь пуста"
      />
      <UiDataTable
        v-else
        :columns="columns"
        :rows="[]"
        caption="Следующие задачи"
        loading
      />
    </div>

    <div class="group">
      <span class="label">Accordion / прогрессивное раскрытие</span>
      <UiAccordion title="Детали · 3" default-open>
        <ul class="demo-list">
          <li>Оценить автомобиль — 18 окт</li>
          <li>Согласовать кредит — 19 окт</li>
          <li>Подготовить договор — 20 окт</li>
        </ul>
      </UiAccordion>
      <UiAccordion title="Скрытые детали · 2">
        <ul class="demo-list">
          <li>Состояние по умолчанию — закрыто</li>
          <li>Раскрывается за 240мс standard-ease</li>
        </ul>
      </UiAccordion>
    </div>
  </section>
</template>

<style scoped>
.gallery {
  margin-top: var(--space-5);
  display: grid;
  gap: var(--space-4);
}

.label {
  display: block;
  margin-bottom: 10px;
  color: var(--muted);
  font: 10px var(--font-mono);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.group {
  padding-top: var(--space-4);
  border-top: 1px solid var(--border);
  display: grid;
  gap: var(--space-3);
}

.row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-2);
}

.group--fields {
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--space-4);
}

.plain-demo {
  color: var(--accent-strong);
  font-size: 12px;
}

.demo-list {
  display: grid;
  gap: 6px;
  margin: 0;
  padding: 0;
  list-style: none;
  color: var(--muted);
  font-size: 13px;
}
</style>
