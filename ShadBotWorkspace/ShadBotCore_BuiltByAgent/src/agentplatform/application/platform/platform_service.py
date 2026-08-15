from dataclasses import dataclass, field
from typing import List

from agentplatform.domain.agents.agent_role import AgentRole
from agentplatform.domain.contracts.agent_contract import AgentContract
from agentplatform.domain.architecture_plan.architecture_plan import ArchitecturePlan
from agentplatform.application.orchestration.agent_orchestrator import AgentOrchestrator
from agentplatform.application.quality_gate.quality_gate_service import QualityGateService
from agentplatform.application.self_improvement.self_improvement_service import SelfImprovementService
from agentplatform.application.release.release_service import ReleaseService

@dataclass(frozen=True)
class PlatformState:
    architecture_plan: ArchitecturePlan
    agents_roles: List[AgentRole]
    contracts: List[AgentContract]

class PlatformService:
    """
    Orchestrates the finalization and API Gateway for the ShadBot Agent Platform.
    """

    def __init__(self,
                 agent_orchestrator: AgentOrchestrator,
                 quality_gate_service: QualityGateService,
                 self_improvement_service: SelfImprovementService,
                 release_service: ReleaseService):
        """
        Initializes the PlatformService with necessary collaborators.

        :param agent_orchestrator: Orchestrates agents.
        :param quality_gate_service: Manages quality gate checks.
        :param self_improvement_service: Handles platform self-improvement.
        :param release_service: Manages platform releases.
        """
        self.agent_orchestrator = agent_orchestrator
        self.quality_gate_service = quality_gate_service
        self.self_improvement_service = self_improvement_service
        self.release_service = release_service

    def finalize_platform(self, architecture_plan: ArchitecturePlan) -> PlatformState:
        """
        Finalizes the platform based on the provided architecture plan.

        :param architecture_plan: The architecture plan to finalize.
        :return: The final state of the platform.
        """
        # Step 1: Deploy agents
        agents_roles = self.agent_orchestrator.deploy_agents(architecture_plan)

        # Step 2: Establish contracts
        contracts = [self.agent_orchestrator.create_contract(agent_role) for agent_role in agents_roles]

        # Step 3: Ensure quality gate compliance
        if not self.quality_gate_service.check_compliance(agents_roles, contracts):
            raise ValueError("Quality gate checks failed.")

        return PlatformState(architecture_plan=architecture_plan, agents_roles=agents_roles, contracts=contracts)

    def release_platform(self, platform_state: PlatformState) -> None:
        """
        Releasess the platform based on its current state.

        :param platform_state: The current state of the platform.
        """
        self.release_service.deploy_release(platform_state)