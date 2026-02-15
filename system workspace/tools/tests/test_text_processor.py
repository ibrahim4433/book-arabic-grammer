import unittest
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.append(str(project_root / "system workspace/tools/automation"))

from modules.text_processing import TextProcessor

class TestTextProcessor(unittest.TestCase):
    
    def setUp(self):
        print("\n--- Setup: Initializing TextProcessor ---")
        self.processor = TextProcessor()

    def test_toc_validation(self):
        print("Test: TOC Validation")
        self.assertTrue(self.processor.validate_toc(), "TOC.txt should be valid")
        print("✅ TOC validated.")

    def test_merge_logic(self):
        print("Test: Merge Logic")
        # Ensure at least one raw file exists for a meaningful test
        # We can create a dummy file if needed, but let's check existing
        raw_files = list(self.processor.raw_dir.glob("raw_*.txt"))
        if raw_files:
            merged_path = self.processor.merge_raw_text()
            self.assertTrue(merged_path.exists(), "Merged file should be created")
            print(f"✅ Merged {len(raw_files)} raw files.")
        else:
            print("⚠️ No raw files to merge. Skipping check.")

if __name__ == "__main__":
    unittest.main()

