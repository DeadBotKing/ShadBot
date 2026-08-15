from dataclasses import dataclass, field
from enum import Enum

@dataclass(frozen=True)
class AgentRole(Enum):
    PROJECT_INTELLIGENCE = "Project Intelligence"
    ARCHITECT = "Architect"
    ENGINEER = "Engineer"

@dataclass(frozen=True)
class ArchitecturePlan:
    id: str
    description: str

class AgentContract:
    """
    Base abstract contract for agents.
    
    This contract defines the methods that all agent implementations must adhere to.
    """

    def get_role(self) -> AgentRole:
        """
        Return the role of this agent as an instance of AgentRole.
        
        Returns:
            AgentRole: The role of the agent.
        """
        raise NotImplementedError("Subclasses must implement get_role method")

    def execute_task(self, task_description: str) -> None:
        """
        Execute a specific task based on the description provided.
        
        Args:
            task_description (str): A string describing the task to be executed.
        
        Returns:
            None
        """
        raise NotImplementedError("Subclasses must implement execute_task method")

    def evaluate_quality(self, architecture_plan: ArchitecturePlan) -> float:
        """
        Evaluate the quality of an architecture plan.
        
        Args:
            architecture_plan (ArchitecturePlan): The architecture plan to evaluate.
        
        Returns:
            float: A score representing the quality of the architecture plan.
        """
        raise NotImplementedError("Subclasses must implement evaluate_quality method")

    def improve_architecture(self, architecture_plan: ArchitecturePlan) -> ArchitecturePlan:
        """
        Improve an architecture plan based on the agent's capabilities.
        
        Args:
            architecture_plan (ArchitecturePlan): The architecture plan to improve.
        
        Returns:
            ArchitecturePlan: The improved architecture plan.
        """
        raise NotImplementedError("Subclasses must implement improve_architecture method")

    def self_improve(self) -> None:
        """
        Perform self-improvement based on recent experiences and feedback.
        
        Returns:
            None
        """
        raise NotImplementedError("Subclasses must implement self_improve method")