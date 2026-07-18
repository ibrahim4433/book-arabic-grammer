import json
import re

def create_toc():
    with open("system-workspace/text-data/raw/raw_001.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    toc = {}
    lesson_num = 1
    
    for i, line in enumerate(lines):
        if "مدخل إلى النص" in line:
            # Look at the previous 6 lines to find the title
            title = "Unknown"
            for j in range(max(0, i-6), i):
                stripped = lines[j].strip()
                # Skip author descriptions
                if not stripped or stripped.startswith("-") or "شاعر" in stripped or "مواليد" in stripped or re.search(r'\d', stripped):
                    continue
                # If it's a short line, it's likely the title
                if len(stripped) < 40:
                    title = stripped
                    break
                    
            if title == "Unknown":
                title = f"Lesson {lesson_num}"
                
            toc[f"{lesson_num:02d}"] = {
                "title": title,
                "level": "الثالث الثانوي",
                "Unit": "النصوص الأدبية",
                "author": "د. محسن المحل",
                "author_number": "٠٩٦٦٥٠١٦١٦"
            }
            lesson_num += 1
            
    with open("input/TOC.json", "w", encoding="utf-8") as f:
        json.dump(toc, f, ensure_ascii=False, indent=4)
        
    print(f"Generated TOC.json with {len(toc)} lessons.")

if __name__ == "__main__":
    create_toc()
