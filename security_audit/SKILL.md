---
name: security_audit
description: Scans the codebase for security vulnerabilities (secrets, injection, dependencies) and creates a SECURITY.md report.
---

# Security Audit

Use this skill to perform a paranoid check on your codebase for security risks.

## Workflow

### 1. Scan (The "Paranoid Eye")
*   **Secrets**: Look for hardcoded API keys, passwords, tokens, or private keys.
*   **Injection**: Check for `innerHTML`, raw SQL queries without parameterization, or `eval()` usage.
*   **Data Handling**: Check how user input is sanitized before use.
*   **Dependencies**: Check for obviously outdated or insecure patterns in `package.json` or `requirements.txt`.

### 2. Report Generation (`SECURITY.md`)
*   Create or update `SECURITY.md` in the project root.
*   **Structure**:
    *   **## Security Policy**: How to report vulnerabilities.
    *   **## Audit Log [Date]**:
        *   **🟢 Passed**: Checks that returned clean.
        *   **🔴 Vulnerabilities**: Critical issues found (with file/line references).
        *   **🟡 Warnings**: Potential risks or best practice violations.

### 3. Remediation
*   For every 🔴 Vulnerability, provide a specific code snippet or instruction on how to fix it immediately.
*   For secrets, suggest moving them to `.env` variables.

### 4. Verification
*   Confirm that `SECURITY.md` is updated and accurate.
