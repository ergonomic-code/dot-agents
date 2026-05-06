# Output Layout

Use `framework_checkout_root/src/conventions/feature-stage-skill.md` for explicit-path handling, feature-dir binding, and write-before-sync order.
This file binds only the chart-specific output container, stage-code use, and bundle layout.

- default feature-dir output container: `<active-feature-dir>/020-structure-charts`
- non-feature default output container: `./tmp/structure-charts`
- When the shared lifecycle keeps an explicit output directory, use it as the chart root directory.
- Create the default chart root directory if it does not exist.
- Use the feature stage code as the file name prefix.
- Use stage `020` for requirements-to-production-code mapping and other current-state analysis artifacts.
- Use stage `030` when the chart belongs to optional preliminary-refactoring review or follow-up fixes after that analysis.
- Use stage `050` when the chart belongs to implementation design.
- If the user gave an explicit stage, keep it.
- If chart output uses a directory layout, write each chart into its own bundle directory.
- For an HTTP entry point, name the bundle directory as `<slug>`, where `<slug>` is `<lowercase-method>-<kebab-case-path>`.
- Derive `<kebab-case-path>` from the normalized HTTP path by stripping leading and trailing `/`, replacing path separators, placeholders, and other non-alphanumeric separators with `-`, lowercasing, collapsing repeated `-`, and using `root` for `/`.
- For a non-HTTP entry point without an explicit output file path, name the bundle directory as `<slug>`, where `<slug>` is a stable kebab-case slug derived from the selected root symbol.
- Inside a bundle directory, write `<slug>.yaml` and `<slug>.mmd`.
- If an explicit output file path is used, keep that file path and place the paired artifact next to it with the same basename and the other extension.
- If multiple charts are needed, create one bundle directory per selected entry point under the chart root directory.
