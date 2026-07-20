### `system-workspace/tools/automation/modules/github_utils.py`
- **Status:** Usable
- **Purpose:** A utility wrapper for the GitHub API to manage pull requests, search for files in branches, and download raw files.
- **Inputs:** Reads the GitHub token from `secrets/Github_Token.txt` or environment variables.
- **Outputs:** Downloads files directly to the local filesystem or returns JSON data (PRs, file info) from the GitHub API.
- **Usage:** `Used programmatically as a helper: `from github_utils import GithubClient; client = GithubClient(); prs = client.list_pull_requests('owner/repo')``
- **Workflow Integration:** A foundational module used by `jules_page_generator.py` and `jules_client_plans.py` to pull generated plans or HTML pages from Jules PRs into the local workspace. It's agnostic to the workflow type.
