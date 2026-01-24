---
name: test_runner
description: Executes the project's test suite, analyzes failures, and provides fix recommendations.
---

# Test Runner

Use this skill to execute tests and understand *why* they might be failing.

## Workflow

### 1. Execution
*   **Command**: Run the appropriate test command for the environment (e.g., `npm test`, `pytest`, `python -m unittest`).
*   **Scope**: Run all tests by default, or target a specific file if requested.

### 2. Analysis
*   **Pass**: If all green, celebrate! 🟢
*   **Fail**: If red 🔴, analyze the output:
    *   **StackTrace**: Where exactly did it blow up?
    *   **Assertion**: What was expected vs. what was received?
    *   **Diff**: Visual comparison of the data mismatch.

### 3. Recommendation
*   If tests failed, provide a summary of the failure.
*   Suggest potential fixes or point to the line of code causing the regression.

### 4. Integrity
*   Ensure that the testing process didn't leave behind artifacts (temp files, database entries) unless intended for debugging.
