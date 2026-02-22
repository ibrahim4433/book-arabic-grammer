import sys
import os
import json
import time
import subprocess
import re
import logging
import requests
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from jules_client import JulesClient

class JulesOCRClient(JulesClient):
    """
    Specialized client for OCR via Jules Sessions.
    Handles the workflow of:
    1. Creating a single session to process ALL images.
    2. Polling for completion (creating a PR/Branch).
    3. Merging and pulling the raw text files.
    """

    def __init__(self, api_key=None, project_root=None):
        super().__init__(api_key, project_root)
        self.output_dir = self.project_root / "system-workspace/text-data/raw"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.github_token = self._get_github_token()
        self.repo_owner = "ibrahim4433"
        self.repo_name = "book-arabic-grammer"

    def _get_github_token(self):
        """Loads GitHub Token from secrets/Github_Token.txt."""
        token_path = self.project_root / "secrets/Github_Token.txt"
        if token_path.exists():
            return token_path.read_text().strip()
        return os.getenv("GITHUB_TOKEN")

    def merge_pr(self, pr_number):
        """
        Merges a Pull Request using the GitHub API.
        """
        if not self.github_token:
            logging.error("❌ GitHub Token missing. Cannot merge PR.")
            return False, "Token Missing"

        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/pulls/{pr_number}/merge"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "commit_title": f"Merge PR #{pr_number} (Jules OCR Auto-Merge)",
            "merge_method": "squash"
        }

        try:
            logging.info(f"🔀 Merging PR #{pr_number}...")
            resp = requests.put(url, headers=headers, json=data, timeout=30)

            if resp.status_code == 200:
                logging.info(f"✅ PR #{pr_number} merged successfully.")
                return True, "Merged"
            elif resp.status_code == 405:
                logging.error(f"❌ PR #{pr_number} is not mergeable (Conflict?).")
                return False, "Not Mergeable"
            elif resp.status_code == 409:
                logging.error(f"❌ PR #{pr_number} merge conflict.")
                return False, "Conflict"
            else:
                logging.error(f"❌ Merge failed: {resp.status_code} - {resp.text}")
                return False, f"API Error {resp.status_code}"

        except requests.exceptions.RequestException as e:
            logging.error(f"❌ Network Error during merge: {e}")
            return False, "Network Error"

    def finalize_pr_and_pull(self, session_details, callback=None):
        """
        Merges the PR (if available) and then pulls changes to local.
        """
        if not callback:
            def callback(t, s, m): pass

        pr_number = session_details.get('pr_number')
        branch_name = session_details.get('branch')

        # 1. Try to Merge
        merged = False
        if pr_number:
            callback("OCR Session", "MERGING", f"Merging PR #{pr_number}...")
            success, msg = self.merge_pr(pr_number)
            if success:
                merged = True
                callback("OCR Session", "PULLING", "Pulling from Main...")
            else:
                callback("OCR Session", "WARN", f"Merge Failed ({msg}). Fetching Branch...")

        # 2. Pull Logic
        try:
            if merged:
                # Checkout main and pull
                subprocess.run(["git", "checkout", "main"], check=True, cwd=self.project_root, capture_output=True)
                subprocess.run(["git", "pull", "origin", "main"], check=True, cwd=self.project_root, capture_output=True)
                logging.info(f"✅ Finalization complete.")
                return True
            elif branch_name:
                # Fallback: Pull from branch
                logging.info(f"⬇️ Pulling branch {branch_name}...")
                subprocess.run(["git", "fetch", "origin", branch_name], check=True, cwd=self.project_root, capture_output=True)
                subprocess.run(["git", "checkout", f"origin/{branch_name}"], check=True, cwd=self.project_root, capture_output=True)

                # Copy files from checkout to current workspace (if needed, or just leave as checkout)
                # But usually we want to merge into main.
                # If merge failed, we at least have the files in the branch.
                return True
            else:
                return False

        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Git Error during pull: {e}")
            callback("OCR Session", "ERROR", "Git Pull Failed")
            return False

    def create_ocr_session(self, prompt):
        """
        Creates a session specifically for OCR.
        """
        title = f"Jules OCR Batch ({int(time.time())})"
        return self.create_session(prompt, title, automation_mode="AUTO_CREATE_PR")

    def get_session_details(self, session_id):
        """
        Retrieves session details including branch name and PR number if available.
        """
        status_data = self.get_session_status(session_id)
        if not status_data:
            return {}

        details = {}

        if 'branch' in status_data:
            details['branch'] = status_data['branch']

        pr_info = status_data.get('pullRequest', {})
        if pr_info:
            if 'number' in pr_info:
                details['pr_number'] = pr_info['number']

            head = pr_info.get('head', {})
            if 'ref' in head:
                details['branch'] = head['ref']

            html_url = pr_info.get('htmlUrl', '')
            if html_url and 'pr_number' not in details:
                match = re.search(r'/pull/(\d+)', html_url)
                if match:
                    details['pr_number'] = match.group(1)

        return details

    def construct_ocr_prompt(self, image_files):
        """
        Constructs the prompt for Jules to perform OCR on a list of images.
        """
        file_list_str = "\n".join([f"- {f}" for f in image_files])

        prompt = f"""
I need you to perform OCR on the following images located in the `input/` directory of this repository:

{file_list_str}

For each image, follow these steps STRICTLY:
1.  **Read the image file.** (e.g., `input/page_01.jpg`)
2.  **Extract the Arabic text** exactly as it appears in the image.
    -   Preserve all diacritics (Harakat).
    -   Do not add any introduction, explanation, or conversational filler.
    -   Do not translate. Keep it in Arabic.
3.  **Save the extracted text to a NEW file** in `system-workspace/text-data/raw/`.
    -   The filename MUST follow the pattern: `raw_{{original_filename}}.txt` (where {{original_filename}} is the name of the image file without extension).
    -   Example: If input is `input/page_01.jpg`, output MUST be `system-workspace/text-data/raw/raw_page_01.txt`.

Please process ALL listed images in this session and submit your changes as a Pull Request.
"""
        return prompt

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client = JulesOCRClient()
    logging.info("JulesOCRClient initialized.")
