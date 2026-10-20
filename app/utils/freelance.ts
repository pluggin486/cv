export interface FreelanceProof {
  value: string
  label: string
  detail: string
}

export interface FreelanceService {
  title: string
  stack: string
  description: string
}

export const freelanceProfile = {
  name: 'Семён Сергеев',
  role: 'Frontend-разработчик',
  stack: 'Vue 2 / Vue 3 · Nuxt 3 · TypeScript',
  availability: 'Занятость и сроки — по договорённости',
  introduction: 'Разрабатываю интерфейсы и frontend-функциональность для веб-продуктов. Помогаю развивать существующие Vue-приложения, собирать интерфейсы на Nuxt и TypeScript, улучшать производительность списков и тестовый процесс.',
}

export const freelanceProof: FreelanceProof[] = [
  {
    value: '3+ года',
    label: 'коммерческой frontend-разработки',
    detail: 'Vue 2 / Vue 3, Nuxt, TypeScript',
  },
  {
    value: '10 000+',
    label: 'строк в VirtualScroll',
    detail: 'без сторонней библиотеки виртуализации',
  },
  {
    value: '50+',
    label: 'компонентов UI Kit',
    detail: 'для корпоративной дизайн-системы',
  },
  {
    value: '−70%',
    label: 'времени тестового этапа CI',
    detail: 'после перехода с Jest на Vitest',
  },
]

export const freelanceServices: FreelanceService[] = [
  {
    title: 'Разработка интерфейса или функции',
    stack: 'Vue 2 / Vue 3 · Nuxt · TypeScript',
    description: 'Новая страница, форма, таблица, каталог или интеграция с REST API в существующем веб-приложении.',
  },
  {
    title: 'Миграция Vue 2 → Vue 3',
    stack: 'Composition API · Pinia · TypeScript',
    description: 'План миграции и перенос выбранного модуля с проверкой совместимости, типов и поведения интерфейса.',
  },
  {
    title: 'UI Kit и большие списки',
    stack: 'Vue · TypeScript · UI Kit · VirtualScroll',
    description: 'Переиспользуемые компоненты интерфейса, таблицы и виртуализация списков. Опыт — 50+ компонентов и списки свыше 10 000 строк.',
  },
  {
    title: 'Тесты и клиентский API',
    stack: 'Vitest · Playwright · OpenAPI',
    description: 'Unit- и e2e-проверки, тесты API-сценариев и настройка генерации клиентских сервисов по OpenAPI.',
  },
]
