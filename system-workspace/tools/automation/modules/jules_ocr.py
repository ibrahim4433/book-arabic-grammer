import sys
import json
import time
import logging
import concurrent.futures
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from jules_client_ocr import JulesOCRClient

class JulesOCR:
    """
    Orchestrates the batch OCR process using Jules Sessions.
    Supports parallel batch processing (5 images per session).

    Architecture:
    1. Parallel API Calls: Create sessions and wait for completion concurrently.
    2. Sequential Git Sync: Merge PRs and pull changes one by one to avoid race conditions.
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

        # 2. Batching Logic
        batch_size = 5
        batches = [image_files[i:i + batch_size] for i in range(0, len(image_files), batch_size)]
        total_batches = len(batches)

        update_callback("RUNNING", f"Found {len(image_files)} images. Processing in {total_batches} concurrent batch(es)...")

        # --- WORKER FUNCTION (API ONLY) ---
        def process_batch_api(batch_files, index):
            batch_id = f"Batch {index}/{total_batches}"
            try:
                # A. Construct Prompt
                rel_paths = [str(p.relative_to(self.project_root)) for p in batch_files]
                prompt = self.client.construct_ocr_prompt(rel_paths)

                # B. Create Session
                update_callback("RUNNING", f"[{batch_id}] Creating Session...")
                session = self.client.create_ocr_session(prompt, title_suffix=f"Batch {index}")

                if not session:
                    update_callback("ERROR", f"[{batch_id}] Failed to create session.")
                    return (False, None, batch_id)

                session_id = session.get('name')
                update_callback("RUNNING", f"[{batch_id}] Session Started: {session_id}")

                # C. Monitor
                def status_update(state):
                    update_callback("RUNNING", f"[{batch_id}] Status: {state}")

                status = self.client.wait_for_completion(session_id, timeout_minutes=30, status_callback=status_update)

                if status not in ["SUCCEEDED", "COMPLETED"]:
                    update_callback("FAILED", f"[{batch_id}] Session ended with status: {status}")
                    return (False, None, batch_id)

                # D. Retrieve Details for Finalization
                details = self.client.get_session_details(session_id)
                if not details:
                    update_callback("WARN", f"[{batch_id}] Could not retrieve PR details.")
                    return (False, None, batch_id)

                return (True, details, batch_id)

            except Exception as e:
                update_callback("ERROR", f"[{batch_id}] Exception: {e}")
                return (False, None, batch_id)

        # 3. Execute API Calls in Parallel
        api_results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=total_batches) as executor:
            # map returning futures
            futures = [executor.submit(process_batch_api, batch, i+1) for i, batch in enumerate(batches)]

            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                if res[0]: # If success
                    api_results.append(res)

        # 4. Execute Git Sync Sequentially
        if not api_results:
            update_callback("ERROR", "All API sessions failed. No git operations performed.")
            return

        update_callback("RUNNING", f"API Phase Complete. Starting Sequential Git Sync for {len(api_results)} batches...")

        final_success_count = 0

        # Sort by batch_id string (approximate but fine)
        api_results.sort(key=lambda x: x[2])

        for success, details, batch_id in api_results:
            update_callback("RUNNING", f"[{batch_id}] Syncing Changes...")

            # Bridge callback
            def bridge_cb(t, s, m):
                update_callback(s, f"[{batch_id}] {m}")

            if self.client.finalize_pr_and_pull(details, callback=bridge_cb):
                update_callback("SUCCESS", f"[{batch_id}] Sync Complete.")
                final_success_count += 1
            else:
                update_callback("ERROR", f"[{batch_id}] Git Sync Failed.")

        if final_success_count == total_batches:
            update_callback("SUCCESS", "All OCR batches completed successfully.")
        else:
            update_callback("WARN", f"OCR Finished. {final_success_count}/{total_batches} batches fully synced.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ocr = JulesOCR()
    ocr.run_ocr_batch()
