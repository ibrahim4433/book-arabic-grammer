<!-- DYNAMIC INSTRUCTION FOR PART: reading lesson / مطالعة -->

CRITICAL STRUCTURAL BLUEPRINT FOR "READING LESSON":
You MUST map this part exactly following this visual hierarchy to ensure the reading text and associated questions flow logically:

1. TOP SECTION (HEADER & AUTHOR INFO):
You MUST use `TEMPLATE_C_SPLIT.html` (`<div class="split-grid">`) to create a side-by-side introduction:
- **Right Column (`w-50pct`)**: Place the Author's Biography (معلومات عن الكاتب). Use `TEMPLATE_C_BLOCK.html` (or `TEMPLATE_C_POET_BIO.html` if available/appropriate).
- **Left Column (`w-50pct`)**: Place the Introduction to the lesson (مدخل إلى النص). Use `TEMPLATE_C_BLOCK.html`.

2. THE READING CONTENT (المقاطع القرائية):
Underneath the split grid, map the main reading text section by section (مقطع مقطع):
- For each section, use `TEMPLATE_C_BLOCK.html` (`.content-block`).
- **Header**: Use `<div class="block-header">` to indicate the section (e.g., <span>المقطع الأول</span>).
- **Body**: Place the reading text inside paragraph tags `<p class="mt-1mm text-accent mb-0">` within the `.block-body`.

3. EXERCISES & QUESTIONS (الأسئلة المقترحة للمقاطع):
Following the reading content blocks, map the questions related to the sections:
- You MUST use the same structure defined in "exercises on the poem":
  - Use `TEMPLATE_C_BLOCK.html` for category headers (e.g., <span>أسئلة وأجوبة المقطع الأول</span>).
  - Inside the `.block-body`, use `TEMPLATE_C_TABLE.html` (`<table class="dense-table w-full">`) to list the Q&A pairs (Question in the first bold column, Answer in the second).
  - For long-form questions, use `TEMPLATE_C_EXAM.html` (`.exam-question`) followed by a `.benefit-box.bg-grey-lighter` for the answer.

4. GENERAL RULE:
- All content blocks, exam questions, and tables MUST have unique IDs (`id="bXXXXX"`).
- Maintain Arabic-Indic numbers (١, ٢, ٣...) for numbered lists and sections.
