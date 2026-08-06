# Feature naming

Name `Feature` as `<human-readable verified object> (<SUT reference>)`.
Use an evidence-backed SUT reference and do not invent one.
If the SUT reference cannot be resolved, stop and report the missing anchor.
Render component and unit SUT references as `<ClassName>.<methodName>`.
Render HTTP boundary SUT references as `<HTTP method> <path>`.
For other boundaries, use the closest stable contract identifier, such as a command, topic, route, CLI command, or external operation.
Do not append the SUT reference when the exact parenthesized suffix is already present.
Treat the SUT reference as a required anchor, not as an incidental technical detail to abstract away.
