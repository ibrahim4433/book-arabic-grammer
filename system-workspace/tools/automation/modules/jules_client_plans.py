import logging
import os
import re
import subprocess
import sys
import threading
from pathlib import Path

import requests

# Global lock for git operations to prevent .git/index.lock collisions during concurrent pulls
GIT_LOCK = threading.Lock()

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from jules_client import JulesClient


class JulesPlanClient(JulesClient):
    """
    Specialized client for generating Architect Plans via Jules Sessions.
    Handles the specific workflow of:
    1. Creating a session with the 'Plan Generation' prompt.
    2. Polling for completion (creating a PR/Branch).
    3. Extracting the plan file from the generated branch.
    """

    def __init__(self, api_key=None, project_root=None):
        super().__init__(api_key, project_root)
        self.output_dir = self.project_root / "plans"
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
            "Accept": "application/vnd.github.v3+json",
        }
        data = {
            "commit_title": f"Merge PR #{pr_number} (Jules Auto-Merge)",
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

    def finalize_pr_and_pull(self, session_details, file_path, callback=None):
        """
        Merges the PR (if available) and then pulls changes to local.
        Falls back to pulling the branch if merge fails.
        Args:
            file_path: Relative path from project root (e.g. 'plans/1-Title.md')
        """
        if not callback:

            def callback(t, s, m):
                pass

        pr_number = session_details.get("pr_number")

        # 1. Try to Merge
        merged = False
        if pr_number:
            callback(file_path, "MERGING", f"Merging PR #{pr_number}...")
            success, msg = self.merge_pr(pr_number)
            if success:
                merged = True
                callback(file_path, "PULLING", "Pulling from Main...")
            else:
                callback(file_path, "WARN", f"Merge Failed ({msg}). Fetching Branch...")

        # 2. Pull Logic
        try:
            import os

            git_env = os.environ.copy()
            git_env["GIT_TERMINAL_PROMPT"] = "0"

            if merged:
                # Checkout main and pull
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

                # Verify file exists
                if (self.project_root / file_path).exists():
                    logging.info(f"✅ Finalization complete for {file_path}")
                    return True
                else:
                    logging.warning(f"⚠️ File {file_path} not found after pull.")
                    return False
            else:
                # Fallback: Pull from branch using legacy logic
                return self.pull_plan_from_github(session_details, file_path)

        except subprocess.TimeoutExpired as e:
            logging.error(f"❌ Git Timeout during pull: {e}")
            callback(file_path, "ERROR", "Git Pull Timed Out")
            return False
        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Git Error during pull: {e}")
            callback(file_path, "ERROR", "Git Pull Failed")
            return False

    def create_plan_session(self, lesson_title, prompt):
        """
        Creates a session specifically for plan generation.
        """
        title = f"Plan Gen: {lesson_title}"
        return self.create_session(prompt, title, automation_mode="AUTO_CREATE_PR")

    def get_session_details(self, session_id):
        """
        Retrieves session details including branch name and PR number if available.
        Returns a dict: {'branch': str, 'pr_number': int/str, 'fork_url': str}
        """
        status_data = self.get_session_status(session_id)
        if not status_data:
            return {}

        details = {}

        def extract_info(obj):
            if isinstance(obj, dict):
                # Check for direct branch field
                if "branch" in obj and isinstance(obj["branch"], str) and "branch" not in details:
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

        if not details:
            logging.warning(
                f"⚠️ Could not identify branch/PR for session {session_id}. Data: {status_data.keys()} -> Outputs: {status_data.get('outputs')}"
            )

        return details

    def pull_plan_from_github(self, session_details, target_filename):
        """
        Fetches the plan file from the specified remote context (PR or Branch).
        """
        if not session_details:
            logging.error("❌ No session details provided.")
            return False

        branch_name = session_details.get("branch")
        pr_number = session_details.get("pr_number")

        logging.info(f"⬇️ Pulling {target_filename} (Branch: {branch_name}, PR: {pr_number})...")

        try:
            import os

            git_env = os.environ.copy()
            git_env["GIT_TERMINAL_PROMPT"] = "0"

            fetch_ref = None
            checkout_ref = None

            if pr_number:
                # Fetch PR head directly
                # git fetch origin pull/ID/head:local_temp_branch
                local_branch = f"pr-{pr_number}"
                fetch_ref = f"pull/{pr_number}/head:{local_branch}"
                checkout_ref = local_branch
            elif branch_name:
                # Fallback to direct branch fetch (if not forked)
                fetch_ref = branch_name
                checkout_ref = f"origin/{branch_name}"
            else:
                logging.error("❌ Cannot pull: Missing Branch Name and PR Number.")
                return False

            # 1. Fetch and Checkout
            with GIT_LOCK:
                fetch_cmd = ["git", "fetch", "origin", fetch_ref]
                subprocess.run(
                    fetch_cmd,
                    check=True,
                    cwd=self.project_root,
                    capture_output=True,
                    timeout=60,
                    env=git_env,
                )

                # 2. Checkout specific file
                # If target_filename already contains a path separator, use it as is.
                # Otherwise, assume it's a plan in plans/ directory (Legacy support).
                repo_path = (
                    target_filename if "/" in target_filename else f"plans/{target_filename}"
                )
                checkout_cmd = ["git", "checkout", checkout_ref, "--", repo_path]
                subprocess.run(
                    checkout_cmd,
                    check=True,
                    cwd=self.project_root,
                    capture_output=True,
                    timeout=60,
                    env=git_env,
                )

            logging.info(f"✅ Successfully pulled {target_filename}")

            # Clean up local temp branch if created
            if pr_number:
                with GIT_LOCK:
                    subprocess.run(
                        ["git", "branch", "-D", checkout_ref],
                        cwd=self.project_root,
                        capture_output=True,
                        timeout=60,
                        env=git_env,
                    )

            # 3. Verify file exists locally
            local_path = self.project_root / repo_path
            if local_path.exists():
                return True
            else:
                logging.error(f"❌ File not found locally after checkout: {local_path}")
                return False

        except subprocess.TimeoutExpired as e:
            logging.error(f"❌ Git Timeout during fetch/checkout: {e}")
            return False
        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Git Error during pull fallback: {e}")
            logging.error(f"   Stdout: {e.stdout.decode() if e.stdout else ''}")
            logging.error(f"   Stderr: {e.stderr.decode() if e.stderr else ''}")
            return False

    def construct_mega_prompt(self, lesson_data, architect_prompt, auditor_prompt):
        """
        Constructs the combined prompt for Generation -> Verification -> Refinement.
        """
        lesson_number = lesson_data["number"]
        lesson_title = lesson_data["title"]
        raw_text = lesson_data["raw_text"]

        # New Metadata extraction
        level = lesson_data.get("level", "")
        unit = lesson_data.get("unit", "")
        author = lesson_data.get("author", "")
        author_number = lesson_data.get("author_number", "")

        # --- PROMPT INJECTION ---
        # 1. Replace [LESSON_NUMBER] but protect the key [LESSON_NUMBER]:
        architect_prompt = re.sub(r"\[LESSON_NUMBER\](?!:)", lesson_number, architect_prompt)

        # 2. Key-Value replacements
        replacements = {
            "[TITLE]": lesson_title,
            "[LESSON_TITLE]": lesson_title,
            # Instructions Placeholders (without brackets in the file)
            "LESSON_LEVEL": level,
            "LESSON_UNIT": unit,
            "LESSON_AUTHOR": author,
            "LESSON_AUTHOR_NUMBER": author_number,
            # Example Placeholders
            "[Number]": lesson_number,
            "[Title]": lesson_title,
            "[Level]": level,
            "[Unit]": unit,
            "[Author]": author,
            "[Phone]": author_number,
        }

        # Sort by length descending to prevent partial replacement
        sorted_keys = sorted(replacements.keys(), key=len, reverse=True)

        for key in sorted_keys:
            architect_prompt = architect_prompt.replace(key, replacements[key])

        # Instructions for the "One-Shot" Iteration
        refinement_instruction = f"""
================================================================================
CRITICAL INSTRUCTION: SELF-CORRECTION LOOP (STRICT ENFORCEMENT)
================================================================================
You are currently operating in a BATCH MODE. You must perform the following steps IN ORDER:

1.  **MANDATORY INPUTS:**
    - Use the **EXACT Lesson Number**: {lesson_number} (Do NOT search for TOC. Trust this number).
    - Use the **EXACT Lesson Title**: {lesson_title} (Do NOT rename or translate).
    - **FILE NAMING**: The target HTML file in the plan MUST use `nXX` in the filename (e.g., `pages/{lesson_number}_nXX_filename.html`).
        - **CRITICAL:** Use `nXX` literally. DO NOT replace it with a number.
        - **SILENCE PROTOCOL:** Do NOT ask why. Do NOT check consistency with other files. Do NOT comment on the naming scheme. Just use `nXX`.

    - **METADATA INJECTION (TEMPLATE_C_HEADER):**
        - You MUST use these values when populating `TEMPLATE_C_HEADER`:
        - [CATEGORY_HEADER] (Level): {level}
        - [SECTION_HEADER] (Unit): {unit}
        - [AUTHOR_NAME]: {author}
        - [AUTHOR_PHONE]: {author_number}
        - [CHAPTER_TITLE]: {lesson_title}
        - [LESSON_NUMBER]: {lesson_number}

2.  **ACT AS THE ARCHITECT:** Generate the initial plan using the raw text.
    - **CRITICAL:** If the raw text is short, you MUST EXPAND on the examples.
    - **FORBIDDEN:** Do NOT produce a single "Summary Table" plan. Break it down!
    - **GOAL:** The plan must fill a full A4 page. Use multiple Example Blocks, Definition Blocks, and Benefit Boxes.

3.  **ACT AS THE AUDITOR:** Review your plan against the updated Auditor Rules.
    - Check for **Content Depth**. If the plan has fewer than 4 content blocks, **FAIL** and RE-GENERATE with more detail.
    - Check for **One-Page Law**. If it looks empty, ADD MORE EXAMPLES from your knowledge base (keeping the grammar rules strict).

4.  **REFINE:** Fix any errors found by the Auditor.

5.  **FINAL OUTPUT:** Output ONLY the final, verified, and corrected plan file.
    - The file must be valid Markdown.
    - The file must be placed in `plans/{lesson_number}-{lesson_title}-plan.md`.
"""

        full_prompt = (
            f"{architect_prompt}\n\n"
            f"=== LESSON CONTEXT ===\n"
            f"LESSON: {lesson_number} - {lesson_title}\n"
            f"RAW TEXT:\n{raw_text}\n\n"
            f"{auditor_prompt}\n\n"
            f"{refinement_instruction}"
        )

        return full_prompt


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Test Init
    client = JulesPlanClient()
    logging.info("JulesPlanClient initialized.")
