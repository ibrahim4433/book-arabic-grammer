import re
import os
import ast
import random
import string

PLAN_FILE = "plans/11-الإبدال-plan.md"
OUTPUT_FILE = "pages/11.0_nXX_الإبدال.html"
TEMPLATE_DIR = "Jules-workspace/Templates"

def load_template(name):
    path = os.path.join(TEMPLATE_DIR, name)
    if not os.path.exists(path):
        # Fallback to appending .html if missing
        if not name.endswith(".html"):
            path += ".html"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generate_id(prefix="b"):
    return prefix + ''.join(random.choices(string.digits, k=5))

def parse_plan(plan_text):
    blocks = []

    # Extract Content Stream
    stream_match = re.search(r'--- START STREAM ---(.*?)--- END STREAM ---', plan_text, re.DOTALL)
    if not stream_match:
        print("No stream found")
        return []

    stream_content = stream_match.group(1)

    # Split by blocks
    # Look for "=== BLOCK"
    # We can split by regex
    parts = re.split(r'(=== BLOCK \d+:.*?===)', stream_content)

    current_block = {}

    for part in parts:
        part = part.strip()
        if not part: continue

        if part.startswith("=== BLOCK"):
            # New block
            # Extract title if needed, but mainly we wait for the next part which is content
            pass
        else:
            # This is the content body
            # Extract Component
            comp_match = re.match(r'\(Component: (TEMPLATE_C_.*?)\)', part)
            if not comp_match:
                continue

            component = comp_match.group(1)
            content_body = part[comp_match.end():].strip()

            data = {"_component": component}

            if component == "TEMPLATE_C_HEADER":
                # Parse [KEY]: Value
                for line in content_body.split('\n'):
                    m = re.match(r'\[(.*?)]: (.*)', line)
                    if m:
                        data[m.group(1)] = m.group(2).strip()

            elif component == "TEMPLATE_C_BLOCK":
                # Title: ... Content: ...
                m_title = re.search(r'^Title: (.*)', content_body, re.MULTILINE)
                if m_title:
                    data['BLOCK_TITLE'] = m_title.group(1).strip()

                # Content: ... (rest of text)
                # We need to capture from "Content:" to end or next key?
                # In Block, Content is usually last.
                # But be careful if I added Benefit keys later.
                # Assuming Content is everything after "Content:"
                m_content = re.search(r'Content:\s*(.*)', content_body, re.DOTALL)
                if m_content:
                    data['CONTENT_TEXT'] = m_content.group(1).strip()
                else:
                    print(f"Warning: Content not found for block {component}")
                    print(f"Body: {content_body[:50]}...")

            elif component == "TEMPLATE_C_SPLIT":
                # [LEFT_TITLE], [LEFT_CONTENT], etc.
                keys = ["LEFT_TITLE", "LEFT_CONTENT", "RIGHT_TITLE", "RIGHT_CONTENT"]
                for k in keys:
                    # Regex to capture content between keys
                    # We look for [KEY]:
                    # And capture until the next [KEY]: or end
                    # Construct a regex that matches specific key
                    pattern = re.compile(rf'\[{k}\]:\s*(.*?)(?=\n\[[A-Z_]+\]:|$)', re.DOTALL)
                    m = pattern.search(content_body)
                    if m:
                        data[k] = m.group(1).strip()

            elif component == "TEMPLATE_C_TABLE":
                m_title = re.search(r'^Title: (.*)', content_body, re.MULTILINE)
                if m_title:
                    data['TABLE_TITLE'] = m_title.group(1).strip()

                m_cols = re.search(r'^Columns: \[(.*)\]', content_body, re.MULTILINE)
                if m_cols:
                    cols = [c.strip().strip('"\'') for c in m_cols.group(1).split(',')]
                    data['TABLE_HEADERS'] = "".join([f"<th>{c}</th>" for c in cols])

                m_rows = re.search(r'^Rows:\s*\[(.*)\]', content_body, re.DOTALL | re.MULTILINE)
                if m_rows:
                    try:
                        rows_str = m_rows.group(1).strip()
                        # Use ast.literal_eval for safe parsing of python list syntax
                        # Wrap in brackets to make it a list of lists if it isn't already (it is [ ... ] in text so it's a list)
                        # Wait, text has "Rows: [\n [..], [..] \n]"
                        # So rows_str is "[..], [..]"? Or does it include outer brackets?
                        # Regex `\[(.*)\]` captures everything inside outermost brackets?
                        # `re.DOTALL` makes . match newlines.
                        # `r'^Rows:\s*\[(.*)\]'` matches `Rows: [...]`. Group 1 is inside.
                        # So `rows_str` is `["col", "col"], ["col", "col"]`
                        # We need to wrap it in `[]` to evaluate as list of lists.
                        rows = ast.literal_eval(f"[{rows_str}]")
                        rows_html = ""
                        for row in rows:
                            rows_html += "<tr>"
                            for cell in row:
                                rows_html += f"<td>{cell}</td>"
                            rows_html += "</tr>"
                        data['TABLE_ROWS'] = rows_html
                    except Exception as e:
                        print(f"Error parsing rows in {component}: {e}")

            elif component == "TEMPLATE_C_EXAM":
                m_q = re.search(r'Question: (.*)', content_body, re.DOTALL)
                if m_q:
                    data['QUESTION_TEXT'] = m_q.group(1).strip()
                    data['TOPIC'] = "الإبدال"

            blocks.append(data)

    return blocks

