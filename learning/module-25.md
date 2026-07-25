# Module 25: The AST DOM Fixer (`fix_book.py`)

## 1. Tool Definition
**What is it?** 
The AI models frequently hallucinate when dealing with titles. Because the book is restricted to a "1-Page Layout", lessons that are too long get split into two pages (e.g., `05.1` and `05.2`). The AI often names both pages identically, or randomly appends messy suffixes like `(تابع)` or `(تتمة)`. 

`system-workspace/tools/new-tools/fix_book.py` is a specialized technical debt cleaner. It uses `BeautifulSoup` to scan the entire repository, mathematically grouping identical titles, and then physically mutating the DOM of the HTML files to inject standardized Arabic part suffixes (`الْجُزْءُ الْأَوَّلُ`, `الثَّانِي`).

## 2. I/O Mapping
*   **Inputs:** 
    *   The `pages/` directory.
*   **Processes:**
    *   Scans every `<title>` tag and strips out hallucinatory suffixes using Regex.
    *   Groups identically-named files together.
    *   Injects beautifully translated Arabic multi-part strings into the DOM of the grouped files.
    *   Finds every single *Answer Key* file that references the old titles, and updates them to match the new titles!
*   **Outputs:**
    *   Overwritten HTML files with perfectly standardized multi-part titles.

---

## 3. The Deep Dive: Codebase Analysis

Below is an exhaustive, 100% codebase breakdown of the AST DOM Fixer.

### Block A: File Discovery & Grouping
The script first figures out which pages belong to the same parent lesson.

```python
# From system-workspace/tools/new-tools/fix_book.py

38: pages_dir = Path("pages")
39: 
40: # 1. Gather all lesson files except 00.* and 98.*
41: all_files = sorted(glob.glob("pages/*.html"))
42: lesson_files = [
43:     f
44:     for f in all_files
45:     if "TEMPLATE_" not in f
46:     and not os.path.basename(f).startswith("00.")
47:     and not os.path.basename(f).startswith("98.")
48: ]
49: 
50: # Analyze titles to group duplicates
51: groups = {}
52: file_info = []
53: 
54: for file in lesson_files:
55:     basename = os.path.basename(file)
56:     with open(file, encoding="utf-8") as f:
57:         soup = BeautifulSoup(f.read(), "html.parser")
58: 
59:     lt_h1 = soup.find("h1", class_="header-title")
60:     title = lt_h1.get_text(strip=True) if lt_h1 else ""
61: 
62:     # Clean up (تابع), (تتمة), etc.
63:     # regex to remove (تابع) or (تتمة) or تابع or تتمة at the end
64:     clean_title = re.sub(r"\(?\s*(تابع|تتمة|تَتِمَّةٌ|تَتِمَّة|تَابِع)\s*\)?", "", title).strip()
65:     clean_title = re.sub(r"\s+", " ", clean_title)  # normalize spaces
66: 
67:     if clean_title not in groups:
68:         groups[clean_title] = []
69:     groups[clean_title].append(file)
70: 
71:     file_info.append({"file": file, "clean_title": clean_title, "soup": soup, "basename": basename})
```
#### Line-by-Line Commentary
*   **Lines 40-48:** It strictly ignores Answer Keys (`98.`) and TOC pages (`00.`) because they don't follow standard naming conventions.
*   **Lines 64-65:** *The Hallucination Stripper*. The AI loves adding random Arabic words meaning "Continued" (`تابع`) to the end of multi-page titles. This aggressive regex targets every possible spelling variant (with or without Tashkeel, with or without parentheses) and physically deletes them to generate a pure, clean title string.
*   **Lines 67-69:** It uses a Python Dictionary to group identical titles. If Lesson 5 has 3 pages, `groups["Lesson 5"]` will now contain an array of 3 file paths.

### Block B: AST Modification & Multi-Part Suffixing
Now it replaces the raw titles with standardized, mathematically generated Arabic numbers.

