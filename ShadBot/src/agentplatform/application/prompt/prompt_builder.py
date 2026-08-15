"""
ShadBot Agent Platform

Prompt builder.

Purpose:
    Turn an execution context into the text sent to the LLM.

Two modes:
    1. General agent prompt - the full context dump, used by researcher,
       architect, reviewer and friends where breadth is the point.

    2. Focused per-file code generation prompt - used when the engineer is
       implementing ONE module.

Why mode 2 exists:
    The general prompt embeds the whole task description, metadata,
    intelligence context and memory context. When the engineer generated 11
    different modules, those 11 prompts were measured at 96.4% similar: the
    only difference was one `Instructions` line buried in a wall of text. The
    model therefore returned the SAME response 8 times (1746 chars each),
    every response overwrote the same 5 files, and 659 seconds produced 32
    lines of code.

    A focused prompt puts the target file first, states its single
    responsibility, and omits everything the model cannot act on.

Design rules honoured:
    - Rule 27: no fake implementations.
    - Rule 18: failures are reported, not swallowed.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext

# Metadata keys that switch the builder into focused single-file mode.
CODEGEN_FILE_KEY = "codegen_target_file"
CODEGEN_PURPOSE_KEY = "codegen_target_purpose"
CODEGEN_SIBLINGS_KEY = "codegen_sibling_files"

_MAX_CONTEXT_CHARS = 600


def _clip(value: object, limit: int = _MAX_CONTEXT_CHARS) -> str:
    """
    Render a context value without letting it swamp the prompt.
    """

    text = str(value).strip()

    if not text or text in {"{}", "[]", "None"}:
        return ""

    if len(text) <= limit:
        return text

    return text[:limit].rstrip() + " ...[truncated]"


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

        Returns a focused single-file prompt when the context carries a
        code generation target, otherwise the general agent prompt.
        """

        target_file = context.metadata.get(CODEGEN_FILE_KEY)

        if target_file:
            return self._build_codegen_prompt(
                context=context,
                target_file=str(target_file),
            )

        return self._build_general_prompt(
            role=role,
            context=context,
        )

    def _build_codegen_prompt(
        self,
        context: AgentExecutionContext,
        target_file: str,
    ) -> str:
        """
        Build a prompt for implementing exactly one module.
        """

        purpose = str(
            context.metadata.get(CODEGEN_PURPOSE_KEY, "")
        ).strip() or "Implement this module."

        siblings = context.metadata.get(CODEGEN_SIBLINGS_KEY) or []

        sibling_block = ""

        if siblings:
            listed = "\n".join(f"- {path}" for path in siblings)
            sibling_block = (
                "\nOther modules in this project (import from them when "
                f"needed, do NOT re-implement them):\n{listed}\n"
            )

        feedback = _clip(context.metadata.get("review_feedback", ""))

        feedback_block = ""

        if feedback:
            feedback_block = (
                "\nThe previous attempt at this file was rejected. Fix these "
                f"issues:\n{feedback}\n"
            )

        project_goal = _clip(context.task_title, 200)

        module_name = target_file.rsplit("/", 1)[-1]

        layer = self._infer_layer(target_file)

        return f"""Write ONE Python file: {module_name}

FULL PATH:
{target_file}

WHAT {module_name} MUST DO (this and nothing else):
{purpose}

{layer}
PROJECT (context only, do not implement all of it here):
{project_goal}
{sibling_block}{feedback_block}
HARD REQUIREMENTS:
- Output ONLY the code for {target_file}. Nothing else.
- Do NOT write other modules in this response.
- Do NOT emit "# path/to/other_file.py" section headers.
- Every function and method needs PEP 484 type annotations.
- Every module, class and public function needs a docstring.
- Domain layer classes must be immutable: use
  @dataclass(frozen=True).
- Import what you use. Every name you reference must be defined or imported
  in THIS file.
- No placeholder bodies. No `pass` where logic belongs. No TODO comments.
  If you cannot implement something, raise NotImplementedError with a message
  explaining what is missing.
- The code must run. A caller must be able to import this module and use it
  without a TypeError or AttributeError.

Return the file contents inside a single ```python code block."""

    @staticmethod
    def _infer_layer(target_file: str) -> str:
        """
        Derive Clean Architecture rules for the layer this file belongs to.

        This also differentiates prompts: without it every per-file prompt
        shares the same boilerplate and the model cannot tell the requests
        apart.
        """

        path = target_file.replace("\\", "/").lower()

        if "/domain/" in path:
            return (
                "LAYER: DOMAIN (innermost).\n"
                "- Pure Python. No I/O, no HTTP, no filesystem, no database.\n"
                "- MUST NOT import from application/ or infrastructure/.\n"
                "- Entities and value objects MUST be "
                "@dataclass(frozen=True).\n"
                "- Use Enum for fixed sets of values.\n"
            )

        if "/application/" in path:
            return (
                "LAYER: APPLICATION (use cases).\n"
                "- Orchestrates domain objects. Stateless: no mutable "
                "instance state between calls.\n"
                "- May import from domain/. MUST NOT import from "
                "infrastructure/.\n"
                "- Depend on abstractions; receive collaborators via "
                "__init__ injection.\n"
            )

        if "/infrastructure/" in path:
            return (
                "LAYER: INFRASTRUCTURE (adapters).\n"
                "- Concrete I/O: filesystem, HTTP, subprocess, database.\n"
                "- May import from domain/ and application/.\n"
                "- Never use shell=True. Pass argument lists to subprocess.\n"
                "- Any subprocess call must pass "
                'encoding="utf-8", errors="replace".\n'
            )

        if path.endswith(("__main__.py", "run.py", "main.py")):
            return (
                "LAYER: ENTRY POINT.\n"
                "- Wire the object graph and call into the application "
                "layer.\n"
                "- Define main() -> int returning an exit code.\n"
                "- Guard execution with if __name__ == '__main__'.\n"
                "- Running this file MUST NOT raise. Verify every call you "
                "make against the module you import it from.\n"
            )

        if "/tests/" in path or path.rsplit("/", 1)[-1].startswith("test_"):
            return (
                "LAYER: TESTS.\n"
                "- Use pytest. Plain asserts, no unittest classes.\n"
                "- Each test asserts one real behaviour. No trivial "
                "assert True.\n"
            )

        return "LAYER: general module.\n"

    def _build_general_prompt(
        self,
        role: AgentRole,
        context: AgentExecutionContext,
    ) -> str:
        """
        Build the broad, context-rich prompt for non-codegen agents.
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
{_clip(context.intelligence_context)}

Agent Memory Context:
{_clip(context.memory_context)}

Metadata:
{_clip(context.metadata)}

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
