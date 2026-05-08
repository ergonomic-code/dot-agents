# Requirements Coverage Checklist

- `SUT` names the concrete endpoint, API surface, component, operation, or other object under verification.
- `Check` states one contract-visible required property.
- `Variant` lines cover only materially distinct input or context classes for the same `Check`.
- Check sets cover the smallest useful semantic classes that would expose plausible one-case, hard-coded, or overfit implementations.
- Relevant inputs, context values, and preconditions that affect behavior are covered.
- Authoritative data sources and decision logic are reflected only through contract-visible behavior.
- Result scope, filtering, selection, ordering, cardinality, and mandatory presence rules are covered.
- Required and forbidden visible properties are covered.
- Explicit state changes and visible side effects are covered.
- Explicit rejection conditions and visible rejection reasons are covered.
- Explicit invariants and representation rules are covered.
- Overlapping checks are merged.
- Material conflicts are treated as a stop, not guessed through.
- Temporary, rollout-bound, migration-bound, or other transition-only notes are excluded unless interim behavior was explicitly requested.
- Layout matches `references/layout.md`.
