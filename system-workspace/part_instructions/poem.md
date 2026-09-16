<!-- DYNAMIC INSTRUCTION FOR PART: poem -->

CRITICAL STRUCTURAL BLUEPRINT FOR POEMS:
You MUST map this part exactly following this visual hierarchy:

1. TOP SECTION (SPLIT GRID):
You MUST use `TEMPLATE_C_SPLIT.html` (`<div class="split-grid">`) to create a side-by-side layout that dynamically compacts blank space and balances column heights:
- **Right Column**: Place the Poet Bio here. If there is a picture, poet name, and info, put it here.
- **Left Column**: Place the "مدخل الى النص" (Introduction to the text) here.
- **Rule**: Do NOT use raw inline CSS or arbitrary width percentages. The `.split-grid` utility class from `main.css` will automatically handle the proportional width splitting and height matching you require.

2. BOTTOM SECTION (VERSES):
Underneath the split grid, you MUST use `TEMPLATE_C_POEM.html` (`.poem-container`) for the poem verses. 
- Ensure all verses are centered and cleanly split into right and left hemistichs using the template placeholders.
- CRITICAL: You MUST extract BOTH hemistichs (شطرين) for every single verse. DO NOT leave the first hemistich empty.
- If the source text is merged or poorly separated, you must intelligently split it based on poetic rhythm and meaning before outputting.
