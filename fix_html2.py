import re
import os

def fix_html():
    with open('pages/page_108_tbuuz.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The previous regex might not have caught all <p> wrapping <div> because of nested <div>s.
    # We can just manually clean it up by replacing the specific bad patterns.
    html = html.replace('<p class="mt-1mm text-accent">\n            <div class="flex', '<div class="flex')
    html = html.replace('</div>\n        </p>', '</div>')

    # Check if there are still any block elements inside <p>
    if re.search(r'<p[^>]*>.*?(<div|<table)', html, re.DOTALL):
        print("Still found block elements inside <p>")
        # Let's fix them manually
        html = re.sub(r'<p class="mt-1mm text-accent">\s*(<div.*?)</div>\s*</p>', r'\1</div>', html, flags=re.DOTALL)

    with open('pages/page_108_tbuuz.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_html()
