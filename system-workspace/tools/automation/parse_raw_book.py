import os
import re
import json

def parse_raw_text(input_path, output_json_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    toc = {"units": []}
    current_unit = None
    current_lesson = None
    current_part = None

    # Helper function to sanitize lines
    def clean_line(line):
        return line.strip()

    # Predefined headings that indicate parts
    part_headings = [
        "مدخل إلى النص:",
        "مهارات الاستماع",
        "مهارات القراءة",
        "الاستيعاب والفهم",
        "المستوى الفكري",
        "المستوى الفني",
        "المستوى الإبداعي",
        "التعبير الكتابي",
        "التعبير الأدبي",
        "التطبيقات اللغوية",
        "تحليل مفصل",
        "اعراب النص",
        "معاني النص",
        "شرح المفردات",
    ]

    delete_headings = [
        "اسطر النص المتتمة",
        "ملحق الابيات المتممة",
        "الموضوعات المقترحة المكتوبة",
        "الموضوعات المقترحة غير المكتوبة",
        "( للحذف )",
        "للحذف"
    ]

    skip_mode = False

    for line in lines:
        c_line = clean_line(line)
        if not c_line:
            continue

        # Remove page separators
        if c_line.startswith("----- PAGE"):
            continue

        # Check if we should enter or exit skip mode
        should_skip = False
        for dh in delete_headings:
            if dh in c_line:
                should_skip = True
                break
        
        if should_skip:
            skip_mode = True
            continue

        # We need a heuristic to exit skip_mode, typically when a new known heading or lesson starts
        if skip_mode:
            is_new_section = False
            for ph in part_headings:
                if ph in c_line:
                    is_new_section = True
                    break
            if "الوحدة" in c_line and ":" in c_line and len(c_line) < 250:
                is_new_section = True
            if is_new_section:
                skip_mode = False
            else:
                continue

        # Unit detection
        if "الوحدة" in c_line and ":" in c_line and len(c_line) < 250:
            current_unit = {
                "title": c_line,
                "lessons": []
            }
            toc["units"].append(current_unit)
            current_lesson = None
            current_part = None
            continue

        # Lesson detection (heuristic: starts with a dash or just text after unit, but real lessons have titles)
        # Let's assume lines that don't match parts and are short might be lessons if they follow a unit or end of previous lesson
        # Or we can just group content. For the sake of this script, we'll collect content into the current part.
        
        if current_unit is None:
            # If we haven't found a unit yet, create a default one
            current_unit = {"title": "Default Unit", "lessons": []}
            toc["units"].append(current_unit)

        if current_lesson is None:
            current_lesson = {"title": "Intro/Lesson", "parts": []}
            current_unit["lessons"].append(current_lesson)
            current_part = {"title": "Intro", "content": []}
            current_lesson["parts"].append(current_part)

        # Check for new parts
        is_part_heading = False
        for ph in part_headings:
            if c_line.startswith(ph):
                is_part_heading = True
                current_part = {"title": c_line, "content": []}
                current_lesson["parts"].append(current_part)
                break

        # If it looks like a new lesson (e.g. short title right before "مدخل إلى النص")
        # We can refine this later. For now, just append to current part
        if not is_part_heading:
            current_part["content"].append(c_line)

    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(toc, f, ensure_ascii=False, indent=2)

    print(f"Parsed {len(toc['units'])} units. Saved to {output_json_path}")
    
    # Generate plans for each part
    plans_dir = "/mnt/c/Documents and Settings/ibrah/Documents/GitHub/book-arabic-grammer/plans"
    os.makedirs(plans_dir, exist_ok=True)
    
    lesson_idx = 1
    for u_idx, unit in enumerate(toc["units"]):
        unit_num = u_idx + 1
        for lesson in unit["lessons"]:
            lesson_title_clean = re.sub(r'[^\\w\\s-]', '', lesson['title']).strip().replace(' ', '_')
            if not lesson_title_clean:
                lesson_title_clean = f"lesson_{lesson_idx}"
            
            for p_idx, part in enumerate(lesson["parts"]):
                part_num = p_idx + 1
                part_title_clean = re.sub(r'[^\\w\\s-]', '', part['title']).strip().replace(' ', '_')
                if not part_title_clean:
                    part_title_clean = f"part_{part_num}"
                
                # Naming: XX.X_nXXX_[title]-plan.md
                # Example: 01.1_n001_intro-plan.md
                filename = f"{unit_num:02d}.{part_num}_n{lesson_idx:03d}_{part_title_clean}-plan.md"
                filepath = os.path.join(plans_dir, filename)
                
                with open(filepath, 'w', encoding='utf-8') as pf:
                    pf.write(f"# {lesson['title']}\\n")
                    pf.write(f"## {part['title']}\\n\\n")
                    pf.write("### Raw Content\\n")
                    pf.write("\\n".join(part["content"]))
            
            lesson_idx += 1

    print(f"Generated plans in {plans_dir}")

if __name__ == "__main__":
    parse_raw_text(
        "/mnt/c/Documents and Settings/ibrah/Documents/GitHub/book-arabic-grammer/system-workspace/text-data/raw/raw_001.txt",
        "/mnt/c/Documents and Settings/ibrah/Documents/GitHub/book-arabic-grammer/system-workspace/text-data/TOC.json"
    )
