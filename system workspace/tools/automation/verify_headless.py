#!/usr/bin/env python3
import os
import sys
import argparse
import json
from weasyprint import HTML
from pathlib import Path

# Constants matching build.py
PROJECT_ROOT = Path(__file__).parent.parent.parent
STYLES_DIR = PROJECT_ROOT / "styles"
OUTPUT_DIR = PROJECT_ROOT / "output/debug"

def verify_layout(file_path):
    """
    Renders an HTML file to PDF and checks if it fits on a single A4 page.
    Returns a dictionary with verification results.
    """
    input_path = Path(file_path)
    if not input_path.exists():
        return {"status": "ERROR", "message": "File not found"}

    # Ensure output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_filename = input_path.stem + ".pdf"
    output_path = OUTPUT_DIR / output_filename

    try:
        # Read content
        content = input_path.read_text(encoding='utf-8')

        # Extract body (simplistic regex, assumes standard structure)
        import re
        match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
        body_inner = match.group(1) if match else content

        # Inject into Master Template
        # Note: We must point base_url to PROJECT_ROOT so styles/main.css resolves
        master_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Verify: {input_path.name}</title>
    <link rel="stylesheet" href="styles/main.css">
</head>
<body>
    <div class="global-background-layer"></div>
    <div class="global-watermark-layer">
        <span class="watermark-text">أ. الياس خفيف</span>
    </div>
    {body_inner}
</body>
</html>
"""
        
        # Render
        doc = HTML(string=master_html, base_url=str(PROJECT_ROOT)).render()
        page_count = len(doc.pages)
        
        # Write PDF for manual inspection if needed
        doc.write_pdf(output_path)

        # Decision Logic
        if page_count == 1:
            return {
                "status": "PASS",
                "pages": 1,
                "path": str(output_path)
            }
        else:
            return {
                "status": "OVERFLOW",
                "pages": page_count,
                "path": str(output_path)
            }

    except Exception as e:
        return {"status": "ERROR", "message": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Headless Layout Verifier")
    parser.add_argument("file", help="Path to HTML file")
    args = parser.parse_args()

    result = verify_layout(args.file)
    print(json.dumps(result))
