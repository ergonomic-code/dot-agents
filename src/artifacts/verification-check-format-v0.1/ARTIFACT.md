# Verification Check Format

## Goal

Write requirement verification checks as concise contract prose.
Use one format for requirement derivation, requirement review, test-case design, executable test-case writing, and reverse engineering from tests.

## Structure

Use one `Feature` per one concrete endpoint, API surface, component, operation, or other object under verification.
Use one `Rule` per one externally observable required property, invariant, rejection, side effect, or result obligation.
Use named `Example` only to enumerate materially distinct input or context classes for the same `Rule`.
Use unnamed `Example` only as the full-mode case container when no example name is needed.
If a `Rule` has an unnamed `Example`, that unnamed example must be the only `Example` under that `Rule`.
Do not use `Example` for independent properties.
Keep one abstraction level inside one `Feature`.
Write `Rule` in the obligation form of the artifact language when that language has one.
For Russian `Rule`, use `должен` or `должна`.
Put any input or state condition either before the obligation or after the required output.
Bare present-tense descriptions are nonconforming unless they are exact public contract wording.
Write all human-readable text in the configured `artifact_language`.
Use only the English keywords `Feature`, `Rule`, `Example`, `Given`, `When`, `Then`, and `And`.
Read `references/layout.md` before rendering.

## Optional Source Reference

One `Rule` or `Example` block may carry at most one optional source reference.
Treat it as metadata, not as a `Given` / `When` / `Then` step.
In plain artifact text, place the machine form immediately under `Rule` when no `Example` is rendered, or immediately under the matching `Example`.
When the surrounding container supports clickable links, the same metadata may be rendered in a container-native human form outside the raw artifact block.
Read `references/source-reference.md`.

## Modes

This artifact has exactly two modes:
- `short`
- `full`

Both modes require `Feature` and `Rule`.
`short` keeps only `Feature`, `Rule`, and optional named `Example` lines.
If a `Rule` has exactly one unnamed `Example` in `full`, omit that `Example` in `short`.
`full` adds one or more `Example` blocks with `Given`, `When`, `Then`, and `And` under each `Rule`.
In `full`, unnamed examples render as `Example`.

Read the mode rules in:
- `references/mode-short.md`
- `references/mode-full.md`

## Shared Content Rules

Describe only externally observable contract behavior.
Use domain language.
Mention technical details only when they are observable contract terms and no stable domain wording can express the same behavior.
When a request parameter, field, flag, enum value, status, timestamp, or other technical symbol has a stable domain meaning, write that meaning instead of the literal symbol.
Do not keep a literal only because it appears in API, storage, code, or tests.
Keep literal symbols only when the requirement is specifically about that named contract member or value, no clear domain equivalent exists, or replacing it would lose checked precision.
Keep only contract-visible requirements about request interpretation, authoritative data sources, decision logic, result scope and selection, required response or returned-value properties, ordering, cardinality, state changes, side effects, rejection conditions, explicit invariants, and representation of contract-visible values.
Do not mention implementation structure, storage schema, helper names, mocks, fixtures, or migration steps.
Do not invent routes, statuses, defaults, validation, fallback behavior, or internal design.
Keep behaviorally distinguishing literal values literal when they are part of the contract.
Otherwise prefer abstract wording over incidental sample data.
Merge near-duplicate rules and examples into the smallest complete non-redundant set.
