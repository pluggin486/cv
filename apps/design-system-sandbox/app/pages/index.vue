<script setup lang="ts">
import { markRaw } from 'vue'
import PreviewColorCard from '~/components/preview/ColorCard.vue'
import PreviewTypographyCard from '~/components/preview/TypographyCard.vue'
import PreviewSpacingCard from '~/components/preview/SpacingCard.vue'
import PreviewRadiusCard from '~/components/preview/RadiusCard.vue'
import PreviewComponentsCard from '~/components/preview/ComponentsCard.vue'
import PreviewAssetsCard from '~/components/preview/AssetsCard.vue'
import PreviewAppliedCard from '~/components/preview/AppliedCard.vue'

useHead({ title: 'SS Core — обзор системы' })

const reviewItems = [
  {
    index: '01',
    title: 'Цвет',
    heading: 'Цветовые токены',
    note: 'Токены и состояния',
    copy: 'Токены, состояния и границы контраста.',
    href: '/colors',
    card: markRaw(PreviewColorCard),
  },
  {
    index: '02',
    title: 'Типографика',
    heading: 'Типографика',
    note: 'Ритм текста и чисел',
    copy: 'Display, body, mono и табличные цифры.',
    href: '/typography',
    card: markRaw(PreviewTypographyCard),
  },
  {
    index: '03',
    title: 'Ритм',
    heading: 'Spacing и density',
    note: 'Spacing и density',
    copy: 'Шкала отступов и рабочая плотность.',
    href: '/spacing',
    card: markRaw(PreviewSpacingCard),
  },
  {
    index: '04',
    title: 'Слои',
    heading: 'Радиусы и слои',
    note: 'Радиусы и тени',
    copy: 'Радиусы, границы и редкие тени для отдельных слоёв.',
    href: '/radius-shadows',
    card: markRaw(PreviewRadiusCard),
  },
  {
    index: '05',
    title: 'Компоненты',
    heading: 'Компонентный язык',
    note: 'Actions и states',
    copy: 'Кнопки, поля, tabs и статусы в одном словаре.',
    href: '/components',
    card: markRaw(PreviewComponentsCard),
  },
  {
    index: '06',
    title: 'Assets',
    heading: 'Brand assets',
    note: 'Source evidence',
    copy: 'Сохранённый source preview и границы evidence.',
    href: '/assets',
    card: markRaw(PreviewAssetsCard),
  },
  {
    index: '07',
    title: 'Applied UI',
    heading: 'Applied UI',
    note: 'Сделка и следующий шаг',
    copy: 'Сделка, маршрут и очередь задач в одном окне.',
    href: '/applied',
    card: markRaw(PreviewAppliedCard),
  },
]

const selectedIndex = ref(0)
const itemRefs = ref<HTMLButtonElement[]>([])

const activeItem = computed(() => reviewItems[selectedIndex.value]!)

const select = (index: number) => {
  selectedIndex.value = index
  if (import.meta.client) {
    localStorage.setItem('ss-preview-selection', String(index))
  }
}

const onKeydown = (event: KeyboardEvent, index: number) => {
  const keys = ['ArrowDown', 'ArrowUp', 'Home', 'End']
  if (!keys.includes(event.key)) return
  event.preventDefault()
  const last = reviewItems.length - 1
  let next = index
  if (event.key === 'ArrowDown') next = (index + 1) % reviewItems.length
  if (event.key === 'ArrowUp') next = (index - 1 + reviewItems.length) % reviewItems.length
  if (event.key === 'Home') next = 0
  if (event.key === 'End') next = last
  select(next)
  itemRefs.value[next]?.focus()
}

onMounted(() => {
  const saved = Number(localStorage.getItem('ss-preview-selection'))
  if (Number.isInteger(saved) && saved >= 0 && saved < reviewItems.length) {
    selectedIndex.value = saved
  }
})
</script>

<template>
  <main class="page">
    <section class="intro">
      <div class="intro-copy">
        <UiEyebrow>ДИЗАЙН-СИСТЕМА / РЕВЬЮ</UiEyebrow>
        <h1>Система, которую можно применять</h1>
        <p>Проверьте правила на конкретных поверхностях: от токенов и компонентов до рабочего окна сделки.</p>
      </div>
      <aside class="reading-note">
        <strong>Три контрольные точки</strong>
        <ul>
          <li data-index="01">Нейтральная база и один функциональный сигнал</li>
          <li data-index="02">Моно-слой для статусов, дат и чисел</li>
          <li data-index="03">Рабочее окно сделки без декоративных слоёв</li>
        </ul>
      </aside>
    </section>

    <section class="workbench" aria-label="Фокусные preview-карточки">
      <div class="review-list" role="list">
        <div class="list-heading">ПРЕДМЕТ РЕВЬЮ</div>
        <button
          v-for="(item, index) in reviewItems"
          :key="item.index"
          :ref="(el) => { if (el) itemRefs[index] = el as HTMLButtonElement }"
          class="review-item"
          :class="{ active: index === selectedIndex }"
          type="button"
          role="listitem"
          :aria-pressed="index === selectedIndex"
          @click="select(index)"
          @keydown="onKeydown($event, index)"
        >
          <span class="review-item-index">{{ item.index }}</span>
          <span>
            <strong>{{ item.title }}</strong>
            <small>{{ item.note }}</small>
          </span>
        </button>
      </div>
      <div class="viewport">
        <div class="viewport-head">
          <div>
            <h2>{{ activeItem.heading }}</h2>
            <p>{{ activeItem.copy }}</p>
          </div>
          <span class="viewport-index mono">{{ activeItem.index }}</span>
        </div>
        <div class="viewport-frame">
          <component :is="activeItem.card" />
        </div>
        <div class="viewport-foot">
          <span>Встроенная карточка показывает реальный source-backed паттерн.</span>
          <NuxtLink class="standalone-link" :to="activeItem.href">Открыть отдельно →</NuxtLink>
        </div>
      </div>
    </section>

    <footer class="footer">
      <span>SS Core · UI-kit реализован на Nuxt 4 + Vue 3</span>
      <span class="meta mono">ONE WORKSPACE / ONE SIGNAL</span>
    </footer>
  </main>