def process_template(tpl, data):
    # Replace simple keys
    for k, v in data.items():
        if k.startswith("_"): continue
        tpl = tpl.replace(f"[{k}]", str(v))

    comp = data.get("_component")

    # Special Logic
    if comp == "TEMPLATE_C_BLOCK":
        if "[BENEFIT_TITLE]" in tpl and "BENEFIT_TITLE" not in data:
            # Remove benefit box
             tpl = re.sub(r'<div class="benefit-box">.*?</div>', '', tpl, flags=re.DOTALL)

    if comp == "TEMPLATE_C_EXAM":
        # Remove Q2 if unused
        # We assume only 1 question for now based on plan
        if "[Q2_ID]" in tpl:
             # Regex to find the Q2 block.
             # It starts with <!-- Question 2
             # Ends with </div> (closing exam-question)
             # This is risky with regex.
             # Template:
             # <!-- Question 2 ... -->
             # <div class="exam-question ..."> ... </div>

             # Better: Split by "<!-- Question 2" and keep the first part?
             # But we need the closing </div> of the section?
             # Let's just replace the specific Q2 block string if I can match it.
             # Or just hide it with CSS? No, generate clean HTML.

             parts = tpl.split("<!-- Question 2")
             if len(parts) > 1:
                 # Reconstruct: Part 0 + closing logic
                 # Part 0 ends after Q1.
                 # The Template ends with </div> (body) </div> (section)
                 # We need to close the block-body and section.
                 # Part 0 usually contains open tags.
                 # Let's inspect Template C_EXAM again.
                 # It ends with: </div> </section>
                 # Q2 is the last item.
                 # So we can just cut off Q2 and append closing tags.
                 # Be careful not to cut off Q1 closing tags.
                 # Q1 ends with </div>.
                 # So we look for the last </div> before Question 2?

                 # Simplest: Regex replace the Q2 div.
                 tpl = re.sub(r'<!-- Question 2.*?<div class="exam-question.*?</div>', '', tpl, flags=re.DOTALL)

        # Generate IDs
        tpl = tpl.replace("[BLOCK_ID]", generate_id())
        tpl = tpl.replace("[Q1_ID]", generate_id("q"))
        tpl = tpl.replace("[Q2_ID]", generate_id("q")) # If still there

    # Generic ID injection if needed (the plan says "Unique IDs... use id_manager")
    # But I can generate them now.

    return tpl

def main():
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        plan_text = f.read()

    blocks = parse_plan(plan_text)

    base = load_template("TEMPLATE_C_BASE.html")

    html_content = ""
    for block in blocks:
        tpl = load_template(block["_component"] + ".html")
        processed = process_template(tpl, block)
        html_content += processed + "\n"

    final_html = base.replace("<!-- INJECT_CONTENT_HERE -->", html_content)

    # Ensure pages dir exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Generated {OUTPUT_FILE} with {len(blocks)} blocks.")

if __name__ == "__main__":
    main()
