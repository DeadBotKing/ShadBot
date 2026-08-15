"""
ShadBot Project Intelligence

Package Builder
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.package.package_layout import (
    PackageLayout,
)
from projectintelligence.package.package_manifest import (
    PackageManifest,
)
from projectintelligence.package.package_metadata import (
    PackageMetadata,
)
from projectintelligence.package.package_writer import (
    PackageWriter,
)


@dataclass(frozen=True, slots=True)
class PackageBuildResult:
    """
    Result of package build operation.
    """

    package_path: Path

    metadata: PackageMetadata

    manifest: PackageManifest


class PackageBuilder:
    """
    Builds Project Intelligence packages.
    """

    def __init__(
        self,
        writer: PackageWriter,
    ) -> None:
        self._writer = writer

    def build(
        self,
        layout: PackageLayout,
        metadata: PackageMetadata,
        manifest: PackageManifest,
    ) -> PackageBuildResult:
        """
        Build package artifacts.
        """

        layout.create()

        self._writer.write(
            path=layout.metadata_file,
            data=metadata,
        )

        self._writer.write(
            path=layout.manifest_file,
            data=manifest,
        )

        return PackageBuildResult(
            package_path=layout.root,
            metadata=metadata,
            manifest=manifest,
        )
