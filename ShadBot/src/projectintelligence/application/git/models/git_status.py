from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GitStatus:
    """
    Represents the current status of a Git repository.
    """

    is_repository: bool
    is_dirty: bool
    ahead: int
    behind: int
    current_branch: str
