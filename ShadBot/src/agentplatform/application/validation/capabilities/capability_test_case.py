"""
ShadBot Agent Platform

Capability Test Case
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class CapabilityTestCase:
    """
    Defines a capability validation scenario.
    """

    capability_id: UUID

    test_name: str

    description: str

    expected_success: bool = True
