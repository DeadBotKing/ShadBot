"""
ShadBot Project Intelligence

In Memory Agent Context Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class InMemoryAgentContextRepository:
    """
    In-memory storage implementation for agent contexts.
    """

    def __init__(self) -> None:
        self._contexts: dict[UUID, list[AgentContextPackage]] = {}

    def save(
        self,
        context: AgentContextPackage,
    ) -> None:
        """
        Store an agent context package.
        """

        if context.project_id not in self._contexts:
            self._contexts[context.project_id] = []

        self._contexts[context.project_id].append(
            context,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Return the latest stored context for a project.
        """

        contexts = self._contexts.get(
            project_id,
            [],
        )

        if not contexts:
            return None

        return contexts[-1]

    def get_by_id(
        self,
        context_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Find a context package by id.

        Note:
        Current domain model does not expose a dedicated
        context_id, therefore lookup is not supported yet.
        """

        return None
