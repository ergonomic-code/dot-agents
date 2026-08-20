# Feature naming

Name `Feature` as `<human-readable verified object> (<SUT reference>)`.
Use an evidence-backed SUT reference and do not invent one.
For an explicitly planned new SUT whose technical reference has not been designed yet, temporarily omit the parenthesized SUT reference.
Keep the human-readable verified object unambiguous, do not render a placeholder, and report `$align-required-design` as required before test coding.
Treat this provisional form as valid for behavior design only.
Materialize its evidence-backed SUT reference through `$align-required-design` before test coding.
If neither a SUT reference nor an explicitly planned new SUT can be resolved, stop and report the missing anchor.
Render component and unit SUT references as `<ClassName>.<methodName>`.
Render HTTP boundary SUT references as `<HTTP method> <path>`.
For other boundaries, use the closest stable contract identifier, such as a command, topic, route, CLI command, or external operation.
Do not append the SUT reference when the exact parenthesized suffix is already present.
Treat the materialized SUT reference as a required coding anchor, not as an incidental technical detail to abstract away.
