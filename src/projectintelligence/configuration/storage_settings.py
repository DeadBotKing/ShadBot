"""
Project Intelligence

Storage Configuration Model
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class StorageSettings:
    """
    Storage locations used by Project Intelligence.
    """

    storage_path: str

    reports_path: str
    history_path: str
    cache_path: str
    exports_path: str