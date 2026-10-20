export function format(value: number): string {
  return new Intl.NumberFormat('ru-RU').format(value)
}
