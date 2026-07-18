import logging
import os
import time
from pathlib import Path

import requests


class JulesClient:
    """
    A robust client for the Google Jules (Code Assist) API (v1alpha).
    Handles session creation, monitoring, and error management.
    """

    def __init__(self, api_key=None, project_root=None):
        self.project_root = (
            Path(project_root)
            if project_root
            else Path(__file__).parent.parent.parent.parent.parent
        )
        self.api_key = api_key or self._load_api_key()
        self.base_url = "https://jules.googleapis.com/v1alpha/sessions"
        self.source_context = "sources/github/ibrahim4433/book-arabic-grammer"  # Default

        if not self.api_key:
            raise ValueError(
                "Jules API Key not found. Set JULES_API_KEY env var or check secrets/Jules_API.txt"
            )

    def _load_api_key(self):
        """Loads API key from environment or secrets file."""
        key = os.getenv("JULES_API_KEY")
        if key:
            return key

        secrets_file = self.project_root / "secrets/Jules_API.txt"
        if secrets_file.exists():
            return secrets_file.read_text().strip()

        return None

    def create_session(self, prompt, title, automation_mode="AUTO_CREATE_PR"):
        """
        Creates a new Jules session.

        Args:
            prompt (str): The instruction prompt for Jules.
            title (str): A descriptive title for the session.
            automation_mode (str): 'AUTO_CREATE_PR' or 'INTERACTIVE'.

        Returns:
            dict: The session object (including 'name' i.e., session ID) or None on failure.
        """
        headers = {"X-Goog-Api-Key": self.api_key, "Content-Type": "application/json"}

        payload = {
            "prompt": prompt,
            "sourceContext": {
                "source": self.source_context,
                "githubRepoContext": {"startingBranch": "main"},
            },
            "automationMode": automation_mode,
            "title": title,
        }

        try:
            logging.info(f"🚀 JulesClient: Dispatching Session '{title}'...")
            resp = requests.post(self.base_url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()

            data = resp.json()
            session_id = data.get("name")
            logging.info(f"✅ JulesClient: Session Created: {session_id}")
            return data

        except requests.exceptions.RequestException as e:
            logging.error(f"❌ JulesClient Error (Create): {e}")
            if e.response:
                logging.error(f"   Response: {e.response.text}")
            return None

    def get_session_status(self, session_id):
        """
        Retrieves the current status of a session.

        Args:
            session_id (str): The full session name (e.g., "sessions/wh83...").

        Returns:
            dict: The full session object or None on failure.
        """
        headers = {"X-Goog-Api-Key": self.api_key}

        # Ensure session_id is a full path if not provided
        url = (
            f"https://jules.googleapis.com/v1alpha/{session_id}"
            if "https" not in session_id
            else session_id
        )

        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            return resp.json()

        except requests.exceptions.RequestException as e:
            logging.error(f"❌ JulesClient Error (Get Status): {e}")
            return None

    def send_response(self, session_id, message):
        """
        Sends a response (user input) to a session that is waiting for input.

        Args:
            session_id (str): The session ID.
            message (str): The text message to send.

        Returns:
            bool: True if successful, False otherwise.
        """
        headers = {"X-Goog-Api-Key": self.api_key, "Content-Type": "application/json"}

        # Construct URL - assuming :sendMessage or similar action
        # Based on typical patterns, it might be appending a turn or a specific action.
        # Since we don't have the spec, we will try the most common "addInput" or "sendMessage" pattern
        # for these types of agents.
        # IF THIS FAILS, we might need to adjust.

        url = f"https://jules.googleapis.com/v1alpha/{session_id}:send"
        if "https" in session_id:
            # If session_id is a URL, strip it to get base and append :send
            url = f"{session_id}:send"

        payload = {"text": message}

        try:
            logging.info(f"📤 Sending response to {session_id}...")
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            logging.info("✅ Response sent.")
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ JulesClient Error (Send Response): {e}")
            if e.response:
                logging.error(f"   Response: {e.response.text}")
            return False

    def get_latest_message(self, session_data):
        """
        Extracts the latest message/question from the session data.

        Args:
            session_data (dict): The session object from get_session_status.

        Returns:
            str: The text of the last message from the agent, or None.
        """
        # Attempt to parse 'turns' or 'messages'
        # Structure assumption: { "turns": [ { "role": "MODEL", "parts": [ { "text": "..." } ] } ] }

        if not session_data:
            return None

        turns = session_data.get("turns", [])
        if not turns:
            return None

        last_turn = turns[-1]

        # Check if it's from the Model (Agent)
        if last_turn.get("role") != "MODEL":
            return None

        parts = last_turn.get("parts", [])
        if parts and "text" in parts[0]:
            return parts[0]["text"]

        return None

    def wait_for_completion(
        self, session_id, timeout_minutes=15, check_interval=30, status_callback=None
    ):
        """
        Polls the session until it reaches a terminal state (COMPLETED, FAILED, CANCELLED).

        Args:
            session_id (str): The session ID.
            timeout_minutes (int): Max wait time.
            check_interval (int): Seconds between checks.
            status_callback (callable, optional): function(state) to call on updates.

        Returns:
            str: The final state (e.g., 'SUCCEEDED', 'FAILED', 'TIMEOUT').
        """
        start_time = time.time()
        end_time = start_time + (timeout_minutes * 60)

        logging.info(
            f"⏳ JulesClient: Monitoring session {session_id} (Timeout: {timeout_minutes}m)..."
        )

        while time.time() < end_time:
            status_data = self.get_session_status(session_id)
            if not status_data:
                logging.warning("⚠️ JulesClient: Could not fetch status. Retrying...")
                time.sleep(check_interval)
                continue

            # Extract state - API structure may vary, checking common fields
            # 'state' or 'status' field is expected in v1alpha
            state = status_data.get("state", "UNKNOWN")
            logging.info(f"   Status: {state}")

            if status_callback:
                status_callback(state)

            if state in ["SUCCEEDED", "COMPLETED", "FAILED", "CANCELLED"]:
                logging.info(f"✅ JulesClient: Session finished with state: {state}")
                return state

            time.sleep(check_interval)

        logging.error("❌ JulesClient: Monitoring timed out.")
        return "TIMEOUT"


# Quick test when running as script
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client = JulesClient()
    logging.info("JulesClient initialized successfully.")
