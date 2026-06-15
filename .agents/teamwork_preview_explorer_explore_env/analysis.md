# Environment Audit and YouTube-to-Text Design Recommendation

This analysis covers:
1. An audit of the environment and repository configuration for YouTube downloading and API keys.
2. A review of `system.py` and the automation tools codebase.
3. A detailed design recommendation for implementing the YouTube-to-Text transcription tool.

---

## 1. Environment and Tools Audit

### 1.1 Python Libraries & System Tools
- **`yt-dlp` & `pytube`**: 
  - Neither library is declared in the root `requirements.txt` (which only lists `weasyprint`, `beautifulsoup4`, `requests`, `rich`, and `questionary`).
  - To prevent import failures, `yt-dlp` should be added to the project's dependencies.
  - **Recommendation**: Use `yt-dlp` over `pytube`. `pytube` is prone to breaking due to YouTube's frequent cipher changes. `yt-dlp` is actively maintained and has robust error recovery.
- **`ffmpeg`**: 
  - Required if we need to convert downloaded audio/video streams into a specific format (e.g. `.mp3`).
  - **Fallback strategy**: If `ffmpeg` is missing in the host system, `yt-dlp` can download the native audio stream directly (e.g. `.m4a` or `.webm`). Since Gemini 1.5 Pro/Flash supports `.m4a` and `.webm` natively, the pipeline can run successfully without `ffmpeg`.
- **`gemini` CLI**:
  - The codebase (e.g. `all_pics_to_text.py` and `plan_refiner.py`) frequently invokes the `gemini` command line tool (installed via `@google/gemini-cli`).
  - In `plan_refiner.py`, text prompts and file contents are piped to the CLI via `stdin` (`cmd = ["gemini", "--prompt", "Follow context.", "--model", model, "--output-format", "text"]`).
  - For audio/video files, the CLI does not natively support stdin audio piping. A REST API-based file upload model is the most reliable approach for binary media.

### 1.2 Secrets & API Keys
We searched the `secrets/` directory and identified two keys:
1. `secrets/Jules_API.txt` (Present) - The API key for Jules AI.
2. `secrets/Github_Token.txt` (Present) - The token used for GitHub PR integration.
3. `secrets/Gemini_API.txt` (**Missing**) - There is no separate Gemini API key file.

**Key Fallback Behavior**:
In `GeminiClient` (`system-workspace/tools/automation/modules/gemini_client.py`), if `Gemini_API.txt` is missing, the code automatically falls back to `Jules_API.txt`:
```python
# Fallback to Jules key
jules_path = self.project_root / "secrets/Jules_API.txt"
if jules_path.exists():
    return jules_path.read_text().strip()
```
Therefore, `Jules_API.txt` acts as the unified API key for both Jules AI sessions and Gemini REST API queries.

---

## 2. Review of the Automation Codebase

### 2.1 State Management (`StateManager`)
- Location: `system-workspace/tools/automation/modules/state_manager.py`
- Schema structure in `project_workflow_state.json`:
  ```json
  {
    "lessons": {
      "Lesson Title": {
        "status": "OCR_DONE | PLAN_READY | PAGE_GENERATED | AUDIT_PASS",
        "files": { "raw": "...", "plan": "...", "html": "..." },
        "last_updated": 1718469138
      }
    }
  }
  ```
- **Integration Plan**: When transcribing YouTube videos, the output raw files (`Ny-raw.txt`) are not lesson files in the standard sequence. They are raw video transcriptions. However, we should record their transcription status in the state manager or a dedicated section of the state file to track downloaded and transcribed videos (e.g., matching the YouTube URL/Title to `status: "TRANSCRIBED"` and path `"raw": "system-workspace/text-data/raw/Ny-raw.txt"`).

### 2.2 Client Structures
1. **`GeminiClient`**:
   - Location: `system-workspace/tools/automation/modules/gemini_client.py`
   - Handles REST calls via `generate_content` and CLI execution via `generate_content_headless`.
   - Modifying `GeminiClient` to support the **Gemini Files API** is the cleanest method to handle audio/video uploads.
2. **`JulesClient`**:
   - Location: `system-workspace/tools/automation/modules/jules_client.py`
   - Manages developer sessions that run directly in a Git environment (modifies repository contents on branches and submits PRs).
   - Sending audio/video directly to Jules for "listening" is inefficient and not supported by the session API payload. Gemini REST API with Files API is the designated design path.

---

## 3. Design Recommendation: YouTube Transcription Pipeline

We recommend a Python-based pipeline integrated into the existing control room menu (`system.py`).

### 3.1 YouTube Downloading (`youtube_downloader.py`)
Use `yt-dlp` as a Python library to download the audio stream.

