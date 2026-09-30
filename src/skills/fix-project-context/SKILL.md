---
name: fix-project-context
description: Исправляет локальные инструкции агента в целевом проекте, который использует фреймворк.
---

# Исправление контекста целевого проекта

Определи `framework_checkout_root` по каноническому пути этого `SKILL.md` после разрешения симлинков: это корень репозитория над `src/skills/fix-project-context/`.
Считай `project_root` корнем текущего репозитория.
Прочитай `framework_checkout_root/src/references/context-fix-minimality.md`.
Прочитай `framework_checkout_root/src/references/context-fix-workflow.md`.

Изменяемые корни:
- `project_root/AGENTS.md`
- локальные `project_root/.agents/**` вне `framework_checkout_root/**`
- локальные `project_root/.codex/**` вне `framework_checkout_root/**`
- `project_root/README.md` только когда он является действующей точкой входа для агента или самым узким согласованным местом.

Если запрос относится к `framework_checkout_root/src/**`, `bootstrap/**` или `docs/**`, предложи `$fix-framework-context`.
