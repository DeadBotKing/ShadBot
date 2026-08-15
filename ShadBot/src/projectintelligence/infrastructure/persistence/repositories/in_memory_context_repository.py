"""
ShadBot Project Intelligence

In Memory Context Repository
"""

from __future__ import annotations

from uuid import UUID

from projectintelligence.application.ports.outbound.context_repository import (
    ContextRepository,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)


class InMemoryContextRepository(
    ContextRepository,
):
    """
    In-memory implementation of context persistence.
    """

    def __init__(self) -> None:
        self._storage: dict[
            UUID,
            ProjectContext,
        ] = {}

    def save(
        self,
        context: ProjectContext,
    ) -> None:
        self._storage[context.context_id] = context

    def update(
        self,
        context: ProjectContext,
    ) -> None:
        self._storage[context.context_id] = context

    def delete(
        self,
        context_id: UUID,
    ) -> None:
        self._storage.pop(
            context_id,
            None,
        )

    def exists(
        self,
        context_id: UUID,
    ) -> bool:
        return context_id in self._storage

    def get_by_id(
        self,
        context_id: UUID,
    ) -> ProjectContext | None:
        return self._storage.get(
            context_id,
        )

    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectContext | None:

        contexts = [
            context
            for context in self._storage.values()
            if context.project_id == project_id
        ]

        if not contexts:
            return None

        return max(
            contexts,
            key=lambda item: item.created_at,
        )

    def get_by_snapshot(
        self,
        snapshot_id: UUID,
    ) -> ProjectContext | None:

        for context in self._storage.values():
            if context.snapshot_id == snapshot_id:
                return context

        return None

    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectContext]:

        return [
            context
            for context in self._storage.values()
            if context.project_id == project_id
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
