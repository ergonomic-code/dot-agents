from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_init_task_workdir_creates_work_state_from_standard_template():
    skill = (
        ROOT / "src" / "task-workdir" / "skills" / "init-task-workdir" / "SKILL.md"
    ).read_text(encoding="utf-8")
    template = (
        ROOT / "src" / "task-workdir" / "references" / "work-state-template.md"
    ).read_text(encoding="utf-8")

    assert "references/work-state-template.md" in skill
    assert "`work-state.md`" in skill
    assert template.startswith("# Work state\n")
    assert "## Current objective\n" in template
    assert "## Verification\n" in template
