"""
ShadBot Project Intelligence

Project Scanner Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.pipelines.project_scanner_pipeline import (
    ProjectScannerPipeline,
)
from projectintelligence.domain.project.project_entity import ProjectEntity
from projectintelligence.domain.snapshot.project_snapshot import ProjectSnapshot


@dataclass(slots=True)
class ProjectScannerService:
    """
    Orchestrates the project scanning workflow.

    This service coordinates all scanning components through their
    contracts without containing scanning logic itself.
    """

    pipeline: ProjectScannerPipeline

    def scan(
        self,
        project: ProjectEntity,
    ) -> ProjectSnapshot:
        """
        Execute the project scanning pipeline.
        """

        workspace_entries = self.pipeline.workspace_scanner.scan(
            project.workspace,
        )

        self.pipeline.language_detector.detect(
            workspace_entries,
        )

        self.pipeline.framework_detector.detect(
            workspace_entries,
        )

        self.pipeline.dependency_analyzer.analyze(
            project.workspace,
        )

        return self.pipeline.snapshot_builder.build(
            project,
        )
