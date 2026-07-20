# Tools Documentation

This document is a catalog of every tool in the project, its exact purpose, expected inputs/outputs, usage examples, and how it integrates into the new 1-Plan-Per-Page workflow.

## `Jules-workspace/batch_refactor.py`
- **Status:** Usable
- **Workflow:** 1-Plan-Per-Page
```
batch_refactor.py — Batch refactor tool for HTML pages using regex.

Usage:
    python Jules-workspace/batch_refactor.py --pattern "regex" --replace "new_string" [--dry-run]
```

## `Jules-workspace/generate.py`
- **Status:** Usable
- **Workflow:** 1-Plan-Per-Page
```
generate.py — Minimal HTML template generation script.

Usage:
    python Jules-workspace/generate.py
```

## `Jules-workspace/id_manager.py`
- **Status:** Usable
- **Workflow:** 1-Plan-Per-Page
```
id_manager.py — Unique ID Manager for Arabic Grammar Book HTML pages.

Manages the bXXXXX ID system used on every significant content block.

Commands:
    auto-tag   Automatically add IDs to elements that are missing them.
    verify     Check for duplicate IDs across all pages.
    next-id    Print a single new unique ID (useful for manual editing).

Usage:
    python Jules-workspace/id_manager.py auto-tag
    python Jules-workspace/id_manager.py auto-tag --dry-run
    python Jules-workspace/id_manager.py auto-tag --files pages/01.0_intro.html
    python Jules-workspace/id_manager.py verify
    python Jules-workspace/id_manager.py next-id
```

## `Jules-workspace/lint_autofixer.py`
- **Status:** Usable
- **Workflow:** 1-Plan-Per-Page
```
lint_autofixer.py — Auto-fixer for common HTML class violations.

Usage:
    python Jules-workspace/lint_autofixer.py
```

## `Jules-workspace/lint_pages.py`
- **Status:** Usable
- **Workflow:** 1-Plan-Per-Page
```
lint_pages.py — Arabic Grammar Book HTML Page Linter.

Enforces Atomic Design compliance, forbidden patterns, and CSS class whitelist.

Usage:
    python Jules-workspace/lint_pages.py                     # lint all pages/
    python Jules-workspace/lint_pages.py pages/01.0_intro.html
    python Jules-workspace/lint_pages.py pages/              # lint a directory
    python Jules-workspace/lint_pages.py --json              # machine-readable output
```

## `Jules-workspace/lint_templates.py`
- **Status:** Usable
- **Workflow:** 1-Plan-Per-Page
```
lint_templates.py — Validation script for HTML template styles.

Usage:
    python Jules-workspace/lint_templates.py
```

## `Jules-workspace/verify_layout.py`
- **Status:** Usable
- **Workflow:** 1-Plan-Per-Page
```
verify_layout.py — One-Page Law Verifier for Arabic Grammar Book.

Checks that an HTML page renders to exactly one A4 page and is not
significantly underfilled. Integrates with the linter for full compliance.

Exit codes:
    0  — Layout check ran successfully (inspect JSON for PASS/FAIL status).
    1  — Critical failure (file not found, render error, linter errors).

Usage:
    python Jules-workspace/verify_layout.py pages/01.0_intro.html
    python Jules-workspace/verify_layout.py pages/01.0_intro.html --skip-lint
```

## `build.py`
- **Status:** Usable
- **Workflow:** General
```
build.py — Arabic Grammar Book PDF Builder.

Compiles all pages in /pages/ into a single A4 PDF using WeasyPrint.

Usage:
    python build.py
    python build.py --output output/export/my_book.pdf
    python build.py --pages-dir pages/ --dry-run
```

## `doc_generator_md.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `network_ai_ocr/colab_surya_ocr.py`
- **Status:** Error/Trash
- **Workflow:** General
```
Error parsing: invalid syntax (<unknown>, line 6)
```

## `network_ai_ocr/server.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `preview-theme.py`
- **Status:** Usable
- **Workflow:** General
```
preview-theme.py — Arabic Grammar Book Theme Preview Generator.

Compiles all pages into a single A4 PDF using a specified theme from new-style-options.

Usage:
    python preview-theme.py --theme v1
    python preview-theme.py --all
```

