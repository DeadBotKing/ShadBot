"""
ShadBot Agent Platform

Unified service for 7.4 State Management.
"""

from __future__ import annotations

from uuid import UUID, uuid4
from .consistency_validation import StateConsistencyReport, StateConsistencyValidator
from .runtime_state_model import RuntimeStateModel
from .state_cleanup import StateCleanupManager
from .state_storage import RuntimeStateStorage
from .state_synchronization import RuntimeStateSynchronizer, StateSyncReport
from .transition_manager import RuntimeStateTransitionManager


class StateManagementServiceLayer:
    """
    Orchestrates state model storage, transitions, synchronization, consistency validation, and cleanup.
    """

    def __init__(
        self,
        storage: RuntimeStateStorage | None = None,
        transition_mgr: RuntimeStateTransitionManager | None = None,
        sync_mgr: RuntimeStateSynchronizer | None = None,
        validator: StateConsistencyValidator | None = None,
    ) -> None:
        self._storage = storage or RuntimeStateStorage()
        self._transition_mgr = transition_mgr or RuntimeStateTransitionManager()
        self._sync_mgr = sync_mgr or RuntimeStateSynchronizer()
        self._validator = validator or StateConsistencyValidator()
        self._cleanup = StateCleanupManager(self._storage)

    def init_state(self, project_id: UUID, session_id: UUID | None = None) -> RuntimeStateModel:
        state = RuntimeStateModel(
            state_id=uuid4(),
            project_id=project_id,
            active_session_id=session_id,
            execution_phase="BOOTSTRAP",
            status="INITIALIZED",
        )
        return self._storage.save_state(state)

    def update_phase(self, project_id: UUID, phase: str, status: str) -> tuple[RuntimeStateModel, StateConsistencyReport, StateSyncReport]:
        curr = self._storage.load_state(project_id)
        if curr is None:
            curr = self.init_state(project_id)
        updated = self._transition_mgr.transition(curr, phase, status)
        self._storage.save_state(updated)
        val = self._validator.validate_consistency(updated)
        sync = self._sync_mgr.sync(updated)
        return updated, val, sync
