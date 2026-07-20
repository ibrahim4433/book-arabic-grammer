### `./system-workspace/tools/new-tools/extract_footer.py`
- **Status:** Needs fixing (or partial Trash)
- **Purpose:** Intended to extract footers from the PDF, but contains broken logic (attempts to pass `output/export/book.pdf` to WeasyPrint `HTML()`, which only accepts HTML, failing immediately before falling back to rendering the whole book from HTML to count pages).
- **Inputs:** Attempts to read `output/export/book.pdf` and then `pages/*.html`.
- **Outputs:** Prints total physical pages in the final render (essentially duplicating `count_pages.py` or `rename_to_absolute.py` behavior but poorly).
- **Usage:** `python ./system-workspace/tools/new-tools/extract_footer.py`
- **Workflow Integration:** Obsolete or broken experiment from the old workflow trying to parse back the generated PDF. Not useful for the 1-Plan-Per-Page workflow as it currently errors out reading a PDF as HTML.
