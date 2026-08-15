"""
ShadBot Agent Platform

Session Context Storage component for 7.3 Session Runtime.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID


class SessionContextStorage:
    """
    Stores and retrieves temporary context data for an execution session.
    """

    def __init__(self) -> None:
        self._storage: dict[UUID, dict[str, Any]] = {}

    def save_context(self, session_id: UUID, key: str, value: Any) -> None:
        if session_id not in self._storage:
            self._storage[session_id] = {}
        self._storage[session_id][key] = value

    def load_context(self, session_id: UUID) -> dict[str, Any]:
        return dict(self._storage.get(session_id, {}))
