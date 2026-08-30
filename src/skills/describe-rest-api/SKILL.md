---
name: describe-rest-api
description: Write and validate a humanistic-api/v1 description of a JSON-over-HTTP contract from code, OpenAPI, curl, natural-language requirements, JSON Schema, or mixed inputs.
---

# Describing REST API

Read `../../artifacts/humanistic-api-v1/ARTIFACT.md` before writing the artifact.

## Inputs and destination

- Accept code, OpenAPI, curl, requirements, JSON Schema, or mixed contract evidence.
- Accept an explicit output path and optional existing API artifact.
- If no output path is supplied, ask for one before repository-backed generation or return the artifact inline for standalone generation.
- Use Markdown for a current-state description and AsciiDoc for a target change or before/after description unless the caller selects a format.

When writing to a supplied output path, create its parent directory if missing.
Write the final `humanistic-api/v1` artifact directly.
Do not create an intermediate representation or a parallel machine-readable artifact.

## Hard Gate

Validate the final artifact by running:

```text
python framework_checkout_root/src/artifacts/humanistic-api-v1/scripts/validate_humanistic_api.py <artifact-path>
```

If validation fails, fix the artifact and rerun validation until it passes.

## Workflow

1. Resolve the output format and use the caller-supplied target path when writing.
2. Derive the externally observable contract from the available evidence.
3. For a change, derive before and after independently and compute only the observable difference.
4. Write the final artifact directly in `humanistic-api/v1`.
5. Validate the final artifact.

## Contract Scope

Describe the final externally observable HTTP contract.
For commit ranges or commit lists, describe the net change from before the earliest relevant change to after the latest relevant change.
Treat commits as evidence only.
Do not narrate commit history or emit per-commit summaries unless requested.

Accept code, OpenAPI, curl, natural-language requirements, JSON Schema, or mixed inputs.
Resolve conflicts by priority: user instruction, code, JSON Schema, OpenAPI, curl, natural language.
Use code names for models, enums, and named sum types when available.
Do not invent behavior, constraints, statuses, or schemas.

Extract only externally visible facts.
Omit internal refactors, code moves, DTO renames without wire change, annotation churn without wire effect, persistence or service changes without wire effect, unchanged items, and duplicates.
Collapse multiple commits into one final observable change.
Collapse rename plus reshape into one API evolution when it is the same endpoint or model role.
If a commit does not affect the wire contract, omit it.

Use the narrowest externally valid type.
Use enums for closed value sets.
Use `Enum<A|B|C>` for one-off local enums.
Use named enums only when reused or source-named.
Default values and examples do not weaken enum constraints.
For multipart bodies, use the artifact's multipart form.
Do not move expressible constraints into comments.

Ignore wiring, framework boilerplate, internals, and non-serialized models.
Mark the smallest changed fragment.
Do not mark unchanged context.

## Rules And Comments

Encode client-observable validation and runtime behavior as explicit rules on the smallest reusable owner.
Use endpoint rules for request acceptance or rejection, response status behavior, endpoint-scoped business checks, and request-body semantics tied to one endpoint slot.
Use model rules for reusable or cross-field constraints of a named request or response shape.
Use sum-type or enum rules only when the behavior belongs to that sum type or enum.
Do not put rules on parameters, fields, or type expressions.
Make each rule atomic, declarative, and client-observable.

Use comments only for local, checkable semantics or for a short pointer to an explicit rule on the same owner.
Do not use comments as the only carrier of validation, business, cross-field, reusable, or endpoint-wide behavior.

## Changes

Build changes in this order:
1. derive the before-state wire contract;
2. derive the after-state wire contract;
3. compute the observable difference;
4. write only the difference and the context needed to understand it.

When one endpoint slot before and after points to DTOs serving the same API role, treat them as one changed model even if the class name or fields changed.
Endpoint slot means the request or one response status of the same method and normalized path.
Derive both sides from side-local evidence.
Do not copy after-only fields into the before side or keep before-only fields in the after side.
If evidence is ambiguous, omit the field.
Rename plus reshape preserves endpoint-role identity, not field membership.

For a before/after description, use AsciiDoc by default and follow the artifact's document-level paired-table convention.

## Before Finishing

Verify:
- every endpoint has a method and path;
- every referenced model, enum, and named sum type is defined or intentionally external;
- nullability is explicit where relevant;
- enums and sum types are normalized and deduplicated;
- unchanged details are omitted unless needed as context;
- every observable reusable rule belongs to an endpoint, model, sum type, or enum;
- comments either point to such a rule or state a local checkable fact;
- the final artifact passes `validate_humanistic_api.py`.

## Output

Output only the requested API description or files.
Do not add unchanged details, commit-by-commit explanations, or explanations outside the target artifact unless requested.
Write all human-readable parts in the configured `artifact_language`.
