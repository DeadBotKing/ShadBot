"""
ShadBot Agent Platform

Brain memory integration.
"""

from __future__ import annotations

from agentplatform.application.memory import (
    MemoryService,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)


class BrainMemory:
    """
    Provides memory access for agent reasoning.
    """

    def __init__(
        self,
        memory_service: MemoryService,
    ) -> None:
        self._memory_service = memory_service

    def retrieve(
        self,
        context: AgentExecutionContext,
    ) -> dict[str, object]:
        """
        Retrieve relevant project memory.
        """

        memories = self._memory_service.recall(
            context.project_id,
        )

        return {
            "memories": [memory.content for memory in memories],
        }
