export interface Metric {
  value: string
  num: number
  prefix?: string
  suffix?: string
  label: string
  note: string
}

export interface ExperienceProject {
  name: string
  stack: string
  bullets: string[]
}

export interface ExperienceItem {
  company: string
  period: string
  role: string
  location: string
  current?: boolean
  projects: ExperienceProject[]
}

export type ProjectCategory = 'ui-kit' | 'nuxt' | 'infra' | 'product'

export interface Project {
  name: string
  company: string
  stack: string
  result: string
  category: ProjectCategory
}

export interface SkillGroup {
  label: string
  items: string[]
}

export const identity = {
  name: 'Семён Сергеев',
  full: 'Сергеев Семён Николаевич',
  role: 'Frontend Developer',
  stackLine: 'Vue 3 / Nuxt / TypeScript',
  location: 'Москва · удалённо или гибрид',
  availability: 'Открыт к предложениям',
  employment: 'Полная занятость',
  phone: '+7 (996) 581-15-09',
  phoneHref: 'tel:+79965811509',
  email: 'futurefind123121@gmail.com',
  emailHref: 'mailto:futurefind123121@gmail.com',
  telegram: '@srgt68lang',
  telegramHref: 'https://t.me/srgt68lang',
}

export const about = 'Frontend-разработчик с 3+ годами коммерческого опыта. Стек: Vue 3, Nuxt, TypeScript. Разработал компоненты UI Kit и виртуализацию списков из 10 000+ строк. Перевёл тесты биллинга с Jest на Vitest: время тестового этапа CI сократилось на 70%. Есть опыт миграции Vue 2 на Vue 3, API-кодогенерации, ревью и декомпозиции.'

export const metrics: Metric[] = [
  { value: '3+ лет', num: 3, suffix: '+ лет', label: 'коммерческого опыта', note: 'Vue 2 / Vue 3 / Nuxt / TypeScript' },
  { value: '−70%', num: 70, prefix: '−', suffix: '%', label: 'время CI-тестов', note: 'Jest → Vitest в биллинге ЖКХ' },
  { value: '10 000+', num: 10000, suffix: '+', label: 'строк в VirtualScroll', note: 'без сторонних библиотек виртуализации' },
  { value: '50+', num: 50, suffix: '+', label: 'компонентов Plex-UI', note: 'корпоративная дизайн-система' },
]

