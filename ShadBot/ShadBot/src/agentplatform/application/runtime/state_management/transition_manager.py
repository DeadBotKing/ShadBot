"""
ShadBot Agent Platform

State Transition Manager component for 7.4 State Management.
"""

from __future__ import annotations

from datetime import datetime, timezone
from .runtime_state_model import RuntimeStateModel


class RuntimeStateTransitionManager:
    """
    Manages transitions of runtime states across execution phases.
    """

    def transition(self, current: RuntimeStateModel, new_phase: str, new_status: str) -> RuntimeStateModel:
        return RuntimeStateModel(
            state_id=current.state_id,
            project_id=current.project_id,
            active_session_id=current.active_session_id,
            execution_phase=new_phase,
            status=new_status,
            state_metadata=dict(current.state_metadata),
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
