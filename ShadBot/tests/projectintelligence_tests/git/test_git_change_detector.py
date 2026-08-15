from __future__ import annotations

from unittest.mock import Mock

from projectintelligence.application.git.models.git_change import (
    GitChange,
    GitChangeType,
)
from projectintelligence.application.git.services.git_change_detector import (
    GitChangeDetector,
)


def test_git_change_detector_returns_changes() -> None:
    repository = Mock()

    expected_changes = (
        GitChange(
            path="src/main.py",
            change_type=GitChangeType.MODIFIED,
            is_staged=False,
        ),
        GitChange(
            path="README.md",
            change_type=GitChangeType.ADDED,
            is_staged=True,
        ),
    )

    repository.get_changes.return_value = expected_changes

    detector = GitChangeDetector(repository)

    result = detector.detect()

    assert result == expected_changes
    repository.get_changes.assert_called_once()
