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
from projectintelligence.domain.resume.project_state import (
    ProjectState,
)


@dataclass(slots=True)
class StateStorageService:
    """
    Coordinates persistence of project intelligence state.
    """

    repository: StateRepository

    def save(
        self,
        state: ProjectState,
    ) -> PersistenceResult:
        self.repository.save(
            state,
        )

        return PersistenceResult.succeeded(
            operation="save",
            entity="ProjectState",
            identifier=None,
            message="Project intelligence state stored successfully.",
        )
