# Full Mode Checklist

- `Feature` names the SUT directly.
- `Rule` expresses one material condition set and all required response, persistent state, and outbound-interaction obligations for it.
- `Scenario` checks a representative branch of that condition set.
- All meaningful branch differences are in `Given`.
- `When` describes the action on the SUT.
- `Then` describes observable results.
- No assertion depends on internal implementation instead of contract.
- No precondition is irrelevant to the outcome.
- No assertion is outside the scope of the `Rule`.
- Each negative path states the absence of the required side effect.
- Layout matches `references/layout.md`.
- Wording is short, domain-based, and implementation-light.
- Raw request, response, code, storage, helper, flag, timestamp, and field symbols are absent unless the scenario is about that named contract member or value.
- Entity names, flags, statuses, and errors match the contract.
- A single scenario can be implemented as a test without guessing intended behavior.
