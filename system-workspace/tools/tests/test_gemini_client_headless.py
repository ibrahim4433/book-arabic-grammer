import sys
import unittest
from pathlib import Path
from unittest.mock import patch

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(project_root / "system-workspace/tools/automation"))

from modules.gemini_client import GeminiClient
from modules.text_processing import TextProcessor


class TestGeminiClientHeadless(unittest.TestCase):
    def test_gemini_client_headless_init(self):
        print("\nTest: GeminiClient Headless Init")
        client = GeminiClient(use_headless=True)
        self.assertTrue(client.use_headless, "use_headless should be True")
        print("✅ GeminiClient initialized with use_headless=True")

    @patch("modules.gemini_client.GeminiClient.generate_content_headless")
    def test_gemini_client_force_headless(self, mock_headless):
        print("\nTest: GeminiClient Force Headless")
        # Ensure API key is set so we test the override logic
        client = GeminiClient(api_key="fake_key", use_headless=True)

        mock_headless.return_value = "Headless Result"

        result = client.generate_content("System", "User")

        mock_headless.assert_called_once()
        self.assertEqual(result, "Headless Result")
        print("✅ generate_content switched to headless mode correctly.")

    def test_text_processor_headless_init(self):
        print("\nTest: TextProcessor Headless Init")
        tp = TextProcessor(use_headless=True)
        self.assertTrue(
            tp.client.use_headless, "TextProcessor should pass use_headless to GeminiClient"
        )
        print("✅ TextProcessor initialized correctly with use_headless=True")


if __name__ == "__main__":
    unittest.main()
