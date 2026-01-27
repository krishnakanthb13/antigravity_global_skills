---
name: generate_release_image
description: create or edit promotional images for releases, adding version numbers, feature highlights, and modern styling.
---

# Generate Release Image

This skill helps create visually stunning assets to announce a new software release.

## Inputs
*   **Version Number**: e.g. v1.0.0.
*   **Key Features**: List of highlights.
*   **Source Image**: (Optional) Path to existing image.

## Tooling Strategy
*   Use `generate_image` to create or edit the asset.

## Workflow

### 1. Gather Inputs
*   **Version Number**: e.g., v2.0.1
*   **Key Features**: 2-3 main highlights to feature on the image.
*   **Source Image** (Optional): Does the user have a screenshot or existing asset to modify?

### 2. Prompt Strategy (generate_image)

**Option A: User provides an image (Edit Mode)**
*   **Action**: Use the `generate_image` tool, passing the user's file path in `ImagePaths`.
*   **Prompt Construction**:
    *   "Edit this image to add a premium, modern overlay."
    *   "Add the text '[Version Number]' prominently."
    *   "Add a sleek list or callout bubbles highlighting: [Feature 1], [Feature 2]."
    *   "Style: Glassmorphism, dynamic lighting, professional tech aesthetic."
    *   "Ensure text is legible and integrated into the design."

**Option B: No image provided (Creation Mode)**
*   **Action**: Use the `generate_image` tool to create a new asset.
*   **Prompt Construction**:
    *   "A modern, high-tech promotional image for a software release version [Version Number]."
    *   "Visual style: [Choose based on context, e.g., Dark mode, Neon, Minimalist, Corporate]."
    *   "Include visual representations or text overlays for these features: [Feature List]."
    *   "Composition: Hero header style, plenty of negative space for text."

### 3. Execution
*   **Ensure Directory**: Check if an `assets/` folder exists in the project root. If not, create it.
*   **Save**: Call `generate_image` with the constructed prompt.
*   **Filename**: Save the image specifically to `assets/release_[version].png`.

### 4. Review
*   Show the generated image to the user.
*   If text is malformed (common in AI image gen), offer to regenerate or suggest using a dedicated design tool for the final text overlay.
