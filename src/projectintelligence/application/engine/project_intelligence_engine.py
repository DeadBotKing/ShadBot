"""
ShadBot Project Intelligence

Project Intelligence Engine
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.orchestration.project_intelligence_orchestrator import (
    ProjectIntelligenceOrchestrator,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


@dataclass(slots=True)
class ProjectIntelligenceEngine:
    """
    Public entry point of the Project Intelligence Engine.
    """

    orchestrator: ProjectIntelligenceOrchestrator

    def analyze(
        self,
        project: ProjectEntity,
    ):
        """
        Analyze a project and execute the complete intelligence pipeline.
        """

        return self.orchestrator.execute(
            project,
        )
