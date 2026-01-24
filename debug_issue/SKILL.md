---
name: debug_issue
description: A strict, scientific debugging protocol to isolate, reproduce, and fix software defects without guessing.
---

# Debug Issue Protocol

Use this skill when something isn't working and "trying random things" is not an option.

## Workflow

### 1. Isolation & Symptom Analysis (Triage)
*   **Deviation**: Clearly define the delta between *Expected Behavior* and *Observed Behavior*.
*   **Scope & Context**: Triage the failure domain (Frontend, Backend API, DB Transaction, Network Latency, Race Condition).
*   **Variable Reduction**: Strip away confounding variables. Reduce the system state to the *Minimal Reproducible Example (MRE)*.

### 2. Reproduction (Determinism)
*   **Reproduction Path**: Define a discrete, deterministic sequence of steps (1, 2, 3) to trigger the fault.
*   **Environment Parity**: Verify environment consistency (Dev vs. Prod, OS version, Dependency tree). Is it flaky or 100% reproducible?

### 3. Root Cause Analysis (Instrumentation)
*   **Instrumentation**: "Measure, Don't Guess." Inject telemetry, `console.log`, or breakpoints at critical data boundaries.
*   **State Inspection**: Examine the runtime state, memory heap, or variable values immediately preceding the exception (Pre-crash State).
*   **Stack Trace Analysis**: Traverse the full call stack. Do not ignore inner exceptions or causal chains.

### 4. Patch & Resolution
*   **Root Cause Hypothesis**: Formulate a technical hypothesis: "Component X fails when Input Y occurs because of Logic Z."
*   **Implementation**: Apply the structural fix (avoid "band-aid" patches).

### 5. Verification & Regression
*   **Verification**: Execute the Reproduction Path to confirm the fault is neutralized.
*   **Regression Testing**: Ensure side effects are contained. Run smoke tests or unit tests to guarantee system stability (Reference `enhance_ui` for UI integrity).
