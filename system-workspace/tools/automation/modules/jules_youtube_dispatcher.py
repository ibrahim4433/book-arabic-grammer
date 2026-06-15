import time
import yt_dlp
import re
from pathlib import Path
from modules.jules_client import JulesClient

class JulesYouTubeDispatcher:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.jules_client = JulesClient(project_root=self.project_root)
        
    def resolve_urls(self, url):
        ydl_opts = {
            'extract_flat': True,
            'quiet': True,
            'no_warnings': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if info.get('_type') == 'playlist' or 'entries' in info:
                entries = info.get('entries', [])
                urls = []
                for entry in entries:
                    if not entry: continue
                    v_url = entry.get('url')
                    if not v_url and 'id' in entry:
                        v_url = f"https://www.youtube.com/watch?v={entry['id']}"
                    if v_url:
                        urls.append((v_url, entry.get('title', 'video')))
                return urls, True
            else:
                title = info.get('title', 'video')
                return [(url, title)], False

    def sanitize_title(self, title):
        # Keep alphanumeric, Arabic chars, spaces, and hyphens
        clean = re.sub(r'[^\w\s\u0600-\u06FF-]', '', title)
        return clean.strip().replace(' ', '_')

    def build_prompt(self, video_url, video_title, seq_num=None):
        clean_title = self.sanitize_title(video_title)
        n_prefix = f"{seq_num}-" if seq_num else ""
        out_filename = f"{n_prefix}{clean_title}-video-raw.txt"
        
        prompt = f"""
# TASK: YouTube Video Processing and Transcription

You are required to process a YouTube video and transcribe its content (audio speech and any on-screen text) into an easy-to-read, accurate raw text document. 

**Target Video URL**: {video_url}
**Target Output File**: `system-workspace/text-data/video-raw/{out_filename}`

## Instructions:
1. **Prepare Dependencies**:
   First, ensure `ffmpeg` is installed so you can extract audio/frames if needed.
   Run: `sudo apt-get update && sudo apt-get install -y ffmpeg`

2. **Download the Media**:
   We have provided a local utility for you. Run the following command in the terminal:
   `python Jules-workspace/yt_downloader.py "{video_url}" --audio-only`
   *(If you prefer to extract video frames as well, you can run it with `--extract-frames`, but audio is usually sufficient for transcription).*

3. **Process and Transcribe**:
   - Use your AI capabilities to "listen" or "watch" the downloaded media file.
   - Transcribe the audio exactly in Arabic.
   - Apply full diacritics (Tashkeel) to ALL Arabic text.
   - Do NOT translate. Keep the text in Arabic.
   - Do NOT generate HTML templates. Do not use `TEMPLATE_C_BLOCK` or any other book templates. The output must be pure raw text.

4. **Save the Result**:
   Save the raw transcription text to:
   `system-workspace/text-data/video-raw/{out_filename}`
   Create the directory if it does not exist.

5. **Cleanup**:
   DELETE the downloaded media file (e.g., `output/temp_media/*.mp3` or `.mp4`) before finalizing the PR so you do not bloat the repository with media files. Only commit the raw text file!

CRITICAL: ONLY submit the PR with the `.txt` file. Ensure the media file is deleted.
"""
        return prompt.strip()

    def dispatch_session(self, video_url, video_title, seq_num=None, progress_callback=None):
        prompt = self.build_prompt(video_url, video_title, seq_num)
        clean_title = self.sanitize_title(video_title)
        n_prefix = f"{seq_num}-" if seq_num else ""
        session_title = f"YT-Process-{n_prefix}{clean_title}"[:60]
        
        if progress_callback:
            progress_callback(f"Dispatching Jules Session: {session_title}")
            
        session = self.jules_client.create_session(prompt, session_title, automation_mode="AUTO_CREATE_PR")
        if not session:
            raise Exception("Failed to create Jules session.")
            
        return session.get('name')
