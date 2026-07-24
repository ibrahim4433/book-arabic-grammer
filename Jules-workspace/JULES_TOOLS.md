# Jules Agent Tools

This document lists the essential tools available for the Jules agent, specifically tailored for the '1-Plan-Per-Page' workflow.

### `./Jules-workspace/batch_refactor.py`
- **Status:** Usable
- **Purpose:** A batch refactoring tool that performs regex-based search and replace operations across all HTML files in the `pages/` directory.
- **Inputs:** Requires `--pattern` (regex) and `--replace` (replacement string) arguments. Can accept an optional `--dry-run` flag.
- **Outputs:** Modifies HTML files in-place or prints potential changes to the console (if in dry-run mode).
- **Usage:** `python Jules-workspace/batch_refactor.py --pattern "old-class" --replace "new-class"`
- **Workflow Integration:** Useful for bulk updates to styling or element IDs when migrating from legacy designs to the new Golden Style Configurations in the 1-page workflow.

### `./Jules-workspace/id_manager.py`
- **Status:** Usable
- **Purpose:** Manages the generation and assignment of cryptographically unique `bXXXXX` IDs across significant structural elements in HTML files. Prevents ID collisions.
- **Inputs:** Scans target HTML files in `pages/` directory (or specified via `--files`).
- **Outputs:** Injects missing `id="bXXXXX"` properties to elements defined in `TARGET_SELECTORS` directly within the file (unless `--dry-run` is used). Can also print new IDs or verify duplicates.
- **Usage:** `python Jules-workspace/id_manager.py auto-tag --files pages/01.html`
- **Workflow Integration:** Plays a critical role in mapping specific content blocks. Should be run after a new 1-page HTML generation or refactoring, but strictly before `verify_layout.py` or linting processes.

### `./Jules-workspace/lint_autofixer.py`
- **Status:** Usable
- **Purpose:** Automatically scans all HTML files in `pages/` and replaces known bad/forbidden CSS classes with approved Golden Style equivalents (e.g., `border-dashed` to `border-light`). It also removes `<hr>` tags.
- **Inputs:** Scans all `.html` files in the `pages/` directory.
- **Outputs:** In-place modifications to HTML files, followed by automatically running `lint_pages.py` to verify the fixes.
- **Usage:** `python Jules-workspace/lint_autofixer.py`
- **Workflow Integration:** Can be run immediately after an agent generates a page to automatically correct minor styling hallucinations before the final layout verification is performed.

### `./Jules-workspace/lint_pages.py`
- **Status:** Usable
- **Purpose:** Lints HTML files for design constraints and allowable utility classes.
- **Inputs:** Target files (command-line arguments, defaults to all files in `pages/`) and Golden Style Configurations (dynamically read from CSS via `get_valid_utility_classes`).
- **Outputs:** Console messages showing errors, and optional JSON output. Fails fast if violations are found.
- **Usage:** `python Jules-workspace/lint_pages.py pages/01.html`
- **Workflow Integration:** Can verify new files immediately generated under the new '1-Plan-Per-Page' or legacy pipeline.

### `./Jules-workspace/lint_templates.py`
- **Status:** Usable
- **Purpose:** An Anti-Bloat Pre-Flight check for HTML templates to ensure they do not contain forbidden tags (`<hr>`), inline styles, or generic `<ul>` tags without required classes. Ensures templates are clean shells.
- **Inputs:** Reads all HTML template files in `Templates/` or `Jules-workspace/Templates/` (skipping `TEMPLATE_CHAPTER*`).
- **Outputs:** Console output indicating success or listing rule violations. Fails with exit code 1 if violations exist.
- **Usage:** `python Jules-workspace/lint_templates.py`
- **Workflow Integration:** Can be run during testing or before generation to ensure base templates adhere to global styling rules for the 1-page workflow.

### `./Jules-workspace/verify_layout.py`
- **Status:** Usable
- **Purpose:** Verifies that a generated HTML page renders exactly to one A4 page without overflowing or significantly underflowing. Uses WeasyPrint to simulate PDF rendering. Also runs `lint_pages.py` internally unless skipped.
- **Inputs:** The target HTML page file.
- **Outputs:** Console output or JSON output with a layout status (`PASS`, `FAIL`, `OVERFLOW`, `UNDERFLOW`) and recommendations for fixing.
- **Usage:** `python Jules-workspace/verify_layout.py pages/01.0_intro.html`
- **Workflow Integration:** Critical for the new 1-Plan-Per-Page workflow to verify that generated pages satisfy layout constraints before finalization.

### `./docs/Archive/C3/plus/C3/C3_Lessons_Text/old/test_gemini.py`
- **Status:** Usable
- **Purpose:** A simple diagnostic test script to verify connection to the Google GenAI API using the `gemini-2.5-flash` model.
- **Inputs:** None (relies on environment variables for API keys)
- **Outputs:** Standard output (prints success or error message)
- **Usage:** `python3 ./docs/Archive/C3/plus/C3/C3_Lessons_Text/old/test_gemini.py`
- **Workflow Integration:** Can be used generally as a diagnostic tool to verify the AI provider connection in both the old workflow and the new '1-Plan-Per-Page' workflow before running large batch generation tasks.

### `./network_ai_ocr/colab_surya_ocr.py`
- **Status:** Usable
- **Purpose:** A script intended to be run in a Google Colab notebook to perform batch Arabic OCR on PDF files stored in Google Drive using Surya OCR. It converts PDF pages to images and writes the extracted text page-by-page.
- **Inputs:** PDF files from Google Drive (`/content/drive/MyDrive/OCR`)
- **Outputs:** Text file (`..._ocr_output.txt`) in the same Drive folder.
- **Usage:** Run inside a Google Colab cell.
- **Workflow Integration:** Similar to `server.py`, this is an upstream text generation utility. It is highly relevant to the new '1-Plan-Per-Page' workflow, as its page-by-page output format (`--- Page X ---`) aligns closely with the new raw text slicing requirement (`----- PAGE X -----`).

### `./network_ai_ocr/server.py`
- **Status:** Usable
- **Purpose:** Runs a local FastAPI server hosting Surya OCR models to process uploaded images and extract Arabic text.
- **Inputs:** Image files via POST request to `/api/ocr`
- **Outputs:** JSON response containing the extracted text string.
- **Usage:** `python3 ./network_ai_ocr/server.py` (runs on `0.0.0.0:8000`)
- **Workflow Integration:** This tool acts as an independent external utility for converting scanned documents to raw text. It sits upstream of the new '1-Plan-Per-Page' workflow, which expects the raw text (with page markers) as its input.

