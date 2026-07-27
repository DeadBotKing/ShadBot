"""
ShadBot Project Intelligence

Project Intelligence Runtime
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.orchestration.project_intelligence_orchestrator import (
    ProjectIntelligenceOrchestrator,
)
from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


@dataclass(slots=True)
class ProjectIntelligenceRuntime:
    """
    Runtime entry point for the Project Intelligence subsystem.

    This class coordinates the execution of the complete
    Project Intelligence workflow and serves as the stable
    entry point for external consumers such as APIs,
    AI agents, CLI tools, and background workers.
    """

    orchestrator: ProjectIntelligenceOrchestrator

    def execute(
        self,
        project: ProjectEntity,
    ) -> PipelineResult:
        """
        Execute the complete Project Intelligence workflow.
        """

        return self.orchestrator.execute(
            project,
        )
