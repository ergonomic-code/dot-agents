import subprocess
import sys
from pathlib import Path


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
    assert result.stdout == "BASELINE\n\nINDEX\n"


def test_emits_optional_config_after_mandatory_context(tmp_path):
    repo = create_repo(tmp_path)
    (repo / "ergo-config.yaml").write_text("artifact_language: en\n", encoding="utf-8")

    result = run_hook(repo, "--framework-config-path", "ergo-config.yaml")

    assert result.returncode == 0
    assert result.stdout.startswith("BASELINE\n\nINDEX\n\n# Framework config\n")
    assert "```yaml\nartifact_language: en\n```" in result.stdout


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