### `./scripts/preview.py`
- **Status:** Usable
- **Purpose:** Renders individual HTML pages or templates from the pages directory into PDF format using WeasyPrint. It wraps the selected page in a master HTML template (injecting a global watermark text) to provide an accurate representation of how a single page will look when printed.
- **Inputs:**
  - Reads `.html` files from the pages directory.
  - Takes user input via CLI to select the file to render (by number or 't' for template).
- **Outputs:**
  - Writes a `.pdf` file to the generated output path.
- **Usage:** `python3 ./scripts/preview.py`
- **Workflow Integration:** In the new 1-Plan-Per-Page workflow (Options M & N), this tool is essential for the agent to verify that the generated HTML doesn't exceed a single PDF page before finalizing its task. It allows quick rendering of a single generated page into a PDF to check for layout issues without needing to compile the entire book.

### `./system-workspace/tools/automation/auto_book_maker.py`
- **Status:** Usable
- **Purpose:** A pipeline script that performs OCR on Arabic text images using Gemini, generates an Architect Plan from the transcribed text using Gemini, and sends the plan to Jules for implementation.
- **Inputs:** Images (`.jpg`, `.png`) from `input/` directory, and project rules/prompts.
- **Outputs:** Raw transcribed text files (`raw_*.txt`), generated plan files (`plan_*.md`), and Jules sessions.
- **Usage:** `python3 ./system-workspace/tools/automation/auto_book_maker.py`
- **Workflow Integration:** This script works file-by-file on images. If each image represents a single page, it naturally aligns with the '1-Plan-Per-Page' workflow.

### `./system-workspace/tools/automation/create_lesson_index.py`
- **Status:** Usable
- **Purpose:** Maps raw text transcriptions to exact lesson titles based on a provided TOC by finding the exact start and end line markers for each topic using the Gemini AI.
- **Inputs:** Raw text files in `system-workspace/text-data/raw/` and `input/TOC.json`.
- **Outputs:** `system-workspace/text-data/raw_to_lesson_index.json` containing the lesson mapping.
- **Usage:** `python system-workspace/tools/automation/create_lesson_index.py`
- **Workflow Integration:** Crucial for initial text processing. In the 1-Plan-Per-Page workflow, it can be run before text is sliced by page markers, or used in conjunction with paginated text to build a robust index of where concepts start and end across page boundaries.

### `./system-workspace/tools/automation/dispatch_jules.py`
- **Status:** Usable (Note: specific plans hardcoded)
- **Purpose:** Dispatches predefined `.md` plan files to the Jules AI API via POST requests to create new Github PR sessions for automated generation. It uses secrets to authenticate with Google's APIs.
- **Inputs:** Hardcoded paths (`output/plan_1.md`, `output/plan_2.md`), API Key at `secrets/Jules_API.txt`
- **Outputs:** Console progress/response status and created API session metadata.
- **Usage:** `python system-workspace/tools/automation/dispatch_jules.py`
- **Workflow Integration:** The API dispatcher. For the 1-Plan-Per-Page workflow, it needs to be updated to stop hardcoding logical lessons (e.g. "Lesson 28") and instead dynamically fetch or batch-process 1-page plans (Options M & N from the roadmap).

### `./system-workspace/tools/automation/lesson_compiler.py`
- **Status:** Usable
- **Purpose:** Parses a structured markdown plan to extract blocks and fields, then compiles these into an HTML page by injecting content into base layout templates (e.g., `TEMPLATE_C_BASE.html`, `TEMPLATE_C_PAGE_WRAPPER.html`).
- **Inputs:** Markdown plan file path (`<plan_file>`) and HTML templates located in `assets/Templates`.
- **Outputs:** Compiled HTML file saved into the `pages/` directory.
- **Usage:** `python system-workspace/tools/automation/lesson_compiler.py <plan_file>`
- **Workflow Integration:** Seamlessly fits the 1-Plan-Per-Page workflow. It compiles a single HTML page based directly on the plan provided. It uses the `TEMPLATE_C_PAGE_WRAPPER.html` to ensure content respects page limits.

### `./system-workspace/tools/automation/lesson_maker.py`
- **Status:** Usable
- **Purpose:** Combines multiple raw text files for specified lessons, generates an Architect Plan using Gemini, and dispatches the plan to a Jules session to generate code.
- **Inputs:** Lesson names, raw text data (`raw_*.txt`), project state (`project_state.json`), and index file (`raw_to_lesson_index.json`).
- **Outputs:** Saves a combined Markdown plan file (`plan_*_batch.md`) and creates a Jules session.
- **Usage:** `python3 ./system-workspace/tools/automation/lesson_maker.py "Lesson Name 1" "Lesson Name 2"`
- **Workflow Integration:** This implements a batching approach (combining multiple lessons into one plan). It directly contrasts with the new '1-Plan-Per-Page' workflow which demands single, exact text slices per page, but this script could potentially be adapted to handle single-page plans.

### `./system-workspace/tools/automation/modules/__init__.py`
- **Status:** Usable
- **Purpose:** An empty initialization file that marks the `modules` directory as a Python package, allowing its scripts to be imported by other modules.
- **Inputs:** None
- **Outputs:** None
- **Usage:** N/A (Imported automatically by Python when importing from `modules`)
- **Workflow Integration:** Required for both the old lesson-based workflow and the new '1-Plan-Per-Page' workflow to allow proper importing of the various module scripts (like compiler, state_manager, etc.).

### `./system-workspace/tools/automation/modules/compiler.py`
- **Status:** Usable
- **Purpose:** Compiles Architect Plans (Markdown) into final HTML pages. It parses `=== BLOCK ===` markers, extracts component names and fields, maps them to HTML templates via `plan_to_template.json`, handles markdown-to-HTML transformations (lists, tables), and wraps the final output in the `TEMPLATE_C_PAGE_WRAPPER.html`. It can also dispatch plans to Jules.
- **Inputs:** `plan_path` (Path to a generated markdown plan file)
- **Outputs:** Saves an `.html` file inside the `pages/` directory.
- **Usage:** `python system-workspace/tools/automation/modules/compiler.py "path/to/plan.md"`
- **Workflow Integration:** This is a core translation engine. In the old workflow, it compiles lesson plans. In the new '1-Plan-Per-Page' workflow (Options M & N), it will be used to compile the strict 1-page plans into individual HTML files, relying heavily on the new Golden Style CSS wrappers to ensure perfect fit.

