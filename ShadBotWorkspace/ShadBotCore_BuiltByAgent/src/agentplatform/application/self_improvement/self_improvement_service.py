from dataclasses import dataclass, field

from agentplatform.domain.agents.agent_role import AgentRole
from agentplatform.domain.contracts.agent_contract import AgentContract
from agentplatform.domain.architecture_plan.architecture_plan import ArchitecturePlan
from agentplatform.application.orchestration.agent_orchestrator import AgentOrchestrator
from agentplatform.application.quality_gate.quality_gate_service import QualityGateService
from agentplatform.application.platform.platform_service import PlatformService
from agentplatform.application.release.release_service import ReleaseService

@dataclass(frozen=True)
class SelfImprovementPlan:
    role: AgentRole
    contract: AgentContract
    plan: ArchitecturePlan

class SelfImprovementService:
    """
    Orchestrates the self-improvement process for agents.
    
    This service is stateless and depends on other application services and domain objects.
    """

    def __init__(self, orchestrator: AgentOrchestrator,
                 quality_gate_service: QualityGateService,
                 platform_service: PlatformService,
                 release_service: ReleaseService):
        """
        Initialize the self-improvement service with dependencies.

        :param orchestrator: AgentOrchestrator to manage agent orchestration.
        :param quality_gate_service: QualityGateService to ensure quality during improvement.
        :param platform_service: PlatformService for platform-related operations.
        :param release_service: ReleaseService for managing software releases.
        """
        self.orchestrator = orchestrator
        self.quality_gate_service = quality_gate_service
        self.platform_service = platform_service
        self.release_service = release_service

    def generate_improvement_plan(self, role: AgentRole) -> SelfImprovementPlan:
        """
        Generate an improvement plan for the given agent role.

        :param role: The agent role to improve.
        :return: A SelfImprovementPlan object containing the improvement details.
        """
        contract = self.platform_service.get_agent_contract(role)
        current_plan = self.orchestrator.get_current_architecture_plan()
        new_plan = ArchitecturePlan(
            id=current_plan.id,
            version=current_plan.version + 1,
            features=current_plan.features | set([role.feature])
        )
        return SelfImprovementPlan(role, contract, new_plan)

    def apply_improvement(self, plan: SelfImprovementPlan):
        """
        Apply the improvement plan to enhance the agent's capabilities.

        :param plan: The SelfImprovementPlan object containing the improvement details.
        """
        if not self.quality_gate_service.check_quality(plan.contract, plan.plan):
            raise ValueError("Improvement does not meet quality gate criteria.")
        
        updated_plan = self.orchestrator.update_architecture_plan(plan.role, plan.plan)
        self.release_service.create_release(updated_plan)

    def evaluate_improvement(self, role: AgentRole):
        """
        Evaluate the effectiveness of an agent's improvement.

        :param role: The agent role to evaluate.
        """
        updated_plan = self.orchestrator.get_current_architecture_plan()
        if role.feature in updated_plan.features:
            print(f"Improvement for {role} is effective.")
        else:
            print(f"Improvement for {role} did not take effect.")

# Example usage
if __name__ == "__main__":
    # Mock dependencies
    orchestrator = AgentOrchestrator()
    quality_gate_service = QualityGateService()
    platform_service = PlatformService()
    release_service = ReleaseService()

    service = SelfImprovementService(orchestrator, quality_gate_service, platform_service, release_service)
    
    role = AgentRole(id="1", feature="AI")
    plan = service.generate_improvement_plan(role)
    service.apply_improvement(plan)
    service.evaluate_improvement(role)