"""
ShadBot Project Intelligence

Resume Builder Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)


@dataclass(slots=True)
class ResumeBuilderService:
    """
    Builds complete ProjectResume aggregate.

    This service coordinates resume generation
    from intelligence artifacts.
    """

    completion_analyzer: object

    pending_task_analyzer: object

    recommendation_engine: object

    project_state_analyzer: object

    summary_builder: object

    def build(
        self,
        context: ResumeBuildContext,
    ) -> ProjectResume:
        """
        Build complete project resume.
        """

        completed_work = self.completion_analyzer.analyze(
            context,
        )

        pending_work = self.pending_task_analyzer.analyze(
            context,
        )

        recommendations = self.recommendation_engine.generate(
            context,
        )

        state = self.project_state_analyzer.analyze(
            context,
        )

        summary = self.summary_builder.build(
            context,
        )

        return ProjectResume(
            project_id=context.snapshot.project_id,
            metadata=context.metadata,
            state=state,
            summary=summary,
            completed_work=tuple(
                completed_work,
            ),
            pending_work=tuple(
                pending_work,
            ),
            recommendations=tuple(
                recommendations,
            ),
        )
