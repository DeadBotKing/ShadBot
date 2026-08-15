from dataclasses import dataclass, field
from enum import Enum

@dataclass(frozen=True)
class ArchitecturePlanStatus(Enum):
    """Enum for fixed sets of values representing the status of an architecture plan."""
    DRAFT = 'draft'
    REVIEW = 'review'
    APPROVED = 'approved'
    DEPLOYED = 'deployed'

@dataclass(frozen=True)
class ArchitecturePlan:
    """Domain entity representing the architecture plan."""
    
    id: str
    title: str
    description: str
    status: ArchitecturePlanStatus = field(default=ArchitecturePlanStatus.DRAFT)
    created_at: str = None
    updated_at: str = None
    
    def __post_init__(self):
        if not self.id:
            raise ValueError("ID cannot be empty")
        if not self.title:
            raise ValueError("Title cannot be empty")
        if not self.description:
            raise ValueError("Description cannot be empty")

    def update_status(self, new_status: ArchitecturePlanStatus) -> 'ArchitecturePlan':
        """Update the status of the architecture plan."""
        return dataclasses.replace(self, status=new_status)

    def to_dict(self) -> dict:
        """Convert the architecture plan to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status.value,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }