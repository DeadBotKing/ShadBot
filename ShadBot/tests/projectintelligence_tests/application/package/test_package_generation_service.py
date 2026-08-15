"""
ShadBot Project Intelligence

Package Generation Service Tests
"""

from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from projectintelligence.application.package.package_generation_service import (
    PackageGenerationService,
)
from projectintelligence.package.package_builder import (
    PackageBuilder,
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


def test_package_generation_service_creates_package(
    tmp_path: Path,
) -> None:
    """
    Package generation service should create a package.
    """

    service = PackageGenerationService(
        builder=PackageBuilder(
            writer=PackageWriter(),
        ),
    )

    metadata = PackageMetadata(
        project_id=uuid4(),
        project_name="DemoProject",
    )

    result = service.generate(
        output_directory=tmp_path,
        metadata=metadata,
        manifest=PackageManifest(),
    )

    assert result.package_path.exists()
    assert result.metadata.project_name == "DemoProject"
