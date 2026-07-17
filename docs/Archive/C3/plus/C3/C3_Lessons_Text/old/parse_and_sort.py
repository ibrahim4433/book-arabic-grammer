import re
from collections import defaultdict

with open("all_content.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split by file separator
blocks = re.split(r'={50}\nFile: ', text)

parsed_blocks = []
for block in blocks:
    if not block.strip():
        continue
    # block starts with filename
    lines = block.split('\n')
    filename = lines[0].strip()
    title = ""
    content_lines = []
    for i, line in enumerate(lines[1:]):
        if line.startswith("Title: "):
            title = line.replace("Title: ", "").strip()
        elif line.startswith("=" * 50):
            continue
        else:
            content_lines.append(line)
    
    content = "\n".join(content_lines).strip()
    parsed_blocks.append({"filename": filename, "title": title, "content": content})

# Now group them. We can just keep the original order but move C2 lessons next to their C1 counterparts if they exist.
# Or just print all titles to see them.
for i, b in enumerate(parsed_blocks):
    print(f"{i}: {b['title']}")

