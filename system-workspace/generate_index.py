"""
generate_index.py — Generates an index map with raw file markers and titles from full_raw_indexed.txt.

Usage:
    python system-workspace/generate_index.py
"""

import json
import re


def remove_tashkeel(text):
    tashkeel = re.compile(r"[\u0617-\u061A\u064B-\u0652\u0657-\u065F\u0670]")
    return re.sub(tashkeel, "", text)


with open("system-workspace/text-data/full_raw_indexed.txt", encoding="utf-8") as f:
    lines = f.readlines()

headings = []
for idx, line in enumerate(lines):
    if line.split("]")[1].strip().startswith("# "):
        # Extract raw file marker
        marker = line.split("]")[0].replace("[", "")
        # Extract title
        title = remove_tashkeel(line.split("]")[1].replace("# ", "").strip())
        headings.append({"title": title, "start": marker, "start_idx": idx})

for i in range(len(headings)):
    if i < len(headings) - 1:
        # End is the line before the next heading
        end_idx = headings[i + 1]["start_idx"] - 1
        end_marker = lines[end_idx].split("]")[0].replace("[", "")
        headings[i]["end"] = end_marker
    else:
        # Last heading
        end_idx = len(lines) - 1
        end_marker = lines[end_idx].split("]")[0].replace("[", "")
        headings[i]["end"] = end_marker

output = {}
for idx, h in enumerate(headings, 1):
    output[f"{idx} - {h['title']}"] = {"start": h["start"], "end": h["end"]}

print(json.dumps(output, ensure_ascii=False, indent=2))
