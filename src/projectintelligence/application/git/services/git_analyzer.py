from __future__ import annotations

from ..models.git_context import GitContext
from .git_branch_detector import GitBranchDetector
from .git_change_detector import GitChangeDetector
from .git_history_analyzer import GitHistoryAnalyzer
from .git_status_detector import GitStatusDetector


class GitAnalyzer:
    """
    Main Git analysis orchestrator.

    Coordinates Git analysis services and produces
    a unified GitContext.
    """

    def __init__(
        self,
        status_detector: GitStatusDetector,
        branch_detector: GitBranchDetector,
        change_detector: GitChangeDetector,
        history_analyzer: GitHistoryAnalyzer,
    ) -> None:
        self._status_detector = status_detector
        self._branch_detector = branch_detector
        self._change_detector = change_detector
        self._history_analyzer = history_analyzer

    def analyze(self) -> GitContext:
        """
        Executes Git intelligence analysis pipeline.
        """

        return GitContext(
            status=self._status_detector.detect(),
            current_commit=None,
            branches=self._branch_detector.detect_all(),
            changes=self._change_detector.detect(),
            recent_commits=self._history_analyzer.analyze(),
        )
