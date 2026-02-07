import requests
import base64
import os

api_key = "" 
url = "https://jules.googleapis.com/v1alpha/sessions"

with open("input/1.jpg", "rb") as f:
    img_data = base64.b64encode(f.read()).decode("utf-8")

payload = {
    "prompt": "Extract text from this image.",
    "sourceContext": {
        "githubRepo": {"name": "ibrahim4433/book-arabic-grammer"}
    },
    "config": {
        "tools": ["EDIT_CODE"]
    }
}

# Try adding an image part if Jules supports it
# Since Jules is built on Gemini, maybe it uses the same multi-part structure?
# Let's try the standard 'prompt' first, then try 'contents'.

headers = {
    "X-Goog-Api-Key": api_key,
    "Content-Type": "application/json"
}

print("Trying standard prompt...")
resp = requests.post(url, headers=headers, json=payload)
print(f"Status: {resp.status_code}")
print(f"Response: {resp.text}")
