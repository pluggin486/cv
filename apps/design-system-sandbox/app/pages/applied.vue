<script setup lang="ts">
useHead({ title: 'ROLFTECH — рабочее окно сделки' })
</script>

<template>
  <div class="applied-page">
    <header class="applied-head">
      <div>
        <UiEyebrow>ONE-WINDOW WORKSPACE</UiEyebrow>
        <h1>Сделка и следующий шаг</h1>
      </div>
      <p>Статус, контекст сделки и очередь задач в одной рабочей поверхности. UI-kit: SideNav, Status, Tabs, DataTable, Button.</p>
    </header>
    <DealWorkspace />
    <p class="applied-note">
      Applied UI связывает статус, контекст сделки и следующий шаг в одной рабочей поверхности.
    </p>
  </div>
</template>

<style scoped>
.applied-page {
  --page-gutter: clamp(20px, 4vw, 64px);
  width: min(var(--container), calc(100% - (var(--page-gutter) * 2)));
  margin-inline: auto;
  padding-block: clamp(32px, 5vw, 64px);
  flex: 1;
}

.applied-head {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(260px, 0.5fr);
  gap: var(--space-5);
  align-items: end;
  margin-bottom: var(--space-5);
}

.applied-head h1 {
  margin-top: var(--space-3);
  font-size: clamp(28px, 4vw, 44px);
  line-height: 1.02;
  letter-spacing: -0.035em;
}

.applied-head p {
  color: var(--muted);
  font-size: 14px;
  line-height: 1.5;
}

.applied-note {
  margin-top: var(--space-4);
  color: var(--muted);
  font-size: 13px;
}

@media (max-width: 820px) {
  .applied-head {
    grid-template-columns: 1fr;
    gap: var(--space-3);
  }
}
</style>
