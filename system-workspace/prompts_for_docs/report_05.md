### `./system-workspace/tools/automation/modules/jules_client.py`
- **Status:** Usable
- **Purpose:** A robust client for the Google Jules (Code Assist) API (v1alpha). Handles session creation, monitoring, status polling, and error management.
- **Inputs:** Jules API key (from environment `JULES_API_KEY` or `secrets/Jules_API.txt`), user prompts, session titles, session IDs.
- **Outputs:** API responses (JSON session objects including session IDs and state updates).
- **Usage:** `client = JulesClient(); client.create_session(prompt, title)`
- **Workflow Integration:** Can be used in both the old and new '1-Plan-Per-Page' workflows to interact programmatically with the Jules coding agent, create implementation sessions, and poll for their completion.

### `./system-workspace/tools/automation/modules/full_auto_workflow.py`
- **Status:** Usable
- **Purpose:** Manages high-level automated workflow phases, particularly synchronizing plans and generated HTML pages with a GitHub repository, recovering missing plans/pages, and auditing/verifying HTML pages using various other tools (ID Manager, linting, etc.).
- **Inputs:** PR numbers, project state dictionaries, generated files (`-plan.md`, `.html`), GitHub API responses.
- **Outputs:** Downloaded files (plans, pages) and updated project states/stats.
- **Usage:** Typically instantiated within a larger orchestration script, e.g., `workflow = FullAutoWorkflow(); workflow._step_audit()`
- **Workflow Integration:** Essential for the overall generation pipeline. It can verify page generations, fitting well with a '1-Plan-Per-Page' model by verifying specific lesson plans and HTML output files one by one, downloading them from PRs, and auditing them.

### `./system-workspace/tools/automation/pattern_extractor.py`
- **Status:** Usable
- **Purpose:** Analyzes existing "Gold Standard" HTML pages to extract common design patterns (CSS classes, HTML structures, color usage) and outputs statistics to a JSON file.
- **Inputs:** HTML files located in the `pages/` directory matching a specific naming pattern (Lesson 1 to 08.4).
- **Outputs:** A JSON file `assets/design_patterns.json` containing class frequencies and structure/color usage stats.
- **Usage:** `python3 ./system-workspace/tools/automation/pattern_extractor.py`
- **Workflow Integration:** Acts as a reference generator. Useful before starting the '1-Plan-Per-Page' workflow to ensure Jules adheres to existing styling and structure rules based on golden examples.

### `./system-workspace/tools/automation/lesson_maker.py`
- **Status:** Usable
- **Purpose:** Combines multiple raw text files for specified lessons, generates an Architect Plan using Gemini, and dispatches the plan to a Jules session to generate code.
- **Inputs:** Lesson names, raw text data (`raw_*.txt`), project state (`project_state.json`), and index file (`raw_to_lesson_index.json`).
- **Outputs:** Saves a combined Markdown plan file (`plan_*_batch.md`) and creates a Jules session.
- **Usage:** `python3 ./system-workspace/tools/automation/lesson_maker.py "Lesson Name 1" "Lesson Name 2"`
- **Workflow Integration:** This implements a batching approach (combining multiple lessons into one plan). It directly contrasts with the new '1-Plan-Per-Page' workflow which demands single, exact text slices per page, but this script could potentially be adapted to handle single-page plans.

### `./system-workspace/tools/automation/workflow_manager.py`
- **Status:** Needs fixing
- **Purpose:** Manages the end-to-end workflow for a single lesson: generating a plan using `plan_refiner.py`, dispatching it to Jules via `requests`, answering developer questions via a ProxyAgent (Gemini), merging GitHub PRs, and verifying results.
- **Inputs:** Lesson name as CLI argument, raw text files.
- **Outputs:** Updates `project_state.json` (states like `STATE_PLANNED`, `STATE_CODED`), saved plan files, merged GitHub PRs, and verification logs.
- **Usage:** `python3 ./system-workspace/tools/automation/workflow_manager.py "Lesson 1"`
- **Workflow Integration:** It currently processes a full lesson at once. To fit the '1-Plan-Per-Page' model, this script needs refactoring to handle page-level boundaries rather than full lesson chunks, and to integrate properly with single-page strict rules.

### `./system-workspace/tools/automation/auto_book_maker.py`
- **Status:** Usable
- **Purpose:** A pipeline script that performs OCR on Arabic text images using Gemini, generates an Architect Plan from the transcribed text using Gemini, and sends the plan to Jules for implementation.
- **Inputs:** Images (`.jpg`, `.png`) from `input/` directory, and project rules/prompts.
- **Outputs:** Raw transcribed text files (`raw_*.txt`), generated plan files (`plan_*.md`), and Jules sessions.
- **Usage:** `python3 ./system-workspace/tools/automation/auto_book_maker.py`
- **Workflow Integration:** This script works file-by-file on images. If each image represents a single page, it naturally aligns with the '1-Plan-Per-Page' workflow.

### `./system-workspace/tools/automation/orchestrator.py`
- **Status:** Usable
- **Purpose:** Orchestrates the process of extracting text (via OCR/VisionGEM) from images or loading text, using the Architect (Gemini via CLI) to generate a plan, and dispatching it to Jules for execution. It acts as an orchestrator for the 'Architect-Jules' loop.
- **Inputs:** `--lesson` (raw text file) or `--image-dir` (directory of images), model selection, repo name.
- **Outputs:** Extracted text (`extracted_vision.txt`), generated plan (`latest_plan.md`), and a new Jules session.
- **Usage:** `python3 ./system-workspace/tools/automation/orchestrator.py --lesson path/to/lesson.txt`
- **Workflow Integration:** Highly integrated. This can serve the '1-Plan-Per-Page' workflow effectively if the input (`--lesson` or `--image-dir`) is restricted to the exact text slice intended for a single page, adhering strictly to the Golden Style Configurations without summarizing.
