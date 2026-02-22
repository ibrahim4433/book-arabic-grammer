# 📖 User Guide: From Pictures to Book

This guide explains how to use the **Modern Arabic Grammar Book** system to convert raw images of book pages into a fully formatted, professional HTML5/PDF book.

---

## **Phase 1: Input & Digitization**

### 1. Prepare Your Images
*   **Action:** Place your book page images (scanned or photographed) into the `input/` folder.
*   **Format:** `.jpg` or `.png`.
*   **Naming:** Use sequential numbers (e.g., `1.jpg`, `2.jpg`, `10.jpg`).
*   **Why:** The system processes files in alphanumeric order.

### 2. Convert Images to Text (OCR)
*   **Command:** `python3 system.py` -> Select **Option B**.
*   **What happens:**
    *   The system sends each image to Gemini (AI Vision).
    *   It extracts all Arabic text with full Tashkeel (diacritics).
    *   It saves the text to `system-workspace/text-data/raw/raw_X.txt`.
*   **Output:** Check `system-workspace/text-data/raw/` to see the text files.

### 3. Create the Lesson Index
*   **Prerequisite:** Ensure you have a `TOC.txt` (Table of Contents) file in `system-workspace/text-data/`. This file should list the lesson titles exactly as they appear in the book.
*   **Command:** `python3 system.py` -> Select **Option C**.
*   **What happens:**
    *   The system reads all raw text files.
    *   It asks Gemini to match the `TOC.txt` titles to the raw text content.
    *   It generates `assets/data/raw_to_lesson_index.json`.
*   **Output:** Open `assets/data/raw_to_lesson_index.json` to verify the mapping (e.g., "The Verb" starts at `raw_1.txt:Line 5`).

---

## **Phase 2: Planning & Architecture**

### 4. Generate Lesson Plans (The Architect)
*   **Command:** `python3 system.py` -> Select **Option D** (Standard) or **Option E** (Jules Batch).
*   **What happens:**
    *   The "Architect" (AI) reads the raw text for the lesson.
    *   It designs a layout using the project's atomic components (Blocks, Tables, Examples).
    *   It creates a **Markdown Plan** in `plans/`.
    *   The "Auditor" (AI) checks the plan against design rules.
*   **Output:** Check `plans/` for the generated `.md` files.

---

## **Phase 3: Production (Coding)**

### 5. Compile Plans to HTML (The Builder)
*   **Command:** `python3 system.py` -> Select **Option F** (Page Generation).
*   **What happens:**
    *   The system reads the Markdown Plan.
    *   It loads the HTML Templates from `Jules-workspace/Templates/`.
    *   It fills in the content and assembles the final HTML page.
    *   It saves the file to `pages/XX.X_nXX_lesson_name.html`.
*   **Output:** Check `pages/` for the new HTML files.

### 6. Verify Layout (The Quality Gate)
*   **Command:** `python3 "Jules-workspace/verify_layout.py" pages/YOUR_FILE.html`
*   **What happens:**
    *   The system renders the page to a temporary PDF.
    *   It checks if the content fits on **One A4 Page**.
    *   **PASS:** Page Count = 1.
    *   **FAIL:** Page Count > 1 (Overflow).
*   **Action:** If it fails, split the content into two pages or condense the text.

---

## **Phase 4: Final Assembly**

### 7. Assign Unique IDs
*   **Command:** `python3 "Jules-workspace/id_manager.py" auto-tag`
*   **What happens:**
    *   Scans all HTML files.
    *   Assigns a unique `bXXXXX` ID to every content block.
*   **Why:** Required for cross-referencing and digital indexing.

### 8. Build the Book (PDF)
*   **Command:** `python3 build.py`
*   **What happens:**
    *   Merges all HTML pages.
    *   Injects global styles, watermarks, and covers.
    *   Generates the final PDF.
*   **Output:** `output/export/book.pdf`.

---

## **Summary of Commands**

| Step | Task | Command |
| :--- | :--- | :--- |
| 1 | **OCR** | `python3 system.py` (Option B) |
| 2 | **Index** | `python3 system.py` (Option C) |
| 3 | **Plan** | `python3 system.py` (Option D or E) |
| 4 | **Compile** | `python3 system.py` (Option F) |
| 5 | **Verify** | `python3 "Jules-workspace/verify_layout.py" pages/X.html` |
| 6 | **Tag IDs** | `python3 "Jules-workspace/id_manager.py" auto-tag` |
| 7 | **Build** | `python3 build.py` |

---

## **Troubleshooting**

*   **"Lesson not found"**: Check `assets/data/raw_to_lesson_index.json`. The name must match exactly.
*   **"Overflow" (Page > 1)**: The content is too long for one A4 page. Split the lesson into two parts (e.g., "The Verb Part 1", "The Verb Part 2") in your `TOC.txt` and regenerate the index.
*   **"Missing Template"**: Ensure `Jules-workspace/Templates/` contains the template requested by the plan.
