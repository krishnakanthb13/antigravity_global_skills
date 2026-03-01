---
name: repo_infographic
description: Generates a crisp, clear full infographic of the repository with a unique theme based on the repo's content. Saves the infographic to the assets folder and links it in the README.md file.
---

# Repo Infographic

Use this skill to create a comprehensive infographic of the current repository.

## Workflow

1. **Analyze Repository**:
   - Understand the current repository structure, purpose, and key components using directory listings and file analysis.
   - Determine a unique and appropriate visual theme for the infographic based on the repository's main focus.

2. **Generate Infographic**:
   - Use the `generate_image` tool to create a visual infographic.
   - The prompt should request a crisp, clear infographic that visualizes the repository's modules, features, or architecture, heavily leaning into the determined theme.
   - Provide the ImageName as `repo_infographic`.

3. **Save Asset**:
   - Locate the `assets` folder in the repository root (create it if it doesn't exist).
   - Ensure the generated image is saved, downloaded, or moved to this `assets` directory.

4. **Update README.md**:
   - Identify the main `README.md` file of the repository.
   - Append or insert an embedded image link to the generated infographic pointing to the correct relative path in the `assets` folder.
