---
name: code_review
description: Comprehensive code review covering Functionality, Security (OWASP), Performance, and Maintainability. Includes good/bad examples.
---

# Code Review Checklist

Use this skill to conduct a thorough, senior-level code review.

## Inputs
*   **Target**: The file or directory to review.
*   **Focus**: (Optional) Specific area to check (e.g., security, performance).

## Tooling Strategy
*   Use `view_file` to read the code.
*   Use `grep_search` if looking for specific patterns across multiple files.

## Workflow

### 1. Functionality & Logic (The "Does it Work?" Check)
*   **Requirements**: Does this solving the stated problem?
*   **Edge Cases**: Nulls, empty states, limits (min/max).
*   **Error Handling**: Are errors caught, logged, and handled gracefully (no silent failures)?

### 2. Security (The OWASP Check)
*   **Injection**: Check for raw SQL, `innerHTML`, or `eval()`.
    *   *❌ Bad*: `db.query("SELECT * FROM users WHERE name = " + input)`
    *   *✅ Good*: `db.query("SELECT * FROM users WHERE name = $1", [input])`
*   **Secrets**: Ensure NO API keys or passwords are committed. (Use `.env`).
*   **Auth**: Are permission checks present on sensitive routes?

### 3. Performance (The Scalability Check)
*   **Loops**: No expensive operations inside loops (e.g., DB calls).
*   **N+1 Problems**: Check for fetching data in a loop instead of batches.
*   **Memory**: Are listeners/connections cleaned up?

4. **Code Quality (The Maintainability Check)**
*   **Naming**: Variables should be intentional (`isValid` vs `v`).
*   **DRY (Don't Repeat Yourself)**: Can distinct logic be extracted to a helper?
*   **SOLID Principles**:
    *   **S**: Does the class/function do only ONE thing?
    *   **O**: Can we add features without changing this code?
    *   **L**: Can subclasses be used interchangeably?
    *   **I**: Are interfaces too bloated?
    *   **D**: Is it hard-coded to a specific implementation? (Use dependency injection).
*   **Comments**: Explain *WHY*, not *WHAT*.

### 5. Git & Hygiene
*   **Commits**: Are they atomic and descriptive?
*   **Leftovers**: No `console.log` (debug only), commented-out code, or TODOs without an issue tracking them.

## Output Format
Structure your review like this:

**Summary**: [High level opinion - Ready to Merge / Changes Requested]

| Category | Status | Notes |
| :--- | :--- | :--- |
| **Functionality** | ✅ / ⚠️ | ... |
| **Security** | ✅ / 🔴 | ... |
| **Performance** | ✅ / ⚠️ | ... |

**Detailed Comments**:
*   [File/Line]: [Issue description]
    *   *Suggestion*: [Code snippet check]

## Comprehensive Review Guidelines

### 1. The Review Mindset
- **Goals**: Catch bugs, ensure maintainability, share knowledge, improve architecture.
- **Not Goals**: Nitpicking formatting, showing off, rewriting to personal preference.
- **Provide Effective Feedback**: Be specific, actionable, educational, and focused on the code, not the person. Suggest, don't command.

### 2. Differentiate Severity (The Label System)
Use explicit labels to set expectations:
- 🔴 `[blocking]`: Must fix before merge (e.g., security flaws, breaking bugs).
- 🟡 `[important]`: Should fix, discuss if disagree (e.g., architectural issues, N+1 queries).
- 🟢 `[nit]`: Nice to have, not blocking (e.g., minor naming improvements).
- 💡 `[suggestion]`: Alternative approach to consider.
- 📚 `[learning]`: Educational comment, no action needed.
- 🎉 `[praise]`: Acknowledge good work and solid patterns!

### 3. Review Techniques
- **The Question Approach**: Ask questions to encourage thinking (e.g., "What happens if `items` is empty?" instead of "This fails if empty").
- **Collaborative Language**: Use suggestions (e.g., "Would it make sense to extract this?" instead of "Extract this").
- **Avoid Implementation Detail Reviews**: Ensure tests describe behavior, not internal state (e.g., test what happens on click, not that an internal counter incremented).

### 4. Handling Disagreements
If there's disagreement: Seek to understand the author's approach, acknowledge valid points, request data (like a benchmark) if needed, and know when to let go if it's working and not critical.
