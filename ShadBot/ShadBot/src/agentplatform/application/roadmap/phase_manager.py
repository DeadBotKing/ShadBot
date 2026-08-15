"""
ShadBot Agent Platform

Phase manager.
"""

from __future__ import annotations

from agentplatform.application.roadmap.roadmap_parser import (
    ProjectPhase,
)


class PhaseManager:
    """
    Manages project phases.
    """

    def get_active_phase(
        self,
        phases: list[ProjectPhase],
    ) -> ProjectPhase | None:
        """
        Return currently running phase.
        """

        for phase in phases:
            if phase.status == "running":
                return phase

        return None
