from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_runtime_has_no_role_layer():
    assert not (ROOT / "src" / "roles.md").exists()
    assert not (ROOT / "src" / "roles").exists()
    assert not (ROOT / ".agents" / "roles").exists()


def test_session_start_loads_only_the_baseline():
    script = (ROOT / "bootstrap" / "hooks" / "session_start_load_project_baseline.py").read_text(
        encoding="utf-8"
    )

    assert 'FRAMEWORK_SRC_RELATIVE_FILES = [\n    "project-baseline.md",\n]' in script
    assert '"roles.md"' not in script


def test_architecture_entry_points_do_not_restore_role_indirection():
    paths = [
        ROOT / "src" / "project-baseline.md",
        ROOT / "src" / "references" / "context-layering.md",
        ROOT / "src" / "task-workdir" / "context.md",
        ROOT / "src" / "skills" / "fix-framework-context" / "SKILL.md",
        ROOT / "src" / "skills" / "fix-project-context" / "SKILL.md",
        ROOT / "bootstrap" / "skills" / "installing-framework" / "assets" / "AGENTS.md.template",
        ROOT / "README.md",
    ]
    forbidden = (
        "selected role",
        "active role",
        "roles.md",
        "src/roles",
        "roles/",
        "разделение на роли",
    )

    for path in paths:
        text = path.read_text(encoding="utf-8").lower()
        for phrase in forbidden:
            assert phrase not in text, f"{phrase!r} remains in {path.relative_to(ROOT)}"
