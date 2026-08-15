# ShadBot Agent Platform
# Autonomous Self-Hosting / Meta-Agent Execution Guide

Version: 1.0.0-Enterprise-Production  
Date: 2026-08-10  
Status: Official Meta-Agent Bootstrapping Specification

---

## 1. What is Self-Hosting / Meta-Agent Mode?

In compiler theory, **bootstrapping** (or self-hosting) occurs when a compiler can compile its own source code.
In Autonomous AI Engineering, **Meta-Agent Mode** occurs when an AI Agent Platform can read its own architectural specifications, understand its own development rules, and autonomously generate, refactor, or build its own platform codebase from start to finish.

**ShadBot Agent Platform V1.0** is natively capable of operating in **Meta-Agent Mode** to autonomously implement or evolve `src/agentplatform/` using the specification documents in `docs/`.

---

## 2. How ShadBot Reads and Understands `docs/`

When ShadBot operates in Meta-Agent Mode:
1. **Document Intake (`Project Intelligence Agent`)**:
   - The agent reads `docs/doc/DEVELOPMENT_RULES.md` to internalize mandatory Clean Architecture rules (`Presentation -> Application -> Domain <- Infrastructure`).
   - The agent reads `docs/doc/ARCHITECTURE_HANDOFF.md` and `docs/doc/CONTRACT_REGISTRY.md` to understand layer boundaries and immutable contract interfaces.
2. **Phase-by-Phase Roadmap Execution (`Architect & Engineer Agents`)**:
   - For each phase in `docs/Phases/Phase X/`:
     - It reads `Handoff X.txt` and `Phase X.txt`.
     - It designs the Domain interfaces in `src/agentplatform/domain/`.
     - It implements the stateless Application services in `src/agentplatform/application/`.
     - It creates exhaustive unit tests in `tests/agentplatform_tests/`.
3. **Quality Gate Verification (`Reviewer & QA Agents`)**:
   - After generating each phase, it runs pytest and syntax checks to guarantee 100% Green test execution before proceeding to the next phase.

---

## 3. Step-by-Step Instructions to Run Self-Implementation on Windows

To have ShadBot autonomously read your `docs/` directory and rebuild/implement the platform:

### 3.1 Prepare the Target Workspace
In `ShadBotWorkspace/`, create a project folder named `ShadBotCore`:
```text
ShadBotWorkspace\ShadBotCore\
├── docs\               <--- (Copy the entire docs/ folder containing all Handoffs)
├── src\                <--- (Empty or skeleton src/ directory)
└── tasks\
    └── backlog.yaml    <--- (Meta-Agent Task Definition)
```

### 3.2 Create the Meta-Agent Task (`backlog.yaml`)
Place the following manifest inside `ShadBotWorkspace\ShadBotCore\tasks\backlog.yaml`:

```yaml
tasks:
  - id: "c1111111-1111-1111-1111-111111111111"
    phase: "phase_1_to_12"
    title: "Autonomous Implementation of ShadBot Agent Platform"
    description: |
      You are an Autonomous AI Engineering Platform operating in Self-Hosting / Meta-Agent mode.
      Implement the complete ShadBot Agent Platform from Phase 1 through Phase 12.
      
      Instructions:
      1. Document Intake: Read 'docs/doc/DEVELOPMENT_RULES.md' and enforce Clean Architecture (Domain-First, Contract-First).
      2. Sequential Implementation: Read each 'docs/Phases/Phase X/Handoff X.txt' and implement:
         - Domain entities and contracts in 'src/agentplatform/domain/'
         - Stateless application services in 'src/agentplatform/application/'
         - Complete unit tests in 'tests/agentplatform_tests/'
      3. Quality Gate: Execute automated validation after each phase to guarantee zero regressions.
    type: "full_lifecycle"
    priority: "critical"
    status: "pending"
```

### 3.3 Ensure High-Precision LLM Configuration
In PowerShell, verify that Ollama is serving the high-precision 14B Qwen model:
```powershell
ollama run qwen2.5-coder-14b-dev:latest
```

### 3.4 Execute Meta-Agent Implementation
Run the agent runner against `ShadBotCore`:
```powershell
$env:PYTHONPATH="src"
python run_agent.py --project ShadBotCore
```

The platform will sequentially read the `docs/` specifications, reason over Clean Architecture rules, write the implementation files to disk, and validate the test suite autonomously.
