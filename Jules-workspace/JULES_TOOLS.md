# Jules AI Tools Documentation

This document catalogs the tools specifically available to the Jules AI agent in the Jules-workspace folder.

## `Jules-workspace/batch_refactor.py`
- **Status:** Usable
```
batch_refactor.py — Batch refactor tool for HTML pages using regex.

Usage:
    python Jules-workspace/batch_refactor.py --pattern "regex" --replace "new_string" [--dry-run]
```

## `Jules-workspace/generate.py`
- **Status:** Usable
```
generate.py — Minimal HTML template generation script.

Usage:
    python Jules-workspace/generate.py
```

## `Jules-workspace/id_manager.py`
- **Status:** Usable
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
```
lint_autofixer.py — Auto-fixer for common HTML class violations.

Usage:
    python Jules-workspace/lint_autofixer.py
```

## `Jules-workspace/lint_pages.py`
- **Status:** Usable
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
```
lint_templates.py — Validation script for HTML template styles.

Usage:
    python Jules-workspace/lint_templates.py
```

## `Jules-workspace/verify_layout.py`
- **Status:** Usable
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
