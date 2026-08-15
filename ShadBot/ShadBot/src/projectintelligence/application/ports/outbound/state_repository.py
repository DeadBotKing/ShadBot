"""
ShadBot Project Intelligence

State Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.resume.project_state import (
    ProjectState,
)


class StateRepository(ABC):
    """
    Outbound port for persisting project intelligence state.
    """

    @abstractmethod
    def save(
        self,
        state: ProjectState,
    ) -> None:
        """
        Persist project intelligence state.
        """

    @abstractmethod
    def update(
        self,
        state: ProjectState,
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
    ) -> ProjectState | None:
        """
        Retrieve state by identifier.
        """

    @abstractmethod
    def list_all(
        self,
    ) -> list[ProjectState]:
        """
        Retrieve all stored states.
        """

    @abstractmethod
    def count(
        self,
    ) -> int:
        """
        Count stored states.
        """
