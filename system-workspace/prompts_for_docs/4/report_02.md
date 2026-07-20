### `system-workspace/tools/automation/modules/text_processing.py`
- **Status:** Usable
- **Purpose:** Validates TOC structure, merges raw OCR text files, maps raw text to lessons using Gemini, and provides an auto-pagination method based on page markers.
- **Inputs:** Reads raw text files from `system-workspace/text-data/raw`, `input/TOC.json`, `system-workspace/settings.json`.
- **Outputs:** Merged text `system-workspace/text-data/full_raw_indexed.txt`, updated `input/TOC.json`, index mapping `system-workspace/text-data/raw_to_lesson_index.json`.
- **Usage:** Programmatically used via `TextProcessor` class to manage text workflows.
- **Workflow Integration:** Very relevant to the '1-Plan-Per-Page' workflow as it handles slicing raw text into indexable pieces that bypass AI completely by relying on page markers.
