---
name: create_skill
description: Automates the creation of professional-grade Antigravity skills. Incorporates best practices for progressive disclosure, resource organization, and automatic agent registration.
---

# Create Skill

Use this skill to define a new capability for Antigravity. It enforces a professional structure inspired by industry best practices (conciseness, progressive disclosure, and modularity).

## Workflow

### 1. Design & Strategy
Before creating files, ask the user (or deduce from context):
*   **Trigger**: What specifically should trigger this skill? (This goes into the `description`).
*   **Complexity**:
    *   *Simple*: Just a `SKILL.md` checklist.
    *   *Complex*: Needs `scripts/` (for tools) or `references/` (for docs).

### 2. Create Skill Structure
Create the directory at `c:/Users/ADMIN/.gemini/antigravity/global_skills/[skill_name]/`.
Based on **Complexity**, create subfolders if needed:
*   `[skill_name]/scripts/` (Executable code)
*   `[skill_name]/references/` (Documentation)
*   `[skill_name]/assets/` (Templates/Images)

### 3. Write `SKILL.md` (The "Concise" Rule)
*   **Frontmatter**:
    *   `name`: `snake_case_name`
    *   `description`: **CRITICAL**. This is what the AI router reads.
*   **Body**:
    *   **Progressive Disclosure**: Keep it under 500 words. Refactor long context into `references/`.
    *   **Structure**:
        ```markdown
        ---
        name: [skill_name]
        description: [description]
        ---
        
        # [Human Readable Title]
        
        [Instructions, prompts, and steps provided by the user]
        ```

### 4. Register Slash Command (Workflow)
Create the workflow trigger:
*   **Target**: `c:/Users/ADMIN/.gemini/antigravity/global_skills/.agent/workflows/[skill_name].md`
*   **Content**:
    ```markdown
    ---
    description: [Short, action-oriented summary]
    ---
    1. Run the [skill_name] skill.
    ```

### 5. Update README.md
*   **Target**: `c:/Users/ADMIN/.gemini/antigravity/global_skills/README.md`
*   **Action**: Add the new skill to the `## 🛠️ Available Skills` section.
*   **Logic**:
    *   Determine the appropriate category (header) for the skill (e.g., Development, Documentation, Strategy).
    *   If the category exists, append the skill to it.
    *   If not, create a new category header `### [Category Name]` and add the skill there.
    *   **Format**: `* [**[Human Name]**](./[skill_name]/SKILL.md) (/[skill_name]) - [Short description]`

### 6. Final Confirmation
Confirm to the user:
*   Structure created (with any extra folders, if required).
*   Slash command `/[skill_name]` ready.
*   Documentation file `README.md` updated.
