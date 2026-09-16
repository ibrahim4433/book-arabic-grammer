<!-- DYNAMIC INSTRUCTION FOR PART: poem verses in detail - اعراب النص / إعراب مقاطع النص -->

CRITICAL STRUCTURAL BLUEPRINT FOR "POEM VERSES I'RAB (SECTIONS)":
You MUST map this part exactly following this visual hierarchy. This is strictly for the syntax parsing (الإعراب) of the poem, divided by sections (المقاطع), without other detailed analysis sub-parts.

FOR EACH SECTION (المقطع), FOLLOW THIS EXACT SEQUENCE:

1. SECTION HEADER AND I'RAB BODY:
You MUST use `TEMPLATE_C_BLOCK.html` (`.content-block`) to house the parsing details for the entire section:
- **Header**: Use `<div class="block-header">` and place the section title inside (e.g., <span>إعراب المقطع الأول</span>).
- **Body**: Inside the `.block-body p-1mm`, use `TEMPLATE_C_LIST.html` (`<ul class="structured-list">`) to list the parsing (الإعراب) of the vocabulary and sentences within that section.
- Highlight the parsed word/sentence at the start of the bullet point using `<span class="text-accent font-bold">...</span>`.

2. OPTIONAL SIDE-BY-SIDE VIEW (If space permits):
If the section is short and you need to save vertical space, you MAY use `TEMPLATE_C_SPLIT.html` (`<div class="split-grid">`):
- **Right Column (`w-50pct`)**: Place the verses of the section using `TEMPLATE_C_POEM.html`.
- **Left Column (`w-50pct`)**: Place the `TEMPLATE_C_BLOCK` containing the I'rab list.
*(Only use this split if it logically fits the A4 page layout without causing text squishing).*

3. GENERAL RULE:
- All content blocks MUST have unique IDs (`id="bXXXXX"`).
- Ensure 100% accurate reproduction of Arabic Harakat in the I'rab text.
