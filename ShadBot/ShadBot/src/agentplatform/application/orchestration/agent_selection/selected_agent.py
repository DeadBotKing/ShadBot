"""
ShadBot Agent Platform

Selected Agent model for 6.2 Agent Selection.
"""

from __future__ import annotations

from dataclasses import dataclass
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.contracts import AgentContract


@dataclass(frozen=True, slots=True)
class SelectedAgentPackage:
    agent: AgentContract
    role: AgentRole
    selection_score: float
    selection_reason: str
