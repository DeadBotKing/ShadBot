from __future__ import annotations

from unittest.mock import Mock

from projectintelligence.application.git.models.git_branch import (
    GitBranch,
)
from projectintelligence.application.git.models.git_commit import (
    GitCommit,
)
from projectintelligence.application.git.models.git_status import (
    GitStatus,
)
from projectintelligence.application.git.services.git_analyzer import (
    GitAnalyzer,
)


def test_git_analyzer_builds_git_context() -> None:
    status_detector = Mock()
    branch_detector = Mock()
    change_detector = Mock()
    history_analyzer = Mock()

    status_detector.detect.return_value = GitStatus(
        is_repository=True,
        is_dirty=False,
        ahead=0,
        behind=0,
        current_branch="main",
    )

    branch_detector.detect_all.return_value = (
        GitBranch(
            name="main",
            is_current=True,
            is_remote=False,
        ),
    )

    change_detector.detect.return_value = ()

    history_analyzer.analyze.return_value = (
        GitCommit(
            hash="abc123",
            short_hash="abc123",
            author="Developer",
            email="developer@example.com",
            message="Initial commit",
            date=None,
        ),
    )

    analyzer = GitAnalyzer(
        status_detector=status_detector,
        branch_detector=branch_detector,
        change_detector=change_detector,
        history_analyzer=history_analyzer,
    )

    result = analyzer.analyze()

    assert result.status.current_branch == "main"
    assert len(result.branches) == 1
    assert result.changes == ()
    assert len(result.recent_commits) == 1
