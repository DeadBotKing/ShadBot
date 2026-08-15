"""
ShadBot Project Intelligence

Snapshot Difference Service
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.snapshot.architecture_difference_service import (
    ArchitectureDifferenceService,
)
from projectintelligence.application.snapshot.dependency_difference_service import (
    DependencyDifferenceService,
)
from projectintelligence.application.snapshot.framework_difference_service import (
    FrameworkDifferenceService,
)
from projectintelligence.application.snapshot.git_difference_service import (
    GitDifferenceService,
)
from projectintelligence.application.snapshot.language_difference_service import (
    LanguageDifferenceService,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.domain.snapshot.snapshot_difference import (
    SnapshotDifference,
)


@dataclass(slots=True)
class SnapshotDifferenceService:
    """
    Coordinates snapshot comparison services.
    """

    dependency_difference: DependencyDifferenceService

    language_difference: LanguageDifferenceService

    framework_difference: FrameworkDifferenceService

    architecture_difference: ArchitectureDifferenceService

    git_difference: GitDifferenceService

    def compare(
        self,
        previous: ProjectSnapshot,
        current: ProjectSnapshot,
    ) -> SnapshotDifference:

        difference = SnapshotDifference()

        difference.added_files = sorted(
            set(current.file_hashes) - set(previous.file_hashes),
        )

        difference.removed_files = sorted(
            set(previous.file_hashes) - set(current.file_hashes),
        )

        difference.modified_files = sorted(
            file
            for file in (set(previous.file_hashes) & set(current.file_hashes))
            if previous.file_hashes[file] != current.file_hashes[file]
        )

        self.dependency_difference.compare(
            previous.dependencies,
            current.dependencies,
            difference,
        )

        self.language_difference.compare(
            previous.detected_languages,
            current.detected_languages,
            difference,
        )

        self.framework_difference.compare(
            previous.detected_frameworks,
            current.detected_frameworks,
            difference,
        )

        self.architecture_difference.compare(
            previous.architecture_tree,
            current.architecture_tree,
            difference,
        )

        self.git_difference.compare(
            previous.git_commit,
            current.git_commit,
            previous.git_branch,
            current.git_branch,
            difference,
        )

        return difference
