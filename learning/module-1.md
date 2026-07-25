# Module 1: Scaling Up to the Real Pipeline (Loops, Components & Data Structures)

Welcome to Module 1! In Module 0, we learned the absolute core mechanic of the `book-arabic-grammer` repository: **String Replacement**. We took a single string of Arabic text and injected it into a placeholder inside a Base HTML Template.

But if you look at any physical page of this Arabic Grammar book, you'll immediately see it is vastly more complex than a single sentence. A real page contains headers, multiple definition blocks, bulleted lists, dense conjugation tables, and colored I'rab (parsing) boxes. 

If we tried to use the simple method from Module 0, we would need 50 different placeholders (`[TITLE]`, `[PARAGRAPH_1]`, `[TABLE_ROW_1]`, etc.) in our base template. That would be an unmaintainable nightmare.

In this module, you will learn how the real pipeline elegantly scales up. We do this by combining **Data Structures** (to organize the raw text), **Component Snippets** (tiny, modular HTML templates), and **Python Loops** (to assemble them rapidly).

---

## Beginner Primer: Understanding Python Dataclasses

As a beginner, you might see `@dataclass` used frequently in this repository and wonder what it does. 

Normally, if you want to create a structured object in Python to hold data, you have to write a lot of boilerplate code using `__init__` functions. A `dataclass` is a built-in Python shortcut that does all this boring work for you automatically!

Here is a real example from the repository's main `build.py` script:

```python
# From build.py
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class BuildConfig:
    """Immutable build configuration."""
    pages_dir: Path = Path("pages")
    output_pdf: Path = Path("output/export/book.pdf")
    dry_run: bool = False
```

**What does this mean for a beginner?**
1. **`@dataclass`**: This tells Python, "Hey, just turn these variables into a nice, organized container automatically."
2. **`frozen=True`**: This acts as a security lock. It means once `BuildConfig` is created, nobody can accidentally change `dry_run = True` later in the code. It is "frozen" in place, preventing disastrous bugs during the PDF compilation process.

---

## Lesson 1: Beyond Simple Strings (Data Structures)

When the AI agents parse an image of an Arabic grammar textbook, they don't extract one massive block of text. They break the text down logically. 

To manage this logical breakdown in Python, we move away from simple string variables and start using structured data. In this repository, you will heavily see the use of **Dictionaries** and **Dataclasses**.

### Why Dataclasses?
If you look inside scripts like `Jules-workspace/lint_pages.py` or `Jules-workspace/id_manager.py`, you will see `@dataclass` used everywhere. Dataclasses are a clean, built-in Python feature that allows you to bundle data together logically without writing clunky object-oriented boilerplate code.

Let's imagine we are extracting a grammar rule. Instead of having separate variables...
```python
# The messy way (Do not do this)
rule_1_title = "الْفَاعِلُ"
rule_1_text = "هُوَ مَنْ قَامَ بِالْفِعْلِ"
rule_1_color = "text-accent"
```

...we create a blueprint for a `GrammarBlock`:

```python
from dataclasses import dataclass

@dataclass
class GrammarBlock:
    title: str
    content: str
    color_class: str

# Now we can cleanly instantiate our data
subject_rule = GrammarBlock(
    title="الْفَاعِلُ",
    content="هُوَ مَنْ قَامَ بِالْفِعْلِ",
    color_class="text-accent"
)

# We access the data cleanly using "dot" notation
print(subject_rule.title) # Output: الْفَاعِلُ
```

By organizing our Arabic text into lists of Dictionaries or Dataclasses, we prepare the data to be perfectly processed by Python loops.

---

## Lesson 2: The Atomic Design System (Component Snippets)

In the real repository, `TEMPLATE_C_BASE.html` is just the outer shell (the `<html>`, `<head>`, and `<body>` tags). It does *not* contain the HTML for the internal boxes, borders, and colored headers.

Instead, those elements live in tiny, separate files inside `Jules-workspace/Templates/`. We call these **Component Snippets**.

For example, a file named `TEMPLATE_C_BLOCK.html` looks like this:
```html
<section class="content-block">
    <div class="block-header">
        <span>[BLOCK_TITLE]</span>
    </div>
    <div class="block-body">
        <p class="[COLOR_CLASS]">[BLOCK_CONTENT]</p>
    </div>
</section>
```

### The Strategy: "String Concatenation"
Instead of injecting directly into the Base Template, the pipeline follows a two-step assembly process:
1.  **Snippet Filling:** We load the small `TEMPLATE_C_BLOCK.html` string into memory. We inject our data into it.
2.  **Concatenation (Adding it up):** We append (add) that filled snippet to a giant growing string called `html_body`. 
3.  **Final Injection:** Once all snippets are filled and added to `html_body`, we inject that massive string into `TEMPLATE_C_BASE.html`.

Let's look at this in code:

```python
# 1. Load the small component template
snippet_template = """
<div class="content-block">
    <h3>[BLOCK_TITLE]</h3>
    <p class="[COLOR_CLASS]">[BLOCK_CONTENT]</p>
</div>
"""

# 2. We have our data from Lesson 1 (subject_rule)
# 3. We create an empty string to hold our final page body
master_html_body = ""

# 4. We fill the snippet
filled_snippet = snippet_template.replace("[BLOCK_TITLE]", subject_rule.title)
filled_snippet = filled_snippet.replace("[COLOR_CLASS]", subject_rule.color_class)
filled_snippet = filled_snippet.replace("[BLOCK_CONTENT]", subject_rule.content)

# 5. We add the filled snippet to our master body!
master_html_body += filled_snippet 

# (We could repeat steps 4 and 5 dozens of times for different blocks)
```

