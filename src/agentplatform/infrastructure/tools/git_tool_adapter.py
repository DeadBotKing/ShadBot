"""
ShadBot Agent Platform

Git tool adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .git_tool import GitTool


class GitToolAdapter(ToolContract):
    """
    Adapter exposing git operations.
    """

    def __init__(self) -> None:
        self._tool = GitTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.GIT

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        action = str(
            payload.get(
                "action",
                "",
            ),
        )

        path = str(
            payload["path"],
        )

        if action == "status":
            return {
                "success": True,
                "status": self._tool.status(path),
            }

        if action == "diff":
            return {
                "success": True,
                "diff": self._tool.diff(path),
            }

        if action == "log":
            return {
                "success": True,
                "log": self._tool.log(path),
            }

        raise ValueError(
            f"Unsupported git action: {action}",
        )
