"""
ShadBot Project Intelligence

Intelligence Export Service
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.application.export.project_intelligence_exporter import (
    ProjectIntelligenceExporter,
)
from projectintelligence.application.models.results.runtime_result import (
    RuntimeResult,
)


@dataclass(slots=True)
class IntelligenceExportService:
    """
    Application service responsible for exporting
    Project Intelligence runtime artifacts.
    """

    exporter: ProjectIntelligenceExporter

    def export(
        self,
        result: RuntimeResult,
        workspace: Path,
    ) -> Path:
        """
        Export runtime intelligence package.
        """

        output_path = (
            workspace / ".shadbot" / "intelligence" / "intelligence_package.json"
        )

        return self.exporter.export(
            result=result.pipeline_result,
            output_path=output_path,
        )
