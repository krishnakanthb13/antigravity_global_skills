---
name: release_helper
description: Automates release note generation and social media announcements. Handles version incrementing (minor vs major).
---

# Release Helper

This skill helps you package up a release by generating release notes and social media content.

## Inputs
*   **Version Number**: (Optional) The target version (e.g. v2.1.0).
*   **Release Type**: Major/Minor/Patch (if no version provided).

## Tooling Strategy
*   Use `read_file` to read `RELEASE_NOTES.md` and `SOCIAL_MEDIA.md`.
*   Use `run_command` (e.g., `git describe --tags --abbrev=0` and `git log <last_release>..HEAD`) to fetch the latest git version, the last git release, and everything that changed from the last release till the latest git commit. Use this as the context to create content.
*   Use `replace_file_content` to prepend new entries to the VERY TOP, ensuring all previous history is completely untouched (DO NOT replace or modify old entries).

## Workflow

### 1. Determine Version Number
*   **Check inputs**: Did the user provide a version number?
*   **Auto-increment**: If not, find the last version number in `RELEASE_NOTES.md`.
    *   **Tiny/Minor**: Increment the right-most number (e.g., `v1.0.1` -> `v1.0.2`) for standard updates.
    *   **Major**: If the user specifies "major", increment the number to the left (e.g., `v1.0.1` -> `v1.1.0`).

### 2. Update `RELEASE_NOTES.md`
Create this file if it doesn't exist. If it exists, ALWAYS prepend new entries to the top to maintain a complete historical log. The old release information MUST remain untouched.

*   **Analyze Changes**: Fetch the latest git version and last git release, and get everything that changed from the last release till the latest git commit to understand what changed and create the content based on that context.
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
Generate engaging posts for the new release. Create this file if it doesn't exist. If it exists, ALWAYS prepend new posts to the top to maintain a record of past announcements. The old social media posts MUST remain untouched.

*   **Platform 1: LinkedIn**
    *   Professional but exciting tone.
    *   Focus on the "value add" / problem solved.
    *   Use hashtags (#OpenSource #Dev #Update).
    *   **Formatting**: Plain text only (No Markdown).
    *   **Length**: Target ~1,500 characters (Max 3,000 allowed).
    *   Write multiple lines, each line separated by a newline character.
*   **Platform 2: Reddit**
    *   Suggest best and extensive list of sub-reddits to post on - (Eg: r/programming, r/webdev style).
    *   Suggest the title of the post.
    *   **Formatting**: Markdown supported (Bold, Italic, Code blocks, Links).
    *   **Length**: Target ~2,500 characters (Max 40,000 allowed).
    *   Conversational, "Show don't tell".
    *   Focus on the tech stack or the interesting technical challenge solved.
*   **Platform 3: X (Twitter)**
    *   Short, crisp, punchy.
    *   Use emojis and threads if the update is large.
    *   Include a call to action (Check it out here!).
    *   **Formatting**: Plain text only (No Markdown).
    *   **Limit**: 280 characters (Free Plan).

## Output
*   Confirm the new version number used.
*   Show the path to the updated `RELEASE_NOTES.md` and `SOCIAL_MEDIA.md`.

## Critical Rules
*   **NEVER OVERWRITE**: Always prepend new release information to the top of existing files. Previous release history must be preserved.
*   **IDEMPOTENCY**: If the version already exists in the file, ask the user if they want to update it or skip.
