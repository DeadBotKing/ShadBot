"""
ShadBot Project Intelligence

Test Framework Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TestFramework:
    """
    Represents detected testing framework.
    """

    name: str

    language: str

    manifest: str
