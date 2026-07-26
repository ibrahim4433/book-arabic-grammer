import re
import sys
import subprocess

def get_new_ids(count):
    # Call id_manager.py count times to get new IDs
    ids = []
    for _ in range(count):
        result = subprocess.run(
            ['python3', 'Jules-workspace/id_manager.py', 'next-id'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            ids.append(result.stdout.strip())
        else:
            print("Failed to get ID", result.stderr)
    return ids

def fix_html():
    with open('pages/page_108_tbuuz.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove <div class="force-new-page"> wrapper
    html = re.sub(r'<div class="force-new-page">\s*', '', html)
    html = re.sub(r'\s*</div>\s*</body>', '\n</body>', html)

    # 2. Fix invalid nesting (remove <p> wrappers around divs and tables)
    # The <p class="mt-1mm text-accent"> tag wraps irab flex grids and tables in the generated html.
    # We can just remove the <p class="mt-1mm text-accent"> and </p> tags where they wrap flex grids or tables

    # We will do a generic replacement for <p ...> wrapping <div class="flex ..."> and </div> wrapping </p>
    # Also <p ...> wrapping <div class="block-body p-0"> and </div> wrapping </p>
    html = re.sub(r'<p class="mt-1mm text-accent">\s*(<div class="flex gap-2mm mb-1-5mm">.*?)\s*</p>', r'\1', html, flags=re.DOTALL)
    html = re.sub(r'<p class="mt-1mm text-accent">\s*(<div class="flex flex-col gap-2mm">.*?)\s*</p>', r'\1', html, flags=re.DOTALL)
    html = re.sub(r'<p class="mt-1mm text-accent">\s*(<div class="block-body p-0">.*?)\s*</p>', r'\1', html, flags=re.DOTALL)

    # Alternatively just use a clean up script
    # Let's write the file out and fix IDs

    # 3. Fix duplicate IDs
    # Find all ids
    id_matches = re.finditer(r'id="([^"]+)"', html)
    all_ids = [m.group(1) for m in id_matches]

    seen = set()
    duplicates = set()
    for id_val in all_ids:
        if id_val in seen:
            duplicates.add(id_val)
        seen.add(id_val)

    print(f"Found {len(duplicates)} duplicate IDs")

    # Replace duplicates
    new_ids = get_new_ids(len(all_ids))

    # We will replace all IDs to be safe
    def replace_id(match):
        return f'id="{new_ids.pop(0)}"'

    html = re.sub(r'id="([^"]+)"', replace_id, html)

    with open('pages/page_108_tbuuz.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_html()
