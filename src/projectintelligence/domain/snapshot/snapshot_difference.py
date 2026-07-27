"""
ShadBot Project Intelligence

Snapshot Difference
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SnapshotDifference:
    """
    Represents the differences between two project snapshots.
    """

    added_files: list[str] = field(default_factory=list)

    removed_files: list[str] = field(default_factory=list)

    modified_files: list[str] = field(default_factory=list)

    added_dependencies: dict[str, str] = field(default_factory=dict)

    removed_dependencies: dict[str, str] = field(default_factory=dict)

    updated_dependencies: dict[str, str] = field(default_factory=dict)

    language_changes: list[str] = field(default_factory=list)

    framework_changes: list[str] = field(default_factory=list)

    architecture_changed: bool = False

    git_changed: bool = False

    breaking_changes: list[str] = field(default_factory=list)
