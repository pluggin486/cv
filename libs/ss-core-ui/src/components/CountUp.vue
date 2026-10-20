<script setup lang="ts">
import { format } from '../utils/format'

interface Props {
  value: number
  prefix?: string
  suffix?: string
  duration?: number
}

const props = withDefaults(defineProps<Props>(), {
  prefix: '',
  suffix: '',
  duration: 900,
})

const el = ref<HTMLElement | null>(null)
const display = ref(format(props.value))

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return

  const target = el.value
  if (!target) return

  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)')
  const observer = new IntersectionObserver((entries) => {
    if (!entries[0]?.isIntersecting) return
    observer.disconnect()

    const start = performance.now()
    const tick = (now: number) => {
      if (reduce.matches) {
        display.value = format(props.value)
        return
      }
      const progress = Math.min((now - start) / props.duration, 1)
      const eased = 1 - Math.pow(1 - progress, 3)
      display.value = format(Math.round(props.value * eased))
      if (progress < 1) requestAnimationFrame(tick)
    }
    requestAnimationFrame(tick)
  }, { threshold: 0.4 })

  observer.observe(target)
  onBeforeUnmount(() => observer.disconnect())
})
</script>

<template>
  <span ref="el" class="ui-countup mono">{{ prefix }}{{ display }}{{ suffix }}</span>
</template>
