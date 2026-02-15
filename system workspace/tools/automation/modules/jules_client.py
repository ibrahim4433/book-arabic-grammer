import requests
import json
import os
import time
from pathlib import Path

class JulesClient:
    """
    A robust client for the Google Jules (Code Assist) API (v1alpha).
    Handles session creation, monitoring, and error management.
    """
    
    def __init__(self, api_key=None, project_root=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.api_key = api_key or self._load_api_key()
        self.base_url = "https://jules.googleapis.com/v1alpha/sessions"
        self.source_context = "sources/github/ibrahim4433/book-arabic-grammer" # Default
        
        if not self.api_key:
            raise ValueError("Jules API Key not found. Set JULES_API_KEY env var or check secrets/Jules_API.txt")

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
        headers = {
            "X-Goog-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }
        
        payload = {
            "prompt": prompt,
            "sourceContext": {
                "source": self.source_context,
                "githubRepoContext": {
                    "startingBranch": "main"
                }
            },
            "automationMode": automation_mode,
            "title": title
        }
        
        try:
            print(f"🚀 JulesClient: Dispatching Session '{title}'...")
            resp = requests.post(self.base_url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            
            data = resp.json()
            session_id = data.get('name')
            print(f"✅ JulesClient: Session Created: {session_id}")
            return data
            
        except requests.exceptions.RequestException as e:
            print(f"❌ JulesClient Error (Create): {e}")
            if e.response:
                print(f"   Response: {e.response.text}")
            return None

    def get_session_status(self, session_id):
        """
        Retrieves the current status of a session.
        
        Args:
            session_id (str): The full session name (e.g., "sessions/wh83...").
            
        Returns:
            dict: The full session object or None on failure.
        """
        headers = {
            "X-Goog-Api-Key": self.api_key
        }
        
        # Ensure session_id is a full path if not provided
        url = f"https://jules.googleapis.com/v1alpha/{session_id}" if "https" not in session_id else session_id
        
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            return resp.json()
            
        except requests.exceptions.RequestException as e:
            print(f"❌ JulesClient Error (Get Status): {e}")
            return None

    def wait_for_completion(self, session_id, timeout_minutes=15, check_interval=30):
        """
        Polls the session until it reaches a terminal state (COMPLETED, FAILED, CANCELLED).
        
        Args:
            session_id (str): The session ID.
            timeout_minutes (int): Max wait time.
            check_interval (int): Seconds between checks.
            
        Returns:
            str: The final state (e.g., 'SUCCEEDED', 'FAILED', 'TIMEOUT').
        """
        start_time = time.time()
        end_time = start_time + (timeout_minutes * 60)
        
        print(f"⏳ JulesClient: Monitoring session {session_id} (Timeout: {timeout_minutes}m)...")
        
        while time.time() < end_time:
            status_data = self.get_session_status(session_id)
            if not status_data:
                print("⚠️ JulesClient: Could not fetch status. Retrying...")
                time.sleep(check_interval)
                continue
            
            # Extract state - API structure may vary, checking common fields
            # 'state' or 'status' field is expected in v1alpha
            state = status_data.get('state', 'UNKNOWN')
            print(f"   Status: {state}")
            
            if state in ['SUCCEEDED', 'COMPLETED', 'FAILED', 'CANCELLED']:
                print(f"✅ JulesClient: Session finished with state: {state}")
                return state
                
            time.sleep(check_interval)
            
        print("❌ JulesClient: Monitoring timed out.")
        return "TIMEOUT"

# Quick test when running as script
if __name__ == "__main__":
    client = JulesClient()
    print("JulesClient initialized successfully.")
