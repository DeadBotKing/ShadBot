from __future__ import annotations

from unittest.mock import Mock

from projectintelligence.application.git.models.git_status import (
    GitStatus,
)
from projectintelligence.application.git.services.git_status_detector import (
    GitStatusDetector,
)


def test_git_status_detector_returns_repository_status() -> None:
    repository = Mock()

    expected_status = GitStatus(
        is_repository=True,
        is_dirty=False,
        ahead=0,
        behind=0,
        current_branch="main",
    )

    repository.get_status.return_value = expected_status

    detector = GitStatusDetector(repository)

    result = detector.detect()

    assert result == expected_status
    repository.get_status.assert_called_once()
