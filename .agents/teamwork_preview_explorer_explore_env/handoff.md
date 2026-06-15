# Handoff Report

## 1. Observation
- **Required Libraries**: Under `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/requirements.txt`, the contents are:
  ```text
  weasyprint
  beautifulsoup4
  requests
  rich
  questionary
  ```
  No mention of `yt-dlp` or `pytube`.
- **API Keys**: Under `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/secrets/`, the files found are:
  - `Github_Token.txt`
  - `Jules_API.txt`
  No `Gemini_API.txt` exists.
- **Client Fallback Logic**: In `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/system-workspace/tools/automation/modules/gemini_client.py` lines 37-45:
  ```python
  # Try Gemini specific key
  gemini_path = self.project_root / "secrets/Gemini_API.txt"
  if gemini_path.exists():
      return gemini_path.read_text().strip()
      
  # Fallback to Jules key
  jules_path = self.project_root / "secrets/Jules_API.txt"
  if jules_path.exists():
      return jules_path.read_text().strip()
  ```
- **CLI Commands Usage**: In `system-workspace/tools/automation/plan_refiner.py` lines 45:
  ```python
  cmd = ["gemini", "--prompt", "Follow context.", "--model", model, "--output-format", "text"]
  ```
  Passing text context via standard input.
- **State Management**: In `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/system-workspace/tools/automation/modules/state_manager.py` lines 10-18:
  ```python
  {
    "lessons": {
      "Lesson Title": {
          "status": "OCR_DONE | PLAN_READY | PAGE_GENERATED | AUDIT_PASS",
          "files": { "raw": "...", "plan": "...", "html": "..." },
          "last_updated": timestamp
      }
    }
  }
  ```

## 2. Logic Chain
- Since `requirements.txt` does not declare `yt-dlp` or `pytube`, we need to install the chosen downloading library manually or add it to the requirements.
- `yt-dlp` is actively maintained, unlike `pytube`, making it the correct choice to handle YouTube cipher updates.
- In `GeminiClient`, since `Gemini_API.txt` is missing, the fallback chain ensures `Jules_API.txt` is loaded and used as the authorization key for all Gemini REST API calls.
- The `gemini` CLI tool handles text inputs via standard input, but does not natively support standard input audio stream parsing. Therefore, uploading audio/video streams requires the Gemini REST Files API (`/upload/v1beta/files`), which can be called via Python's `requests` library using the API key from `Jules_API.txt`.
- Output raw transcription files need to be saved sequentially inside `system-workspace/text-data/raw/` under the format `Ny-raw.txt`.

## 3. Caveats
- Since the terminal execution permission prompt timed out, the existence of `ffmpeg`, `yt-dlp` CLI, and `gemini` CLI in the host system's PATH could not be verified programmatically. We assume the implementation agent will verify their presence locally or add installation instructions.
- We assume that `Jules_API.txt` has permission to access the Gemini API (specifically `gemini-1.5-flash` or `gemini-1.5-pro` models).

## 4. Conclusion
- A design using Python's `yt-dlp` library to download native audio streams (e.g. `.m4a` or `.webm`) is recommended. This avoids an absolute dependency on `ffmpeg` for transcoding since Gemini natively supports these audio MIME types.
- The Gemini REST Files API (`https://generativelanguage.googleapis.com/upload/v1beta/files`) should be used to upload downloaded files, poll their status, generate transcribed Arabic text (with full Tashkeel), and delete the uploaded files from Gemini cloud storage upon completion.
- Sequential files (`Ny-raw.txt`) should be saved in `system-workspace/text-data/raw/` and the system control menu in `system.py` should be updated with a new option `I`.

## 5. Verification Method
- Inspect the design report generated at `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/.agents/teamwork_preview_explorer_explore_env/analysis.md`.
- Invalidation condition: If the Gemini Files API does not support file upload via `multipart/form-data` with `Jules_API.txt`, or if the REST API restricts usage of Jules keys for Generative Language Files API endpoints.
