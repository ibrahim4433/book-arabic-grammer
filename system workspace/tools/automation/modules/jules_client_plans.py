import sys
import json
import time
import subprocess
import re
from pathlib import Path

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

        # Check for direct branch field
        if 'branch' in status_data:
            details['branch'] = status_data['branch']

        # Check for pull request info
        pr_info = status_data.get('pullRequest', {})
        if pr_info:
            if 'number' in pr_info:
                details['pr_number'] = pr_info['number']

            head = pr_info.get('head', {})
            if 'ref' in head:
                details['branch'] = head['ref']

            # Extract number from htmlUrl if not present directly
            # "https://github.com/user/repo/pull/123"
            html_url = pr_info.get('htmlUrl', '')
            if html_url and 'pr_number' not in details:
                match = re.search(r'/pull/(\d+)', html_url)
                if match:
                    details['pr_number'] = match.group(1)

        if not details:
            print(f"⚠️ Could not identify branch/PR for session {session_id}. Data: {status_data.keys()}")

        return details

    def pull_plan_from_github(self, session_details, target_filename):
        """
        Fetches the plan file from the specified remote context (PR or Branch).
        """
        if not session_details:
            print("❌ No session details provided.")
            return False

        branch_name = session_details.get('branch')
        pr_number = session_details.get('pr_number')

        print(f"⬇️ Pulling {target_filename} (Branch: {branch_name}, PR: {pr_number})...")

        try:
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
                print("❌ Cannot pull: Missing Branch Name and PR Number.")
                return False

            # 1. Fetch
            fetch_cmd = ["git", "fetch", "origin", fetch_ref]
            subprocess.run(fetch_cmd, check=True, cwd=self.project_root, capture_output=True)

            # 2. Checkout specific file
            repo_path = f"plans/{target_filename}"
            checkout_cmd = ["git", "checkout", checkout_ref, "--", repo_path]
            subprocess.run(checkout_cmd, check=True, cwd=self.project_root, capture_output=True)

            print(f"✅ Successfully pulled {target_filename}")

            # Clean up local temp branch if created
            if pr_number:
                subprocess.run(["git", "branch", "-D", checkout_ref], cwd=self.project_root, capture_output=True)

            # 3. Verify file exists locally
            local_path = self.project_root / repo_path
            if local_path.exists():
                return True
            else:
                print(f"❌ File not found locally after checkout: {local_path}")
                return False

        except subprocess.CalledProcessError as e:
            print(f"❌ Git Error: {e}")
            if e.stderr:
                print(f"   Stderr: {e.stderr.decode()}")
            return False

    def construct_mega_prompt(self, lesson_data, architect_prompt, auditor_prompt):
        """
        Constructs the combined prompt for Generation -> Verification -> Refinement.
        """
        lesson_number = lesson_data['number']
        lesson_title = lesson_data['title']
        raw_text = lesson_data['raw_text']

        # Instructions for the "One-Shot" Iteration
        refinement_instruction = """
================================================================================
CRITICAL INSTRUCTION: SELF-CORRECTION LOOP
================================================================================
You are currently operating in a BATCH MODE. You must perform the following steps IN ORDER:

1.  **ACT AS THE ARCHITECT:** Generate the initial plan for this lesson using the raw text provided above and the Architect Rules.
2.  **ACT AS THE AUDITOR:** Immediately review the plan you just generated using the Auditor Rules provided below.
3.  **REFINE:** If you find any errors (missing content, bad formatting, wrong IDs), FIX THEM.
4.  **FINAL OUTPUT:** Output ONLY the final, verified, and corrected plan file.
    - The file must be valid Markdown.
    - The file must be placed in `plans/{lesson_number}-{lesson_title}-plan.md`.
    - Do not output the "Audit Report", only the final Plan.
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
    # Test Init
    client = JulesPlanClient()
    print("JulesPlanClient initialized.")
