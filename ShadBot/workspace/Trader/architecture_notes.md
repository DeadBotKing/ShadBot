from dataclasses import dataclass, field
import uuid
from datetime import datetime

@dataclass
class Entity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Project(Entity):
    title: str
    description: str
    type: str
    steps: list = field(default_factory=list)

@dataclass
class Step(Entity):
    step_number: int
    total_steps: int
    agent_name: str
    action: str
    status: str
    started_at: datetime
    completed_at: datetime

class ProjectManager:
    def create_project(self, title, description, type):
        project = Project(title=title, description=description, type=type)
        return project

    def add_step_to_project(self, project, step_number, total_steps, agent_name, action, status, started_at, completed_at):
        step = Step(step_number=step_number, total_steps=total_steps, agent_name=agent_name, action=action, status=status, started_at=started_at, completed_at=completed_at)
        project.steps.append(step)
        return project

# Example usage
project_manager = ProjectManager()
new_project = project_manager.create_project("Trader", "A system for automated trading", "Finance")
new_step = project_manager.add_step_to_project(new_project, 1, 4, "architect", "execute", "running", datetime.utcnow(), None)