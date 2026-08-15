"""
ShadBot Agent Platform

Prompt builder.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext


class PromptBuilder:
    """
    Builds prompts for agents.
    """

    def build(
        self,
        role: AgentRole,
        context: AgentExecutionContext,
    ) -> str:
        """
        Create agent prompt.
        """

        review_feedback = context.metadata.get(
            "review_feedback",
            "",
        )

        return f"""
You are an AI software engineering agent.

Role:
{role.value}

Task:
Title:
{context.task_title}

Description:
{context.task_description}

Type:
{context.task_type}

Instructions:
{context.instructions}

Project Intelligence Context:
{context.intelligence_context}

Agent Memory Context:
{context.memory_context}

Metadata:
{context.metadata}

Previous Review Feedback:
{review_feedback}

You are an autonomous software engineering agent.

Your responsibility:
- Analyze the task.
- Make reasonable engineering assumptions when details are missing.
- Do NOT ask questions.
- Do NOT request more information.
- Produce the implementation directly.

If previous review feedback exists:
- Fix all reported issues.
- Improve the previous implementation.
- Do not repeat rejected patterns.

Output requirements:
- Return only the technical solution.
- Prefer production-quality Python code.
- Include necessary classes, functions, and structure.
- Follow clean architecture principles.

Complete the assigned task now.
"""
