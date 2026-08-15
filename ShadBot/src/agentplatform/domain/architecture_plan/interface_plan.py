"""
Interface planning model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class InterfacePlan:
    """
    Interface contract definition.
    """

    name: str

    contract: str

    responsibility: str
