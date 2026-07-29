"""
ShadBot Project Intelligence

Agent Context Service
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.application.handoff.agent_context_builder import (
    AgentContextBuilder,
)
from projectintelligence.application.handoff.contracts.agent_context_repository import (
    IAgentContextRepository,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


@dataclass(slots=True)
class AgentContextService:
    """
    Application service responsible for managing
    agent handoff contexts.
    """

    builder: AgentContextBuilder

    repository: IAgentContextRepository

    def build_and_store(
        self,
        knowledge: ProjectKnowledge,
        context: ProjectContext,
        resume: ProjectResume | None = None,
        git_context: GitContext | None = None,
    ) -> AgentContextPackage:
        """
        Build an agent context package and persist it.
        """

        package = self.builder.build(
            knowledge=knowledge,
            context=context,
            resume=resume,
            git_context=git_context,
        )

        self.repository.save(
            package,
        )

        return package

    def get_latest(
        self,
        project_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Retrieve latest agent context package.
        """

        return self.repository.get_latest(
            project_id,
        )

    def get_by_id(
        self,
        context_id: UUID,
    ) -> AgentContextPackage | None:
        """
        Retrieve agent context package by identifier.
        """

        return self.repository.get_by_id(
            context_id,
        )