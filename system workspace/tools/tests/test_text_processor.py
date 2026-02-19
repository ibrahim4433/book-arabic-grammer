import unittest
import sys
import os
import json
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(project_root / "system workspace/tools/automation"))

from modules.text_processing import TextProcessor

class TestTextProcessor(unittest.TestCase):
    
    def setUp(self):
        print("\n--- Setup: Initializing TextProcessor ---")
        self.processor = TextProcessor()

    def test_toc_validation(self):
        print("Test: TOC Validation (JSON)")
        self.assertTrue(self.processor.validate_toc(), "TOC.json should be valid")
        print("✅ TOC validated.")

    def test_get_lesson_number(self):
        print("Test: Get Lesson Number")
        # Load TOC to find a valid title
        toc_path = self.processor.toc_path
        if toc_path.exists():
            data = json.loads(toc_path.read_text(encoding='utf-8'))
            if data:
                # Test with the first item
                first_key = next(iter(data))
                first_title = data[first_key]['title']
                number = self.processor.get_lesson_number(first_title)
                self.assertEqual(number, first_key.zfill(2), f"Should return correct number for '{first_title}'")
                print(f"✅ Correctly identified '{first_title}' as lesson {number}")
        else:
            print("⚠️ TOC.json not found. Skipping lesson number test.")

    def test_merge_logic(self):
        print("Test: Merge Logic")
        # Ensure at least one raw file exists for a meaningful test
        raw_files = list(self.processor.raw_dir.glob("raw_*.txt"))
        if raw_files:
            merged_path = self.processor.merge_raw_text()
            self.assertTrue(merged_path.exists(), "Merged file should be created")
            print(f"✅ Merged {len(raw_files)} raw files.")
        else:
            print("⚠️ No raw files to merge. Skipping check.")

if __name__ == "__main__":
    unittest.main()
