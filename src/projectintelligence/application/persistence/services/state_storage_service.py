"""
ShadBot Project Intelligence

State Storage Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.ports.outbound.state_repository import (
    StateRepository,
)
from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)


@dataclass(slots=True)
class StateStorageService:
    """
    Coordinates persistence of project intelligence state.
    """

    repository: StateRepository

    def save(
        self,
        state: ProjectIntelligenceState,
    ) -> PersistenceResult:
        self.repository.save(
            state,
        )

        return PersistenceResult.succeeded(
            operation="save",
            entity="ProjectIntelligenceState",
            identifier=str(state.state_id),
            message="Project intelligence state stored successfully.",
        )
