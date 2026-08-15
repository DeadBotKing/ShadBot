"""
ShadBot Agent Platform

Session Manager component for 7.3 Session Runtime.
"""

from __future__ import annotations

from uuid import UUID, uuid4
from .session_entity import ExecutionSession


class SessionManager:
    """
    Creates and tracks active execution sessions.
    """

    def __init__(self) -> None:
        self._sessions: dict[UUID, ExecutionSession] = {}

    def create_session(self, project_id: UUID, task_id: UUID) -> ExecutionSession:
        sess = ExecutionSession(
            session_id=uuid4(),
            project_id=project_id,
            task_id=task_id,
            status="ACTIVE",
        )
        self._sessions[sess.session_id] = sess
        return sess

    def get_session(self, session_id: UUID) -> ExecutionSession | None:
        return self._sessions.get(session_id)
