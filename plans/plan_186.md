1. **Create HTML File:** Generate `pages/page_186_4q30t.html` with the required HTML structure, strictly using templates `TEMPLATE_C_HEADER`, `TEMPLATE_C_POET_BIO`, `TEMPLATE_C_BLOCK`, and `TEMPLATE_C_POEM`. Ensure `pb-0` is used instead of `pb-2mm` for the block body to avoid undefined class errors.
2. **Create Dummy Image:** Run `touch input/integrated-pictures/pic_186.jpg` to create the dummy image for the poet's bio.
3. **Auto-Tag IDs:** Run `python3 Jules-workspace/id_manager.py auto-tag` to generate unique IDs for the HTML blocks.
4. **Verify Layout:** Run `python3 Jules-workspace/verify_layout.py pages/page_186_4q30t.html --one-page-mode` to ensure the content fits on one page.
5. **Lint the File:** Run `cd pages && python3 ../Jules-workspace/lint_pages.py --one-page-mode page_186_4q30t.html` to ensure CSS class compliance and structure constraints.
6. **Verify Plan:** Run `python3 verify_plan.py plans/plan_186.md` to fulfill the Completeness Rule.
