# Feature Directory Index Template

Use this template when creating `index.md` for a new feature directory.
Render all human-readable text in `artifact_language`.
For this repo with `artifact_language: ru`, use the Russian text below.

## File Template

This fenced block is the target file content.

~~~md
# Индекс каталога

Каталог содержит артефакты по фиче `<feature title>`.

## Содержимое

| Путь | Назначение |
| --- | --- |
| [010-feature-brief.md](./010-feature-brief.md) | Основной фича-бриф. |
| [progress.md](./progress.md) | Текущий статус проработки и реализации фичи. |
~~~

## Agent Rules

- Keep the file short.
- List only files and directories that already exist or are being created in the same step.
