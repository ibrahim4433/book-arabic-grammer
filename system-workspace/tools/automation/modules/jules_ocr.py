import sys
import json
import time
import logging
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from jules_client_ocr import JulesOCRClient

class JulesOCR:
    """
    Orchestrates the batch OCR process using a single Jules Session.
    """

    def __init__(self, project_root=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.client = JulesOCRClient(project_root=self.project_root)
        self.input_dir = self.project_root / "input"
        self.output_dir = self.project_root / "system-workspace/text-data/raw"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run_ocr_batch(self, update_callback=None):
        """
        Main entry point. Orchestrates the batch processing.
        Args:
            update_callback (callable): Function(status, message)
        """
        if not update_callback:
            def default_callback(status, msg):
                logging.info(f"[{status}] {msg}")
            update_callback = default_callback

        update_callback("RUNNING", "Scanning for images...")

        # 1. Gather Images
        if not self.input_dir.exists():
            update_callback("ERROR", "Input directory not found.")
            return

        image_files = sorted(
            list(self.input_dir.glob("*.jpg")) +
            list(self.input_dir.glob("*.png")) +
            list(self.input_dir.glob("*.jpeg"))
        )

        if not image_files:
            update_callback("WARN", "No images found in input/.")
            return

        update_callback("RUNNING", f"Found {len(image_files)} images to process.")

        # 2. Construct Prompt
        # We pass relative paths to keep prompt clean and relative to repo root
        rel_paths = [str(p.relative_to(self.project_root)) for p in image_files]
        prompt = self.client.construct_ocr_prompt(rel_paths)

        # 3. Create Session
        update_callback("RUNNING", "Creating Jules Session...")
        session = self.client.create_ocr_session(prompt)

        if not session:
            update_callback("ERROR", "Failed to create Jules session.")
            return

        session_id = session.get('name')
        update_callback("RUNNING", f"Session Created: {session_id}")

        # 4. Monitor Session
        def status_update(state):
            update_callback("RUNNING", f"Jules Status: {state}")

        status = self.client.wait_for_completion(session_id, timeout_minutes=30, status_callback=status_update)

        if status not in ["SUCCEEDED", "COMPLETED"]:
            update_callback("FAILED", f"Session ended with status: {status}")
            return

        # 5. Finalize (Merge/Pull)
        update_callback("RUNNING", "Finalizing changes (Merge & Pull)...")
        details = self.client.get_session_details(session_id)

        if not details:
            update_callback("WARN", "Could not retrieve PR details. Check manually.")
            return

        success = self.client.finalize_pr_and_pull(details, callback=lambda t, s, m: update_callback(s, m))

        if success:
            update_callback("SUCCESS", "OCR Batch Complete. Files synced.")
        else:
            update_callback("ERROR", "Failed to merge/pull changes.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ocr = JulesOCR()
    ocr.run_ocr_batch()
