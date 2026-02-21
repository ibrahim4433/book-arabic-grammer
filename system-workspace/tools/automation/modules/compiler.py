import sys
import json
import re
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient
from jules_client import JulesClient

class Compiler:
    """
    Compiles Architect Plans into HTML pages using a mapping schema.
    Can also dispatch plans to Jules for execution.
    """
    
    def __init__(self, project_root=None, api_key=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.templates_dir = self.project_root / "assets/Templates"
        self.mappings_path = self.project_root / "system-workspace/tools/automation/mappings/plan_to_template.json"
        self.pages_dir = self.project_root / "pages"
        
        self.jules_client = JulesClient(api_key, self.project_root)
        
        # Load Mappings
        if self.mappings_path.exists():
            self.mappings = json.loads(self.mappings_path.read_text(encoding='utf-8'))
        else:
            print(f"⚠️ Mapping file not found: {self.mappings_path}")
            self.mappings = {}

    def parse_plan(self, plan_content):
        """
        Parses the markdown plan into a structured list of blocks.
        Handles multi-line content robustly.
        """
        # Extract filename
        filename_match = re.search(r"File:\s*`?([^`\n]+)`?", plan_content)
        filename = filename_match.group(1) if filename_match else "output.html"
        
        blocks = []
        # Split by "=== BLOCK" markers
        parts = re.split(r"=== BLOCK \d+:? (.*?) ===", plan_content)
        
        # Parts[0] is preamble
        for i in range(1, len(parts), 2):
            block_title = parts[i].strip() # e.g., "Header" or "Definition"
            body = parts[i+1].strip()
            
            # Extract Component Name
            comp_match = re.search(r"\(Component:\s*([\w_]+)\)", body)
            component = comp_match.group(1) if comp_match else "TEMPLATE_C_BLOCK"
            
            # Parse Fields
            fields = {}
            current_key = None
            current_value = []
            
            lines = body.splitlines()
            for line in lines:
                # Check for Key: Value pattern at start of line
                # We assume keys are Title case words followed by colon
                key_match = re.match(r"^([A-Z][a-zA-Z ]+):\s*(.*)", line)
                
                if key_match and "Component:" not in line:
                    # Save previous key if exists
                    if current_key:
                        fields[current_key] = "\n".join(current_value).strip()
                    
                    current_key = key_match.group(1).strip()
                    current_value = [key_match.group(2).strip()]
                else:
                    # Continuation of previous key or unkeyed text
                    if current_key:
                        current_value.append(line)
            
            # Save last key
            if current_key:
                fields[current_key] = "\n".join(current_value).strip()
            
            blocks.append({
                "type": block_title,
                "component": component,
                "fields": fields
            })
            
        return filename, blocks

    def compile_page(self, plan_path):
        """
        Compiles a plan file into HTML.
        """
        plan_path = Path(plan_path)
        if not plan_path.exists():
            print(f"❌ Plan not found: {plan_path}")
            return None
            
        content = plan_path.read_text(encoding='utf-8')
        filename, blocks = self.parse_plan(content)
        
        body_content = ""
        
        for block in blocks:
            comp_name = block["component"]
            tpl_path = self.templates_dir / (comp_name + ".html")
            
            if not tpl_path.exists():
                print(f"⚠️ Template not found: {comp_name}")
                continue
                
            tpl_content = tpl_path.read_text(encoding='utf-8')
            filled_tpl = tpl_content
            
            # Get Mapping for this component
            comp_mapping = self.mappings.get(comp_name, {})
            
            # 1. Apply Default Values
            defaults = comp_mapping.get("default_values", {})
            for ph, val in defaults.items():
                filled_tpl = filled_tpl.replace(ph, val)
                
            # 2. Apply Field Mappings
            for field_name, field_value in block["fields"].items():
                # Check if field is mapped
                mapping_entry = comp_mapping.get(field_name)
                
                if not mapping_entry:
                    # Try direct placeholder match as fallback
                    # e.g. "Title" -> "[TITLE]"
                    placeholder = f"[{field_name.upper()}]"
                    filled_tpl = filled_tpl.replace(placeholder, field_value)
                    continue
                
                if isinstance(mapping_entry, str):
                    # Direct String Replacement
                    filled_tpl = filled_tpl.replace(mapping_entry, field_value)
                    
                elif isinstance(mapping_entry, dict):
                    # Transformation needed
                    target = mapping_entry.get("target")
                    transform = mapping_entry.get("transform")
                    
                    if transform == "markdown_to_html_table":
                        # TODO: Implement robust markdown table parser
                        # For now, placeholder or simple replacement
                        # A real implementation would parse | headers | and | rows |
                        filled_tpl = self._transform_table(filled_tpl, field_value)
                    elif transform == "markdown_list_to_html":
                        html_list = self._transform_list(field_value)
                        filled_tpl = filled_tpl.replace(target, html_list)

            body_content += filled_tpl + "\n"
            
        # Wrap in Base Template
        base_tpl = (self.templates_dir / "TEMPLATE_C_BASE.html").read_text(encoding='utf-8')
        wrapper_tpl = (self.templates_dir / "TEMPLATE_C_PAGE_WRAPPER.html").read_text(encoding='utf-8')
        
        full_body = wrapper_tpl.replace("<!-- CONTENT_GOES_HERE -->", body_content)
        final_html = base_tpl.replace("<!-- BODY_CONTENT -->", full_body)
        
        # Save
        output_path = self.pages_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(final_html, encoding='utf-8')
        print(f"✅ Generated Page: {output_path}")
        return output_path

    def _transform_list(self, markdown_text):
        """Converts markdown list to HTML list items."""
        html_items = ""
        for line in markdown_text.splitlines():
            line = line.strip()
            if line.startswith("- ") or line.startswith("* "):
                content = line[2:]
                html_items += f'<li class="list-item-content">{content}</li>\n'
            elif re.match(r"\d+\\. ", line):
                content = line.split(".", 1)[1].strip()
                html_items += f'<li class="list-item-content">{content}</li>\n'
        return html_items

    def _transform_table(self, tpl_content, markdown_table):
        """Converts markdown table to HTML table rows/headers."""
        lines = markdown_table.strip().splitlines()
        headers = []
        rows_data = [] # Rename to avoid confusion with rows_html string later
        
        if len(lines) >= 3:
             # Header | Header
             # --- | ---
             # Row | Row
             header_line = lines[0]
             # Skip separator line [1]
             row_lines = lines[2:]
             
             # Split by pipe, filter empty strings (start/end pipes)
             headers = [h.strip() for h in header_line.split("|") if h.strip()]
             
             for line in row_lines:
                 cols = [c.strip() for c in line.split("|") if c.strip()]
                 if cols: rows_data.append(cols)
                 
        # Generate HTML Headers
        header_html = ""
        for h in headers:
            header_html += f"<th>{h}</th>"
            
        # Generate HTML Rows
        rows_html = ""
        for r in rows_data:
            rows_html += "<tr>"
            for c in r:
                rows_html += f"<td>{c}</td>"
            rows_html += "</tr>\n"
            
        return tpl_content.replace("[TABLE_HEADERS]", header_html).replace("[TABLE_ROWS]", rows_html)

    def dispatch_to_jules(self, plan_path, title="New Lesson Plan"):
        """Sends the plan to Jules."""
        plan_content = Path(plan_path).read_text(encoding='utf-8')
        return self.jules_client.create_session(plan_content, title)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        c = Compiler()
        c.compile_page(sys.argv[1])