### `./system-workspace/tools/automation/modules/full_auto_workflow.py`
- **Status:** Usable
- **Purpose:** Manages high-level automated workflow phases, particularly synchronizing plans and generated HTML pages with a GitHub repository, recovering missing plans/pages, and auditing/verifying HTML pages using various other tools (ID Manager, linting, etc.).
- **Inputs:** PR numbers, project state dictionaries, generated files (`-plan.md`, `.html`), GitHub API responses.
- **Outputs:** Downloaded files (plans, pages) and updated project states/stats.
- **Usage:** Typically instantiated within a larger orchestration script, e.g., `workflow = FullAutoWorkflow(); workflow._step_audit()`
- **Workflow Integration:** Essential for the overall generation pipeline. It can verify page generations, fitting well with a '1-Plan-Per-Page' model by verifying specific lesson plans and HTML output files one by one, downloading them from PRs, and auditing them.

### `./system-workspace/tools/automation/modules/jules_client.py`
- **Status:** Usable
- **Purpose:** A robust client for the Google Jules (Code Assist) API (v1alpha). Handles session creation, monitoring, status polling, and error management.
- **Inputs:** Jules API key (from environment `JULES_API_KEY` or `secrets/Jules_API.txt`), user prompts, session titles, session IDs.
- **Outputs:** API responses (JSON session objects including session IDs and state updates).
- **Usage:** `client = JulesClient(); client.create_session(prompt, title)`
- **Workflow Integration:** Can be used in both the old and new '1-Plan-Per-Page' workflows to interact programmatically with the Jules coding agent, create implementation sessions, and poll for their completion.

### `./system-workspace/tools/automation/modules/jules_youtube_dispatcher.py`
- **Status:** Usable
- **Purpose:** Resolves YouTube playlists or single URLs and dispatches automated tasks (via `JulesClient`) to a Jules AI session. It builds a detailed markdown prompt instructing the agent to download the media locally, transcribe it precisely in Arabic with Tashkeel, save it as a raw `.txt` file, and perform cleanup.
- **Inputs:** `video_url` (YouTube video URL), `video_title` (String), `seq_num` (Integer)
- **Outputs:** Creates a Jules session/PR that will generate a raw text file in `system-workspace/text-data/video-raw/`.
- **Usage:** `python -c "from modules.jules_youtube_dispatcher import JulesYouTubeDispatcher; d = JulesYouTubeDispatcher('.'); d.dispatch_session('https://www.youtube.com/watch?v=...', 'Title', 1)"`
- **Workflow Integration:** This allows outsourcing the heavy transcription work directly to a separate Jules AI agent session. It generates the base raw text material required before the core system can slice it and initiate the '1-Plan-Per-Page' generation engine.

### `./system-workspace/tools/automation/modules/pdf_ocr_local.py`
- **Status:** Usable
- **Purpose:** Extracts text from PDF files using local Tesseract OCR. It features smart image preprocessing (grayscale, thresholding), optimized OCR configurations for Arabic text, chunked processing for large PDFs, and a custom autocorrect dictionary to fix common Arabic OCR errors.
- **Inputs:** `pdf_path` (string: path to the source PDF file)
- **Outputs:** `output_txt_path` (string: path to the output raw text file)
- **Usage:** `python -c "from modules.pdf_ocr_local import LocalPDFOCR; ocr = LocalPDFOCR(); ocr.process_pdf('input.pdf', 'output.txt')"`
- **Workflow Integration:** This tool is typically used in the early stages of both workflows to convert raw source materials (PDFs) into text. Its output forms the foundational text that will eventually be sliced by page markers (for the '1-Plan-Per-Page' workflow) or by lessons (for the old workflow) before being fed to the Jules agent for planning.

### `./system-workspace/tools/automation/modules/state_manager.py`
- **Status:** Usable
- **Purpose:** Manages and persists the workflow state across the system by reading and writing to `project_workflow_state.json`. It tracks the progression status (e.g., OCR_DONE, PLAN_READY, PAGE_GENERATED) of lessons/pages, cleans up state for deleted files, and provides consolidated views.
- **Inputs:** State modifications (via class methods), internal JSON file.
- **Outputs:** Updates `system-workspace/tools/automation/project_workflow_state.json`.
- **Usage:** `python -c "from modules.state_manager import StateManager; sm = StateManager(); sm.update_lesson_status('Lesson 1', 'PLAN_READY')"`
- **Workflow Integration:** Acts as the central nervous system tracking progress. For the new '1-Plan-Per-Page' workflow, it will be critical to track the status of individual sliced pages rather than monolithic lessons to guarantee no pages are skipped during batch generation.

### `./system-workspace/tools/automation/modules/youtube_offline_transcriber.py`
- **Status:** Usable
- **Purpose:** Extracts YouTube transcripts directly via the `youtube_transcript_api` (bypassing `yt-dlp` to avoid 403 errors), prioritizing Arabic transcripts. It then applies full Arabic diacritics (Tashkeel) using the local Mishkal library and saves the output to a raw text file.
- **Inputs:** `url` (YouTube video URL), `title` (Video title for naming), `seq_num` (Sequence number for naming)
- **Outputs:** Saves a `.txt` file containing the diacritized transcript in `system-workspace/text-data/video-raw/`
- **Usage:** `python -c "from modules.youtube_offline_transcriber import YouTubeOfflineTranscriber; t = YouTubeOfflineTranscriber('.'); t.process_video('https://www.youtube.com/watch?v=...', 'Title', 1)"`
- **Workflow Integration:** Can be used to gather raw text content. The generated raw text files will later be sliced using `----- PAGE X -----` markers to feed the '1-Plan-Per-Page' engine, ensuring the AI agent receives perfectly diacritized Arabic source material for its page generation tasks.

### `./system-workspace/tools/automation/modules/youtube_transcriber.py`
- **Status:** Usable
- **Purpose:** Downloads YouTube video audio via `yt-dlp`, uploads the audio file to the Google Gemini File API, and instructs the Gemini AI model to transcribe the audio into Arabic with full diacritics (Tashkeel). It handles polling the API and local file cleanup.
- **Inputs:** `url` (YouTube video URL), `sequence_n` (Optional: Sequence number for naming output file)
- **Outputs:** Saves a `.txt` transcription file in `system-workspace/text-data/video-raw/` (e.g., `1y-raw.txt`)
- **Usage:** `python -c "from modules.youtube_transcriber import YouTubeTranscriber; t = YouTubeTranscriber(api_key='YOUR_KEY', project_root='.'); t.process_url('https://www.youtube.com/watch?v=...')"`
- **Workflow Integration:** Acts as an alternative, more intelligent transcript generator (compared to the offline Mishkal version) when standard YouTube transcripts are poor or unavailable. The high-quality, AI-transcribed output becomes the raw source text that will be processed by either the old workflow or paginated for the new '1-Plan-Per-Page' workflow.

