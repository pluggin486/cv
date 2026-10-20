<script setup lang="ts">
import { identity as who } from '~/utils/resume'

definePageMeta({ layout: 'workspace' })
useHead({ title: 'Контакты — Семён Сергеев' })

const copiedKey = ref('')

const copy = async (key: string, value: string) => {
  try {
    await navigator.clipboard.writeText(value)
    copiedKey.value = key
    setTimeout(() => {
      copiedKey.value = ''
    }, 1600)
  }
  catch {
    /* clipboard недоступен — остаётся ручное копирование */
  }
}
</script>

<template>
  <div class="cnt">
    <UiEyebrow>СВЯЗЬ / КОНТАКТЫ</UiEyebrow>
    <h1>Открыт к предложениям</h1>
    <p class="cnt-sub">{{ who.role }} · {{ who.stackLine }} · {{ who.location }}</p>

    <div class="cnt-actions">
      <UiButton variant="primary" :href="who.telegramHref" target="_blank">
        Telegram {{ who.telegram }}
      </UiButton>
      <UiButton variant="secondary" :href="who.emailHref">{{ who.email }}</UiButton>
      <UiButton variant="ghost" :href="who.phoneHref">{{ who.phone }}</UiButton>
    </div>

    <div class="cnt-rows">
      <div class="cnt-row">
        <span class="mono cnt-key">TELEGRAM</span>
        <a class="cnt-value" :href="who.telegramHref" target="_blank" rel="noopener noreferrer">{{ who.telegramHref.replace('https://', '') }}</a>
        <UiButton variant="ghost" size="sm" :aria-label="copiedKey === 'tg' ? 'Ссылка скопирована' : 'Скопировать Telegram'" @click="copy('tg', who.telegramHref)">
          {{ copiedKey === 'tg' ? 'Скопировано' : 'Копировать' }}
        </UiButton>
      </div>
      <div class="cnt-row">
        <span class="mono cnt-key">EMAIL</span>
        <a class="cnt-value" :href="who.emailHref">{{ who.email }}</a>
        <UiButton variant="ghost" size="sm" :aria-label="copiedKey === 'email' ? 'Email скопирован' : 'Скопировать email'" @click="copy('email', who.email)">
          {{ copiedKey === 'email' ? 'Скопировано' : 'Копировать' }}
        </UiButton>
      </div>
      <div class="cnt-row">
        <span class="mono cnt-key">PHONE</span>
        <a class="cnt-value" :href="who.phoneHref">{{ who.phone }}</a>
        <UiButton variant="ghost" size="sm" :aria-label="copiedKey === 'phone' ? 'Телефон скопирован' : 'Скопировать телефон'" @click="copy('phone', who.phone)">
          {{ copiedKey === 'phone' ? 'Скопировано' : 'Копировать' }}
        </UiButton>
      </div>
      <div class="cnt-row">
        <span class="mono cnt-key">ФОРМАТ</span>
        <span class="cnt-value cnt-value--muted">{{ who.location }} · {{ who.employment }}</span>
      </div>
    </div>
    <p class="cnt-live mono" aria-live="polite">{{ copiedKey ? 'Скопировано в буфер обмена' : '' }}</p>
  </div>
</template>

<style scoped>
.cnt {
  display: grid;
  gap: var(--space-4);
}

h1 {
  font-size: clamp(24px, 4vw, 34px);
  letter-spacing: -0.03em;
}

.cnt-sub {
  margin-top: -8px;
  color: var(--muted);
  font-size: 14px;
}

.cnt-actions {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}

.cnt-rows {
  display: grid;
  border-top: 1px solid var(--fg);
}

.cnt-row {
  display: grid;
  grid-template-columns: 110px minmax(0, 1fr) auto;
  gap: var(--space-3);
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
}

.cnt-key {
  color: var(--muted);
  font-size: 10px;
  letter-spacing: 0.08em;
}

.cnt-value {
  color: var(--fg);
  font-size: 14px;
  text-decoration: none;
  overflow-wrap: anywhere;
  transition: color var(--motion-02) var(--ease-standard);
}

a.cnt-value:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cnt-value--muted {
  color: var(--muted);
}

.cnt-live {
  min-height: 16px;
  margin: 0;
  color: var(--accent-strong);
  font-size: 11px;
}

@media (max-width: 520px) {
  .cnt-row {
    grid-template-columns: 1fr auto;
  }

  .cnt-key {
    grid-column: 1 / -1;
  }
}
</style>
