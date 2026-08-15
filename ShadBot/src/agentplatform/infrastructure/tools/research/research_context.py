"""
ShadBot Agent Platform

Research Execution Context
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from .research_operation import ResearchOperation


@dataclass(frozen=True, slots=True)
class ResearchContext:
    """
    Context required for research execution.
    """

    project_id: UUID

    agent_role: str

    operation: ResearchOperation

    query: str

    sources: tuple[str, ...] = ()
