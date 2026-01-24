---
name: create_skill
description: Automates the creation of new Antigravity skills and their corresponding slash commands.
---

# Create Skill

Use this skill when the user wants to define a new capability or "skill" for Antigravity.

## Workflow

### 1. Gather Information
If the user hasn't provided them, ask for:
*   **Skill Name**: A short, underscore_separated name (e.g., `git_commit`, `test_runner`).
*   **Description**: What the skill does.
*   **Instructions**: The specific steps or prompts to automate.

### 2. Create Skill Structure
Create the directory and instruction file in `c:/Users/ADMIN/.gemini/antigravity/global_skills/`.

*   **Path**: `global_skills/[skill_name]/SKILL.md`
*   **Content Template**:
    ```markdown
    ---
    name: [skill_name]
    description: [description]
    ---
    
    # [Human Readable Title]
    
    [Instructions, prompts, and steps provided by the user]
    ```

### 3. Create Slash Command (Workflow)
Create a workflow file to enable the `/[skill_name]` slash command.

*   **Path**: `c:/Users/ADMIN/.gemini/antigravity/global_skills/.agent/workflows/[skill_name].md`
*   **Content Template**:
    ```markdown
    ---
    description: [Short description for the menu]
    ---
    1. Run the [skill_name] skill.
    ```

### 4. Update README.md
*   **Target**: `c:/Users/ADMIN/.gemini/antigravity/global_skills/README.md`
*   **Action**: Add the new skill to the `## 🛠️ Available Skills` section.
*   **Logic**:
    *   Determine the appropriate category (header) for the skill (e.g., Development, Documentation, Strategy).
    *   If the category exists, append the skill to it.
    *   If not, create a new category header `### [Category Name]` and add the skill there.
    *   **Format**: `* [**[Human Name]**](./[skill_name]/SKILL.md) (/[skill_name]) - [Short description]`

### 5. Confirmation
Confirm to the user that:
*   The Skill framework is created.
*   The Slash Command `/[skill_name]` is ready.
*   The `README.md` has been updated.
