"""
ShadBot Project Intelligence

Project Intelligence Runtime
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.runtime_result import (
    RuntimeResult,
)
from projectintelligence.application.orchestration.project_intelligence_orchestrator import (
    ProjectIntelligenceOrchestrator,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


@dataclass(slots=True)
class ProjectIntelligenceRuntime:
    """
    Runtime entry point for the Project Intelligence subsystem.
    """

    orchestrator: ProjectIntelligenceOrchestrator

    def execute(
        self,
        project: ProjectEntity,
    ) -> RuntimeResult:

        return self.orchestrator.execute(
            project,
        )
