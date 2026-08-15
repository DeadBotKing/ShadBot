"""
ShadBot Agent Platform

Agent execution context factory.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.application.context.project_intelligence_adapter import (
    ProjectIntelligenceAdapter,
)
from agentplatform.application.memory import MemoryService
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.tasks import AgentTask
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class AgentContextFactory:
    """
    Creates AgentExecutionContext instances
    enriched with Project Intelligence data.
    """

    def __init__(
        self,
        adapter: ProjectIntelligenceAdapter | None = None,
        memory_service: MemoryService | None = None,
    ) -> None:
        self._adapter = adapter or ProjectIntelligenceAdapter()
        self._memory_service = memory_service

    def create(
        self,
        project_id: UUID,
        task: AgentTask,
        package: AgentContextPackage | None = None,
        instructions: str = "",
        metadata: dict[str, object] | None = None,
    ) -> AgentExecutionContext:
        """
        Build execution context for agents.
        """

        intelligence_context: dict[str, object] = {}

        memory_context: list[dict[str, object]] = []

        if self._memory_service:
            memories = self._memory_service.recall(
                project_id,
            )

            memory_context = [
                {
                    "content": memory.content,
                    "source": memory.source,
                    "confidence": memory.confidence,
                }
                for memory in memories
            ]

        if package:
            intelligence_context = self._adapter.convert(
                package,
            )

            intelligence_context["agent_memory"] = memory_context
        else:
            intelligence_context = {
                "agent_memory": memory_context,
            }

        return AgentExecutionContext(
            project_id=project_id,
            task_id=task.id,
            instructions=instructions,
            intelligence_context=intelligence_context,
            metadata=metadata or {},
            task_title=task.title,
            task_description=task.description,
            task_type=task.task_type.value,
        )
