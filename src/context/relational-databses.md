---
requires_modules:
  - database
applies_when: Работа затрагивает схему реляционной БД, запросы к ней или транзакции.
routing_order: 40
---

# Контекст реляционных баз данных

Загружай только пункты, соответствующие запрошенной или запланированной работе с БД:

- добавление или изменение миграций продакшн-схемы БД: `../conventions/database/db-schema-migrations.md`;
- добавление или изменение кода, работающего внутри транзакции или содержащего логику внесения или изменения данных в БД (на уровне SQL): `../conventions/database/transaction-boundaries.md`;
- добавление или изменение SQL SELECT-запросов: `../conventions/database/db-query-shaping.md`;
- добавление или изменение DTO для работы с БД и мапперов строк БД: `../conventions/database/db-read-model-boundaries.md`;
- добавление или изменение условных атомирных модификаций данных на уровне БД: `../conventions/database/db-conditional-writes.md`.

После внесения изменений выполни `../conventions/database/checklist.md`.
Если найдёшь нарушения - внеси правки для их устранения.