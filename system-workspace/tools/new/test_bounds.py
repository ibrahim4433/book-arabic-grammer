import re

def find_block_bounds(raw_html, tag_name, id_value):
    start_match = re.search(f'<{tag_name}[^>]*id=[\'"]{id_value}[\'"][^>]*>', raw_html)
    if not start_match: 
        # try matching class if id is not unique or present?
        # But this function requires id
        return None, None
    start_idx = start_match.start()
    
    idx = start_match.end()
    depth = 1
    
    tag_pattern = re.compile(f'</?{tag_name}(?:>|\s[^>]*>)')
    
    while depth > 0:
        match = tag_pattern.search(raw_html, idx)
        if not match:
            break
        tag_str = match.group(0)
        if tag_str.startswith("</"):
            depth -= 1
        elif not tag_str.endswith("/>"):
            depth += 1
        idx = match.end()
        
    return start_idx, idx

if __name__ == "__main__":
    with open("pages/044.0_n088_page_108.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # Let's test on id="b10805" which is a poem container
    start, end = find_block_bounds(html, "div", "b10805")
    if start:
        print("Found block!")
        print(html[start:end])
    else:
        print("Not found")
