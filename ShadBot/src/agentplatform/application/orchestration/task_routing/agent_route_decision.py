"""
ShadBot Agent Platform

Agent Route Decision model for 6.1 Task Routing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from uuid import UUID
from agentplatform.domain.agents import AgentRole


@dataclass(frozen=True, slots=True)
class AgentRouteDecision:
    task_id: UUID
    required_role: AgentRole
    candidate_roles: tuple[AgentRole, ...]
    routing_strategy: str
    is_valid: bool
    validation_notes: str
