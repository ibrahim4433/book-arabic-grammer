import sys
import os
import logging
import json
from weasyprint import HTML

# Add current directory to path to allow importing lint_pages
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import lint_pages
except ImportError:
    lint_pages = None

# Mute WeasyPrint logging
logging.getLogger('weasyprint').setLevel(logging.ERROR)

def verify_layout(filepath):
    result = {
        "status": "UNKNOWN",
        "remaining_height_mm": 0.0,
        "recommendation": "NONE",
        "details": ""
    }

    if not os.path.exists(filepath):
        result["status"] = "FAIL"
        result["details"] = f"File not found: {filepath}"
        print(json.dumps(result, indent=2))
        sys.exit(1)

    # CHECK 0: Linter (Atomic Design Compliance)
    if lint_pages:
        l_errors, l_warnings = lint_pages.lint_file(filepath)
        if l_errors:
            result["status"] = "FAIL"
            result["details"] = "Linter Errors: " + "; ".join(l_errors)
            print(json.dumps(result, indent=2))
            sys.exit(1)

        # Warnings don't fail the layout check, but could be noted
        if l_warnings:
             result["details"] = "Linter Warnings: " + "; ".join(l_warnings)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        result["status"] = "FAIL"
        result["details"] = f"Error reading file: {e}"
        print(json.dumps(result, indent=2))
        sys.exit(1)

    # Extract body content (robust)
    import re
    match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    if match:
        body_inner = match.group(1)
    else:
        body_inner = content

    # Master Template for verification
    html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Verify</title>
    <link rel="stylesheet" href="styles/main.css">
    <style>
        /* Remove footer for verification to avoid measuring it */
        @page {{ @bottom-center {{ content: none; }} }}
    </style>
</head>
<body>
    <!-- Fixed layers removed for layout verification to avoid interference -->
    {body_inner}
</body>
</html>
"""

    # Render
    try:
        doc = HTML(string=html_content, base_url='.').render()
    except Exception as e:
        result["status"] = "FAIL"
        result["details"] = f"Rendering error: {e}"
        print(json.dumps(result, indent=2))
        sys.exit(1)

    page_count = len(doc.pages)

    # CHECK 1: One-Page Law
    if page_count > 1:
        result["status"] = "OVERFLOW"
        result["details"] = f"Page count is {page_count} (Expected: 1)"
        result["recommendation"] = "SPLIT_PAGE_OR_CONDENSE"
        print(json.dumps(result, indent=2))
        sys.exit(1) # Or 0 depending on pipeline needs, but typically overflow is a failure to meet constraints

    # Analyze Page 1 for Density/Underflow
    page = doc.pages[0]

    # WeasyPrint pixels (96 DPI)
    px_to_mm = 25.4 / 96.0

    # Layout Constants
    PAGE_HEIGHT_MM = 297.0
    MARGIN_TOP_MM = 5.0
    MARGIN_BOTTOM_MM = 10.0 # From CSS @page margin-bottom: 9mm, but let's be safe/consistent with previous
    # Actually, CSS says margin-bottom: 9mm. Let's use 9mm + buffer or stick to Printable Area.
    # Previous code used 10.0. Let's check CSS again.
    # CSS: margin: 5mm 5mm 9mm 5mm;

    printable_bottom_limit = PAGE_HEIGHT_MM - 9.0 # 288mm

    max_y = 0

    # Iterate through all boxes on the page to find the lowest point
    for box in page._page_box.descendants():
        if type(box).__name__ in ['MarginBox', 'PageBox']:
            continue

        if box.element is not None:
            classes = box.element.get('class', '').split() if box.element.get('class') else []
            # Skip fixed layers
            if 'global-background-layer' in classes: continue
            if 'global-watermark-layer' in classes: continue
            if 'watermark-text' in classes: continue
            # Skip root containers
            if box.element.tag in ['html', 'body']: continue

        # Check geometry (border box)
        # box.position_y is from top of page
        bottom = box.position_y + box.height

        if bottom > max_y:
            max_y = bottom

    max_y_mm = max_y * px_to_mm

    # Remaining height relative to the bottom margin
    remaining_height_mm = printable_bottom_limit - max_y_mm

    result["remaining_height_mm"] = round(remaining_height_mm, 2)

    # CHECK 2: Underflow
    if remaining_height_mm > 30.0:
        result["status"] = "UNDERFLOW"
        result["recommendation"] = "FETCH_NEXT_SECTION"
        result["details"] = f"Page has {remaining_height_mm:.1f}mm empty space at bottom."
    else:
        result["status"] = "PASS"
        result["recommendation"] = "NONE"
        result["details"] = "Layout Valid"

    print(json.dumps(result, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # result["status"] = "FAIL"
        # result["details"] = "Usage: python tools/verify_layout.py <filepath>"
        # print(json.dumps(result, indent=2))
        print("Usage: python tools/verify_layout.py <filepath>")
        sys.exit(1)
    else:
        verify_layout(sys.argv[1])
