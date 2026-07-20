### `./system-workspace/tools/new-tools/generate_toc.py`
- **Status:** Needs fixing
- **Purpose:** Reads `raw_001.txt` line-by-line, identifies sections containing "مدخل إلى النص", and scans the preceding lines to dynamically extract the lesson's main title.
- **Inputs:** `system-workspace/text-data/raw/raw_001.txt`
- **Outputs:** Creates a TOC mapping containing titles, levels, and authors.
- **Usage:** `python3 system-workspace/tools/new-tools/generate_toc.py`
- **Workflow Integration:** An early-stage raw parsing tool. It needs updates to recognize the `----- PAGE X -----` markers for compatibility with the new 1-Plan-Per-Page workflow.
