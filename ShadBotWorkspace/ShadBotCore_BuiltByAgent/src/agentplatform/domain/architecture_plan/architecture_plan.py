from dataclasses import dataclass
from enum import Enum

# Import necessary classes from existing modules
from agentplatform.domain.agents.agent_role import AgentRole
from agentplatform.domain.contracts.agent_contract import AgentContract

@dataclass(frozen=True)
class ArchitecturePlanStatus(Enum):
    """Enum for fixed sets of values representing the status of an architecture plan."""
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

@dataclass(frozen=True)
class ArchitecturePlan:
    """Domain entity representing the architectural plan of an agent platform."""
    
    plan_id: str
    description: str
    status: ArchitecturePlanStatus
    agent_role: AgentRole
    contracts: list[AgentContract]
    
    def update_status(self, new_status: ArchitecturePlanStatus) -> None:
        """Update the status of the architecture plan."""
        self.status = new_status

# Example usage (uncomment to test)
# if __name__ == "__main__":
#     agent_role = AgentRole.DEVELOPER
#     contract1 = AgentContract(contract_id="contract001", details="Initial setup")
#     contract2 = AgentContract(contract_id="contract002", details="Enhancements")
#     plan = ArchitecturePlan(
#         plan_id="plan001",
#         description="Main architecture plan for ShadBot Agent Platform",
#         status=ArchitecturePlanStatus.IN_PROGRESS,
#         agent_role=agent_role,
#         contracts=[contract1, contract2]
#     )
#     print(plan)
#     plan.update_status(ArchitecturePlanStatus.COMPLETED)
#     print(plan.status)