"""
ShadBot Agent Platform

Artifact lifecycle status.
"""

from __future__ import annotations

from enum import Enum


class ArtifactStatus(str, Enum):
    """
    Generated artifact states.
    """

    CREATED = "created"

    WRITTEN = "written"

    FAILED = "failed"

    REPLACED = "replaced"
