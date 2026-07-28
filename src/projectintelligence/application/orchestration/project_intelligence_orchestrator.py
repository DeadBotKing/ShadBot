"""
ShadBot Project Intelligence

Project Intelligence Orchestrator
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.runtime_result import (
    RuntimeResult,
)
from projectintelligence.application.persistence.services.persistence_service import (
    PersistenceService,
)
from projectintelligence.application.persistence.services.snapshot_history_service import (
    SnapshotHistoryService,
)
from projectintelligence.application.pipeline.project_intelligence_pipeline import (
    ProjectIntelligencePipeline,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)

from projectintelligence.application.resume.resume_generator import (
    ResumeGenerator,
)


@dataclass(slots=True)
class ProjectIntelligenceOrchestrator:
    """
    Coordinates the complete Project Intelligence workflow.
    """

    pipeline: ProjectIntelligencePipeline

    persistence_service: PersistenceService

    snapshot_history_service: SnapshotHistoryService

    resume_generator: ResumeGenerator

    def execute(
        self,
        project: ProjectEntity,
    ) -> RuntimeResult:

        previous_snapshot = self.snapshot_history_service.get_latest_snapshot(
            project.project_id,
        )

        pipeline_result = self.pipeline.run(
            project,
        )

        resume_context = ResumeBuildContext(
            snapshot=pipeline_result.snapshot,
            knowledge=pipeline_result.knowledge,
            history=pipeline_result.history,
            context=pipeline_result.context,
        )

        pipeline_result.resume = self.resume_generator.generate(
            resume_context,
        )

        self.persistence_service.save_all(
            snapshot=pipeline_result.snapshot,
            knowledge=pipeline_result.knowledge,
            history=pipeline_result.history,
            state=pipeline_result.state,
            context=pipeline_result.context,
            resume=pipeline_result.resume,
        )

        return RuntimeResult(
            pipeline_result=pipeline_result,
            previous_snapshot=previous_snapshot,
        )