```python
import yt_dlp
from pathlib import Path

def download_youtube_audio(url, output_dir):
    """
    Downloads the audio stream from a YouTube URL.
    Attempts to extract MP3 if ffmpeg is available;
    otherwise downloads native audio format (.m4a/.webm).
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Options template
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    # Try adding ffmpeg converter to output mp3
    try:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # Find download filename
            filename = ydl.prepare_filename(info)
            # Replace extension since postprocessor converted it to mp3
            filename_path = Path(filename).with_suffix('.mp3')
            return filename_path, info.get('title', 'video')
    except Exception as e:
        # Fallback if ffmpeg is not installed on the system
        print("⚠️ ffmpeg not available. Downloading native audio stream...")
        if 'postprocessors' in ydl_opts:
            del ydl_opts['postprocessors']
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return Path(filename), info.get('title', 'video')
```

### 3.2 Gemini File Upload & Transcription
Since media files are large, we must upload them using the **Gemini Files API** before asking for content generation. We will add the following helper methods to `GeminiClient` or a new utility module:

1. **Upload File**:
   ```python
   def upload_file(self, file_path, mime_type):
       """Uploads a media file to Gemini Files API."""
       import json
       import requests
       
       url = f"https://generativelanguage.googleapis.com/upload/v1beta/files?key={self.api_key}"
       
       headers = {
           "X-Goog-Upload-Protocol": "multipart",
           "Content-Type": "application/json"
       }
       
       # Setup metadata
       metadata = {"file": {"displayName": Path(file_path).name}}
       
       # Setup multipart parts
       files = {
           "metadata": (None, json.dumps(metadata), "application/json"),
           "file": (open(file_path, "rb"), mime_type)
       }
       
       resp = requests.post(url, files=files)
       resp.raise_for_status()
       return resp.json()["file"]
   ```

2. **Poll File Status** (Ensure media processing is complete):
   ```python
   def wait_for_file_active(self, file_name):
       """Polls the status of the file until it is ACTIVE."""
       import time
       import requests
       
       url = f"https://generativelanguage.googleapis.com/v1beta/{file_name}?key={self.api_key}"
       
       while True:
           resp = requests.get(url)
           resp.raise_for_status()
           state = resp.json().get("state", "PROCESSING")
           if state == "ACTIVE":
               return True
           elif state == "FAILED":
               raise ValueError("File processing failed on Gemini server.")
           time.sleep(2)
   ```

3. **Generate Transcription**:
   ```python
   def transcribe_audio(self, file_uri, mime_type):
       """Sends file URI to Gemini for transcription with full Arabic diacritics."""
       import requests
       
       url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}"
       
       payload = {
           "contents": [{
               "parts": [
                   {
                       "text": (
                           "You are an expert Arabic transcription assistant.\n"
                           "Task: Listen to the attached audio file (which is an Arabic grammar lesson).\n"
                           "Transcribe the spoken words exactly.\n"
                           "Instructions:\n"
                           "1. Apply full diacritics (Tashkeel) to ALL Arabic text.\n"
                           "2. Do not translate. Keep the text in Arabic.\n"
                           "3. Capture both the speaker's speech and any visible/spoken text referenced.\n"
                           "4. Output ONLY the transcription. Do not add intro/outro comments or formatting metadata."
                       )
                   },
                   {
                       "file_data": {
                           "mime_type": mime_type,
                           "file_uri": file_uri
                       }
                   }
               ]
           }]
       }
       
       resp = requests.post(url, json=payload)
       resp.raise_for_status()
       return resp.json()["candidates"][0]["content"]["parts"][0]["text"]
   ```

4. **Delete File**:
   ```python
   def delete_file(self, file_name):
       """Deletes the file from Gemini storage to free space."""
       import requests
       url = f"https://generativelanguage.googleapis.com/v1beta/{file_name}?key={self.api_key}"
       requests.delete(url)
   ```

### 3.3 Playlist Processing & File Saving
The output files must be saved to `system-workspace/text-data/raw/` with the format `Ny-raw.txt`.
- When a user provides a single video URL, we determine the next unused number `N` by scanning `system-workspace/text-data/raw/` for files matching `(\d+)y-raw.txt` and incrementing the max `N`.
- When a user provides a playlist URL, `yt-dlp` extracts the playlist items. We download, upload, and transcribe them sequentially, naming them `1y-raw.txt`, `2y-raw.txt`, etc., matching the playlist sequence.

---

## 4. UI Integration in `system.py`

1. Add option `I) YouTube to Text (Video -> Raw Text)` to the interactive questionary menu.
2. When chosen, prompt the user for the YouTube URL:
   ```python
   url = questionary.text("Enter YouTube Video or Playlist URL:").ask()
   ```
3. Run the processing workflow inside a wrapper class `YouTubeWorkflow` (integrated similarly to `FullAutoWorkflow` or `JulesOCR`) that prints logs using the `Console` and `Progress` indicators.
