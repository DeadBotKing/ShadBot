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
    Builds the Project Intelligence State from project artifacts.
    """

    def build(
        self,
        context: ResumeBuildContext,
    ) -> ProjectIntelligenceState:
        """
        Build the current project intelligence state.
        """

        completed_components = self._calculate_completed_components(
            context,
        )

        total_components = self._calculate_total_components(
            context,
        )

        pending_components = (
            total_components - completed_components
        )

        completion_percentage = 0.0

        if total_components > 0:
            completion_percentage = (
                completed_components / total_components
            ) * 100

        return ProjectIntelligenceState(
            current_phase="Project Intelligence Engine",
            current_sub_phase="Analysis Pipeline",
            architecture_version=context.context.version,
            completed_components=completed_components,
            pending_components=pending_components,
            total_components=total_components,
            completion_percentage=completion_percentage,
        )

    def _calculate_completed_components(
        self,
        context: ResumeBuildContext,
    ) -> int:
        """
        Estimate completed project intelligence components.
        """

        completed = 0

        if context.snapshot.detected_languages:
            completed += 1

        if context.snapshot.detected_frameworks:
            completed += 1

        if context.knowledge.dependency_map:
            completed += 1

        if context.knowledge.architecture_patterns:
            completed += 1

        if context.history.differences:
            completed += 1

        return completed

    def _calculate_total_components(
        self,
        context: ResumeBuildContext,
    ) -> int:
        """
        Total measurable intelligence components.
        """

        return 5