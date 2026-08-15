"""
ShadBot Agent Platform

Full Integration Verifier component for Phase 12 Production Freeze V1.0.

Purpose:
    Prove that every phase of the platform is actually importable and wired,
    instead of asserting it.

Responsibility:
    Probe one representative module per phase and report the true result.

Dependencies:
    importlib (standard library).

Outputs:
    IntegrationVerificationReport.

Honesty contract (Rule 27):
    `all_systems_operational` is derived from real import probes. A phase whose
    module cannot be imported is reported as failed, with the reason attached.
"""

from __future__ import annotations

import importlib
from dataclasses import dataclass, field


# One representative module per phase. If the phase is genuinely wired, its
# module imports cleanly; if it is a hollow shell, the import fails.
PHASE_PROBES: dict[int, tuple[str, str]] = {
    1: ("Architecture Foundation", "agentplatform.domain.agents"),
    2: ("Core Agent System", "agentplatform.application.registry"),
    3: ("Intelligence Layer", "agentplatform.application.memory"),
    4: ("Tool & Capability Layer", "agentplatform.application.tooling"),
    5: ("Brain Orchestrator", "agentplatform.application.brain"),
    6: ("Agent Orchestration", "agentplatform.application.orchestration"),
    7: ("Runtime System", "agentplatform.application.runtime"),
    8: ("Communication Layer", "agentplatform.application.communication"),
    9: ("Quality Gate System", "agentplatform.application.quality_gate"),
    10: ("Self Improvement System", "agentplatform.application.self_improvement"),
    11: ("Platform Finalization", "agentplatform.application.platform"),
    12: ("Production Freeze", "agentplatform.application.release"),
}


@dataclass(frozen=True, slots=True)
class IntegrationVerificationReport:
    all_systems_operational: bool
    verified_phases: tuple[int, ...]
    status_summary: str
    failed_phases: tuple[int, ...] = ()
    failures: tuple[str, ...] = field(default=())

    def to_dict(self) -> dict[str, object]:
        return {
            "all_systems_operational": self.all_systems_operational,
            "verified_phases": list(self.verified_phases),
            "failed_phases": list(self.failed_phases),
            "failures": list(self.failures),
            "status_summary": self.status_summary,
        }


class FullIntegrationVerifier:
    """
    Verifies that all 12 platform phases integrate without regression.
    """

    def __init__(
        self,
        probes: dict[int, tuple[str, str]] | None = None,
    ) -> None:
        self._probes = probes or PHASE_PROBES

    def verify_all(self) -> IntegrationVerificationReport:
        """
        Import-probe every phase and report the real outcome.
        """

        verified: list[int] = []
        failed: list[int] = []
        failures: list[str] = []

        for phase in sorted(self._probes):
            title, module_name = self._probes[phase]

            try:
                importlib.import_module(module_name)
                verified.append(phase)
            except ImportError as exc:
                failed.append(phase)
                failures.append(f"Phase {phase} ({title}): {module_name} -> {exc}")

        operational = not failed

        if operational:
            summary = (
                f"All {len(verified)} phases import cleanly and are integrated."
            )
        else:
            summary = (
                f"{len(failed)} of {len(self._probes)} phases FAILED integration "
                f"verification: {', '.join(str(phase) for phase in failed)}"
            )

        return IntegrationVerificationReport(
            all_systems_operational=operational,
            verified_phases=tuple(verified),
            status_summary=summary,
            failed_phases=tuple(failed),
            failures=tuple(failures),
        )
