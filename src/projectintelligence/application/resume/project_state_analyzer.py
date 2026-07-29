"""
ShadBot Project Intelligence

Project State Analyzer
"""

from __future__ import annotations

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)


class ProjectStateAnalyzer:
    """
    Analyzes the current project state for resume generation.
    """

    def analyze(
        self,
        context: ResumeBuildContext,
    ) -> dict[str, object]:
        """
        Produce a high-level project state analysis.
        """

        completed_areas: list[str] = []

        pending_areas: list[str] = []

        if context.snapshot.detected_languages:
            completed_areas.append(
                "Language Analysis",
            )
        else:
            pending_areas.append(
                "Language Analysis",
            )

        if context.snapshot.detected_frameworks:
            completed_areas.append(
                "Framework Analysis",
            )
        else:
            pending_areas.append(
                "Framework Analysis",
            )

        if context.knowledge.dependency_map:
            completed_areas.append(
                "Dependency Analysis",
            )
        else:
            pending_areas.append(
                "Dependency Analysis",
            )

        if context.knowledge.architecture_patterns:
            completed_areas.append(
                "Architecture Analysis",
            )
        else:
            pending_areas.append(
                "Architecture Analysis",
            )

        if context.history.differences:
            completed_areas.append(
                "Evolution Tracking",
            )
        else:
            pending_areas.append(
                "Evolution Tracking",
            )

        completion_percentage = (
            len(completed_areas) / (len(completed_areas) + len(pending_areas)) * 100
            if completed_areas or pending_areas
            else 0.0
        )

        return {
            "completed_areas": completed_areas,
            "pending_areas": pending_areas,
            "completion_percentage": completion_percentage,
            "phase": "Project Intelligence Engine",
            "status": ("Active" if pending_areas else "Complete"),
        }
