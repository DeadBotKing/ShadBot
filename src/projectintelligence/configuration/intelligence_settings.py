"""
ShadBot Project Intelligence

Intelligence Configuration Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class IntelligenceSettings:
    """
    Core intelligence engine configuration.
    """

    enable_architecture_analysis: bool

    enable_dependency_analysis: bool

    enable_git_analysis: bool

    enable_test_analysis: bool

    enable_change_analysis: bool