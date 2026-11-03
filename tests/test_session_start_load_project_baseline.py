import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "bootstrap" / "hooks" / "session_start_load_project_baseline.py"


def create_repo(tmp_path: Path, baseline: str | None = "BASELINE", index: str | None = "INDEX") -> Path:
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    src = tmp_path / ".agents" / "ergo" / "src"
    (src / "context").mkdir(parents=True)
    if baseline is not None:
        (src / "project-baseline.md").write_text(baseline, encoding="utf-8")
    if index is not None:
        (src / "context" / "index.md").write_text(index, encoding="utf-8")
    routes = [
        ("production-code.md", ["core"], 20, "production"),
        ("tdd.md", ["tdd"], 25, "tdd"),
        ("tests.md", ["core"], 30, "tests"),
        ("ergonomic-testing.md", ["ergonomic-testing"], 35, "ergonomic tests"),
        ("relational-databses.md", ["database"], 40, "database"),
        ("http-api.md", ["http-api"], 50, "http"),
        ("test-doubles.md", ["core"], 80, "test doubles"),
        ("http-api-errors.md", ["http-api"], 100, "http errors"),
        ("http-api-test-clients.md", ["http-api"], 105, "http test clients"),
        ("complex-test-fixtures.md", ["core"], 125, "complex fixtures"),
        ("junit.md", ["junit"], 130, "junit"),
        ("kotest.md", ["kotest"], 140, "kotest"),
    ]
    for name, modules, order, applicability in routes:
        modules_yaml = "\n".join(f"  - {module}" for module in modules)
        (src / "context" / name).write_text(
            f"---\nrequires_modules:\n{modules_yaml}\n"
            f"applies_when: {applicability}\nrouting_order: {order}\n---\n\nBODY {name}\n",
            encoding="utf-8",
        )
    return tmp_path


def run_hook(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )


def test_emits_baseline_then_root_index(tmp_path):
    repo = create_repo(tmp_path)

    result = run_hook(repo)

    assert result.returncode == 0
    assert result.stdout.startswith("BASELINE\n\nINDEX\n\n# Разрешённые тематические маршруты\n")
    assert "`.agents/ergo/src/context/production-code.md`" in result.stdout
    assert "`.agents/ergo/src/context/tests.md`" in result.stdout
    assert "`.agents/ergo/src/context/complex-test-fixtures.md`" in result.stdout
    assert "`.agents/ergo/src/context/test-doubles.md`" in result.stdout
    assert "BODY" not in result.stdout


def test_emits_optional_config_after_mandatory_context(tmp_path):
    repo = create_repo(tmp_path)
    (repo / "ergo-config.yaml").write_text(
        "artifact_language: en\nmodules:\n  - core\n  - junit\n",
        encoding="utf-8",
    )

    result = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert result.returncode == 0
    assert result.stdout.startswith("BASELINE\n\nINDEX\n\n# Разрешённые тематические маршруты\n")
    assert "`.agents/ergo/src/context/junit.md`" in result.stdout
    assert "`.agents/ergo/src/context/test-doubles.md`" in result.stdout
    assert "`.agents/ergo/src/context/relational-databses.md`" not in result.stdout
    assert "`.agents/ergo/src/context/http-api.md`" not in result.stdout
    assert result.stdout.index("# Разрешённые тематические маршруты") < result.stdout.index("# Framework config")
    assert "```yaml\nartifact_language: en\nmodules:" in result.stdout


def test_ergonomic_testing_route_requires_explicit_module(tmp_path):
    repo = create_repo(tmp_path)
    config = repo / "ergo-config.yaml"
    config.write_text("modules:\n  - core\n", encoding="utf-8")

    without_module = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert without_module.returncode == 0
    assert "`.agents/ergo/src/context/tests.md`" in without_module.stdout
    assert "`.agents/ergo/src/context/ergonomic-testing.md`" not in without_module.stdout

    config.write_text(
        "modules:\n  - core\n  - ergonomic-testing\n", encoding="utf-8"
    )

    with_module = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert with_module.returncode == 0
    assert "`.agents/ergo/src/context/ergonomic-testing.md`" in with_module.stdout


