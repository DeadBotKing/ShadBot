"""
ShadBot Agent Platform

Capability Requirements Model
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True, slots=True)
class CapabilityRequirements:
    """
    Runtime requirements needed by a capability.
    """

    required_tools: FrozenSet[str] = frozenset()

    required_contexts: FrozenSet[str] = frozenset()

    required_permissions: FrozenSet[str] = frozenset()

    required_dependencies: FrozenSet[str] = frozenset()
