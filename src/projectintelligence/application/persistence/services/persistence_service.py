"""
ShadBot Project Intelligence

Persistence Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.models.results.persistence_batch_result import (
    PersistenceBatchResult,
)
from projectintelligence.application.models.results.persistence_result import (
    PersistenceResult,
)
from projectintelligence.application.persistence.services.context_storage_service import (
    ContextStorageService,
)
from projectintelligence.application.persistence.services.history_storage_service import (
    HistoryStorageService,
)
from projectintelligence.application.persistence.services.knowledge_storage_service import (
    KnowledgeStorageService,
)
from projectintelligence.application.persistence.services.resume_storage_service import (
    ResumeStorageService,
)
from projectintelligence.application.persistence.services.snapshot_storage_service import (
    SnapshotStorageService,
)
from projectintelligence.application.persistence.services.state_storage_service import (
    StateStorageService,
)
from projectintelligence.application.state.project_intelligence_state import (
    ProjectIntelligenceState,
)
from projectintelligence.domain.context.project_context import (
    ProjectContext,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.resume.project_resume import (
    ProjectResume,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.application.persistence.services.agent_context_storage_service import (
    AgentContextStorageService,
)
from projectintelligence.domain.handoff.agent_context_package import (
    AgentContextPackage,
)


@dataclass(slots=True)
class PersistenceService:
    """
    Coordinates persistence operations for Project Intelligence.
    """

    snapshot_storage: SnapshotStorageService

    context_storage: ContextStorageService

    knowledge_storage: KnowledgeStorageService

    state_storage: StateStorageService

    resume_storage: ResumeStorageService

    history_storage: HistoryStorageService

    agent_context_storage: AgentContextStorageService

    def save_snapshot(
        self,
        snapshot: ProjectSnapshot,
    ) -> PersistenceResult:
        return self.snapshot_storage.save(
            snapshot,
        )

    def save_context(
        self,
        context: ProjectContext,
    ) -> PersistenceResult:
        return self.context_storage.save(
            context,
        )

    def save_all(
        self,
        snapshot: ProjectSnapshot,
        knowledge: ProjectKnowledge,
        history: SnapshotHistory,
        state: ProjectIntelligenceState,
        context: ProjectContext,
        resume: ProjectResume,
        agent_context: AgentContextPackage
    ) -> PersistenceBatchResult:
        results = (
            self.save_snapshot(
                snapshot,
            ),
            self.save_knowledge(
                knowledge,
            ),
            self.save_history(
                history,
            ),
            self.save_state(
                state,
            ),
            self.save_context(
                context,
            ),
            self.save_resume(
                resume,
            ),
            self.save_agent_context(
                agent_context,
            ),
        )

        return PersistenceBatchResult(
            results=results,
        )

    def save_knowledge(
        self,
        knowledge: ProjectKnowledge,
    ) -> PersistenceResult:
        return self.knowledge_storage.save(
            knowledge,
        )


    def save_state(
        self,
        state: ProjectIntelligenceState,
    ) -> PersistenceResult:
        return self.state_storage.save(
            state,
        )

    def save_history(
        self,
        history: SnapshotHistory,
    ) -> PersistenceResult:
        return self.history_storage.save(
            history,
        )

    def save_resume(
        self,
        resume: ProjectResume,
    ) -> PersistenceResult:
        return self.resume_storage.save(
            resume,
        )

    def save_agent_context(
        self,
        context: AgentContextPackage,
    ) -> PersistenceResult:
        return self.agent_context_storage.save(
            context,
        )
