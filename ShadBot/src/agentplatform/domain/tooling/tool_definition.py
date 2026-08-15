"""
ShadBot Agent Platform

Tool definition model.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.tools import ToolType


@dataclass(frozen=True, slots=True)
class ToolDefinition:
    """
    Describes an executable agent tool.
    """

    name: str

    tool_type: ToolType

    description: str
