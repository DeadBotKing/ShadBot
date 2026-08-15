"""
ShadBot Agent Platform

State Storage component for 7.4 State Management.
"""

from __future__ import annotations

from uuid import UUID
from .runtime_state_model import RuntimeStateModel


class RuntimeStateStorage:
    """
    Stores and retrieves runtime state models.
    """

    def __init__(self) -> None:
        self._states: dict[UUID, RuntimeStateModel] = {}

    def save_state(self, state: RuntimeStateModel) -> RuntimeStateModel:
        self._states[state.project_id] = state
        return state

    def load_state(self, project_id: UUID) -> RuntimeStateModel | None:
        return self._states.get(project_id)
