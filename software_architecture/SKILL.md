---
name: software_architecture
description: Guide for quality-focused software architecture. Use this when designing architecture, writing code, or analyzing software systems.
---

# Software Architecture

This skill provides guidance for quality-focused software development and architecture. It focuses on Clean Architecture and Domain-Driven Design principles.

## Core Rules & Principles

1. **Early Return Pattern**: Always use early returns when possible over nested conditions.
2. **Decompose Components**: Break down components longer than 80 lines and split files larger than 200 lines.
3. **Library-First Approach**:
   - ALWAYS search for existing solutions before writing custom code.
   - Use libraries for common problems (retry logic, state management, validation).
4. **Clean Architecture & DDD**:
   - Separate domain entities from infrastructure. Keep business logic independent of frameworks.
5. **Naming & Bounded Contexts**:
   - AVOID generic names (`utils`, `helpers`, `common`, `shared`).
   - USE domain-specific names (`OrderCalculator`, `InvoiceGenerator`).
6. **Separation of Concerns**:
    - Do NOT mix business logic with UI components.
    - Keep database queries out of controllers.
7. **SOLID Principles**:
   - **S**ingle Responsibility: A class should have one reason to change. Decompose large monoliths.
   - **O**pen/Closed: Design for extension without modifying existing source code (e.g., plugins, inheritance).
   - **L**iskov Substitution: Subclasses must be interchangeable with their base classes.
   - **I**nterface Segregation: Prefer many specific interfaces over one general-purpose interface.
   - **D**ependency Inversion: Depend on abstractions (interfaces/abstract classes), not concrete implementations.

## Anti-Patterns to Avoid

- **NIH (Not Invented Here) Syndrome**: Don't build custom auth when Auth0 exists.
- **Dumping Grounds**: Don't create `utils.js` or `shared.js` with lots of unrelated functions. Every module should have a single, clear purpose.
