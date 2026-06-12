# Implementation order

Use this rule when choosing or ordering new behavior cases for implementation.

- Prefer cases that require the smallest new test and production code.
- For a new resource or endpoint, put interface-only cases first: syntax validation, authorization, access control, and missing resource reads.
- Do not make the first case require a full successful create-read-persist path when a validation, access, or missing-resource read case is implied by the same contract.
- Put happy-path reads or writes after interface-only and absent-resource cases.
- Put domain-error and infrastructure-error cases after the happy path unless they are cheaper and explicitly selected.
