"""
ShadBot Agent Platform

Capability Description Model
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import FrozenSet


@dataclass(frozen=True, slots=True)
class CapabilityDescription:
    """
    Human and machine readable capability description.
    """

    summary: str

    purpose: str

    usage_guidelines: FrozenSet[str] = frozenset()

    limitations: FrozenSet[str] = frozenset()

    keywords: FrozenSet[str] = frozenset()
