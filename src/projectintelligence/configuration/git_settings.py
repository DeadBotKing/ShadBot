"""
ShadBot Project Intelligence

Git Configuration Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class GitSettings:
    """
    Git repository configuration.
    """

    enabled: bool

    repository_path: str

    branch_name: str

    remote_name: str
