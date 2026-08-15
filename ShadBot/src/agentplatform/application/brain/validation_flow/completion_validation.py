"""
ShadBot Agent Platform

Completion Validation component for 5.10 Validation Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .output_validation import OutputValidationResult
from .quality_check import QualityCheckResult
from .requirement_verification import RequirementVerificationResult


@dataclass(frozen=True, slots=True)
class CompleteValidationPackage:
    fully_validated: bool
    output_val: OutputValidationResult
    quality_chk: QualityCheckResult
    req_ver: RequirementVerificationResult


class ValidationFlowService:
    """
    Orchestrates output validation, quality check, and requirement verification.
    """

    def validate_all(
        self,
        files: tuple[str, ...],
        passed_tests: int,
        total_tests: int,
        instructions: str,
        delivered_capabilities: tuple[str, ...],
    ) -> CompleteValidationPackage:
        from .output_validation import OutputValidator
        from .quality_check import QualityChecker
        from .requirement_verification import RequirementVerifier

        out_res = OutputValidator().validate(files)
        qual_res = QualityChecker().check(passed_tests, total_tests)
        req_res = RequirementVerifier().verify(instructions, delivered_capabilities)

        fully_valid = out_res.valid and qual_res.passed and req_res.satisfied
        return CompleteValidationPackage(
            fully_validated=fully_valid,
            output_val=out_res,
            quality_chk=qual_res,
            req_ver=req_res,
        )
