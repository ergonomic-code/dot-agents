import importlib.util
from pathlib import Path

import pytest


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


def test_id_between_escaped_newlines_resolves_without_model(tmp_path):
    task = make_task(tmp_path, "123-example")
    prompt = r"123\n\nPlease implement devlog/123-example/040-plan.md"
    assert resolver.resolve_task(prompt, tmp_path, fail_if_called) == task


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


@pytest.mark.parametrize("task_id", ["7", "12345", "001", "001.02", "ABC", "АБВ", "371.1", "EL.363", "A.B.42"])
@pytest.mark.parametrize("prompt", ["{task_id}", "$work {task_id}", "`src/skills/work/SKILL.md` {task_id}", r"{task_id}\nPlease implement"])
def test_full_task_code_resolves(tmp_path, task_id, prompt):
    task = make_task(tmp_path, f"{task_id}-export-events")
    assert resolver.resolve_task(prompt.format(task_id=task_id), tmp_path, fail_if_called) == task


@pytest.mark.parametrize("task_id", ["12345", "ABC", "АБВ"])
def test_legacy_task_without_metadata_resolves(tmp_path, task_id):
    task = make_task(tmp_path, f"{task_id}-export-events")
    assert resolver.resolve_task(task_id, tmp_path, fail_if_called) == task


def test_dotted_code_is_not_confused_with_prefix_or_slug(tmp_path):
    short = make_task(tmp_path, "371-doctor-portal")
    full = make_task(tmp_path, "371.1-refactor-roles")
    assert resolver.resolve_task("$work 371.1", tmp_path, fail_if_called) == full
    assert resolver.resolve_task("$work 371", tmp_path, fail_if_called) == short
    assert resolver.resolve_task("$work 371.1-refactor-roles", tmp_path, fail_if_called) is None


@pytest.mark.parametrize("prompt", ["371-1", "$work 371-1"])
def test_hyphen_separates_slug_instead_of_code(tmp_path, prompt):
    task = make_task(tmp_path, "371-1-refactor-roles", '---\ntask_id: "371-1"\n---\nbrief')
    assert resolver.directory_task_id(task) == "371"
    assert resolver.resolve_task(prompt, tmp_path, fail_if_called) is None
    assert resolver.resolve_task("371", tmp_path, fail_if_called) == task


@pytest.mark.parametrize("code", [".371", "371.", "371..1", "371_1", "371.1x", "371.1-", "371.1.2"])
@pytest.mark.parametrize("prompt", ["{code}", "$work {code}", "`src/skills/work/SKILL.md` {code}"])
def test_invalid_or_partial_dotted_codes_are_not_matched(tmp_path, code, prompt):
    make_task(tmp_path, "371-base")
    make_task(tmp_path, "371.1-subtask")
    assert resolver.resolve_task(prompt.format(code=code), tmp_path, fail_if_called) is None


@pytest.mark.parametrize("name", [".371-example", "371.-example", "371..1-example", "371_1-example", "371.1-"])
def test_invalid_directory_codes_are_excluded(tmp_path, name):
    make_task(tmp_path, name)
    assert resolver.active_tasks(tmp_path) == {}


@pytest.mark.parametrize("prompt", ["$work abc", "$work ABC_def", "$work ABC-", "Fix ABC errors"])
def test_inexact_or_unrelated_codes_are_ignored(tmp_path, prompt):
    make_task(tmp_path, "ABC-export")
    assert resolver.resolve_task(prompt, tmp_path, fail_if_called) is None


@pytest.mark.parametrize("metadata", ['task_id: "EL.363"', 'task_id: "OTHER"', 'task_id: "../EL"', 'task_id: "EL--363"', 'task_id: 123', 'task_id: [EL]', 'task_id: [', '[]'])
def test_metadata_does_not_affect_directory_code(tmp_path, metadata):
    task = make_task(tmp_path, "EL.363-export", f"---\n{metadata}\n---\nbrief")
    assert resolver.resolve_task("EL.363", tmp_path, fail_if_called) == task
    assert resolver.resolve_task("OTHER\nEL", tmp_path, fail_if_called) is None


def test_duplicate_full_codes_are_excluded(tmp_path):
    for slug in ("first", "second"):
        make_task(tmp_path, f"EL.363-{slug}")
    assert resolver.resolve_task("EL.363", tmp_path, fail_if_called) is None


def test_mixed_codes_reach_semantic_resolver_without_numeric_conversion(tmp_path):
    tasks = {}
    for task_id in ("001", "12345", "ABC", "EL.363"):
        tasks[task_id] = make_task(tmp_path, f"{task_id}-export")

    def select(_prompt, candidates):
        assert candidates == tasks
        return "EL.363"

    assert resolver.resolve_task("\n".join(tasks), tmp_path, select) == tasks["EL.363"]


def test_metadata_without_task_id_preserves_legacy_resolution(tmp_path):
    task = make_task(tmp_path, "001-export", "---\ntitle: export\n---\nbrief")
    assert resolver.resolve_task("001", tmp_path, fail_if_called) == task
