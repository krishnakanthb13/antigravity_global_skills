---
name: optimize_codebase
description: Identifies and refactors monolithic files (>2k lines) into modular, performance-safe component structures.
---

# Optimize Code Base

Use this skill to clean up technical debt by checking for massive source files and logically breaking them down.

## Inputs
*   **Scope**: The directory to scan.
*   **Threshold**: Line count limit (Default: 2000).

## Tooling Strategy
*   Use `list_dir` to see file sizes.
*   Use `view_file_outline` to understand structure before splitting.
*   Use `write_to_file` to create new modular files.

## Workflow

### 1. Analysis (The "Weigh-in")
*   **Scan**: Identify files in the relevant scope (HTML, Python, JS, etc.) that exceed **2,000 lines**.
*   **Assess**: correct functionality is paramount. Does this file *need* to be this big (e.g., a generated asset), or is it just technical debt?
*   **Comprehensive Tech Debt Scan**: 
    *   **Code Debt**: Identify duplicated code (copy-paste), high cyclomatic complexity (>10), deeply nested conditionals (>3 levels), and long methods (>50 lines).
    *   **Architecture Debt**: Look for missing abstractions, circular dependencies, and feature envy.
    *   **Testing Debt**: Check for untested critical paths or brittle, environment-dependent tests.
    *   **Impact Assessment**: Quantify the cost (e.g., "Developer velocity is impacted by changing this logic in 5 places").

### 2. The Refactoring Plan
Before touching any code, propose a strategy:
*   **Target Folder**: Create a new directory named after the monolithic file (e.g., `app.js` -> `app/`).
*   **Modules**: Identify distinct logical blocks (classes, helper functions, distinct UI sections) that can be extracted.
*   **Dependencies**: Map out how these new modules will import/export to each other to avoid circular dependencies.

### 3. Execution (The "Split")
*   **Create Modules**: Move code into smaller, purpose-built files.
*   **Entry Point**: Create an `index` file (or keep the original filename as a shell) that imports and aggregates the new modules, preserving the original external API.
*   **Constraint**: *Do not* change the logic. This is a refactor, not a rewrite.

### 4. Verification
*   **Integrity**: Ensure all imports are resolved.
*   **Functionality**: Run existing tests or walk through the critical path to ensure nothing broke.
*   **Performance**: verify that splitting the file didn't introduce significant load overhead (e.g., excessive network requests in a web context without bundling).
