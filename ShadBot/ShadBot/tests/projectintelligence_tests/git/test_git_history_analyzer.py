from __future__ import annotations

from datetime import datetime
from unittest.mock import Mock

from projectintelligence.application.git.models.git_commit import (
    GitCommit,
)
from projectintelligence.application.git.services.git_history_analyzer import (
    GitHistoryAnalyzer,
)


def test_git_history_analyzer_returns_recent_commits() -> None:
    repository = Mock()

    expected_commits = (
        GitCommit(
            hash="abc123456",
            short_hash="abc1234",
            author="Developer",
            email="developer@example.com",
            message="Initial commit",
            date=datetime.now(),
        ),
    )

    repository.get_recent_commits.return_value = expected_commits

    analyzer = GitHistoryAnalyzer(repository)

    result = analyzer.analyze(limit=10)

    assert result == expected_commits
    repository.get_recent_commits.assert_called_once_with(10)
