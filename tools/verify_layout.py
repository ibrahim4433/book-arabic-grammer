import sys
import os
import logging
from weasyprint import HTML

# Add current directory to path to allow importing lint_pages
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import lint_pages
except ImportError:
    lint_pages = None

# Mute WeasyPrint logging
logging.getLogger('weasyprint').setLevel(logging.ERROR)

# ANSI Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def verify_layout(filepath):
    if not os.path.exists(filepath):
        print(f"{RED}[FAIL] File not found: {filepath}{RESET}")
        sys.exit(1)

    # CHECK 0: Linter (Atomic Design Compliance)
    if lint_pages:
        l_errors, l_warnings = lint_pages.lint_file(filepath)
        if l_errors:
            print(f"{RED}[FAIL] Lint Errors found (Atomic Design Violation):{RESET}")
            for err in l_errors:
                print(f"  - {err}")
            # We fail immediately on structure violations
            sys.exit(1)

        if l_warnings:
            print(f"{YELLOW}[WARN] Lint Warnings:{RESET}")
            for warn in l_warnings:
                print(f"  - {warn}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"{RED}[FAIL] Error reading file: {e}{RESET}")
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
        print(f"{RED}[FAIL] Rendering error: {e}{RESET}")
        sys.exit(1)

    page_count = len(doc.pages)

    # CHECK 1: One-Page Law
    if page_count > 1:
        print(f"{RED}[FAIL] Page count is {page_count} (Expected: 1){RESET}")
        sys.exit(1)

    # Analyze Page 1 for Density/Underflow
    page = doc.pages[0]

    # WeasyPrint pixels (96 DPI)
    px_to_mm = 25.4 / 96.0

    # Layout Constants
    PAGE_HEIGHT_MM = 297.0
    MARGIN_TOP_MM = 5.0
    MARGIN_BOTTOM_MM = 10.0
    USABLE_HEIGHT_MM = PAGE_HEIGHT_MM - MARGIN_TOP_MM - MARGIN_BOTTOM_MM # 282mm

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

    # Calculate Used Height vs Usable Height
    # Note: max_y_mm is from the top of the page (0).
    # Content starts roughly at MARGIN_TOP_MM.
    # But we care about where it ENDS relative to the bottom margin.

    # The lowest element ended at max_y_mm.
    # The printable area ends at (PAGE_HEIGHT_MM - MARGIN_BOTTOM_MM) = 287mm.

    printable_bottom_limit = PAGE_HEIGHT_MM - MARGIN_BOTTOM_MM

    # Empty space at the bottom of the printable area
    # If content ends at 100mm, and limit is 287mm, empty space is 187mm.
    empty_space_mm = printable_bottom_limit - max_y_mm

    # Percentage of USABLE area that is empty
    empty_pct = (empty_space_mm / USABLE_HEIGHT_MM) * 100

    print(f"Lowest Element Y: {max_y_mm:.1f}mm")
    print(f"Empty Space: {empty_pct:.1f}%")

    # CHECK 2: Underflow Warning
    if empty_pct > 20.0:
        print(f"{YELLOW}[WARN] Page is {empty_pct:.1f}% empty (> 20% allowed){RESET}")
        sys.exit(0) # Exit 0 as it's just a warning

    # PASS
    print(f"{GREEN}[PASS] Layout Valid{RESET}")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/verify_layout.py <filepath>")
        sys.exit(1)
    else:
        verify_layout(sys.argv[1])
