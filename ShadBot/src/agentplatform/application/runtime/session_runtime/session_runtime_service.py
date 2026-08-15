"""
ShadBot Agent Platform

Unified service for 7.3 Session Runtime.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID
from .session_context_storage import SessionContextStorage
from .session_entity import ExecutionSession
from .session_lifecycle import SessionLifecycle
from .session_manager import SessionManager
from .session_recovery import SessionRecoveryHandler
from .session_termination import SessionTerminationManager


class SessionRuntimeServiceLayer:
    """
    Orchestrates session creation, context storage, recovery, and termination.
    """

    def __init__(
        self,
        mgr: SessionManager | None = None,
        lifecycle: SessionLifecycle | None = None,
        storage: SessionContextStorage | None = None,
        recovery: SessionRecoveryHandler | None = None,
        term: SessionTerminationManager | None = None,
    ) -> None:
        self._mgr = mgr or SessionManager()
        self._lifecycle = lifecycle or SessionLifecycle()
        self._storage = storage or SessionContextStorage()
        self._recovery = recovery or SessionRecoveryHandler()
        self._term = term or SessionTerminationManager()

    def open_session(self, project_id: UUID, task_id: UUID) -> ExecutionSession:
        return self._mgr.create_session(project_id, task_id)

    def store_session_data(self, session_id: UUID, key: str, value: Any) -> None:
        self._storage.save_context(session_id, key, value)

    def recover_session(self, session: ExecutionSession) -> ExecutionSession:
        return self._recovery.recover(session)

    def close_session(self, session: ExecutionSession) -> ExecutionSession:
        return self._term.terminate(session)
