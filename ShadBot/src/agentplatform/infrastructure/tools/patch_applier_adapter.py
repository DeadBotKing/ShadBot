"""
ShadBot Agent Platform

Patch applier adapter.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)


class PatchApplierAdapter(ToolContract):

    @property
    def tool_type(self) -> ToolType:
        return ToolType.PATCH_APPLIER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        path = Path(
            str(payload["path"]),
        )

        content = str(
            payload["content"],
        )

        path.write_text(
            content,
            encoding="utf-8",
        )

        return {
            "success": True,
            "path": str(path),
        }
