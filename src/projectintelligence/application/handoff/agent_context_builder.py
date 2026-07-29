"""
ShadBot Project Intelligence

Agent Context Builder
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime, timezone

from projectintelligence.application.git.models.git_context import (
    GitContext,
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
from projectintelligence.domain.handoff.agent_context_metadata import (
    AgentContextMetadata,
)


@dataclass(slots=True)
class AgentContextBuilder:
    """
    Builds stable context packages for Agent Platform.

    This class translates internal Project Intelligence
    artifacts into an external agent consumption model.
    """

    def build(
        self,
        knowledge: ProjectKnowledge,
        context: ProjectContext,
        resume: ProjectResume | None = None,
        git_context: GitContext | None = None,
    ) -> AgentContextPackage:
        """
        Build an agent-ready context package.
        """

        summary = (
            resume.summary.overview
            if resume
            else (
                knowledge.architecture_description
                or "Project intelligence analysis completed."
            )
        )

        current_state = (
            resume.state.current_phase
            if resume
            else None
        )

        recommendations = (
            tuple(resume.recommendations)
            if resume
            and isinstance(
                resume.recommendations,
                tuple | list,
            )
            else tuple()
        )

        metadata = AgentContextMetadata(
            context_id=uuid4(),
            version="1.0",
            created_at=datetime.now(timezone.utc),
        )

        return AgentContextPackage(
            project_id=knowledge.project_id,
            summary=summary,
            technologies=tuple(
                knowledge.technologies,
            ),
            frameworks=tuple(
                knowledge.frameworks,
            ),
            languages=tuple(
                knowledge.languages,
            ),
            dependencies=dict(
                knowledge.dependency_map,
            ),
            architecture_description=(
                knowledge.architecture_description
            ),
            conventions=tuple(
                knowledge.project_conventions,
            ),
            constraints=tuple(
                knowledge.known_constraints,
            ),
            recommendations=recommendations,
            current_state=current_state,
            metadata=metadata,
        )