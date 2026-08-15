"""
ShadBot Agent Platform

Git Service
"""

from __future__ import annotations

from .git_repository_tool import (
    GitRepositoryTool,
)


class GitService:
    """
    Application service for git operations.
    """

    def __init__(
        self,
        repository_tool: GitRepositoryTool,
    ) -> None:

        self._repository_tool = repository_tool

    def execute(
        self,
        request: dict[str, object],
    ) -> dict[str, object]:

        return self._repository_tool.execute(
            request,
        )
