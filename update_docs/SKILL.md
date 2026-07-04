---
name: update_docs
description: Updates standard project documentation files (README, CODE_DOCUMENTATION, DESIGN_PHILOSOPHY) to reflect the current state of the codebase.
---

# Update Documentation

This skill systematically updates the core documentation files of the project.

## Inputs
*   **Changes**: Summary of what changed (or ask Agent to scan).
*   **Docs to Update**: README, CODE_DOCUMENTATION, etc.

## Tooling Strategy
*   Use `view_file` to read current docs.
*   Use `replace_file_content` to update sections.

## Workflow

1.  **Analyze Changes**: Briefly scan the recent changes in the codebase to understand what functionality has been added, modified, or removed.

2.  **Update README.md**:
    *   **Focus**: "HOW TO'S".
    *   Ensure installation and usage instructions are up to date.
    *   Add any new features to the feature list.
    *   Verify prerequisites and configuration steps.

3.  **Update CODE_DOCUMENTATION.md**:
    *   **Focus**: "Code functionality - crisp, clear, and simple".
    *   Describe the technical implementation of new features.
    *   Update architecture diagrams or descriptions if flow has changed.
    *   Keep it concise; avoid over-explaining standard boilerplate.

4.  **Update DESIGN_PHILOSOPHY.md**:
    *   **Focus**: "Why and what are we trying to do - ideology".
    *   Explain the *reasoning* behind recent major changes.
    *   Re-align the document with the project's evolving goals if necessary.
    *   Ensure the tone reflects the project's core values.

5.  **Review**: Check for consistency across all three documents.

## Standard Documentation Templates
When creating or heavily updating files, adhere to these structural templates:

### README Structure
Prioritize sections in this order:
1. **Title + One-liner**: What is this?
2. **Quick Start**: How to run in <5 min.
3. **Features**: What can I do?
4. **Configuration**: Environment variables and defaults.
5. **API Reference/Documentation**: Link to details.
6. **Contributing & License**.

### Code Comment Guidelines (JSDoc/TSDoc)
Comment the *Why* (business logic), not the *What* (obvious). Document API contracts and complex algorithms.
```typescript
/**
 * Brief description of what the function does.
 * 
 * @param paramName - Description of parameter
 * @returns Description of return value
 * @throws ErrorType - When this error occurs
 */
```

### Changelog Format (Keep a Changelog)
```markdown
## [Unreleased]
### Added
### Changed
### Fixed
```
