"""
ShadBot Agent Platform

Handoff Request model for 6.4 Agent Handoff.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import UUID
from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class HandoffRequest:
    source_agent_name: str
    target_agent_name: str
    previous_result: AgentResult
    task_id: UUID
