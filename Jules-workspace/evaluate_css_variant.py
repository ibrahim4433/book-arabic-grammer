#!/usr/bin/env python3
"""evaluate_css_variant.py — Oracle for AI CSS Tuning.

Evaluates an HTML page against a specific CSS file and outputs strict JSON.
"""

import argparse
import json
import logging
import re
import sys
from pathlib import Path

# Mute WeasyPrint's verbose logging
logging.getLogger("weasyprint").setLevel(logging.ERROR)
logging.getLogger("fonttools").setLevel(logging.ERROR)

# Constants
PX_TO_MM = 25.4 / 96.0
PAGE_HEIGHT_MM = 297.0
PRINTABLE_BOTTOM_MM = PAGE_HEIGHT_MM - 9.0
UNDERFLOW_THRESHOLD_PCT = 10.0
SKIP_CLASSES = {"global-background-layer", "global-watermark-layer", "watermark-text", "force-new-page"}
SKIP_TAGS = {"html", "body"}
SKIP_BOX_TYPES = {"MarginBox", "PageBox"}

def _extract_body(content: str) -> str:
    match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else content

def _build_verification_html(body_inner: str, stylesheet: Path) -> str:
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{stylesheet.absolute().as_posix()}">
    <style>
        @page {{ @bottom-center {{ content: none; }} }}
    </style>
</head>
<body>
    {body_inner}
</body>
</html>
"""

def _find_content_bottom(page):
    max_y = 0.0
    page_box = getattr(page, "_page_box", None)
    if page_box is None: return max_y

    for box in page_box.descendants():
        if type(box).__name__ in SKIP_BOX_TYPES: continue
        element = getattr(box, "element", None)
        if element is None: continue

        el_classes = element.get("class", "").split() if element.get("class") else []
        if any(c in SKIP_CLASSES for c in el_classes): continue
        if element.tag in SKIP_TAGS: continue

        bottom = getattr(box, "position_y", 0) + getattr(box, "height", 0)
        if bottom > max_y: max_y = bottom

    return max_y

def evaluate(html_path: Path, css_path: Path) -> dict:
    if not html_path.exists():
        return {"status": "ERROR", "message": f"HTML file not found: {html_path}"}
    if not css_path.exists():
        return {"status": "ERROR", "message": f"CSS file not found: {css_path}"}

    try:
        from weasyprint import HTML
    except ImportError:
        return {"status": "ERROR", "message": "WeasyPrint not installed."}

    content = html_path.read_text(encoding="utf-8")
    body_inner = _extract_body(content)
    html_content = _build_verification_html(body_inner, css_path)

    try:
        doc = HTML(string=html_content, base_url=str(html_path.parent)).render()
    except Exception as exc:
        return {"status": "ERROR", "message": f"Rendering error: {exc}"}

    page_count = len(doc.pages)
    if page_count == 0:
        return {"status": "ERROR", "message": "No pages generated."}

    max_y_px = _find_content_bottom(doc.pages[0])
    max_y_mm = max_y_px * PX_TO_MM
    remaining_mm = PRINTABLE_BOTTOM_MM - max_y_mm
    blank_pct = (remaining_mm / PAGE_HEIGHT_MM) * 100.0

    result = {
        "page_count": page_count,
        "remaining_mm": round(remaining_mm, 2),
        "blank_pct": round(blank_pct, 1)
    }

    if page_count > 1:
        result["status"] = "OVERFLOW"
    elif blank_pct >= UNDERFLOW_THRESHOLD_PCT:
        result["status"] = "UNDERFLOW"
    else:
        result["status"] = "PASS"

    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("html_path", type=Path)
    parser.add_argument("css_path", type=Path)
    args = parser.parse_args()

    res = evaluate(args.html_path, args.css_path)
    print(json.dumps(res))

if __name__ == "__main__":
    main()