</template>

<style scoped>
.page {
  --page-gutter: clamp(20px, 4vw, 64px);
  width: min(var(--container), calc(100% - (var(--page-gutter) * 2)));
  margin-inline: auto;
  padding-block: clamp(48px, 8vw, 96px);
  flex: 1;
}

.intro {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(280px, 0.46fr);
  gap: var(--space-7);
  align-items: end;
  margin-bottom: var(--space-7);
}

.intro-copy {
  display: grid;
  gap: var(--space-4);
}

h1 {
  max-width: 12ch;
  font-size: clamp(42px, 7vw, 78px);
  line-height: 0.98;
  letter-spacing: -0.045em;
}

.intro-copy > p:not(.ui-eyebrow) {
  max-width: 58ch;
  color: var(--muted);
  font-size: 18px;
}

.reading-note {
  border-top: 1px solid var(--fg);
  padding-top: var(--space-3);
}

.reading-note strong {
  display: block;
  margin-bottom: var(--space-3);
  font-size: 14px;
}

.reading-note ul {
  display: grid;
  gap: 9px;
  margin: 0;
  padding: 0;
  list-style: none;
  color: var(--muted);
  font-size: 13px;
}

.reading-note li {
  display: grid;
  grid-template-columns: 34px minmax(0, 1fr);
  gap: 10px;
}

.reading-note li::before {
  content: attr(data-index);
  color: var(--fg);
  font: 11px var(--font-mono);
}

.workbench {
  display: grid;
  grid-template-columns: minmax(220px, 0.42fr) minmax(0, 1.58fr);
  border-top: 1px solid var(--fg);
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}

.review-list {
  min-width: 0;
  border-right: 1px solid var(--border);
}

.list-heading {
  padding: 16px 20px;
  color: var(--muted);
  font: 10px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.review-item {
  display: grid;
  grid-template-columns: 32px minmax(0, 1fr);
  gap: 12px;
  width: 100%;
  min-height: 70px;
  padding: 14px 20px;
  border: 0;
  border-top: 1px solid var(--border);
  background: transparent;
  color: var(--fg);
  text-align: left;
  cursor: pointer;
  transition: background var(--motion-02) var(--ease), color var(--motion-02) var(--ease);
}

.review-item:hover {
  background: var(--fg-soft);
  color: var(--fg);
}

.review-item.active {
  background: var(--fg);
  color: var(--surface);
}

.review-item.active:hover {
  background: color-mix(in oklch, var(--fg) 88%, var(--surface));
  color: var(--surface);
}

.review-item-index {
  color: inherit;
  opacity: 0.68;
  font: 11px var(--font-mono);
}

.review-item strong {
  display: block;
  font-size: 14px;
}

.review-item small {
  display: block;
  margin-top: 4px;
  color: inherit;
  opacity: 0.68;
  font-size: 11px;
  line-height: 1.35;
}

.viewport {
  min-width: 0;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr) auto;
}

.viewport-head {
  display: flex;
  align-items: start;
  justify-content: space-between;
  gap: 20px;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
}

.viewport-head h2 {
  font-size: 22px;
  line-height: 1.15;
  letter-spacing: -0.02em;
}

.viewport-head p {
  max-width: 46ch;
  margin-top: 5px;
  color: var(--muted);
  font-size: 12px;
}

.viewport-index {
  color: var(--muted);
  font-size: 12px;
}

.viewport-frame {
  min-width: 0;
  height: 470px;
  overflow-y: auto;
  background: var(--surface);
}

.viewport-foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 12px 20px;
  border-top: 1px solid var(--border);
}

.viewport-foot span {
  color: var(--muted);
  font-size: 12px;
}

.standalone-link {
  color: var(--fg);
  font-size: 12px;
  font-weight: 650;
  text-decoration: none;
  white-space: nowrap;
}

.standalone-link:hover {
  color: var(--fg);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.standalone-link:focus-visible {
  outline-offset: 4px;
}

.footer {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  margin-top: var(--space-7);
  padding-top: var(--space-4);
  border-top: 1px solid var(--border);
  color: var(--muted);
  font-size: 13px;
}

.footer .meta {
  font-size: 11px;
}

@media (max-width: 820px) {
  .intro,
  .workbench {
    grid-template-columns: 1fr;
  }

  .intro {
    gap: var(--space-5);
  }

  .review-list {
    border-right: 0;
    border-bottom: 1px solid var(--border);
  }

  .list-heading {
    padding-bottom: 10px;
  }

  .review-item {
    display: inline-grid;
    width: 50%;
    vertical-align: top;
    border-top: 1px solid var(--border);
  }

  .viewport-frame {
    height: 420px;
  }
}

@media (max-width: 520px) {
  h1 {
    max-width: 11ch;
  }

  .review-item {
    width: 100%;
  }

  .viewport-head,
  .viewport-foot {
    align-items: flex-start;
    flex-direction: column;
  }

  .viewport-frame {
    height: 380px;
  }

  .footer {
    flex-direction: column;
  }
}
</style>
