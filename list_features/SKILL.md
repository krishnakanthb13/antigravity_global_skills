---
name: list_features
description: Scans the codebase to generate a comprehensive, prompt-based feature list in 'features_listed.md' for recreating the app in any language.
---

# List Features (Recreation Spec)

Use this skill to extract a complete, technically precise blueprint of the application, formatted as a series of prompts that could be used to rebuild the app from scratch.

## Inputs
*   **Project Scope**: The root directory of the application to analyze.
*   **Output File**: `features_listed.md` (default).

## Tooling Strategy
*   Use `list_dir` to map the project structure.
*   Use `view_file` to inspect `README.md`, `CODE_DOCUMENTATION.md` (if available), and key source files (entry points, controllers, UI components).
*   Use `write_to_file` to generate the final Markdown report.

## Workflow

### 1. Analysis (Deep Scan)
*   **Objective**: Understand *exactly* what the app does, not just how it's written.
*   **Sources**:
    *   Documentation (`README.md`, `DESIGN_PHILOSOPHY.md`).
    *   Configuration (`package.json`, `requirements.txt`) to identify tech stack implications.
    *   Source Code: Look for routes, UI components, state management, and database schemas.

### 2. Feature Extration & Prompt Generation
For every identified feature, convert it into a **Technical Prompt**.
*   **Format**: "Implement [Feature Name] using [Input/Constraint]. The system must [Action] when [Trigger]."
*   **Precision**: Use standard technical jargon (e.g., "JWT Authentication", "Responsive Grid Layout", "RESTful Endpoint", "WebSocket Stream").
*   **Completeness**: If a button exists, the feature is "Clickable Button that triggers X". If a background task runs, the feature is "Background Cron Job for X".

### 3. Report Structuring (`features_listed.md`)
Create a file that looks like a specification document for an AI or Developer:

**Structure**:
1.  **Core Architecture**: High-level stack agnostic requirements (e.g., "Client-Server Architecture").
2.  **User Interface (UI)**: Detailed prompts for every page/component (e.g., "Create a dashboard with glassmorphism...").
3.  **Business Logic & Functional Requirements**: (e.g., "Calculate tax based on...").
4.  **Data Persistence**: (e.g., "Schema must support...").
5.  **API & Integration**: (e.g., "Expose GET /api/v1/users...").

### 4. Verification
*   **The "Rebuild Test"**: Ask yourself: "If I gave this file to a stranger, could they build the *exact* same app without seeing the code?"
*   Ensure no hidden features (middleware, schedulers) are missed.

### 5. Final Output
*   Save the file to `features_listed.md` in the project root.