### `./system-workspace/tools/automation/orchestrator.py`
- **Status:** Usable
- **Purpose:** Orchestrates the process of extracting text (via OCR/VisionGEM) from images or loading text, using the Architect (Gemini via CLI) to generate a plan, and dispatching it to Jules for execution. It acts as an orchestrator for the 'Architect-Jules' loop.
- **Inputs:** `--lesson` (raw text file) or `--image-dir` (directory of images), model selection, repo name.
- **Outputs:** Extracted text (`extracted_vision.txt`), generated plan (`latest_plan.md`), and a new Jules session.
- **Usage:** `python3 ./system-workspace/tools/automation/orchestrator.py --lesson path/to/lesson.txt`
- **Workflow Integration:** Highly integrated. This can serve the '1-Plan-Per-Page' workflow effectively if the input (`--lesson` or `--image-dir`) is restricted to the exact text slice intended for a single page, adhering strictly to the Golden Style Configurations without summarizing.

### `./system-workspace/tools/automation/pattern_extractor.py`
- **Status:** Usable
- **Purpose:** Analyzes existing "Gold Standard" HTML pages to extract common design patterns (CSS classes, HTML structures, color usage) and outputs statistics to a JSON file.
- **Inputs:** HTML files located in the `pages/` directory matching a specific naming pattern (Lesson 1 to 08.4).
- **Outputs:** A JSON file `assets/design_patterns.json` containing class frequencies and structure/color usage stats.
- **Usage:** `python3 ./system-workspace/tools/automation/pattern_extractor.py`
- **Workflow Integration:** Acts as a reference generator. Useful before starting the '1-Plan-Per-Page' workflow to ensure Jules adheres to existing styling and structure rules based on golden examples.

### `./system-workspace/tools/automation/plan_refiner.py`
- **Status:** Usable
- **Purpose:** Generates an architectural plan using a sticky Gemini model fallback chain and refines it via an auditing process (using another Gemini prompt) until the plan is approved or maximum retries are reached.
- **Inputs:** Raw text file path (`<raw_text_path>`), `TOC.json`, `design_patterns.json`, `Architect_GEM_MASTER.md` and `Architect_AUDITOR.md`.
- **Outputs:** Refined plan text file saved to `<output_plan_path>`.
- **Usage:** `python system-workspace/tools/automation/plan_refiner.py <raw_text_path> <output_plan_path>`
- **Workflow Integration:** Fits the new 1-Plan-Per-Page workflow perfectly. Instead of taking an entire lesson as input, it can take an exact text slice (a single page) and will enforce fitting constraints during the generation and auditing cycles (with updated 1-page specific Prompts).

### `./system-workspace/tools/automation/project_state.py`
- **Status:** Usable (May need fixing for 1-Page Workflow)
- **Purpose:** Manages, reads, updates, and verifies the current state of project generation (e.g., current lesson number, title, page index) by saving to a `project_state.json` file and parsing metadata from compiled HTML headers.
- **Inputs:** HTML files (for extracting metadata like page index and lesson number) and `project_state.json`.
- **Outputs:** `project_state.json` file and console outputs with state/verification results.
- **Usage:** `python system-workspace/tools/automation/project_state.py [init|read|update <filepath>|verify <filepath>]`
- **Workflow Integration:** Primarily designed for the old workflow where files and lessons track continuous progression. Needs to be adapted for the 1-Plan-Per-Page workflow to verify page indexes and handle page breaks within a single lesson properly, rather than relying solely on lesson titles.

### `./system-workspace/tools/automation/verify_headless.py`
- **Status:** Usable
- **Purpose:** Renders a given HTML page into a PDF in memory using WeasyPrint to verify if its visual footprint mathematically fits onto a single A4 page without overflowing. Outputs JSON results (`PASS` or `OVERFLOW`).
- **Inputs:** A path to an HTML file provided via command-line argument.
- **Outputs:** A rendered `.pdf` file in `output/debug/`, JSON text to stdout detailing the page status and count.
- **Usage:** `python system-workspace/tools/automation/verify_headless.py path/to/page.html`
- **Workflow Integration:** Highly critical for the 1-Plan-Per-Page logic. This script directly enforces the exact rule that one slice of content must physically fit into one printed page. Used by the agent dynamically during HTML generation to verify results.

### `./system-workspace/tools/automation/workflow_state.py`
- **Status:** Usable
- **Purpose:** Tracks the high-level workflow status (e.g., RAW, PLANNED, CODED, VERIFIED) and history of lessons, storing this information in a JSON file.
- **Inputs:** `tools/automation/project_workflow_state.json`
- **Outputs:** Updates and saves to `tools/automation/project_workflow_state.json`
- **Usage:** Used as an imported module, or executed directly to print state: `python system-workspace/tools/automation/workflow_state.py`
- **Workflow Integration:** Geared towards tracking progress per lesson. For the 1-Plan-Per-Page workflow, this would need adjusting to track state per *page* rather than per *lesson*, since pages are processed independently.

### `./system-workspace/tools/new-tools/align.py`
- **Status:** Usable
- **Purpose:** Aligns generated paginated output (`output.txt`) back to the original raw text file by performing fuzzy string matching, then inserts exact page break markers (`--- Page X ---`) into the raw text.
- **Inputs:** `output.txt` (containing paginated text) and `system-workspace/text-data/raw/raw_001.txt`.
- **Outputs:** A paginated version of the raw text saved as `system-workspace/text-data/raw/raw_001_paged.txt`.
- **Usage:** `python system-workspace/tools/new-tools/align.py`
- **Workflow Integration:** This tool directly enables the new 1-Plan-Per-Page workflow by injecting the `--- Page X ---` boundaries into raw text files, successfully slicing the text for the planner and page maker agents.

### `./system-workspace/tools/new-tools/align_dp.py`
- **Status:** Usable
- **Purpose:** Uses dynamic programming to align lines from a generated output file with original raw text based on trigram similarity, inserting page markers (`--- Page X ---`) into the raw text where they align.
- **Inputs:** `output.txt` and raw text files.
- **Outputs:** Modifies raw text files to include page markers.
- **Usage:** `python3 ./system-workspace/tools/new-tools/align_dp.py`
- **Workflow Integration:** A preparation tool used to paginate raw text. Since the 1-Plan-Per-Page workflow requires pre-paginated exact text slices, this tool helped generate the required inputs for that workflow.

