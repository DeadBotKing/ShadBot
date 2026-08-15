"""
ShadBot Agent Platform

State Restoration component for 7.6 Resume System.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID
from agentplatform.application.runtime.state_management import RuntimeStateModel, StateManagementServiceLayer


@dataclass(frozen=True, slots=True)
class StateRestorationResult:
    restored: bool
    state: RuntimeStateModel


class StateRestoration:
    """
    Restores runtime state models during resume operations.
    """

    def __init__(self, state_service: StateManagementServiceLayer | None = None) -> None:
        self._state_service = state_service or StateManagementServiceLayer()

    def restore_state(self, project_id: UUID, session_id: UUID) -> StateRestorationResult:
        st = self._state_service.init_state(project_id, session_id)
        up, _, _ = self._state_service.update_phase(project_id, "RESUMED", "RUNNING")
        return StateRestorationResult(True, up)
