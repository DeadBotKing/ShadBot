"""
ShadBot Agent Platform

State Cleanup Manager component for 7.4 State Management.
"""

from __future__ import annotations

from uuid import UUID
from .state_storage import RuntimeStateStorage


class StateCleanupManager:
    """
    Cleans up terminated or expired runtime states.
    """

    def __init__(self, storage: RuntimeStateStorage) -> None:
        self._storage = storage

    def cleanup(self, project_id: UUID) -> bool:
        if project_id in self._storage._states:
            del self._storage._states[project_id]
            return True
        return False
