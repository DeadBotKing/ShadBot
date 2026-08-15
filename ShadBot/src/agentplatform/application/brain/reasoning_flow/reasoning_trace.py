"""
ShadBot Agent Platform

Reasoning Trace component.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ReasoningStep:
    step_number: int
    rationale: str
    conclusion: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ReasoningTrace:
    """
    Records and tracks cognitive reasoning steps.
    """

    def __init__(self, trace_id: UUID | None = None) -> None:
        self.trace_id = trace_id or uuid4()
        self._steps: list[ReasoningStep] = []

    def record_step(self, rationale: str, conclusion: str) -> ReasoningStep:
        step = ReasoningStep(
            step_number=len(self._steps) + 1,
            rationale=rationale,
            conclusion=conclusion,
        )
        self._steps.append(step)
        return step

    def get_steps(self) -> tuple[ReasoningStep, ...]:
        return tuple(self._steps)

    def summary(self) -> str:
        return f"Trace {self.trace_id}: {len(self._steps)} reasoning steps recorded."
