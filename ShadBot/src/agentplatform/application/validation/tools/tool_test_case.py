"""
ShadBot Agent Platform

Tool Test Case
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ToolTestCase:
    """
    Defines a tool validation scenario.
    """

    tool_id: UUID

    test_name: str

    description: str

    expected_success: bool = True
