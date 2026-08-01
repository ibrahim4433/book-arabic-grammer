#!/usr/bin/env python3
"""verify_layout.py — One-Page Law Verifier for Arabic Grammar Book.

Checks that an HTML page renders to exactly one A4 page and is not
significantly underfilled. Integrates with the linter for full compliance.

Exit codes:
    0  — Layout check ran successfully (inspect JSON for PASS/FAIL status).
    1  — Critical failure (file not found, render error, linter errors).

Usage:
    python Jules-workspace/verify_layout.py pages/01.0_intro.html
    python Jules-workspace/verify_layout.py pages/01.0_intro.html --skip-lint
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Literal

# Mute WeasyPrint's verbose logging
logging.getLogger("weasyprint").setLevel(logging.ERROR)
logging.getLogger("fonttools").setLevel(logging.ERROR)

# Add Jules-workspace to path so lint_pages can be imported
sys.path.insert(0, str(Path(__file__).parent))

try:
    import lint_pages

    _LINT_AVAILABLE = True
except ImportError:
    _LINT_AVAILABLE = False


# ── Constants ─────────────────────────────────────────────────────────────────

#: WeasyPrint renders at 96 DPI
PX_TO_MM: float = 25.4 / 96.0

#: A4 page height
PAGE_HEIGHT_MM: float = 297.0

#: Bottom margin in CSS is 9 mm
PRINTABLE_BOTTOM_MM: float = PAGE_HEIGHT_MM - 9.0

#: If blank space exceeds this % of page height, it's UNDERFLOW
UNDERFLOW_THRESHOLD_PCT: float = 10.0

#: CSS classes to skip during geometry analysis (non-content layers)
SKIP_CLASSES: frozenset[str] = frozenset(
    {"global-background-layer", "global-watermark-layer", "watermark-text", "force-new-page"}
)

#: HTML tags to skip
SKIP_TAGS: frozenset[str] = frozenset({"html", "body"})

#: WeasyPrint box types to skip
SKIP_BOX_TYPES: frozenset[str] = frozenset({"MarginBox", "PageBox"})


# ── Data Models ───────────────────────────────────────────────────────────────

LayoutStatus = Literal["PASS", "FAIL", "OVERFLOW", "UNDERFLOW", "UNKNOWN"]
LayoutRecommendation = Literal[
    "NONE", "GO_TO_NEXT_PAGE", "SPLIT_PAGE_OR_CONDENSE", "CONDENSE_OR_USE_ESCAPE_HATCH", "FIT_ANOTHER_SECTION"
]


@dataclass
class ElementInfo:
    tag: str
    id: str
    css_class: str
    bottom_mm: float
    height_mm: float = 0.0


@dataclass
class LayoutResult:
    status: LayoutStatus = "UNKNOWN"
    remaining_height_mm: float = 0.0
    blank_space_percentage: float = 0.0
    recommendation: LayoutRecommendation = "NONE"
    details: str = ""
    split_recommendation: ElementInfo | None = None
    overflow_elements: list[ElementInfo] = field(default_factory=list)

    def to_dict(self) -> dict:  # type: ignore[type-arg]
        d = asdict(self)
        # Convert ElementInfo to plain dict (asdict handles nested dataclasses)
        return d

    def print(self) -> None:
        print(json.dumps(self.to_dict(), indent=2, ensure_ascii=False))


# ── HTML Utilities ────────────────────────────────────────────────────────────


def _extract_body(content: str) -> str:
    match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else content


def _build_verification_html(body_inner: str, stylesheet: Path = Path("styles/main.css")) -> str:
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Verify</title>
    <link rel="stylesheet" href="{stylesheet.as_posix()}">
    <style>
        /* Remove footer during verification to avoid measuring it */
        @page {{ @bottom-center {{ content: none; }} }}
    </style>
</head>
<body>
    {body_inner}
</body>
</html>
"""


# ── Geometry Analysis ─────────────────────────────────────────────────────────


def _find_content_bottom(page: object) -> tuple[float, ElementInfo | None]:  # type: ignore[type-arg]
    """Walk all boxes on the page to find the lowest content boundary."""
    max_y: float = 0.0
    last_element: ElementInfo | None = None

    page_box = getattr(page, "_page_box", None)
    if page_box is None:
        return max_y, last_element

    for box in page_box.descendants():
        if type(box).__name__ in SKIP_BOX_TYPES:
            continue

        element = getattr(box, "element", None)
        if element is None:
            continue

        # Skip non-content layers and root containers
        el_classes: list[str] = element.get("class", "").split() if element.get("class") else []
        if any(c in SKIP_CLASSES for c in el_classes):
            continue
        if element.tag in SKIP_TAGS:
            continue

        bottom: float = getattr(box, "position_y", 0) + getattr(box, "height", 0)
        if bottom > max_y:
            max_y = bottom
            last_element = ElementInfo(
                tag=element.tag,
                id=element.get("id", ""),
                css_class=element.get("class", ""),
                bottom_mm=round(bottom * PX_TO_MM, 2),
                height_mm=round(getattr(box, "height", 0) * PX_TO_MM, 2),
            )

    return max_y, last_element

