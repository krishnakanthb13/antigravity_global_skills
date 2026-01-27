---
name: open_source_prep
description: Comprehensive workflow to prepare a project for public open-source release. Handles licensing, username normalization, code integrity checks, and documentation generation.
---

# Open Source Release Preparation

This skill guides you through the process of preparing a project for a public GitHub release.

## Inputs
*   **GitHub Username**: The target username for links/licensing.
*   **Project Root**: The directory to prep.

## Tooling Strategy
*   Use `grep_search` to find placeholders (`YOUR_USERNAME`).
*   Use `replace_file_content` to update files.
*   Use `run_command` (curl) to fetch licenses.

## 0. Code Integrity & Feature Verification
**Before touching documentation:**
*   **Verification**: Ensure all major parts of the codebase work together. identify broken flows or unused modules.
*   **Clarification**: Explain all features and their interactions.
*   **Assumptions**: explicitly call out limitations or expected runtime behaviors.

## 1. License Management
*   **Check for `LICENSE` file**:
    *   **If exists**: Add the standard header:
        *   Project Name & one-line description
        *   `Copyright (C) 2026 Krishna Kanth B`
        *   Standard GPL v3 boilerplate notice.
        *   Separator line.
    *   **If missing**: Download GPL v3 text (use `curl https://www.gnu.org/licenses/gpl-3.0.txt`) and prepend the header above.

## 2. Username Standardization
Search and replace the following placeholders with **`krishnakanthb13`**:
*   `YOUR_USERNAME`
*   `your-username`
*   `YOUR-USERNAME`
*   `<username>`

**Scope**: `README.md`, `CONTRIBUTING.md`, config files, scripts, and comments.

## 3. Documentation Suite

### A. CODE_DOCUMENTATION.md
*   *Source inspiration: `codewalkthrough.md` or `code_readme.md` (if they exist).*
*   **Structure**:
    1.  File & Folder structure with descriptions.
    2.  High-level architecture.
    3.  Core modules/functions table.
    4.  Data flow (ASCII/Mermaid diagrams).
    5.  Dependencies (runtime vs dev).
    6.  Execution flow (Entry -> Output).

### B. DESIGN_PHILOSOPHY.md
*   *Source inspiration: `walkthrough.md` or `context_readme.md` (if they exist).*
*   **Content**:
    1.  Problem definition.
    2.  Why this solution?
    3.  Design Principles (Simplicity, Performance, etc.).
    4.  Target Audience & Use Cases.
    5.  Real-world workflow fit.
    6.  Trade-offs & Constraints.

### C. CONTRIBUTING.md
*   *Create if missing.*
*   **Content**:
    1.  Bug reporting formats.
    2.  Feature suggestion process.
    3.  Workflow: Fork -> Branch -> PR.
    4.  Local dev setup.
    5.  Pre-submission checklist (Testing/Validation).

## 4. Final Polish
*   **Gitignore**: Ensure secrets, logs, and artifacts are ignored.
*   **References**: Verify all file paths in docs are accurate.
*   **Badges**: Add GPL v3 badge to `README.md`.
*   **Consistency**: Ensure consistent naming and tone across all files.

## Metadata
*   **GitHub Username**: `krishnakanthb13`
*   **Copyright Holder**: `Krishna Kanth B`
