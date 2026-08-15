"""
ShadBot Agent Platform

Code Generator Tool
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .code_generation_context import (
    CodeGenerationContext,
)
from .code_generation_result import (
    CodeGenerationResult,
)
from .code_template_engine import (
    CodeTemplateEngine,
)


class CodeGeneratorTool(ToolContract):
    """
    Generates new source code.
    """

    def __init__(
        self,
        template_engine: CodeTemplateEngine,
    ) -> None:

        self._template_engine = template_engine

    @property
    def tool_type(
        self,
    ) -> ToolType:

        return ToolType.CODE_EXECUTION

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        context = CodeGenerationContext(
            project_id=payload["project_id"],
            target_path=str(
                payload["target_path"],
            ),
            language=str(
                payload["language"],
            ),
            framework=payload.get(
                "framework",
            ),
            requirements=str(
                payload["requirements"],
            ),
            existing_context=dict(
                payload.get(
                    "existing_context",
                    {},
                ),
            ),
        )

        generated = self._template_engine.render(
            template=str(
                payload["template"],
            ),
            variables=context.existing_context,
        )

        result = CodeGenerationResult(
            success=True,
            message="Code generated successfully",
            generated_files=(context.target_path,),
        )

        return {
            "result": result,
            "code": generated,
        }
