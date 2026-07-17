import json

with open("block_titles.txt", "r", encoding="utf-8") as f:
    titles = f.readlines()

# Read the parsed_blocks from previous logic
import re
with open("all_content.txt", "r", encoding="utf-8") as f:
    text = f.read()

blocks = re.split(r'={50}\nFile: ', text)
parsed_blocks = []
for block in blocks:
    if not block.strip():
        continue
    parsed_blocks.append("==================================================\nFile: " + block.strip())

# Split 92 blocks into 8 chunks (approx 11-12 blocks each)
chunk_size = 12
for i in range(0, len(parsed_blocks), chunk_size):
    chunk_blocks = parsed_blocks[i:i+chunk_size]
    chunk_idx = i // chunk_size + 1
    with open(f"raw_chunk_{chunk_idx}.txt", "w", encoding="utf-8") as out:
        out.write("\n\n".join(chunk_blocks))

print("Created 8 chunks.")
