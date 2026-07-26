from __future__ import annotations

from abc import ABC, abstractmethod

from ..models.git_branch import GitBranch
from ..models.git_change import GitChange
from ..models.git_commit import GitCommit
from ..models.git_status import GitStatus


class IGitRepository(ABC):
    """
    Contract for Git repository access.

    Application services depend on this abstraction,
    never on concrete Git implementations.
    """

    @abstractmethod
    def get_status(self) -> GitStatus:
        """
        Returns current repository status.
        """

    @abstractmethod
    def get_current_branch(self) -> GitBranch:
        """
        Returns current active branch.
        """

    @abstractmethod
    def get_branches(self) -> tuple[GitBranch, ...]:
        """
        Returns available branches.
        """

    @abstractmethod
    def get_changes(self) -> tuple[GitChange, ...]:
        """
        Returns repository changes.
        """

    @abstractmethod
    def get_head_commit(self) -> GitCommit | None:
        """
        Returns current HEAD commit.
        """

    @abstractmethod
    def get_recent_commits(
        self,
        limit: int,
    ) -> tuple[GitCommit, ...]:
        """
        Returns recent commits.
        """
