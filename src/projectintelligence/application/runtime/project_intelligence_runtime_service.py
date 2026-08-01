"""
ShadBot Project Intelligence

Project Intelligence Runtime Service
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.package.package_generation_service import (
    PackageGenerationService,
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
from projectintelligence.package.package_manifest import (
    PackageManifest,
)
from projectintelligence.package.package_metadata import (
    PackageMetadata,
)


class ProjectIntelligenceRuntimeService:
    """
    Executes Project Intelligence runtime flow.
    """

    def __init__(
        self,
        pipeline: ProjectIntelligencePipeline,
        package_service: PackageGenerationService,
    ) -> None:
        self._pipeline = pipeline
        self._package_service = package_service

    def execute(
        self,
        project: ProjectEntity,
        output_directory: Path,
    ) -> PipelineResult:
        """
        Execute intelligence analysis and generate package.
        """

        result = self._pipeline.run(
            project,
        )

        metadata = PackageMetadata(
            project_id=project.project_id,
            project_name=project.name,
        )

        self._package_service.generate(
            output_directory=output_directory,
            metadata=metadata,
            manifest=PackageManifest(),
        )

        return result
