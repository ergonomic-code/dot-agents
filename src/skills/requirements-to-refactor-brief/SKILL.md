---
name: requirements-to-refactor-brief
description: Write or update a formal `010-refactor-brief.md` from raw structural-change requirements. Use when the user provides a one-liner, notes, chat dump, issue text, interview answers, or an incomplete refactor brief and wants a repo-style standalone refactor task brief that preserves behavior.
---

# Write Refactor Brief From Requirements

Use configured `artifact_language` for the brief artifact.
Read `framework_checkout_root/src/conventions/lightwight-markup-authoring.md` before writing.
Use it only for documentation formatting.
If it conflicts with this skill or the refactor-brief structure, keep this skill.
Read `framework_checkout_root/src/conventions/feature-workdir.md`.
Use it only for current workdir resolution and flat devlog directory placement.
Read `framework_checkout_root/src/conventions/refactor-flow.md`.
Treat `framework_checkout_root/src/conventions/refactor-flow.md` as the source of truth for standalone refactor phases, behavior-preservation boundaries, progress.md shape, and execution rules.
If the request or referenced material mentions Ergonomic Architecture, `EA`, `EP`, aggregates, operations, resources, DOPs, target architecture, architecture refactoring, or acceptance by tech lead through code shape, also read `framework_checkout_root/src/conventions/ergonomic-architecture.md` and follow its projection-specific loading rules before writing.

## Refactor artifact bindings

- artifact phase code: `010`
- default refactor-dir output path: `<refactor-dir>/010-refactor-brief.md`
- progress.md checklist item: `Определить границу и ожидаемое структурное улучшение`
- artifact phase `010` bootstrap: this skill may create the refactor directory when unresolved

## Refactor brief structure

Use this structure unless the existing brief has a compatible complete shape:

~~~md
# <YYMMDD - краткое название - рефакторинг-бриф>

## Контекст

<какой участок структуры мешает работе и почему эта итерация ограничена refactor-only изменением>

## Цель рефакторинга

1. <ожидаемое структурное улучшение без изменения поведения>

## Граница рефакторинга

- <production или test область и допустимая call-site propagation>

## Сохранение поведения

- <существующая или требуемая проверка текущего поведения>

## Критерии приёмки

1. <проверяемый structural outcome>
2. <проверка сохранения поведения>
~~~

## Workflow

- Treat an explicit refactor directory or brief path as the target.
- When this run creates a new refactor directory, also create `<refactor-dir>/progress.md` from the progress template in `refactor-flow.md`.
- Create or update the resolved brief path.
- Build context only from the user request, explicitly referenced files, files already inside the target refactor directory when it exists, and interview answers.
- Use loaded project context only to identify named architecture or framework constraints.
- Work in interview mode before writing or updating the brief.
- If refactor boundary, structural problem, expected structural improvement, behavior-preservation check, or acceptance criteria are unclear, ask the first blocking question and stop.
- Ask exactly one question per turn.
- Confirm each assumption in chat before relying on it.
- After the user confirms an assumption, write it as context, refactor goal, boundary, behavior-preservation check, term, or acceptance criterion.
- Do not write unconfirmed assumptions into the brief.
- Do not convert silence into approval.
- Write only the target structural change in this refactor task.
- Do not add behavior requirements, endpoint contracts, config changes, retries, defaults, compatibility branches, or product decisions.
- Do not describe implementation increments unless the user explicitly requires them as acceptance scope.
- Preserve correct parts of an existing brief.
- Rewrite only vague, conflicting, duplicated, behavior-changing, or scope-breaking parts.
- Always produce a complete formal brief with the core sections from the structure above.
- Add optional sections only when they add signal.
- Do not leave placeholders in a generated or updated brief.
- If a non-critical gap remains, ask whether to keep it open or resolve it now.
- Add `Открытые вопросы` only when the user explicitly says to leave a question open.
- If a critical gap blocks a correct refactor boundary or behavior-preservation statement, stop and ask.

## Output Rules

- Write the brief in `artifact_language`.
- Describe the structural delta from the current code or test shape, not the whole subsystem.
- Keep the brief at refactor-goal, boundary, behavior-preservation, and acceptance level.
- Keep implementation planning and stage breakdown out of the brief.
- Do not include unresolved assumptions.
- Do not include open questions unless explicitly requested by the user.
- Cover the structural goal, allowed boundary, forbidden behavior changes, validation evidence, and important exclusions.
