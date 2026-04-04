---
name: installing-framework
description: Install the Ergocode AI Agent Framework into a repository. Use when Codex must install the runtime payload under `framework_checkout_root/src`, ensure `AGENTS.md` contains the Ergocode framework section, ensure `skills_symlink_path` points to `framework_checkout_root/src/skills`, and install Codex session hooks. Keep installation idempotent and patch existing `AGENTS.md` minimally.
---

# Core specification

Purpose: install the Ergocode framework runtime payload into the target repository.

Inputs:
- `repo_root`
- `framework_checkout_root`
- `agents_md_path`
- `skills_symlink_path`
- `framework_config_path` (optional)
- `codex_hooks_path` (optional)
- `codex_session_start_hook_script_path` (optional)

Defaults:
- `repo_root=.`
- `framework_checkout_root=./.agents/ergo`
- `agents_md_path=./AGENTS.md`
- `skills_symlink_path=./.agents/skills/ergo`
- `codex_hooks_path=./.codex/hooks.json`
- `codex_session_start_hook_script_path=./.codex/session_start_load_project_baseline.py`

Checks:
- resolve all paths from `repo_root`
- require `framework_checkout_root/src/project-baseline.md`
- require `framework_checkout_root/src/skills` as the intended symlink target
- require installer template `bootstrap/ergo-config.yaml.template`
- require installer template `bootstrap/hooks/hooks.json`
- require installer template `bootstrap/hooks/session_start_load_project_baseline.py`
- installation must be idempotent
- if `framework_config_path` is not provided, ask the user to either:
  - provide it explicitly (suggest `<framework_checkout_root>/../ergo-config.yaml`, i.e. `<framework-root>../ergo-config.yaml`, relative to `repo_root`), or
  - explicitly refuse installing the framework config
- if `framework_config_path` resolves outside `repo_root`, ask for explicit confirmation before writing files
- if `codex_hooks_path` resolves outside `repo_root`, ask for explicit confirmation before writing files
- if `codex_session_start_hook_script_path` resolves outside `repo_root`, ask for explicit confirmation before writing files

Effects:
- ensure `framework_checkout_root` exists
- ensure `framework_checkout_root/src` exists and contains the runtime payload files
- ensure `framework_checkout_root/src/project-baseline.md`
- ensure `agents_md_path`
- ensure `skills_symlink_path` is a symlink to `framework_checkout_root/src/skills`
- ensure `.codex/` directory exists at `repo_root/.codex`
- ensure `codex_session_start_hook_script_path`
- ensure `codex_hooks_path` contains the mandatory framework SessionStart hook
- if `framework_config_path` is provided (the `<framework-root>../` location is preferred) and the file does not exist, create it by copying the installer template `bootstrap/ergo-config.yaml.template` to the resolved `framework_config_path` relative to `repo_root`
  This file defines the default `artifact_language: ru`.
- if the user refuses installing the framework config, do not create any config file

Contract:
- the whole framework repository may be checked out, copied, or symlinked into `framework_checkout_root`
- only `framework_checkout_root/src` is runtime-visible after installation
- the installer itself must live outside `framework_checkout_root/src`
- the installer must install and maintain the framework Codex `SessionStart` hook as the runtime entrypoint
- preferred default: add the framework repository as a git submodule at `framework_checkout_root`

Recommended layout:
- checkout root: `./.agents/ergo`
- runtime payload: `./.agents/ergo/src`

AGENTS.md patch algorithm:
- if `AGENTS.md` is missing
  - create it from `assets/AGENTS.md.template`
  - materialize `<framework-checkout-root>` in the template with `framework_checkout_root`
  - if `framework_config_path` is provided, materialize `<framework-config-path>` in the template with `framework_config_path`
  - if the user refuses installing the framework config, remove the "Framework config path:" line from the template output
  - the generated framework section must reference only `framework_checkout_root/src` paths
- else
  - detect a `## Framework` section that clearly refers to Ergocode or the resolved `framework_checkout_root`
  - if more than one matching section exists, fail
  - the replacement framework section must include the "Framework config path:" line only if `framework_config_path` is provided
  - if one matching section exists, replace only that section with the current framework section
  - else append the framework section to the end of `AGENTS.md`
  - never duplicate the framework section

Symlink algorithm:
- ensure parent directories for `skills_symlink_path`
- if `skills_symlink_path` is a symlink to `framework_checkout_root/src/skills`, leave it unchanged
- if `skills_symlink_path` is a symlink to another target, replace it
- if `skills_symlink_path` is a regular file or directory, fail

Codex hooks algorithm:
- resolve `codex_hooks_path` and `codex_session_start_hook_script_path` from `repo_root`
- copy installer template `bootstrap/hooks/session_start_load_project_baseline.py` to `codex_session_start_hook_script_path` if missing
- if the script exists and differs from the template, overwrite it only if the user confirms
- if the script exists and differs from the template and the user refuses overwrite, fail installation
- compute `codex_session_start_hook_script_path` relative to `repo_root` as `<script_rel>`
- ensure `codex_hooks_path` is valid JSON if it exists
- ensure `codex_hooks_path` contains the mandatory SessionStart hook with:
  - `matcher: "startup"`
  - command:
    - always include `--agents-md-path "<agents_md_path>"`
    - without `framework_config_path`: `python3 "$(git rev-parse --show-toplevel)/<script_rel>" --agents-md-path "<agents_md_path>"`
    - with `framework_config_path`: `python3 "$(git rev-parse --show-toplevel)/<script_rel>" --agents-md-path "<agents_md_path>" --framework-config-path "<framework_config_path>"`
- if `codex_hooks_path` is missing, write installer template `bootstrap/hooks/hooks.json` with the command patched to the computed `<script_rel>`, `--agents-md-path "<agents_md_path>"`, and the optional `--framework-config-path "<framework_config_path>"`
- if `codex_hooks_path` exists, merge the hook in-place and keep unrelated hooks unchanged

Failure conditions:
- multiple matching framework sections exist in `AGENTS.md`
- `skills_symlink_path` exists as a regular file
- `skills_symlink_path` exists as a directory
- `AGENTS.md` cannot be patched without changing content outside the detected framework section
- `codex_hooks_path` exists but is not valid JSON
- `codex_session_start_hook_script_path` exists as a directory
- existing `codex_session_start_hook_script_path` differs from the template and overwrite is refused

Final report:
- `framework_checkout_root`
- `agents_md`
- `skills_symlink`
- `codex_hooks`
- `warnings`
- `errors`

Framework section match: a `## Framework` section that mentions `Ergocode` or the resolved `framework_checkout_root`.

Minimal patch rule: keep surrounding spacing and content unless replacement requires a local normalization.
