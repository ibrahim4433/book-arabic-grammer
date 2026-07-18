import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Setup paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(PROJECT_ROOT / "system-workspace/tools/automation"))

# We import the module, not the class directly, to make patching easier if needed
import modules.jules_ocr as jules_ocr_module


class TestJulesOCRIntegration(unittest.TestCase):
    @patch("modules.jules_ocr.JulesOCRClient")
    def test_batch_processing_logic(self, MockClientClass):
        """Test that images are batched and processed correctly."""

        # Setup Mock Instance
        mock_client = MockClientClass.return_value
        mock_client.construct_ocr_prompt.return_value = "Prompt"
        # Return a dummy session object
        mock_client.create_ocr_session.return_value = {"name": "session_123"}
        mock_client.wait_for_completion.return_value = "SUCCEEDED"
        mock_client.get_session_details.return_value = {"pr_number": 1}
        mock_client.finalize_pr_and_pull.return_value = True

        # Initialize JulesOCR (it will use the mocked client class)
        ocr = jules_ocr_module.JulesOCR(project_root=PROJECT_ROOT)

        # Mock file system interactions on the OCR instance
        ocr.input_dir = MagicMock()
        ocr.input_dir.exists.return_value = True

        # Create dummy image files
        # We need Path objects that can be sorted and globbed
        images = [Path(f"img_{i:02d}.jpg") for i in range(12)]  # 00 to 11
        ocr.input_dir.glob.side_effect = [images, [], []]

        # Mock relative_to
        # Since we use real Path objects in the list, relative_to might fail if project_root is real
        # But glob returns what we give it.
        # The code does: rel_paths = [str(p.relative_to(self.project_root)) ...]
        # So we need to ensure the paths we returned from glob behave like paths relative to root or mock relative_to

        # Easier: Mock relative_to on the path objects themselves?
        # Path objects are immutable/hard to mock methods on directly if they are real Paths.
        # Let's use MagicMocks that look like Paths.
        mock_images = []
        for i in range(12):
            m = MagicMock(spec=Path)
            m.name = f"img_{i:02d}.jpg"
            m.__str__.return_value = f"/abs/path/img_{i:02d}.jpg"
            # Allow sorting? sorted() calls __lt__
            m.__lt__.side_effect = lambda other: m.name < other.name
            m.relative_to.return_value = Path(f"input/img_{i:02d}.jpg")
            mock_images.append(m)

        ocr.input_dir.glob.side_effect = [mock_images, [], []]

        # Callback capture
        logs = []

        def callback(status, msg):
            logs.append(f"[{status}] {msg}")

        # Run
        ocr.run_ocr_batch(update_callback=callback)

        # Assertions

        # 1. Verify Batching (12 images / 5 = 3 batches)
        # construct_ocr_prompt called 3 times?
        self.assertEqual(mock_client.construct_ocr_prompt.call_count, 3)

        # 2. Verify Session Creation with Suffix
        self.assertEqual(mock_client.create_ocr_session.call_count, 3)

        # Check suffixes
        # We need to inspect call_args_list.
        # Each call is (args, kwargs).
        # kwargs should contain title_suffix='Batch X'

        suffixes = []
        for call in mock_client.create_ocr_session.call_args_list:
            args, kwargs = call
            if "title_suffix" in kwargs:
                suffixes.append(kwargs["title_suffix"])

        self.assertIn("Batch 1", suffixes)
        self.assertIn("Batch 2", suffixes)
        self.assertIn("Batch 3", suffixes)

        # 3. Verify Success Callback
        found_success = any("All OCR batches completed successfully" in log for log in logs)
        if not found_success:
            print("\nLOGS DUMP:")
            for l in logs:
                print(l)

        self.assertTrue(found_success)


if __name__ == "__main__":
    unittest.main()
