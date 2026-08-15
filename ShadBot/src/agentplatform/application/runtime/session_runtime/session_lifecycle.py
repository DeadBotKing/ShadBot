"""
ShadBot Agent Platform

Session Lifecycle component for 7.3 Session Runtime.
"""

from __future__ import annotations

from datetime import datetime, timezone
from .session_entity import ExecutionSession


class SessionLifecycle:
    """
    Manages state transitions across an execution session's lifecycle.
    """

    def transition_status(self, session: ExecutionSession, new_status: str) -> ExecutionSession:
        return ExecutionSession(
            session_id=session.session_id,
            project_id=session.project_id,
            task_id=session.task_id,
            status=new_status,
            created_at=session.created_at,
            updated_at=datetime.now(timezone.utc).isoformat(),
        )
