# Module 0: Python & HTML Fundamentals for this Repository

Welcome to the `book-arabic-grammer` project! Before we look at AI automation, massive deployment scripts, or complex orchestrators, we need to understand the absolute basics. 

If you are a junior developer looking at this repository for the first time, it might seem incredibly intimidating. There are dozens of folders, GitHub Actions, and complex terminal UIs. 

But take a deep breath. At its absolute core, this entire project relies on one incredibly simple concept: **Python reading text and putting it into HTML files.** 

If you understand how Python handles files, manipulates strings, and reads JSON, you will understand the foundation of everything else we build. 

In this module, we will explore exactly how Python acts as a bridge to generate HTML and CSS. We will not use any advanced tools, command-line interfaces, or complex libraries. We will stick strictly to the absolute beginner fundamentals.

---

## Beginner Primer: UTF-8 and Pathlib

Before we begin coding, let's look at two critical concepts you will see in almost every file in this project:

**1. What is `encoding="utf-8"`?**
Computers only understand numbers (0s and 1s), not letters. An "encoding" is the dictionary the computer uses to translate numbers back into letters. If you try to open an Arabic text file without explicitly telling Python to use the `utf-8` dictionary, Windows will often guess the wrong dictionary (like `cp1252`), resulting in garbage characters like `Ø§Ù„Ù Ø§Ø¹Ù„`. Always use `encoding="utf-8"` when handling Arabic text!

