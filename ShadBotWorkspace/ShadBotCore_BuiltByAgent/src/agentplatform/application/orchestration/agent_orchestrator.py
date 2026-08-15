from dataclasses import dataclass, field
from typing import List

from agentplatform.domain.agents.agent_role import AgentRole
from agentplatform.domain.contracts.agent_contract import AgentContract
from agentplatform.domain.architecture_plan.architecture_plan import ArchitecturePlan
from agentplatform.application.quality_gate.quality_gate_service import QualityGateService
from agentplatform.application.self_improvement.self_improvement_service import SelfImprovementService
from agentplatform.application.platform.platform_service import PlatformService
from agentplatform.application.release.release_service import ReleaseService

class AgentOrchestrator:
    """
    Orchestrates multi-agent pipeline orchestration.

    This class is stateless and depends on abstractions for its operations.
    """

    def __init__(self,
                 quality_gate_service: QualityGateService,
                 self_improvement_service: SelfImprovementService,
                 platform_service: PlatformService,
                 release_service: ReleaseService):
        """
        Initialize the AgentOrchestrator with necessary collaborators.

        Args:
            quality_gate_service (QualityGateService): Service for quality checks.
            self_improvement_service (SelfImprovementService): Service for self-improvement.
            platform_service (PlatformService): Service for platform operations.
            release_service (ReleaseService): Service for release management.
        """
        self._quality_gate_service = quality_gate_service
        self._self_improvement_service = self_improvement_service
        self._platform_service = platform_service
        self._release_service = release_service

    def orchestrate_pipeline(self, architecture_plan: ArchitecturePlan) -> None:
        """
        Orchestrates the multi-agent pipeline based on the given architecture plan.

        Args:
            architecture_plan (ArchitecturePlan): The architecture plan to follow.
        """
        for agent_role in architecture_plan.agent_roles:
            if agent_role == AgentRole.PROJECT_INTELLIGENCE_AGENT:
                self._platform_service.process_project_intelligence(architecture_plan)
            elif agent_role == AgentRole.ARCHITECT_AGENT:
                self._self_improvement_service.improve_architecture(architecture_plan)
            elif agent_role == AgentRole.ENGINEER_AGENT:
                self._release_service.perform_release(architecture_plan)

        if not self._quality_gate_service.check_quality(architecture_plan):
            raise ValueError("Quality gate failed for the provided architecture plan.")

        self._self_improvement_service.improve_platform_based_on_plan(architecture_plan)