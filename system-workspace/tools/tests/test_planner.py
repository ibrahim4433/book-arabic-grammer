import sys
import unittest
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(project_root / "system-workspace/tools/automation"))

from modules.planner import Planner


class TestPlanner(unittest.TestCase):
    def setUp(self):
        print("\n--- Setup: Initializing Planner ---")
        self.planner = Planner()

    def test_extract_block_quadruple(self):
        print("Test: Extract Block (Quadruple Backticks)")
        input_text = "Here is the plan:\n````text\n# Plan Content\n````"
        expected = "# Plan Content"
        result = self.planner._extract_plan_block(input_text)
        self.assertEqual(result, expected)
        print("✅ Extracted correctly.")

    def test_extract_block_triple(self):
        print("Test: Extract Block (Triple Backticks)")
        input_text = "Here is the plan:\n```text\n# Plan Content\n```"
        expected = "# Plan Content"
        result = self.planner._extract_plan_block(input_text)
        self.assertEqual(result, expected)
        print("✅ Extracted correctly.")

    def test_extract_block_raw(self):
        print("Test: Extract Block (Raw Text)")
        input_text = "# Plan Content"
        expected = "# Plan Content"
        result = self.planner._extract_plan_block(input_text)
        self.assertEqual(result, expected)
        print("✅ Extracted correctly.")


if __name__ == "__main__":
    unittest.main()
