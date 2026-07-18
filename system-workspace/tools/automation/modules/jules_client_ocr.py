import logging
import os
import subprocess
import sys
import time
from pathlib import Path

import requests

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from github_utils import GithubClient
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
        # Init Github Client for fallback
        self.github = GithubClient(token_path=self.project_root / "secrets/Github_Token.txt")

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
            "Accept": "application/vnd.github.v3+json",
        }
        data = {
            "commit_title": f"Merge PR #{pr_number} (Jules OCR Auto-Merge)",
            "merge_method": "squash",
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

            def callback(t, s, m):
                pass

        pr_number = session_details.get("pr_number")

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
            import os

            git_env = os.environ.copy()
            git_env["GIT_TERMINAL_PROMPT"] = "0"

            if merged:
                with GIT_LOCK:
                    subprocess.run(
                        ["git", "checkout", "main"],
                        check=True,
                        cwd=self.project_root,
                        capture_output=True,
                        timeout=60,
                        env=git_env,
                    )
                    subprocess.run(
                        ["git", "pull", "origin", "main"],
                        check=True,
                        cwd=self.project_root,
                        capture_output=True,
                        timeout=60,
                        env=git_env,
                    )

                # Assuming success since checkout/pull didn't throw
                logging.info("✅ Finalization complete.")
                return True
            else:
                return self.pull_raw_files_from_github(session_details)

        except subprocess.TimeoutExpired as e:
            logging.error(f"❌ Git Timeout during pull: {e}")
            callback("OCR Session", "ERROR", "Git Pull Timed Out")
            return False
        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Git Error during pull: {e}")
            callback("OCR Session", "ERROR", "Git Pull Failed")
            return False

    def pull_raw_files_from_github(self, session_details):
        """
        Fetches the raw text files directory from the specified remote context (PR or Branch).
        """
        if not session_details:
            logging.error("❌ No session details provided for pull.")
            return False

        branch_name = session_details.get("branch")
        pr_number = session_details.get("pr_number")
        target_dir = "system-workspace/text-data/raw/"

        logging.info(f"⬇️ Pulling raw files from {branch_name or pr_number}...")

        try:
            import os

            git_env = os.environ.copy()
            git_env["GIT_TERMINAL_PROMPT"] = "0"

            fetch_ref = None
            checkout_ref = None

            if pr_number:
                # Fetch PR head directly
                local_branch = f"pr-ocr-{pr_number}"
                fetch_ref = f"pull/{pr_number}/head:{local_branch}"
                checkout_ref = local_branch
            elif branch_name:
                fetch_ref = branch_name
                checkout_ref = f"origin/{branch_name}"
            else:
                logging.error("❌ Cannot pull: Missing Branch Name and PR Number.")
                return False

            with GIT_LOCK:
                # 1. Fetch
                fetch_cmd = ["git", "fetch", "origin", fetch_ref]
                subprocess.run(
                    fetch_cmd,
                    check=True,
                    cwd=self.project_root,
                    capture_output=True,
                    timeout=60,
                    env=git_env,
                )

                # 2. Checkout the specific directory
                checkout_cmd = ["git", "checkout", checkout_ref, "--", target_dir]
                subprocess.run(
                    checkout_cmd,
                    check=True,
                    cwd=self.project_root,
                    capture_output=True,
                    timeout=60,
                    env=git_env,
                )

                logging.info(f"✅ Successfully pulled raw files from {checkout_ref}")

                # Clean up local temp branch if created
                if pr_number:
                    subprocess.run(
                        ["git", "branch", "-D", checkout_ref],
                        cwd=self.project_root,
                        capture_output=True,
                        timeout=60,
                        env=git_env,
                    )

            return True

        except subprocess.TimeoutExpired as e:
            logging.error(f"❌ Git Timeout during fetch/checkout: {e}")
            return False
        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Git Error: {e}")
            if e.stderr:
                logging.error(f"   Stderr: {e.stderr.decode()}")
            return False

    def create_ocr_session(self, prompt, title_suffix=""):
        """
        Creates a session specifically for OCR.
        """
        title = f"Jules OCR Batch ({int(time.time())})"
        if title_suffix:
            title += f" - {title_suffix}"
        return self.create_session(prompt, title, automation_mode="AUTO_CREATE_PR")

    def get_session_details(self, session_id):
        """
        Retrieves session details including branch name and PR number if available.
        Attempts fallback to GitHub API if session status is incomplete.
        """
        status_data = self.get_session_status(session_id)
        details = {}

        if status_data:

            def extract_info(obj):
                if isinstance(obj, dict):
                    # Check for direct branch field
                    if (
                        "branch" in obj
                        and isinstance(obj["branch"], str)
                        and "branch" not in details
                    ):
                        details["branch"] = obj["branch"]

                    # Check for pull request info
                    if "pullRequest" in obj:
                        pr_info = obj["pullRequest"]
                        if "number" in pr_info and "pr_number" not in details:
                            details["pr_number"] = pr_info["number"]

                        head = pr_info.get("head", {})
                        if "ref" in head and "branch" not in details:
                            details["branch"] = head["ref"]

                        html_url = pr_info.get("htmlUrl", "")
                        if html_url and "pr_number" not in details:
                            import re

                            match = re.search(r"/pull/(\d+)", html_url)
                            if match:
                                details["pr_number"] = match.group(1)

                    for v in obj.values():
                        extract_info(v)
                elif isinstance(obj, list):
                    for item in obj:
                        extract_info(item)

            extract_info(status_data)

            # Ultimate fallback: regex search on the raw JSON string
            if not details.get("pr_number"):
                import json
                import re

                raw_str = json.dumps(status_data)
                match = re.search(r"github\.com/[^/]+/[^/]+/pull/(\d+)", raw_str)
                if match:
                    details["pr_number"] = match.group(1)

        # Fallback: If no details found, search GitHub for recent open PRs
        if not details:
            logging.warning("⚠️ Session status missing PR info. Searching GitHub...")

            # Find open PRs from Jules (or anyone really, but assume Jules)
            # We filter for PRs that touch system-workspace/text-data/raw/
            # Or just the latest one.
            prs = self.github.list_pull_requests(f"{self.repo_owner}/{self.repo_name}")

            for pr in prs:
                # Check if title matches our pattern "Jules OCR Batch"
                # Or if user is Jules (need to know username, usually "google-jules-bot" or similar but varies)
                # Let's rely on title mostly or files.
                title = pr.get("title", "")
                if "OCR" in title or "Batch" in title or "Jules" in title:
                    # This is a candidate.
                    details["pr_number"] = pr["number"]
                    details["branch"] = pr["head"]["ref"]
                    logging.info(f"🔍 Found candidate PR #{pr['number']}: {title}")
                    break

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

DO NOT CREATE A TOOL OR WRITE CODE OR DO ANYTHING ELSE ABOVE !
DO NOT Create a Python script like perform_ocr.py ! , do OCR yourself manually!
"""
        return prompt


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client = JulesOCRClient()
    logging.info("JulesOCRClient initialized.")