### `./system-workspace/tools/new-tools/api.py`
- **Status:** Usable
- **Purpose:** A high-performance async FastAPI application that provides an API for rendering the Arabic Grammar Book PDFs on demand using WeasyPrint in a background thread.
- **Inputs:** `RenderRequest` (JSON) specifying `theme`, `watermark`, and `dry_run`. Reads `pages/*.html` and `styles/main.css` (or theme-specific CSS).
- **Outputs:** Generates a PDF file (`book.pdf`) in the specified theme directory or default export directory. Returns JSON success/error response or a downloadable file.
- **Usage:** `python api.py` (which runs `uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)`)
- **Workflow Integration:** Fits into the modern automated deployment/generation pipeline (likely integrating with the new workflow by dynamically serving the 1-Plan-Per-Page or full book PDF based on API calls).

### `./system-workspace/tools/new-tools/clean_toc.py`
- **Status:** Usable
- **Purpose:** Removes extraneous part designations (e.g., "(الجزء الأول)") from the Table of Contents HTML files.
- **Inputs:** `pages/00.*_TOC.html`.
- **Outputs:** Modifies `pages/00.*_TOC.html` in place.
- **Usage:** `python3 ./system-workspace/tools/new-tools/clean_toc.py`
- **Workflow Integration:** A post-processing cleanup script from the old workflow. If titles in the 1-Plan-Per-Page workflow already omit these designations by default, this script becomes redundant.

### `./system-workspace/tools/new-tools/count_pages.py`
- **Status:** Usable
- **Purpose:** Calculates the exact physical page length (number of PDF pages) each HTML file will consume by rendering them individually via WeasyPrint.
- **Inputs:** Reads all non-template HTML files in `pages/` and `styles/main.css`.
- **Outputs:** Prints out the starting page number and the length (in pages) for each HTML file, and the total expected page count.
- **Usage:** `python ./system-workspace/tools/new-tools/count_pages.py`
- **Workflow Integration:** Critical for the 1-Plan-Per-Page workflow to verify if specific HTML slices underflow or overflow their targeted page counts before full book compilation.

### `./system-workspace/tools/new-tools/fix_content.py`
- **Status:** Usable / Needs fixing
- **Purpose:** Performs a series of hardcoded string replacements across multiple specific HTML lesson files in the `pages/` directory to fix typos, update examples, or correct grammar/spelling in the Arabic text.
- **Inputs:** Reads various `pages/*.html` files specified in the `replacements` dictionary.
- **Outputs:** Modifies and saves the same `pages/*.html` files if changes are found.
- **Usage:** `python system-workspace/tools/new-tools/fix_content.py`
- **Workflow Integration:** This is a hardcoded content patcher. It operates on specific files and strings. While it fixes content, in the 1-Plan-Per-Page workflow, content fixes should ideally be handled within the page's specific plan or source generation rather than relying on a global post-processing script that assumes specific filenames and exact string matches.

### `./system-workspace/tools/new-tools/fix_filenames.py`
- **Status:** Usable
- **Purpose:** Cleans up generated HTML filenames in the `pages/` directory by stripping unneeded strings (like "(تابع)"), removing duplicate underscores, and attempting to extract the true Arabic title from the `<h1>` tag inside the file to rename it appropriately. It skips templates and TOC pages.
- **Inputs:** `pages/*.html` (specifically looks for files matching the regex pattern and reads `<h1>` tags).
- **Outputs:** Renames files within the `pages/` directory. Also deletes `pages/00.0_blank_page1.html` if it exists.
- **Usage:** `python3 ./system-workspace/tools/new-tools/fix_filenames.py`
- **Workflow Integration:** Can be used in the old workflow where batch processing and automated title extraction for filenames were needed. In the strict 1-Plan-Per-Page workflow, filenames are usually strictly controlled and explicitly handled during the plan, rendering this tool somewhat less critical but still potentially useful for batch cleanup.

### `./system-workspace/tools/new-tools/fix_metadata.py`
- **Status:** Usable
- **Purpose:** Automatically updates HTML headers, `<title>` tags, and lesson numbers in all lesson and answer HTML files to match the structural metadata inferred from their filenames.
- **Inputs:** Reads all `pages/*.html` files (excluding templates and specific prefixes).
- **Outputs:** Overwrites the modified HTML files in-place with corrected Arabic indic numerals, titles, and lesson details.
- **Usage:** `python ./system-workspace/tools/new-tools/fix_metadata.py`
- **Workflow Integration:** Heavily supports the 1-Plan-Per-Page workflow by ensuring each isolated HTML slice remains perfectly self-consistent in its metadata according to its filename before final compilation.

### `./system-workspace/tools/new-tools/fix_other.py`
- **Status:** Usable
- **Purpose:** Replaces specific placeholder text in generated Arabic HTML files with completed text and fixes unapproved CSS classes.
- **Inputs:** `Jules-workspace/pages/*_تابع.html`
- **Outputs:** Overwrites the input files in place.
- **Usage:** `python3 ./system-workspace/tools/new-tools/fix_other.py`
- **Workflow Integration:** Primarily a cleanup script for the old workflow to fix text omissions, but could serve as a post-processing tool if the 1-Plan-Per-Page workflow still produces uncompleted text placeholders.

### `./system-workspace/tools/new-tools/fix_toc_answers.py`
- **Status:** Usable
- **Purpose:** Updates the Table of Contents (`00.3_TOC.html`) answer section by looking at `backup_answers/98.*.html` files, parsing which lesson numbers appear on which pages, and replacing generic TOC entries (like "مُلْحَقُ الْإِجَابَاتِ - جُزْءٌ") with specific lesson numbers (e.g., "إِجَابَاتُ الدَّرْسِ 6").
- **Inputs:** `backup_answers/98.*.html`, `pages/00.3_TOC.html`.
- **Outputs:** Modifies `pages/00.3_TOC.html`.
- **Usage:** `python3 ./system-workspace/tools/new-tools/fix_toc_answers.py`
- **Workflow Integration:** Belongs to the old batch workflow where TOC and answers were dynamically assembled post-generation. In the 1-Plan-Per-Page workflow, TOC structures are often explicitly built and modified per instruction rather than via automated batch parsing.

