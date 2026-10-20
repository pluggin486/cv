<template>
  <p class="ui-eyebrow"><slot /></p>
</template>

<style scoped>
.ui-eyebrow {
  margin: 0;
  color: var(--accent-strong);
  font: var(--text-eyebrow) var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
</style>
