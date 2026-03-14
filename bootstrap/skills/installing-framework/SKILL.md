---
name: installing-framework
description: Install the Ergocode AI Agent Framework into a repository. Use when Codex must install the runtime payload under `framework_checkout_root/src`, ensure `AGENTS.md` contains the Ergocode framework section, and ensure `skills_symlink_path` points to `framework_checkout_root/src/skills`. Keep installation idempotent and patch existing `AGENTS.md` minimally.
---

# Core specification

Purpose: install the Ergocode framework runtime payload into the target repository.

Inputs:
- `repo_root`
- `framework_checkout_root`
- `agents_md_path`
- `skills_symlink_path`

Defaults:
- `repo_root=.`
- `framework_checkout_root=./.agents/ergo`
- `agents_md_path=./AGENTS.md`
- `skills_symlink_path=./.agents/skills/ergo`

Checks:
- resolve all paths from `repo_root`
- require `framework_checkout_root/src/project-baseline.md`
- require `framework_checkout_root/src/skills` as the intended symlink target
- installation must be idempotent

Effects:
- ensure `framework_checkout_root` exists
- ensure `framework_checkout_root/src` exists and contains the runtime payload files
- ensure `framework_checkout_root/src/project-baseline.md`
- ensure `agents_md_path`
- ensure `skills_symlink_path` is a symlink to `framework_checkout_root/src/skills`

Contract:
- the whole framework repository may be checked out, copied, or symlinked into `framework_checkout_root`
- only `framework_checkout_root/src` is runtime-visible after installation
- the installer itself must live outside `framework_checkout_root/src`
- preferred default: add the framework repository as a git submodule at `framework_checkout_root`

Recommended layout:
- checkout root: `./.agents/ergo`
- runtime payload: `./.agents/ergo/src`

AGENTS.md patch algorithm:
- if `AGENTS.md` is missing
  - create it from `assets/AGENTS.md.template`
  - materialize `<framework-checkout-root>` in the template with `framework_checkout_root`
  - the generated framework section must reference only `framework_checkout_root/src` paths
- else
  - detect a `## Framework` section that clearly refers to Ergocode or the resolved `framework_checkout_root`
  - if more than one matching section exists, fail
  - if one matching section exists, replace only that section with the current framework section
  - else append the framework section to the end of `AGENTS.md`
  - never duplicate the framework section

Symlink algorithm:
- ensure parent directories for `skills_symlink_path`
- if `skills_symlink_path` is a symlink to `framework_checkout_root/src/skills`, leave it unchanged
- if `skills_symlink_path` is a symlink to another target, replace it
- if `skills_symlink_path` is a regular file or directory, fail

Failure conditions:
- multiple matching framework sections exist in `AGENTS.md`
- `skills_symlink_path` exists as a regular file
- `skills_symlink_path` exists as a directory
- `AGENTS.md` cannot be patched without changing content outside the detected framework section

Final report:
- `framework_checkout_root`
- `agents_md`
- `skills_symlink`
- `warnings`
- `errors`

Framework section match: a `## Framework` section that mentions `Ergocode` or the resolved `framework_checkout_root`.

Minimal patch rule: keep surrounding spacing and content unless replacement requires a local normalization.
