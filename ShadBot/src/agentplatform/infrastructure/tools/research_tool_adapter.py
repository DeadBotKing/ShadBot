"""
ShadBot Agent Platform

Research tool adapter.
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .research_tool import ResearchTool


class ResearchToolAdapter(ToolContract):
    """
    Adapter for research tool.
    """

    def __init__(self) -> None:
        self._tool = ResearchTool()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.RESEARCH

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        """
        Execute research request.
        """

        query = str(
            payload.get(
                "query",
                "",
            ),
        )

        return self._tool.execute(
            query,
        )
