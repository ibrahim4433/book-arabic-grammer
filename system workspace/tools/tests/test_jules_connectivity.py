import unittest
import sys
import os
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(project_root / "system workspace/tools/automation"))

try:
    from modules.jules_client import JulesClient
except ImportError as e:
    print(f"❌ Import Error: {e}")
    sys.exit(1)

class TestJulesConnectivity(unittest.TestCase):
    
    def setUp(self):
        print("\n--- Setup: Initializing JulesClient ---")
        self.client = JulesClient()

    def test_api_key_loaded(self):
        print("Test: API Key Loading")
        self.assertIsNotNone(self.client.api_key, "API Key should be loaded from env or secrets")
        print("✅ API Key loaded successfully.")

    def test_client_structure(self):
        print("Test: Client Structure")
        self.assertTrue(hasattr(self.client, 'create_session'), "Client must have create_session method")
        self.assertTrue(hasattr(self.client, 'get_session_status'), "Client must have get_session_status method")
        print("✅ Client structure verified.")

if __name__ == '__main__':
    unittest.main()

