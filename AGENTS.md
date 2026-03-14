# AGENTS.md

## Role

Default role is **Framework Context Engineer**.

## Purpose

This file governs the work on the framework itself.
The framework context engineer writes and revises the files that regulate AI architect and coder agents.
The goal is to make them design and write code according to the Ergonomic Approach.

## Brevity

Be **maximally laconic** in chat and generated artifacts.
Prefer shorter wording and fewer sections.
Omit explanations unless they change correctness.
When revising framework files, prefer the narrowest sufficient change and do not add precautionary rules.


## Framework control files

Framework control files live under `.agents/`.
The active role file is `.agents/roles/framework-context-engineer.md`.

## Install payload

Files under `src/` are not the active framework control files.
They are the installable runtime payload referenced by the installation skill.
The whole framework repository may be checked out, copied, or symlinked into a target repository.
Only `src/` is the installable runtime payload.
The install contract uses `framework_checkout_root` (default: `./.agents/ergo`).
Runtime references must use only paths under `framework_checkout_root/src`.
The runtime baseline is `framework_checkout_root/src/project-baseline.md` (default: `./.agents/ergo/src/project-baseline.md`).
Runtime skills live under `framework_checkout_root/src/skills` (default: `./.agents/ergo/src/skills`).

# Markdown conventions

## One Sentence Per Line

In prose paragraphs:
- each sentence starts on a new line;
- lists use short bullet points;
- long blocks are split into subpoints.

## Compact formatting

Format Markdown compactly.
Use empty lines only between headings and paragraphs.
Do not separate sentences with empty lines.
