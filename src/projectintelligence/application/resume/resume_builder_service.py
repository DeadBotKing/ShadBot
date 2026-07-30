"""
ShadBot Project Intelligence

Resume Builder Service
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

from projectintelligence.application.resume.completion_analyzer import (
    CompletionAnalyzer,
)
from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.application.resume.pending_task_analyzer import (
    PendingTaskAnalyzer,
)
from projectintelligence.application.resume.project_summary_builder import (
    ProjectSummaryBuilder,
)
from projectintelligence.application.resume.recommendation_engine import (
    RecommendationEngine,
)
from projectintelligence.application.state.builders.project_state_builder import (
    ProjectStateBuilder,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)
from projectintelligence.domain.resume.resume_metadata import (
    ResumeMetadata,
)


@dataclass(slots=True)
class ResumeBuilderService:
    """
    Builds complete ProjectResume aggregate.

    This service coordinates resume generation
    from intelligence artifacts.
    """

    completion_analyzer: CompletionAnalyzer

    pending_task_analyzer: PendingTaskAnalyzer

    recommendation_engine: RecommendationEngine

    project_state_builder: ProjectStateBuilder

    summary_builder: ProjectSummaryBuilder

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

        state = self.project_state_builder.build(context)

        summary = self.summary_builder.build(
            context,
        )

        return ProjectResume(
            project_id=context.snapshot.project_id,
            metadata=ResumeMetadata(
                resume_id=uuid4(),
                snapshot_id=context.snapshot.snapshot_id,
                generated_at=datetime.now(timezone.utc),
                generator_version="1.0",
            ),
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
