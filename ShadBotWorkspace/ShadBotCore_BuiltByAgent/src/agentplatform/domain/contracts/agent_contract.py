from dataclasses import dataclass, field
from enum import Enum

class AgentRole(Enum):
    PROJECT_INTELLIGENCE = 'project_intelligence'
    ARCHITECT = 'architect'
    ENGINEER = 'engineer'

@dataclass(frozen=True)
class AgentContract:
    role: AgentRole
    plan: 'architecture_plan.ArchitecturePlan'
    orchestrator: 'agent_orchestrator.AgentOrchestrator' = field(init=False)

    def __post_init__(self):
        self.orchestrator = agent_orchestrator.AgentOrchestrator(self)