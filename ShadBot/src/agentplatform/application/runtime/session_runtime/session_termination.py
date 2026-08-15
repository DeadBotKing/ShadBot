"""
ShadBot Agent Platform

Session Termination Manager component for 7.3 Session Runtime.
"""

from __future__ import annotations

from .session_entity import ExecutionSession
from .session_lifecycle import SessionLifecycle


class SessionTerminationManager:
    """
    Terminates execution sessions cleanly.
    """

    def __init__(self, lifecycle: SessionLifecycle | None = None) -> None:
        self._lifecycle = lifecycle or SessionLifecycle()

    def terminate(self, session: ExecutionSession) -> ExecutionSession:
        return self._lifecycle.transition_status(session, "TERMINATED")
