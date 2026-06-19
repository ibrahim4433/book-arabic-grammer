1. Use `write_file` to output the exact HTML code based on the provided plan into the target file `Jules-workspace/pages/30.0_nXX_الْمَنْصُوبَاتُ التَّمْيِيزُ.html`.
2. Run `Jules-workspace/lint_pages.py` to ensure there are no class validation errors and inline styles. If any errors occur, correct them using `replace_with_git_merge_diff`.
3. Use `run_in_bash_session` to run `Jules-workspace/id_manager.py auto-tag` to ensure all elements have correct IDs.
4. Run `Jules-workspace/verify_layout.py` to verify the layout constraints and density of the final page, it should fit perfectly within the A4 space.
5. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
6. Verify file using `read_file` to ensure `write_file` successfully applied the exact Tashkeel, colors and layout constraints.
7. Run tests to ensure no regressions were caused.
