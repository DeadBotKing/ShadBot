"""
ShadBot Agent Platform

Git Execution Context
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .git_operation import GitOperation


@dataclass(frozen=True, slots=True)
class GitExecutionContext:
    """
    Context required for git execution.
    """

    project_id: UUID

    repository_path: str

    operation: GitOperation

    arguments: tuple[str, ...] = ()
