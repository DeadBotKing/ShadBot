"""
ShadBot Project Intelligence

Project Context Repository Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.context.project_context import (
    ProjectContext,
)


class IContextRepository(ABC):
    """
    Contract for Project Context persistence.
    """

    @abstractmethod
    def save(
        self,
        context: ProjectContext,
    ) -> None:
        """
        Persist project context.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        context_id: UUID,
    ) -> ProjectContext | None:
        """
        Retrieve context by id.
        """
        raise NotImplementedError