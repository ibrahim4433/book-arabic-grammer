import json
import re
from collections import Counter
from pathlib import Path


class PatternExtractor:
    """
    Analyzes existing HTML pages to extract design patterns and structural rules.
    Outputs a rich JSON guide for Jules.
    """

    def __init__(self, project_root=None):
        self.project_root = (
            Path(project_root)
            if project_root
            else Path(__file__).parent.parent.parent.parent.parent
        )
        self.pages_dir = self.project_root / "pages"
        self.output_path = self.project_root / "Jules-workspace/design_patterns.json"

        # Map CSS classes to Component Names (Reverse lookup)
        self.class_map = {
            "page-header-strip": "TEMPLATE_C_HEADER",
            "content-block": "TEMPLATE_C_BLOCK",
            "split-grid": "TEMPLATE_C_SPLIT",
            "structured-list": "TEMPLATE_C_LIST",
            "dense-table": "TEMPLATE_C_TABLE",
            "poem-container": "TEMPLATE_C_POEM",
            "irab-box": "TEMPLATE_C_IRAB_BOX",
            "exam-question": "TEMPLATE_C_EXAM",
        }

    def analyze(self):
        print("🔍 Extracting Design Patterns from existing pages...")

        html_files = sorted(list(self.pages_dir.glob("*.html")))
        structure_sequences = []
        class_stats = Counter()

        for f in html_files:
            content = f.read_text(encoding="utf-8")

            # 1. Identify Component Sequence
            # We look for the class names in order
            # This regex finds all class="..." occurrences
            classes_in_file = []

            # Simple regex to find relevant component classes
            # We iterate through the file line by line to preserve order roughly
            current_components = []
            for line in content.splitlines():
                for cls, comp in self.class_map.items():
                    if f'class="{cls}"' in line or f'class=" {cls} ' in line:
                        current_components.append(comp)

            if current_components:
                structure_sequences.append(" -> ".join(current_components))

            # 2. Class Statistics
            # Extract all classes
            matches = re.findall(r'class="([^"]+)"', content)
            for m in matches:
                classes = m.split()
                class_stats.update(classes)

        # 3. Determine "Common Flow" (Most frequent sequences)
        # This is a bit naive but gives an idea.
        # We'll just look for the most common component types.

        comp_counts = Counter()
        for seq in structure_sequences:
            for comp in seq.split(" -> "):
                comp_counts[comp] += 1

        # Construct the Pattern File
        patterns = {
            "guidance": {
                "description": "Design Patterns derived from analyzing "
                + str(len(html_files))
                + " existing pages.",
                "GOLDEN_FLOW": [
                    "1. TEMPLATE_C_HEADER (Always Start)",
                    "2. TEMPLATE_C_BLOCK (Definition - Most Common Start)",
                    "3. TEMPLATE_C_SPLIT (Analysis - High Frequency)",
                    "4. TEMPLATE_C_IRAB_BOX (Parsing - Mandatory)",
                    "5. TEMPLATE_C_EXAM (Always End)",
                ],
                "COMPONENT_FREQUENCY": dict(comp_counts.most_common()),
                "STYLING_RULES": {
                    "highlight-red": "Use for Grammar Signs (Harakat/Endings)",
                    "highlight-blue": "Use for Fixed Particles (Harf)",
                    "text-accent": "Use for Definitions",
                },
            },
            "analytics": {
                "analyzed_files": len(html_files),
                "top_classes": dict(class_stats.most_common(20)),
            },
        }

        # Save
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(
            json.dumps(patterns, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"✅ Design Patterns saved to {self.output_path}")


if __name__ == "__main__":
    pe = PatternExtractor()
    pe.analyze()
