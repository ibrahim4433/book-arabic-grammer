"""
lint_autofixer.py — Auto-fixer for common HTML class violations.

Usage:
    python Jules-workspace/lint_autofixer.py
"""

import os
import re
import subprocess


def run_linter():
    print("Running lint_pages.py...")
    result = subprocess.run(
        ["python3", "Jules-workspace/lint_pages.py"], capture_output=True, text=True
    )
    return result.stdout


def autofix():
    print("Analyzing linter output for common auto-fixable errors...")

    # 1. Map common bad classes to good classes
    bad_classes_map = {
        "border-dashed": "border-light",
        "border-2": "border-light",
        "chips-container": "flex flex-wrap gap-2mm",
        "gap-4mm": "gap-2mm",
        "border-blue": "border-light",
        "border-green": "border-light",
        "border-red": "border-light",
        "text-large": "font-bold",
        "text-red": "highlight-red",
        "mt-2": "mt-2mm",
        "p-3mm": "p-2mm",
    }

    pages_dir = "pages"
    fixed_files = 0

    for root, _, files in os.walk(pages_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, encoding="utf-8") as f:
                    content = f.read()

                original = content

                # Fix classes
                for bad, good in bad_classes_map.items():
                    pattern = r"(?<![\w-])" + re.escape(bad) + r"(?![\w-])"
                    content = re.sub(pattern, good, content)

                # Fix <hr> tags (remove them per design rules)
                content = re.sub(r"<hr\s*\/?>", "", content, flags=re.IGNORECASE)

                if content != original:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"🔧 Auto-fixed: {filepath}")
                    fixed_files += 1

    print(f"\n✅ Auto-fix complete. Modified {fixed_files} files.")

    print("\nRunning linter again to verify fixes...")
    subprocess.run(["python3", "Jules-workspace/lint_pages.py"])


if __name__ == "__main__":
    autofix()
