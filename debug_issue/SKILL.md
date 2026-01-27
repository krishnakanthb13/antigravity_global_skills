---
name: debug_issue
description: A strict, scientific debugging protocol (The "Iron Law"). No fixes allowed without root cause investigation.
---

# Systematic Debugging (The Iron Law)

**Core Principle**: NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.
Symptom patching is failure.

## Inputs
*   **Issue Description**: What is broken?
*   **Observed Behavior**: What is happening instead?
*   **Stack Trace/Logs**: (Optional) Error output.

## Tooling Strategy
*   Use `grep_search` to find error messages in code.
*   Use `view_file` to inspect logic.
*   Use `run_command` to run reproduction scripts.

## Workflow

### 1. Isolation & Symptom Analysis
*   **Deviation**: Clearly define `Expected` vs `Observed`.
*   **Error Messages**: Read the ENTIRE stack trace. Do not skim.
*   **Environment**: Dev vs Prod? Recent changes?

### 2. Reproduction (The MRE)
*   **Steps**: List the exact steps to fail.
*   **Determinism**: Is it 100% consistent or flaky?
*   **MRE**: Create a Minimal Reproducible Example (strip away everything else).

### 3. Root Cause Investigation (The "Why")
*   **Trace Data Flow**: Follow the bad value backwards. Where did it originate?
*   **Instrumentation**: "Measure, Don't Guess." Add logs at boundaries.
*   **Hypothesis**: Formulate: "I think X fails because Y."

### 4. Implementation (The Fix)
*   **The 3-Strike Rule**: If you have tried 3 fixes and they failed, STOP.
    *   *Observation*: You likely have an architecture problem, not a bug.
    *   *Action*: Question the fundamental pattern.
*   **Single Change**: Apply ONE fix. Test it.

### 5. Verification & Regression
*   **Verify**: Does the MRE pass now?
*   **Regression**: Did anything else break? Run `enhance_ui` or standard tests.

## Rationalization Busting
If you catch yourself saying these, STOP and return to Step 1:
*   "I'll just try this quickly..."
*   "It's probably X..."
*   "I don't know why this works but it does."
