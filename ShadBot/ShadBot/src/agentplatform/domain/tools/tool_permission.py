"""
ShadBot Agent Platform

Tool permission model.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.tools.tool_type import ToolType


@dataclass(frozen=True, slots=True)
class ToolPermission:
    """
    Assigns a tool permission to an agent.
    """

    agent_role: AgentRole

    tool_type: ToolType

    allowed: bool = True
