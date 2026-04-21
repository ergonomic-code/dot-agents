# Full Mode Checklist

- `Feature` names the SUT directly.
- `Rule` expresses exactly one observable behavior property.
- `Scenario` checks that property and not another one.
- All meaningful branch differences are in `Given`.
- `When` describes the action on the SUT.
- `Then` describes observable results.
- No assertion depends on internal implementation instead of contract.
- No precondition is irrelevant to the outcome.
- No assertion is outside the scope of the `Rule`.
- Each negative path states the absence of the required side effect.
- Wording is short, domain-based, and implementation-light.
- Entity names, flags, statuses, and errors match the contract.
- A single scenario can be implemented as a test without guessing intended behavior.
