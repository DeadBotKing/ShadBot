"""
ShadBot Agent Platform

Decision Generator component for 5.6 Decision Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class DecisionAlternative:
    alternative_id: UUID
    title: str
    description: str
    impact: str


class DecisionGenerator:
    """
    Generates decision alternatives from candidate options.
    """

    def generate(self, options: Sequence[str]) -> tuple[DecisionAlternative, ...]:
        alts: list[DecisionAlternative] = []
        for idx, opt in enumerate(options):
            alts.append(
                DecisionAlternative(
                    alternative_id=uuid4(),
                    title=opt,
                    description=f"Candidate alternative based on: {opt}",
                    impact="High" if idx == 0 else "Medium",
                )
            )
        return tuple(alts)
