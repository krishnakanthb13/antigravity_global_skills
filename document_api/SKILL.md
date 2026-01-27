---
name: document_api
description: Generates standardized API documentation (OpenAPI/Markdown) for backend endpoints.
---

# Document API

Use this skill to automatically map out and document your server's API surface area.

## Inputs
*   **Source Code**: The directory or entry point (e.g., `server.js`).
*   **Format**: Preferred output (Markdown vs Swagger/OpenAPI).

## Tooling Strategy
*   Use `grep_search` to find route definitions (e.g., `.get(`, `@app.route`).
*   Use `view_file` to understand request/response schemas.

## Workflow

### 1. Analysis
*   **Scan**: Identify the server entry point (e.g., `server.js`, `app.py`).
*   **Route Discovery**: Trace route definitions (Express `.get()`, Flask `@app.route`, FastAPI decorators).
*   **Parameters**: specific inputs (Body, Query Params, Path Variables).

### 2. Documentation Generation
*   **Format**: Create/Update `API_DOCUMENTATION.md` (or generate a Swagger JSON if preferred).
*   **Structure**:
    *   **Endpoint**: `METHOD /path`
    *   **Description**: What it does.
    *   **Request**:
        *   Headers (Auth?)
        *   Body Schema (JSON structure)
    *   **Response**:
        *   200 Success: Example JSON
        *   4xx/5xx Errors: Error codes

### 3. Output
*   Make the documentation clear and consistent.
*   Ensure every identified route is listed.
