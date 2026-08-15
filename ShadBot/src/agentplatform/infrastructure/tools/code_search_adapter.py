"""
ShadBot Agent Platform

Code search tool adapter.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class CodeSearchAdapter(ToolContract):
    """
    Search source code.
    """

    @property
    def tool_type(self) -> ToolType:
        return ToolType.CODE_SEARCH

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        root = Path(
            str(payload.get("path", ".")),
        )

        keyword = str(
            payload.get("keyword", ""),
        )

        results: list[str] = []

        for file in root.rglob("*"):
            if file.is_file():
                try:
                    content = file.read_text(
                        encoding="utf-8",
                    )

                    if keyword in content:
                        results.append(
                            str(file),
                        )

                except Exception:
                    continue

        return {
            "success": True,
            "matches": results,
        }
