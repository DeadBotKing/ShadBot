"""
ShadBot Project Intelligence

State Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)


class StateRepository(ABC):
    """
    Outbound port for persisting and retrieving project intelligence state.
    """

    @abstractmethod
    def save(
        self,
        state: ProjectIntelligenceState,
    ) -> None:
        """
        Persist project intelligence state.
        """

    @abstractmethod
    def update(
        self,
        state: ProjectIntelligenceState,
    ) -> None:
        """
        Update existing project intelligence state.
        """

    @abstractmethod
    def delete(
        self,
        state_id: UUID,
    ) -> None:
        """
        Delete project intelligence state.
        """

    @abstractmethod
    def exists(
        self,
        state_id: UUID,
    ) -> bool:
        """
        Check whether state exists.
        """

    @abstractmethod
    def get_by_id(
        self,
        state_id: UUID,
    ) -> ProjectIntelligenceState | None:
        """
        Retrieve state by identifier.
        """

    @abstractmethod
    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectIntelligenceState | None:
        """
        Retrieve latest state of a project.
        """

    @abstractmethod
    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectIntelligenceState]:
        """
        Retrieve all states of a project.
        """

    @abstractmethod
    def count(
        self,
        project_id: UUID,
    ) -> int:
        """
        Count stored states of a project.
        """