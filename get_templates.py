import os
import glob

print("Templates available:")
for filepath in glob.glob("Jules-workspace/Templates/*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        print(f"\n--- {os.path.basename(filepath)} ---")
        print(f.read())
