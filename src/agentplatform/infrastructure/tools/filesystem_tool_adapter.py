"""
ShadBot Agent Platform

Filesystem tool adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .filesystem_tool import FileSystemTool


class FileSystemToolAdapter(ToolContract):
    """
    Adapter exposing filesystem operations as agent tool.
    """

    def __init__(self) -> None:
        self._tool = FileSystemTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.FILE_SYSTEM

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        action = str(
            payload.get("action", ""),
        )

        if action == "read":
            content = self._tool.read_file(
                str(payload["path"]),
            )

            return {
                "success": True,
                "content": content,
            }

        if action == "write":
            self._tool.write_file(
                str(payload["path"]),
                str(payload["content"]),
            )

            return {
                "success": True,
            }

        raise ValueError(
            f"Unsupported filesystem action: {action}",
        )
