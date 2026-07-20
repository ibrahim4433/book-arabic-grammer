### `system-workspace/tools/new-tools/align_clean.py`
- **Status:** Usable
- **Purpose:** Aligns the raw OCR text with the processed output text to insert exact page break markers (`--- Page X ---`) into the raw text file.
- **Inputs:** `output.txt`, `system-workspace/text-data/raw/raw_001.txt`
- **Outputs:** Overwrites `system-workspace/text-data/raw/raw_001.txt` with inserted page markers.
- **Usage:** `python system-workspace/tools/new-tools/align_clean.py`
- **Workflow Integration:** Part of the initial data preparation phase to link raw text with physical pages.