def test_tdd_route_requires_explicit_module(tmp_path):
    repo = create_repo(tmp_path)
    config = repo / "ergo-config.yaml"
    config.write_text(
        "modules:\n  - core\n  - ergonomic-testing\n", encoding="utf-8"
    )

    without_module = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert without_module.returncode == 0
    assert "`.agents/ergo/src/context/tdd.md`" not in without_module.stdout

    config.write_text("modules:\n  - core\n  - tdd\n", encoding="utf-8")

    with_module = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert with_module.returncode == 0
    assert "`.agents/ergo/src/context/tdd.md`" in with_module.stdout
    assert "`.agents/ergo/src/context/ergonomic-testing.md`" not in with_module.stdout


def test_http_routes_require_only_http_api_module(tmp_path):
    repo = create_repo(tmp_path)
    config = repo / "ergo-config.yaml"
    config.write_text("modules:\n  - core\n", encoding="utf-8")

    core_only = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert core_only.returncode == 0
    assert "`.agents/ergo/src/context/test-doubles.md`" in core_only.stdout
    assert "`.agents/ergo/src/context/http-api-errors.md`" not in core_only.stdout
    assert "`.agents/ergo/src/context/http-api-test-clients.md`" not in core_only.stdout

    config.write_text(
        "modules:\n  - core\n  - http-api\n",
        encoding="utf-8",
    )

    with_http = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert with_http.returncode == 0
    assert "`.agents/ergo/src/context/http-api-errors.md`" in with_http.stdout
    assert "`.agents/ergo/src/context/http-api-test-clients.md`" in with_http.stdout
    assert "`.agents/ergo/src/context/complex-test-fixtures.md`" in with_http.stdout


def test_missing_modules_uses_only_core(tmp_path):
    repo = create_repo(tmp_path)
    (repo / "ergo-config.yaml").write_text("artifact_language: ru\n", encoding="utf-8")

    result = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert result.returncode == 0
    assert "`.agents/ergo/src/context/production-code.md`" in result.stdout
    assert "`.agents/ergo/src/context/test-doubles.md`" in result.stdout


@pytest.mark.parametrize("module", ["unknown", "kotlin", "spring"])
def test_invalid_config_fails_without_expanding_routes(tmp_path, module):
    repo = create_repo(tmp_path)
    (repo / "ergo-config.yaml").write_text(
        f"modules:\n  - core\n  - {module}\n",
        encoding="utf-8",
    )

    result = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert result.returncode == 1
    assert result.stdout == ""
    assert f"unknown modules: {module}" in result.stderr


def test_explicit_modules_must_include_core(tmp_path):
    repo = create_repo(tmp_path)
    (repo / "ergo-config.yaml").write_text("modules:\n  - junit\n", encoding="utf-8")

    result = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert result.returncode == 1
    assert "must include core" in result.stderr


def test_malformed_config_fails_without_output(tmp_path):
    repo = create_repo(tmp_path)
    (repo / "ergo-config.yaml").write_text("modules: [core\n", encoding="utf-8")

    result = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert result.returncode == 1
    assert result.stdout == ""
    assert "invalid framework config YAML" in result.stderr


def test_missing_baseline_fails(tmp_path):
    result = run_hook(create_repo(tmp_path, baseline=None))

    assert result.returncode == 1
    assert "mandatory framework context file is missing" in result.stderr
    assert "project-baseline.md" in result.stderr


def test_missing_root_index_fails(tmp_path):
    result = run_hook(create_repo(tmp_path, index=None))

    assert result.returncode == 1
    assert "mandatory framework context file is missing" in result.stderr
    assert "context/index.md" in result.stderr


def test_empty_mandatory_files_fail(tmp_path):
    for baseline, index, expected_path in [
        (" \n", "INDEX", "project-baseline.md"),
        ("BASELINE", "\n", "context/index.md"),
    ]:
        repo = create_repo(tmp_path / expected_path.replace("/", "-"), baseline, index)

        result = run_hook(repo)

        assert result.returncode == 1
        assert "mandatory framework context file is empty" in result.stderr
        assert expected_path in result.stderr
