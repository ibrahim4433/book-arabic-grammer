### `system-workspace/tools/automation/modules/gemini_client.py`
- **Status:** Usable
- **Purpose:** A generic client for the Google Gemini API supporting both REST API (with keys) and a Headless CLI mode (no keys, using the `gemini` command line tool). It handles model fallback chains and image inputs.
- **Inputs:** API keys.
- **Outputs:** Text responses from the Gemini API.
- **Usage:** Used as a library class `GeminiClient(api_key=...)`.
- **Workflow Integration:** This is a foundational utility used by `planner.py` and `text_processing.py`. It ensures stable AI communication for whichever workflow is active.
