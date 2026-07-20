### `./docs/Archive/C3/plus/C3/C3_Lessons_Text/old/split_chunks.py`
- **Status:** Trash/Obsolete
- **Purpose:** Reads extracted content, splits the text by a specific delimiter (`={50}\nFile: `), and groups the blocks into chunks of 12, saving them into separate text files.
- **Inputs:** `all_content.txt`, `block_titles.txt`
- **Outputs:** `raw_chunk_X.txt` (e.g., `raw_chunk_1.txt`)
- **Usage:** `python3 ./docs/Archive/C3/plus/C3/C3_Lessons_Text/old/split_chunks.py`
- **Workflow Integration:** This is an obsolete script from the old workflow used to manually chunk large extracted text files. It does not fit into the new '1-Plan-Per-Page' workflow which processes text based on exact `----- PAGE X -----` markers.
