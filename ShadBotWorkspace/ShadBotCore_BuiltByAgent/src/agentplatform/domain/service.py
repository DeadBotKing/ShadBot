# src/agentplatform/domain/models.py

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass(frozen=True)
class Agent:
    agent_id: str
    name: str
    role: str

@dataclass(frozen=True)
class Task:
    task_id: str
    title: str
    description: str
    status: str = field(default="pending")

@dataclass(frozen=True)
class Module:
    module_id: str
    name: str
    dependencies: List[str] = field(default_factory=list)

# src/agentplatform/domain/services.py

from .models import Agent, Task, Module

class DomainService:
    def get_agents(self) -> List[Agent]:
        pass

    def get_tasks(self) -> List[Task]:
        pass

    def get_modules(self) -> List[Module]:
        pass

# src/agentplatform/application/services.py

from .domain.services import DomainService
from .domain.models import Agent, Task, Module

class ApplicationService:
    def __init__(self, domain_service: DomainService):
        self.domain_service = domain_service

    def list_agents(self) -> List[Agent]:
        return self.domain_service.get_agents()

    def list_tasks(self) -> List[Task]:
        return self.domain_service.get_tasks()

    def list_modules(self) -> List[Module]:
        return self.domain_service.get_modules()

# src/agentplatform/application/services/validation.py

from typing import List, Tuple
from .domain.models import Agent, Task, Module
from ..application.services import ApplicationService

class QualityGate:
    @staticmethod
    def validate_agents(agents: List[Agent]) -> bool:
        return len(agents) > 0

    @staticmethod
    def validate_tasks(tasks: List[Task]) -> bool:
        for task in tasks:
            if task.status != "completed":
                return False
        return True

    @staticmethod
    def validate_modules(modules: List[Module]) -> bool:
        for module in modules:
            if not all(dep in [m.module_id for m in modules] for dep in module.dependencies):
                return False
        return True

# src/agentplatform/application/services/execution.py

from ..application.services import ApplicationService, QualityGate

class ExecutionService:
    def __init__(self, application_service: ApplicationService):
        self.application_service = application_service

    def run_quality_gate(self) -> Tuple[bool, str]:
        agents = self.application_service.list_agents()
        tasks = self.application_service.list_tasks()
        modules = self.application_service.list_modules()

        if QualityGate.validate_agents(agents):
            if QualityGate.validate_tasks(tasks):
                if QualityGate.validate_modules(modules):
                    return True, "All quality gates passed."
                else:
                    return False, "Module dependency validation failed."
            else:
                return False, "Task status validation failed."
        else:
            return False, "Agent presence validation failed."

# src/agentplatform/__init__.py

from .domain.services import DomainService
from .application.services import ApplicationService, ExecutionService

__all__ = [
    "DomainService",
    "ApplicationService",
    "ExecutionService"
]