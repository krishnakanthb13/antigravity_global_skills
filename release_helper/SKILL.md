---
name: release_helper
description: Automates release note generation and social media announcements. Handles version incrementing (minor vs major).
---

# Release Helper

This skill helps you package up a release by generating release notes and social media content.

## Workflow

### 1. Determine Version Number
*   **Check inputs**: Did the user provide a version number?
*   **Auto-increment**: If not, find the last version number in `RELEASE_NOTES.md`.
    *   **Tiny/Minor**: Increment the right-most number (e.g., `v1.0.1` -> `v1.0.2`) for standard updates.
    *   **Major**: If the user specifies "major", increment the number to the left (e.g., `v1.0.1` -> `v1.1.0`).

### 2. Update `RELEASE_NOTES.md`
Create this file if it doesn't exist, or append new posts to the top.

*   **Analyze Changes**: Look at git history or recent file modifications to understand what changed.
*   **Format**:
    *   Header: `## [Version] - [Date]`
    *   Style: Use emojis 🚀, one-liners for quick reading, followed by detailed descriptions if necessary.
    *   Categories:
        *   `### 🚀 New Features`
        *   `### ⚡ Improvements`
        *   `### 🐛 Bug Fixes`
        *   `### 📚 Documentation`
        *   `### 🏗️ Infrastructure & Maintenance`

### 3. Create `SOCIAL_MEDIA.md`
Generate engaging posts for the new release. Create this file if it doesn't exist, or append new posts to the top.

*   **Platform 1: LinkedIn**
    *   Professional but exciting tone.
    *   Focus on the "value add" / problem solved.
    *   Use hashtags (#OpenSource #Dev #Update).
*   **Platform 2: Reddit**
    *   Suggest best sub-reddit to post on - (Eg: r/programming, r/webdev style)
    *   Conversational, "Show don't tell".
    *   Focus on the tech stack or the interesting technical challenge solved.
*   **Platform 3: X (Twitter)**
    *   Short, crisp, punchy.
    *   Use emojis and threads if the update is large.
    *   Include a call to action (Check it out here!).

## Output
*   Confirm the new version number used.
*   Show the path to the updated `RELEASE_NOTES.md` and `SOCIAL_MEDIA.md`.
