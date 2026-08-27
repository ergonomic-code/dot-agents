# Humanistic API

Use `humanistic-api/v1` to describe JSON-over-HTTP contracts in a compact human-readable form.
Write current-state descriptions in Markdown.
Write before/after descriptions in AsciiDoc by default.
The source blocks are the contract; surrounding headings, change markers, tables, and prose are presentation and are not validated.

## Content

Describe only externally observable facts:
- endpoints with typed path and query parameters;
- relevant request and response headers;
- request bodies and response bodies by status;
- shared models, enums, and named sum types;
- validation, business rules, compatibility notes, and read/write asymmetry.

Do not invent behavior, constraints, statuses, or schemas.
Prefer the narrowest externally valid type.
Use shared definitions instead of repeating large structures.
Use one semantic statement per line.
Write human-readable text in the configured `artifact_language`.

## Source Blocks

Put every endpoint, model, enum, or named sum type in its own `text` source block.
In Markdown, use ```` ```text ```` fences.
In AsciiDoc, use `[source,text]` followed by a `----` delimited block.
See `references/humanistic-api.ebnf` for the source-block grammar.

### Endpoint

Start with `Method <HTTP_METHOD> <PATH_TEMPLATE>`.
Keep query parameters on separate indented lines after a trailing `?`.
Use `>` for the request and `<` for responses.
Do not repeat path or query parameters in the request block.
Add `Headers` and `Body` only when present.
Repeat the response status for every relevant response.
Separate `Headers` and `Body` with an empty line when both are present.
Compress standard non-endpoint-specific errors as `400, 401, 403, 500 // standard error body`.

```text
Method POST /users/{userId=String:UUID}?
  notify={Boolean}

>
  Headers:
    If-Match: String

  Body:
    <UserUpdate>

<
  200
    <User>

  404
    none

Rules:
  - The request is rejected when the user does not exist.
```

For multipart bodies, use:

```text
Method POST /users/{userId=String:UUID}/avatar

>
  Body:
    multipart/form-data
      file: Binary

<
  204
    none
```

### Model And Named Sum Type

Start with `Model <Name> =`.
Use JSON-like fields for a model.
Use `|`-separated variant names for a named sum type.
Include only externally visible fields.
Add a `Rules:` block when the definition owns observable constraints.

```text
Model User =

{
  "id": String:UUID,
  "name": String,
  "manager": <User>?
}
```

```text
Model Result =

  Success |
  Failure
```

### Enum

Start with `Enum <Name> =` and put one value on each following line.
Use a dedicated enum for a reused or source-named closed value set.
Use `Enum<A|B|C>` inline only for a local one-off enum.

```text
Enum UserState =

  ACTIVE
  DISABLED
```

## Type Notation

- Primitive: `String`, `Number`, `Boolean`, `Binary`, `Object`.
- Refined primitive: `String:UUID`, `String:timestamp`, `String:date`, `String:uri`, `Number:int`, `Number:int64`, `Number:double`.
- Collection: `[<Type>]`.
- Nullable: append `?` to the whole type.
- Reference: `<Type>`.
- Inline enum: `Enum<A|B|C>`.
- Inline sum type: `<A|B>`.
- Inline object: `{ "items": [<Type>] }`.

Use `$` only in rules and comments to refer to the whole current request or response body.
Do not attach rules to parameters, fields, or type expressions.
Attach rules to endpoints, models, named sum types, or enums.

## Changes

Use `+`, `*`, and `x` in a presentation gutter for added, changed, and removed fragments.
Mark only the smallest changed endpoint, parameter, field, enum item, model title, status, or rule.
For before/after output, use one AsciiDoc document-level two-column table with `separator=!` and headers `Было` and `Стало`.
Set `:max-width: 95%` once.
Put only `[source,text]` blocks in data cells and use `!` cells so `|` inside source blocks cannot split the table.
The validator ignores change gutters and all content outside source blocks.

## Validation

Run:

```text
python framework_checkout_root/src/artifacts/humanistic-api-v1/scripts/validate_humanistic_api.py <artifact-path>
```

Validation checks source-block delimiters and the canonical syntax inside each API source block.
It does not validate surrounding headings, tables, prose, or change-marker semantics.
