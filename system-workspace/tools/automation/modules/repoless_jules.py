import os
import time
import requests
import json
import logging

class RepolessJulesClient:
    """
    A stateless, repoless client for the Jules API that acts like an LLM.
    Uses polling to wait for the agent's message.
    """
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("JULES_API_KEY")
        if not self.api_key:
            # Fallback to secrets file
            secrets_path = os.path.join(
                os.path.dirname(__file__), "../../../../secrets/Jules_API.txt"
            )
            if os.path.exists(secrets_path):
                with open(secrets_path, "r") as f:
                    self.api_key = f.read().strip()
        
        if not self.api_key:
            raise ValueError("JULES_API_KEY not found.")
            
        self.base_url = "https://jules.googleapis.com/v1alpha"
        self.session_id = None
        self.expected_responses = 0

    def generate_content(self, prompt, system_instruction=""):
        full_prompt = f"{system_instruction}\n\n{prompt}"
        
        headers = {
            "X-Goog-Api-Key": self.api_key,
            "Content-Type": "application/json"
        }
        
        if not self.session_id:
            payload = {
                "title": "Repoless Chunking",
                "prompt": full_prompt,
                "requirePlanApproval": False
            }
            logging.info("Creating repoless Jules session...")
            create_resp = requests.post(f"{self.base_url}/sessions", json=payload, headers=headers)
            
            if create_resp.status_code != 200:
                raise Exception(f"Failed to create session: {create_resp.text}")
                
            session_data = create_resp.json()
            self.session_id = session_data.get("name")
            if not self.session_id:
                raise Exception("No session ID returned.")
            self.expected_responses = 1
            logging.info(f"Session created: {self.session_id}. Polling for response...")
        else:
            payload = {"prompt": full_prompt}
            # Extract just the session path if it contains the full url
            session_path = self.session_id
            if "https" in session_path:
                session_path = session_path.split("v1alpha/")[-1]
                
            url = f"{self.base_url}/{session_path}:sendMessage"
            logging.info(f"Reusing session {session_path}. Sending message...")
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code != 200:
                raise Exception(f"Failed to send message to existing session: {resp.text}")
            self.expected_responses += 1
            logging.info(f"Message sent. Polling for response #{self.expected_responses}...")
        
        # Poll activities
        activities_url = f"{self.base_url}/{self.session_id}/activities"
        
        max_retries = 180 # 6 minutes to allow Jules time to process massive 3,000+ line texts
        for _ in range(max_retries):
            time.sleep(2)
            try:
                act_resp = requests.get(activities_url, headers=headers)
                if act_resp.status_code == 404:
                    continue # Eventual consistency
                if act_resp.status_code == 200:
                    activities_data = act_resp.json()
                    activities = activities_data.get("activities", [])
                    
                    # Find all agent responses
                    agent_messages = [act for act in activities if "agentMessaged" in act]
                    
                    if len(agent_messages) >= self.expected_responses:
                        # Ensure we get the absolute latest message
                        agent_messages.sort(key=lambda x: x.get("createTime", ""), reverse=True)
                        latest_act = agent_messages[0]
                        msg = latest_act["agentMessaged"].get("agentMessage", latest_act.get("description", ""))
                        return self._clean_json(msg)
            except Exception as e:
                logging.error(f"Polling error: {e}")
                
        raise Exception("Timeout waiting for Jules response.")
        
    def _clean_json(self, raw_str):
        raw_str = raw_str.strip()
        if raw_str.startswith("```json"):
            raw_str = raw_str[7:]
        if raw_str.startswith("```"):
            raw_str = raw_str[3:]
        if raw_str.endswith("```"):
            raw_str = raw_str[:-3]
        return raw_str.strip()
