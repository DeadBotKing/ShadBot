"""
ShadBot Agent Platform

Priority Evaluator component for 6.2 Agent Selection.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.contracts import AgentContract


class PriorityEvaluator:
    """
    Evaluates and ranks candidate agents by priority and capability fit.
    """

    def evaluate(self, agents: Sequence[AgentContract], primary_role: AgentRole) -> tuple[tuple[AgentContract, float], ...]:
        scored: list[tuple[AgentContract, float]] = []
        for agent in agents:
            agent_role = getattr(agent, "role", None)
            score = 0.98 if agent_role == primary_role else 0.75
            scored.append((agent, score))
        return tuple(sorted(scored, key=lambda item: item[1], reverse=True))
