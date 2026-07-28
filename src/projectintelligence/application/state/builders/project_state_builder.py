"""
ShadBot Project Intelligence

Project State Builder
"""

from __future__ import annotations

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)


class ProjectStateBuilder:
    """
    Builds the Project Intelligence State from the available
    project intelligence artifacts.
    """

    def build(
        self,
        context: ResumeBuildContext,
    ) -> ProjectIntelligenceState:
        """
        Build the high-level project state.

        This method is intentionally left unimplemented until
        the complete PipelineResult exposes every required
        intelligence artifact.
        """

        raise NotImplementedError(
            "ProjectStateBuilder has not been implemented yet."
        )