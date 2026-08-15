from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GitBranch:
    """
    Represents a Git branch.

    This model contains only branch information and is intentionally
    immutable.
    """

    name: str
    is_current: bool
    is_remote: bool
