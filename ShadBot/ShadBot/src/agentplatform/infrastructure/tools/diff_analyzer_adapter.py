"""
ShadBot Agent Platform

Diff analyzer tool adapter.
"""

from __future__ import annotations

import difflib

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class DiffAnalyzerAdapter(ToolContract):
    """
    Analyze text differences.
    """

    @property
    def tool_type(self) -> ToolType:
        return ToolType.DIFF_ANALYZER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        old_content = str(
            payload.get("old", ""),
        )

        new_content = str(
            payload.get("new", ""),
        )

        diff = list(
            difflib.unified_diff(
                old_content.splitlines(),
                new_content.splitlines(),
            ),
        )

        return {
            "success": True,
            "diff": diff,
        }
