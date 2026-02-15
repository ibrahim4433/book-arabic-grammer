import sys
import os
import logging
import json
import re
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
        "blank_space_percentage": 0.0,
        "recommendation": "NONE",
        "details": "",
        "split_recommendation": None
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

    if page_count == 0:
         result["status"] = "FAIL"
         result["details"] = "No pages generated."
         print(json.dumps(result, indent=2))
         sys.exit(1)

    # WeasyPrint pixels (96 DPI)
    px_to_mm = 25.4 / 96.0

    # Layout Constants
    PAGE_HEIGHT_MM = 297.0
    # Printable limit based on 9mm bottom margin (CSS)
    printable_bottom_limit = PAGE_HEIGHT_MM - 9.0

    # Analyze Page 1
    page = doc.pages[0]
    max_y = 0
    last_element_info = None

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

                # Capture info about this element for split suggestions
                el_id = box.element.get('id', '')
                el_class = box.element.get('class', '')
                el_tag = box.element.tag

                last_element_info = {
                    "tag": el_tag,
                    "id": el_id,
                    "class": el_class,
                    "bottom_mm": round(bottom * px_to_mm, 2)
                }

    max_y_mm = max_y * px_to_mm

    # Remaining height relative to the bottom margin
    remaining_height_mm = printable_bottom_limit - max_y_mm

    result["remaining_height_mm"] = round(remaining_height_mm, 2)

    # Calculate Blank Space Percentage (Relative to full page height)
    blank_percentage = (remaining_height_mm / PAGE_HEIGHT_MM) * 100
    result["blank_space_percentage"] = round(blank_percentage, 1)

    # CHECK 1: One-Page Law (Overflow)
    if page_count > 1:
        result["status"] = "OVERFLOW"
        result["details"] = f"Page count is {page_count} (Expected: 1). Content spills over."
        result["recommendation"] = "SPLIT_PAGE_OR_CONDENSE"

        if last_element_info:
            result["split_recommendation"] = {
                "message": "The following element is the last one to fit on Page 1.",
                "element": last_element_info
            }

        print(json.dumps(result, indent=2))
        sys.exit(0) # Logic handled, return valid JSON

    # CHECK 2: Underflow
    # Threshold: 10% of full page height (297mm) = 29.7mm
    THRESHOLD_MM = PAGE_HEIGHT_MM * 0.10

    if remaining_height_mm >= THRESHOLD_MM:
        result["status"] = "UNDERFLOW"
        result["recommendation"] = "FIT_ANOTHER_SECTION"
        result["details"] = f"Page has {result['blank_space_percentage']}% ({remaining_height_mm:.1f}mm) empty space. Fill it."
    else:
        result["status"] = "PASS"
        result["recommendation"] = "GO_TO_NEXT_PAGE"
        result["details"] = f"Layout Valid. Blank space: {result['blank_space_percentage']}%."

    print(json.dumps(result, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/verify_layout.py <filepath>")
        sys.exit(1)
    else:
        verify_layout(sys.argv[1])