### `./system-workspace/tools/new-tools/grid_search_ocr.py`
- **Status:** Usable
- **Purpose:** Performs a grid search over OCR parameters (Threshold, Contrast, PSM) using Tesseract and Pillow to find the most accurate configuration for converting PDF pages back to text by comparing them to ground truth text files.
- **Inputs:** `xxxz.pdf`, `ground_truth_page1.txt`, `ground_truth_page2.txt`, `ground_truth_page3.txt`.
- **Outputs:** Prints accuracy metrics for each configuration and outputs the best parameters to the console.
- **Usage:** `python3 ./system-workspace/tools/new-tools/grid_search_ocr.py`
- **Workflow Integration:** Not part of the HTML generation workflow (old or 1-Plan-Per-Page). It's an auxiliary tool for tuning OCR processing, likely used for extracting initial text content from existing PDF books.

### `./system-workspace/tools/new-tools/index_and_toc.py`
- **Status:** Usable
- **Purpose:** Parses a raw text file to create an indexed version (adding line numbers) and extracts TOC (Table of Contents) information based on page markers, saving it as a JSON file.
- **Inputs:** `system-workspace/text-data/raw/raw_001.txt`
- **Outputs:** `system-workspace/text-data/raw_001_indexed.txt`, `input/TOC.json`
- **Usage:** `python3 system-workspace/tools/new-tools/index_and_toc.py`
- **Workflow Integration:** This tool fits into the initial stages of processing raw text and creating a TOC. It seems geared towards the general workflow rather than being specific to the 1-Plan-Per-Page approach.

### `./system-workspace/tools/new-tools/make_index.py`
- **Status:** Usable
- **Purpose:** Parses raw lesson text files (`raw1.txt` to `raw13.txt`) against a Table of Contents (`TOC.json`) to map the exact starting and ending line locations (`file:line_num`) for each lesson. It outputs an indexed version of the raw text and a JSON map of lesson boundaries.
- **Inputs:** `C3_Lessons_Text/TOC.json`, `C3_Lessons_Text/raw1.txt` to `raw13.txt`.
- **Outputs:** `C3_Lessons_Text/full_raw_indexed.txt`, `C3_Lessons_Text/raw_to_lesson_index.json`.
- **Usage:** `python3 ./system-workspace/tools/new-tools/make_index.py`
- **Workflow Integration:** Part of the old text preprocessing workflow to track exact text segments. With the 1-Plan-Per-Page workflow operating on predefined HTML slices and precise Markdown chunks, mapping raw txt files to lessons may no longer be required.

