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

        # New Metadata extraction
        level = lesson_data.get('level', '')
        unit = lesson_data.get('unit', '')
        author = lesson_data.get('author', '')
        author_number = lesson_data.get('author_number', '')

        # --- PROMPT INJECTION ---
        # 1. Replace [LESSON_NUMBER] but protect the key [LESSON_NUMBER]:
        architect_prompt = re.sub(r'\[LESSON_NUMBER\](?!:)', lesson_number, architect_prompt)

        # 2. Key-Value replacements
        replacements = {
            '[TITLE]': lesson_title,
            '[LESSON_TITLE]': lesson_title,

            # Instructions Placeholders (without brackets in the file)
            'LESSON_LEVEL': level,
            'LESSON_UNIT': unit,
            'LESSON_AUTHOR': author,
            'LESSON_AUTHOR_NUMBER': author_number,

            # Example Placeholders
            '[Number]': lesson_number,
            '[Title]': lesson_title,
            '[Level]': level,
            '[Unit]': unit,
            '[Author]': author,
            '[Phone]': author_number
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
    # Test Init
    client = JulesPlanClient()
    print("JulesPlanClient initialized.")
