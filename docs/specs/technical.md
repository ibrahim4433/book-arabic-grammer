# 🏗️ Technical Specifications

This document defines the engineering standards, technology stack, and code quality rules.

## 💻 Tech Stack

*   **Language:** Python 3.10+
*   **Markup:** HTML5 (Semantic)
*   **Styling:** CSS3 Paged Media Level 3 (Print-focused)
*   **Rendering Engine:** WeasyPrint (Python library)
    *   *Constraint:* Must use GTK3/Pango for font rendering.
*   **AI Backend:** Google Gemini (via `google-generativeai` SDK or REST API).
*   **Version Control:** Git.

## 🛡️ Security Standards

1.  **Secret Management:**
    *   API Keys (Gemini, Jules) MUST be stored in `secrets/` or Environment Variables.
    *   `secrets/` MUST be in `.gitignore`.
    *   NEVER hardcode keys in Python scripts.
2.  **Input Sanitization:**
    *   Although this is an internal tool, file paths from user input must be validated to prevent directory traversal.

## 🧼 Code Quality Guidelines

1.  **Python (PEP 8):**
    *   Use `snake_case` for functions/variables.
    *   Use `PascalCase` for classes.
    *   Type hinting is encouraged (e.g., `def build(page: str) -> bool:`).
2.  **HTML Structure:**
    *   **Strict RTL:** `<html dir="rtl" lang="ar">` is mandatory.
    *   **Semantic Tags:** Use `<article>`, `<section>`, `<header>` instead of nested `<div>` soup where possible.
    *   **No Inline Styles:** All styling must be in `styles/main.css` or utility classes.
3.  **CSS Architecture:**
    *   **Variables:** Use CSS Variables (`--color-primary`, `--spacing-unit`) for theming.
    *   **Print Units:** Use `mm`, `cm`, `pt`, `pc`. NEVER use `px` for layout dimensions.
4.  **File Naming:**
    *   Pages: `XX.X_nXX_name.html` (e.g., `01.0_n05_verb.html`).
    *   Templates: `TEMPLATE_C_NAME.html`.
    *   Scripts: `descriptive_name.py`.

## 📦 Directory Structure

```text
root/
├── .specs/             # Project Requirements (Source of Truth)
├── assets/             # Static Assets (Templates, Images, Fonts)
├── docs/               # Documentation & AI Personas
├── input/              # Raw Images
├── output/             # Generated Artifacts (Text, PDF)
├── pages/              # HTML Source Files (The Book)
├── plans/              # AI Generated Lesson Plans
├── secrets/            # API Keys (Ignored)
├── styles/             # Global CSS
├── tools/              # Automation Scripts
│   ├── automation/     # Core Workflow (OCR, Planner, Builder)
│   └── extra/          # Utilities (ID Manager, Verifier)
└── build.py            # Master Build Script
```
