# ⚖️ Compliance & Constraints

This document defines the strict "Laws" of the project that cannot be violated.

## 📜 The "One-Page Law"
*   **Rule:** Every single HTML file in `pages/` MUST render to **exactly one** A4 page in the final PDF.
*   **Rationale:** Pedagogical focus. Forces concise explanation. Eliminates awkward page breaks mid-sentence.
*   **Verification:** `tools/automation/verify_headless.py` checks this automatically.
*   **Failure Consequence:** The build is flagged as "Unstable".

## 🔡 The "Tashkeel Mandate"
*   **Rule:** All Arabic text used in examples, rules, and definitions MUST have full diacritics (Fatha, Kasra, Damma, Sukun, Shadda).
*   **Exception:** Instructional meta-text (like "See page 5") may be plain, but lesson content must be vocalized.
*   **Rationale:** This is a grammar book. Ambiguity is the enemy.

## 🆔 The "Unique ID Protocol"
*   **Rule:** Every significant content block (Header, Rule, Example, Exam) MUST have a unique ID attribute.
*   **Format:** `id="bXXXXX"` (e.g., `id="b82910"`).
*   **Rationale:** Allows for deep-linking, digital indexing, and precise referencing in future digital apps.
*   **Automation:** `tools/id_manager.py` handles this.

## 🎨 Design System Compliance
*   **Rule:** Do NOT invent new HTML structures. You MUST use the provided Atomic Components in `assets/Templates/`.
*   **Approved Components:**
    *   `TEMPLATE_C_HEADER.html`
    *   `TEMPLATE_C_BLOCK.html` (Definitions)
    *   `TEMPLATE_C_TABLE.html` (Conjugations)
    *   `TEMPLATE_C_SPLIT.html` (Comparisons)
    *   `TEMPLATE_C_POEM.html` (Shawahid)
    *   `TEMPLATE_C_IRAB.html` (Parsing)
*   **Color Coding:**
    *   **Red (`.highlight-red`):** Grammatical Signs / Key Focus.
    *   **Blue (`.highlight-blue`):** Particles / Secondary Focus.
    *   **Teal:** Headers / Structural elements.

## 🔢 Numeric Standard
*   **Rule:** All visible numbers (Page numbers, Lesson numbers, List counters) MUST use **Arabic-Indic Digits** (١, ٢, ٣...).
*   **Implementation:** Handled via CSS `content` replacement or direct text input.
