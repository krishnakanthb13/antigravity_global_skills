---
name: daily_log
description: Scans the current conversation thread and updates a project work log. Useful for tracking progress and generating release notes.
---

# Daily Log

Use this skill to capture the work done in a session/thread and append it to a persistent log file.

## Inputs
*   **Scope**: The current session context (messages, tools used).
*   **Work Log Directory**: `work_log` (default).

## Tooling Strategy
*   Use `list_dir` to find the `work_log` folder.
*   Use `write_to_file` to create the new log entry.

## Workflow

### 1. Identify Target
*   **Folder**: Target the `work_log` folder in the project's base directory.
*   **Context**: Scan the current conversation thread to identify:
    *   Features implemented.
    *   Bugs fixed.
    *   Decisions made.

### 2. Format Entry
Create a markdown entry:

```markdown
## [Date] - [Thread/Topic Name]
-   **Summary**: [One line summary]
-   **Details**:
    -   [Detailed bullet point]
    -   [Detailed bullet point]
-   **Link**: [Markdown Link to Thread/Conversation if available]
```

### 3. Save Log Entry
*   **Directory**: Create or utilize a `work_log` folder in the project's current working directory.
*   **Filename**: Add the entry to a unique log file named with the format `yyyymmdd-hhmmss.log` (e.g., `20260125-005255.log`).
*   **Action**: Use `write_to_file` to create the new log file within the `work_log` folder.

### 4. Output
*   **Confirmation**: Give explicit confirmation to the user that the log entry has been created and mention the filename and path.
