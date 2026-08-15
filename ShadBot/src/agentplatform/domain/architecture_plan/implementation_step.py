"""
Implementation order model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ImplementationStep:
    """
    Ordered implementation step.
    """

    order: int

    description: str
