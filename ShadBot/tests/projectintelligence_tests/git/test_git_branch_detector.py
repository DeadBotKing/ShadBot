from __future__ import annotations

from unittest.mock import Mock

from projectintelligence.application.git.models.git_branch import (
    GitBranch,
)
from projectintelligence.application.git.services.git_branch_detector import (
    GitBranchDetector,
)


def test_git_branch_detector_returns_current_branch() -> None:
    repository = Mock()

    expected_branch = GitBranch(
        name="main",
        is_current=True,
        is_remote=False,
    )

    repository.get_current_branch.return_value = expected_branch

    detector = GitBranchDetector(repository)

    result = detector.detect_current()

    assert result == expected_branch
    repository.get_current_branch.assert_called_once()


def test_git_branch_detector_returns_all_branches() -> None:
    repository = Mock()

    expected_branches = (
        GitBranch(
            name="main",
            is_current=True,
            is_remote=False,
        ),
        GitBranch(
            name="develop",
            is_current=False,
            is_remote=False,
        ),
    )

    repository.get_branches.return_value = expected_branches

    detector = GitBranchDetector(repository)

    result = detector.detect_all()

    assert result == expected_branches
    repository.get_branches.assert_called_once()
