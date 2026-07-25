# Module 16: The AI Communication Layer (`gemini_client.py`)

## 1. Tool Definition
**What is it?** 
The entire automation suite relies on Google Gemini to generate HTML, plan lessons, and read images via OCR. But communicating with an LLM over a network is inherently unstable. Rate limits are hit, quotas are exhausted, and API keys expire. 

`system-workspace/tools/automation/modules/gemini_client.py` is a bulletproof HTTP client designed to ensure the system *never* crashes due to an AI failure. It intelligently switches between REST APIs and local CLI tools, and features a "Fallback Chain" that automatically downgrades to cheaper AI models if the premium models exhaust their quota.

## 2. I/O Mapping
*   **Inputs:** 
    *   System Prompt strings.
    *   User Content strings.
    *   Local Image Paths (for OCR).
*   **Processes:**
    *   Searches the hard drive for API keys.
    *   Base64 encodes images to send over HTTP.
    *   If the REST API hits a `429 Too Many Requests` error, it intercepts the crash, opens a subprocess, and pipes the prompt into the official `@google/gemini-cli` Node.js tool instead.
*   **Outputs:**
    *   A clean string containing the AI's response.

---

## 3. The Deep Dive: Codebase Analysis

Below is an exhaustive, 100% codebase breakdown of the Gemini Client.

### Block A: State Management & API Key Loading
The client must hold its state globally across the entire application so that if one thread exhausts the API quota, the other threads immediately know to switch models.

```python
# From system-workspace/tools/automation/modules/gemini_client.py

9: class GeminiClient:
10:     """
11:     A generic client for the Google Gemini API.
12:     Handles authentication and content generation (Text & Vision).
13:     Supports both REST API (with Key) and Headless CLI (No Key).
14:     """
15: 
16:     # Class-level variables to share state across all instances in the session
17:     models_chain = [
18:         "gemini-3-pro-preview",
19:         "gemini-2.5-pro",
20:         "gemini-3-flash-preview",
21:         "gemini-2.5-flash",
22:         "gemini-2.5-flash-lite",
23:     ]
24:     current_model_index = 0
...
38:     def _load_api_key(self):
39:         """Loads API key from environment, Gemini_API.txt, or Jules_API.txt."""
40:         key = os.getenv("GEMINI_API_KEY")
41:         if key:
42:             return key
43: 
44:         # Try Gemini specific key
45:         gemini_path = self.project_root / "secrets/Gemini_API.txt"
46:         if gemini_path.exists():
47:             return gemini_path.read_text().strip()
48: 
49:         # Fallback to Jules key
50:         jules_path = self.project_root / "secrets/Jules_API.txt"
51:         if jules_path.exists():
52:             return jules_path.read_text().strip()
53: 
54:         return None
```
#### Line-by-Line Commentary
*   **Lines 16-24:** Notice that `models_chain` and `current_model_index` are declared *outside* of `__init__`. In Python, this makes them Class Attributes, shared across *every single instance* of `GeminiClient`. If thread 3 triggers a downgrade to `gemini-2.5-pro`, thread 4 will instantly use the new model on its next call.
*   **Lines 40-52:** The key loader is highly redundant. It checks the OS Environment Variables first (best practice for CI/CD), then checks two different localized `.txt` files in a `secrets/` folder.

### Block B: REST API Generation & Image Handling
This is the primary communication method. It is fast, lightweight, and supports structured JSON responses.

