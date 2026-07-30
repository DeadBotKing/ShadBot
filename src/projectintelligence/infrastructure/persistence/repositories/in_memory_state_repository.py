"""
ShadBot Project Intelligence

In Memory State Repository
"""

from __future__ import annotations

from uuid import UUID, uuid4

from projectintelligence.application.ports.outbound.state_repository import (
    StateRepository,
)
from projectintelligence.domain.resume.project_state import (
    ProjectState,
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
            ProjectState,
        ] = {}

    def save(
        self,
        state: ProjectState,
    ) -> None:

        state_id = uuid4()

        self._storage[state_id] = state

    def update(
        self,
        state: ProjectState,
    ) -> None:

        for state_id, stored_state in self._storage.items():
            if stored_state == state:
                self._storage[state_id] = state
                return

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
    ) -> ProjectState | None:

        return self._storage.get(
            state_id,
        )

    def list_all(
        self,
    ) -> list[ProjectState]:

        return list(
            self._storage.values(),
        )

    def count(
        self,
    ) -> int:

        return len(
            self._storage,
        )
