"""
ShadBot Agent Platform

Session Recovery Handling component for 7.3 Session Runtime.
"""

from __future__ import annotations

from .session_entity import ExecutionSession
from .session_lifecycle import SessionLifecycle


class SessionRecoveryHandler:
    """
    Recovers interrupted execution sessions.
    """

    def __init__(self, lifecycle: SessionLifecycle | None = None) -> None:
        self._lifecycle = lifecycle or SessionLifecycle()

    def recover(self, session: ExecutionSession) -> ExecutionSession:
        if session.status in ("TERMINATED", "COMPLETED"):
            return session
        return self._lifecycle.transition_status(session, "RECOVERED")
