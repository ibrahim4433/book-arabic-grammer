### `./system-workspace/tools/automation/create_lesson_index.py`
- **Status:** Usable
- **Purpose:** Maps raw text transcriptions to exact lesson titles based on a provided TOC by finding the exact start and end line markers for each topic using the Gemini AI.
- **Inputs:** Raw text files in `system-workspace/text-data/raw/` and `input/TOC.json`.
- **Outputs:** `system-workspace/text-data/raw_to_lesson_index.json` containing the lesson mapping.
- **Usage:** `python system-workspace/tools/automation/create_lesson_index.py`
- **Workflow Integration:** Crucial for initial text processing. In the 1-Plan-Per-Page workflow, it can be run before text is sliced by page markers, or used in conjunction with paginated text to build a robust index of where concepts start and end across page boundaries.
