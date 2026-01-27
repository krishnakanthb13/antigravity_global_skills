# Antigravity Global Skills

This repository contains a collection of custom "skills" for Antigravity, designed to automate common development tasks and enforce standardized workflows.

## � Installation

1.  **Download / Clone**
    *   Clone this repository:
        ```bash
        git clone https://github.com/krishnakanthb13/antigravity_global_skills.git
        ```
    *   **OR** Download the ZIP file and extract it.

2.  **Setup Global Skills**
    *   Navigate to your Antigravity global configuration folder:
        *   **Windows**: `C:\Users\%USERNAME%\.gemini\antigravity\skills\`
        *   **Mac/Linux**: `~/.gemini/antigravity/skills/`
    *   **Move**: Copy the *contents* of the unzipped folder/repo directly into `skills`.
    *   *Result: You should see folders like `code_review` and `.agent` directly inside `skills`.*

## �🚀 How to Use

You can invoke these skills in three ways:

1.  **Slash Commands (Recommended)**
    Simply type `/` in the chat to see a list of available commands. Select the one you want to run.
    *   Example: `/code_review`

2.  **Natural Language**
    Describe what you want to do using keywords from the skill description.
    *   Example: "Can you review this code for bugs?" (Triggers `code_review`)

3.  **Explicit Instruction**
    Tell Antigravity specifically which skill to use.
    *   Example: "Run the **release_helper** skill."

---

## 📂 Directory Structure

*   **/[skill_name]/SKILL.md**: The definition and instructions for a specific skill.
*   **/.agent/workflows/**: Contains the markdown files that map Slash Commands (e.g., `/my_command`) to specific skills.

To create a new skill, simply run:
> `/create_skill`

---

## 🛠️ Available Skills

### Strategy & Planning
*   [**Idea to Action**](./idea_to_action/SKILL.md) (`/idea_to_action`)
    *   Converts raw concepts into execution plans with schedules, risk analysis, and founder-level filtering.
*   [**Daily Log**](./daily_log/SKILL.md) (`/daily_log`)
    *   Scans session work and appends a bulleted summary to `WORK_LOG.md`.
*   [**List Features**](./list_features/SKILL.md) (`/list_features`)
    *   Generates a comprehensive, prompt-based feature list for recreating the app.

### Development Actions
*   [**Code Review**](./code_review/SKILL.md) (`/code_review`)
    *   Comprehensive code analysis, bug hunting, and integrity testing checklist.
*   [**Debug Issue**](./debug_issue/SKILL.md) (`/debug_issue`)
    *   Run a strict 5-step debugging protocol (Isolate -> Repr -> Log -> Fix -> Verify).
*   [**Enhance UI**](./enhance_ui/SKILL.md) (`/enhance_ui`)
    *   Upgrade UI styling and run integrity tests to ensure no code regression.
*   [**Optimize Codebase**](./optimize_codebase/SKILL.md) (`/optimize_codebase`)
    *   Checks for large files (>2k lines) and refactors them into modular folders.
*   [**Create Launcher**](./create_launcher/SKILL.md) (`/create_launcher`)
    *   Generate cross-platform launchers (.bat/.sh) with dependency checks and graceful shutdown.
*   [**Create Skill**](./create_skill/SKILL.md) (`/create_skill`)
    *   The meta-skill to interactively build new skills and automatically generate their slash commands.

### Design & UI/UX
*   [**UI/UX Pro Max**](./ui_ux_pro_max/SKILL.md) (`/ui_ux_pro_max`)
    *   UI/UX design intelligence with searchable database of patterns, styles, and stacks.

### Quality Assurance (Testing & Security)
*   [**Scaffold Tests**](./scaffold_tests/SKILL.md) (`/add_tests`)
    *   Generates unit and regression test shells for existing code.
*   [**Test Runner**](./test_runner/SKILL.md) (`/run_tests`)
    *   Executes the test suite and analyzes results.
*   [**Security Audit**](./security_audit/SKILL.md) (`/security_audit`)
    *   Scans codebase for vulnerabilities and updates `SECURITY.md`.
*   [**Document API**](./document_api/SKILL.md) (`/api_docs`)
    *   Generates API documentation (endpoints, requests, responses).

### Documentation & Release
*   [**Update Docs**](./update_docs/SKILL.md) (`/update_docs`)
    *   Systematically updates `README.md`, `CODE_DOCUMENTATION.md`, and `DESIGN_PHILOSOPHY.md`.
*   [**Open Source Prep**](./open_source_prep/SKILL.md) (`/open_source_prep`)
    *   Prepares a repo for public release: genericizes usernames, checks licenses, and verifies integrity.
*   [**Release Helper**](./release_helper/SKILL.md) (`/release_helper`)
    *   Auto-increments versions, writes emoji-rich `RELEASE_NOTES.md`, and drafts social media posts.
*   [**Generate Release Image**](./generate_release_image/SKILL.md) (`/generate_release_image`)
    *   Creates or edits modern, promotional assets for new versions and saves them to `assets/`.

---

## ℹ️ About Skills Architecture

### Official Documentation
For a complete guide on defining, sharing, and using skills, please refer to the official documentation:
🔗 **[https://antigravity.google/docs/skills](https://antigravity.google/docs/skills)**

**Key Concepts:**
*   **Skills** are specialized instruction sets stored as markdown files (`SKILL.md`) with YAML frontmatter.
*   They "teaching" the agent how to perform specific, repeatable tasks.
*   **Workflows** (stored in `.agent/workflows`) act as triggers or aliases (Slash Commands) for these skills.

### How These Skills Were Created
This repository was bootstrapped using a recursive "Meta-Skill" approach:

1.  **Manual Bootstrap**: We manually defined the first skill, `create_skill`, which contains the logic to write files and folder structures.
2.  **Automation**: Once `create_skill` existed, we used it to generate every other skill in this list (e.g., `code_review`, `release_helper`).
3.  **Result**: A self-expanding system where the agent uses its own tools to extend its capabilities.

### File Format Standard
Every skill follows this strict markdown structure:

```markdown
---
name: [skill_name]
description: [Short 1-sentence description used by the AI router]
---

# [Human Readable Title]

## Workflow
1. [Step 1]
2. [Step 2]...
```
