"""
ShadBot Project Intelligence

Framework Detector
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.application.contracts.analysis.framework_detector import (
    IFrameworkDetector,
)
from projectintelligence.application.framework.framework_registry import (
    FrameworkRegistry,
)
from projectintelligence.application.framework.signature_matcher import (
    SignatureMatcher,
)


@dataclass(slots=True)
class FrameworkDetector(IFrameworkDetector):
    """
    Detects frameworks used by a software project.
    """

    framework_registry: FrameworkRegistry
    signature_matcher: SignatureMatcher

    def detect(
        self,
        files: list[Path],
    ) -> list[str]:
        """
        Detect project frameworks.
        """

        detected: list[str] = []

        for signature in self.framework_registry.signatures():
            if self.signature_matcher.matches(
                signature=signature,
                files=files,
            ):
                detected.append(signature.framework)

        return detected
