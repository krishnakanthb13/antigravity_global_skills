---
name: daily_log
description: Scans the current conversation thread and updates a project work log. Useful for tracking progress and generating release notes.
---

# Daily Log

Use this skill to capture the work done in a session/thread and append it to a persistent log file.

## Workflow

### 1. Identify Target
*   **File**: Default to `C:\Users\ADMIN\OneDrive\Documents\GitHub\z Reference Files\WORK_LOG.md`.
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
--- (Horizontal Line separator)
```

### 3. Prepend (Context Efficient)
*   **Zero-Read Policy**: Do NOT read the entire `WORK_LOG.md` file (this saves significant context window tokens).
*   **Action**: Use a tool like `replace_file_content` (targeting StartLine: 1) or a strategic write to insert the new entry at the very top of the file without loading the previous history into the chat context.
*   **Safety**: Ensure you do not overwrite or erase old entries. Only the new entry is added to the top (Reverse Chronological Order).

### 4. Output
*   Confirm the log has been updated.
