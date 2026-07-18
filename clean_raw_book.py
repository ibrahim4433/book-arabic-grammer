import re
import os

RAW_FILE = "system-workspace/text-data/raw/full-book.txt"
CLEAN_FILE = "system-workspace/text-data/raw/full-book-cleaned.txt"

def clean_book():
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    cleaned_lines = []
    
    # Regex patterns for headers and footers
    header_footer_patterns = [
        r"الطريق المباشر",
        r"مكتبة المجد",
        r"حلب - الجميلية",
        r"جلب - الجميلية",
        r"شارع اسكندرون",
        r"\d{7,8}-\d{7,8}", # Phone numbers like 2228125-2222581
        r"^\d{10}$",       # Single phone number 0944510074
        r"^\d{2,3}$",      # Single page numbers (101, 102)
        r"^[\(]?\d+[\)]?$",# Footnote numbers like (1), (2)
        r"^[\u0660-\u0669]+$", # Arabic-Indic digits (page numbers)
    ]
    
    combined_pattern = re.compile("|".join(header_footer_patterns))
    
    buffer = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Skip headers/footers
        if combined_pattern.search(stripped):
            continue
            
        # Optional: Here we could add logic to stitch poetry columns back together,
        # but for now, let's just do a clean pass to get rid of the noise.
        buffer.append(stripped)
        
    # Write the cleaned file
    with open(CLEAN_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(buffer))
        
    print(f"Cleaned file saved to {CLEAN_FILE}")

if __name__ == "__main__":
    clean_book()
