"""
ShadBot Agent Platform

Brain memory integration.
"""

from __future__ import annotations

from agentplatform.application.memory import (
    MemoryContextBuilder,
    MemoryService,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)


class BrainMemory:
    """
    Provides persistent memory context
    for agent reasoning.
    """

    def __init__(
        self,
        memory_service: MemoryService,
        context_builder: MemoryContextBuilder | None = None,
    ) -> None:

        self._memory_service = memory_service
        self._context_builder = context_builder or MemoryContextBuilder()

    def retrieve(
        self,
        context: AgentExecutionContext,
    ) -> dict[str, object]:
        """
        Load project memories.
        """

        memories = self._memory_service.recall(
            context.project_id,
        )

        return self._context_builder.build(
            memories,
        )
