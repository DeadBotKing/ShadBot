"""
ShadBot Agent Platform

Decision request contract.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class DecisionRequest:
    """
    Input contract for decision execution.
    """

    results: Sequence[AgentResult]

    metadata: dict[str, object] = field(
        default_factory=dict,
    )
