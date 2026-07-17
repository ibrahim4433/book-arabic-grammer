#!/usr/bin/env python3
"""lint_pages.py — Arabic Grammar Book HTML Page Linter.

Enforces Atomic Design compliance, forbidden patterns, and CSS class whitelist.

Usage:
    python Jules-workspace/lint_pages.py                     # lint all pages/
    python Jules-workspace/lint_pages.py pages/01.0_intro.html
    python Jules-workspace/lint_pages.py pages/              # lint a directory
    python Jules-workspace/lint_pages.py --json              # machine-readable output
"""

from __future__ import annotations

import argparse
import contextlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup

# ── Configuration ─────────────────────────────────────────────────────────────

PAGES_DIR = Path("pages")
STYLES_FILE = Path("../styles/main.css")

#: Classes explicitly banned even if they appear in main.css
FORBIDDEN_CLASSES: frozenset[str] = frozenset(
    {"list-disc", "list-decimal", "list-reset", "list-none"}
)

#: CSS file extensions to skip when extracting class names
IGNORED_CSS_EXTENSIONS: frozenset[str] = frozenset(
    {"png", "jpg", "jpeg", "gif", "ttf", "woff", "woff2", "eot", "svg"}
)

# ANSI colour codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


# ── Data Models ───────────────────────────────────────────────────────────────

@dataclass
class LintIssue:
    level: str  # "ERROR" | "WARNING"
    message: str
    filepath: Path | None = None

    def __str__(self) -> str:
        loc = f"{self.filepath}: " if self.filepath else ""
        color = RED if self.level == "ERROR" else YELLOW
        return f"{color}[{self.level}]{RESET} {loc}{self.message}"


@dataclass
class LintResult:
    filepath: Path
    issues: list[LintIssue] = field(default_factory=list)

    @property
    def errors(self) -> list[LintIssue]:
        return [i for i in self.issues if i.level == "ERROR"]

    @property
    def warnings(self) -> list[LintIssue]:
        return [i for i in self.issues if i.level == "WARNING"]

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0

    def to_dict(self) -> dict:  # type: ignore[type-arg]
        return {
            "file": str(self.filepath),
            "passed": self.passed,
            "errors": [i.message for i in self.errors],
            "warnings": [i.message for i in self.warnings],
        }


# ── CSS Class Parsing ─────────────────────────────────────────────────────────

def parse_allowed_classes(css_file: Path) -> frozenset[str]:
    """Extract all class names defined in a CSS file."""
    if not css_file.exists():
        print(f"{RED}[ERROR] CSS file not found: {css_file}{RESET}")
        sys.exit(1)

    content = css_file.read_text(encoding="utf-8")
    candidates = re.findall(r"\.([a-zA-Z][a-zA-Z0-9_-]*)", content)
    return frozenset(c for c in candidates if c.lower() not in IGNORED_CSS_EXTENSIONS)


# ── Style Fix Suggestions ─────────────────────────────────────────────────────

def _suggest_fix(style_content: str) -> str:
    """Return a human-readable suggestion for replacing an inline style."""
    lower = style_content.lower()
    suggestions: list[str] = []

    if "color" in lower:
        suggestions.append("Use .text-primary, .text-accent, or .highlight-red/blue/green.")
    if "background" in lower:
        suggestions.append("Use .benefit-box.warning, .benefit-box.tip, or .bg-grey-lighter.")
    if "margin" in lower:
        suggestions.append("Use spacing utilities: .m-0, .mb-1mm, .mt-2mm, etc.")
    if "padding" in lower:
        suggestions.append("Use spacing utilities: .p-0, .p-1mm, .pl-0.")
    if "width" in lower:
        suggestions.append("Use width utilities: .w-20pct, .w-50pct, .w-full.")
    if "border-radius" in lower:
        suggestions.append("Use .rounded.")
    if "font" in lower:
        suggestions.append("Use typography utilities defined in main.css.")

    return " | ".join(suggestions) if suggestions else "Remove inline style and use a CSS class."


# ── Semantic Checks ───────────────────────────────────────────────────────────

def _check_exam_compliance(soup: BeautifulSoup, result: LintResult) -> None:
    """Enforce the Golden Standard for .exam-question blocks."""
    # Rule 1: Exam headers must use .bg-dark, not .accent
    for header in soup.find_all(class_="block-header"):
        text = header.get_text()
        if "اخْتَبِرْ نَفْسَكَ" in text or "Test Yourself" in text:
            classes: list[str] = header.get("class", [])
            if "bg-dark" not in classes:
                result.issues.append(LintIssue(
                    level="ERROR",
                    message=f"Exam header '{text.strip()[:40]}…' must have class .bg-dark. Found: {classes}",
                ))
            if "accent" in classes:
                result.issues.append(LintIssue(
                    level="ERROR",
                    message=f"Exam header '{text.strip()[:40]}…' must NOT have class .accent.",
                ))

    # Rule 2: Exam questions must have an answer box
    for question in soup.find_all(class_="exam-question"):
        if not question.find(class_="bg-grey-lighter"):
            q_id = question.get("id", "N/A")
            result.issues.append(LintIssue(
                level="ERROR",
                message=f"Exam question (id={q_id}) is missing an answer box (div.bg-grey-lighter).",
            ))


