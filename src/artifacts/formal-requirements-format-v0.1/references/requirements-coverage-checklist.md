# Requirements Coverage Checklist

- `Feature` names the concrete endpoint, API surface, component, operation, or other SUT element being described.
- `Rule` expresses exactly one observable obligation or desired behavior property.
- `Scenario` names one materially distinct branch of that `Rule`.
- Relevant inputs, context values, and preconditions that affect behavior are covered.
- Authoritative data sources and decision logic are reflected only through contract-visible behavior.
- Result scope, filtering, selection, ordering, cardinality, and mandatory presence rules are covered.
- Required and forbidden visible properties are covered.
- Explicit state changes and visible side effects are covered.
- Explicit rejection conditions and visible rejection reasons are covered.
- Explicit invariants and representation rules are covered.
- Overlapping rules are merged.
- Material conflicts are treated as a stop, not guessed through.
- Temporary, rollout-bound, migration-bound, or other transition-only notes are excluded unless interim behavior was explicitly requested.
