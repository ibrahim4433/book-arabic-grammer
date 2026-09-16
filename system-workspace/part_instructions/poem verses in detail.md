<!-- DYNAMIC INSTRUCTION FOR PART: poem verses in detail / تحليل مفصل لمضمون الأبيات -->

CRITICAL STRUCTURAL BLUEPRINT FOR "POEM VERSES IN DETAIL":
You MUST map this part exactly following this visual hierarchy, treating each verse as an independent unit:

FOR EACH VERSE, FOLLOW THIS EXACT SEQUENCE:

1. THE VERSE (البيت الشعري):
You MUST start with `TEMPLATE_C_POEM.html` (`.poem-container`).
- Ensure the verse is cleanly split into right and left hemistichs (الشطر الأول والشطر الثاني) using the template placeholders.
- Center the text and make it bold (`text-center font-bold`).

2. THE DETAILED ANALYSIS (التحليل والإعراب):
Immediately beneath the `.poem-container`, you MUST use `TEMPLATE_C_SPLIT.html` (`<div class="split-grid">`) to create a two-column layout for the analysis:

- **Right Column (`w-50pct`)**: Place the Explanations & Rhetoric here.
  - Use `TEMPLATE_C_BLOCK.html` with `<div class="block-header bg-accent p-0 text-xs">`.
  - Title it "المفردات والشرح والبلاغة" (or appropriate title based on available content).
  - Inside the `.block-body`, use `TEMPLATE_C_LIST.html` (`<ul class="structured-list">`).
  - Use bold accent text for the sub-titles within the bullet points: `<span class="text-accent font-bold">المفردات:</span>`, `<span class="text-accent font-bold">الشرح:</span>`, `<span class="text-accent font-bold">الفكرة:</span>`, etc.

- **Left Column (`w-50pct`)**: Place the Parsing (الإعراب) here.
  - Use `TEMPLATE_C_BLOCK.html` with a standard `<div class="block-header p-0 text-xs">`.
  - Title it "الإعراب".
  - Inside the `.block-body`, use `TEMPLATE_C_LIST.html` (`<ul class="structured-list">`) to list the parsing of words and sentences for that specific verse.

3. GENERAL RULE:
- All blocks and grids MUST have unique IDs (`id="bXXXXX"`).
- Keep padding tight (`p-0`, `mb-1mm`) to fit the detailed analysis within the A4 page boundaries.