def _check_anti_bloat(soup: BeautifulSoup, result: LintResult) -> None:
    """Check for forbidden structural patterns."""
    # No nested benefit boxes
    for box in soup.find_all(class_="benefit-box"):
        if box.find(class_="benefit-box"):
            result.issues.append(LintIssue(
                level="ERROR",
                message="Nested .benefit-box found. Benefit boxes must NOT be nested.",
            ))


# ── Main Lint Function ────────────────────────────────────────────────────────

def lint_file(
    filepath: Path,
    allowed_classes: frozenset[str] | None = None,
) -> LintResult:
    """Lint a single HTML file and return a LintResult."""
    result = LintResult(filepath=filepath)

    # Auto-load allowed classes if not provided
    if allowed_classes is None and STYLES_FILE.exists():
        with contextlib.suppress(Exception):
            allowed_classes = parse_allowed_classes(STYLES_FILE)

    try:
        content = filepath.read_text(encoding="utf-8")
    except OSError as exc:
        result.issues.append(LintIssue(level="ERROR", message=f"Cannot read file: {exc}"))
        return result

    # ── Check 1: Inline Styles (STRICT BAN) ───────────────────────────────
    for match in re.finditer(r'style=["\']([^"\']*)["\']', content):
        style_content = match.group(1)
        suggestion = _suggest_fix(style_content)
        result.issues.append(LintIssue(
            level="ERROR",
            message=f"STRICT VIOLATION: Inline style '{style_content[:60]}'. Fix: {suggestion}",
        ))

    # ── Check 2: Class Whitelist & Forbidden Classes ───────────────────────
    used_classes: set[str] = set()
    for attr in re.findall(r'class=["\']([^"\']*)["\']', content):
        used_classes.update(attr.split())

    if allowed_classes:
        for cls in sorted(used_classes):
            if cls not in allowed_classes:
                result.issues.append(LintIssue(
                    level="ERROR",
                    message=f"Class '.{cls}' is NOT defined in styles/main.css.",
                ))

    for cls in sorted(used_classes & FORBIDDEN_CLASSES):
        result.issues.append(LintIssue(
            level="ERROR",
            message=f"Class '.{cls}' is FORBIDDEN. Use .structured-list instead.",
        ))

    # ── Check 3: Raw <ul> without .structured-list ─────────────────────────
    for match in re.finditer(r"<ul([^>]*)>", content):
        attrs = match.group(1)
        if "structured-list" not in attrs and "toc-list" not in attrs:
            result.issues.append(LintIssue(
                level="ERROR",
                message="Raw <ul> found without class 'structured-list'. Use .structured-list.",
            ))

    # ── Check 4: Forbidden <hr> tag ───────────────────────────────────────
    if re.search(r"<hr[^>]*>", content, re.IGNORECASE):
        result.issues.append(LintIssue(
            level="ERROR",
            message="STRICT VIOLATION: Forbidden <hr> tag found. Do not add horizontal rules.",
        ))

    # ── Check 5: BeautifulSoup semantic checks ────────────────────────────
    try:
        soup = BeautifulSoup(content, "html.parser")
        _check_exam_compliance(soup, result)
        _check_anti_bloat(soup, result)
    except Exception as exc:
        result.issues.append(LintIssue(
            level="WARNING",
            message=f"Could not run semantic checks (HTML parse error): {exc}",
        ))

    return result


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="lint_pages.py",
        description="Lint Arabic Grammar Book HTML pages for design compliance.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "target",
        nargs="?",
        type=Path,
        default=None,
        metavar="FILE_OR_DIR",
        help="File or directory to lint (default: pages/)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output results as JSON (machine-readable)",
    )
    return parser.parse_args()


def collect_targets(target: Path | None) -> list[Path]:
    """Resolve the target argument to a list of HTML files."""
    if target is None:
        if not PAGES_DIR.exists():
            print(f"{RED}Directory not found: {PAGES_DIR}{RESET}")
            sys.exit(1)
        return sorted(PAGES_DIR.glob("*.html"))
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.glob("*.html"))
    print(f"{RED}Target not found: {target}{RESET}")
    sys.exit(1)


def main() -> None:
    args = parse_args()
    target_files = collect_targets(args.target)

    print(f"🔍 Parsing {STYLES_FILE} for allowed classes...")
    allowed_classes = parse_allowed_classes(STYLES_FILE)
    print(f"   Found {len(allowed_classes)} allowed classes.\n")

    print(f"📄 Linting {len(target_files)} file(s)...\n")

    results: list[LintResult] = []
    total_errors = 0
    files_with_errors = 0

    for filepath in target_files:
        result = lint_file(filepath, allowed_classes)
        results.append(result)

        if not result.passed:
            files_with_errors += 1
            total_errors += len(result.errors)

            if not args.json_output:
                print(f"  {RED}✗{RESET} {filepath.name}")
                for issue in result.issues:
                    indent = "    "
                    print(f"{indent}{issue}")

    # ── Output ─────────────────────────────────────────────────────────────
    if args.json_output:
        print(json.dumps([r.to_dict() for r in results], indent=2, ensure_ascii=False))
    else:
        print()
        if total_errors > 0:
            print(
                f"{RED}❌ FAILED: {total_errors} error(s) across "
                f"{files_with_errors} file(s).{RESET}"
            )
            sys.exit(1)
        else:
            print(f"{GREEN}✅ SUCCESS: All {len(target_files)} file(s) passed. Zero violations.{RESET}")


if __name__ == "__main__":
    main()