## `scripts/build-with-id.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `scripts/preview.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/check_headings.py`
- **Status:** Usable
- **Workflow:** General
```
check_headings.py — Cross-references titles from TOC.json against full_raw_indexed.txt.

Usage:
    python system-workspace/check_headings.py
```

## `system-workspace/check_titles.py`
- **Status:** Usable
- **Workflow:** General
```
check_titles.py — Searches and normalizes titles found in TOC.json within full_raw_indexed.txt.

Usage:
    python system-workspace/check_titles.py
```

## `system-workspace/generate_index.py`
- **Status:** Usable
- **Workflow:** General
```
generate_index.py — Generates an index map with raw file markers and titles from full_raw_indexed.txt.

Usage:
    python system-workspace/generate_index.py
```

## `system-workspace/tools/automation/all_pics_to_text.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/auto_book_maker.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/create_lesson_index.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/dispatch_jules.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/fix_extractor.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/lesson_compiler.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/lesson_maker.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/__init__.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/auditor.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/compiler.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/full_auto_workflow.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/gemini_client.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/github_utils.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/jules_client.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/jules_client_ocr.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/jules_client_plans.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/jules_ocr.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/jules_page_generator.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/jules_planner.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/jules_youtube_dispatcher.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/pattern_extractor.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/pdf_ocr_local.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/pdf_ocr_network.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/planner.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/state_manager.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/text_processing.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/unified_flow.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/vision.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/youtube_offline_transcriber.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/youtube_transcriber.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/modules/youtube_ui.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/orchestrator.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/pattern_extractor.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/plan_refiner.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/project_state.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/verify_headless.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/workflow_manager.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/automation/workflow_state.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/extra/verify_changes.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/extra/verify_lesson_28.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/extra/verify_pages.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/align.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/align_clean.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/align_dp.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/api.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/clean_raw_book.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/clean_toc.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/clean_toc_duplicates.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/count_pages.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/debug_ocr.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/extract_footer.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fill_missing.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fill_missing_bs4.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_6_answers.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_answers_ids.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_book.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_content.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_content_2.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_filenames.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_logical_pages.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_metadata.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_names.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_none_title.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_other.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_parts.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_toc.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_toc_answers.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/fix_toc_styles.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/full_cleanup.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/generate_toc.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/generate_toc_from_physical.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/grid_search_ocr.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/index_and_toc.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/make_index.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/merge_all_prs.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/merge_answers.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/build_pages.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_14_helper.py`
- **Status:** Usable
- **Workflow:** General
```
Helper script to generate the HTML for Lesson 14 using JulesPageGenerator.
This fulfills the requirement to create a generation script.
```

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_25.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_11.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_12.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_13.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_16.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_19.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_26.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_27.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_28.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_lesson_30.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_page.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_page_18.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_plan.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/generate_session_29.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/test_gemini_yt.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/test_offline_youtube.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/test_plan.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/new-beta-page-maker/test_pytubefix.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/parse_layout.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/parse_layout_ids.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/parse_pdf.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/rebuild_toc.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/rebuild_toc_final.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/rebuild_toc_paginated.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/recover_answers.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/regenerate_answers.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/rename_final.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/rename_to_absolute.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/rename_to_footer.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/rename_to_physical.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/renumber_lessons.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/restore_and_fix.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/sync_exact_pages.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/sync_pages.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/system.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/test.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/test_get.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/test_intro.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/test_next.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/test_sys.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/test_weasy.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/update_all_css_bg.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/update_answers.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/update_answers_and_toc.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/update_pages.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/new-tools/use_6_col_table.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_auditor.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_compiler.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_gemini_client_headless.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_jules_connectivity.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_jules_ocr_integration.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_planner.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_text_processor.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_vision.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `system-workspace/tools/tests/test_youtube_transcriber.py`
- **Status:** Needs fixing/documentation
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `tests/test_batch_refactor.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.

## `tests/test_lint_pages.py`
- **Status:** Needs Review/Trash
- **Workflow:** General
> No docstring provided. This tool needs documentation.
