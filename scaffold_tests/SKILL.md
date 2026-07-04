---
name: scaffold_tests
description: Generates unit and regression test files for existing code. Creates "Happy Path", "Edge Case", and "Error" test stubs.
---

# Scaffold Tests

Use this skill to automatically generate test suites for your code, ensuring functionality is locked in.

## Inputs
*   **Target File**: The source code specific to test.
*   **Test Runner**: (Optional) Jest, Pytest, etc.

## Tooling Strategy
*   Use `view_file` to analyze the source code.
*   Use `write_to_file` to create the test file.

## Workflow

### 1. Context Analysis
*   **Target**: Analyze the open file or the specified module (e.g., `utils.py`, `auth.js`).
*   **Framework Detection**: Determine the project's test runner (Jest, PyTest, Mocha, Unittest). If none, suggest the most lightweight option suitable for the user's legacy hardware.

### 2. Test Strategy
Plan the test coverage:
*   **Unit Tests**: Isolated tests for individual functions/classes.
*   **Regression Tests**: Tests that ensure specific bugs (fixes) don't reappear.
*   **Naming Convention**: Standardize names (e.g., `[filename].test.js` or `test_[filename].py`).

### 3. Generation (The "Safety Net")
Write the test file with three specific sections:
*   **Happy Path**: Standard inputs produce standard outputs (The "It works" check).
*   **Edge Cases**: Nulls, empty strings, zeros, huge numbers (The "Robustness" check).
*   **Error Handling**: Invalid inputs trigger the expected error messages (The "Security" check).

### 4. Output
*   Save the file to a `tests/` directory or alongside the source code (based on project convention).
*   Prompt the user to run them using `/run_tests`.

## Advanced Testing Patterns
*   **Test-Driven Development (TDD)**: Write failing test FIRST, implement minimal code to pass, refactor after green. Never write production code without a failing test.
*   **Behavior-Driven Testing**: Test behavior, not implementation details. Focus on public APIs and business requirements. Use descriptive test names that describe the behavior.
*   **Factory Pattern**: When scaffolding tests, create data factory functions (e.g., `getMockUser(overrides)`) that provide sensible defaults but allow tests to override specific properties. This keeps tests DRY and maintainable.
*   **Mocking Strategies**: Use factory functions to mock entire modules or specific hooks when scaffolding tests to isolate the unit under test.
