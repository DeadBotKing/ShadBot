"""
ShadBot Project Intelligence

Agent Context Storage Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.handoff.contracts.agent_context_repository import (
    IAgentContextRepository,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


@dataclass(slots=True)
class AgentContextStorageService:
    """
    Coordinates persistence operations for agent contexts.
    """

    repository: IAgentContextRepository

    def save(
        self,
        context: AgentContextPackage,
    ) -> PersistenceResult:
        """
        Persist an agent context package.
        """

        self.repository.save(
            context,
        )

        return PersistenceResult(
            success=True,
        )