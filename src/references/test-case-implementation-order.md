# Implementation order

Use this rule when choosing or ordering new behavior cases for implementation.

- Express a configurable quantitative boundary by its behavioral relation.
  Configure the SUT with the smallest test value that preserves that relation instead of materializing production-scale data.
  Use the production value only when that exact value is itself required behavior or the boundary cannot be configured for the test.
- Among unimplemented happy paths, first choose a contract-valid degenerate case that spans the system's external input boundary and final observable effect with the least production behavior.
  - Prefer the case requiring the fewest rules, data sources, state transitions, and branches.
  - A constant implementation is sufficient when its result is correct for the whole selected behavior class, not only the test fixture.
  - Determine completeness from the selected behavior, not paths or effects required only by later cases.
  - Do not substitute a narrower internal entry point or simulated lower-layer result for the external vertical slice.
- If no contract-valid degenerate case exists, choose the narrowest complete happy-path vertical slice.
- Extend the working vertical slice in subsequent increments by one obligation or one behavior axis at a time.
- Implement interface-only, validation, authorization, access-control, missing-resource, domain-error, infrastructure-error, and other extensions after the first happy path.
- Order subsequent increments from the briefs, behavioral necessity, and change size.
- Do not combine independent variants, except for one complete parameterized set allowed by the test-case rules.
