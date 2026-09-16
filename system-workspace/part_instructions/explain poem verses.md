<!-- DYNAMIC INSTRUCTION FOR PART: explain poem verses / شرح مقاطع القصيدة -->

CRITICAL STRUCTURAL BLUEPRINT FOR "EXPLAIN POEM VERSES":
You MUST map this part exactly following this visual hierarchy:

1. VOCABULARY EXPLANATION (شرح المفردات الصعبة):
You MUST use `TEMPLATE_C_BLOCK.html` (`.content-block`) to display the vocabulary:
- **Header**: Use `<div class="block-header bg-accent">` and place the title (e.g., <span>شرح المفردات الصعبة</span>) inside.
- **Body**: Inside the `.block-body p-2mm`, use `TEMPLATE_C_LIST.html` (`<ul class="structured-list">`) with `<span class="marker">•</span>` for each word and its meaning.

2. SECTIONS EXPLANATION (شرح مقاطع النص):
You MUST use `TEMPLATE_C_BLOCK.html` (`.content-block`) to display the paragraph explanations:
- **Header**: Use `<div class="block-header accent">` and place the title (e.g., <span>شرح مقاطع النص</span>) inside.
- **Body**: Inside the `.block-body p-2mm`, map each section's explanation to a paragraph tag: `<p class="m-0 mt-2mm text-sm text-accent">`.
- **Formatting**: Bold the section title at the start of the paragraph using `<strong>` (e.g., `<strong>شرح المقطع الأول:</strong>`). 
- **Rule**: Do NOT use `TEMPLATE_C_LIST` for the section explanations; they must be flowing paragraphs (`<p>`).

3. GENERAL RULE:
- All content blocks MUST have unique IDs (`id="bXXXXX"`).
- Preserve all Arabic Harakat perfectly.
