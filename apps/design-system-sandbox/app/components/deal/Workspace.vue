<script setup lang="ts">
import type { SideNavGroup } from '@ss/core-ui'

interface Task {
  name: string
  due: string
  status: 'done' | 'active' | 'planned'
}

const statusMeta: Record<Task['status'], { variant: 'pill' | 'tag' | 'dark'; label: string }> = {
  active: { variant: 'pill', label: 'В работе' },
  done: { variant: 'dark', label: 'Готово' },
  planned: { variant: 'tag', label: 'По плану' },
}

const deal = {
  id: 'RT-28419',
  client: 'Алексей Морозов',
  stage: 'Подбор автомобиля',
  car: 'EXEED VX · 2025',
  budget: '3 240 000 ₽',
  owner: 'Мария Котова',
}

const tasks: Task[] = [
  { name: 'Оценить автомобиль', due: '18 окт', status: 'done' },
  { name: 'Согласовать кредит', due: '19 окт', status: 'active' },
  { name: 'Подготовить договор', due: '20 окт', status: 'planned' },
]

const groups: SideNavGroup[] = [
  {
    label: 'Продажи',
    items: [
      { key: 'deals', label: 'Сделки' },
      { key: 'clients', label: 'Клиенты' },
      { key: 'cars', label: 'Автомобили' },
    ],
  },
  {
    label: 'Операции',
    items: [
      { key: 'docs', label: 'Документы' },
      { key: 'tasks', label: 'Задачи' },
    ],
  },
]

const section = ref('deals')
const filter = ref('all')
const isSaving = ref(false)

const filterTabs = [
  { key: 'all', label: 'Все' },
  { key: 'active', label: 'Активные' },
  { key: 'done', label: 'Готово' },
]

const columns = [
  { key: 'name', label: 'Задача' },
  { key: 'due', label: 'Срок', mono: true },
  { key: 'status', label: 'Статус' },
]

const filteredTasks = computed(() => {
  if (filter.value === 'active') return tasks.filter(task => task.status !== 'done')
  if (filter.value === 'done') return tasks.filter(task => task.status === 'done')
  return tasks
})

const statusFor = (status: Task['status']) => statusMeta[status]!

const currentSectionMeta = computed(() => sectionMeta[section.value] ?? null)

const sectionMeta: Record<string, { title: string; description: string }> = {
  clients: { title: 'Клиентов нет', description: 'В демо-наборе данных заполнен только раздел «Сделки». Реальные клиенты появятся после подключения CRM.' },
  cars: { title: 'Автомобилей нет', description: 'Сток подгружается из inventory-сервиса. Сейчас показывается пустое состояние раздела.' },
  docs: { title: 'Документов нет', description: 'Документы формируются из шаблонов после согласования кредита.' },
  tasks: { title: 'Очередь пуста', description: 'Задачи создаёт ответственный менеджер внутри открытой сделки.' },
}

const save = () => {
  isSaving.value = true
  setTimeout(() => {
    isSaving.value = false
  }, 1200)
}
</script>

<template>
  <div class="deal-shell">
    <div class="deal-shell__bar">
      <strong>ROLF / Сделки</strong>
      <UiStatus variant="tag" label="Демо-данные" />
    </div>
    <div class="deal-shell__workspace">
      <aside class="deal-shell__side">
        <UiSideNav v-model="section" :groups="groups" />
      </aside>
      <section class="deal-shell__main">
        <template v-if="section === 'deals'">
          <div class="deal-head">
            <div class="min-width-0">
              <span class="deal-head__meta mono">СДЕЛКА · {{ deal.id }}</span>
              <strong class="deal-head__name">{{ deal.client }}</strong>
            </div>
            <UiStatus variant="pill" :label="deal.stage" />
          </div>

          <div class="deal-summary">
            <div class="deal-summary__item">
              <span>Автомобиль</span>
              <strong>{{ deal.car }}</strong>
            </div>
            <div class="deal-summary__item">
              <span>Бюджет</span>
              <strong class="mono">{{ deal.budget }}</strong>
            </div>
            <div class="deal-summary__item">
              <span>Ответственный</span>
              <strong>{{ deal.owner }}</strong>
            </div>
          </div>

          <div class="deal-tasks">
            <div class="deal-tasks__head">
              <h3>Следующие задачи</h3>
              <UiButton variant="primary" size="sm" :loading="isSaving" @click="save">
                Сохранить
              </UiButton>
            </div>
            <UiTabs v-model="filter" :tabs="filterTabs" />
            <UiDataTable
              v-if="filteredTasks.length"
              :columns="columns"
              :rows="filteredTasks"
              caption="Очередь задач сделки"
            >
              <template #cell-name="{ row }">
                <span class="deal-task-name">{{ row.name }}</span>
              </template>
              <template #cell-status="{ row }">
                <UiStatus :variant="statusFor(row.status as Task['status']).variant" :label="statusFor(row.status as Task['status']).label" />
              </template>
            </UiDataTable>
            <DealEmptyState
              v-else
              title="Задач нет"
              description="Выберите фильтр «Все», чтобы увидеть полную очередь по сделке."
              action-label="Сбросить фильтр"
              @action="filter = 'all'"
            />
          </div>
        </template>

        <DealEmptyState
          v-else-if="currentSectionMeta"
          :title="currentSectionMeta.title"
          :description="currentSectionMeta.description"
          action-label="Вернуться к сделкам"
          @action="section = 'deals'"
        />
      </section>
    </div>
  </div>
</template>

<style scoped>
.deal-shell {
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  background: var(--surface);
  overflow: hidden;
}

.deal-shell__bar {
  min-height: 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-2);
  padding: 8px var(--space-4);
  border-bottom: 1px solid var(--border);
  font-size: 13px;
}

.deal-shell__workspace {
  display: grid;
  grid-template-columns: 200px minmax(0, 1fr);
}

.deal-shell__side {
  padding: var(--space-3);
  border-right: 1px solid var(--border);
  background: color-mix(in oklch, var(--bg) 72%, var(--surface));
}

.deal-shell__main {
  min-width: 0;
  padding: var(--space-4);
}

.min-width-0 {
  min-width: 0;
}

.deal-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
}

.deal-head__meta {
  display: block;
  color: var(--muted);
  font-size: 11px;
  letter-spacing: 0.04em;
}

.deal-head__name {
  display: block;
  margin-top: 4px;
  font-size: 20px;
  letter-spacing: -0.02em;
}

.deal-summary {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--space-3);
  margin-bottom: var(--space-4);
}

.deal-summary__item {
  border-top: 1px solid var(--fg);
  padding-top: var(--space-2);
}

.deal-summary__item span {
  display: block;
  color: var(--muted);
  font-size: 11px;
}

.deal-summary__item strong {
  display: block;
  margin-top: 4px;
  font-size: 14px;
  letter-spacing: -0.01em;
}

.deal-tasks__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  margin-bottom: var(--space-2);
}

.deal-tasks__head h3 {
  font-size: 15px;
  letter-spacing: -0.01em;
}

.deal-tasks :deep(.ui-tabs) {
  margin-bottom: var(--space-2);
}

.deal-task-name {
  font-weight: 500;
}

@media (max-width: 820px) {
  .deal-shell__workspace {
    grid-template-columns: 1fr;
  }

  .deal-shell__side {
    border-right: 0;
    border-bottom: 1px solid var(--border);
  }

  .deal-summary {
    grid-template-columns: 1fr;
  }
}
</style>
