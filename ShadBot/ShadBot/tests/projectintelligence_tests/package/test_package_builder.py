"""
ShadBot Project Intelligence

Package Builder Tests
"""

from __future__ import annotations

import json
from pathlib import Path
from uuid import uuid4

from projectintelligence.package.package_builder import (
    PackageBuilder,
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
from projectintelligence.package.package_writer import (
    PackageWriter,
)


def test_package_builder_creates_package_artifacts(
    tmp_path: Path,
) -> None:
    """
    Package builder should create metadata and manifest files.
    """

    layout = PackageLayout(
        root=tmp_path / "intelligence-package",
    )

    metadata = PackageMetadata(
        project_id=uuid4(),
        project_name="TestProject",
    )

    manifest = PackageManifest()

    builder = PackageBuilder(
        writer=PackageWriter(),
    )

    result = builder.build(
        layout=layout,
        metadata=metadata,
        manifest=manifest,
    )

    assert result.package_path == layout.root

    assert layout.metadata_file.exists()
    assert layout.manifest_file.exists()

    with layout.metadata_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        metadata_content = json.load(file)

    assert metadata_content["project_name"] == "TestProject"

    with layout.manifest_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        manifest_content = json.load(file)

    assert manifest_content["format"] == "project-intelligence-package"
