import os
import requests
import logging
import base64
from pathlib import Path

class GithubClient:
    def __init__(self, token_path="secrets/Github_Token.txt"):
        self.token = self._load_token(token_path)
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.api_url = "https://api.github.com"

    def _load_token(self, path):
        try:
            token_file = Path(path)
            if token_file.exists():
                return token_file.read_text().strip()
            # Check env var as fallback
            return os.environ.get("GITHUB_TOKEN", "")
        except Exception as e:
            logging.error(f"Failed to load GitHub token: {e}")
            return ""

    def list_pull_requests(self, repo, author=None):
        """
        List open PRs, optionally filtered by author.
        repo: "owner/repo"
        author: username string to filter by (e.g., "Jules", "Google")
        """
        url = f"{self.api_url}/repos/{repo}/pulls?state=open"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            prs = response.json()

            if author:
                # Filter by user login or part of it (case-insensitive)
                filtered = []
                for pr in prs:
                    user_login = pr.get('user', {}).get('login', '').lower()
                    if author.lower() in user_login:
                        filtered.append(pr)
                return filtered
            return prs
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching PRs: {e}")
            return []

    def list_pr_files(self, repo, pr_number):
        """
        List all files modified in a PR.
        Returns a list of dicts: [{'filename': str, 'raw_url': str}, ...]
        """
        url = f"{self.api_url}/repos/{repo}/pulls/{pr_number}/files?per_page=100"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error listing files for PR #{pr_number}: {e}")
            return []

    def get_file_info(self, repo, path, ref):
        """
        Get file metadata (including download_url) from a specific ref (branch/commit).
        Returns dict or None if not found.
        """
        url = f"{self.api_url}/repos/{repo}/contents/{path}?ref={ref}"
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 404:
                return None
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error getting file info for {path} on {ref}: {e}")
            return None

    def download_file(self, download_url, local_path):
        """
        Download a raw file to local path.
        """
        headers = self.headers.copy()
        if "api.github.com" not in download_url:
            headers.pop("Accept", None)

        try:
            response = requests.get(download_url, headers=headers)
            response.raise_for_status()

            # Ensure directory exists
            Path(local_path).parent.mkdir(parents=True, exist_ok=True)

            with open(local_path, 'wb') as f:
                f.write(response.content)
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading file {download_url}: {e}")
            return False

    def find_file_in_prs(self, repo, filename, target_dir, cached_prs=None, author_filter=None):
        """
        Search for a specific filename in open PRs (or their branches) within a target directory.
        Returns the download URL if found, else None.
        """
        if cached_prs is not None:
            prs = cached_prs
        else:
            prs = self.list_pull_requests(repo, author_filter)

        if not prs:
            return None

        # Build full path
        full_path = f"{target_dir.rstrip('/')}/{filename}"

        for pr in prs:
            branch = pr['head']['ref']
            # Direct check for file existence via API
            # Note: This makes an API call per PR until found.
            # To optimize, we could list files in the PR (GET /repos/{repo}/pulls/{number}/files)
            # but that's paginated. Checking specific file existence is often faster if we know the path.

            # We must use the branch ref to get the file version in that PR
            file_info = self.get_file_info(repo, full_path, branch)
            if file_info and isinstance(file_info, dict) and file_info.get('type') == 'file':
                return file_info.get('download_url')

        return None
