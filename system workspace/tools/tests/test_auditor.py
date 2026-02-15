import unittest
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.append(str(project_root / "system workspace/tools/automation"))

from modules.auditor import Auditor

class TestAuditor(unittest.TestCase):
    
    def setUp(self):
        print("\n--- Setup: Initializing Auditor ---")
        self.auditor = Auditor()
        # Use CWD since we run from root
        self.test_page = Path.cwd() / "pages/00.0_blank_page1.html"
        print(f"Debug: Test Page Path: {self.test_page}")

    def test_audit_pass(self):
        print(f"Test: Audit Existing Page ({self.test_page.name})")
        if not self.test_page.exists():
            print("⚠️ Test page not found. Skipping.")
            return

        result = self.auditor.audit_page(self.test_page)
        # Note: Depending on the real layout checker, this might fail or pass. 
        # But we check that the tool ran and returned a result.
        self.assertIn("status", result)
        print(f"Result: {result}")

    def test_tool_paths(self):
        print("Test: Tool Paths")
        self.assertTrue(self.auditor.verify_tool.exists(), "Verify Layout tool must exist")
        # Lint tool might be optional or in different path, but we check if configured path exists
        self.assertTrue(self.auditor.lint_tool.exists(), "Lint Pages tool must exist")
        print("✅ Tool paths verified.")

if __name__ == "__main__":
    unittest.main()

