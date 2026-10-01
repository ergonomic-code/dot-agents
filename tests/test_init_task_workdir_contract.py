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
    lines = [line for line in template.splitlines() if line.strip()]
    assert lines[0].startswith("# ")
    assert len(lines[1:]) == 7
    assert all(line.startswith("## ") for line in lines[1:])
    assert len(set(lines[1:])) == 7


def test_implementation_design_template_is_connected_to_creation_and_updates():
    task_workdir = ROOT / "src" / "task-workdir"
    template_path = task_workdir / "references" / "implementation-design-template.md"
    template = template_path.read_text(encoding="utf-8")
    context = (task_workdir / "context.md").read_text(encoding="utf-8")

    assert "references/implementation-design-template.md" in context
    assert "030-implementation-design.md" in context
    assert template.splitlines()[0].startswith("# ")
    sections = [line for line in template.splitlines() if line.startswith("## ")]
    assert len(sections) == len(set(sections)) == 5
