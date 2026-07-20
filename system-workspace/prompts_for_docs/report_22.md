### `./system-workspace/tools/new-tools/fix_filenames.py`
- **Status:** Usable
- **Purpose:** Cleans up generated HTML filenames in the `pages/` directory by stripping unneeded strings (like "(تابع)"), removing duplicate underscores, and attempting to extract the true Arabic title from the `<h1>` tag inside the file to rename it appropriately. It skips templates and TOC pages.
- **Inputs:** `pages/*.html` (specifically looks for files matching the regex pattern and reads `<h1>` tags).
- **Outputs:** Renames files within the `pages/` directory. Also deletes `pages/00.0_blank_page1.html` if it exists.
- **Usage:** `python3 ./system-workspace/tools/new-tools/fix_filenames.py`
- **Workflow Integration:** Can be used in the old workflow where batch processing and automated title extraction for filenames were needed. In the strict 1-Plan-Per-Page workflow, filenames are usually strictly controlled and explicitly handled during the plan, rendering this tool somewhat less critical but still potentially useful for batch cleanup.

### `./system-workspace/tools/new-tools/make_index.py`
- **Status:** Usable
- **Purpose:** Parses raw lesson text files (`raw1.txt` to `raw13.txt`) against a Table of Contents (`TOC.json`) to map the exact starting and ending line locations (`file:line_num`) for each lesson. It outputs an indexed version of the raw text and a JSON map of lesson boundaries.
- **Inputs:** `C3_Lessons_Text/TOC.json`, `C3_Lessons_Text/raw1.txt` to `raw13.txt`.
- **Outputs:** `C3_Lessons_Text/full_raw_indexed.txt`, `C3_Lessons_Text/raw_to_lesson_index.json`.
- **Usage:** `python3 ./system-workspace/tools/new-tools/make_index.py`
- **Workflow Integration:** Part of the old text preprocessing workflow to track exact text segments. With the 1-Plan-Per-Page workflow operating on predefined HTML slices and precise Markdown chunks, mapping raw txt files to lessons may no longer be required.

### `./system-workspace/tools/new-tools/fix_toc_answers.py`
- **Status:** Usable
- **Purpose:** Updates the Table of Contents (`00.3_TOC.html`) answer section by looking at `backup_answers/98.*.html` files, parsing which lesson numbers appear on which pages, and replacing generic TOC entries (like "مُلْحَقُ الْإِجَابَاتِ - جُزْءٌ") with specific lesson numbers (e.g., "إِجَابَاتُ الدَّرْسِ 6").
- **Inputs:** `backup_answers/98.*.html`, `pages/00.3_TOC.html`.
- **Outputs:** Modifies `pages/00.3_TOC.html`.
- **Usage:** `python3 ./system-workspace/tools/new-tools/fix_toc_answers.py`
- **Workflow Integration:** Belongs to the old batch workflow where TOC and answers were dynamically assembled post-generation. In the 1-Plan-Per-Page workflow, TOC structures are often explicitly built and modified per instruction rather than via automated batch parsing.

### `./system-workspace/tools/new-tools/test.py`
- **Status:** Trash/Obsolete
- **Purpose:** A simple scratchpad script testing the OpenAI API client against a local endpoint (`http://127.0.0.1:8045/v1`) using a specific model (`gemini-3-flash`).
- **Inputs:** None.
- **Outputs:** Prints the API response to the console.
- **Usage:** `python3 ./system-workspace/tools/new-tools/test.py`
- **Workflow Integration:** Irrelevant to both the old generation workflow and the 1-Plan-Per-Page workflow. It is purely a developer test script.

### `./system-workspace/tools/new-tools/clean_toc.py`
- **Status:** Usable
- **Purpose:** Removes extraneous part designations (e.g., "(الجزء الأول)") from the Table of Contents HTML files.
- **Inputs:** `pages/00.*_TOC.html`.
- **Outputs:** Modifies `pages/00.*_TOC.html` in place.
- **Usage:** `python3 ./system-workspace/tools/new-tools/clean_toc.py`
- **Workflow Integration:** A post-processing cleanup script from the old workflow. If titles in the 1-Plan-Per-Page workflow already omit these designations by default, this script becomes redundant.

### `./system-workspace/tools/new-tools/grid_search_ocr.py`
- **Status:** Usable
- **Purpose:** Performs a grid search over OCR parameters (Threshold, Contrast, PSM) using Tesseract and Pillow to find the most accurate configuration for converting PDF pages back to text by comparing them to ground truth text files.
- **Inputs:** `xxxz.pdf`, `ground_truth_page1.txt`, `ground_truth_page2.txt`, `ground_truth_page3.txt`.
- **Outputs:** Prints accuracy metrics for each configuration and outputs the best parameters to the console.
- **Usage:** `python3 ./system-workspace/tools/new-tools/grid_search_ocr.py`
- **Workflow Integration:** Not part of the HTML generation workflow (old or 1-Plan-Per-Page). It's an auxiliary tool for tuning OCR processing, likely used for extracting initial text content from existing PDF books.

### `./system-workspace/tools/new-tools/sync_exact_pages.py`
- **Status:** Needs fixing
- **Purpose:** Renders the entire HTML document using WeasyPrint in-memory to calculate physical page boundaries, and then renames the individual HTML files to include their exact rendered physical page number.
- **Inputs:** `pages/*.html`, `pages/cover/front-cover.jpg` (optional).
- **Outputs:** Renames `pages/*.html` files based on actual physical page calculation.
- **Usage:** `python3 ./system-workspace/tools/new-tools/sync_exact_pages.py`
- **Workflow Integration:** Highly integrated into the old batch workflow where pages might flow dynamically. The script currently struggles because `page.anchors` is handled differently depending on the WeasyPrint version, requiring fallback logic that may not assign page numbers correctly. In the 1-Plan-Per-Page workflow, content should be strictly bounded per file, mitigating the need for post-render physical page calculation.
