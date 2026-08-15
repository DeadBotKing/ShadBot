from dataclasses import dataclass, field
from typing import List

from src.agentplatform.domain.agents.agent_role import AgentRole
from src.agentplatform.domain.contracts.agent_contract import AgentContract
from src.agentplatform.domain.architecture_plan.architecture_plan import ArchitecturePlan
from src.agentplatform.application.orchestration.agent_orchestrator import AgentOrchestrator
from src.agentplatform.application.quality_gate.quality_gate_service import QualityGateService
from src.agentplatform.application.self_improvement.self_improvement_service import SelfImprovementService
from src.agentplatform.application.release.release_service import ReleaseService

@dataclass(frozen=True)
class PlatformFinalization:
    agent_orchestrator: AgentOrchestrator
    quality_gate_service: QualityGateService
    self_improvement_service: SelfImprovementService
    release_service: ReleaseService

@dataclass(frozen=True)
class PlatformAPIGateway:
    architecture_plan: ArchitecturePlan
    agent_roles: List[AgentRole]
    contracts: List[AgentContract]

class PlatformService:
    def __init__(
        self,
        platform_finalization: PlatformFinalization,
        platform_api_gateway: PlatformAPIGateway,
    ):
        self.platform_finalization = platform_finalization
        self.platform_api_gateway = platform_api_gateway

    def finalize_platform(self) -> None:
        """
        Orchestrates the finalization of the platform.
        """
        self.platform_finalization.agent_orchestrator.finalize_agents()
        self.platform_finalization.quality_gate_service.run_quality_gates()
        self.platform_finalization.self_improvement_service.improve_self()
        self.platform_finalization.release_service.prepare_release()

    def expose_api_gateway(self) -> None:
        """
        Orchestrates the exposure of the platform API gateway.
        """
        self.platform_api_gateway.architecture_plan.deploy_architecture()
        for role in self.platform_api_gateway.agent_roles:
            role.register_role()
        for contract in self.platform_api_gateway.contracts:
            contract.activate_contract()