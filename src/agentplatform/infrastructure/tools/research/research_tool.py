"""
ShadBot Agent Platform

Research Tool
"""

from __future__ import annotations

from agentplatform.domain.tools import (
    ToolContract,
    ToolType,
)

from .research_context import (
    ResearchContext,
)
from .research_operation import (
    ResearchOperation,
)
from .research_result import (
    ResearchResult,
)


class ResearchTool(ToolContract):
    """
    Agent research execution tool.
    """

    @property
    def tool_type(
        self,
    ) -> ToolType:

        return ToolType.RESEARCH

    def execute(
        self,
        payload: dict[str, object],
    ) -> dict[str, object]:

        context = ResearchContext(
            project_id=payload["project_id"],
            agent_role=str(
                payload["agent_role"],
            ),
            operation=ResearchOperation(
                payload["operation"],
            ),
            query=str(
                payload["query"],
            ),
            sources=tuple(
                payload.get(
                    "sources",
                    (),
                ),
            ),
        )

        result = self._execute_research(
            context,
        )

        return {
            "result": result,
        }

    def _execute_research(
        self,
        context: ResearchContext,
    ) -> ResearchResult:

        findings = (
            f"Research operation '{context.operation.value}' "
            f"executed for query: {context.query}"
        )

        return ResearchResult(
            success=True,
            query=context.query,
            findings=findings,
            sources=context.sources,
            confidence=0.0,
        )
