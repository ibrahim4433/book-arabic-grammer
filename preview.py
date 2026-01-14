import os
import glob
from weasyprint import HTML

def get_chapter_map():
    """
    Scans the /pages directory and maps numbers to filenames.
    Example: Returns {2: '02_chapter1.html', 0: '00_cover.html'}
    """
    files = sorted(glob.glob('pages/*.html'))
    chapter_map = {}
    
    for file_path in files:
        filename = os.path.basename(file_path)
        # Extract the first digits (e.g., "02" from "02_chapter1.html")
        try:
            prefix = filename.split('_')[0]
            number = int(prefix) # Converts "02" to 2
            chapter_map[number] = filename
        except ValueError:
            continue # Skip files that don't start with a number
            
    return chapter_map

def main():
    # 1. Setup Output Directory
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Get available chapters
    chapter_map = get_chapter_map()
    if not chapter_map:
        print("❌ No numbered HTML files found in pages/.")
        return

    # 3. Ask User for Input
    print("📘 Available Chapters:")
    for num in sorted(chapter_map.keys()):
        print(f"   [{num}] {chapter_map[num]}")
        
    try:
        selection = input("\n👉 Enter the chapter number to preview: ")
        selection_num = int(selection)
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    # 4. Find and Render
    if selection_num in chapter_map:
        target_file = chapter_map[selection_num]
        input_path = os.path.join('pages', target_file)
        
        # Output name: 02_chapter1.pdf
        output_filename = target_file.replace('.html', '.pdf')
        output_path = os.path.join(output_dir, output_filename)

        print(f"\n🎨 Rendering: {target_file}...")
        
        try:
            # WeasyPrint rendering
            HTML(input_path).write_pdf(output_path)
            print(f"✅ Done! Saved to: {output_path}")
        except Exception as e:
            print(f"❌ Error during rendering: {e}")
            
    else:
        print(f"❌ Chapter {selection_num} not found.")

if __name__ == "__main__":
    main()