"""
ShadBot Project Intelligence

Context Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.context.project_context import (
    ProjectContext,
)


class ContextRepository(ABC):
    """
    Outbound port for persisting and retrieving project contexts.

    This contract is implemented by infrastructure adapters
    while remaining completely independent from any persistence
    technology.
    """

    @abstractmethod
    def save(self, context: ProjectContext) -> None:
        """Persist a new project context."""

    @abstractmethod
    def update(self, context: ProjectContext) -> None:
        """Update an existing project context."""

    @abstractmethod
    def delete(self, context_id: UUID) -> None:
        """Delete a project context."""

    @abstractmethod
    def exists(self, context_id: UUID) -> bool:
        """Return True if the context exists."""

    @abstractmethod
    def get_by_id(self, context_id: UUID) -> ProjectContext | None:
        """Retrieve a context by its unique identifier."""

    @abstractmethod
    def get_latest(self, project_id: UUID) -> ProjectContext | None:
        """Retrieve the latest context for a project."""

    @abstractmethod
    def get_by_snapshot(
        self,
        snapshot_id: UUID,
    ) -> ProjectContext | None:
        """Retrieve the context generated from a snapshot."""

    @abstractmethod
    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectContext]:
        """Return all contexts belonging to a project."""

    @abstractmethod
    def count(self, project_id: UUID) -> int:
        """Return the number of contexts for a project."""
