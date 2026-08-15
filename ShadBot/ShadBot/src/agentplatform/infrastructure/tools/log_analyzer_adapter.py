"""
ShadBot Agent Platform

Log analyzer adapter.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .log_analyzer import LogAnalyzer


class LogAnalyzerAdapter(ToolContract):
    """
    Adapter exposing log analysis.
    """

    def __init__(self) -> None:
        self._analyzer = LogAnalyzer()

    @property
    def tool_type(
        self,
    ) -> ToolType:
        return ToolType.LOG_ANALYZER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:
        action = str(
            payload.get(
                "action",
                "file",
            ),
        )

        path = Path(
            str(
                payload.get(
                    "path",
                    ".",
                ),
            ),
        )

        if action == "directory" or path.is_dir():
            return self._analyzer.analyze_directory(
                path,
            )

        return self._analyzer.analyze_file(
            path,
        )
