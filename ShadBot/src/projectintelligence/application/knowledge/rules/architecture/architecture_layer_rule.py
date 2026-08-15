from __future__ import annotations

from projectintelligence.application.knowledge.rules.base_rule import (
    BaseRule,
)
from projectintelligence.application.knowledge.rules.models.rule_result import (
    RuleResult,
)
from projectintelligence.domain.knowledge.knowledge_finding import (
    KnowledgeFinding,
)
from projectintelligence.domain.knowledge.rule_severity import (
    RuleSeverity,
)


class ArchitectureLayerRule(BaseRule):
    """
    Detects common layered architecture patterns
    inside analyzed project knowledge.
    """

    REQUIRED_LAYERS = {
        "domain",
        "application",
        "infrastructure",
    }

    @property
    def name(self) -> str:
        return "architecture.layer_detection"

    def evaluate(self, context: object) -> RuleResult:
        """
        Analyze available project structure information.

        The rule expects extracted architecture information
        from previous knowledge extraction stages.
        """

        layers = self._extract_layers(context)

        if not layers:
            return RuleResult(
                rule_name=self.name,
            )

        findings: list[KnowledgeFinding] = []

        detected_layers = set(layers)

        if self.REQUIRED_LAYERS.issubset(detected_layers):
            findings.append(
                KnowledgeFinding(
                    rule_name=self.name,
                    category="architecture",
                    title="Layered architecture detected",
                    description=(
                        "Project structure contains domain, "
                        "application and infrastructure layers."
                    ),
                    severity=RuleSeverity.INFO,
                )
            )
        else:
            missing_layers = self.REQUIRED_LAYERS - detected_layers

            findings.append(
                KnowledgeFinding(
                    rule_name=self.name,
                    category="architecture",
                    title="Incomplete layered architecture",
                    description=(
                        "Expected architecture layers are missing: "
                        f"{sorted(missing_layers)}"
                    ),
                    severity=RuleSeverity.WARNING,
                )
            )

        return RuleResult(
            rule_name=self.name,
            findings=tuple(findings),
        )

    @staticmethod
    def _extract_layers(context: object) -> list[str]:
        """
        Extract architecture layers from rule context.

        This adapter remains isolated until ProjectKnowledge
        becomes the final input contract.
        """

        if isinstance(context, dict):
            layers = context.get("layers")

            if isinstance(layers, list):
                return layers

        return []
