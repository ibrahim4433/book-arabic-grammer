import os
import glob
from weasyprint import HTML

def get_chapter_map():
    """
    Scans the /pages directory.
    Maps numbers (1, 2) to chapters.
    Maps 't' specifically to the Template.
    """
    files = sorted(glob.glob('pages/*.html'))
    chapter_map = {}
    
    for file_path in files:
        filename = os.path.basename(file_path)
        
        # 1. SPECIAL CASE: Detect the Template
        if filename == 'TEMPLATE_CHAPTER.html':
            chapter_map['t'] = filename
            continue
            
        # 2. STANDARD CASE: Detect Numbered Chapters
        try:
            prefix = filename.split('_')[0]
            number = int(prefix) # Converts "02" to 2
            chapter_map[str(number)] = filename # Store as string keys
        except ValueError:
            continue # Skip files that don't match the pattern
            
    return chapter_map

def main():
    # 1. Setup Output Directory
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 2. Get available chapters
    chapter_map = get_chapter_map()
    if not chapter_map:
        print("❌ No HTML files found in pages/.")
        return

    # 3. Display Options
    print("\n📘 Available Files to Preview:")
    
    # Print the Template first if it exists
    if 't' in chapter_map:
        print(f"   [t] 🎨 {chapter_map['t']} (THE MASTER TEMPLATE)")
    
    # Print numbered chapters sorted
    numeric_keys = sorted([k for k in chapter_map.keys() if k.isdigit()], key=int)
    for key in numeric_keys:
        print(f"   [{key}]    {chapter_map[key]}")
        
    # 4. Ask User
    selection = input("\n👉 Enter number (or 't' for template): ").strip().lower()

    # 5. Render
    if selection in chapter_map:
        target_file = chapter_map[selection]
        input_path = os.path.join('pages', target_file)
        
        # Output name: TEMPLATE_CHAPTER.pdf or 02_chapter1.pdf
        output_filename = target_file.replace('.html', '.pdf')
        output_path = os.path.join(output_dir, output_filename)

        print(f"\n🎨 Rendering: {target_file}...")
        
        try:
            HTML(input_path).write_pdf(output_path)
            print(f"✅ Done! Saved to: {output_path}")
        except Exception as e:
            print(f"❌ Error during rendering: {e}")
            
    else:
        print(f"❌ Selection '{selection}' not found.")

if __name__ == "__main__":
    main()