### `./system-workspace/tools/new-tools/merge_answers.py`
- **Status:** Usable / Needs fixing
- **Purpose:** Merges the content of two HTML answer files (`98.00_p120_Answers.html` and `98.43_p163_Answers.html`) into one, by appending the content of the second file (excluding headers) into the first file's container, and then deletes the second file.
- **Inputs:** `pages/98.00_p120_Answers.html`, `pages/98.43_p163_Answers.html`
- **Outputs:** Modifies `pages/98.00_p120_Answers.html`, deletes `pages/98.43_p163_Answers.html`
- **Usage:** `python system-workspace/tools/new-tools/merge_answers.py`
- **Workflow Integration:** This script appears to be a one-off or transitional tool used to consolidate split answer pages into a single logical file, possibly prior to rebuilding TOC or fixing physical pages. It may conflict with the 1-Plan-Per-Page workflow if it dynamically alters layout structures across multiple physical pages without verifying layout constraints.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_25.py`
- **Status:** Usable
- **Purpose:** Parses a plan text file (`plan.txt`), generates HTML blocks using templates, checks the layout dynamically, and splits the content across multiple pages if overflow is detected.
- **Inputs:** `plan.txt`, `Jules-workspace/Templates/*.html`
- **Outputs:** `pages/25.X_nXX_علامات الترقيم.html`
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_25.py`
- **Workflow Integration:** This script directly implements the dynamic parsing and generation envisioned in the 1-Plan-Per-Page workflow, converting a structured plan into verified HTML pages.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_plan.py`
- **Status:** Usable
- **Purpose:** Generates a sample markdown execution plan string outlining constraints and structure for an AI agent to build a specific lesson page.
- **Inputs:** None (contains hardcoded string)
- **Outputs:** A markdown file (a plan file containing the generated string mentioning `pages/01.0...`).
- **Usage:** `python generate_plan.py`
- **Workflow Integration:** Fits into the new '1-Plan-Per-Page' workflow as a utility to produce template plan structures for the AI agent to follow, setting the rules and content stream.

### `./system-workspace/tools/new-tools/new-beta-page-maker/test_plan.py`
- **Status:** Usable
- **Purpose:** Tests a specific plan markdown file (`01-أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ-plan.md`) to ensure it meets minimum requirements, such as having at least 4 blocks, including mandatory components, correct author metadata, and class usage.
- **Inputs:** `plans/01-أَقْسَامُ الْكَلَاَمِ الْمُفِيدِ فِي اللُّغَةَ الْعَرَبِيَّةَ-plan.md`
- **Outputs:** Console output (pass/fail assertions)
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/test_plan.py`
- **Workflow Integration:** Fits perfectly into the 1-Plan-Per-Page workflow by acting as a validator for generated plan files before they are processed into HTML.

### `./system-workspace/tools/new-tools/parse_pdf.py`
- **Status:** Usable
- **Purpose:** Scans the final generated PDF (`book.pdf`) to locate and extract pages containing answer keys ("إجابات:") by dumping their raw text.
- **Inputs:** Reads `output/export/book.pdf`.
- **Outputs:** Writes a JSON dump file `pdf_text_dump.json` containing a list of page numbers and their corresponding raw text.
- **Usage:** `python ./system-workspace/tools/new-tools/parse_pdf.py`
- **Workflow Integration:** A utility script, likely used in a transition/verification phase to extract data from an existing monolithic PDF (old workflow) for debugging or migrating into the new 1-Plan-Per-Page structure.

### `./system-workspace/tools/new-tools/rebuild_toc_paginated.py`
- **Status:** Usable
- **Purpose:** Rebuilds the Table of Contents (TOC) into multiple paginated HTML files by chunking TOC rows and answer references to prevent visual overflow.
- **Inputs:** `backup_answers/98.*.html` and `pages/00.3_TOC.html.bak`
- **Outputs:** Multiple paginated HTML files representing the new TOC.
- **Usage:** `python3 ./system-workspace/tools/new-tools/rebuild_toc_paginated.py`
- **Workflow Integration:** Directly aligns with the 1-Plan-Per-Page workflow by calculating and enforcing strict page item limits to prevent layout overflow in the final PDF.

### `./system-workspace/tools/new-tools/rename_final.py`
- **Status:** Usable
- **Purpose:** Renders HTML pages (excluding templates) into a single WeasyPrint document and determines the absolute PDF page number for each file by injecting anchors. It calculates an offset based on a target file containing '98.34' (with a fallback) and renames the source HTML files using a regex-based pattern to include their calculated pagination.
- **Inputs:** `pages/*.html`, optional `pages/cover/front-cover.jpg`.
- **Outputs:** Renames HTML files in the `pages/` directory.
- **Usage:** `python3 system-workspace/tools/new-tools/rename_final.py`
- **Workflow Integration:** Syncs file names with actual PDF page numbers. Useful for the old workflow; for the 1-Plan-Per-Page workflow, it might need adjustments if the page mapping is already strict.

### `./system-workspace/tools/new-tools/rename_to_absolute.py`
- **Status:** Usable
- **Purpose:** Determines the absolute page number in the final compiled PDF for each source HTML file by injecting anchors and rendering a virtual PDF using WeasyPrint.
- **Inputs:** Reads all HTML files in the `pages/` directory (excluding templates), `styles/main.css`, and a front cover image if present.
- **Outputs:** Prints out the mapping of HTML filenames to their absolute page numbers in the resulting PDF. Does not directly modify files.
- **Usage:** `python ./system-workspace/tools/new-tools/rename_to_absolute.py`
- **Workflow Integration:** Useful for aligning the logical 1-Plan-Per-Page HTML files with the final continuous physical PDF layout, helping trace where a specific HTML snippet lands in the final book.

### `./system-workspace/tools/new-tools/rename_to_physical.py`
- **Status:** Usable / Needs fixing
- **Purpose:** Renames HTML files in the `pages/` directory to include the physical page number they will start on in the final PDF. It does this by rendering each HTML file using WeasyPrint to determine how many physical pages it spans, maintaining a running total to calculate the starting page of the next file.
- **Inputs:** `pages/*.html`
- **Outputs:** Renames `pages/*.html` files (modifies filenames, not contents).
- **Usage:** `python system-workspace/tools/new-tools/rename_to_physical.py`
- **Workflow Integration:** Useful for syncing filenames with physical page numbers, but it requires running WeasyPrint on every file sequentially which is slow. In the strict 1-Plan-Per-Page workflow, files should ideally map 1:1 to physical pages, making this tool potentially redundant or indicating that files are still spanning multiple pages.

### `./system-workspace/tools/new-tools/update_answers.py`
- **Status:** Usable
- **Purpose:** Synchronizes lesson numbers in the master answers file (`98.00_p120_Answers.html`) based on the current sequential numbering of the main lesson HTML files.
- **Inputs:** Reads `pages/*.html` lesson files to build a mapping, and reads `pages/98.00_p120_Answers.html`.
- **Outputs:** Overwrites `pages/98.00_p120_Answers.html` with updated Arabic lesson numbers and corresponding HTML `id` attributes.
- **Usage:** `python ./system-workspace/tools/new-tools/update_answers.py`
- **Workflow Integration:** Part of the maintenance for the new workflow, ensuring the consolidated answers index stays in sync when 1-Plan-Per-Page lesson files are added, removed, or renumbered.

### `system-workspace/tools/automation/modules/auditor.py`
- **Status:** Usable
- **Purpose:** Acts as a Quality Assurance module. It runs verification scripts on generated HTML pages to check for layout overflows and linting errors.
- **Inputs:** Takes the path to an HTML file (e.g. `pages/01.html`). Uses internal tools like `Jules-workspace/verify_layout.py` and `Jules-workspace/lint_pages.py`.
- **Outputs:** Returns a status dictionary (`PASS` or `FAIL`) with details about layout and lint checks.
- **Usage:** ``python3 -c "from system_workspace.tools.automation.modules.auditor import Auditor; a = Auditor(); print(a.audit_page('pages/01.html'))"``
- **Workflow Integration:** Crucial for the '1-Plan-Per-Page' workflow. It validates that the generated HTML strictly adheres to the 'One-Page Law' (fits visually without overflow) and conforms to structural/linting rules before finalizing the page.

### `system-workspace/tools/automation/modules/jules_client_ocr.py`
- **Status:** Usable
- **Purpose:** A specialized subclass of `JulesClient` for managing OCR tasks via Jules sessions. It handles creating specific OCR prompts, merging pull requests automatically, and pulling raw files from GitHub.
- **Inputs:** API keys (GitHub token, Jules key).
- **Outputs:** Remote PR merges, local git fetch/pull commands saving files to local raw directory.
- **Usage:** Programmatically used via `JulesOCRClient` class.
- **Workflow Integration:** A pre-processing component part of the raw data ingestion phase. It is agnostic to the '1-Plan-Per-Page' vs general workflow.

### `system-workspace/tools/automation/modules/jules_client_plans.py`
- **Status:** Usable
- **Purpose:** Orchestrates the generation of Markdown plans by interacting with Jules and GitHub. Includes sophisticated logic for extracting PR details, pulling files via `git`, and constructing a massive 'mega prompt' for plan generation.
- **Inputs:** Takes lesson data (number, title, raw_text, metadata) and raw agent prompts.
- **Outputs:** Pulls generated plan `.md` files directly using Git checkout. Constructs the combined AI prompt string.
- **Usage:** `Used programmatically: `client = JulesPlanClient(); client.pull_plan_from_github(details, 'file.md')``
- **Workflow Integration:** Highly critical for the '1-Plan-Per-Page' workflow (Option M). The `construct_mega_prompt` function is responsible for injecting the explicit instructions (1-page fit, exact text slices, forbidden summaries) into the prompt sent to the Jules planner agent.

### `system-workspace/tools/automation/modules/jules_ocr.py`
- **Status:** Usable
- **Purpose:** Orchestrates the batch OCR process using Jules Sessions. It gathers images, creates parallel API sessions to process them in batches, and sequentially syncs/merges the resulting PRs.
- **Inputs:** Image files.
- **Outputs:** Triggers remote Jules sessions that output raw text files; eventually pulls these into local text data raw directory.
- **Usage:** `python jules_ocr.py` or used via `JulesOCR` class.
- **Workflow Integration:** This is a pre-processing step. It extracts the raw text from images which is then formatted with page markers to feed into the '1-Plan-Per-Page' engine.

### `system-workspace/tools/automation/modules/jules_page_generator.py`
- **Status:** Usable
- **Purpose:** Submits generated Markdown plans to a Jules AI session, monitors the session, answers questions via Gemini, and pulls the finalized HTML file via PR.
- **Inputs:** Reads Markdown plans from the `plans/` directory.
- **Outputs:** Produces the final `.html` file, downloading it to `pages/` or `Jules-workspace/pages/`. Saves session IDs to the state manager.
- **Usage:** ``python3 -c "from system_workspace.tools.automation.modules.jules_page_generator import JulesPageGenerator; g = JulesPageGenerator('.'); g.run_batch_generation()"``
- **Workflow Integration:** Currently geared towards full lessons. For the '1-Plan-Per-Page' update (Option N), this module needs to handle the specialized 1-page agent prompts and enforce the strict file naming (`nXX` instead of lesson-based names). It executes the final step of turning a 1-page plan into a physical 1-page HTML.

### `system-workspace/tools/automation/modules/jules_planner.py`
- **Status:** Usable
- **Purpose:** Orchestrates batch generation of lesson plans using Jules Sessions. It reads the text index, extracts text slices, constructs prompts, monitors remote Jules planning sessions, and pulls the resulting plan files.
- **Inputs:** System prompts and text index files.
- **Outputs:** Markdown plan files saved to `plans/` directory.
- **Usage:** Programmatically used via `JulesPlanner` class to execute batch generation.
- **Workflow Integration:** Needs minor adjustments to fit the '1-Plan-Per-Page' workflow. Currently maps texts to plans but must adapt its prompts strictly to page markers instead of broader lessons.

### `system-workspace/tools/automation/modules/pattern_extractor.py`
- **Status:** Usable
- **Purpose:** Analyzes existing HTML pages to extract design patterns, structural rules, and common component sequences.
- **Inputs:** Reads all HTML files located in the `pages/` directory.
- **Outputs:** Generates a rich JSON guide for Jules located at `Jules-workspace/design_patterns.json`.
- **Usage:** ``python3 system-workspace/tools/automation/modules/pattern_extractor.py``
- **Workflow Integration:** Provides essential context (Golden Flow, Component Frequencies) for the planner agents. In the '1-Plan-Per-Page' workflow, this helps the agent understand which templates to use and how they flow visually on a page, though it may need to be run against 1-page test files to extract 1-page specific patterns.

### `system-workspace/tools/automation/modules/pdf_ocr_network.py`
- **Status:** Usable
- **Purpose:** Converts local PDF files into images page-by-page and sends them to a network AI server for OCR processing, returning the extracted text.
- **Inputs:** Local PDF file path, output TXT file path.
- **Outputs:** Extracted text saved to the specified TXT file.
- **Usage:** Instantiated as `NetworkPDFOCR(server_ip)` and called via `.process_pdf(pdf_path, output_txt_path)`.
- **Workflow Integration:** Acts as an alternative OCR ingestion method to Jules. Fits into the pre-processing stage to get raw text, which must then be manually paginated for the '1-Plan-Per-Page' engine.

### `system-workspace/tools/automation/modules/planner.py`
- **Status:** Usable
- **Purpose:** Generates structured lesson plans using the Architect (Gemini) Persona by calling the Gemini API with raw Arabic text, metadata, and design patterns.
- **Inputs:** Reads from `system-workspace/Architect_GEM_MASTER.md`, `system-workspace/tools/automation/project_state.json`, `input/TOC.json`.
- **Outputs:** Markdown plan file in `plans/` directory.
- **Usage:** Used programmatically to generate lesson plans from raw text.
- **Workflow Integration:** This tool fits into both workflows but is primarily designed for the older lesson-based planning where it uses TOC data. To fully support the new '1-Plan-Per-Page' workflow (`ROADMAP_1_PAGE_PLAN.md`), it would need to strictly focus on the single page's text slice without relying heavily on whole-lesson metadata.

### `system-workspace/tools/automation/modules/text_processing.py`
- **Status:** Usable
- **Purpose:** Validates TOC structure, merges raw OCR text files, maps raw text to lessons using Gemini, and provides an auto-pagination method based on page markers.
- **Inputs:** Reads raw text files from `system-workspace/text-data/raw`, `input/TOC.json`, `system-workspace/settings.json`.
- **Outputs:** Merged text `system-workspace/text-data/full_raw_indexed.txt`, updated `input/TOC.json`, index mapping `system-workspace/text-data/raw_to_lesson_index.json`.
- **Usage:** Programmatically used via `TextProcessor` class to manage text workflows.
- **Workflow Integration:** Very relevant to the '1-Plan-Per-Page' workflow as it handles slicing raw text into indexable pieces that bypass AI completely by relying on page markers.

### `system-workspace/tools/automation/modules/unified_flow.py`
- **Status:** Usable
- **Purpose:** Manages concurrent generation of Plans and Pages using a unified task queue and thread pool. Identifies missing plans and pages, runs JulesPlanner and JulesPageGenerator, and monitors their tasks.
- **Inputs:** Reads `system-workspace/text-data/raw_to_lesson_index.json` to identify pending tasks. Also checks filesystem in `plans/` to see what is already generated.
- **Outputs:** Updates task statuses and eventually triggers creation of Plan `.md` and HTML files (via its sub-tools). Outputs logs via callbacks.
- **Usage:** ``python3 -c "from system_workspace.tools.automation.modules.unified_flow import UnifiedProductionManager; m = UnifiedProductionManager('.'); m.populate_queue([]); m.run()"``
- **Workflow Integration:** In the 'old' lesson-based workflow, it generates whole lesson plans. For the '1-Plan-Per-Page' workflow, it will need to be updated to populate tasks based on 1-page slices rather than full lessons (e.g. reading from a paginated index instead of `raw_to_lesson_index.json`).

### `system-workspace/tools/automation/modules/youtube_ui.py`
- **Status:** Usable
- **Purpose:** A CLI user interface (using `questionary` and `rich`) for offline batch transcription of YouTube videos, applying Tashkeel to Arabic text.
- **Inputs:** Takes a YouTube URL or reads a CSV file containing URLs and titles from `input/csv-youtube/` or `Pdf-new-resource/`.
- **Outputs:** Calls `YouTubeOfflineTranscriber` to download audio and produce transcriptions (usually text/JSON files, though the actual writing is done by the transcriber module). Outputs progress tables to the terminal.
- **Usage:** ``python3 system-workspace/tools/automation/modules/youtube_ui.py``
- **Workflow Integration:** It operates independently of the '1-Plan-Per-Page' book generation workflow. It is an auxiliary tool used for gathering or processing raw data/audio before it enters the book generation pipeline.


### `./Jules-workspace/generate.py`
- **Status:** Usable
- **Purpose:** Minimal HTML template generation script used as a baseline reference.
- **Inputs:** None.
- **Outputs:** Generates a minimal HTML output.
- **Usage:** `python Jules-workspace/generate.py`
- **Workflow Integration:** Reference script for template generation.
