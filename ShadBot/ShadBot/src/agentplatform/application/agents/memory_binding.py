"""
ShadBot Agent Platform

Agent Memory Binding
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.brain.brain_memory import (
    BrainMemory,
)


@dataclass(frozen=True, slots=True)
class MemoryBinding:
    """
    Memory capability attached to an agent.
    """

    memory: BrainMemory