**2. What is `Pathlib`?**
In older Python tutorials, you might see paths written as strings: `"pages/01_lesson.html"`. But Windows uses backslashes (`\`) and Linux uses forward slashes (`/`). If you use strings, your code will crash if someone uses a different operating system. 
This project uses `pathlib.Path`. It automatically fixes the slashes for you!
```python
# From build.py
from pathlib import Path
# Path automatically handles the slashes whether you are on Mac, Linux, or Windows!
output_pdf: Path = Path("output/export/book.pdf")
```

---

## Lesson 1: Basic File Reading & Writing in Python

The most frequent action taken by the scripts in this repository is reading raw, diacritized (Tashkeel) Arabic text from an input file, formatting it, and saving it out as an HTML file. 

To do this, we use Python's built-in `open()` function. 

### Reading a File

Let's imagine we have a simple text file called `input/lesson_1.txt` that contains the following Arabic sentence:
> الْفَاعِلُ مَرْفُوعٌ دَائِمًا

Here is how we read that file using Python:

```python
# A simple script to read Arabic text
with open("input/lesson_1.txt", "r", encoding="utf-8") as file:
    raw_arabic_text = file.read()

print("The text we read is:", raw_arabic_text)
```

**Line-by-Line Breakdown:**
*   **`with open(...) as file:`**: This is called a "context manager". It is the safest way to open files in Python. Why? Because when the indented block of code finishes running, Python automatically closes the file for you. If you don't use `with`, and your script crashes, the file might remain "locked" by the operating system, which causes massive headaches when running automated pipelines.
*   **`"input/lesson_1.txt"`**: The relative path to the file we want to read.
*   **`"r"`**: This stands for **R**ead mode. We are telling Python that we only want to look at the file, not change it.
*   **`encoding="utf-8"`**: **CRITICAL RULE.** You will see this on almost every `open()` call in this repository. Arabic text, especially with heavy Harakat (diacritics), requires UTF-8 encoding. If you forget this, Python will try to read the file using your computer's default encoding (like ASCII or CP1252 on Windows), and the Arabic text will instantly turn into unreadable gibberish (e.g., `Ø§Ù„Ù Ø§Ø¹Ù„`).
*   **`file.read()`**: This method grabs the entire contents of the text file and saves it into our variable, `raw_arabic_text`.

### Writing to a File

Once we have our text (and perhaps after we've wrapped it in some HTML tags, which we'll cover soon), we need to save it.

```python
# A simple script to save text as an HTML file
my_html_content = "<h1>الْفَاعِلُ</h1>"

with open("pages/output.html", "w", encoding="utf-8") as file:
    file.write(my_html_content)
```

**Line-by-Line Breakdown:**
*   **`"pages/output.html"`**: The destination where we want to save our file. In this project, all final HTML files go into the `pages/` directory.
*   **`"w"`**: This stands for **W**rite mode. Be careful! Write mode will *completely overwrite* the file if it already exists. If the file doesn't exist, Python will create it.
*   **`file.write(my_html_content)`**: Instead of reading, we are pushing our string variable directly into the file.

---

## Lesson 2: Essential Python Imports Used in this Project

When you open the complex scripts in this repository, you will see a block of `import` statements at the top. While some are advanced, the core pipeline relies on three absolute standard Python libraries. Let's demystify them.

### 1. `import os`
The `os` (Operating System) module allows Python to interact with your computer's file system. 

When we try to save a file to the `pages/` directory (as we did in the example above), what happens if the `pages/` folder doesn't actually exist yet? Python will crash with a `FileNotFoundError`.

To prevent this, we use `os`:

```python
import os

# Ensure the destination directory exists before we try to write to it
os.makedirs("pages", exist_ok=True)

# Now it is perfectly safe to open and write the file
with open("pages/safe_output.html", "w", encoding="utf-8") as f:
    f.write("<p>Hello!</p>")
```
*   **`os.makedirs("pages")`**: Creates a folder named "pages".
*   **`exist_ok=True`**: This is a magic argument. It tells Python: "If the folder already exists, don't crash and don't throw an error. Just quietly move on." You will see this line everywhere in our build scripts.

### 2. `import json`
JSON (JavaScript Object Notation) is a lightweight format for storing data. In this repository, we don't hardcode rules inside our Python scripts; we store them in JSON files so they are easy to edit.

For example, look at the real file located at `Jules-workspace/design_patterns.json`. A portion of it looks like this:

```json
{
  "guidance": {
    "STYLING_RULES": {
      "highlight-red": "Use for Grammar Signs (Harakat/Endings)",
      "highlight-blue": "Use for Fixed Particles (Harf)",
      "text-accent": "Use for Definitions"
    }
  }
}
```

How does Python read this?

```python
import json

# 1. Open the JSON file exactly like a normal text file
with open("Jules-workspace/design_patterns.json", "r", encoding="utf-8") as f:
    # 2. Use json.load() to convert the text into a Python Dictionary
    patterns = json.load(f)

# 3. Access the data using dictionary keys!
definition_rule = patterns["guidance"]["STYLING_RULES"]["text-accent"]

print("The rule is:", definition_rule) 
# Terminal Output: The rule is: Use for Definitions
```
*   **`json.load(f)`**: This function does all the heavy lifting. It parses the raw text from the file and translates it into native Python dictionaries and lists. 

### 3. `import re` (Regular Expressions)
Sometimes, simple string searching isn't enough. We need to find complex patterns. This is where `re` comes in.

Imagine an AI agent accidentally generated a file with HTML tags, and we need to extract only the Arabic text inside the `<title>` tag.

```python
import re

bad_html_string = "<head><title>الْمُبْتَدَأُ وَالْخَبَرُ</title></head>"

# We want to find the exact text between <title> and </title>
# The (.*?) means "capture everything in between, but stop at the first closing tag"
match = re.search(r"<title>(.*?)</title>", bad_html_string)

if match:
    # match.group(1) returns the exact string captured by the parentheses (.*?)
    clean_title = match.group(1)
    print(clean_title) 
    # Terminal Output: الْمُبْتَدَأُ وَالْخَبَرُ
```
*   `re.search()` is heavily used in our repository to clean up AI outputs and extract specific data from HTML before rebuilding it.

---

## Lesson 3: The Python-to-HTML Bridge (The String Replacement Trick)

Now we reach the absolute core of the project's logic. **How does Python actually create a beautifully styled webpage?**

Does Python have magical HTML knowledge? No. 
Does Python construct the DOM tree? No.

Python uses an incredibly simple trick: **String Replacement**.

If you look inside the `Jules-workspace/Templates/` folder, you will find a file named `TEMPLATE_C_BASE.html`. This is the foundational shell for every single page in the book. It looks exactly like this:

```html
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>[PAGE_TITLE]</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
    <div class="force-new-page">
        <!-- Content components go here -->
    </div>
</body>
</html>
```

Look closely at line 5 (`[PAGE_TITLE]`) and line 10 (`<!-- Content components go here -->`). These are intentionally written placeholders.

When our Python script wants to build a grammar lesson, it does the following:

1.  It reads the `TEMPLATE_C_BASE.html` file into a string variable.
2.  It generates the Arabic content as another string.
3.  It uses the `.replace()` method to swap out the placeholders.

```python
# 1. Imagine we have loaded our template into a variable
base_template_string = """
<html>
    <title>[PAGE_TITLE]</title>
    <body><!-- Content components go here --></body>
</html>
"""

# 2. We define our dynamic data
lesson_name = "الْفَاعِلُ (The Subject)"
lesson_body_html = "<p>الْفَاعِلُ دَائِمًا مَرْفُوعٌ.</p>"

# 3. We use string replacement!
# First, we replace the title
step_1 = base_template_string.replace("[PAGE_TITLE]", lesson_name)

# Next, we replace the body placeholder with our actual HTML content
final_page_html = step_1.replace("<!-- Content components go here -->", lesson_body_html)

print(final_page_html)
```

The output of that print statement would be a perfectly formed HTML document:
```html
<html>
    <title>الْفَاعِلُ (The Subject)</title>
    <body><p>الْفَاعِلُ دَائِمًا مَرْفُوعٌ.</p></body>
</html>
```

This simple `.replace()` trick is the heartbeat of the entire `generate.py` pipeline. We take raw data, inject it into an atomic HTML template snippet, and then inject that snippet into the base template.

---

## Lesson 4: How CSS Gets Attached

A common question from beginners is: *"If Python is just mashing strings together, how does the page actually get styled?"*

The answer lies in understanding that Python doesn't "know" about CSS. Python is completely blind to it. 

Look back at line 6 of `TEMPLATE_C_BASE.html`:
```html
<link href="../styles/main.css" rel="stylesheet"/>
```

Because Python simply copies this template line for line, the resulting HTML file that is saved to the `pages/` directory will include that exact `<link>` tag. 

When you open `pages/10.0_lesson.html` in a web browser, it is the **Browser** (or WeasyPrint, our PDF engine) that reads that `<link>` tag, navigates up one directory (`../`), enters the `styles/` folder, and applies the `main.css` rules. 

Our Python script only has one job regarding styling: It must ensure that the strings it injects contain the correct `class="..."` attributes. 

For example, if the JSON configuration says definitions must use the `text-accent` class, Python simply formats the string like this:
```python
definition = "This is a grammar rule."
html_injection = f'<p class="text-accent">{definition}</p>'
```
When the browser loads that injected string, it matches the `class="text-accent"` to the `main.css` file automatically.

---

## Lesson 5: The 15-Line Mini Sandbox Script

Let's tie everything you've learned in this module into a single, fully functional script. 

This is a **Sandbox Script**. You can copy this code, save it as `sandbox.py` in the root of the repository, and run it via `python sandbox.py`. It will perform the entire lifecycle: reading a simulated JSON config, formatting the string, injecting it into an HTML template, and safely saving it to disk.

```python
import os
import json

# 1. Simulate reading our design_patterns.json config
# (We use json.loads here to read from a string instead of a file for the sandbox)
simulated_json = '{"lesson_title": "الْفَاعِلُ", "color_class": "text-accent"}'
config = json.loads(simulated_json)

# 2. Extract data from our dictionary
title = config["lesson_title"]
color = config["color_class"]

# 3. Format our specific content string (using f-strings)
dynamic_content = f'<h1 class="{color}">{title}</h1>'

# 4. Define our Base Template (Simulating reading TEMPLATE_C_BASE.html)
base_html = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head><link href="../styles/main.css" rel="stylesheet"/></head>
<body>
    <!-- Content components go here -->
</body>
</html>"""

# 5. The Python-to-HTML Bridge (String Replacement)
final_output = base_html.replace("<!-- Content components go here -->", dynamic_content)

# 6. Safe File I/O
os.makedirs("pages", exist_ok=True)
with open("pages/sandbox_lesson.html", "w", encoding="utf-8") as file:
    file.write(final_output)

print("✅ Success! Check the 'pages/' folder for sandbox_lesson.html")
```

### Review
If you understand the 15-line script above, you have mastered the foundational mechanics of this repository. 
*   You know how to safely read and write files with `utf-8`.
*   You know why we import `os`, `json`, and `re`.
*   You know that the complex HTML structure is achieved simply by replacing placeholders in base templates.

In **Module 1**, we will leave the sandbox and look at how this exact same logic is scaled up using loops and dataclasses to process thousands of words and generate a massive 200-page book.
