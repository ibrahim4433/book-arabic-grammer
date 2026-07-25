# Module 23: The Indexer (`rebuild_toc.py`)

## 1. Tool Definition
**What is it?** 
The Table of Contents (TOC) page in this grammar book is highly complex. It is a dense, 2-column HTML table that lists the lessons on the left, and the corresponding "Exam Answer Keys" on the right. 

`system-workspace/tools/new-tools/rebuild_toc.py` is a specialized technical debt fixer. If the AI generated 34 different answer pages, this script automatically scans the hard drive, parses the HTML files using Regex to figure out exactly which lesson an answer belongs to, and dynamically rebuilds the HTML Table of Contents to flawlessly link everything together.

## 2. I/O Mapping
*   **Inputs:** 
    *   34 HTML files in `backup_answers/` (e.g., `98.0_n42_answers_p12_.html`).
    *   `pages/00.3_TOC.html.bak` (The existing HTML Table of Contents).
*   **Processes:**
    *   Uses Regex to scrape Arabic text and extract the mathematical lesson numbers out of the generated HTML.
    *   Uses `BeautifulSoup` to strip the `<tbody>` tags out of the existing TOC.
    *   Mathematically calculates how to fit 24 lessons and 34 answer keys into a single 2-column A4 grid without overflowing the page.
*   **Outputs:**
    *   A perfectly formatted, overwritten `pages/00.3_TOC.html`.

---

## 3. The Deep Dive: Codebase Analysis

Below is an exhaustive, 100% codebase breakdown of the TOC Rebuilder.

### Block A: File Parsing & Regex Extraction
The script must first figure out what it is trying to index.

```python
# From system-workspace/tools/new-tools/rebuild_toc.py

1: import glob
2: import re
3: 
4: from bs4 import BeautifulSoup
5: 
6: ar_to_en = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
7: en_to_ar = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
8: 
9: # Step 1: Collect and sort all 34 Answer entries from the backup files
10: entries = []
11: for f in glob.glob("backup_answers/98.*.html"):
12:     m = re.search(r"_p([0-9]+)_", f)
13:     if not m:
14:         continue
15:     page = int(m.group(1))
16: 
17:     text = open(f, encoding="utf-8").read()
18:     headers = re.findall(r"إِجَابَاتُ[^<]+", text)
19:     lessons = []
20:     for h in headers:
21:         m2 = re.search(r"الدَّرْسُ\s*([0-9]+)", h)
22:         if m2:
23:             lessons.append(int(m2.group(1)))
24: 
25:     if lessons:
26:         lessons = sorted(list(set(lessons)))
27:         entries.append((lessons, page))
28: 
29: # Sort by first lesson number
30: entries.sort(key=lambda x: x[0][0])
```
#### Line-by-Line Commentary
*   **Lines 6-7:** `str.maketrans`
    *   This is a highly efficient Python translation map. It allows the script to instantly convert English integers (`5`) into Arabic-Indic digits (`٥`) and vice versa.
*   **Lines 11-15:** It uses Python's `glob` to find all answer files (which start with `98.`). It then uses regex to pull the physical page number directly out of the filename string (e.g., `_p12_` -> `12`).
*   **Lines 17-23:** It opens the file and uses Arabic-specific Regex (`الدَّرْسُ\s*([0-9]+)`) to scan the raw HTML code and find exact strings like "Lesson 15". It converts the string "15" into a Python integer.
*   **Lines 26-30:** It deduplicates the array (using `set()`) and sorts them so the TOC isn't scrambled out of order.

### Block B: Arabic String Translation & Title Generation
The script now dynamically generates the Arabic text that will be displayed in the TOC.

```python
# From system-workspace/tools/new-tools/rebuild_toc.py

32: answer_blocks = []
33: for lessons, page in entries:
34:     if len(lessons) > 2:
35:         lessons_str = " وَ ".join(str(l) for l in lessons)
36:         title = f"إِجَابَاتُ الدُّرُوسِ {lessons_str}".translate(en_to_ar)
37:     elif len(lessons) == 2:
38:         title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]} وَ {lessons[1]}".translate(en_to_ar)
39:     else:
40:         title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]}".translate(en_to_ar)
41:     ar_page = str(page).translate(en_to_ar)
42:     answer_blocks.append((title, ar_page))
```
#### Line-by-Line Commentary
*   **Lines 34-40:** Arabic has strict pluralization rules. 
    *   If a page has >2 lessons on it, it must use the plural "Lessons" (`الدُّرُوسِ`).
    *   If a page has exactly 1 or 2 lessons on it, it must use the singular/dual "Lesson" (`الدَّرْسِ`).
*   **Lines 36, 38, 40:** Notice the `.translate(en_to_ar)` method. This applies the translation map from Block A. If the Python f-string generated `إِجَابَاتُ الدَّرْسِ 5`, this instantly converts it to `إِجَابَاتُ الدَّرْسِ ٥`!

### Block C: BeautifulSoup DOM Extraction
We need to extract the existing lessons from the old TOC without breaking the HTML layout.

