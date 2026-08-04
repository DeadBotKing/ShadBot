"""
ShadBot Agent Platform

Architecture directory model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ArchitectureDirectory:
    """
    Represents a directory defined by architecture planning.
    """

    path: str
