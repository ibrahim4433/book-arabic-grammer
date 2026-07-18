import json
import re


def remove_tashkeel(text):
    tashkeel = re.compile(r"[\u0617-\u061A\u064B-\u0652\u0657-\u065F\u0670]")
    return re.sub(tashkeel, "", text)


with open("input/TOC.json", encoding="utf-8") as f:
    toc = json.load(f)

toc_titles = [v["title"] for k, v in toc.items()]

with open("system-workspace/text-data/full_raw_indexed.txt", encoding="utf-8") as f:
    lines = f.readlines()

print("TOC titles:")
for t in toc_titles:
    print(t)

print("\nHeadings found:")
for line in lines:
    if "]" in line and "#" in line:
        clean = remove_tashkeel(line)
        print(clean.strip())
