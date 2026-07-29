"""
ShadBot Project Intelligence

In Memory State Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.application.ports.outbound.state_repository import (
    StateRepository,
)
from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)


class InMemoryStateRepository(
    StateRepository,
):
    """
    In-memory implementation of project intelligence state persistence.
    """

    def __init__(self) -> None:
        self._storage: dict[
            UUID,
            ProjectIntelligenceState,
        ] = {}

    def save(
        self,
        state: ProjectIntelligenceState,
    ) -> None:
        self._storage[
            state.state_id
        ] = state

    def update(
        self,
        state: ProjectIntelligenceState,
    ) -> None:
        self._storage[
            state.state_id
        ] = state

    def delete(
        self,
        state_id: UUID,
    ) -> None:
        self._storage.pop(
            state_id,
            None,
        )

    def exists(
        self,
        state_id: UUID,
    ) -> bool:
        return state_id in self._storage

    def get_by_id(
        self,
        state_id: UUID,
    ) -> ProjectIntelligenceState | None:
        return self._storage.get(
            state_id,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectIntelligenceState | None:

        states = [
            state
            for state in self._storage.values()
            if state.project_id == project_id
        ]

        if not states:
            return None

        return max(
            states,
            key=lambda item: item.created_at,
        )

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectIntelligenceState]:

        return [
            state
            for state in self._storage.values()
            if state.project_id == project_id
        ]

    def count(
        self,
        project_id: UUID,
    ) -> int:

        return len(
            self.list_by_project(
                project_id,
            ),
        )