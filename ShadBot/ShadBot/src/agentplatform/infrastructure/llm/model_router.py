"""
ShadBot Agent Platform

LLM model routing optimized for NVIDIA GTX 1050Ti 4GB + Intel i7-10700K 32GB RAM.
By default (SHADBOT_FAST_MODE=1), uses fast 7B models (qwen2.5-coder:7b) that fit inside 4GB VRAM.
Set SHADBOT_FAST_MODE=0 to use heavy 14B models.
"""

from __future__ import annotations

import os
from agentplatform.domain.agents import AgentRole


class ModelRouter:
    """
    Selects LLM model based on agent role and hardware optimization.
    """

    def resolve(
        self,
        role: AgentRole,
    ) -> str:
        fast_mode = os.getenv("SHADBOT_FAST_MODE", "1") == "1"

        # 1. Copilot (Conversational natural language helper)
        if role is AgentRole.COPILOT:
            return "aya23:latest"

        # 2. Reviewer (Code review & quality audits)
        if role is AgentRole.REVIEWER:
            return "codellama7b:latest"

        # 3. QA (Quality Assurance, test generation & verification)
        if role is AgentRole.QA:
            return "codegemma7b:latest"

        # 4. RND (Research & Development experimentation)
        if role is AgentRole.RND:
            return "starcoder2:latest"

        # 5. Runtime Observer (Execution monitoring & anomaly detection)
        if role is AgentRole.RUNTIME_OBSERVER:
            return "mistral7b:latest"

        # 6. Project Intelligence (Eye of the Brain, docs & vision scanner)
        if role is AgentRole.PROJECT_INTELLIGENCE:
            return "qwen2.5-coder:7b"

        # 7. Researcher (Technical & documentation research)
        if role is AgentRole.RESEARCHER:
            return "qwen2.5-coder:7b"

        # 8. Architect (Clean Architecture & system design)
        if role is AgentRole.ARCHITECT:
            return "qwen2.5-coder:7b" if fast_mode else "qwen2.5-coder-14b-dev-16k:latest"

        # 9. Engineer (Source code generation & implementation)
        if role is AgentRole.ENGINEER:
            return "qwen2.5-coder:7b" if fast_mode else "qwen2.5-coder-14b-dev-16k:latest"

        # 10. ML Scientist (Machine Learning evaluation, experiments, retraining)
        if role is AgentRole.ML_SCIENTIST:
            return "qwen2.5-coder:7b" if fast_mode else "qwen2.5-coder-14b-dev-16k:latest"

        # Fallback default for any custom or new role
        return "qwen2.5-coder:7b" if fast_mode else "qwen2.5-coder-14b-dev-16k:latest"
