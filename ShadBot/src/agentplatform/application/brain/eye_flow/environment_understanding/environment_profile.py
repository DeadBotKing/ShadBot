"""
ShadBot Agent Platform

Environment Profile
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class EnvironmentProfile:
    """
    Describes detected workspace environment.
    """

    operating_system: str

    workspace_path: Path

    languages: tuple[str, ...]

    frameworks: tuple[str, ...]

    tools: tuple[str, ...]

    runtime_versions: dict[str, str]
