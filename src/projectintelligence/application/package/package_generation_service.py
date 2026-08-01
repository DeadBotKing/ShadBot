"""
ShadBot Project Intelligence

Package Generation Service
"""

from __future__ import annotations

from pathlib import Path

from projectintelligence.package.package_builder import (
    PackageBuilder,
    PackageBuildResult,
)
from projectintelligence.package.package_layout import (
    PackageLayout,
)
from projectintelligence.package.package_manifest import (
    PackageManifest,
)
from projectintelligence.package.package_metadata import (
    PackageMetadata,
)


class PackageGenerationService:
    """
    Application service responsible for generating
    Project Intelligence packages.
    """

    def __init__(
        self,
        builder: PackageBuilder,
    ) -> None:
        self._builder = builder

    def generate(
        self,
        output_directory: Path,
        metadata: PackageMetadata,
        manifest: PackageManifest,
    ) -> PackageBuildResult:
        """
        Generate a complete intelligence package.
        """

        package_directory = output_directory / metadata.project_name

        layout = PackageLayout(
            root=package_directory,
        )

        return self._builder.build(
            layout=layout,
            metadata=metadata,
            manifest=manifest,
        )
