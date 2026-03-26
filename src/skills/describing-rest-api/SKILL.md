---
name: describing-rest-api
description: Build REST API IR JSON for JSON over HTTP from code, OpenAPI, curl, natural-language requirements, JSON Schema, or mixed inputs, then validate it and render Markdown.
---

# Describing REST API

Write files in the working directory.
Use `./tmp` when no path is given.
Create `./tmp` if missing.
Use `./tmp/rest-api-ir.json` for IR.
Use `./tmp/rest-api.md` for Markdown.
Use `references/rest-api-ir-schema.json`, `scripts/validate_json.py`, and `scripts/render_rest_api.py`.

## Hard Gate

Always generate IR at `./tmp/rest-api-ir.json`, even when the user asks only for Markdown.
Always validate IR by running `python scripts/validate_json.py references/rest-api-ir-schema.json ./tmp/rest-api-ir.json`.
If validation fails, fix IR and rerun validation until it passes.
Do not render Markdown before validation passes.

## Workflow

1. Build REST API IR JSON matching `references/rest-api-ir-schema.json`.
2. Validate it with `python scripts/validate_json.py references/rest-api-ir-schema.json ./tmp/rest-api-ir.json`.
3. Render Markdown from the validated IR with `python scripts/render_rest_api.py ./tmp/rest-api-ir.json > ./tmp/rest-api.md`.

## Contract Scope

Describe the final externally observable HTTP contract.
For commit ranges or commit lists, describe the net change from before the earliest relevant change to after the latest relevant change.
Treat commits as evidence only.
Do not narrate commit history.
Do not emit per-commit summaries unless requested.

## IR Rules

Accept code, OpenAPI, curl, natural-language requirements, JSON Schema, or mixed inputs.
Resolve conflicts by priority: user instruction, code, JSON Schema, OpenAPI, curl, natural language.
Use code names for models, enums, and named sum types when available.
Do not invent behavior, constraints, statuses, or schemas.

Extract only externally visible facts:
- endpoints;
- typed path and query parameters;
- relevant headers;
- request body;
- response bodies by status;
- error reasons in `response.description`;
- shared models, enums, and named sum types;
- nullability, formats, validation, business rules, compatibility notes, read or write asymmetry, and expressed changes.

Report only observable contract changes.
Omit internal refactors, code moves, DTO renames without wire change, annotation churn without wire effect, persistence or service changes without wire effect, unchanged items, and duplicates.
Collapse multiple commits into one final observable change.
Collapse rename plus reshape into one API evolution when it is the same endpoint or model role.
If a commit does not affect the wire contract, omit it.

Use the narrowest externally valid type.
Use enums for closed value sets.
Use `Enum<A|B|C>` for one-off local enums.
Use named enums only when reused or source-named.
Default values and examples do not weaken enum constraints.
For constant headers, use `header.value`.
For multipart bodies, use `body.kind = "multipart"` with `parts`.
Do not move expressible constraints into comments.

Ignore wiring, framework boilerplate, internals, and non-serialized models.
Use `change` only when the input expresses change.
Mark the smallest changed node.
Do not mark unchanged context.

Build diffs in this order:
1. derive before-state wire contract;
2. derive after-state wire contract;
3. compute observable diff only;
4. encode the minimal IR for that diff.

## Rules And Comments

Encode client-observable validation and runtime behavior as explicit `rules` on the smallest reusable owner.
Use endpoint rules for request acceptance or rejection, response status behavior, endpoint-scoped business checks, and request-body semantics tied to one endpoint slot.
Use model rules for reusable or cross-field constraints of a named request or response shape.
Use sum-type or enum rules only when the behavior belongs to that sum type or enum.
Do not put `rules` on parameters, fields, or type expressions.
Do not hide reusable behavior only in comments.
Do not encode commit history or implementation history as rules.
Make each rule atomic, declarative, and client-observable.
If evidence gives rejection reasons, accepted-value rules, or status-triggering conditions, materialize them as explicit rules even if also mentioned in descriptions or comments.
For changed endpoints and models, prefer rules over descriptive comments whenever the behavior is observable.

Use comments only for local, checkable semantics or for a short pointer to an explicit rule on the same owner.
Do not use comments as the only carrier of validation, business, cross-field, reusable, or endpoint-wide behavior.
Do not put hidden behavior into comments.

## Marked Mode

In `marked` mode, every top-level reusable block that exists only after the change must have `change: "added"`.
Apply this transitively across top-level refs.
If after-only content reaches a new top-level `model`, `enum`, or named `sumType`, mark it as added.

When `changeMode = "marked"` and `request.body` or `responses[].body` is a ref type, include `body.type.refId`.
Treat `type.ref` as display name and `type.refId` as stable identity.
When a model is renamed, keep `model.id` and `type.refId` stable across before and after.
Update `type.ref` per side through `diff.before` and `diff.after`.

For stable-ref checks, endpoint identity is `(<method>, <path>)` after stripping query strings and replacing every `{...}` path segment with `{}`.

When one endpoint slot before and after points to DTOs serving the same API role, and the task is to describe change rather than replacement, represent them as one changed model with stable identity.
Endpoint slot means `(endpoint key, request)` or `(endpoint key, response <status>)`.
Use this even if the class name changed, fields changed, or annotations changed without wire effect.

For rename plus reshape:
- keep one stable `model.id`;
- keep one stable endpoint `body.type.refId`;
- use the after-name as current `name`;
- put the previous name into `diff.before.name`;
- keep removed fields only in `diff.before.fields`;
- keep added and current fields in `fields`;
- do not split into removed model plus added model unless evidence says these are different API entities.

Derive before and after independently from side-local evidence.
Stable identity does not justify copying fields across sides.
For `diff.before`, include only fields evidenced on the before side of the same endpoint slot.
Do not copy after-only fields into `diff.before`.
Do not infer before fields from the after model name, current `fields`, shared `model.id`, or intermediate commits.
For current `fields`, include only after-side evidence.
Do not keep before-only fields unless they still exist after.
Treat each side as closed-world.
If evidence is absent, the field is absent.
If evidence is ambiguous, omit the field.
Rename plus reshape preserves endpoint-role identity, not field membership.

## Before Finishing

Verify:
- every endpoint has method and path;
- every referenced model, enum, and named sum type is defined or intentionally external;
- nullability is explicit where relevant;
- enums and sum types are normalized and deduplicated;
- unchanged details are omitted unless needed as context;
- IR JSON has no duplicate object keys, including inside `diff`;
- every observable reusable rule is attached to an endpoint, model, sum type, or enum;
- comments either point to such a rule or state a local checkable fact;
- no response description or comment is the only carrier of endpoint-wide or model-wide behavior;
- `diff.before.fields` contains no after-only field;
- current `fields` contains no before-only field;
- the IR passes `validate_json.py`.

## Output

Output only the requested API description, IR, or files.
Do not add unchanged details.
Do not add commit-by-commit explanations unless requested.
Do not add explanations outside the target artifact unless requested.
Write all human-readable parts of the output (Markdown descriptions, comments and notes) in the configured `artifact_language` (see `project-baseline.md`).
