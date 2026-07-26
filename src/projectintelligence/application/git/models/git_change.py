from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class GitChangeType(str, Enum):
    """
    Supported Git change types.
    """

    ADDED = "added"
    MODIFIED = "modified"
    DELETED = "deleted"
    RENAMED = "renamed"
    UNTRACKED = "untracked"


@dataclass(frozen=True, slots=True)
class GitChange:
    """
    Represents a single changed file in a Git repository.
    """

    path: str
    change_type: GitChangeType
    is_staged: bool
