"""
ShadBot Agent Platform

Agent learned knowledge.
"""

from __future__ import annotations

from dataclasses import dataclass

from .memory_record import MemoryRecord


@dataclass(frozen=True, slots=True)
class KnowledgeRecord:
    """
    Extracted project knowledge.
    """

    memory: MemoryRecord

    domain: str

    rule: str
