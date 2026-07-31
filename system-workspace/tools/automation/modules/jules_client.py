import logging
import os
import time
from pathlib import Path
from datetime import datetime

import requests


class APIBlockError(Exception):
    """Raised when the Jules API returns a rate limit or quota exceeded response."""


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
        
        if not self.api_key:
            raise ValueError(
                "Jules API Key not found. Set JULES_API_KEY env var or check secrets/Jules_API.txt"
            )
            
        self.source_context = self._discover_source()

    def _load_api_key(self):
        """Loads API key from environment or secrets file."""
        key = os.getenv("JULES_API_KEY")
        if key:
            return key

        secrets_file = self.project_root / "secrets/Jules_API.txt"
        if secrets_file.exists():
            return secrets_file.read_text().strip()

        return None
        
    def _discover_source(self):
        """Dynamically discovers the GitHub source ID."""
        headers = {"X-Goog-Api-Key": self.api_key}
        url = "https://jules.googleapis.com/v1alpha/sources"
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            sources = resp.json().get("sources", [])
            for s in sources:
                if "ibrahim4433" in s.get("name", "") and "book-arabic-grammer" in s.get("name", ""):
                    return s["name"]
            # Fallback
            if sources:
                return sources[0]["name"]
        except Exception as e:
            logging.warning(f"⚠️ Could not discover sources dynamically: {e}")
        return "sources/github/ibrahim4433/book-arabic-grammer"

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
            if e.response is not None:
                logging.error(f"   Response: {e.response.text}")
                status = e.response.status_code
                if status in [429, 403, 400] and ("quota" in e.response.text.lower() or "limit" in e.response.text.lower() or status in [429, 403]):
                    raise APIBlockError("Jules API limit or quota reached.") from e
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

    def get_activities(self, session_id, page_size=50):
        """
        Retrieves activities for a session.
        """
        headers = {"X-Goog-Api-Key": self.api_key}
        
        session_path = session_id
        if "https" in session_path:
            session_path = session_path.split("v1alpha/")[-1]
            
        url = f"https://jules.googleapis.com/v1alpha/{session_path}/activities?pageSize={page_size}"
        
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            return resp.json().get("activities", [])
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ JulesClient Error (Get Activities): {e}")
            return []

    def send_response(self, session_id, message):
        """
        Sends a response (user input) to a session that is waiting for input.
        """
        headers = {"X-Goog-Api-Key": self.api_key, "Content-Type": "application/json"}
        
        session_path = session_id
        if "https" in session_path:
            session_path = session_path.split("v1alpha/")[-1]
            
        url = f"https://jules.googleapis.com/v1alpha/{session_path}:sendMessage"
        payload = {"prompt": message}

        try:
            logging.info(f"📤 Sending response to {session_path}...")
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            logging.info("✅ Response sent.")
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ JulesClient Error (Send Response): {e}")
            if e.response:
                logging.error(f"   Response: {e.response.text}")
            return False

    def get_latest_message(self, session_id):
        """
        Extracts the latest message/question from the agent using activities.
        """
        activities = self.get_activities(session_id)
        if not activities:
            return None
            
        # Sort activities by createTime descending (just in case they aren't ordered)
        activities.sort(key=lambda x: x.get("createTime", ""), reverse=True)
        
        for act in activities:
            if act.get("originator") == "agent" and "progressUpdated" in act:
                # Often the message to the user is in progressUpdated.description
                pu = act["progressUpdated"]
                if "description" in pu and pu["description"]:
                    return pu["description"]
                elif "title" in pu and pu["title"]:
                    return pu["title"]
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
                if state in ["FAILED", "CANCELLED"]:
                    try:
                        acts = self.get_activities(session_id)
                        if acts:
                            acts.sort(key=lambda x: x.get("createTime", ""), reverse=True)
                            for act in acts:
                                if "progressUpdated" in act and "title" in act["progressUpdated"]:
                                    logging.error(f"❌ Jules Error Detail: {act['progressUpdated']['title']} - {act['progressUpdated'].get('description', '')}")
                                    break
                    except Exception as e:
                        pass
                logging.info(f"✅ JulesClient: Session finished with state: {state}")
                return state
                
            if state in ["WAITING_FOR_INPUT", "ACTION_REQUIRED"]:
                logging.info("💬 JulesClient: Agent needs input. Auto-replying to continue...")
                self.send_response(session_id, "Please continue generating the plan strictly according to the original instructions. Do not ask for further confirmation.")
                time.sleep(10)

            time.sleep(check_interval)

        logging.error("❌ JulesClient: Monitoring timed out.")
        return "TIMEOUT"


# Quick test when running as script
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    client = JulesClient()
    logging.info("JulesClient initialized successfully.")
