"""
ShadBot Project Intelligence

Agent Context Builder
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.evolution.project_evolution import (
    ProjectEvolution,
)
from projectintelligence.domain.handoff.agent_context_metadata import (
    AgentContextMetadata,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)
from projectintelligence.domain.handoff.evolution_summary import (
    EvolutionSummary,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
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
        evolution: ProjectEvolution | None = None,
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

        current_state = resume.state.current_phase if resume else None

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

        evolution_summary = None

        if evolution:
            added_files: list[str] = []
            removed_files: list[str] = []
            modified_files: list[str] = []
            recent_changes: list[str] = []

            for change in evolution.changes:
                recent_changes.append(
                    change.description,
                )

                if change.change_type.value == "added":
                    added_files.append(
                        change.path,
                    )

                elif change.change_type.value == "removed":
                    removed_files.append(
                        change.path,
                    )

                elif change.change_type.value in (
                    "modified",
                    "renamed",
                    "moved",
                ):
                    modified_files.append(
                        change.path,
                    )

            evolution_summary = EvolutionSummary(
                recent_changes=tuple(
                    recent_changes,
                ),
                added_files=tuple(
                    added_files,
                ),
                removed_files=tuple(
                    removed_files,
                ),
                modified_files=tuple(
                    modified_files,
                ),
                impact_summary=(f"{len(evolution.changes)} project changes detected."),
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
            architecture_description=(knowledge.architecture_description),
            conventions=tuple(
                knowledge.project_conventions,
            ),
            constraints=tuple(
                knowledge.known_constraints,
            ),
            recommendations=recommendations,
            current_state=current_state,
            metadata=metadata,
            evolution=evolution_summary,
        )
