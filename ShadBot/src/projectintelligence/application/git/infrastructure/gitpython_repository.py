from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..contracts.git_repository import IGitRepository
from ..models.git_branch import GitBranch
from ..models.git_change import GitChange, GitChangeType
from ..models.git_commit import GitCommit
from ..models.git_status import GitStatus

try:
    from git import Repo
    _GIT_AVAILABLE = True
except ImportError:
    Repo = Any  # type: ignore[assignment,misc]
    _GIT_AVAILABLE = False


class GitPythonRepository(IGitRepository):
    """
    Git repository adapter using GitPython.

    This class belongs to Infrastructure layer only.
    Application services depend on IGitRepository.
    """

    def __init__(self, repository_path: Path) -> None:
        self._repository_path = repository_path
        self._repo: Any = None
        if _GIT_AVAILABLE:
            try:
                self._repo = Repo(repository_path)
            except Exception:
                self._repo = None

    def get_status(self) -> GitStatus:
        if self._repo is None:
            return GitStatus(
                is_repository=False,
                is_dirty=False,
                ahead=0,
                behind=0,
                current_branch="main",
            )

        branch = self.get_current_branch()

        return GitStatus(
            is_repository=True,
            is_dirty=self._repo.is_dirty(),
            ahead=0,
            behind=0,
            current_branch=branch.name,
        )

    def get_current_branch(self) -> GitBranch:
        if self._repo is None:
            return GitBranch(
                name="main",
                is_current=True,
                is_remote=False,
            )

        branch = self._repo.active_branch

        return GitBranch(
            name=branch.name,
            is_current=True,
            is_remote=False,
        )

    def get_branches(self) -> tuple[GitBranch, ...]:
        if self._repo is None:
            return (
                GitBranch(
                    name="main",
                    is_current=True,
                    is_remote=False,
                ),
            )

        return tuple(
            GitBranch(
                name=branch.name,
                is_current=branch == self._repo.active_branch,
                is_remote=False,
            )
            for branch in self._repo.branches
        )

    def get_changes(self) -> tuple[GitChange, ...]:
        if self._repo is None:
            return ()

        changes: list[GitChange] = []

        for item in self._repo.index.diff(None):
            changes.append(
                GitChange(
                    path=item.a_path or "",
                    change_type=GitChangeType.MODIFIED,
                    is_staged=False,
                )
            )

        return tuple(changes)

    def get_head_commit(self) -> GitCommit | None:
        if self._repo is None:
            return GitCommit(
                hash="0000000000000000000000000000000000000000",
                short_hash="0000000",
                author="ShadBot",
                email="bot@shadbot.ai",
                message="Initial commit",
                date=datetime.now(timezone.utc),
            )

        commit = self._repo.head.commit

        return GitCommit(
            hash=commit.hexsha,
            short_hash=commit.hexsha[:7],
            author=commit.author.name or "",
            email=commit.author.email or "",
            message=str(commit.message).strip(),
            date=commit.committed_datetime,
        )

    def get_recent_commits(
        self,
        limit: int,
    ) -> tuple[GitCommit, ...]:
        if self._repo is None:
            head = self.get_head_commit()
            return (head,) if head else ()

        commits = []

        for commit in self._repo.iter_commits(max_count=limit):
            commits.append(
                GitCommit(
                    hash=commit.hexsha,
                    short_hash=commit.hexsha[:7],
                    author=commit.author.name or "",
                    email=commit.author.email or "",
                    message=str(commit.message).strip(),
                    date=commit.committed_datetime,
                )
            )

        return tuple(commits)
