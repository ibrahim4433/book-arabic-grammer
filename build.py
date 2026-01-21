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

    # Master HTML template
    # We include the stylesheet and the global fixed layers
    master_html_start = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Book Compilation</title>
    <link rel="stylesheet" href="styles/main.css">
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

    # Loop through files and extract body content
    for page_file in pages_files:
        print(f"Processing {page_file}...")
        try:
            with open(page_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract content between <body> and </body>
            # Using regex to capture everything inside body tags
            match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
            if match:
                body_inner_html = match.group(1)
                # Append to master content
                # We wrap each file's content in a div or just append.
                # Since the files seem to be complete sections/pages, appending is fine.
                # However, to avoid ID conflicts or just to separate, we could wrap them.
                # But looking at 00_cover.html, it has <section class="cover-page">.
                # So we just append the inner HTML.
                accumulated_body_content += body_inner_html + "\n"
            else:
                print(f"Warning: No <body> tag found in {page_file}")

        except Exception as e:
            print(f"Error reading {page_file}: {e}")

    # Combine everything
    full_html = master_html_start + accumulated_body_content + master_html_end

    # Render the final PDF
    print("Rendering final PDF...")
    # base_url='.' allows the CSS link to find styles/main.css relative to the current directory
    HTML(string=full_html, base_url='.').write_pdf(os.path.join(output_dir, 'book.pdf'))

    print(f"PDF successfully generated at {os.path.join(output_dir, 'book.pdf')}")

if __name__ == "__main__":
    main()
