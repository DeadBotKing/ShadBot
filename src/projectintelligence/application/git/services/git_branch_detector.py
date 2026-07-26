from __future__ import annotations

from ..contracts.git_repository import IGitRepository
from ..models.git_branch import GitBranch


class GitBranchDetector:
    """
    Detects Git branches from repository information.

    Depends only on IGitRepository abstraction.
    """

    def __init__(
        self,
        git_repository: IGitRepository,
    ) -> None:
        self._git_repository = git_repository

    def detect_current(self) -> GitBranch:
        """
        Returns the current active branch.
        """

        return self._git_repository.get_current_branch()

    def detect_all(self) -> tuple[GitBranch, ...]:
        """
        Returns all available branches.
        """

        return self._git_repository.get_branches()
