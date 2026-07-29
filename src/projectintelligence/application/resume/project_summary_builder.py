"""
ShadBot Project Intelligence

Project Summary Builder
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.domain.resume.project_summary import (
    ProjectSummary,
)


@dataclass(slots=True)
class ProjectSummaryBuilder:
    """
    Builds a human and AI readable project summary.
    """

    def build(
        self,
        context: ResumeBuildContext,
    ) -> ProjectSummary:
        """
        Build project summary from intelligence context.
        """

        snapshot = context.snapshot
        knowledge = context.knowledge
        history = context.history

        title = (
            snapshot.workspace.name if snapshot.workspace.name else "Unknown Project"
        )

        overview = (
            f"Project contains {snapshot.file_count} files "
            f"using technologies: "
            f"{', '.join(knowledge.technologies)}."
        )

        architecture_summary = (
            knowledge.architecture_description
            or "No architecture description available."
        )

        if knowledge.architecture_patterns:
            architecture_summary += (
                " Patterns: "
                + ", ".join(
                    knowledge.architecture_patterns,
                )
                + "."
            )

        current_focus = (
            knowledge.intelligence_notes[0]
            if knowledge.intelligence_notes
            else "Project analysis completed."
        )

        latest_changes = (
            "; ".join(history.differences)
            if history.differences
            else "No historical changes available."
        )

        next_goal = (
            knowledge.known_constraints[0]
            if knowledge.known_constraints
            else "Continue project evolution."
        )

        return ProjectSummary(
            title=title,
            overview=overview,
            architecture_summary=architecture_summary,
            current_focus=current_focus,
            latest_changes=latest_changes,
            next_goal=next_goal,
        )