```python
# From system-workspace/tools/new-tools/rebuild_toc.py

44: # Step 2: Read the current 00.3_TOC.html
45: with open("pages/00.3_TOC.html.bak", encoding="utf-8") as f:
46:     html_content = f.read()
47: 
48: soup = BeautifulSoup(html_content, "html.parser")
49: tbody = soup.find("tbody")
50: 
51: # Collect actual lessons from the left side
52: left_lessons = []
53: for tr in tbody.find_all("tr"):
54:     tds = tr.find_all("td")
55:     if len(tds) >= 3:
56:         # Check if the left column is an answer (98) or a real lesson
57:         lesson_num = tds[0].get_text(strip=True)
58:         if lesson_num.translate(ar_to_en) != "98":
59:             # Store the 3 elements of the left column
60:             left_lessons.append([str(tds[0]), str(tds[1]), str(tds[2])])
61: 
62: # Create an empty tbody to rebuild
63: tbody.clear()
```
#### Line-by-Line Commentary
*   **Lines 48-49:** `BeautifulSoup` parses the HTML into an Abstract Syntax Tree (AST), allowing us to target the `<tbody>` tag like a Python dictionary.
*   **Lines 53-60:** It loops through every `<tr>` (table row). It checks the first `<td>` element. If the lesson number isn't `98` (which is the internal code for "Answer Keys"), it saves the 3 cells (Number, Title, Page) into the `left_lessons` array.
*   **Line 63:** `tbody.clear()`
    *   *The Nuke*. It physically deletes all children of the `<tbody>` tag in the AST, preparing for a total structural rebuild.

### Block D: Intelligent Multi-Column Row Assembly
This is where the 1-Page Layout rules are enforced. A 2-column layout requires careful mathematical balancing to avoid wasting vertical space.

```python
# From system-workspace/tools/new-tools/rebuild_toc.py

65: # Step 3: Rebuild the table rows
66: # We need max(len(left_lessons), len(answer_blocks)) rows.
67: # But wait! If we just put them all on the right, we will have 34 rows. 24 will have left lessons, 10 will have empty left sides.
68: # Wait, if we want to save space and keep it neat, we could put the remaining answers on the LEFT side of the extra rows!
69: # Let's see: left_lessons has 24 items. answer_blocks has 34 items.
70: # Row 1-24: Left = lesson, Right = Answer (1-24)
71: # Row 25-29: Left = Answer (25-29), Right = Answer (30-34)
72: # That's exactly 5 rows!
73: # Let's do that to save vertical space and match the style!
74: 
75: # Let's build the rows
76: num_rows = 24 + 5  # 29 rows total
77: ans_idx = 0
78: 
79: for i in range(29):
80:     tr = soup.new_tag("tr")
81: 
82:     # --- LEFT SIDE ---
83:     if i < len(left_lessons):
84:         # Add actual lesson
85:         for td_str in left_lessons[i]:
86:             tr.append(BeautifulSoup(td_str, "html.parser"))
87:     else:
88:         # Add an answer block on the left
89:         if ans_idx < len(answer_blocks):
90:             title, ar_page = answer_blocks[ans_idx]
91:             ans_idx += 1
92:             td1 = soup.new_tag(
93:                 "td", attrs={"class": "text-center font-bold text-grey bg-grey-lighter"}
94:             )
95:             td1.string = "٩٨"
96:             td2 = soup.new_tag("td", attrs={"class": "font-bold bg-grey-lighter"})
97:             td2.string = title
98:             td3 = soup.new_tag(
99:                 "td", attrs={"class": "text-center font-bold text-primary bg-grey-lighter"}
100:             )
101:             td3.string = ar_page
102:             tr.append(td1)
103:             tr.append(td2)
104:             tr.append(td3)
...
114:     # --- SPACER ---
115:     spacer = soup.new_tag("td", attrs={"class": "spacer-col"})
116:     tr.append(spacer)
...
146: # Write back to file
147: with open("pages/00.3_TOC.html", "w", encoding="utf-8") as f:
148:     f.write(str(soup))
```
#### Line-by-Line Commentary
*   **Lines 66-73:** Excellent developer comments! The developer realized that printing 34 Answer blocks on the right column while only having 24 Lessons on the left column would result in 10 rows of empty white space on the left, making the A4 page overflow! The solution? Math. Wrap the final 10 Answer blocks around so they take up both the Left and Right columns at the bottom of the page!
*   **Line 79-86:** For the first 24 rows, it injects the `left_lessons` array (which contains the actual grammar lessons) directly into the left column of the `<tr>`.
*   **Lines 87-104:** For the remaining 5 rows, it dynamically generates the `<td>` nodes using `soup.new_tag()`. It aggressively applies `bg-grey-lighter` utility classes to visually differentiate these Answer Blocks from the standard lessons.
*   **Line 115:** `spacer = soup.new_tag("td", attrs={"class": "spacer-col"})`
    *   This is the middle column that physically separates the Left data from the Right data, giving the HTML table its 2-column aesthetic.
*   **Lines 147-148:** The fully rebuilt AST is dumped back to the hard drive as raw HTML, perfectly formatted for A4 rendering.

### Review
You have successfully dissected `rebuild_toc.py`. You now understand Python translation maps, Arabic regex grouping, and advanced DOM reconstruction using `BeautifulSoup`!
