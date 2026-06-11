# Feature artifact phases

Use this rule for phase-coded artifacts inside a feature workdir.

- Artifact phase codes are independent from implementation stages.
- Artifact phase code is the numeric file name prefix such as `010`, `020`, or `030`.
- Implementation stage code is the two-digit code used in `stage-<stage-code>` and `<feature-code>/<stage-code>`.
- Resolve artifact phase from the skill binding, artifact purpose, or explicit output path, not from the implementation stage.
- Use the artifact phase code as the file name prefix unless the user gave an explicit path.
- In staged layout, keep the same phase-coded artifact names inside `stage-<stage-code>/`, for example `stage-01/020-api-current.md` or `stage-01/030-api-new.adoc`.

## Standard artifact phases

- `010` means requirements preparation.
- Standard `010` artifacts are `010-feature-brief.md` and other `010-*` requirement files.
- `020` means current code analysis.
- Standard `020` artifacts are `020-api-current.md`, `020-test-cases-current.md`, `020-sut-acceptance-criteria-current.adoc`, `020-model-current.md`, `020-persistence-current.md`, and `020-schema.md`.
- `030` means implementation design.
- Standard `030` artifacts are `030-api-new.adoc`, `030-test-cases-new.adoc`, `030-model-new.md`, `030-persistence-new.md`, and `030-schema.md`.
- If more than one artifact phase is plausible, use the earliest phase that still matches the artifact purpose.
