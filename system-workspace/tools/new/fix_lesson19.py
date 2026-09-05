import os
import glob

# HTML Shell template
html_shell_start = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>الهمزة المتطرفة</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>
"""
html_shell_end = """</body>
</html>
"""

files = ["pages/005.0_n013_الهمزة_المتطرفة.html", "pages/005.1_n014_الهمزة_المتطرفة.html"]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if "<!DOCTYPE html>" not in content:
            content = html_shell_start + content + html_shell_end
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Fixed missing shell in {filepath}")
        else:
            print(f"File {filepath} already has HTML shell.")
