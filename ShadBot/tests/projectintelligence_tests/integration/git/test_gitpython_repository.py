from __future__ import annotations

from pathlib import Path
import pytest

git = pytest.importorskip("git")
Repo = git.Repo

from projectintelligence.application.git.infrastructure.gitpython_repository import (
    GitPythonRepository,
)


def test_gitpython_repository_reads_repository(tmp_path: Path) -> None:
    repo_path = tmp_path / "test_repo"
    repo_path.mkdir()

    repo = Repo.init(repo_path)

    file_path = repo_path / "README.md"
    file_path.write_text(
        "# Test Repository",
        encoding="utf-8",
    )

    repo.index.add(
        ["README.md"],
    )

    repo.index.commit(
        "Initial commit",
    )

    repository = GitPythonRepository(
        repo_path,
    )

    status = repository.get_status()

    assert status.is_repository is True
    assert status.current_branch is not None
