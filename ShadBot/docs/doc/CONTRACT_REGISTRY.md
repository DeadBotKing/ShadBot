\# ShadBot Agent Platform

\# Contract Registry



Version: 1.0



Status: Official Contract Registry





\# Purpose



This document defines every public contract that exists inside the Agent Platform.



A contract is the only legal communication boundary between modules.



Nothing may bypass these contracts.



Every implementation must satisfy its contract.



Every future module must register its contracts here.





\---



\# Architecture Rule



Communication is always:



Presentation

&#x20;       ↓

Application

&#x20;       ↓

Domain Contracts

&#x20;       ↓

Infrastructure Implementations





Infrastructure NEVER owns business logic.



Domain NEVER imports Infrastructure.



Application ONLY depends on contracts.



Infrastructure implements contracts.





====================================================================

SECTION 1

GOAL EXECUTION CONTRACTS

====================================================================





IGoalIntake



Purpose



Receive a raw goal from Task Intake.



Input



Raw Task



Output



Goal





\--------------------------------------------------





IGoalUnderstanding



Purpose



Transform Goal into semantic representation.



Input



Goal



Output



Goal Intent





\--------------------------------------------------





IGoalLifecycleManager



Purpose



Manage goal lifecycle.



States



Created



Active



Paused



Completed



Failed



Cancelled





\--------------------------------------------------





IGoalTracker



Purpose



Track current goal progress.





\--------------------------------------------------





IGoalCompletionDetector



Purpose



Detect completion conditions.





====================================================================

SECTION 2

CONTEXT CONTRACTS

====================================================================





IContextCollector



Purpose



Collect every available context.





Sources



Workspace



Memory



Goal



Profile



Runtime



History



Project





\--------------------------------------------------





IContextMerger



Purpose



Merge all context.





\--------------------------------------------------





IContextPrioritizer



Purpose



Prioritize context.





\--------------------------------------------------





IContextSnapshot



Purpose



Produce immutable context snapshot.





====================================================================

SECTION 3

MEMORY CONTRACTS

====================================================================





IMemoryRetriever



Purpose



Retrieve memory.





\--------------------------------------------------





IMemoryRanker



Purpose



Rank memories.





\--------------------------------------------------





IMemoryInjector



Purpose



Inject memory into reasoning context.





\--------------------------------------------------





IMemoryUpdater



Purpose



Persist new memories.





====================================================================

SECTION 4

EYE CONTRACTS

====================================================================





IWorkspaceObserver



Purpose



Observe Project Workspace.





Reads



Files



Folders



Git



Artifacts



Tasks



Reports





\--------------------------------------------------





IEnvironmentReader



Purpose



Observe execution environment.





\--------------------------------------------------





IProjectStateReader



Purpose



Read current project state.





\--------------------------------------------------





IVisualContextInjector



Purpose



Inject workspace observations into context.





====================================================================

SECTION 5

REASONING CONTRACTS

====================================================================





IReasoningEngine



Purpose



Perform reasoning.





Input



Goal



Context



Memory



Workspace





Output



Reasoning Result





\--------------------------------------------------





IProblemAnalyzer



Purpose



Analyze problem.





\--------------------------------------------------





IDecisionSupport



Purpose



Generate reasoning support.





\--------------------------------------------------





IReasoningTrace



Purpose



Persist reasoning trace.





====================================================================

SECTION 6

DECISION CONTRACTS

====================================================================





IDecisionGenerator



Purpose



Generate decision.





\--------------------------------------------------





IDecisionEvaluator



Purpose



Evaluate candidate decisions.





\--------------------------------------------------





IDecisionApproval



Purpose



Approve execution.





\--------------------------------------------------





IDecisionOutput



Purpose



Publish decision.





====================================================================

SECTION 7

PROFILE CONTRACTS

====================================================================





IAgentProfileLoader



Purpose



Load Agent profile.





\--------------------------------------------------





ICapabilityAwareness



Purpose



Expose capabilities.





\--------------------------------------------------





IBehaviorConstraints



Purpose



Apply profile constraints.





====================================================================

SECTION 8

PLANNING CONTRACTS

====================================================================





ITaskDecomposer



Purpose



Split goal into executable tasks.





\--------------------------------------------------





IExecutionPlanner



Purpose



Build execution plan.





\--------------------------------------------------





IAgentAssignment



Purpose



Assign tasks.





\--------------------------------------------------





IPlanTracker



Purpose



Track execution plan.





====================================================================

SECTION 9

REFLECTION CONTRACTS

====================================================================





