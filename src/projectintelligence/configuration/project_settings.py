"""
Project Intelligence

Project Configuration Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ProjectSettings:
    """
    Main project configuration.

    Defines target project information.
    """

    project_name: str
    workspace: str

    storage_path: str
    reports_path: str
    history_path: str
    cache_path: str
    exports_path: str
