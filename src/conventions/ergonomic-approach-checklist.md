# Ergonomic Approach checklist

## General

- Does every implementation-code change serve required behavior rather than only making tests pass?
- Is there any duplication in the code beyond acceptable repetition of setup and assertions between test cases?
- Are non-trivial operations shaped as explicit read-query, I/O-free pure-calculation-query, and write-command branches?
- Are complex decisions kept in calculate branches and costly external dependency calls kept in read or write branches?
- Are write-side humble objects limited to mapping already prepared result or display data into the target format?
- Are values whose meaning, unit, range, or nullability is narrower than their primitive type represented by semantic types, or made explicit at required primitive boundaries?
- Are domain states, variants, or semantic subgroups represented by explicit types instead of correlated nullable fields?

## Tests

- For each changed or added operation and computation, is each normal and realistically reachable path covered by at least one test case, excluding paths that exist only to handle unexpected and practically impossible failures?
- Does the proposed or implemented test set avoid component tests that duplicate behavior reasonably verifiable by boundary tests?
