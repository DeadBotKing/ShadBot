"""
ShadBot Agent Platform

Architecture file model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ArchitectureFile:
    """
    Represents a file defined by architecture planning.
    """

    path: str

    content: str
