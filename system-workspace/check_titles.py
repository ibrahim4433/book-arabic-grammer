"""
check_titles.py — Searches and normalizes titles found in TOC.json within full_raw_indexed.txt.

Usage:
    python system-workspace/check_titles.py
"""

import json
import re


def remove_tashkeel(text):
    tashkeel = re.compile(r"[\u0617-\u061A\u064B-\u0652\u0657-\u065F\u0670]")
    return re.sub(tashkeel, "", text)


with open("input/TOC.json", encoding="utf-8") as f:
    toc = json.load(f)

toc_titles = [v["title"] for k, v in toc.items()]
# To normalize titles
norm_titles = {remove_tashkeel(t): t for t in toc_titles}

with open("system-workspace/text-data/full_raw_indexed.txt", encoding="utf-8") as f:
    lines = f.readlines()

print("Searching for:")
for t in norm_titles:
    print(t)

print("\nMatches:")
for line in lines:
    clean_line = remove_tashkeel(line)
    for nt in norm_titles:
        if nt in clean_line:
            print(f"Found {nt} in: {line.strip()}")
