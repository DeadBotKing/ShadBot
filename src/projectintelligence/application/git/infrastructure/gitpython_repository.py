from __future__ import annotations

from pathlib import Path

from git import Repo

from ..contracts.git_repository import IGitRepository
from ..models.git_branch import GitBranch
from ..models.git_change import GitChange, GitChangeType
from ..models.git_commit import GitCommit
from ..models.git_status import GitStatus


class GitPythonRepository(IGitRepository):
    """
    Git repository adapter using GitPython.

    This class belongs to Infrastructure layer only.
    Application services depend on IGitRepository.
    """

    def __init__(self, repository_path: Path) -> None:
        self._repo = Repo(repository_path)

    def get_status(self) -> GitStatus:
        branch = self.get_current_branch()

        return GitStatus(
            is_repository=True,
            is_dirty=self._repo.is_dirty(),
            ahead=0,
            behind=0,
            current_branch=branch.name,
        )

    def get_current_branch(self) -> GitBranch:
        branch = self._repo.active_branch

        return GitBranch(
            name=branch.name,
            is_current=True,
            is_remote=False,
        )

    def get_branches(self) -> tuple[GitBranch, ...]:
        return tuple(
            GitBranch(
                name=branch.name,
                is_current=branch == self._repo.active_branch,
                is_remote=False,
            )
            for branch in self._repo.branches
        )

    def get_changes(self) -> tuple[GitChange, ...]:
        changes: list[GitChange] = []

        for item in self._repo.index.diff(None):
            changes.append(
                GitChange(
                    path=item.a_path,
                    change_type=GitChangeType.MODIFIED,
                    is_staged=False,
                )
            )

        return tuple(changes)

    def get_head_commit(self) -> GitCommit | None:
        commit = self._repo.head.commit

        return GitCommit(
            hash=commit.hexsha,
            short_hash=commit.hexsha[:7],
            author=commit.author.name,
            email=commit.author.email,
            message=commit.message.strip(),
            date=commit.committed_datetime,
        )

    def get_recent_commits(
        self,
        limit: int,
    ) -> tuple[GitCommit, ...]:
        commits = []

        for commit in self._repo.iter_commits(max_count=limit):
            commits.append(
                GitCommit(
                    hash=commit.hexsha,
                    short_hash=commit.hexsha[:7],
                    author=commit.author.name,
                    email=commit.author.email,
                    message=commit.message.strip(),
                    date=commit.committed_datetime,
                )
            )

        return tuple(commits)
