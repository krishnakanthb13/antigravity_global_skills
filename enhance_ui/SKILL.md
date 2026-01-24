---
name: enhance_ui
description: Systematic UI enhancement and verification. Covers styling upgrades, responsiveness, and rigorous integrity testing to prevent code regression/loss.
---

# Enhance UI & Verification

Use this skill when the user wants to improve the appearance/interaction of a UI or ensure that recent edits haven't broken the interface.

## Workflow

### 1. Visual Polish & UX
For the target UI component/page:
*   **Interaction**: Add distinct hover/active states for all interactive elements.
*   **Typography**: Ensure hierarchy (headings vs body) and legibility.
*   **Spacing**: Check padding/margins to prevent "crowded" layouts.
*   **Responsiveness**: Verify layout behavior on mobile vs desktop.

### 2. Integrity Checks (The "Anti-Regression" Filter)
Before finalizing any UI code change:
*   **Code Block Check**: Explicitly verify that no existing logic or code blocks were accidentally removed.
*   **Completeness**: ensure large files weren't truncated.
*   **Event Listeners**: Ensure button clicks/inputs still trigger their attached JS functions.

### 3. Testing Suite
*   **Smoke Test**: Does the code compile/render without immediate errors?
*   **UI Test**: Do key elements (buttons, forms, modals) appear as expected?
*   **Responsive Check**: Does it break when the viewport shrinks?

### 4. Output
*   Apply the enhancements.
*   Report: "Applied [Styles]. Verified [Integrity Checks]. Confirmed no code loss."
