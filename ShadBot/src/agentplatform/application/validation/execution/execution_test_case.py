"""
ShadBot Agent Platform

Execution Test Case
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ExecutionTestCase:
    """
    Defines execution validation scenario.
    """

    capability_id: UUID

    tool_id: UUID

    test_name: str

    description: str

    expected_success: bool = True
