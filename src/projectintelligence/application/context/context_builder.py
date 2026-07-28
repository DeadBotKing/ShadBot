"""
ShadBot Project Intelligence

Context Builder
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


@dataclass(slots=True)
class ContextBuilder:
    """
    Builds a ProjectContext from ProjectKnowledge and Git analysis.
    """

    def build(
        self,
        snapshot: ProjectSnapshot,
        knowledge: ProjectKnowledge,
        git_context: GitContext,
    ) -> ProjectContext:
        """
        Build the runtime project context.
        """

        return ProjectContext(
            project_id=snapshot.project_id,
            snapshot_id=snapshot.snapshot_id,
            architecture_context=knowledge.architecture_patterns.copy(),
            technology_context=(
                knowledge.technologies
                + knowledge.frameworks
                + knowledge.languages
            ),
            dependency_context=list(
                knowledge.dependency_map.keys(),
            ),
            change_context=knowledge.historical_changes.copy(),
            constraint_context=knowledge.known_constraints.copy(),
            git_state=None,
        )