def _get_elements_on_page(page: object) -> list[ElementInfo]:  # type: ignore[type-arg]
    """Extract all distinct elements (and their heights) that appear on this page."""
    elements: list[ElementInfo] = []
    seen_ids: set[str] = set()
    
    page_box = getattr(page, "_page_box", None)
    if page_box is None:
        return elements

    for box in page_box.descendants():
        if type(box).__name__ in SKIP_BOX_TYPES:
            continue

        element = getattr(box, "element", None)
        if element is None:
            continue

        el_classes: list[str] = element.get("class", "").split() if element.get("class") else []
        if any(c in SKIP_CLASSES for c in el_classes):
            continue
        if element.tag in SKIP_TAGS:
            continue
            
        el_id = element.get("id", "")
        if not el_id or el_id in seen_ids:
            continue
            
        bottom: float = getattr(box, "position_y", 0) + getattr(box, "height", 0)
        elements.append(ElementInfo(
            tag=element.tag,
            id=el_id,
            css_class=element.get("class", ""),
            bottom_mm=round(bottom * PX_TO_MM, 2),
            height_mm=round(getattr(box, "height", 0) * PX_TO_MM, 2),
        ))
        seen_ids.add(el_id)
        
    return elements


# ── Core Verifier ─────────────────────────────────────────────────────────────


def verify_layout(filepath: Path, *, skip_lint: bool = False, one_page_mode: bool = False) -> LayoutResult:
    """Verify that a page renders to exactly one A4 page."""
    result = LayoutResult()

    if not filepath.exists():
        result.status = "FAIL"
        result.details = f"File not found: {filepath}"
        return result

    # ── Linter Check ──────────────────────────────────────────────────────
    if not skip_lint and _LINT_AVAILABLE:
        lint_result = lint_pages.lint_file(filepath)
        # Support both old tuple API and new LintResult API
        if isinstance(lint_result, tuple):
            l_errors, l_warnings = lint_result
            if l_errors:
                result.status = "FAIL"
                result.details = "Linter errors: " + "; ".join(l_errors[:5])
                return result
            if l_warnings:
                result.details = "Linter warnings: " + "; ".join(l_warnings[:3])
        else:
            # New LintResult dataclass
            if not lint_result.passed:
                result.status = "FAIL"
                result.details = "Linter errors: " + "; ".join(
                    i.message for i in lint_result.errors[:5]
                )
                return result

    # ── Read file ──────────────────────────────────────────────────────────
    try:
        content = filepath.read_text(encoding="utf-8")
    except OSError as exc:
        result.status = "FAIL"
        result.details = f"Error reading file: {exc}"
        return result

    # ── Render ────────────────────────────────────────────────────────────
    try:
        from weasyprint import HTML
    except (ImportError, OSError) as exc:
        result.status = "FAIL"
        result.details = f"WeasyPrint unavailable: {exc}"
        return result

    body_inner = _extract_body(content)
    html_content = _build_verification_html(body_inner)

    try:
        doc = HTML(string=html_content, base_url=".").render()
    except Exception as exc:
        result.status = "FAIL"
        result.details = f"Rendering error: {exc}"
        return result

    page_count = len(doc.pages)
    if page_count == 0:
        result.status = "FAIL"
        result.details = "No pages generated."
        return result

    # ── Geometry Analysis ─────────────────────────────────────────────────
    max_y_px, last_element = _find_content_bottom(doc.pages[0])
    max_y_mm = max_y_px * PX_TO_MM
    remaining_mm = PRINTABLE_BOTTOM_MM - max_y_mm
    blank_pct = (remaining_mm / PAGE_HEIGHT_MM) * 100.0

    result.remaining_height_mm = round(remaining_mm, 2)
    result.blank_space_percentage = round(blank_pct, 1)

    # ── Rule 1: Overflow ──────────────────────────────────────────────────
    if page_count > 1:
        overflow_elements = _get_elements_on_page(doc.pages[1])
        overflow_ids = [el.id for el in overflow_elements if el.id]
        total_overflow_mm = sum(e.height_mm for e in overflow_elements)
        
        result.status = "OVERFLOW"
        result.overflow_elements = overflow_elements
        
        if one_page_mode:
            result.details = (
                f"Page count is {page_count} (expected 1). Content overflows by approx {total_overflow_mm:.1f}mm. "
                f"Overflowing elements: {overflow_ids}. "
                "Condense previous elements using zero-margins, convert to dense templates, or use Escape Hatch."
            )
            result.recommendation = "CONDENSE_OR_USE_ESCAPE_HATCH"
        else:
            result.details = (
                f"Page count is {page_count} (expected 1). Content overflows by approx {total_overflow_mm:.1f}mm. "
                f"Overflowing elements: {overflow_ids}. "
                "Split into multiple files or condense content."
            )
            result.recommendation = "SPLIT_PAGE_OR_CONDENSE"
            
        result.split_recommendation = last_element
        return result

    # ── Rule 2: Underflow ─────────────────────────────────────────────────
    if blank_pct >= UNDERFLOW_THRESHOLD_PCT:
        result.status = "UNDERFLOW"
        result.recommendation = "FIT_ANOTHER_SECTION"
        result.details = (
            f"Page is {blank_pct:.1f}% empty ({remaining_mm:.1f} mm blank). "
            "Add more content or pull from adjacent pages."
        )
    else:
        result.status = "PASS"
        result.recommendation = "GO_TO_NEXT_PAGE"
        result.details = f"Layout valid. Blank space: {blank_pct:.1f}%."

    return result


# ── CLI ───────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="verify_layout.py",
        description="Verify the One-Page Law for an HTML page.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "filepath",
        type=Path,
        metavar="FILE",
        help="HTML page file to verify",
    )
    parser.add_argument(
        "--skip-lint",
        action="store_true",
        help="Skip the linter compliance check before layout verification",
    )
    parser.add_argument(
        "--one-page-mode",
        action="store_true",
        help="Enforce strict 1-Page constraints (forbids splitting)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = verify_layout(args.filepath, skip_lint=args.skip_lint, one_page_mode=args.one_page_mode)
    result.print()

    # Exit 1 only on hard failures (file not found, render error)
    if result.status == "FAIL":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
