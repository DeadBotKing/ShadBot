from __future__ import annotations

from dataclasses import dataclass, field

from projectintelligence.domain.knowledge.knowledge_finding import (
    KnowledgeFinding,
)


@dataclass(frozen=True, slots=True)
class RuleResult:
    """
    Represents the execution result of a knowledge rule.

    A rule execution may produce zero or more knowledge findings.
    """

    rule_name: str

    findings: tuple[KnowledgeFinding, ...] = field(default_factory=tuple)

    executed: bool = True

    error: str | None = None

    @property
    def has_findings(self) -> bool:
        """
        Indicates whether the rule produced any findings.
        """

        return bool(self.findings)

    @property
    def failed(self) -> bool:
        """
        Indicates whether rule execution failed.
        """

        return self.error is not None
