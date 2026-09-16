<!-- DYNAMIC INSTRUCTION FOR PART: exercises on the poem / تطبيقات القصيدة -->

CRITICAL STRUCTURAL BLUEPRINT FOR "EXERCISES ON THE POEM":
You MUST map this part exactly following this visual hierarchy:

1. MAIN CATEGORIES (مهارات الاستماع، مهارات القراءة، الاستيعاب والفهم والتحليل، إلخ):
You MUST use `TEMPLATE_C_BLOCK.html` (`.content-block`) to separate major categories:
- **Header**: Use `<div class="block-header">` and place the category title inside.
- **Body (`.block-body`)**: If the category contains a list of short questions and answers (e.g., true/false, multiple choice, short extraction), use `TEMPLATE_C_TABLE.html` (`<table class="dense-table w-full">`). 
  - Place the question in the first column (`<td class="font-bold w-30pct">`) and the answer in the second column (`<td>`).
- **Sub-Categories**: If a main category has a sub-category (e.g. المستوى الفكري), insert a `<p class="mt-1mm text-accent mb-0">` at the top of the `.block-body` before the table.

2. LONG-FORM QUESTIONS & ESSAYS (التعبير الكتابي، الأسئلة المقالية):
You MUST use `TEMPLATE_C_EXAM.html` (`.exam-question`) for questions that require a long paragraph or essay answer:
- Place the question text inside the `<p>` tag of `.exam-question`.
- For the answer, immediately follow the question `<p>` with an answer box using `TEMPLATE_C_BENEFIT.html` style: `<div class="benefit-box mt-1mm p-1mm bg-grey-lighter">`. Place the answer paragraph inside it with `<strong>الجواب:</strong>`.

3. LAYOUT OPTIMIZATION (THE ONE-PAGE LAW):
- To prevent A4 overflow, you MUST group smaller, related blocks (like two short tables or an exam question and a small table) horizontally using `TEMPLATE_C_SPLIT.html` (`<div class="split-grid">`).
- NEVER group non-sequential blocks side-by-side. Only logically adjacent items may be split this way.

4. GENERAL RULE:
- All content blocks, exam questions, and tables MUST have unique IDs (`id="bXXXXX"`).
- Maintain Arabic-Indic numbers (١, ٢, ٣...) for all numbered lists and questions.
