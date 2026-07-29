"""
ShadBot Project Intelligence

Knowledge Repository Port
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)


class KnowledgeRepository(ABC):
    """
    Outbound port for persisting and retrieving project knowledge.

    Implementations may use SQL Server, SQLite, JSON,
    or any other persistence technology.
    """

    @abstractmethod
    def save(
        self,
        knowledge: ProjectKnowledge,
    ) -> None:
        """
        Persist project knowledge.
        """

    @abstractmethod
    def update(
        self,
        knowledge: ProjectKnowledge,
    ) -> None:
        """
        Update existing project knowledge.
        """

    @abstractmethod
    def delete(
        self,
        knowledge_id: UUID,
    ) -> None:
        """
        Delete project knowledge.
        """

    @abstractmethod
    def exists(
        self,
        knowledge_id: UUID,
    ) -> bool:
        """
        Check whether knowledge exists.
        """

    @abstractmethod
    def get_by_id(
        self,
        knowledge_id: UUID,
    ) -> ProjectKnowledge | None:
        """
        Retrieve knowledge by identifier.
        """

    @abstractmethod
    def get_latest(
        self,
        project_id: UUID,
    ) -> ProjectKnowledge | None:
        """
        Retrieve latest knowledge snapshot of a project.
        """

    @abstractmethod
    def list_by_project(
        self,
        project_id: UUID,
    ) -> list[ProjectKnowledge]:
        """
        Retrieve all knowledge versions of a project.
        """

    @abstractmethod
    def count(
        self,
        project_id: UUID,
    ) -> int:
        """
        Count knowledge versions for a project.
        """
