# Response Contract Guard

Use when the selected example is an HTTP success path and the task changes endpoint, response shape, or resource representation.

- Before adding the case, use the `030-api-new.adoc` or `030-api-new-ir.json` as the target endpoint and response shape when present; otherwise use the controller contract.
- Bind changed typed `*HttpApi` success methods to that target shape before writing assertions.
- Do not reuse an old-version helper, route, DTO, or schema until it matches the target contract.
- If no production contract type exists yet, add only the compile-time contract surface needed by the selected case.
- Assert at least one changed response property that would fail on the old shape.
- Do not treat status-only success, pagination-only success, or old DTO decoding as proof of the changed response contract.
- Use raw JSON only for transport/member absence that cannot be represented by a typed contract shape.