export const experience: ExperienceItem[] = [
  {
    company: 'МСДис',
    period: '03.2026 — н. в.',
    role: 'Fullstack-разработчик с фокусом на frontend',
    location: 'Москва',
    current: true,
    projects: [
      {
        name: 'Корпоративный таск-трекер «Шива»',
        stack: 'Vue 3, TypeScript, Vite, Vue Query, Vue Flow, ELK, Chart.js',
        bullets: [
          'В frontend-команде из 5 человек отвечал за архитектуру, декомпозицию, ревью и CI.',
          'Реализовал диаграммы бизнес-процессов на Vue Flow с автоматической компоновкой узлов через ELK.',
          'Подключил Vue Query для кэширования данных API и Chart.js для графиков.',
          'Интегрировал корпоративный модульный фреймворк в приложение.',
        ],
      },
      {
        name: 'АПГ',
        stack: 'Vue 3, TypeScript, Vitest, Playwright, REST API',
        bullets: [
          'Руководил разработкой, организовал монорепозиторий и разработал UI Kit.',
          'Развивал unit-тесты на Vitest для отправки обращений: ошибки API, повторные запросы и ключи идемпотентности.',
          'Проверял гонки ответов API, отмену запросов через AbortController и очистку при размонтировании Vue-компонента.',
          'Дорабатывал e2e-тест на Playwright: каталог → карточка → расчёт → обращение с проверкой сохранения данных в PostgreSQL.',
        ],
      },
      {
        name: 'Корпоративный портал МСДис',
        stack: 'Nuxt, Vue 3, TypeScript, Vite',
        bullets: [
          'Разрабатывал портал на Nuxt с учётом SEO и общие composables.',
          'Написал общий HTTP-клиент; разработал базовый UI Kit и дизайн-токены по макетам.',
        ],
      },
      {
        name: '«Системный специалист» — учёт инструментов',
        stack: 'Vue 3, .NET 10.0, Nx, npm workspaces, PWA',
        bullets: [
          'Интегрировал Nx и npm workspaces в монорепозиторий; реализовал PWA-версию приложения.',
        ],
      },
      {
        name: 'TRIP — фреймворк для проектов с ИИ-агентами',
        stack: 'Интеграции: CI, корпоративный таск-трекер',
        bullets: [
          'Разрабатывал цикл ИИ-агента, интеграцию с корпоративным таск-трекером и подключение среды автономной разработки к CI.',
        ],
      },
    ],
  },
  {
    company: 'BarsGroup',
    period: '11.2024 — 03.2026',
    role: 'Frontend-разработчик',
    location: 'Казань',
    projects: [
      {
        name: 'Plex-UI — корпоративная дизайн-система',
        stack: 'Vue 3, TypeScript, Composition API',
        bullets: [
          'Дизайн-система на Vue 3, 50+ компонентов.',
          'Разработал VirtualScroll для компонентов с линейной структурой данных: списки из 10 000+ строк без сторонних библиотек виртуализации.',
          'Разработал древовидную таблицу с виртуализацией, SearchSelectInput и MenuButton.',
        ],
      },
      {
        name: 'Биллинговая система ЖКХ',
        stack: 'Nuxt 3, TypeScript, Plex-UI, Vite, VueUse, Yarn Workspaces, Jest, Vitest',
        bullets: [
          'Разрабатывал интерфейсы и Nuxt-плагины; работал с API-контрактами и библиотеками core/ui-kit в монорепозитории Yarn Workspaces.',
          'Перевёл тесты с Jest на Vitest. Медианное время выполнения тестового этапа CI сократилось на 70% на сопоставимых запусках.',
          'Разработал useGridSchema и генератор псевдосхем DTO для конфигурации гридов, сократив ручную настройку таблиц.',
        ],
      },
      {
        name: 'АИС «Реформа ЖКХ»',
        stack: 'Vue 3, TypeScript, Vite, OpenAPI, Git Submodules',
        bullets: [
          'Разрабатывал frontend-модули на Vue 3 в микрофронтенд-архитектуре.',
          'Интегрировал генерацию клиентских API-сервисов по OpenAPI-описанию при изменениях API backend; подключал общие библиотеки через Git Submodules.',
        ],
      },
      {
        name: 'УАРТ',
        stack: 'Nuxt, TypeScript, Vite, i18n',
        bullets: [
          'Разрабатывал Nuxt middleware и плагины приложения. Внедрил i18n-механизм интернационализации.',
        ],
      },
    ],
  },
  {
    company: 'ITCODE',
    period: '01.2023 — 11.2024',
    role: 'Frontend-разработчик Vue и TypeScript',
    location: 'Стек: Vue 2 / Vue 3, TypeScript, Nuxt, Pinia, Vuex, Vite, Webpack',
    projects: [
      {
        name: 'Система экстренного реагирования 112',
        stack: 'Vue 2, Vue 3, TypeScript, Vuex, Pinia, Leaflet, FSD, Web API, Element Plus',
        bullets: [
          'Перевёл проект с Vue 2, Options API и Vuex на Vue 3, Composition API и Pinia; внедрил строгую типизацию TypeScript и Feature-Sliced Design (FSD).',
          'Разработал корпоративный UI Kit на базе Element Plus и выделил его в отдельный npm-пакет; реализовал кастомную валидацию и общий билдер масок ввода.',
          'Реализовал карту Leaflet с кластеризацией и движущимися маркерами, модуль диагностики устройств и composables для браузерных Web API.',
        ],
      },
      {
        name: 'Медицинская система 103',
        stack: 'Телефония: WebRTC, JsSIP',
        bullets: [
          'Сопровождал frontend медицинской системы и браузерную телефонию на WebRTC и JsSIP.',
        ],
      },
      {
        name: 'Система 122',
        stack: 'Интеграции: REST API',
        bullets: [
          'Разрабатывал формы с валидацией и таблицы с фильтрами. Подключал REST API и выполнял адаптивную вёрстку.',
        ],
      },
      {
        name: 'Внутренние сервисы ITCODE',
        stack: 'Vue.js, Pinia, REST API, корпоративный UI Kit',
        bullets: [
          'Реализовал метафреймворк с роутингом, Pinia Store и корпоративным UI Kit, включёнными в сборку приложения, для сокращения шаблонного кода.',
        ],
      },
    ],
  },
  {
    company: 'Фриланс',
    period: '08.2023 — 01.2024',
    role: 'Frontend-разработчик · удалённо',
    location: '4 месяца работы в указанном периоде, параллельно работе в ITCODE',
    projects: [
      {
        name: 'Интернет-магазин строительных материалов',
        stack: 'Quasar Framework v2, Vue 3, SSR, REST API',
        bullets: [
          'Разработал адаптивный каталог из 500+ товаров с фильтрами, сортировкой и REST API.',
          'Реализовал корзину и валидацию заказа; сократил оформление с 5 до 3 шагов.',
          'Оптимизировал SSR в Quasar: время генерации страницы сократилось на 20%. Добавил ленивую загрузку компонентов и изображений.',
        ],
      },
    ],
  },
]

