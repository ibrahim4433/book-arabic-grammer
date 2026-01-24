import sys
import os
import logging
from weasyprint import HTML

# Mute WeasyPrint logging
logging.getLogger('weasyprint').setLevel(logging.ERROR)

def verify_layout(filepath):
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return

    # Extract body content (simple regex or fallback)
    import re
    match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
    if match:
        body_inner = match.group(1)
    else:
        body_inner = content

    # Master Template
    html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Verify</title>
    <link rel="stylesheet" href="styles/main.css">
</head>
<body>
    <div class="global-background-layer"></div>
    <div class="global-watermark-layer"><span class="watermark-text">Test</span></div>
    {body_inner}
</body>
</html>
"""

    # Render
    # base_url='.' assumes running from repo root
    doc = HTML(string=html_content, base_url='.').render()

    page_count = len(doc.pages)
    if page_count != 1:
        print(f"FAIL: Pages: {page_count}")
        return

    # Analyze Page 1
    page = doc.pages[0]

    # WeasyPrint pixels (96 DPI)
    # A4 Height = 297mm = 1122.52px
    # Margin Bottom = 10mm = 37.8px
    # Margin Top = 5mm = 18.9px

    px_to_mm = 25.4 / 96.0
    page_height_px = 297.0 / px_to_mm
    margin_bottom_px = 10.0 / px_to_mm
    margin_top_px = 5.0 / px_to_mm

    limit_y_px = page_height_px - margin_bottom_px
    usable_height_mm = 297 - 5 - 10 # 282mm

    max_y = 0
    lowest_elem = None

    for box in page._page_box.descendants():
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
            lowest_elem = box.element.tag if box.element is not None else "UnknownBox"

    max_y_mm = max_y * px_to_mm

    # Whitespace
    # (Page Height - Margin Bottom) - Lowest Element
    bottom_whitespace_mm = (297 - 10) - max_y_mm

    # Calculate % based on Usable Height (282mm)
    whitespace_pct = (bottom_whitespace_mm / usable_height_mm) * 100

    print(f"PASS: Pages: 1")
    print(f"Lowest Element Y: {max_y_mm:.1f}mm (Limit: {287}mm)")
    print(f"Whitespace: {whitespace_pct:.1f}%")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/verify_layout.py <filepath>")
    else:
        verify_layout(sys.argv[1])
