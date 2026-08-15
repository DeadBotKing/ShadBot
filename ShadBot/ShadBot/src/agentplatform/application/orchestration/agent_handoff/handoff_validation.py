"""
ShadBot Agent Platform

Handoff Validation component for 6.4 Agent Handoff.
"""

from __future__ import annotations

from dataclasses import dataclass
from .handoff_request import HandoffRequest


@dataclass(frozen=True, slots=True)
class HandoffValidationResult:
    valid: bool
    reason: str


class HandoffValidator:
    """
    Validates if a handoff request contains required preceding artifacts.
    """

    def validate(self, request: HandoffRequest) -> HandoffValidationResult:
        if not request.previous_result.success:
            return HandoffValidationResult(
                valid=False,
                reason=f"Previous result from {request.source_agent_name} was unsuccessful.",
            )
        if request.source_agent_name == "architect" and "architecture_plan" not in request.previous_result.data:
            return HandoffValidationResult(
                valid=False,
                reason="Architect handoff missing architecture_plan.",
            )
        return HandoffValidationResult(
            valid=True,
            reason="Handoff validated successfully.",
        )
