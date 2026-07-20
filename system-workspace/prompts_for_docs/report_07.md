### `./system-workspace/tools/new-tools/align.py`
- **Status:** Usable
- **Purpose:** Aligns generated paginated output (`output.txt`) back to the original raw text file by performing fuzzy string matching, then inserts exact page break markers (`--- Page X ---`) into the raw text.
- **Inputs:** `output.txt` (containing paginated text) and `system-workspace/text-data/raw/raw_001.txt`.
- **Outputs:** A paginated version of the raw text saved as `system-workspace/text-data/raw/raw_001_paged.txt`.
- **Usage:** `python system-workspace/tools/new-tools/align.py`
- **Workflow Integration:** This tool directly enables the new 1-Plan-Per-Page workflow by injecting the `--- Page X ---` boundaries into raw text files, successfully slicing the text for the planner and page maker agents.
