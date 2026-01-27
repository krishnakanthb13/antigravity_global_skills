---
name: create_launcher
description: Generates robust, cross-platform launcher scripts (Windows .bat, Unix .sh, Mac .sh) with dependency checking, .env handling, and graceful shutdown logic.
---

# Create Launcher (Web & Scripts)

Use this skill to generate professional-grade entry point scripts for applications.

## Inputs
*   **App Name**: Name of the application (for display).
*   **Entry Point**: Main script to run (e.g., `main.py`, `index.js`).

## Tooling Strategy
*   Use `write_to_file` to create the scripts.
*   Use `run_command` with `pwsh` (Windows) or `bash` (Unix) to verify dependency checks if needed.

## Workflow

### 1. Requirements Gathering
*   **Target OS**: Windows, macOS, Linux (default to creating for ALL).
*   **Environment**: Does it need `.env` variables?
*   **Dependencies**: What needs to run? (npm, python, node, docker).

### 2. Script Generation Rules

#### Common Features
*   **Single Click Launch**: Scripts must run without user argument input (or have defaults).
*   **Pre-flight Checks**:
    *   Check if required tools (node, python) are in PATH.
    *   Check if `node_modules` or `venv` exists.
    *   Check for `.env` file presence.

#### Windows (`.bat` / `.cmd`)
*   Use `@echo off`.
*   Title the window.
*   Handle `Ctrl+C` gracefully if possible.

#### Unix (`.sh` for Mac/Linux)
*   Shebang: `#!/bin/bash`.
*   Permission: Remind user to `chmod +x`.
*   **Trap Signals**: Implement `trap 'kill 0' SIGINT` or similar to clean up subprocesses on exit.

### 3. Graceful Shutdown (The "No Orphan" Rule)
*   Ensure that killing the launcher kills the spawned processes.
*   For python scripts, consider wrapping in try-finally blocks.

### 4. Output
*   Generate the scripts in the project root.
*   Provide a quick Markdown snippet on how to run them.
