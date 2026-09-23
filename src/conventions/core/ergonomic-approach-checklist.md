---
keywords:
  - ergonomic-approach
  - checklist
---

# Ergonomic Approach checklist

- Does each implementation-code change serve required behavior rather than only making tests pass?
- Is each responsibility implemented once, with complete shared behavior centralized except for local test setup or assertions that improve readability?
- Does one method control acquisition and one cleanup path for each resource unless ownership is explicitly transferred?
- Are values whose meaning, unit, range, or nullability is narrower than their primitive type represented by semantic types, or made explicit at required primitive boundaries?
- Покрыт ли каждый normal и realistically reachable path изменённой или добавленной operation и computation хотя бы одним test case, исключая unexpected и practically impossible failures?
- Предпочитает ли test selection unit test без infrastructure или I/O, иначе boundary test, и component test только при существенном уменьшении размера, времени или для standard test infrastructure?
