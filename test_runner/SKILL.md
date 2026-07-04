---
name: test_runner
description: Executes the project's test suite, analyzes failures, and provides fix recommendations.
---

# Test Runner

Use this skill to execute tests and understand *why* they might be failing.

## Inputs
*   **Test Command**: (Optional) Override defaults (e.g., `npm test -- -t "search"`).
*   **Scope**: Specific file or all tests.

## Tooling Strategy
*   Use `run_command` to execute tests.
*   Use `view_file` to read failure logs or source code if tests fail.

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

## E2E Testing Patterns (Advanced)
When running or debugging End-to-End (E2E) tests:
*   **Isolation**: Ensure tests run in complete isolation (dedicated test accounts/data). Do not run destructive tests against production.
*   **Flakiness**: Debug flaky tests by checking for race conditions, unstable DOM selectors, or implicit waits rather than explicit waits.
*   **Tracing**: Utilize artifacts (screenshots, video recordings, network traces) captured during CI/CD failures to reconstruct the test state.
*   **Critical Journeys**: Focus E2E tests on critical user journeys rather than exhaustive edge-case testing (which belongs in unit tests).
