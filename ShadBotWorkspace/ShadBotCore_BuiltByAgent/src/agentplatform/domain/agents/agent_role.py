from dataclasses import dataclass, field
from enum import Enum

class AgentRole(Enum):
    """Fixed set of values representing different agent roles."""
    ARCHITECT = 'architect'
    ENGINEER = 'engineer'
    INTELLIGENCE = 'intelligence'

@dataclass(frozen=True)
class AgentIdentity:
    """Immutable data class for agent identity and role enumeration."""
    agent_id: str
    role: AgentRole

def get_agent_role(agent_identity: AgentIdentity) -> AgentRole:
    """Retrieve the role of the given agent."""
    return agent_identity.role