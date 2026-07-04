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
*   **Format**: Create/Update `API_DOCUMENTATION.md` (or generate an OpenAPI/Swagger spec).
*   **Structure**:
    *   **Endpoint Details**: `METHOD /path`, description, rate limiting limits, and Auth requirements.
    *   **Request Specification**: Path/Query params, headers, and precise body schemas (with types & validation rules).
    *   **Response Specification**: 
        *   200 Success: Include a full JSON example.
        *   Error Responses: Document ALL possible error codes (e.g., 400 Bad Request, 401 Unauthorized, 409 Conflict), their message formats, and troubleshooting tips.
    *   **Code Examples**: Include a `cURL` command example and a JavaScript/Python snippet if applicable.
    *   **Usage Guidelines**: Provide a getting started guide, pagination patterns, and filtering/sorting options.

### 3. Output
*   Make the documentation clear and consistent.
*   Ensure every identified route is listed.
