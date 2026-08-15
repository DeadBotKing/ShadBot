from dataclasses import dataclass, field
from enum import Enum

@dataclass(frozen=True)
class ArchitecturePlanStatus(Enum):
    DRAFT = "draft"
    REVIEW = "review"
    APPROVED = "approved"
    DEPRECATED = "deprecated"

@dataclass(frozen=True)
class ArchitecturePlan:
    """
    Domain entity representing an architecture plan.
    
    Immutable: all attributes are frozen and cannot be modified after creation.
    """
    id: int
    title: str
    description: str
    status: ArchitecturePlanStatus = field(default=ArchitecturePlanStatus.DRAFT)

    def update_status(self, new_status: ArchitecturePlanStatus) -> 'ArchitecturePlan':
        """
        Creates a new instance with the updated status.

        Args:
            new_status (ArchitecturePlanStatus): The new status to set for the plan.

        Returns:
            ArchitecturePlan: A new instance with the updated status.
        """
        return ArchitecturePlan(id=self.id, title=self.title, description=self.description, status=new_status)

    def __post_init__(self):
        if not isinstance(self.status, ArchitecturePlanStatus):
            raise ValueError(f"Invalid status value: {self.status}. Must be an ArchitecturePlanStatus enum.")

# Example usage
if __name__ == "__main__":
    plan = ArchitecturePlan(id=1, title="Initial System Design", description="Design for the initial system architecture.")
    print(plan)
    updated_plan = plan.update_status(ArchitecturePlanStatus.REVIEW)
    print(updated_plan)