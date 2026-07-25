# Module 24: The Synchronizer (`sync_pages.py`)

## 1. Tool Definition
**What is it?** 
In a physical book, you cannot predict what page Lesson 10 will land on until you have perfectly typeset Lessons 1 through 9. If you add a new page to Lesson 4, all the page numbers for the rest of the book instantly break.

`system-workspace/tools/new-tools/sync_pages.py` is the architectural solution to this physical constraint. It ignores the filenames, parses the actual layout order, calculates physical A4 page numbers, renames every single file to lock in the page number, and then dynamically builds a brand new HTML Table of Contents from scratch.

## 2. I/O Mapping
*   **Inputs:** 
    *   The entire `pages/` directory (e.g., `05.0_p00_topic.html`).
*   **Processes:**
    *   Sorts all files alphabetically to determine print order.
    *   Uses `BeautifulSoup` to open every HTML file and extract its `<title>`.
    *   Renames the files to inject the true physical page number into the filename (e.g., `05.0_p24_topic.html`).
    *   Generates `00.2_TOC.html` and `00.3_TOC.html` tables dynamically.
*   **Outputs:**
    *   Synchronized file names in the `pages/` directory.
    *   Brand new Table of Contents HTML files.

---

## 3. The Deep Dive: Codebase Analysis

Below is an exhaustive, 100% codebase breakdown of the Synchronizer.

### Block A: Physical Page Discovery
The script must sort the directory to match how `build.py` prints the book.

```python
# From system-workspace/tools/new-tools/sync_pages.py

8: def to_arabic_indic(text):
9:     english_to_arabic = {
10:         "0": "٠",
11:         "1": "١",
12:         "2": "٢",
13:         "3": "٣",
14:         "4": "٤",
15:         "5": "٥",
16:         "6": "٦",
17:         "7": "٧",
18:         "8": "٨",
19:         "9": "٩",
20:     }
21:     return "".join(english_to_arabic.get(c, c) for c in str(text))
22: 
23: 
24: # build.py processes all files in pages/*.html alphabetically (except TEMPLATE_)
25: all_files = sorted(glob.glob("pages/*.html"))
26: pages_files = [f for f in all_files if "TEMPLATE_" not in f]
27: 
28: # We need to compute the physical page number for each file.
29: # WeasyPrint prints 1 page per file (since they don't overflow).
30: # Front Cover is page 1 (injected by build.py).
31: # The first file in pages_files is page 2.
32: current_physical_page = 2
33: toc_entries = []
34: 
35: # We will store the renaming operations to do them at the end safely
36: rename_ops = []
37: 
38: for file in pages_files:
39:     basename = os.path.basename(file)
```
#### Line-by-Line Commentary
*   **Lines 8-21:** The standard English-to-Arabic integer mapping function (replacing `.translate()` used in Module 23).
*   **Line 25:** `sorted()`
    *   This is why the `05.0_n12` naming convention is so strict! The compiler (`build.py`) physically concatenates the PDF by sorting the filenames alphabetically. Therefore, to predict the page numbers, this script must simulate the exact same alphabetical sort.
*   **Lines 28-32:** Excellent developer logic. It initializes `current_physical_page = 2` because the PDF engine always physically injects the Cover Page (`00.0_cover.html`) at index 1!

### Block B: AST Parsing & Title Extraction
For every single HTML file, the script must figure out what the lesson is actually about.

```python
# From system-workspace/tools/new-tools/sync_pages.py

41:     # Extract info for TOC
42:     with open(file, encoding="utf-8") as f:
43:         soup = BeautifulSoup(f.read(), "html.parser")
44: 
45:     lesson_number = None
46:     ln_div = soup.find("div", class_="lesson-number")
47:     if ln_div:
48:         lesson_number = ln_div.get_text(strip=True)
49: 
50:     lesson_title = None
51:     title_tag = soup.find("title")
52:     if title_tag:
53:         lesson_title = title_tag.get_text(strip=True)
54: 
55:     if basename.startswith("98."):
56:         if lesson_title and not lesson_title.startswith("حَلُّ تَدْرِيبَاتِ الْكِتَابِ"):
57:             lesson_title = "مُلْحَقُ الْإِجَابَاتِ - " + lesson_title
58: 
59:     # Determine new filename
60:     # E.g. 01.0_p05_أَقْسَامُ.html -> 01.0_p06_أَقْسَامُ.html
61:     new_basename = basename
62:     match = re.match(r"^([0-9]+\.[0-9]+)_p[0-9]+_(.*\.html)$", basename)
63:     if match:
64:         new_basename = f"{match.group(1)}_p{current_physical_page:02d}_{match.group(2)}"
65:         if new_basename != basename:
66:             rename_ops.append((file, os.path.join("pages", new_basename)))
67: 
68:     # We only add to TOC if it's not 00.* and not 99.*
69:     if not basename.startswith("00.") and not basename.startswith("99."):
70:         toc_entries.append(
71:             {
72:                 "title": lesson_title or "بدون عنوان",
73:                 "number": to_arabic_indic(lesson_number) if lesson_number else "-",
74:                 "arabic_page": to_arabic_indic(current_physical_page),
75:             }
76:         )
77: 
78:     current_physical_page += 1
```
#### Line-by-Line Commentary
*   **Lines 45-53:** `BeautifulSoup` digs into the DOM to scrape the exact Arabic title directly from the HTML `<title>` tag, guaranteeing the TOC perfectly matches the page content.
*   **Lines 55-57:** It detects if the file is an Answer Key (`98.`). If so, it forcibly prepends "مُلْحَقُ الْإِجَابَاتِ" (Answer Appendix) to the title so it stands out in the TOC.
*   **Lines 62-66:** *The Safe Regex Renamer*. It grabs the chapter prefix (`01.0`), ignores the old page number (`_p05_`), and grabs the rest of the filename. It then injects `current_physical_page` directly into the string (e.g., formatting it to `_p06_`). Crucially, it doesn't execute `os.rename()` here! It adds it to an array so it can perform the renames safely at the very end.
*   **Lines 68-76:** The Cover and the Back pages (`00.` and `99.`) are excluded from the visual TOC. Everything else is appended to the `toc_entries` array for HTML generation.

