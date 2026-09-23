---
keywords:
  - ergonomic-architecture
  - checklist
---

# Ergonomic Architecture checklist

- Is `port` used only for an entry point receiving an external signal, with outbound and internal dependencies modeled as resources?
- Are non-trivial operations explicit read-query, pure-calculation-query, and write-command branches, with decisions in calculate branches and costly dependency calls in read or write branches?
- Are output-side humble objects limited to mapping prepared display data?
- Are domain states, variants, and semantic subgroups represented explicitly by types?
- Is every new component interface supported by current requirements, the selected design, or verified production code indicating at least two production implementations, excluding test doubles?
- When a domain specialization fixes generic type arguments, do its code and tests use a domain-named type alias?
