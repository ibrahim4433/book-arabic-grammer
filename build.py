import os
import glob
import re
from weasyprint import HTML

def main():
    # Ensure output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Find all HTML files in pages/ sorted alphabetically
    all_files = sorted(glob.glob('pages/*.html'))
    pages_files = [f for f in all_files if "TEMPLATE_" not in f]

    if not pages_files:
        print("No HTML files found in pages/.")
        return

    print(f"Found {len(pages_files)} pages: {pages_files}")

    # Check for cover images
    front_cover_path = "pages/cover/front-cover.jpg"
    back_cover_path = "pages/cover/back-cover.jpg"

    has_front_cover = os.path.exists(front_cover_path)
    has_back_cover = os.path.exists(back_cover_path)

    if has_front_cover:
        print(f"Found Front Cover: {front_cover_path}")
    if has_back_cover:
        print(f"Found Back Cover: {back_cover_path}")

    # Master HTML template
    # We include the stylesheet and the global fixed layers
    # We inject a specific style for the cover page to ensure zero margins
    master_html_start = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Book Compilation</title>
    <link rel="stylesheet" href="styles/main.css">
    <style>
        @page cover {
            margin: 0;
            size: A4;
        }
        .cover-page-wrapper {
            page: cover;
            width: 210mm;
            height: 297mm;
            overflow: hidden;
            break-after: page;
        }
        .cover-page-wrapper img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <!-- Global Fixed Background -->
    <div class="global-background-layer"></div>

    <!-- Global Fixed Watermark -->
    <div class="global-watermark-layer">
        <span class="watermark-text">أ. الياس خفيف</span>
    </div>

    <!-- Content Pages -->
"""

    master_html_end = """
</body>
</html>
"""

    accumulated_body_content = ""

    # Inject Front Cover
    if has_front_cover:
        accumulated_body_content += f"""
        <div class="cover-page-wrapper">
            <img src="{front_cover_path}" alt="Front Cover">
        </div>
        """

    # Loop through files and extract body content
    for page_file in pages_files:
        print(f"Processing {page_file}...")
        try:
            with open(page_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Robust Body Extraction
            body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
            if body_match:
                page_content = body_match.group(1)
            else:
                print(f"  -> Info: No <body> tag in {page_file}. Using full content as fragment.")
                page_content = content

            accumulated_body_content += page_content + "\n"

        except Exception as e:
            print(f"Error reading {page_file}: {e}")

    # Inject Back Cover
    if has_back_cover:
        # Note: We don't necessarily need break-after: page for the very last page,
        # but it doesn't hurt.
        accumulated_body_content += f"""
        <div class="cover-page-wrapper" style="break-after: auto;">
            <img src="{back_cover_path}" alt="Back Cover">
        </div>
        """

    # Combine everything
    full_html = master_html_start + accumulated_body_content + master_html_end

    # Render the final PDF
    print("Rendering final PDF...")
    # base_url='.' allows the CSS link to find styles/main.css relative to the current directory
    HTML(string=full_html, base_url='.').write_pdf(os.path.join(output_dir, 'book.pdf'))

    print(f"PDF successfully generated at {os.path.join(output_dir, 'book.pdf')}")

if __name__ == "__main__":
    main()
