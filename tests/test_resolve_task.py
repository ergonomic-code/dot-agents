import importlib.util
from pathlib import Path


RESOLVER_PATH = (
    Path(__file__).parents[1] / "src" / "task-workdir" / "resolve_task.py"
)
SPEC = importlib.util.spec_from_file_location("resolve_task", RESOLVER_PATH)
assert SPEC and SPEC.loader
resolver = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(resolver)


def make_task(repo: Path, name: str, brief: str = "brief") -> Path:
    task = repo / "devlog" / name
    task.mkdir(parents=True)
    (task / "010-task-brief.md").write_text(brief, encoding="utf-8")
    return task


def fail_if_called(_prompt, _candidates):
    raise AssertionError("semantic resolver must not be called")


def test_no_devlog(tmp_path):
    assert resolver.resolve_task("123", tmp_path, fail_if_called) is None


def test_no_active_tasks(tmp_path):
    (tmp_path / "devlog" / "done").mkdir(parents=True)
    (tmp_path / "devlog" / "notes").mkdir()
    assert resolver.resolve_task("123", tmp_path, fail_if_called) is None


def test_active_tasks_without_recognized_id(tmp_path):
    make_task(tmp_path, "123-example")
    assert resolver.resolve_task("Update the example task", tmp_path, fail_if_called) is None


def test_standalone_id_line_resolves_without_model(tmp_path):
    task = make_task(tmp_path, "123-example")
    assert resolver.resolve_task("Please implement\n123\nThanks", tmp_path, fail_if_called) == task


def test_id_after_skill_invocation_resolves(tmp_path):
    task = make_task(tmp_path, "123-example")
    assert resolver.resolve_task("Use $implement-task 123", tmp_path, fail_if_called) == task


def test_id_after_skill_reference_resolves(tmp_path):
    task = make_task(tmp_path, "123-example")
    prompt = "Use `src/skills/implement-task/SKILL.md` 123"
    assert resolver.resolve_task(prompt, tmp_path, fail_if_called) == task


def test_unrelated_numbers_are_ignored(tmp_path):
    make_task(tmp_path, "123-example")
    prompt = "Fix 123 errors in version 123 and keep the HTTP 123 behavior."
    assert resolver.resolve_task(prompt, tmp_path, fail_if_called) is None


def test_inactive_and_nonexistent_ids_are_ignored(tmp_path):
    make_task(tmp_path, "123-active")
    (tmp_path / "devlog" / "done" / "456-done").mkdir(parents=True)
    (tmp_path / "devlog" / "on-hold" / "789-paused").mkdir(parents=True)
    prompt = "456\n789\n999"
    assert resolver.resolve_task(prompt, tmp_path, fail_if_called) is None


def test_done_and_on_hold_are_not_active_tasks(tmp_path):
    (tmp_path / "devlog" / "done").mkdir(parents=True)
    (tmp_path / "devlog" / "on-hold").mkdir()
    make_task(tmp_path, "123-active")
    assert set(resolver.active_tasks(tmp_path)) == {"123"}


def test_multiple_matches_invoke_semantic_resolver_with_candidates(tmp_path):
    first = make_task(tmp_path, "123-first", "first brief")
    second = make_task(tmp_path, "456-second", "second brief")
    calls = []

    def select(prompt, candidates):
        calls.append((prompt, candidates))
        return "456"

    prompt = "$work 123\n$work 456\nImplement the second task"
    assert resolver.resolve_task(prompt, tmp_path, select) == second
    assert calls == [(prompt, {"123": first, "456": second})]


def test_semantic_resolver_can_return_na(tmp_path):
    make_task(tmp_path, "123-first")
    make_task(tmp_path, "456-second")
    assert resolver.resolve_task("123\n456", tmp_path, lambda *_: "n/a") is None


def test_invalid_semantic_resolver_output_becomes_na(tmp_path):
    make_task(tmp_path, "123-first")
    make_task(tmp_path, "456-second")
    assert resolver.resolve_task("123\n456", tmp_path, lambda *_: "Task 123") is None
