<script setup lang="ts">
import type { SideNavGroup } from '@rolftech/core-ui'

const route = useRoute()
const router = useRouter()

const groups: SideNavGroup[] = [
  {
    label: 'Кандидат',
    items: [
      { key: '/', label: 'Обзор' },
      { key: '/experience', label: 'Опыт' },
      { key: '/projects', label: 'Проекты' },
      { key: '/skills', label: 'Навыки' },
    ],
  },
  {
    label: 'Связь',
    items: [{ key: '/contacts', label: 'Контакты' }],
  },
]

const bottomItems = groups.flatMap(group => group.items)

const section = computed<string>({
  get: () => route.path,
  set: (path: string) => {
    router.push(path)
  },
})

const theme = ref<'light' | 'dark'>('light')

onMounted(() => {
  theme.value = document.documentElement.dataset.theme === 'dark' ? 'dark' : 'light'
})

const toggleTheme = () => {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'
  document.documentElement.dataset.theme = theme.value
  localStorage.setItem('rt-theme', theme.value)
}
</script>

<template>
  <div class="ws-page">
    <div class="ws-bar">
      <strong>Семён Сергеев <span class="ws-bar__dim">/ Frontend Developer</span></strong>
      <div class="ws-bar__actions">
        <UiStatus variant="pill" label="Открыт к предложениям" class="ws-bar__status" />
        <button class="ws-theme mono" type="button" :aria-label="`Переключить тему: сейчас ${theme === 'dark' ? 'тёмная' : 'светлая'}`" @click="toggleTheme">
          {{ theme === 'dark' ? 'DARK' : 'LIGHT' }}
        </button>
      </div>
    </div>
    <div class="ws-body">
      <aside class="ws-side">
        <UiSideNav v-model="section" :groups="groups" />
      </aside>
      <section class="ws-main">
        <slot />
      </section>
    </div>

    <nav class="ws-bottombar" aria-label="Разделы">
      <NuxtLink
        v-for="item in bottomItems"
        :key="item.key"
        class="ws-bottombar__item mono"
        :to="item.key"
        :aria-current="item.key === route.path ? 'page' : undefined"
      >
        {{ item.label }}
      </NuxtLink>
    </nav>
  </div>
</template>

<style scoped>
.ws-page {
  --page-gutter: clamp(20px, 4vw, 64px);
  width: min(var(--container), calc(100% - (var(--page-gutter) * 2)));
  margin-inline: auto;
  padding-block: clamp(24px, 4vw, 56px);
  flex: 1;
}

.ws-bar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  min-height: 52px;
  padding: 8px var(--space-4);
  border: 1px solid var(--border);
  border-bottom: 0;
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  background: var(--surface);
  font-size: 14px;
}

.ws-bar strong {
  letter-spacing: -0.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.ws-bar__dim {
  color: var(--muted);
  font-weight: 500;
}

.ws-bar__actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-shrink: 0;
}

.ws-theme {
  min-height: 32px;
  padding: 4px 10px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: transparent;
  color: var(--muted);
  font-size: 10px;
  letter-spacing: 0.08em;
  cursor: pointer;
  transition: color var(--motion-02) var(--ease-standard), border-color var(--motion-02) var(--ease-standard);
}

.ws-theme:hover {
  color: var(--fg);
  border-color: var(--muted);
}

.ws-body {
  display: grid;
  grid-template-columns: 200px minmax(0, 1fr);
  border: 1px solid var(--border);
  border-radius: 0 0 var(--radius-lg) var(--radius-lg);
  background: var(--surface);
  overflow: hidden;
}

.ws-side {
  padding: var(--space-3);
  border-right: 1px solid var(--border);
  background: color-mix(in oklch, var(--bg) 72%, var(--surface));
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
}

.ws-main {
  min-width: 0;
  padding: clamp(var(--space-4), 3vw, var(--space-5));
}

.ws-bottombar {
  display: none;
}

@media (max-width: 820px) {
  .ws-body {
    grid-template-columns: 1fr;
  }

  .ws-side {
    display: none;
  }

  .ws-page {
    padding-bottom: 76px;
  }

  .ws-bottombar {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 30;
    display: grid;
    grid-auto-flow: column;
    justify-content: space-around;
    border-top: 1px solid var(--border);
    background: var(--surface);
    padding-bottom: env(safe-area-inset-bottom);
  }

  .ws-bottombar__item {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 56px;
    padding: 8px 12px;
    border-top: 2px solid transparent;
    margin-top: -1px;
    color: var(--muted);
    font-size: 11px;
    text-decoration: none;
    transition: color var(--motion-02) var(--ease-standard), border-color var(--motion-02) var(--ease-standard);
  }

  .ws-bottombar__item[aria-current='page'] {
    border-top-color: var(--accent);
    color: var(--fg);
    font-weight: 650;
  }
}

@media print {
  .ws-page {
    width: 100%;
    padding: 0;
  }

  .ws-bar,
  .ws-side,
  .ws-bottombar {
    display: none;
  }

  .ws-body {
    border: 0;
    border-radius: 0;
    overflow: visible;
  }

  .ws-main {
    padding: 0;
  }
}
</style>
