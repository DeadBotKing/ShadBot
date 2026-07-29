"""
ShadBot Project Intelligence

Project State Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.application.state.builders.project_state_builder import (
    ProjectStateBuilder,
)
from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)


@dataclass(slots=True)
class ProjectStateService:
    """
    Produces the high-level project state from intelligence artifacts.
    """

    builder: ProjectStateBuilder

    def build(
        self,
        context: ResumeBuildContext,
    ) -> ProjectIntelligenceState:
        """
        Build the current Project Intelligence state.
        """

        return self.builder.build(
            context,
        )
