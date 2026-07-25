# Module 6: The Vibe-Coding Aftermath (Managing 80+ Fixer Scripts)

Welcome to Module 6. If you look inside the `system-workspace/tools/new-tools/` directory, you will see over 80 individual Python scripts with names like `fix_book.py`, `restore_and_fix.py`, `rebuild_toc.py`, and `sync_pages.py`.

Why are there so many? 

This project was built rapidly using AI agents (a process sometimes called "vibe coding"). While AI is incredibly fast at generating 200 pages of Arabic grammar lessons, it is also prone to making repetitive, microscopic errors across all 200 pages. It might add a weird suffix to a title, drop an ID, or misalign a table column.

Instead of opening 200 HTML files and fixing these errors manually, the developers wrote programmatic **Fixer Scripts** to parse the HTML trees (using BeautifulSoup) and repair the damage automatically.

In this module, we will dissect two prominent fixer scripts to understand exactly how we manage the technical debt of AI generation.

---

## Beginner Primer: The Document Object Model (DOM) Explained

In this module, you will see a library called `BeautifulSoup` used constantly. What does it actually do?

When a browser (or a Python script) reads an HTML file, it doesn't see it as a flat string of text. It converts it into a 3D "Tree" called the Document Object Model (DOM).

Imagine this HTML:
```html
<div class="box">
    <h1>Title</h1>
    <p>Text</p>
</div>
```

`BeautifulSoup` turns that flat text into a family tree in Python's memory:
* **Parent**: `div` (class: box)
  * **Child 1**: `h1` (text: Title)
  * **Child 2**: `p` (text: Text)

Instead of using messy string replacements (like we did in Module 0), `BeautifulSoup` lets us safely say: *"Find the `h1` child inside the `div` parent, and change its text."* This is how we programmatically fix 200 pages of broken AI HTML without destroying the layout!

---

## Lesson 1: Script Dissection - `fix_book.py` (Title Cleanup)

When the AI generated the book, it sometimes appended Arabic words like "(تابع)" (Continued) or "(تتمة)" (Conclusion) to the lesson titles in the HTML headers. We needed a script to strip these out, group lessons by their true title, and rename them uniformly (e.g., Part 1, Part 2).

Here is the exact core logic from `fix_book.py` that handles the extraction and Regex cleanup:

```python
# From system-workspace/tools/new-tools/fix_book.py
from bs4 import BeautifulSoup
import re
import os

# Analyze titles to group duplicates
groups = {}
file_info = []

for file in lesson_files: # (lesson_files is a list of all HTML paths in pages/)
    basename = os.path.basename(file)
    with open(file, encoding="utf-8") as f:
        # 1. Parse the HTML file into an Abstract Syntax Tree (AST)
        soup = BeautifulSoup(f.read(), "html.parser")

    # 2. Target the exact <h1> tag containing the title
    lt_h1 = soup.find("h1", class_="header-title")
    title = lt_h1.get_text(strip=True) if lt_h1 else ""

    # 3. Clean up AI hallucinations (تابع), (تتمة), etc. using Regex
    # This regex removes (تابع) or (تتمة) or تابع or تتمة at the end of the title
    clean_title = re.sub(r"\(?\s*(تابع|تتمة|تَتِمَّةٌ|تَتِمَّة|تَابِع)\s*\)?", "", title).strip()
    clean_title = re.sub(r"\s+", " ", clean_title)  # normalize spaces

    # 4. Group the files by their new clean title
    if clean_title not in groups:
        groups[clean_title] = []
    groups[clean_title].append(file)

    # 5. Store the soup object so we can modify and save it later
    file_info.append({"file": file, "clean_title": clean_title, "soup": soup, "basename": basename})
```

**Line-by-Line Breakdown:**
1.  **`soup = BeautifulSoup(f.read(), "html.parser")`**: We NEVER use basic string replacement (like in Module 0) to *fix* complex HTML. We parse it into a DOM tree so we can target specific tags safely.
2.  **`lt_h1 = soup.find("h1", class_="header-title")`**: We instantly jump to the exact node in the HTML tree that holds the lesson title.
3.  **`re.sub(r"\(?\s*(تابع|تتمة...`**: This is a powerful Regular Expression. It looks for the specific Arabic words for "Continued" (with or without parenthesis or diacritics) and replaces them with an empty string `""`, effectively deleting them.
4.  **`groups[clean_title].append(file)`**: By grouping files that share the exact same clean title, a later part of the script knows it needs to rename them to "Lesson Name (Part 1)" and "Lesson Name (Part 2)".
5.  **`file_info.append({"soup": soup...})`**: We keep the `BeautifulSoup` object in memory. Later in the script, we just do `lt_h1.string = new_title` and `f.write(str(soup))` to save the perfectly repaired HTML back to the hard drive.

---

## Lesson 2: Script Dissection - `rebuild_toc.py` (Cross-File Synchronization)

A major challenge with 200 separate HTML files is synchronization. If you rename a lesson in `pages/05.0_lesson.html`, the Table of Contents (`pages/00.3_TOC.html`) instantly becomes outdated.

