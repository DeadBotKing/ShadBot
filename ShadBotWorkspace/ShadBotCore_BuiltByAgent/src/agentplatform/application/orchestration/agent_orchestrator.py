from dataclasses import dataclass, field

from src.agentplatform.domain.agents.agent_role import AgentRole
from src.agentplatform.domain.contracts.agent_contract import AgentContract
from src.agentplatform.domain.architecture_plan.architecture_plan import ArchitecturePlan
from src.agentplatform.application.quality_gate.quality_gate_service import QualityGateService
from src.agentplatform.application.self_improvement.self_improvement_service import SelfImprovementService
from src.agentplatform.application.platform.platform_service import PlatformService
from src.agentplatform.application.release.release_service import ReleaseService

@dataclass(frozen=True)
class AgentOrchestrator:
    """
    Orchestrates multi-agent pipeline orchestration (Phase 6).
    
    Stateless: no mutable instance state between calls.
    Dependent on abstractions; receives collaborators via __init__ injection.
    """
    
    quality_gate_service: QualityGateService
    self_improvement_service: SelfImprovementService
    platform_service: PlatformService
    release_service: ReleaseService
    
    def orchestrate_pipeline(self, architecture_plan: ArchitecturePlan) -> None:
        """
        Orchestrates the pipeline based on the given architecture plan.
        
        :param architecture_plan: The architecture plan to base the pipeline on.
        :type architecture_plan: ArchitecturePlan
        """
        # Step 1: Quality Gate Check
        if not self.quality_gate_service.check(architecture_plan):
            raise ValueError("Architecture plan does not meet quality gate requirements.")
        
        # Step 2: Self-Improvement
        improved_architecture_plan = self.self_improvement_service.improve(architecture_plan)
        
        # Step 3: Platform Setup
        platform = self.platform_service.setup(improved_architecture_plan)
        
        # Step 4: Release
        release = self.release_service.create(platform)
        
        # Final step: Output the release details
        print(f"Release created: {release}")