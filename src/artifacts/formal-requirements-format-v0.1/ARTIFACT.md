# Formal Requirements Format

## Goal

Write formal requirements as concise Gherkin-like contract prose.
Use one format for requirement derivation, requirement review, test-case design, executable test-case writing, and reverse engineering from tests.

## Structure

Use one `Feature` per one concrete endpoint, API surface, component, operation, or other concrete SUT element.
Use one `Rule` per one observable obligation or desired observable behavior property.
Use one `Scenario` per one materially distinct branch of one `Rule`.
Place each `Scenario` under its `Rule`.
Keep one abstraction level inside one `Feature`.
Write `Rule` in the obligation form of the artifact language when that language has one.
Write all human-readable text in the configured `artifact_language`.
Use only the English Gherkin keywords `Feature`, `Rule`, `Scenario`, `Given`, `When`, `Then`, and `And`.

## Optional Source Reference

One `Scenario` may carry at most one optional source reference.
Treat it as scenario metadata, not as a `Given` / `When` / `Then` step.
In plain artifact text, place the machine form immediately under `Scenario`.
When the surrounding container supports clickable links, the same metadata may be rendered in a container-native human form outside the raw Gherkin block.
Read `references/source-reference.md`.

## Modes

This artifact has exactly two modes:
- `short`
- `full`

Both modes require `Feature`, `Rule`, and `Scenario`.
`short` keeps only scenario headers.
`full` adds `Given`, `When`, `Then`, and `And` under each `Scenario`.

Read the mode rules in:
- `references/mode-short.md`
- `references/mode-full.md`

## Shared Content Rules

Describe only externally observable contract behavior.
Use domain language.
Mention technical details only when they are part of the stable public contract or no stable domain equivalent exists.
Keep only contract-visible requirements about request interpretation, authoritative data sources, decision logic, result scope and selection, required response or returned-value properties, ordering, cardinality, state changes, side effects, rejection conditions, explicit invariants, and representation of contract-visible values.
Do not mention implementation structure, storage schema, helper names, mocks, fixtures, or migration steps.
Do not invent routes, statuses, defaults, validation, fallback behavior, or internal design.
Keep literals literal when they are part of the contract.
Otherwise prefer abstract wording over incidental sample data.
Merge near-duplicate branches into the smallest complete non-redundant scenario set.

## Skeleton

```gherkin
Feature: <concrete surface or SUT element>

  Rule: <obligation>

    Scenario: <branch or case>
      # <commit>:<relative-file-path>:<line-number>
```

```gherkin
Feature: <concrete surface or SUT element>

  Rule: <obligation>

    Scenario: <branch or case>
      # <commit>:<relative-file-path>:<line-number>
      Given <relevant condition>
      When <action on the surface or SUT>
      Then <observable result>
```
