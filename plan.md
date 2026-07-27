1. Write `pages/page_142_tbuuz.html` using a python script with heredoc to combine templates as per the planner's output. The python script will read the templates, replace `<section>` with `<div>`, fill placeholders, and output to `pages/page_142_tbuuz.html`.
2. Run `cd pages && python3 ../Jules-workspace/lint_pages.py page_142_tbuuz.html --one-page-mode` to check for compliance.
3. Run `python3 Jules-workspace/verify_layout.py pages/page_142_tbuuz.html` to verify layout constraints.
4. Run `python3 verify_plan.py plan.md` to ensure plan completeness.
5. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
6. Submit the final output.
