import os

files_to_check = [114, 115, 123, 127, 134, 151, 161, 163, 170, 183, 185, 189, 200, 210, 215, 219, 222, 226, 227, 230, 237, 240, 256, 260]
pages_dir = 'pages'
all_files = os.listdir(pages_dir)

for num in files_to_check:
    matching_files = [f for f in all_files if f.startswith(f'page_{num}') and f.endswith('.html')]
    for match in matching_files:
        path = os.path.join(pages_dir, match)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_doctype = '<!DOCTYPE html>' in content
        has_css_link = 'styles/main.css' in content
        has_head = '<head>' in content
        
        if not has_doctype:
            # Wrap content in the DOCTYPE shell
            new_content = f"""<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="utf-8"/>
<title>page {num}</title>
<link href="../styles/main.css" rel="stylesheet"/>
</head>
<body class="p-0 m-0">
{content}
</body>
</html>
"""
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Wrapped {match} in HTML shell.")
            
        elif not has_css_link:
            # Inject CSS link into <head>
            # Find the closing </head> and insert before it
            if '</head>' in content:
                new_content = content.replace('</head>', '<link href="../styles/main.css" rel="stylesheet"/>\n</head>')
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Injected CSS link into {match}.")
            else:
                print(f"Error: No </head> found in {match} despite having DOCTYPE.")
