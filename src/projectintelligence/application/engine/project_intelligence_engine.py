"""
ShadBot Project Intelligence

Project Intelligence Engine
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
class ProjectIntelligenceEngine:
    """
    Top-level entry point for Project Intelligence.

    This class intentionally contains no business logic.
    It delegates execution to the orchestrator.
    """

    orchestrator: ProjectIntelligenceOrchestrator

    def execute(
        self,
        project: ProjectEntity,
    ) -> RuntimeResult:
        """
        Execute the complete Project Intelligence workflow.
        """

        return self.orchestrator.execute(
            project=project,
        )
