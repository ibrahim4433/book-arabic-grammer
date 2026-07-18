import os
import re

with open("all_content_edited.txt", encoding="utf-8") as f:
    content = f.read()

sections = re.split(r"={50}\nFile: ", content)
sections = sections[1:]  # Skip the first empty part before the first separator

# We'll build a mapping of index (0-70) to section content
# But wait, we need to add back the "File: " header or just the title.
# Let's clean the section content: it starts with filename, \nTitle: ..., \n={50}\n
# We can extract the title and the body.

parsed_sections = []
for sec in sections:
    lines = sec.split("\n")
    filename = lines[0].strip()
    title = lines[1].replace("Title: ", "").strip()
    body = "\n".join(lines[3:]).strip()  # Skip the '=======' line
    parsed_sections.append({"title": title, "body": body})

# Now let's define the new curriculum units and the section indices they map to (0-indexed).
# From titles.txt:
# 1-8 (0-7): Word, Ism, Fiil, Harf
# 9-10 (8-9): Mufrad, Muthanna, Jam
# 24-25 (23-24): Pronouns
# 11, 12, 13 (10, 11, 12): Irab steps, Jumal types
# 16, 17, 26, 27, 28 (15, 16, 25, 26, 27): Nominal sentence & Mubtada Advanced
# 18 (17): Faail
# 19, 20 (18, 19): Mafool Bihi
# 21, 22, 23 (20, 21, 22): Verbs Past, Present, Command
# 14, 15 (13, 14): Huroof Jarr
# 32, 33, 34, 35, 36 (31, 32, 33, 34, 35): Mansubat
# 38, 39 (37, 38): Munada
# 29, 30, 31 (28, 29, 30): Followers (Tawabia)
# 37 (36): Mamnou Sarf
# 40, 41, 42 (39, 40, 41): Irab Jumal
# 43 (42): Mizan Sarfi
# 44, 45, 46, 47, 48, 49, 50 (43-49): Sarf (I'lal, Ibdal, Mushtaq, Masadir)
# 51-62 (50-61): Imla
# 63-70 (62-69): Balagha
# 71 (70): Mu'jam

plan = [
    ("U01_The_Word", [0, 1, 2, 3, 4, 5, 6, 7]),
    ("U02_Numbers_and_Pronouns", [8, 9, 23, 24]),
    ("U03_Sentences_and_Irab", [10, 11, 12]),
    ("U04_Nominal_Sentence", [15, 16, 25, 26, 27]),
    ("U05_Verbal_Sentence_and_Verbs", [20, 21, 22, 17, 18, 19]),
    ("U06_Genitive_Huroof_Jarr", [13, 14]),
    ("U07_Accusatives_Mansubat", [31, 32, 33, 34, 35, 37, 38]),
    ("U08_Followers_Tawabia", [28, 29, 30]),
    ("U09_Advanced_Syntax", [36, 39, 40, 41]),
    ("U10_Morphology_Sarf", [42, 43, 44, 45, 46, 47, 48, 49]),
    ("U11_Spelling_Imla", [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]),
    ("U12_Rhetoric_Balagha", [62, 63, 64, 65, 66, 67, 68, 69]),
    ("U13_Dictionaries", [70]),
]

os.makedirs("C3_Lessons_Text", exist_ok=True)

with open("C3_Curriculum_Final_Plan.md", "w", encoding="utf-8") as plan_file:
    plan_file.write("# منهج المستوى الثالث (C3) - الخطة النهائية\n\n")

    for unit_name, indices in plan:
        plan_file.write(f"## {unit_name}\n")
        filename = f"C3_Lessons_Text/{unit_name}.txt"
        with open(filename, "w", encoding="utf-8") as out:
            for idx in indices:
                sec = parsed_sections[idx]
                plan_file.write(f"- {sec['title']}\n")
                out.write(f"=== {sec['title']} ===\n")
                out.write(sec["body"] + "\n\n")

print("Files generated successfully in C3_Lessons_Text/")
