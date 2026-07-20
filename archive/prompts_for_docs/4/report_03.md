### `system-workspace/tools/automation/modules/jules_ocr.py`
- **Status:** Usable
- **Purpose:** Orchestrates the batch OCR process using Jules Sessions. It gathers images, creates parallel API sessions to process them in batches, and sequentially syncs/merges the resulting PRs.
- **Inputs:** Image files.
- **Outputs:** Triggers remote Jules sessions that output raw text files; eventually pulls these into local text data raw directory.
- **Usage:** `python jules_ocr.py` or used via `JulesOCR` class.
- **Workflow Integration:** This is a pre-processing step. It extracts the raw text from images which is then formatted with page markers to feed into the '1-Plan-Per-Page' engine.
