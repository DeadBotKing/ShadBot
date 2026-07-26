"""
ShadBot Project Intelligence

Knowledge Builder
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.knowledge.architecture_context_builder import (
    ArchitectureContextBuilder,
)
from projectintelligence.application.knowledge.change_context_builder import (
    ChangeContextBuilder,
)
from projectintelligence.application.knowledge.dependency_context_builder import (
    DependencyContextBuilder,
)
from projectintelligence.application.knowledge.technology_context_builder import (
    TechnologyContextBuilder,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.application.git.models.git_context import (
    GitContext,
)


@dataclass(slots=True)
class KnowledgeBuilder:
    """
    Builds a unified ProjectContext from a ProjectSnapshot.
    """

    architecture_builder: ArchitectureContextBuilder

    technology_builder: TechnologyContextBuilder

    dependency_builder: DependencyContextBuilder

    change_builder: ChangeContextBuilder

    def build(
        self,
        snapshot: ProjectSnapshot,
        git_context: GitContext,
    ) -> ProjectContext:
        """
        Build unified project context.
        """

        return ProjectContext(
            project_id=snapshot.project_id,
            architecture_context=self.architecture_builder.build(
                snapshot,
            ),
            technology_context=self.technology_builder.build(
                snapshot,
            ),
            dependency_context=self.dependency_builder.build(
                snapshot,
            ),
            change_context=self.change_builder.build(
                snapshot,
                git_context,
            ),
        )
