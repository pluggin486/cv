<script setup lang="ts">
interface Props {
  delay?: number
}

const props = withDefaults(defineProps<Props>(), {
  delay: 0,
})

const el = ref<HTMLElement | null>(null)
const enabled = ref(false)

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  enabled.value = true

  const target = el.value
  if (!target) return

  const observer = new IntersectionObserver((entries) => {
    if (entries[0]?.isIntersecting) {
      target.classList.add('is-in')
      observer.disconnect()
    }
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' })

  observer.observe(target)
  onBeforeUnmount(() => observer.disconnect())
})
</script>

<template>
  <div
    ref="el"
    class="ui-reveal"
    :class="{ 'is-enabled': enabled }"
    :style="enabled ? { transitionDelay: `${delay}ms` } : undefined"
  >
    <slot />
  </div>
</template>

<style scoped>
.ui-reveal.is-enabled {
  opacity: 0;
  transform: translateY(10px);
  transition: opacity var(--motion-04) var(--ease-standard), transform var(--motion-04) var(--ease-standard);
}

.ui-reveal.is-enabled.is-in {
  opacity: 1;
  transform: translateY(0);
}
</style>
