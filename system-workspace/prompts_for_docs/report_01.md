### `./system-workspace/generate_index.py`
- **Status:** Usable
- **Purpose:** Generates an index map in JSON format mapping headings (extracted from `full_raw_indexed.txt` with markers like `[...]`) to their title, start marker, and end marker (the marker right before the next heading). It normalizes titles by stripping Arabic tashkeel.
- **Inputs:** `system-workspace/text-data/full_raw_indexed.txt`
- **Outputs:** Standard output (JSON)
- **Usage:** `python system-workspace/generate_index.py`
- **Workflow Integration:** Supports processing raw content by generating a structured map. Useful for automating page divisions or structuring content correctly for the old system or as a foundation step for new 1-page slices.

### `./system-workspace/check_headings.py`
- **Status:** Usable
- **Purpose:** Prints out all headings found in `input/TOC.json` followed by all raw headings (with diacritics removed) found in `full_raw_indexed.txt` to help visually cross-reference and verify TOC titles exist in the raw index.
- **Inputs:** `input/TOC.json`, `system-workspace/text-data/full_raw_indexed.txt`
- **Outputs:** Standard output (Text)
- **Usage:** `python system-workspace/check_headings.py`
- **Workflow Integration:** Part of data preparation and validation logic, useful for both 1-page generation or logical lesson tracking to ensure table of contents headings align correctly with parsed text headers.

### `./system-workspace/check_titles.py`
- **Status:** Usable
- **Purpose:** Normalizes titles from `input/TOC.json` (removing diacritics) and systematically searches `full_raw_indexed.txt` for them. Prints any matches found, helping verify that TOC entries accurately correspond to the indexed raw text map.
- **Inputs:** `input/TOC.json`, `system-workspace/text-data/full_raw_indexed.txt`
- **Outputs:** Standard output (Text)
- **Usage:** `python system-workspace/check_titles.py`
- **Workflow Integration:** Validation tooling for verifying text and structure synchronization before slicing and planning, aligning with "Option L (Raw Processing)" which precedes plan-generation tasks.

### `./system-workspace/tools/automation/all_pics_to_text.py`
- **Status:** Usable
- **Purpose:** Orchestrates batch OCR using the Gemini model. Takes all images in `input/`, triggers text transcription using `gemini`, skipping already transcribed files, outputs them to a raw text directory, and then calls a post-processing cleaner script.
- **Inputs:** Directory `input/` (`*.png`, `*.jpg`)
- **Outputs:** Text files in `system-workspace/text-data/raw/` (`raw_X.txt`)
- **Usage:** `python system-workspace/tools/automation/all_pics_to_text.py`
- **Workflow Integration:** The foundational ingestion tool to retrieve Arabic text. Operates entirely independently of 1-page constraints. Feeds text into the pipeline before slicing logic takes over.

### `./system-workspace/tools/automation/dispatch_jules.py`
- **Status:** Usable (Note: specific plans hardcoded)
- **Purpose:** Dispatches predefined `.md` plan files to the Jules AI API via POST requests to create new Github PR sessions for automated generation. It uses secrets to authenticate with Google's APIs.
- **Inputs:** Hardcoded paths (`output/plan_1.md`, `output/plan_2.md`), API Key at `secrets/Jules_API.txt`
- **Outputs:** Console progress/response status and created API session metadata.
- **Usage:** `python system-workspace/tools/automation/dispatch_jules.py`
- **Workflow Integration:** The API dispatcher. For the 1-Plan-Per-Page workflow, it needs to be updated to stop hardcoding logical lessons (e.g. "Lesson 28") and instead dynamically fetch or batch-process 1-page plans (Options M & N from the roadmap).

### `./system-workspace/tools/automation/verify_headless.py`
- **Status:** Usable
- **Purpose:** Renders a given HTML page into a PDF in memory using WeasyPrint to verify if its visual footprint mathematically fits onto a single A4 page without overflowing. Outputs JSON results (`PASS` or `OVERFLOW`).
- **Inputs:** A path to an HTML file provided via command-line argument.
- **Outputs:** A rendered `.pdf` file in `output/debug/`, JSON text to stdout detailing the page status and count.
- **Usage:** `python system-workspace/tools/automation/verify_headless.py path/to/page.html`
- **Workflow Integration:** Highly critical for the 1-Plan-Per-Page logic. This script directly enforces the exact rule that one slice of content must physically fit into one printed page. Used by the agent dynamically during HTML generation to verify results.

### `./system-workspace/tools/automation/modules/vision.py`
- **Status:** Usable
- **Purpose:** A utility module containing the `VisionClient` class which interfaces with `gemini_client.py`. It packages exact prompt instructions to extract strict diacritic-preserved Arabic text from images without added filler.
- **Inputs:** A list of image paths via python function call.
- **Outputs:** Returns the raw extracted Arabic text as a string.
- **Usage:** Used as a library/module by other scripts (e.g. `client = VisionClient()`)
- **Workflow Integration:** An upstream dependency for extracting content from book pictures. Serves as the OCR backbone to build the raw Arabic text that eventually gets paginated in later phases.
