### `./system-workspace/tools/new-tools/parse_pdf.py`
- **Status:** Usable
- **Purpose:** Scans the final generated PDF (`book.pdf`) to locate and extract pages containing answer keys ("إجابات:") by dumping their raw text.
- **Inputs:** Reads `output/export/book.pdf`.
- **Outputs:** Writes a JSON dump file `pdf_text_dump.json` containing a list of page numbers and their corresponding raw text.
- **Usage:** `python ./system-workspace/tools/new-tools/parse_pdf.py`
- **Workflow Integration:** A utility script, likely used in a transition/verification phase to extract data from an existing monolithic PDF (old workflow) for debugging or migrating into the new 1-Plan-Per-Page structure.
