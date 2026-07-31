import re

with open("pages/page_130_h4pom.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to split the page to fit.
# The layout tool said it recommended splitting at b1020 (poem-container).
# Wait, if I split, I need to create page_130_h4pom.html and page_130_h4pom_part2.html, but the task is specifically to generate `pages/page_130.html` (batch `pages/page_130_h4pom.html`).
# "When splitting an overflowing HTML page to satisfy the 1-page fit constraint using verify_layout.py, append the _part<N> suffix to the original filename before the extension"

# Let's see what is at b1020
print("Content to split around:")
match = re.search(r'id="b1020".*?id="b1021"', content, re.DOTALL)
if match:
    print(match.group(0))
