"""
ShadBot Project Intelligence

Resume Generator
"""

from __future__ import annotations

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
from projectintelligence.application.resume.project_state_analyzer import (
    ProjectStateAnalyzer,
)
from projectintelligence.application.resume.project_summary_builder import (
    ProjectSummaryBuilder,
)
from projectintelligence.application.resume.recommendation_engine import (
    RecommendationEngine,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)
from projectintelligence.domain.resume.project_state import (
    ProjectState,
)
from projectintelligence.domain.resume.resume_metadata import (
    ResumeMetadata,
)


class ResumeGenerator:
    """
    Generates complete project resume artifacts.
    """

    def __init__(
        self,
        summary_builder: ProjectSummaryBuilder,
        completion_analyzer: CompletionAnalyzer,
        pending_task_analyzer: PendingTaskAnalyzer,
        recommendation_engine: RecommendationEngine,
        project_state_analyzer: ProjectStateAnalyzer,
    ) -> None:

        self.summary_builder = summary_builder
        self.completion_analyzer = completion_analyzer
        self.pending_task_analyzer = pending_task_analyzer
        self.recommendation_engine = recommendation_engine
        self.project_state_analyzer = project_state_analyzer

    def generate(
        self,
        context: ResumeBuildContext,
    ) -> ProjectResume:
        """
        Generate a complete project resume.
        """

        state_analysis = self.project_state_analyzer.analyze(
            context,
        )

        state = ProjectState(
            current_phase=state_analysis["phase"],
            current_sub_phase=state_analysis["status"],
            architecture_version=context.context.version,
            completed_components=len(
                state_analysis["completed_areas"],
            ),
            pending_components=len(
                state_analysis["pending_areas"],
            ),
            total_components=(
                len(state_analysis["completed_areas"])
                +
                len(state_analysis["pending_areas"])
            ),
            completion_percentage=state_analysis[
                "completion_percentage"
            ],
        )

        return ProjectResume(
            project_id=context.snapshot.project_id,
            metadata=ResumeMetadata(
                resume_id=uuid4(),
                snapshot_id=context.snapshot.snapshot_id,
                generated_at=lambda: datetime.now(timezone.utc),
                generator_version="1.0",
            ),
            state=state,
            summary=self.summary_builder.build(
                context,
            ),
            completed_work=tuple(
                self.completion_analyzer.analyze(
                    context,
                ),
            ),
            pending_work=tuple(
                self.pending_task_analyzer.analyze(
                    context,
                ),
            ),
            recommendations=tuple(
                self.recommendation_engine.generate(
                    context,
                ),
            ),
        )