```python
# From system-workspace/tools/new-tools/fix_book.py

25: arabic_parts = [
26:     "الْأَوَّلُ",
27:     "الثَّانِي",
28:     "الثَّالِثُ",
29:     "الرَّابِعُ",
30:     "الْخَامِسُ",
...
36: ]
...
73: # Assign new titles
74: new_titles = {}  # file -> new_title
75: for title, files_in_group in groups.items():
76:     if len(files_in_group) == 1:
77:         new_titles[files_in_group[0]] = title
78:     else:
79:         for idx, f in enumerate(files_in_group):
80:             part_name = arabic_parts[idx] if idx < len(arabic_parts) else str(idx + 1)
81:             new_titles[f] = f"{title} (الْجُزْءُ {part_name})"
82: 
83: # Update the HTML files with new titles
84: print("Updating lesson titles in HTML files...")
85: for info in file_info:
86:     f = info["file"]
87:     new_title = new_titles[f]
88:     soup = info["soup"]
89: 
90:     lt_h1 = soup.find("h1", class_="header-title")
91:     if lt_h1 and lt_h1.get_text(strip=True) != new_title:
92:         lt_h1.string = new_title
93:         with open(f, "w", encoding="utf-8") as out:
94:             out.write(str(soup))
```
#### Line-by-Line Commentary
*   **Lines 25-36:** A hardcoded array of perfectly vocalized Arabic ordinal numbers (First, Second, Third...).
*   **Line 79-81:** It loops over the grouped files. If a lesson has 3 pages, the `enumerate(files_in_group)` loop uses `idx` to grab the correct Arabic string from the array. It dynamically constructs a beautiful title: `Lesson 5 (Part First)`, `Lesson 5 (Part Second)`, etc.
*   **Lines 90-94:** It locates the `<h1>` element in the AST using BeautifulSoup, overwrites the string property (`lt_h1.string = new_title`), and saves the file back to the hard drive.

### Block C: Syncing External Dependencies (Answer Keys)
If we change a lesson title from "Lesson 5 (Continued)" to "Lesson 5 (Part 2)", then the *Answer Key* file (which says "Answers for Lesson 5 (Continued)") is now broken! We must fix the dependencies.

```python
# From system-workspace/tools/new-tools/fix_book.py

110: # Since we know the lesson numbers (from the header span), we can map lesson_number -> new_title
111: lesson_num_to_title = {}
112: for info in file_info:
113:     ln_div = info["soup"].find("div", class_="lesson-number")
114:     if ln_div:
115:         ln = ln_div.get_text(strip=True)
116:         lesson_num_to_title[to_arabic_indic(ln)] = new_titles[info["file"]]
117:         lesson_num_to_title[ln] = new_titles[info["file"]]
118: 
119: for f in answer_files:
120:     with open(f, encoding="utf-8") as ans_f:
121:         content = ans_f.read()
122: 
123:     soup = BeautifulSoup(content, "html.parser")
124:     changed = False
125:     for section in soup.find_all("section", class_="content-block"):
126:         header_span = section.find("div", class_="block-header").find("span")
127:         if header_span:
128:             text = header_span.get_text(strip=True)
129:             # format is إِجَابَاتُ: TITLE (الدَّرْسُ NUMBER)
130:             match = re.search(r"إِجَابَاتُ: (.*?) \(الدَّرْسُ (.*?)\)", text)
131:             if match:
132:                 old_title = match.group(1)
133:                 num = match.group(2)
134: 
135:                 # normalize num (might be arabic-indic or ascii)
136:                 if num in lesson_num_to_title:
137:                     correct_title = lesson_num_to_title[num]
138:                     new_text = f"إِجَابَاتُ: {correct_title} (الدَّرْسُ {num})"
139:                     if text != new_text:
140:                         header_span.string = new_text
141:                         changed = True
142: 
143:     if changed:
144:         with open(f, "w", encoding="utf-8") as out:
145:             out.write(str(soup))
```
#### Line-by-Line Commentary
*   **Lines 111-117:** It builds a dictionary mapping the absolute lesson number (`05`) to the newly generated perfect title (`Lesson 5 (Part 1)`).
*   **Lines 125-130:** It loops through every single Answer Key file in the repository, targets the `<div class="block-header">`, and uses Regex to extract whatever broken title the AI generated.
*   **Lines 137-141:** It cross-references the extracted lesson number with our `lesson_num_to_title` dictionary, generates the correct answer string, and overwrites the DOM node!

### Review
You have successfully dissected `fix_book.py`. You now understand advanced Regex mutation, string grouping logic, and deep dependency synchronization using AST manipulation!
