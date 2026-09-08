import importlib.util
from pathlib import Path
import sys


TASK_WORKDIR = Path(__file__).parents[1] / "src" / "task-workdir"
WORK_STATE_TEMPLATE = TASK_WORKDIR / "references" / "work-state-template.md"
sys.path.insert(0, str(TASK_WORKDIR))
SPEC = importlib.util.spec_from_file_location(
    "load_task_context", TASK_WORKDIR / "load_task_context.py"
)
assert SPEC and SPEC.loader
loader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(loader)


def make_task(repo: Path, name: str, brief: str = "Task brief body\n") -> Path:
    task = repo / "devlog" / name
    task.mkdir(parents=True)
    (task / "010-task-brief.md").write_text(brief, encoding="utf-8")
    return task


def write_rules(tmp_path: Path, content: str = "Task-workdir rule body\n") -> Path:
    context = tmp_path / "context.md"
    context.write_text(content, encoding="utf-8")
    return context


def test_no_resolved_task(tmp_path):
    output = loader.load_task_context(
        "request", tmp_path, lambda _prompt, _root: None, write_rules(tmp_path)
    )

    assert output == loader.NO_TASK_CONTEXT


def test_resolved_task_emits_complete_context(tmp_path):
    task = make_task(tmp_path, "123-example", "Complete task brief\n")
    context = write_rules(tmp_path, "Complete task-workdir rules\n")

    output = loader.load_task_context(
        "request", tmp_path, lambda _prompt, _root: task, context
    )

    assert "Active task: `devlog/123-example`" in output
    assert "## Task-workdir rules\n\nComplete task-workdir rules\n" in output
    assert "## Task brief" in output
    assert "Source: `devlog/123-example/010-task-brief.md`" in output
    assert "Complete task brief\n" in output


def test_resolved_task_emits_non_empty_work_state(tmp_path):
    task = make_task(tmp_path, "123-example")
    (task / "work-state.md").write_text(
        "# Work state\n\n## Current state\n\nTests are green.\n", encoding="utf-8"
    )

    output = loader.load_task_context(
        "request", tmp_path, lambda _prompt, _root: task, write_rules(tmp_path)
    )

    assert "## Work state" in output
    assert "Source: `devlog/123-example/work-state.md`" in output
    assert "Tests are green." in output


def test_missing_or_template_only_work_state_does_not_prevent_loading(tmp_path):
    context = write_rules(tmp_path)
    missing_task = make_task(tmp_path, "123-missing-state")
    template_task = make_task(tmp_path, "124-template-state")
    (template_task / "work-state.md").write_text(
        WORK_STATE_TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8"
    )

    missing_output = loader.load_task_context(
        "request", tmp_path, lambda _prompt, _root: missing_task, context
    )
    template_output = loader.load_task_context(
        "request", tmp_path, lambda _prompt, _root: template_task, context
    )

    assert "Active task: `devlog/123-missing-state`" in missing_output
    assert "Active task: `devlog/124-template-state`" in template_output
    assert "## Work state" not in missing_output
    assert "## Work state" not in template_output


def test_missing_task_brief_emits_no_partial_context(tmp_path):
    task = tmp_path / "devlog" / "123-example"
    task.mkdir(parents=True)
    context = write_rules(tmp_path, "rules that must not leak")

    output = loader.load_task_context(
        "request", tmp_path, lambda _prompt, _root: task, context
    )

    assert output == loader.NO_TASK_CONTEXT
    assert "rules that must not leak" not in output


def test_invalid_resolver_result_emits_no_partial_context(tmp_path):
    context = write_rules(tmp_path, "rules that must not leak")

    output = loader.load_task_context(
        "request", tmp_path, lambda _prompt, _root: "devlog/123-example", context
    )

    assert output == loader.NO_TASK_CONTEXT
    assert "rules that must not leak" not in output


def test_missing_resolved_task_directory_emits_no_partial_context(tmp_path):
    context = write_rules(tmp_path, "rules that must not leak")

    output = loader.load_task_context(
        "request",
        tmp_path,
        lambda _prompt, root: root / "devlog" / "123-missing",
        context,
    )

    assert output == loader.NO_TASK_CONTEXT
    assert "rules that must not leak" not in output


def test_resolver_failure_emits_no_partial_context(tmp_path):
    context = write_rules(tmp_path, "rules that must not leak")

    def fail(_prompt, _root):
        raise RuntimeError("resolver failed")

    output = loader.load_task_context("request", tmp_path, fail, context)

    assert output == loader.NO_TASK_CONTEXT
    assert "rules that must not leak" not in output


def test_missing_task_workdir_rules_emits_no_partial_context(tmp_path):
    task = make_task(tmp_path, "123-example", "brief that must not leak")

    output = loader.load_task_context(
        "request",
        tmp_path,
        lambda _prompt, _root: task,
        tmp_path / "missing-context.md",
    )

    assert output == loader.NO_TASK_CONTEXT
    assert "brief that must not leak" not in output