export const projects: Project[] = [
  { name: 'Plex-UI', company: 'BarsGroup', stack: 'Vue 3, TypeScript', result: 'Дизайн-система: 50+ компонентов, VirtualScroll на 10 000+ строк, древовидная таблица', category: 'ui-kit' },
  { name: 'АПГ', company: 'МСДис', stack: 'Vue 3, Vitest, Playwright', result: 'UI Kit + монорепозиторий; unit-тесты ошибок API и ключей идемпотентности, e2e-сценарий', category: 'ui-kit' },
  { name: 'Корпоративный портал МСДис', company: 'МСДис', stack: 'Nuxt, Vue 3, TypeScript', result: 'Портал с SEO; общий HTTP-клиент, базовый UI Kit и дизайн-токены по макетам', category: 'nuxt' },
  { name: 'Биллинговая система ЖКХ', company: 'BarsGroup', stack: 'Nuxt 3, TypeScript, Plex-UI', result: 'Jest → Vitest: медианное время тестового этапа CI −70%; useGridSchema для гридов', category: 'nuxt' },
  { name: 'УАРТ', company: 'BarsGroup', stack: 'Nuxt, TypeScript, i18n', result: 'Nuxt middleware и плагины; внедрён i18n-механизм интернационализации', category: 'nuxt' },
  { name: '«Системный специалист»', company: 'МСДис', stack: 'Vue 3, Nx, npm workspaces, PWA', result: 'Монорепозиторий на Nx + npm workspaces; PWA-версия приложения учёта инструментов', category: 'infra' },
  { name: 'TRIP', company: 'МСДис', stack: 'ИИ-агенты, CI', result: 'Цикл ИИ-агента, интеграция с таск-трекером и средой автономной разработки в CI', category: 'infra' },
  { name: 'АИС «Реформа ЖКХ»', company: 'BarsGroup', stack: 'Vue 3, OpenAPI, Git Submodules', result: 'Микрофронтенды; кодогенерация API-клиентов по OpenAPI при изменениях backend', category: 'infra' },
  { name: 'Метафреймворк ITCODE', company: 'ITCODE', stack: 'Vue.js, Pinia, UI Kit', result: 'Роутинг, Pinia Store и корпоративный UI Kit в сборке — меньше шаблонного кода', category: 'infra' },
  { name: 'Таск-трекер «Шива»', company: 'МСДис', stack: 'Vue 3, Vue Flow, ELK, Chart.js', result: 'Диаграммы бизнес-процессов с автокомпоновкой через ELK; архитектура и CI в команде из 5', category: 'product' },
  { name: 'Система 112', company: 'ITCODE', stack: 'Vue 2→3, Pinia, FSD, Leaflet', result: 'Миграция на Vue 3 + TS + FSD; UI Kit в npm-пакете; карта Leaflet с кластеризацией', category: 'ui-kit' },
  { name: 'Медицинская система 103', company: 'ITCODE', stack: 'WebRTC, JsSIP', result: 'Браузерная телефония на WebRTC/JsSIP в медицинской системе', category: 'product' },
  { name: 'Система 122', company: 'ITCODE', stack: 'Vue, REST API', result: 'Формы с валидацией, таблицы с фильтрами, адаптивная вёрстка', category: 'product' },
  { name: 'Интернет-магазин стройматериалов', company: 'Фриланс', stack: 'Quasar v2, SSR, REST API', result: 'Каталог 500+ товаров; чекаут с 5 до 3 шагов; SSR быстрее на 20%', category: 'product' },
]

export const projectCategories: Array<{ key: 'all' | ProjectCategory; label: string }> = [
  { key: 'all', label: 'Все' },
  { key: 'ui-kit', label: 'UI Kit' },
  { key: 'nuxt', label: 'Nuxt' },
  { key: 'infra', label: 'Инфраструктура' },
  { key: 'product', label: 'Продукт' },
]

export const skills: SkillGroup[] = [
  {
    label: 'Frontend',
    items: ['Vue 2 / Vue 3', 'Nuxt 3', 'TypeScript', 'JavaScript', 'Composition API', 'Pinia', 'Vuex', 'HTML5', 'CSS3', 'SCSS', 'Адаптивная вёрстка'],
  },
  {
    label: 'API и архитектура',
    items: ['REST API', 'OpenAPI', 'Vue Query', 'Web API', 'SPA', 'SSR', 'FSD', 'UI Kit', 'Монорепозитории', 'Nx', 'npm workspaces', 'Yarn Workspaces'],
  },
  {
    label: 'Тестирование и инструменты',
    items: ['Vitest', 'Jest', 'Playwright', 'Vue Test Utils', 'Vite', 'Webpack', 'Git', 'CI'],
  },
  {
    label: 'Дополнительно',
    items: ['Quasar', 'Element Plus', 'i18n', 'PWA', 'WebRTC', 'JsSIP', 'Vue Flow', 'ELK'],
  },
]

export const stackStrip = [
  'Vue 3',
  'Nuxt 3',
  'TypeScript',
  'Pinia',
  'Composition API',
  'Vite',
  'Vitest',
  'Playwright',
  'FSD',
  'OpenAPI',
  'PWA',
  'WebRTC',
  'i18n',
  'SSR',
]

export const languages = [
  { label: 'Русский', level: 'родной' },
  { label: 'English', level: 'B1' },
]

export const education = {
  school: 'Уфимский университет науки и технологий (УУНиТ)',
  period: '2023 — настоящее время',
  program: 'ФИРТ · Прикладная информатика (по областям)',
  note: 'Неоконченное высшее, сейчас в академическом отпуске.',
}