IExecutionReviewer



Purpose



Review execution.





\--------------------------------------------------





IFailureAnalyzer



Purpose



Analyze failures.





\--------------------------------------------------





IImprovementSuggestion



Purpose



Generate improvements.





\--------------------------------------------------





ISelfCritique



Purpose



Self evaluation.





====================================================================

SECTION 10

VALIDATION CONTRACTS

====================================================================





IOutputValidator



Purpose



Validate outputs.





\--------------------------------------------------





IQualityChecker



Purpose



Run quality gates.





\--------------------------------------------------





IRequirementVerifier



Purpose



Verify requirements.





\--------------------------------------------------





ICompletionValidator



Purpose



Validate completion.





====================================================================

SECTION 11

LEARNING CONTRACTS

====================================================================





IExperienceExtractor



Purpose



Extract experience.





\--------------------------------------------------





IPatternRecognizer



Purpose



Recognize patterns.





\--------------------------------------------------





IKnowledgeUpdater



Purpose



Update knowledge.





\--------------------------------------------------





IStrategyImprover



Purpose



Improve strategies.





====================================================================

SECTION 12

GOAL \& INTENT CONTRACTS

====================================================================





IIntentDetector



Purpose



Detect intent.





\--------------------------------------------------





IGoalAlignment



Purpose



Align intent with goals.





\--------------------------------------------------





IPriorityManager



Purpose



Manage priorities.





\--------------------------------------------------





IIntentCorrection



Purpose



Correct intent.





====================================================================

SECTION 13

ATTENTION CONTRACTS

====================================================================





IFocusManager



Purpose



Control focus.





\--------------------------------------------------





IContextFiltering



Purpose



Remove irrelevant context.





\--------------------------------------------------





IPriorityAllocator



Purpose



Allocate reasoning priority.





\--------------------------------------------------





IResourceAttention



Purpose



Allocate reasoning resources.





====================================================================

SECTION 14

TASK INTAKE CONTRACTS

====================================================================





IProjectWorkspaceDiscovery



Purpose



Locate Project Workspace.





\--------------------------------------------------





ITaskInputInterface



Purpose



Receive task.





Sources



CLI



API



Scheduler



Workspace





\--------------------------------------------------





ITaskFileReader



Purpose



Read



ProjectWorkspace



└── Tasks



&#x20;     └── task.md





\--------------------------------------------------





ITaskParser



Purpose



Parse Markdown.





\--------------------------------------------------





ITaskNormalizer



Purpose



Normalize task.





\--------------------------------------------------





ITaskStateManager



Purpose



Manage state.





States



Waiting



Running



Paused



Completed



Failed





\--------------------------------------------------





ITaskCompletionReporter



Purpose



Report completion.





====================================================================

SECTION 15

ORCHESTRATION CONTRACTS

====================================================================





IAgentSelector



Purpose



Select agent.





\--------------------------------------------------





IAgentPipeline



Purpose



Manage execution pipeline.





\--------------------------------------------------





IAgentMessenger



Purpose



Inter-agent messaging.





\--------------------------------------------------





IHandoffManager



Purpose



Transfer execution between agents.





====================================================================

SECTION 16

RUNTIME CONTRACTS

====================================================================





IAgentRuntime



Purpose



Agent execution runtime.





\--------------------------------------------------





IBrainRuntime



Purpose



Brain runtime.





\--------------------------------------------------





ISessionRuntime



Purpose



Session lifecycle.





\--------------------------------------------------





IStateManager



Purpose



Runtime state.





\--------------------------------------------------





ICheckpointManager



Purpose



Persist checkpoints.





\--------------------------------------------------





IResumeManager



Purpose



Resume execution.





====================================================================

SECTION 17

QUALITY GATE CONTRACTS

====================================================================





IPytestRunner



IRuffRunner



IBlackRunner



IMypyRunner



ISecurityValidator



IArchitectureValidator





====================================================================

SECTION 18

SELF IMPROVEMENT CONTRACTS

====================================================================





IReflectionAnalyzer



IPerformanceTracker



IExperimentEngine



IImprovementProposal



ILearningUpdater



IBrainEvolution





====================================================================

SECTION 19

PLATFORM CONTRACTS

====================================================================





IConfiguration



ILogger



IDatabase



IPlugin



IDeployment





====================================================================

FINAL RULES

====================================================================



Every contract:



• Must have exactly one responsibility.



• May have multiple implementations.



• Must never depend on Infrastructure.



• Must remain backward compatible after Freeze v1.0.



• Breaking a contract requires architecture version increment.

