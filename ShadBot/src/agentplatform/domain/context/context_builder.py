"""
ShadBot Agent Platform

Execution context builder.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from agentplatform.domain.context.execution_context import (
    AgentExecutionContext,
)


class ExecutionContextBuilder:
    """
    Builds execution context objects.
    """

    def build(
        self,
        project_id: UUID,
        task_id: UUID,
        instructions: str,
        intelligence_context: dict[str, Any],
    ) -> AgentExecutionContext:
        """
        Create execution context.
        """

        return AgentExecutionContext(
            project_id=project_id,
            task_id=task_id,
            instructions=instructions,
            intelligence_context=intelligence_context,
        )
