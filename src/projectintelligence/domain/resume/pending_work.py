"""
ShadBot Project Intelligence

Pending Work
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PendingWork:
    """
    Represents a unit of work that is still pending.

    Pending work describes unfinished milestones, planned
    implementations, or required architectural tasks that
    should be completed in future revisions.
    """

    title: str

    description: str

    category: str

    priority: str

    reason: str
