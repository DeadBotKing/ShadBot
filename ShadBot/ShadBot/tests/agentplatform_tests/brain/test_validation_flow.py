"""
ShadBot Agent Platform

Unit tests for 5.10 Validation Flow.
"""

from __future__ import annotations

from agentplatform.application.brain.validation_flow import (
    OutputValidator,
    QualityChecker,
    RequirementVerifier,
    ValidationFlowService,
)


def test_output_validator_checks_extensions() -> None:
    res = OutputValidator().validate(["src/main.py", "README.md"])
    assert res.valid is True
    res_bad = OutputValidator().validate(["src/main.py", "bad.bin"])
    assert res_bad.valid is False


def test_quality_checker_validates_score() -> None:
    chk = QualityChecker().check(95, 100)
    assert chk.passed is True
    assert chk.score == 0.95


def test_requirement_verifier_checks_instructions() -> None:
    ver = RequirementVerifier().verify("Implement feature with tests", ("test_generation",))
    assert ver.satisfied is True


def test_validation_flow_service_validates_package() -> None:
    service = ValidationFlowService()
    pkg = service.validate_all(
        files=("src/main.py",),
        passed_tests=10,
        total_tests=10,
        instructions="Implement API",
        delivered_capabilities=("code_generation",),
    )
    assert pkg.fully_validated is True
