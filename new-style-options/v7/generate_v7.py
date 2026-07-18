import re

# Read original
with open(
    "C:/Users/ibrah/Documents/GitHub/book-arabic-grammer/styles/main.css", encoding="utf-8"
) as f:
    content = f.read()

# Replace variables
content = re.sub(r"--color-primary:\s*#[0-9A-Fa-f]+;", "--color-primary: #34495E;", content)
content = re.sub(r"--color-accent:\s*#[0-9A-Fa-f]+;", "--color-accent: #F1948A;", content)
content = re.sub(r"--color-dark:\s*#[0-9A-Fa-f]+;", "--color-dark: #2C3E50;", content)
content = re.sub(r"--color-light:\s*#[0-9A-Fa-f]+;", "--color-light: #E5E7E9;", content)

# Replace background image
content = content.replace("url('../assets/page-background/background.png')", "url('../v7.png')")


# Replace font-weights
def replace_font_weight(match):
    val = match.group(1)
    if val == "900":
        return "font-weight: 900"
    return "font-weight: 700"


content = re.sub(r"font-weight:\s*(normal|bold|\d+)", replace_font_weight, content)

# Ensure target directory exists (v7)
import os

os.makedirs(
    "C:/Users/ibrah/Documents/GitHub/book-arabic-grammer/new-style-options/v7", exist_ok=True
)

# Write to target
with open(
    "C:/Users/ibrah/Documents/GitHub/book-arabic-grammer/new-style-options/v7/main.css",
    "w",
    encoding="utf-8",
) as f:
    f.write(content)
