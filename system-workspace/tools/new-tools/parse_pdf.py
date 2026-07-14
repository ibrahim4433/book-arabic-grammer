import fitz
import re
import json

doc = fitz.open('output/export/book.pdf')
answers = []

for i, page in enumerate(doc):
    text = page.get_text("text")
    # PyMuPDF extracts Arabic text. It might be reversed or logical.
    # Let's just find the text "إجابات:" or its reversed form
    if "إجابات:" in text or "إِجَابَاتُ:" in text or ":تَابَاجِإ" in text or ":ُتَابَاجِإ" in text:
        # Instead of parsing the exact lesson, let's just dump the text of the page
        answers.append((i+1, text))

with open('pdf_text_dump.json', 'w', encoding='utf-8') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)
