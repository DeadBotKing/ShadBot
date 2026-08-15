"""
ShadBot Agent Platform

Memory Injection Result
"""

from __future__ import annotations

from dataclasses import dataclass

from .injected_memory import InjectedMemory


@dataclass(frozen=True, slots=True)
class MemoryInjectionResult:
    """
    Final injected memories.
    """

    injected_memories: tuple[InjectedMemory, ...]

    total_memories: int
