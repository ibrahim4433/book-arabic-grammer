### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_page_18.py`
- **Status:** Trash/Obsolete
- **Purpose:** Generates HTML output for Lesson 18 by hardcoding Arabic content and structural replacements using regex into templates.
- **Inputs:** Base templates (`TEMPLATE_C_*.html`) from `Jules-workspace/Templates/`.
- **Outputs:** An HTML file: `pages/18-الهمزة المتوسطة.html`.
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_page_18.py`
- **Workflow Integration:** This belongs to the old workflow (hardcoded lessons, single file output instead of 1-page-per-file), not compatible with the `1-Plan-Per-Page` workflow.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_30.py`
- **Status:** Trash/Obsolete
- **Purpose:** Generates HTML output for Lesson 30 across multiple pages dynamically checking layout (`verify_layout.py`) and adding filler content if underflowing.
- **Inputs:** Base templates (`TEMPLATE_C_*.html`) from `Jules-workspace/Templates/`.
- **Outputs:** Multiple HTML files: `pages/30.X_nXX_العاطفة.html`.
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_30.py`
- **Workflow Integration:** This belongs to the old workflow. Although it implements page breaking using layout checking, it operates on a full lesson basis and hardcodes all the content internally, not adhering to the `1-Plan-Per-Page` modular text slicing structure.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_26.py`
- **Status:** Trash/Obsolete
- **Purpose:** Generates HTML output for Lesson 26 dynamically using the layout checker to split overflowing pages and adds filler content.
- **Inputs:** Base templates from `Jules-workspace/Templates/`.
- **Outputs:** Multiple HTML files.
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_26.py`
- **Workflow Integration:** Similar to `generate_lesson_30.py`, this belongs to the old workflow. It processes a full lesson with hardcoded data rather than generating 1 page from an exact slice via `1-Plan-Per-Page`.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_27.py`
- **Status:** Trash/Obsolete
- **Purpose:** Generates HTML output for Lesson 27, explicitly splitting it across two pages statically via hardcoded blocks.
- **Inputs:** Base templates from `Jules-workspace/Templates/`.
- **Outputs:** `pages/27.0_n106_المحسنات_البديعية_1.html` and `pages/27.1_n107_المحسنات_البديعية_2.html`
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_27.py`
- **Workflow Integration:** Old workflow. It operates on a static lesson level, entirely hardcoding the content instead of dynamically processing per-page text chunks.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_14_helper.py`
- **Status:** Usable / Needs fixing
- **Purpose:** Helper script designed to initialize the `JulesPageGenerator` for Lesson 14 specifically, but does not actually run the process by default (commented out).
- **Inputs:** Plan file at `plans/14-الجامد والمشتق-plan.md`.
- **Outputs:** Intended to generate an HTML page via `JulesPageGenerator`.
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_14_helper.py`
- **Workflow Integration:** An ad-hoc helper tool. Doesn't quite match either workflow as a robust tool, but acts as a manual trigger for an older iteration of the agent's workflow.

### `./system-workspace/tools/new-tools/new-beta-page-maker/test_offline_youtube.py`
- **Status:** Usable
- **Purpose:** Tests the `YouTubeOfflineTranscriber` module to download and process audio/transcription from a specific YouTube video.
- **Inputs:** Hardcoded YouTube URL (`https://www.youtube.com/watch?v=sWCQMMfP8p8`).
- **Outputs:** Downloaded audio/transcripts within the respective workspace directories (via the transcriber logic), and prints success/fail messages to standard output.
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/test_offline_youtube.py`
- **Workflow Integration:** Extraneous testing script unrelated to the page planning or generation engine.

### `./system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_28.py`
- **Status:** Trash/Obsolete
- **Purpose:** Script for generating HTML output for Lesson 28 dynamically processing layout checking (inferred by similar structure to 26/30).
- **Inputs:** Base templates from `Jules-workspace/Templates/`.
- **Outputs:** Multiple HTML files.
- **Usage:** `python3 system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_28.py`
- **Workflow Integration:** Similar to `generate_lesson_30.py`, this belongs to the old workflow processing a full lesson with hardcoded data rather than generating 1 page from an exact slice.
