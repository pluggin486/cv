<script setup lang="ts">
import UiSkeleton from './Skeleton.vue'
import type { TableColumn } from '../types'

const skeletonWidths = ['82%', '46%', '64%', '58%']

defineProps<{
  columns: TableColumn[]
  rows: Array<Record<string, any>>
  caption?: string
  emptyLabel?: string
  loading?: boolean
}>()
</script>

<template>
  <div class="ui-table-wrap">
    <table class="ui-table">
      <caption v-if="caption" class="ui-table__caption">
        {{ caption }}
      </caption>
      <thead>
        <tr>
          <th
            v-for="col in columns"
            :key="col.key"
            class="ui-table__th"
            :class="{ 'is-mono': col.mono }"
            scope="col"
          >
            {{ col.label }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="loading">
          <td v-for="(col, index) in columns" :key="col.key" class="ui-table__td" :colspan="undefined">
            <UiSkeleton :width="skeletonWidths[index % skeletonWidths.length]" />
          </td>
        </tr>
        <tr v-else-if="rows.length === 0">
          <td class="ui-table__td ui-table__empty" :colspan="columns.length">
            {{ emptyLabel ?? 'Нет данных' }}
          </td>
        </tr>
        <tr v-for="(row, rowIndex) in rows" :key="rowIndex" class="ui-table__row">
          <td
            v-for="col in columns"
            :key="col.key"
            class="ui-table__td"
            :class="{ 'is-mono': col.mono }"
          >
            <slot :name="`cell-${col.key}`" :row="row" :value="row[col.key]">
              {{ row[col.key] }}
            </slot>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.ui-table-wrap {
  min-width: 0;
  overflow-x: auto;
}

.ui-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}

.ui-table__caption {
  text-align: left;
  padding-bottom: var(--space-2);
  color: var(--muted);
  font: 11px var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.ui-table__th {
  padding: 10px 12px;
  border-bottom: 1px solid var(--border);
  color: var(--muted);
  font: 11px var(--font-mono);
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  text-align: left;
  white-space: nowrap;
}

.ui-table__td {
  padding: 12px;
  border-bottom: 1px solid var(--border);
  text-align: left;
  vertical-align: middle;
}

.ui-table__row:hover .ui-table__td {
  background: var(--fg-soft);
}

.is-mono {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
}

.ui-table__empty {
  color: var(--muted);
}
</style>
