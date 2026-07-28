"""
ShadBot Project Intelligence

Project State Service
"""

from __future__ import annotations

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)


class ProjectStateService:
    """
    Produces the high-level project state from the available
    Project Intelligence context.
    """

    def build(
        self,
        context: ResumeBuildContext,
    ) -> ProjectIntelligenceState:
        """
        Build the current Project Intelligence state.
        """

        raise NotImplementedError(
            "Project state analysis has not been implemented yet."
        )