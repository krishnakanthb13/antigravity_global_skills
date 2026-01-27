---
name: security_audit
description: Scans the codebase for OWASP Top 10 vulnerabilities (Secrets, Injection, Auth) and manages SECURITY.md.
---

# Security Audit (OWASP Standards)

Use this skill to perform a "Paranoid Mode" security sweep.

## Inputs
*   **Scope**: The directory to audit.
*   **Depth**: Full scan or quick check.

## Tooling Strategy
*   Use `grep_search` to find secrets ("API_KEY", "password") and vulnerable patterns (`innerHTML`, `eval`).
*   Use `view_file` to check auth logic.

## Workflow

### 1. Secrets Detection (Credentials)
*   **Scan**: Look for API keys, passwords, tokens, or private keys.
*   **Fix**: Move to `.env`. Add `.env` to `.gitignore`.

### 2. Injection Prevention (OWASP #1)
*   **SQL Injection**: Are queries parameterized? (`$1` vs string concat).
*   **XSS (Cross-Site Scripting)**:
    *   JS: Check `innerHTML` or `dangerouslySetInnerHTML`.
    *   User Input: Is it sanitized/escaped before rendering?

### 3. Authentication & Authorization (Broken Access Control)
*   **Endpoints**: Do sensitive routes (e.g., `/admin`, `/delete`) have middleware checks?
*   **IDOR**: can User A access User B's data by changing an ID in the URL?

### 4. Dependency Analysis (Supply Chain)
*   **Verify**: Check `package.json` or `requirements.txt` for known vulnerable versions.
*   **Unused**: Remove unused packages to reduce attack surface.

### 5. Report Generation (`SECURITY.md`)
Create/Update the report in the root:
*   **Audit Log**: Date of scan.
*   **Findings**:
    *   🔴 **Critical**: Secrets, Injection holes.
    *   🟡 **Warning**: Outdated deps, missing CSRF tokens.
    *   🟢 **Passed**: "Auth implemented on /admin".

### 6. Verification
*   Confirm the fix is applied (e.g., secret is gone from code).
*   Confirm `SECURITY.md` is updated.
