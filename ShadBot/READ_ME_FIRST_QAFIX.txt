SHADBOT QAFIX PATCH — 2026-08-13
================================

ML_SCIENTIST is fixed. The pipeline now dies at QA with an EMPTY error:

    [AGENT COMPLETED: QA] Status: FAILED
    [AGENT ERROR]

CAUSE
-----
QA calls QualityValidator, which runs `ruff check .`, `black --check .`,
`mypy src`, and `pytest`. TerminalTool used to do:

    raise RuntimeError(stderr.strip())

Ruff/black/pytest write findings to STDOUT and leave STDERR empty, so
the exception message is "" and the orchestrator prints a blank error
then ABORT_EXECUTION. Reviewer never runs.

This patch:
- QualityValidator never raises; it reports PASS/FAIL per check
- TerminalTool includes stdout (or exit code) when stderr is empty
- QA captures tool errors as findings and completes the workflow
- Reviewer also uses the same safe tool wrapper

INSTALL
-------
1. Extract this zip. You get qafix\ShadBot\...
2. Copy qafix\ShadBot\* over:
      C:\Users\DeadBotKing\Desktop\ShadBot-fixed\ShadBot\
   Choose Replace.
3. Clear pycache:

      Remove-Item -Recurse -Force .\src\agentplatform\infrastructure\tools\__pycache__ -ErrorAction SilentlyContinue
      Remove-Item -Recurse -Force .\src\agentplatform\infrastructure\agents\__pycache__ -ErrorAction SilentlyContinue

4. python run_agent.py

You should see:

    SHADBOT BUILD: 2026-08-13-qafix
    [QA] build=2026-08-13-qafix validating ...
    [AGENT COMPLETED: QA] Status: SUCCESS
