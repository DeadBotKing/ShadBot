"""
ShadBot Project Intelligence

Project Intelligence Bootstrap
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.infrastructure.persistence.repositories.in_memory_snapshot_repository import (
    InMemorySnapshotRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_context_repository import (
    InMemoryContextRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_knowledge_repository import (
    InMemoryKnowledgeRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_history_repository import (
    InMemoryHistoryRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_state_repository import (
    InMemoryStateRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_resume_repository import (
    InMemoryResumeRepository,
)
from projectintelligence.application.persistence.services.snapshot_storage_service import (
    SnapshotStorageService,
)
from projectintelligence.application.persistence.services.context_storage_service import (
    ContextStorageService,
)
from projectintelligence.application.persistence.services.knowledge_storage_service import (
    KnowledgeStorageService,
)
from projectintelligence.application.persistence.services.history_storage_service import (
    HistoryStorageService,
)
from projectintelligence.application.persistence.services.state_storage_service import (
    StateStorageService,
)
from projectintelligence.application.persistence.services.resume_storage_service import (
    ResumeStorageService,
)
from projectintelligence.application.persistence.services.persistence_service import (
    PersistenceService,
)
from projectintelligence.application.engine.project_intelligence_engine import (
    ProjectIntelligenceEngine,
)
from projectintelligence.application.orchestration.project_intelligence_orchestrator import (
    ProjectIntelligenceOrchestrator,
)


@dataclass(slots=True)
class ProjectIntelligenceBootstrap:
    """
    Composition root for the Project Intelligence Engine.

    Responsible for constructing the complete dependency graph.
    """

    def build(self):
        """
        Build the complete Project Intelligence Engine.
        """
        snapshot_repository = InMemorySnapshotRepository()

        context_repository = InMemoryContextRepository()

        knowledge_repository = InMemoryKnowledgeRepository()

        history_repository = InMemoryHistoryRepository()

        state_repository = InMemoryStateRepository()

        resume_repository = InMemoryResumeRepository()

        snapshot_storage = SnapshotStorageService(
            repository=snapshot_repository,
        )

        context_storage = ContextStorageService(
            repository=context_repository,
        )

        knowledge_storage = KnowledgeStorageService(
            repository=knowledge_repository,
        )

        history_storage = HistoryStorageService(
            repository=history_repository,
        )

        state_storage = StateStorageService(
            repository=state_repository,
        )

        resume_storage = ResumeStorageService(
            repository=resume_repository,
        )

        persistence_service = PersistenceService(
            snapshot_storage=snapshot_storage,
            context_storage=context_storage,
            knowledge_storage=knowledge_storage,
            state_storage=state_storage,
            resume_storage=resume_storage,
        )

        orchestrator = ProjectIntelligenceOrchestrator(
            pipeline=None,
            persistence_service=persistence_service,
            snapshot_history_service=None,
            resume_generator=None,
        )

        return ProjectIntelligenceEngine(
            orchestrator=orchestrator,
        )