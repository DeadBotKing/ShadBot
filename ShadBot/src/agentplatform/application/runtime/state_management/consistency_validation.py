"""
ShadBot Agent Platform

State Consistency Validation component for 7.4 State Management.
"""

from __future__ import annotations

from dataclasses import dataclass
from .runtime_state_model import RuntimeStateModel


@dataclass(frozen=True, slots=True)
class StateConsistencyReport:
    consistent: bool
    notes: str


class StateConsistencyValidator:
    """
    Validates internal consistency of runtime state models.
    """

    def validate_consistency(self, state: RuntimeStateModel) -> StateConsistencyReport:
        if state.status in ("RUNNING", "ACTIVE") and state.active_session_id is None:
            return StateConsistencyReport(False, "Active state requires an active_session_id.")
        return StateConsistencyReport(True, "Runtime state is consistent.")
