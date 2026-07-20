### `system-workspace/tools/automation/modules/jules_client_ocr.py`
- **Status:** Usable
- **Purpose:** A specialized subclass of `JulesClient` for managing OCR tasks via Jules sessions. It handles creating specific OCR prompts, merging pull requests automatically, and pulling raw files from GitHub.
- **Inputs:** API keys (GitHub token, Jules key).
- **Outputs:** Remote PR merges, local git fetch/pull commands saving files to local raw directory.
- **Usage:** Programmatically used via `JulesOCRClient` class.
- **Workflow Integration:** A pre-processing component part of the raw data ingestion phase. It is agnostic to the '1-Plan-Per-Page' vs general workflow.