### Block C: Mass File Renaming
With the calculations done, the system commits the changes to the hard drive.

```python
# From system-workspace/tools/new-tools/sync_pages.py

80: # Execute renames
81: for old_file, new_file in rename_ops:
82:     os.rename(old_file, new_file)
83: 
84: print(f"Renamed {len(rename_ops)} files to match physical page numbers.")
```
#### Line-by-Line Commentary
*   **Lines 80-84:** It iterates through the tuples array and executes `os.rename()`. Delaying this until the end guarantees that if `BeautifulSoup` crashes on file #42, the first 41 files aren't permanently corrupted.

### Block D: Multi-Column TOC Generation
It takes the `toc_entries` array and builds the physical HTML pages.

```python
# From system-workspace/tools/new-tools/sync_pages.py

86: # Generate TOC files
87: mid_point = (len(toc_entries) + 1) // 2
88: chunks = [toc_entries[:mid_point], toc_entries[mid_point:]]
89: 
90: for idx, chunk in enumerate(chunks):
91:     page_num = idx + 2
...
134:         
135:         <table class="toc-table">
136:             <thead>
137:                 <tr>
138:                     <th class="w-5pct text-center">الدَّرْسُ</th>
139:                     <th class="w-35pct">الْمَوْضُوعُ</th>
140:                     <th class="w-5pct text-center">ص</th>
141:                     <th class="spacer-col"></th>
142:                     <th class="w-5pct text-center">الدَّرْسُ</th>
143:                     <th class="w-35pct">الْمَوْضُوعُ</th>
144:                     <th class="w-5pct text-center">ص</th>
145:                 </tr>
146:             </thead>
147:             <tbody>"""
148: 
149:     col_size = (len(chunk) + 1) // 2
150:     col1 = chunk[:col_size]
151:     col2 = chunk[col_size:]
152: 
153:     for row_idx in range(col_size):
154:         item1 = col1[row_idx]
155:         item2 = col2[row_idx] if row_idx < len(col2) else None
156: 
157:         bg1 = "bg-grey-lighter" if ("مُلْحَق" in item1["title"] or "حَلُّ" in item1["title"]) else ""
158:         bg2 = ""
159:         if item2:
160:             bg2 = "bg-grey-lighter" if ("مُلْحَق" in item2["title"] or "حَلُّ" in item2["title"]) else ""
161: 
162:         toc_html += f"""
163:                 <tr>
164:                     <td class="text-center font-bold text-grey {bg1}">{item1["number"]}</td>
165:                     <td class="font-bold {bg1}">{item1["title"]}</td>
166:                     <td class="text-center font-bold text-primary {bg1}">{item1["arabic_page"]}</td>
167:                     
168:                     <td class="spacer-col"></td>
169:                     """
170:         if item2:
171:             toc_html += f"""
172:                     <td class="text-center font-bold text-grey {bg2}">{item2["number"]}</td>
173:                     <td class="font-bold {bg2}">{item2["title"]}</td>
174:                     <td class="text-center font-bold text-primary {bg2}">{item2["arabic_page"]}</td>
175:                 </tr>"""
176:         else:
177:             toc_html += """
178:                     <td></td><td></td><td></td>
179:                 </tr>"""
180: 
181:     toc_html += """
182:             </tbody>
183:         </table>
184:     </div>
185: </body>
186: </html>"""
187: 
188:     with open(f"pages/00.{page_num}_TOC.html", "w", encoding="utf-8") as f:
189:         f.write(toc_html)
190: 
191: print("TOC generated with completely accurate physical page numbers.")
```
#### Line-by-Line Commentary
*   **Lines 87-88:** Because the TOC has ~100 entries, it will not fit on one A4 page. It slices the array perfectly in half to generate two separate TOC pages (e.g., `00.2_TOC.html` and `00.3_TOC.html`).
*   **Lines 149-151:** Inside a specific TOC page, the layout must be a 2-column table. It splits the `chunk` array in half again, creating `col1` (for the left side) and `col2` (for the right side).
*   **Lines 157-160:** It runs a regex-like check against the title. If the title contains "Appendix" or "Solution", it injects a CSS class (`bg-grey-lighter`) into a Python f-string variable (`bg1`).
*   **Lines 162-179:** A standard `for` loop dynamically concatenates the raw HTML, dropping in the titles, Arabic page numbers, and custom CSS classes.
*   **Lines 188-189:** The files are saved, and the physical page numbers for the entire repository are perfectly synchronized!

### Review
You have successfully dissected `sync_pages.py`. You now understand alphabetical ordering, delayed state mutation arrays, mathematical DOM layout splits, and dynamic HTML injection!
