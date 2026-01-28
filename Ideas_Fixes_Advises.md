# Project Review: Ideas, Fixes, & Advises

This document outlines the findings from the review of the "Arabic Grammar Book" project, specifically focusing on the discrepancies found in pages 8 and 9, and provides actionable advice to perfect the workflow and output.

## 1. Analysis of Discrepancies (Pages 8-9)

The investigation revealed that Pages 8 and 9 deviated from the project's "Atomic Design" philosophy, which caused them to look inconsistent compared to Pages 3-7.

### Key Issues Identified:
*   **Generic HTML vs. Atomic Components:** The pages used generic HTML tags with utility classes (e.g., `<ul class="list-disc mr-5mm">`) instead of the mandatory Atomic Components (e.g., `TEMPLATE_C_LIST` / `<ul class="structured-list">`).
*   **Manual Inline Styling:** There was excessive use of manual inline styles (e.g., `style="background-color: #E3F2FD..."`) for benefit boxes, creating "off-theme" colors (Blue) that are not part of the standard semantic palette (Teal, Orange, Yellow).
*   **Nested List Inconsistency:** The use of `list-reset-pr` and `list-none` for nested lists created a visual break from the established rhythm of the book.

## 2. Recommendations for the "Architect GEM"

To prevent the Architect from generating non-compliant plans, the `GEM_PROMPT.md` should be updated with stricter negative constraints.

### Proposed Rules to Add:
1.  **FORBID Generic Lists:** Explicitly forbid the use of `<ul>` or `<ol>` tags unless they are strictly wrapped in `<ul class="structured-list">` with `TEMPLATE_C_LIST_ITEM` markers.
    *   *Prompt Instruction:* "NEVER use `<ul class="list-disc">`. ALWAYS use `TEMPLATE_C_LIST`."
2.  **Standardize Colors:** Prohibit arbitrary hex codes for benefit boxes. Force the selection of one of the three semantic types:
    *   **Standard:** Teal (`TEMPLATE_C_BENEFIT`)
    *   **Warning:** Orange (`TEMPLATE_C_BENEFIT_WARNING`)
    *   **Tip:** Yellow (`TEMPLATE_C_BENEFIT_TIP`)
    *   *If a new color is needed (e.g., Blue for Parsing Notes), it should be added as a formal template or CSS class, not hacked inline.*
3.  **Nested Content Pattern:** Define a standard pattern for nested content (e.g., "Use a `<div>` with `.mt-1mm` inside the list item, do not start a new `<ul>`").

## 3. Workflow Improvements

### Automated Linting (Pre-Commit)
Implement a simple "Grep Linter" in the workflow to catch deviations before they reach the verification stage.
*   **Check:** `grep "list-disc" pages/*.html` -> Should return empty.
*   **Check:** `grep "style=" pages/*.html` -> Should be minimized (or allowed only for specific components like Exam/Poem).

### "One-Page Law" Nuance
The current verification tool checks for page count but not for "Visual Density".
*   **Idea:** Update `verify_layout.py` to also warn if strictly non-semantic tags are found (e.g., `style="margin-top: -5mm"` which implies hacking the layout).

## 4. Technical Advises for "Jules"

*   **Atomic Discipline:** When implementing a plan, if the Architect requests a generic list, "Jules" should auto-correct it to a `structured-list` rather than blindly following the generic HTML instruction.
*   **Refactoring:** Periodically scan `styles/main.css` to ensure utility classes (like `.list-disc`) are actually needed. If they tempt misuse, remove them.

## 5. Summary of Fixes Applied
*   **Pages 3, 4, 5 Refactored:**
    *   Replaced generic lists (`list-disc`, `list-reset-pr`) with `structured-list` using `•` markers.
    *   Standardized list styling to mimic the cleaner "simple list" aesthetic (removed dashed borders from `structured-list` via CSS).
*   **Pages 8 & 9 Standardized:**
    *   Replaced complex markers (e.g., `✅` where repetitive) with simple bullets (`•`) to unify the book's visual theme across all pages.
    *   Replaced custom Blue benefit boxes with standard Teal/Yellow patterns.
    *   Standardized nested content using `<div>` wrappers instead of raw lists.
*   **Documentation Updated:**
    *   `ARCHITECTURE.md`: Updated file structure.
    *   `BOOK_RULES.md`: Added missing atomic components (Chips, Irab Row, TOC).
    *   `styles/main.css`: Modified `.structured-list` to act as the single source of truth for all lists, supporting both complex (numbered) and simple (bulleted) styles.
