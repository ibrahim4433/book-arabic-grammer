### `./system-workspace/tools/new-tools/fix_answers_ids.py`
- **Status:** Usable
- **Purpose:** Updates `98.00_p120_Answers.html` by assigning unique `id` attributes to each answer section's header based on the lesson number mapping from `lesson_mapping.json`.
- **Inputs:** `lesson_mapping.json`, `pages/98.00_p120_Answers.html`
- **Outputs:** Modifies `pages/98.00_p120_Answers.html`
- **Usage:** `python system-workspace/tools/new-tools/fix_answers_ids.py`
- **Workflow Integration:** This is a crucial step for the dynamic TOC generation, as it creates the anchor targets (`#ans-lesson-X`) that `rebuild_toc_final.py` uses for its `target-counter` links. It fits well into the workflow as a necessary linking step.
