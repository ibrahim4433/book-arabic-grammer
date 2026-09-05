import glob
import re
from bs4 import BeautifulSoup

def to_arabic_number(n):
    english_to_arabic = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
    return str(n).translate(english_to_arabic)

def strip_leading_numbers(text):
    # Remove leading Arabic/English numbers, dashes, and whitespace
    # e.g., "١- ", "1 -", "١٢ - "
    return re.sub(r'^[\s\u200B]*[\u0660-\u06690-9]+[\s\u200B]*[-ـ][\s\u200B]*', '', text).strip()

def process_all_files():
    # Sort files to ensure _cont files come immediately after their main files
    files = sorted(glob.glob("pages/*.html"))
    
    current_counter = 1
    
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        modified = False
        
        # Find all poem verses blocks
        poem_containers = soup.find_all(class_="poem-container")
        for i, container in enumerate(poem_containers):
            # If it's a main page, reset the counter for each container.
            # If it's a _cont page, we continue the counter from the previous page.
            if "_cont" not in filepath:
                current_counter = 1
                
            poem_lines = container.find_all(class_="poem-line")
            for line in poem_lines:
                hemistichs = line.find_all(class_="hemistich")
                if not hemistichs: continue
                
                first_hemi = hemistichs[0]
                
                # Find the first text node that is not empty whitespace
                first_text_node = None
                for descendant in first_hemi.descendants:
                    if isinstance(descendant, str) and descendant.strip():
                        first_text_node = descendant
                        break
                
                if first_text_node:
                    original_text = str(first_text_node)
                    stripped_text = strip_leading_numbers(original_text)
                    
                    arabic_num = to_arabic_number(current_counter)
                    new_text = f"{arabic_num}- {stripped_text}"
                    
                    first_text_node.replace_with(new_text)
                    modified = True
                    
                current_counter += 1
                
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(str(soup))
            print(f"Numbered verses in {filepath}")

if __name__ == "__main__":
    process_all_files()
    print("Done numbering verses.")
