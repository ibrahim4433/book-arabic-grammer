import os
import re
from bs4 import BeautifulSoup

PAGES_DIR = "pages/"

# Refined Keywords based on analysis
KEYWORDS_ORANGE = [
    "مثال", "أمثلة", "شواهد", "تطبيق", "فائدة", "تنبيه", "نماذج",
    "تمرين", "تدريب", "ملاحظة", "فرق", "ملخص", "جدول"
]
KEYWORDS_BLACK = [
    "اختبر", "أسئلة", "تمارين", "تطبيقات"
]
# Keywords Teal are implicit (Default)

def remove_tashkeel(text):
    # Remove Arabic diacritics
    tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652\u0670\u06D6-\u06ED]')
    return tashkeel.sub('', text)

def fix_colors(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    modified = False

    # Find all content blocks
    blocks = soup.find_all("section", class_="content-block")
    div_blocks = soup.find_all("div", class_="content-block")
    all_blocks = blocks + div_blocks

    for block in all_blocks:
        header = block.find("div", class_="block-header")

        if not header:
            continue

        raw_text = header.get_text().strip()
        text = remove_tashkeel(raw_text)

        # Determine current class
        classes = header.get("class", [])

        # Determine target style
        target_style = "default" # Teal

        # Check Keywords
        # We check BLACK first as it's most specific (Exams)
        is_black = any(k in text for k in KEYWORDS_BLACK)
        # Then Orange
        is_orange = any(k in text for k in KEYWORDS_ORANGE)

        if is_black:
            target_style = "dark"
        elif is_orange:
            target_style = "accent"
        else:
            target_style = "default"

        # Apply Logic
        current_classes = set(classes)
        new_classes = current_classes.copy()

        if target_style == "dark":
            if "bg-dark" not in new_classes:
                new_classes.add("bg-dark")
                new_classes.discard("accent") # Remove accent if present
                modified = True
        elif target_style == "accent":
            if "accent" not in new_classes:
                new_classes.add("accent")
                new_classes.discard("bg-dark") # Remove dark if present
                modified = True
        else: # default
            if "accent" in new_classes:
                new_classes.discard("accent")
                modified = True
            if "bg-dark" in new_classes:
                new_classes.discard("bg-dark")
                modified = True

        if modified:
             header["class"] = list(new_classes)

    if modified:
        print(f"Fixed colors in: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))

def main():
    if not os.path.exists(PAGES_DIR):
        print(f"Directory {PAGES_DIR} not found.")
        return

    files = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith(".html")])

    for filename in files:
        filepath = os.path.join(PAGES_DIR, filename)
        try:
            fix_colors(filepath)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
