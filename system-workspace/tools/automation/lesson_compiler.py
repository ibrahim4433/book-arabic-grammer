import re
import sys
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "assets/Templates"
PAGES_DIR = PROJECT_ROOT / "pages"
STYLES_DIR = PROJECT_ROOT / "styles"


def load_template(name):
    """Loads a template file from assets/Templates."""
    path = TEMPLATES_DIR / name
    if not path.exists():
        print(f"⚠️ Template not found: {name}")
        return ""
    return path.read_text(encoding="utf-8")


def parse_plan(plan_path):
    """Parses the markdown plan into a structured list of blocks."""
    content = Path(plan_path).read_text(encoding="utf-8")

    # Extract filename
    filename_match = re.search(r"File:\s*`?([^`\n]+)`?", content)
    filename = filename_match.group(1) if filename_match else "output.html"

    # Extract blocks
    blocks = []
    # Split by "=== BLOCK" markers
    parts = re.split(r"=== BLOCK \d+:? (.*?) ===", content)

    # Parts[0] is preamble, then we have title, content, title, content...
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        body = parts[i + 1].strip()

        # Extract Component Name
        comp_match = re.search(r"\(Component:\s*([\w_]+)\)", body)
        component = comp_match.group(1) if comp_match else "TEMPLATE_C_BLOCK"

        # Extract fields (Simple key-value parsing for now)
        fields = {}
        for line in body.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                fields[key.strip()] = val.strip()

        blocks.append({"type": title, "component": component, "fields": fields, "raw_body": body})

    return filename, blocks


def compile_page(filename, blocks):
    """Compiles the HTML page from blocks."""

    # Start with Base Template
    base_html = load_template("TEMPLATE_C_BASE.html")
    page_wrapper = load_template("TEMPLATE_C_PAGE_WRAPPER.html")

    body_content = ""

    for block in blocks:
        tpl_name = block["component"] + ".html"
        tpl_content = load_template(tpl_name)

        # Simple substitution logic
        # In a real engine, we'd use Jinja2, but here we do simple replace
        # based on standard markers in the templates.
        # Since templates aren't provided in full context, I'll assume standard placeholders
        # or just inject content loosely for now.

        # Heuristic: Inject fields into template
        filled_tpl = tpl_content
        for key, val in block["fields"].items():
            placeholder = f"[{key}]"
            filled_tpl = filled_tpl.replace(placeholder, val)

            # Try lowercase too
            placeholder_lower = f"[{key.lower()}]"
            filled_tpl = filled_tpl.replace(placeholder_lower, val)

        body_content += filled_tpl + "\n"

    # Wrap body
    full_body = page_wrapper.replace("<!-- CONTENT_GOES_HERE -->", body_content)

    # Inject into Base
    final_html = base_html.replace("<!-- BODY_CONTENT -->", full_body)

    # Save
    output_path = PAGES_DIR / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(final_html, encoding="utf-8")
    print(f"✅ Generated: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python lesson_compiler.py <plan_file>")
        return

    plan_file = sys.argv[1]
    filename, blocks = parse_plan(plan_file)
    compile_page(filename, blocks)


if __name__ == "__main__":
    main()
