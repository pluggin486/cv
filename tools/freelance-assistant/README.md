# Локальный помощник откликов

Проект принимает сохранённые уведомления `.eml`, JSON-записи или описание, введённое вручную. Он отмечает совпадения по ключевым словам, объясняет оценку, выбирает подтверждённые факты из резюме и создаёт markdown-черновики в `.local/freelance-assistant/drafts/`.

Скрипт использует только Python standard library. Он не входит в аккаунты, не открывает страницы бирж, не читает cookies и пароли, не отправляет отклики и не вызывает внешние API. Перед отправкой человек проверяет каждый черновик и вручную обновляет локальную квоту.

## Входной JSON

```json
{
  "jobs": [
    {
      "platform": "flru",
      "id": "job-123",
      "url": "https://example.test/job-123",
      "title": "Vue 3: доработать таблицу",
      "description": "Нужны Vue, Nuxt и виртуализация списка.",
      "budget": "по договорённости",
      "deadline": "2026-11-10",
      "project_type": "for_all"
    }
  ]
}
```

Для `.eml` передайте площадку отдельно; заголовок берётся из Subject, текст — из plain text или HTML-тела письма. Вложения не открываются.

## Команды Nx

- `nx run freelance-assistant:match -- --input .local/freelance-assistant/jobs.json`
- `nx run freelance-assistant:match -- --input .local/freelance-assistant/notice.eml --platform flru`
- `nx run freelance-assistant:manual -- --platform kwork --title "Vue 3 форма" --description "Добавить проверку формы и связать её с REST API"`
- `nx run freelance-assistant:quota`
- `nx run freelance-assistant:quota -- --platform kwork --limit 12`
- `nx run freelance-assistant:mark-sent -- --platform peopleperhour --job-id 123`

`mark-sent` только записывает уже отправленный вручную отклик. Учёт PeoplePerHour считается с начала текущего календарного месяца из 15 бесплатных credits. Лимит Kwork не угадывается: его нужно сверить в аккаунте и задать локально. На FL.ru стоимость определяется типом проекта и меткой «для всех»; универсальной месячной квоты нет.

## Оценка

Vue, Nuxt, TypeScript и frontend-формулировки дают профильное совпадение. React и Svelte дают заметную метку «проверить вручную», поскольку CV не подтверждает этот опыт. Общие слова вроде «программирование» дают низкое совпадение и тоже требуют проверки. Бюджет и срок без данных указываются как требующие уточнения. Повторные ID или URL не порождают второй черновик.

Все входные уведомления, локальные квоты, история и тексты профилей хранятся под `.local/`, который исключён из Git.