---

## Lesson 3: Handling Repeated Structures (Loops in Action)

The magic of the Component Assembly strategy is that it allows us to use **Loops** to automatically generate repetitive HTML. 

Look at a conjugation table, a list of examples, or an exam section. They are just the exact same HTML structure repeated 5, 10, or 20 times with different Arabic text.

Let's simulate processing an Exam section. We have a list of exam questions stored as dictionaries. 

```python
# Our structured data (a list of dictionaries)
exam_questions = [
    {"number": "١", "text": "اسْتَخْرِجِ الْفَاعِلَ مِنَ الْجُمْلَةِ."},
    {"number": "٢", "text": "أَعْرِبْ مَا تَحْتَهُ خَطٌّ."},
    {"number": "٣", "text": "حَدِّدْ نَوْعَ الْفَاعِلِ."}
]

# Our small Exam Snippet template
exam_snippet = """
<div class="exam-question">
    <p><span class="exam-number">[NUM]</span> [QUESTION_TEXT]</p>
    <div class="border-light h-8mm bg-grey-lighter"></div>
</div>
"""

# The Master Body
exam_html_body = ""

# THE LOOP
for question in exam_questions:
    # 1. Take a fresh copy of the snippet template
    current_block = exam_snippet
    
    # 2. Replace the placeholders with the current loop's data
    current_block = current_block.replace("[NUM]", question["number"])
    current_block = current_block.replace("[QUESTION_TEXT]", question["text"])
    
    # 3. Append to the master body
    exam_html_body += current_block

print(exam_html_body)
```

When this loop runs, Python instantly generates the HTML for all three exam questions stacked perfectly on top of each other. The AI didn't have to write the HTML tags three times; it just provided the structured data, and Python did the heavy lifting.

---

## Lesson 4: The Multi-Component Sandbox Script

It's time to put it all together into a robust, runnable script. 

This Sandbox Script simulates the actual flow of `generate.py`. We will:
1. Define a list of structured data blocks (simulating data parsed by an AI).
2. Load a simulated Component Snippet.
3. Loop through our data, filling the snippet and appending it to a master body string.
4. Inject that massive master body string into a Base Template.
5. Save the final multi-block page to disk.

You can copy this, save it as `sandbox_loop.py` in the root directory, and run it.

```python
import os
from dataclasses import dataclass

# --- 1. DATA STRUCTURES ---
@dataclass
class ContentBlock:
    title: str
    content: str
    is_warning: bool = False

# Simulating data extracted by our AI pipeline
extracted_data = [
    ContentBlock(
        title="الْفَاعِلُ (The Subject)", 
        content="The subject is always in the Nominative case (مَرْفُوعٌ)."
    ),
    ContentBlock(
        title="تَحْذِيرٌ هَامٌّ (Important Warning)", 
        content="Do not confuse the Subject with the Object (الْمَفْعُولُ بِهِ).",
        is_warning=True
    ),
    ContentBlock(
        title="أَنْوَاعُ الْفَاعِلِ (Types of Subject)", 
        content="1. Explicit Noun (اسْمٌ ظَاهِرٌ)  2. Attached Pronoun (ضَمِيرٌ مُتَّصِلٌ)"
    )
]

# --- 2. TEMPLATES ---
# Simulated TEMPLATE_C_BASE.html
base_template = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8">
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
    <div class="force-new-page">
        <!-- ALL_CONTENT_GOES_HERE -->
    </div>
</body>
</html>
"""

# Simulated TEMPLATE_C_BLOCK.html
snippet_template = """
<section class="content-block [EXTRA_CLASS]">
    <div class="block-header">
        <span>[BLOCK_TITLE]</span>
    </div>
    <div class="block-body">
        <p>[BLOCK_CONTENT]</p>
    </div>
</section>
"""

# --- 3. COMPONENT ASSEMBLY (THE LOOP) ---
master_html_body = ""

for block_data in extracted_data:
    # Get a fresh copy of the snippet string for this loop iteration
    html_chunk = snippet_template
    
    # Handle conditional styling (Warning vs Normal block)
    if block_data.is_warning:
        html_chunk = html_chunk.replace("[EXTRA_CLASS]", "benefit-box warning")
    else:
        html_chunk = html_chunk.replace("[EXTRA_CLASS]", "")
        
    # Replace text content
    html_chunk = html_chunk.replace("[BLOCK_TITLE]", block_data.title)
    html_chunk = html_chunk.replace("[BLOCK_CONTENT]", block_data.content)
    
    # Append the completed HTML chunk to our massive master body string
    master_html_body += html_chunk

# --- 4. FINAL INJECTION & SAVING ---
# Inject the master string into the Base Template
final_page_html = base_template.replace("<!-- ALL_CONTENT_GOES_HERE -->", master_html_body)

# Save to disk
os.makedirs("pages", exist_ok=True)
output_path = "pages/sandbox_advanced.html"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(final_page_html)

print(f"✅ Success! Generated a complex multi-block page at {output_path}")
```

### Review
By mastering loops, dataclasses, and component appending, you have bypassed the need to manually write hundreds of lines of HTML. You are now manipulating the DOM programmatically using pure Python strings.

This is the exact mechanism running inside `Jules-workspace/generate.py`.

In **Module 2: The True Foundations & Entry Points**, we will finally look at how to properly start up the environment using `system.sh` and explore the massive folder architecture where all of these real scripts actually live.
