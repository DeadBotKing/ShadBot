from __future__ import annotations

from ..contracts.git_repository import IGitRepository
from ..models.git_change import GitChange


class GitChangeDetector:
    """
    Detects file changes in a Git repository.

    Uses repository abstraction only.
    """

    def __init__(
        self,
        git_repository: IGitRepository,
    ) -> None:
        self._git_repository = git_repository

    def detect(self) -> tuple[GitChange, ...]:
        """
        Returns current repository changes.
        """

        return self._git_repository.get_changes()
