# Verification Check Format

## Goal

Write requirement verification checks as concise contract prose.
Use one format for requirement derivation, requirement review, test-case design, executable test-case writing, and reverse engineering from tests.

## Structure

Use one `SUT` per one concrete endpoint, API surface, component, operation, or other object under verification.
Use one `Check` per one externally observable required property, invariant, rejection, side effect, or result obligation.
Use `Variant` only to enumerate materially distinct input or context classes for the same `Check`.
Do not use `Variant` for independent properties.
Keep one abstraction level inside one `SUT`.
Write `Check` in the obligation form of the artifact language when that language has one.
Write all human-readable text in the configured `artifact_language`.
Use only the English keywords `SUT`, `Check`, `Variant`, `Given`, `When`, `Then`, and `And`.
Read `references/layout.md` before rendering.

## Optional Source Reference

One `Check` block may carry at most one optional source reference.
Treat it as check metadata, not as a `Given` / `When` / `Then` step.
In plain artifact text, place the machine form immediately under `Check` or after its `Variant`.
When the surrounding container supports clickable links, the same metadata may be rendered in a container-native human form outside the raw check block.
Read `references/source-reference.md`.

## Modes

This artifact has exactly two modes:
- `short`
- `full`

Both modes require `SUT` and `Check`.
`short` keeps only `SUT`, `Check`, and optional `Variant` lines.
`full` adds `Given`, `When`, `Then`, and `And` under each `Check`.

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
Merge near-duplicate checks into the smallest complete non-redundant set.
