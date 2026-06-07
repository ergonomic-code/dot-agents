# Full Mode Checklist

- `SUT` names the object under verification directly.
- `Check` expresses one required observable property in the artifact-language obligation form.
- `Variant` is absent or names one semantic input or context class for that `Check`.
- All meaningful check differences are in `Given` or `Variant`.
- `When` describes the action on the SUT.
- Composite flows split sequential actions across `When` and following `And`.
- `Then` describes observable results.
- No assertion depends on internal implementation instead of contract.
- No precondition is irrelevant to the outcome.
- No assertion is outside the scope of the `Check`.
- No positive result is paired with a mirrored absence assertion unless the absence is a distinct contract obligation.
- Each negative path states the absence of the required side effect.
- Layout matches `references/layout.md`.
- Wording is short, domain-based, and implementation-light.
- Raw request, response, code, storage, helper, flag, timestamp, and field symbols are absent unless the check is about that named contract member or value.
- Check and step wording has no avoidable endpoint, parameter, field, DTO, payload, or response-model names.
- Entity names, flags, statuses, and errors match the contract.
- A single check block can be implemented as a test without guessing intended behavior.
