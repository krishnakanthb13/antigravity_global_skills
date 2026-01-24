---
name: code_review
description: Comprehensive code review and testing assistant. Focuses on identifying bugs, ensuring code integrity, and detecting errors or potential issues.
---

# Code Review & Testing Skill

This skill guides you through a systematic process to review code, ensuring high quality, stability, and correctness.

## Workflow

When asked to perform a code review or test, follow these steps:

### 1. Analysis & Understanding
*   **Context**: Identify the specific files or code blocks the user wants reviewed.
*   **Intent**: Understand what the code is supposed to do. If it's not clear, ask for clarification.

### 2. Static Analysis & "Linting"
*   **Syntax Errors**: Check for obvious syntax errors that would prevent the code from running.
*   **Typos**: Look for variable name typos, missing imports, or undefined symbols.
*   **Style**: Ensure consistency in formatting (e.g., indentation, naming conventions) matching the existing project style.

### 3. Logic & Bug Detection (The "Bug Hunt")
*   **Edge Cases**: Check how the code handles null/undefined values, empty lists/arrays, or unexpected input types.
*   **Control Flow**: Verify loops (infinite loops?), conditionals (are all cases covered?), and error handling (try-catch blocks).
*   **Concurrency**: If applicable, check for race conditions or deadlocks.
*   **Resource Management**: Check for memory leaks, unclosed file handles, or database connections.

### 4. Code Integrity & Security
*   **Input Validation**: Ensure all external inputs are validated and sanitized.
*   **Dependency Check**: Are there imports of deprecated or insecure libraries?
*   **Logic gaps**: Are there "TODO" comments or placeholder logic that shouldn't be in production?

### 5. Validation (Testing)
*   **Dry Run**: mentally "execute" the code with sample inputs to trace the logic.
*   **Test Cases**: Propose specific test cases (happy path, edge cases, failure modes) that sould be run.
*   **Execution**: If permissions allow (and it's safe), use `run_command` to execute existing tests or creates a temporary test script to validate the code.

## Output Format

Present your findings in a clear, structured manner:

1.  **Summary**: A high-level overview of the code quality.
2.  **Critical Issues**: (If any) bugs that must be fixed immediately.
3.  **Improvements**: Suggestions for better performance, readability, or best practices.
4.  **Nitpicks**: Minor style or formatting issues.
5.  **Test Plan**: A list of recommended tests to verify the fixes.
