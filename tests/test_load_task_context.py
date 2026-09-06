import importlib.util
from pathlib import Path
import sys


TASK_WORKDIR = Path(__file__).parents[1] / "src" / "task-workdir"
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
