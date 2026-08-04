"""
ShadBot Agent Platform

Terminal tool adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .terminal_tool import TerminalTool


class TerminalToolAdapter(ToolContract):
    """
    Adapter exposing terminal operations as agent tool.
    """

    def __init__(self) -> None:
        self._tool = TerminalTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.TERMINAL

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        command = str(
            payload["command"],
        )

        path = str(
            payload["path"],
        )

        output = self._tool.execute(
            command=command,
            path=path,
        )

        return {
            "success": True,
            "output": output,
        }
