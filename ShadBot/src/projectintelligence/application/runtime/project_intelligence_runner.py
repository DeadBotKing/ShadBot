"""
ShadBot Project Intelligence

Project Intelligence Runtime Runner
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.application.export.project_intelligence_exporter import (
    ProjectIntelligenceExporter,
)
from projectintelligence.application.orchestration.project_intelligence_orchestrator import (
    ProjectIntelligenceOrchestrator,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


class ProjectIntelligenceRunner:
    """
    Executes Project Intelligence against a workspace.

    This is the runtime boundary between
    external interfaces and the application layer.
    """

    def __init__(
        self,
        orchestrator: ProjectIntelligenceOrchestrator,
        exporter: ProjectIntelligenceExporter,
    ) -> None:
        self.orchestrator = orchestrator
        self.exporter = exporter

    def analyze(
        self,
        workspace: Path,
        output_path: Path,
    ) -> Path:
        """
        Analyze workspace and export intelligence result.
        """

        project = ProjectEntity(
            name=workspace.name,
            workspace=workspace,
        )

        result = self.orchestrator.execute(
            project,
        )

        self.exporter.export(
            result.pipeline_result,
            output_path,
        )

        return output_path
