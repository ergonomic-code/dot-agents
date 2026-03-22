# Human-Readable REST API Format

Describe JSON over HTTP APIs in compact human-readable Markdown.
Prefer externally observable behavior over protocol noise.
Use change markers: `+`, `*`, `x`.
Use plain text and Markdown.
Keep one semantic statement per line.
Do not invent behavior or constraints.
Separate protocol facts from comments.
Use `>` for request.
Use `<` for response.
Use `$` only inside generated rules and comments to refer to the whole current request or response body block.
`$` is output notation only.
Do not model `$` as a separate IR type.
Use `<Type>` for model, enum, and named sum-type references.
Use `Enum<A|B|C>` for inline enums.
Use `<A|B>` for inline sum types.
Append `?` to the whole type for nullability.
Use refined primitives when format matters.
Use shared notes only for facts that are genuinely document-level.
Do not use shared notes as a substitute for multiple changed endpoint blocks.
Preferred order: endpoints, definitions, shared notes.

## Endpoint Format

Section title: `## Method <HTTP_METHOD> <PATH_WITHOUT_QUERY_OR_PATH_TYPES>`.
Start with `Method <HTTP_METHOD> <PATH_TEMPLATE>[?]`.
If the endpoint has query parameters, put each query parameter on its own indented line under the path line.
Never keep query parameters on the same line as `Method ... <PATH_TEMPLATE>`.
Append `&` to every query-parameter line except the last.
If spaces, indentation, and line breaks are removed, the signature must collapse back to the one-line URL-like form.
Path and query parameters belong to the endpoint signature.
Do not repeat them in the request block.
Render the whole endpoint block in a fenced code block.
Use the full typed path and query only inside the endpoint block, not in the `##` section title.
If both `Headers` and `Body` are present in the same request or response block, separate them with one blank line.
Use:

```text
Method <HTTP_METHOD> <PATH_TEMPLATE>[?]
    param={Type}[&]
    otherParam={Type}

>
  Headers:
    Header-Name: <Type>
    Header-Name: "const-value"

  Body:
    <body or "none">

<
  <status>
    <body or "none">
```

Add `Headers` only when present.
Repeat per relevant status.
Separate response statuses with a blank line.
Indent the response body under its status.
Keep the same indentation for all statuses in the block.
Compress standard non-endpoint-specific errors as `400, 401, 403, 500 // standard error body`.
After request and response, add only behavior-relevant notes:

```text
Rules:
  - <statement>
```

Use `$` in rules or comments only when it makes the statement shorter and unambiguous.
Example: `- $ is localized according to languageTag.`

For multipart request bodies, use:

```text
  Body:
    multipart/form-data
      partName: <Type>
      file: Binary
```

## Model Format

Start with `Model <Name> =`.
Use:

```text
  Model <Name> =
  
  {
    "fieldName": <Type>, // comment
    "otherField": <Type>?, // comment
  }
```

Include only externally visible fields.
Comment only behavior-relevant details.
Prefer `<Type>` references for reused or large nested structures.
Explicitly note read/write asymmetry when present.
In change descriptions, you may replace a contiguous sequence of unchanged fields with a single `<...>` line in `### Before` and `### After`.
Never omit changed fields.
If the model needs its own behavioral constraints, add a `Rules:` block at the end of the model code block.
Use the same rule syntax as endpoints.

## Sum Type Format

Use a dedicated block when the union has a stable name or is reused.
Render a named sum type as a model-like block.
Use:

```text
  Model <Name> =
  
    VariantA |
    VariantB
```

Use variant names without extra angle brackets inside the alternatives.
Inline one-off unions at the usage site:

```text
  "value": <VariantA|VariantB>
```

A sum-type variant may point to a named model or be inlined.
Prefer named models when variants are reused or non-trivial.
If the sum type needs its own constraints (e.g., discriminator rules), add a `Rules:` block at the end of its code block.

## Enum Format

Start with `Enum <Name> =`.
Add one empty line.
Then use one item per line or `Enum<A|B|C>`.
Use comments only for non-obvious meaning.
If an enum is reused or has a stable source name, give it a dedicated `Enum <Name> =` block and reference it by name at usage sites.
Use inline `Enum<A|B|C>` only for local one-off enums.
If the enum needs its own constraints (e.g., deprecation policy), add a `Rules:` block at the end of the enum code block.

## Type Notation

Primitive: `String`, `Number`, `Boolean`, `Binary`, `Object`.
Refined: `String:UUID`, `String:timestamp`, `String:date`, `String:uri`, `Number:int`, `Number:int64`, `Number:double`.
Containers: `[<Type>]`, `{ "items": [<Type>] }`.
Nullable: `String?`, `<Type>?`, `[<Type>]?`, `<A|B>?`.
Reference: `<Type>`.
Enum: `Enum<A|B|C>`.
Named enum reference: `<EnumName>`.
Inline sum: `<A|B>`, `<VariantA|VariantB>`.
Named sum-type reference: `<TypeName>`.
Do not attach rules to parameters, fields, or type expressions.
Attach rules to endpoints, models, sum types, or enums.

## Change Notation

Mark only changed fragments.
Use `+` for added, `*` for changed, and `x` for removed.
Place the marker before the changed endpoint, field, enum item, model title line, status, or rule.
For path and query parameters, place the marker before the whole parameter.
If one parameter changed inside a longer path or query signature, mark that parameter inline.
Do not mark the whole endpoint signature or the whole query string for a single-parameter change.
If the whole model, enum, or sum type is added or removed, mark its title line.

## Compression Rules

Prefer one endpoint block per endpoint, one model block per shared structure, one changed endpoint section per changed endpoint, short comments, shared models instead of repeated large inline bodies, and named sum types instead of repeating the same union in multiple places.
Avoid duplicating the same structure inline and separately, duplicating the same enum inline and as a named enum block, collapsing multiple endpoints into one shared-notes section, repeating standard errors in full, and comments that restate obvious type information.
