"""
ShadBot Agent Platform

Project analyzer tool adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .project_analyzer_tool import ProjectAnalyzerTool


class ProjectAnalyzerToolAdapter(ToolContract):
    """
    Adapter exposing project analysis operations as agent tool.
    """

    def __init__(self) -> None:
        self._tool = ProjectAnalyzerTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.PROJECT_ANALYZER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        path = str(
            payload.get("path", "."),
        )

        result = self._tool.analyze(
            path,
        )

        return {
            "success": True,
            "analysis": result,
        }