Instead of updating the TOC manually, `rebuild_toc.py` acts as a scraper. It crawls through the actual lesson files, extracts the real data, and programmatically rebuilds the TOC `<tbody>` table.

```python
# From system-workspace/tools/new-tools/rebuild_toc.py
import glob
import re

# Translation tables to convert English numbers to Arabic-Indic numbers
ar_to_en = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
en_to_ar = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

# Step 1: Collect and sort all 34 Answer entries from the backup files
entries = []
# We use glob to dynamically find all answer files (which start with 98)
for f in glob.glob("backup_answers/98.*.html"):
    
    # 1. Extract the physical page number from the filename (e.g., ..._p45_...)
    m = re.search(r"_p([0-9]+)_", f)
    if not m:
        continue
    page = int(m.group(1))

    # 2. Open the file and search for the header text
    text = open(f, encoding="utf-8").read()
    headers = re.findall(r"إِجَابَاتُ[^<]+", text)
    
    lessons = []
    for h in headers:
        # Extract the exact lesson number the answers belong to
        m2 = re.search(r"الدَّرْسُ\s*([0-9]+)", h)
        if m2:
            lessons.append(int(m2.group(1)))

    # 3. Store the relation between the Lesson Number and the Physical Page
    if lessons:
        lessons = sorted(list(set(lessons)))
        entries.append((lessons, page))

# 4. Sort the master list by lesson number so the TOC is in order
entries.sort(key=lambda x: x[0][0])
```

**Line-by-Line Breakdown:**
1.  **`str.maketrans(...)`**: The book strictly uses Arabic-Indic numbers (١, ٢, ٣). However, Python math requires English numbers. This setup allows the script to translate between them instantly.
2.  **`glob.glob("backup_answers/98.*.html")`**: `glob` dynamically searches the folder for any file matching that pattern. It prevents hardcoding filenames.
3.  **`re.search(r"_p([0-9]+)_", f)`**: The physical page number is stored directly in the filename. The regex `_p([0-9]+)_` captures those digits perfectly.
4.  **`entries.append((lessons, page))`**: We build a massive list of tuples linking Lesson Numbers to Page Numbers. 
*Later in the script, `BeautifulSoup` is used to inject this exact list of tuples directly into the `<tr>` and `<td>` tags of the TOC HTML file.*

---

## Lesson 3: Writing a Standardized Fixer

The `new-tools/` directory is cluttered with 80+ scripts. Many of them are "hardcoded single-use scripts" (e.g., fixing one specific spelling error on page 14). 

According to the rules in `GEMINI.md`, **this practice is now forbidden.** 

*"When automating fixes or refactoring, do NOT write hardcoded, single-use scripts. Always build or utilize generalized, argument-driven tools."*

If you need to write a fixer, you must use `argparse` to make it reusable. Here is the official boilerplate template for a new fixer script:

```python
#!/usr/bin/env python3
"""
Standardized Fixer Script Boilerplate
Description: Replaces a specific target string across all HTML files in a directory.
Usage: python tools/fix_text.py --dir pages/ --target "Old" --replacement "New"
"""

import argparse
from pathlib import Path
from bs4 import BeautifulSoup

def process_files(directory: Path, target: str, replacement: str):
    # 1. Glob all HTML files in the provided directory
    for filepath in directory.glob("*.html"):
        if "TEMPLATE" in filepath.name:
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        # 2. Modify the DOM (Example: Replace text in paragraphs)
        changed = False
        for p_tag in soup.find_all("p"):
            if p_tag.string and target in p_tag.string:
                p_tag.string = p_tag.string.replace(target, replacement)
                changed = True
                
        # 3. Only write to disk if a change actually occurred (saves I/O time)
        if changed:
            with open(filepath, "w", encoding="utf-8") as out:
                out.write(str(soup))
            print(f"✅ Updated: {filepath.name}")

if __name__ == "__main__":
    # 4. Use Argparse to make the script reusable!
    parser = argparse.ArgumentParser(description="A generic text replacer.")
    parser.add_argument("--dir", type=Path, default=Path("pages"), help="Target directory")
    parser.add_argument("--target", type=str, required=True, help="Text to find")
    parser.add_argument("--replacement", type=str, required=True, help="Replacement text")
    
    args = parser.parse_args()
    
    if not args.dir.exists():
        print(f"❌ Directory {args.dir} not found.")
    else:
        process_files(args.dir, args.target, args.replacement)
```

By strictly using `argparse`, you ensure the script can be used again next month when a completely different typo is discovered, preventing the repository from filling up with 80 more single-use scripts.

### Review
You have now seen the reality of AI-assisted development. 
*   You know why the `new-tools/` directory exists (to manage AI tech debt).
*   You've seen how `fix_book.py` uses BeautifulSoup and Regex to surgically repair HTML.
*   You've seen how `rebuild_toc.py` scrapes data across multiple files to synchronize the project.
*   You know how to write a standardized, reusable fixer script using `argparse`.

Congratulations! You have completed the technical curriculum. In the final step, we will prepare the Walkthrough Artifact for your review.
