"""
ShadBot Agent Platform

Execution Continuation Manager component for 7.6 Resume System.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .recovery_engine import ExecutionRecoveryState


@dataclass(frozen=True, slots=True)
class ContinuedExecutionPackage:
    can_continue: bool
    next_step: int
    active_context: dict[str, Any]


class ExecutionContinuationManager:
    """
    Manages resumption of execution from the recovered step number.
    """

    def continue_execution(self, state: ExecutionRecoveryState) -> ContinuedExecutionPackage:
        return ContinuedExecutionPackage(
            can_continue=True,
            next_step=state.resumed_step,
            active_context=dict(state.context_data),
        )
