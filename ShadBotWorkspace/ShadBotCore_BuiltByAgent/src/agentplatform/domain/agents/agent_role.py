from enum import Enum

class AgentRole(Enum):
    """Enumeration of agent roles."""
    ARCHITECT = 'architect'
    ENGINEER = 'engineer'
    PROJECT_INTELLIGENCE = 'project_intelligence'

class AgentIdentity:
    """
    Immutable data class representing the identity and role of an agent.
    
    :param str name: The name of the agent
    :param AgentRole role: The role of the agent
    """
    def __init__(self, name: str, role: AgentRole):
        self.name = name
        self.role = role

    def __eq__(self, other):
        if not isinstance(other, AgentIdentity):
            return False
        return self.name == other.name and self.role == other.role

    def __hash__(self):
        return hash((self.name, self.role))

    def __repr__(self):
        return f"AgentIdentity(name={self.name}, role={self.role})"