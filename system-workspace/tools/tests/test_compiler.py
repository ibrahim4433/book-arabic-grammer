import sys
import unittest
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.append(str(project_root / "system-workspace/tools/automation"))

from modules.compiler import Compiler


class TestCompiler(unittest.TestCase):
    def setUp(self):
        print("\n--- Setup: Initializing Compiler ---")
        self.compiler = Compiler()

    def test_parse_plan_multiline(self):
        print("Test: Parse Plan (Multi-line Content)")
        plan_content = """
=== BLOCK 1: Definition ===
(Component: TEMPLATE_C_BLOCK)
Title: My Title
Content: This is a
multi-line content
block.
Key2: Value2
"""
        filename, blocks = self.compiler.parse_plan(plan_content)
        self.assertEqual(len(blocks), 1)
        self.assertEqual(blocks[0]["type"], "Definition")
        self.assertEqual(blocks[0]["fields"]["Title"], "My Title")
        self.assertIn("multi-line content", blocks[0]["fields"]["Content"])
        print("✅ Multi-line parsing successful.")

    def test_transform_table(self):
        print("Test: Table Transformation")
        tpl = "<table><thead>[TABLE_HEADERS]</thead><tbody>[TABLE_ROWS]</tbody></table>"
        markdown = """
| Name | Age |
|---|---|
| Alice | 30 |
| Bob | 25 |
"""
        result = self.compiler._transform_table(tpl, markdown)
        self.assertIn("<th>Name</th>", result)
        self.assertIn("<td>Alice</td>", result)
        print("✅ Table transformation successful.")


if __name__ == "__main__":
    unittest.main()
