"""
ShadBot Project Intelligence

Agent Context Repository Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


class IAgentContextRepository(ABC):
    """
    Contract for storing and retrieving agent context packages.

    Application layer depends only on this abstraction.
    Infrastructure provides concrete implementations.
    """

    @abstractmethod
    def save(
        self,
        context: AgentContextPackage,
    ) -> None:
        """
        Store an agent context package.
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest(
        self,
        project_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Retrieve the latest agent context package
        for a project.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        context_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Retrieve an agent context package by identifier.
        """
        raise NotImplementedError
