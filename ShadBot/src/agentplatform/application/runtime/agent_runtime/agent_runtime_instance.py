"""
ShadBot Agent Platform

Agent Runtime Instance component for 7.1 Agent Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from uuid import UUID, uuid4
from agentplatform.domain.contracts import AgentContract
from .runtime_state import AgentRuntimeState


@dataclass(frozen=True, slots=True)
class AgentRuntimeInstance:
    instance_id: UUID
    agent: AgentContract
    state: AgentRuntimeState
