# Module 7: Real-World Scenarios & Hardcore Debugging

Welcome to the final module. You now understand the full architecture of this automated typesetting pipeline, from Python's string manipulation bridge to the mathematical constraints of the A4 layout engine.

In this module, you will face the final exam. These are three hardcore, real-world scenarios that happen frequently during automated AI generation. As the Senior Developer, you must know exactly how to interpret the logs, utilize the CLI tools, and execute surgical programmatic fixes.

---

## Beginner Primer: How to Read a Python Stack Trace

In this module, you are going to see error logs. When a Python script crashes, it spits out a massive, terrifying wall of red text called a "Stack Trace". 

Beginners often look at the top of the error, panic, and give up. **Never start at the top.**

Here is the secret to reading a Stack Trace:
1. **Scroll to the very bottom line.** This line will tell you exactly *what* broke (e.g., `FileNotFoundError: No such file or directory: 'pages/01.html'`).
2. **Look one paragraph up.** You will see a file path and a line number (e.g., `File "verify_layout.py", line 45`). 
3. **Ignore the rest.** The middle of the trace just shows the internal Python libraries that crashed as a result of your mistake. You only care about the bottom two pieces of information: What broke, and exactly what line of your code caused it!

---

## Scenario 1: The A4 Layout Overflow

### The Incident
You launch `python system.py` and trigger the "Audit & Verify Pages" operation. The system crunches through 150 pages silently until the terminal turns red and throws this exact trace:

```text
[FAIL] pages/12.2_n45_hal_types.html
[ERROR] OVERFLOW detected. Remaining height: -12.5 mm. 
[INFO] Overflow boundary breached at element ID: b93012
```

### The Diagnosis
The "1-Page Law" has been broken. The `verify_layout.py` script calculated that the bottom of element `b93012` sits 12.5 millimeters off the physical A4 page. 

### The Resolution
You **cannot** blindly open the HTML and delete content. This is a grammar textbook; every sentence matters.

**Step 1: Identify the Culprit**
Open `pages/12.2_n45_hal_types.html` and search for `id="b93012"`. You discover it is a massive `TEMPLATE_C_TABLE.html` showing 15 conjugations.

**Step 2: Choose the Splitting Strategy**
Since a table cannot easily be condensed by 12.5mm without breaking the font sizes, you must split the page logically.

**Step 3: Programmatic Execution**
1.  Copy `pages/12.2_n45_hal_types.html` and name the copy `pages/12.3_n45_hal_types_cont.html`.
2.  In `12.2`, delete the table (`b93012`) and everything beneath it.
3.  In `12.3`, delete the introduction paragraphs above the table.
4.  Update the header titles in both files to indicate "(الْجُزْءُ الْأَوَّلُ)" (Part 1) and "(الْجُزْءُ الثَّانِي)" (Part 2) using `fix_book.py` logic.

**Step 4: Re-Validation**
Run the verification script directly on both new files:
```bash
python Jules-workspace/verify_layout.py pages/12.2_n45_hal_types.html
python Jules-workspace/verify_layout.py pages/12.3_n45_hal_types_cont.html
```
If both return `Exit code: 0`, the crisis is resolved.

---

## Scenario 2: ID Collisions & DOM Corruption

### The Incident
You are running `python Jules-workspace/lint_pages.py --one-page-mode` to ensure all HTML matches the Atomic Design templates. The linter suddenly crashes:

```text
[CRITICAL FAIL] pages/03.1_n10_verbs.html
[LINT ERROR] Duplicate ID 'b48291' found on <div class="content-block"> and <table class="dense-table">.
[FATAL] ID Collisions will corrupt the verify_layout DOM tracking. Halting.
```

### The Diagnosis
During a manual edit or a flawed AI generation run, two HTML blocks were assigned the same unique identifier (`b48291`). Because `verify_layout.py` tracks Y-coordinates based on IDs, a collision completely corrupts the math.

### The Resolution
You must use the central ID manager to scrub and repair the file.

**Step 1: Verify the Collision Scope**
Check if this collision exists across the entire project or just in one file:
```bash
python Jules-workspace/id_manager.py verify
```
The output confirms `b48291` only collides inside `03.1_n10_verbs.html`.

**Step 2: Strip the Duplicate**
Open `pages/03.1_n10_verbs.html`. Find the second instance of `id="b48291"` (on the `<table class="dense-table">`) and completely delete the `id` attribute. Do not invent a new ID manually. 

**Step 3: Auto-Tag Regeneration**
Run the `id_manager.py` tool in `auto-tag` mode. This script uses `secrets.randbelow` to find any element missing an ID and securely generates a non-colliding `bXXXXX` tag.
```bash
python Jules-workspace/id_manager.py auto-tag
```

**Step 4: Confirm Clean Build**
Run the linter again:
```bash
python Jules-workspace/lint_pages.py --one-page-mode
```
It should now pass silently, confirming the DOM is perfectly healthy.

---

## Scenario 3: OCR Hallucinations & Missing Tashkeel

### The Incident
You are reviewing a newly generated PDF. On page 45, instead of a clean grammar rule, you see:

> *"Sure, I can help with that. Here is the transcription of the image:*  
> *ان الفاعل مرفوع بالضمة"*

### The Diagnosis
Two catastrophic failures occurred simultaneously:
1.  **Hallucination:** The AI ignored the `VisionClient` prompt and included conversational filler.
2.  **Missing Tashkeel:** The Arabic text `ان الفاعل مرفوع بالضمة` has zero diacritics, rendering it useless for a grammar book.

### The Resolution
You cannot fix this in HTML. The raw data source was corrupted. You must force the AI orchestrator to re-extract the image, but you don't want to rebuild the entire 200-page book.

**Step 1: Reset the State Manager**
The system remembers what it has already generated inside `project_state.json`. You must selectively erase the memory of Lesson 45.

Open `system-workspace/tools/automation/project_state.json` and find the entry for Lesson 45. Change its status from `"PASS"` to `"FAIL"`. Delete its artifact paths so the system thinks it never generated the HTML.

**Step 2: Engage Headless CLI Fallback**
Sometimes the REST API drifts into conversational modes due to server-side updates. We can force a retry using the highly deterministic `GeminiClient` Headless CLI mode, passing the strict prompt again.

Run the Orchestrator via `system.py`:
1. Select "1) book making by 1-lesson-1-plan method".
2. Select "G) Retry batch planning / generation to selected lessons".

Because you wiped Lesson 45 from `project_state.json`, the orchestrator will ONLY trigger the vision extraction for Lesson 45.

**Step 3: Verify Raw Output**
Before letting the system compile HTML, check the raw output in `system-workspace/raw_text/45.txt`. Ensure the conversational filler is gone and the Tashkeel is fully present (`إِنَّ الْفَاعِلَ مَرْفُوعٌ بِالضَّمَّةِ`).

---

### Conclusion

Congratulations. You have completed the curriculum. You now have a professional, deep, architectural understanding of how to maintain, debug, and scale an automated AI typesetting pipeline. 

You are no longer a junior developer in this repository. You are ready to take control of the Control Room.
