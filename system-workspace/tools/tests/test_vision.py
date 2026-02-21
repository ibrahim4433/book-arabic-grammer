import unittest
import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.append(str(project_root / "system-workspace/tools/automation"))

from modules.vision import VisionClient

class TestVisionClient(unittest.TestCase):
    
    def setUp(self):
        print("\n--- Setup: Initializing VisionClient ---")
        self.client = VisionClient()
        self.test_image = project_root / "input/3.jpg"

    def test_key_loaded(self):
        print("Test: API Key Loading")
        self.assertIsNotNone(self.client.api_key, "Gemini API Key should be loaded")
        print("✅ API Key loaded.")

    def test_image_path_resolution(self):
        print("Test: Image Path Resolution")
        if self.test_image.exists():
            print(f"✅ Found test image: {self.test_image}")
            # We won't call the API in unit test unless we mock it or explicitly want an integration test
            # integration_test = self.client.extract_text([self.test_image])
            # self.assertTrue(len(integration_test) > 0)
        else:
            print("⚠️ Test image not found (input/3.jpg). Skipping integration check.")

if __name__ == '__main__':
    unittest.main()

