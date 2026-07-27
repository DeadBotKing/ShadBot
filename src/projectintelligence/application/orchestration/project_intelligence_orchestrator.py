"""
ShadBot Project Intelligence

Project Intelligence Orchestrator
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.persistence.services.persistence_service import (
    PersistenceService,
)
from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)
from projectintelligence.application.pipeline.project_intelligence_pipeline import (
    ProjectIntelligencePipeline,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


@dataclass(slots=True)
class ProjectIntelligenceOrchestrator:
    """
    Coordinates the complete Project Intelligence workflow.
    """

    pipeline: ProjectIntelligencePipeline

    persistence_service: PersistenceService

    def execute(
        self,
        project: ProjectEntity,
    ) -> PipelineResult:

        result = self.pipeline.run(
            project,
        )

        self.persistence_service.save_all(
            snapshot=result.snapshot,
            context=result.context,
        )

        return result