```python
# From system-workspace/tools/automation/modules/gemini_client.py

56:     def generate_content(self, system_instruction, user_content, images=None, response_schema=None):
57:         """
58:         Generates content using Gemini REST API.
59:         """
60:         if self.use_headless or not self.api_key:
61:             print("⚠️ API Key missing or Headless mode requested. Switching to Headless CLI...")
62:             return self.generate_content_headless(
63:                 system_instruction + "\n\n" + user_content, images=images
64:             )
...
72:         # Process Images
73:         if images:
74:             for img_path in images:
75:                 img_path = Path(img_path)
76:                 if not img_path.exists():
77:                     print(f"⚠️ Image not found: {img_path}")
78:                     continue
79: 
80:                 try:
81:                     with open(img_path, "rb") as image_file:
82:                         encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
83: 
84:                     mime_type = "image/jpeg"
85:                     if img_path.suffix.lower() == ".png":
86:                         mime_type = "image/png"
87:                     elif img_path.suffix.lower() == ".webp":
88:                         mime_type = "image/webp"
89: 
90:                     parts.append({"inline_data": {"mime_type": mime_type, "data": encoded_string}})
91:                 except Exception as e:
92:                     print(f"❌ Error reading image {img_path}: {e}")
93: 
94:         payload = {"contents": [{"parts": parts}], "generationConfig": {"temperature": 0.0}}
...
101:         try:
102:             resp = requests.post(
103:                 url, headers={"Content-Type": "application/json"}, json=payload, timeout=120
104:             )
105:             resp.raise_for_status()
106:             result = resp.json()
107:             return result["candidates"][0]["content"]["parts"][0]["text"]
108: 
109:         except requests.exceptions.RequestException as e:
110:             status_code = getattr(e.response, "status_code", None)
111:             print(f"❌ Gemini API Failed (Status: {status_code}): {e}")
112: 
113:             # Fallback for authentication or quota errors
114:             if status_code in [401, 403, 429] or not self.api_key:
115:                 print("🔄 Falling back to Headless CLI...")
116:                 return self.generate_content_headless(full_prompt, images)
117:             return ""
```
#### Line-by-Line Commentary
*   **Lines 60-64:** An immediate circuit-breaker. If the user forgot to add an API key, the script doesn't crash. It reroutes the data to the local node.js Headless CLI tool.
*   **Lines 81-82:** `base64.b64encode(...)`
    *   You cannot send raw JPG binaries inside a JSON packet. The client must physically convert the binary image into a Base64 string before appending it to the HTTP payload.
*   **Line 94:** `"temperature": 0.0`
    *   Strictly enforced. The AI must be deterministic for coding and typesetting.
*   **Lines 114-116:** *The Ultimate Safety Net*. If Google's servers return a `429 Too Many Requests` (Quota Exhausted) or `403` (Bad API Key), the `except` block catches it and immediately reroutes the exact same prompt to the Headless fallback engine.

### Block C: Headless CLI Fallback Chain
If the HTTP API fails, the script uses Python's `subprocess` library to secretly type commands into a locally installed CLI tool, reading the terminal output to get the AI's response.

```python
# From system-workspace/tools/automation/modules/gemini_client.py

122:     def generate_content_headless(self, full_prompt, images=None):
...
132:         # Start from the current successful model index
133:         for i in range(GeminiClient.current_model_index, len(GeminiClient.models_chain)):
134:             model = GeminiClient.models_chain[i]
135:             result_text = self._run_cli(full_prompt, model)
136: 
137:             if result_text:
138:                 if i != GeminiClient.current_model_index:
139:                     print(f"🔄 Switched to model '{model}' for this session.")
140:                 GeminiClient.current_model_index = i
141:                 return result_text
142: 
143:             print(f"⚠️ Model '{model}' failed or quota exhausted. Trying next in chain...")
144: 
145:         print("❌ All models in the fallback chain failed.")
146:         return ""
...
148:     def _run_cli(self, full_prompt, model):
149:         """Helper to run the CLI command."""
150:         try:
151:             print(f"⏳ Running Gemini CLI (Model: {model})...")
152:             # The CLI requires -p/--prompt to trigger non-interactive mode.
153:             cmd = [
154:                 "gemini",
155:                 "--prompt",
156:                 "Process input from stdin.",
157:                 "--model",
158:                 model,
159:                 "--output-format",
160:                 "text",
161:             ]
162: 
163:             result = subprocess.run(
164:                 cmd,
165:                 input=full_prompt,
166:                 capture_output=True,
167:                 text=True,
168:                 encoding="utf-8",
169:                 check=False,
170:                 timeout=300,  # 5 minutes timeout to prevent indefinite hangs
171:             )
...
177:             return result.stdout.strip()
178: 
179:         except subprocess.TimeoutExpired:
180:             print(f"❌ Gemini CLI Timeout ({model}) after 300s.")
181:             return ""
```
#### Line-by-Line Commentary
*   **Lines 133-146:** *The Fallback Loop*. It attempts to run the CLI with `gemini-3-pro-preview`. If the CLI fails, the loop advances `i`, and instantly retries the prompt with `gemini-2.5-pro`, working its way down all the way to `gemini-2.5-flash-lite`.
*   **Lines 153-161:** Prepares the exact bash command. The `--prompt "Process input from stdin."` flag tells the Node.js tool to expect a massive block of text piped into it, rather than waiting for human typing.
*   **Lines 163-171:** `subprocess.run(..., input=full_prompt)`
    *   This executes the bash command and pipes the prompt directly into the standard input stream.
    *   `timeout=300`: If the CLI hangs and stops responding for 5 minutes, Python physically kills the subprocess to prevent memory leaks and returns an empty string.

### Review
You have successfully dissected `gemini_client.py`. You now understand HTTP fallback handling, Base64 image encoding, Class-level state sharing, and `subprocess` piping!
