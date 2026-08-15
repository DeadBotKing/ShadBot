"""
ShadBot Agent Platform

Documentation analyzer adapter.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .documentation_analyzer import DocumentationAnalyzer


class DocumentationAnalyzerAdapter(ToolContract):
    """
    Adapter for documentation analyzer.
    """

    def __init__(self) -> None:
        self._tool = DocumentationAnalyzer()

    @property
    def tool_type(self) -> ToolType:
        return ToolType.DOCUMENTATION_ANALYSIS

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        path = Path(
            str(
                payload.get(
                    "path",
                    ".",
                ),
            ),
        )

        return self._tool.execute(
            path,
        )
