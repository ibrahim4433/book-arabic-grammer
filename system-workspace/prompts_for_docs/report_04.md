### `./docs/Archive/C3/plus/C3/C3_Lessons_Text/old/make_c3.py`
- **Status:** Trash/Obsolete
- **Purpose:** Parses edited content, groups lessons into units according to a hardcoded mapping list (e.g., "U01_The_Word", "U02_Numbers_and_Pronouns"), and generates a markdown curriculum plan along with grouped text files.
- **Inputs:** `all_content_edited.txt`
- **Outputs:** `C3_Curriculum_Final_Plan.md`, and text files in `C3_Lessons_Text/` directory
- **Usage:** `python3 ./docs/Archive/C3/plus/C3/C3_Lessons_Text/old/make_c3.py`
- **Workflow Integration:** A legacy script specific to restructuring old C3 curriculum lessons into units. It conflicts with the new '1-Plan-Per-Page' workflow which bypasses logical lesson groups entirely and relies purely on `----- PAGE X -----` raw text pagination.
