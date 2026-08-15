"""
ShadBot Project Intelligence

In Memory Agent Context Repository
"""

from __future__ import annotations

from uuid import UUID, uuid4

from projectintelligence.application.handoff.contracts.agent_context_repository import (
    IAgentContextRepository,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class InMemoryAgentContextRepository(
    IAgentContextRepository,
):
    """
    In-memory implementation for agent context persistence.
    """

    def __init__(self) -> None:
        self._contexts: dict[
            UUID,
            AgentContextPackage,
        ] = {}

        self._project_index: dict[
            UUID,
            list[UUID],
        ] = {}

    def save(
        self,
        context: AgentContextPackage,
    ) -> None:
        """
        Store an agent context package.
        """

        context_id = uuid4()

        self._contexts[context_id] = context

        if context.project_id not in self._project_index:
            self._project_index[context.project_id] = []

        self._project_index[context.project_id].append(
            context_id,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Retrieve the latest agent context package
        for a project.
        """

        context_ids = self._project_index.get(
            project_id,
            [],
        )

        if not context_ids:
            return None

        return self._contexts.get(
            context_ids[-1],
        )

    def get_by_id(
        self,
        context_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Retrieve an agent context package by identifier.
        """

        return self._contexts.get(
            context_id,
        )
