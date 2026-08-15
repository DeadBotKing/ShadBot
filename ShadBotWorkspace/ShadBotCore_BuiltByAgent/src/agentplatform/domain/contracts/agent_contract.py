from dataclasses import dataclass, field
from enum import Enum

class AgentRole(Enum):
    PROJECT_INTELLIGENCE_AGENT = 'PROJECT_INTELLIGENCE_AGENT'
    ARCHITECT_AGENT = 'ARCHITECT_AGENT'
    ENGINEER_AGENT = 'ENGINEER_AGENT'

@dataclass(frozen=True)
class AgentContract:
    role: AgentRole
    architecture_plan: 'architecture_plan.ArchitecturePlan'  # Import path required
    agent_role: 'agents.agent_role.AgentRole'  # Import path required

    def execute_task(self, task_description: str) -> None:
        """Execute a specific task based on the agent's role and architecture plan."""
        raise NotImplementedError("Subclasses must implement the execute_task method")

    def assess_quality(self) -> bool:
        """Assess the quality of the current state based on the architecture plan."""
        raise NotImplementedError("Subclasses must implement the assess_quality method")

    def improve_self(self) -> None:
        """Implement self-improvement strategies based on feedback and progress."""
        raise NotImplementedError("Subclasses must implement the improve_self method")