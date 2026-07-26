import re

def fix_html():
    with open('pages/page_108_tbuuz.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find <p class="mt-1mm text-accent"> ... </p> that contain <div

    # Let's write a simple state machine to find and remove them
    lines = html.split('\n')
    new_lines = []
    in_p = False

    for line in lines:
        if '<p class="mt-1mm text-accent">' in line and '<div' in lines[lines.index(line)+1]:
            # This is a <p> wrapping a <div> block
            line = line.replace('<p class="mt-1mm text-accent">', '')
            in_p = True
        elif '</p>' in line and in_p:
            line = line.replace('</p>', '')
            in_p = False

        new_lines.append(line)

    html = '\n'.join(new_lines)

    # Handle the ones with text and <br> that we generated in the script
    # Oh wait, the script generated:
    # b = b.replace('[CONTENT]', irab_content)
    # And TEMPLATE_C_BLOCK has:
    # <p class="mt-1mm text-accent">
    #     [CONTENT]
    # </p>

    # Let's just remove the <p class="mt-1mm text-accent"> and </p> from blocks that have irab_content (which start with <div class="flex gap-2mm mb-1-5mm">)
    # Actually, we can use beautifulsoup to unwrap <divs> inside <p>s

    with open('pages/page_108_tbuuz.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    fix_html()
