import os
import glob
from weasyprint import HTML

def main():
    # Ensure output directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Find all HTML files in pages/ sorted alphabetically
    pages_files = sorted(glob.glob('pages/*.html'))

    if not pages_files:
        print("No HTML files found in pages/.")
        return

    print(f"Found {len(pages_files)} pages: {pages_files}")

    # Render the first page to create the initial document
    print(f"Rendering {pages_files[0]}...")
    main_doc = HTML(filename=pages_files[0]).render()

    # Render and append subsequent pages
    for page_file in pages_files[1:]:
        print(f"Rendering {page_file}...")
        doc = HTML(filename=page_file).render()
        main_doc.pages.extend(doc.pages)

    # Save the final PDF
    output_file = os.path.join(output_dir, 'book.pdf')
    main_doc.write_pdf(output_file)
    print(f"PDF successfully generated at {output_file}")

if __name__ == "__main__":
    main()
