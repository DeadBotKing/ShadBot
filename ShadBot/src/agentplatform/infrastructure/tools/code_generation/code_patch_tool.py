"""
ShadBot Agent Platform

Code Patch Tool
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .code_generation_result import (
    CodeGenerationResult,
)


class CodePatchTool(ToolContract):
    """
    Generates controlled code patches.
    """

    @property
    def tool_type(
        self,
    ) -> ToolType:

        return ToolType.PATCH_APPLIER

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        patch = str(
            payload["patch"],
        )

        result = CodeGenerationResult(
            success=True,
            message="Patch generated successfully",
            patches=(patch,),
        )

        return {
            "result": result,
            "patch": patch,
        }
