from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .git_branch import GitBranch
from .git_change import GitChange
from .git_commit import GitCommit
from .git_status import GitStatus


@dataclass(frozen=True, slots=True)
class GitContext:
    """
    Aggregated Git intelligence context.

    This is the main output model consumed by higher layers.
    """

    project_id: UUID

    status: GitStatus
    current_commit: GitCommit | None
    branches: tuple[GitBranch, ...]
    changes: tuple[GitChange, ...]
    recent_commits: tuple[GitCommit, ...]
