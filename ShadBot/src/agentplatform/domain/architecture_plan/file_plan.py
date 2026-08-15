"""
File planning model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FilePlan:
    """
    Planned file modification.
    """

    path: str

    action: str

    purpose: str
