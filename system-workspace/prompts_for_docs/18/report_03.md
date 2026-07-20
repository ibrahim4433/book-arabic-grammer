### `./system-workspace/tools/new-tools/align_dp.py`
- **Status:** Usable
- **Purpose:** Uses dynamic programming to align lines from a generated output file with original raw text based on trigram similarity, inserting page markers (`--- Page X ---`) into the raw text where they align.
- **Inputs:** `output.txt` and raw text files.
- **Outputs:** Modifies raw text files to include page markers.
- **Usage:** `python3 ./system-workspace/tools/new-tools/align_dp.py`
- **Workflow Integration:** A preparation tool used to paginate raw text. Since the 1-Plan-Per-Page workflow requires pre-paginated exact text slices, this tool helped generate the required inputs for that workflow.
