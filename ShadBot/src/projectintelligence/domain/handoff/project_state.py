"""
ShadBot Project Intelligence

Project lifecycle state.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectState:
    """
    Current project development state.
    """

    completed_tasks: tuple[str, ...] = ()

    active_tasks: tuple[str, ...] = ()

    pending_tasks: tuple[str, ...] = ()

    blockers: tuple[str, ...] = ()

    decisions: tuple[str, ...] = ()

    def to_dict(
        self,
    ) -> dict[str, object]:

        return {
            "completed_tasks": list(
                self.completed_tasks,
            ),
            "active_tasks": list(
                self.active_tasks,
            ),
            "pending_tasks": list(
                self.pending_tasks,
            ),
            "blockers": list(
                self.blockers,
            ),
            "decisions": list(
                self.decisions,
            ),
        }
