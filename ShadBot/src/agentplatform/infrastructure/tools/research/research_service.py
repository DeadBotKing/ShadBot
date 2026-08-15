"""
ShadBot Agent Platform

Research Service
"""

from __future__ import annotations

from .research_tool import (
    ResearchTool,
)


class ResearchService:
    """
    Application service for research execution.
    """

    def __init__(
        self,
        research_tool: ResearchTool,
    ) -> None:

        self._research_tool = research_tool

    def execute(
        self,
        request: dict[str, object],
    ) -> dict[str, object]:

        return self._research_tool.execute(
            request,
        )
