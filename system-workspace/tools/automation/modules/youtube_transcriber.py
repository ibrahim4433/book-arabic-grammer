import os
import re
import time
import requests
import json
import yt_dlp
from pathlib import Path
from modules.gemini_client import GeminiClient

class YouTubeTranscriber:
    def __init__(self, project_root=None, api_key=None, model="gemini-1.5-flash"):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.gemini_client = GeminiClient(api_key=api_key, project_root=self.project_root)
        self.api_key = self.gemini_client.api_key
        self.model = model
        self.raw_dir = self.project_root / "system-workspace/text-data/raw"
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir = self.project_root / "output/temp_audio"
        self.temp_dir.mkdir(parents=True, exist_ok=True)

    def get_mime_type(self, filepath):
        ext = Path(filepath).suffix.lower()
        if ext == '.m4a':
            return 'audio/mp4'
        elif ext == '.webm':
            return 'audio/webm'
        elif ext == '.mp3':
            return 'audio/mpeg'
        elif ext == '.wav':
            return 'audio/wav'
        elif ext == '.ogg':
            return 'audio/ogg'
        return 'application/octet-stream'

    def upload_file(self, filepath, progress_callback=None):
        """Uploads a media file using Gemini Files API."""
        if not self.api_key:
            raise ValueError("API Key is missing. Cannot upload file to Gemini REST API.")

        url = f"https://generativelanguage.googleapis.com/upload/v1beta/files?key={self.api_key}"
        mime_type = self.get_mime_type(filepath)
        filename = Path(filepath).name
        
        headers = {
            "X-Goog-Upload-Protocol": "multipart",
        }
        
        metadata = {"file": {"displayName": filename}}
        
        if progress_callback:
            progress_callback("Uploading...")
            
        with open(filepath, "rb") as f:
            files = {
                "metadata": (None, json.dumps(metadata), "application/json"),
                "file": (filename, f, mime_type)
            }
            resp = requests.post(url, headers=headers, files=files, timeout=600)
            
        resp.raise_for_status()
        file_info = resp.json()["file"]
        return file_info["name"], file_info["uri"], mime_type

    def poll_file_status(self, file_name, progress_callback=None):
        """Polls the status of the uploaded file until it is ACTIVE."""
        if not self.api_key:
            raise ValueError("API Key is missing.")

        url = f"https://generativelanguage.googleapis.com/v1beta/{file_name}?key={self.api_key}"
        
        start_time = time.time()
        while True:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            state = data.get("state", "PROCESSING")
            
            if progress_callback:
                elapsed = int(time.time() - start_time)
                progress_callback(f"Processing ({elapsed}s, State: {state})...")
                
            if state == "ACTIVE":
                return True
            elif state == "FAILED":
                raise ValueError(f"File processing failed on Gemini server: {data.get('error', {}).get('message', 'Unknown error')}")
            
            time.sleep(3)

    def transcribe_audio_uri(self, file_uri, mime_type, progress_callback=None):
        """Sends the file URI to Gemini for transcription with diacritics."""
        if not self.api_key:
            raise ValueError("API Key is missing.")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        
        prompt = (
            "You are an expert Arabic transcription assistant.\n"
            "Task: Listen to the attached audio file (which is an Arabic grammar lesson).\n"
            "Transcribe the spoken words exactly.\n"
            "Instructions:\n"
            "1. Apply full diacritics (Tashkeel) to ALL Arabic text.\n"
            "2. Do not translate. Keep the text in Arabic.\n"
            "3. Capture both the speaker's speech and any visible/spoken text referenced.\n"
            "4. Output ONLY the transcription. Do not add intro/outro comments or formatting metadata."
        )
        
        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt},
                    {
                        "file_data": {
                            "mime_type": mime_type,
                            "file_uri": file_uri
                        }
                    }
                ]
            }],
            "generationConfig": {
                "temperature": 0.0
            }
        }
        
        if progress_callback:
            progress_callback("Transcribing...")
            
        resp = requests.post(url, headers={"Content-Type": "application/json"}, json=payload, timeout=600)
        resp.raise_for_status()
        
        result = resp.json()
        try:
            return result["candidates"][0]["content"]["parts"][0]["text"].strip()
        except (KeyError, IndexError) as e:
            raise ValueError(f"Unexpected response format from Gemini API: {result}") from e

    def delete_file(self, file_name):
        """Deletes the file from Gemini storage to free space."""
        if not self.api_key:
            return
        url = f"https://generativelanguage.googleapis.com/v1beta/{file_name}?key={self.api_key}"
        try:
            requests.delete(url, timeout=30)
        except Exception:
            pass # Best effort cleanup

    def download_audio_stream(self, url, progress_callback=None):
        """Downloads the audio stream from a YouTube URL to self.temp_dir."""
        # Setup output template
        outtmpl = str(self.temp_dir / '%(title)s.%(ext)s')
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'quiet': True,
            'no_warnings': True,
        }
        
        if progress_callback:
            progress_callback("Extracting video info...")
            
        # Try using ffmpeg audio extraction if available
        try:
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'video')
                # Find the downloaded file path
                filepath = None
                if 'requested_downloads' in info and info['requested_downloads']:
                    filepath = info['requested_downloads'][0].get('filepath')
                if not filepath or not Path(filepath).exists():
                    prep_name = ydl.prepare_filename(info)
                    p = Path(prep_name).with_suffix('.mp3')
                    if p.exists():
                        filepath = str(p)
                return filepath, title
        except Exception:
            # Fallback if ffmpeg is missing
            if progress_callback:
                progress_callback("ffmpeg conversion unavailable. Downloading native stream...")
            if 'postprocessors' in ydl_opts:
                del ydl_opts['postprocessors']
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                title = info.get('title', 'video')
                filepath = None
                if 'requested_downloads' in info and info['requested_downloads']:
                    filepath = info['requested_downloads'][0].get('filepath')
                if not filepath or not Path(filepath).exists():
                    filepath = ydl.prepare_filename(info)
                return filepath, title

    def get_next_unused_index(self):
        max_n = 0
        if self.raw_dir.exists():
            for f in self.raw_dir.glob("*y-raw.txt"):
                m = re.match(r'^(\d+)y-raw\.txt$', f.name)
                if m:
                    val = int(m.group(1))
                    if val > max_n:
                        max_n = val
        return max_n + 1

    def resolve_urls(self, url):
        """Resolves input URL to a list of (url, title) tuples."""
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
                    if not entry:
                        continue
                    v_url = entry.get('url')
                    if not v_url and 'id' in entry:
                        v_url = f"https://www.youtube.com/watch?v={entry['id']}"
                    if v_url:
                        urls.append((v_url, entry.get('title', 'video')))
                return urls, True # (urls, is_playlist)
            else:
                title = info.get('title', 'video')
                return [(url, title)], False # (urls, is_playlist)

    def process_url(self, url, sequence_n=None, progress_callback=None):
        """Downloads, uploads, polls, transcribes, saves, and cleans up for a single URL."""
        local_file = None
        gemini_file_name = None
        try:
            # 1. Download
            if progress_callback:
                progress_callback("Starting download...")
            local_file, title = self.download_audio_stream(url, progress_callback)
            if not local_file or not Path(local_file).exists():
                raise FileNotFoundError(f"Failed to locate downloaded audio file for: {url}")
                
            # 2. Upload
            if progress_callback:
                progress_callback("Uploading audio...")
            gemini_file_name, file_uri, mime_type = self.upload_file(local_file, progress_callback)
            
            # 3. Poll
            if progress_callback:
                progress_callback("Waiting for processing...")
            self.poll_file_status(gemini_file_name, progress_callback)
            
            # 4. Transcribe
            if progress_callback:
                progress_callback("Transcribing audio...")
            transcription = self.transcribe_audio_uri(file_uri, mime_type, progress_callback)
            
            # 5. Save
            if sequence_n is None:
                n = self.get_next_unused_index()
            else:
                n = sequence_n
                
            out_file = self.raw_dir / f"{n}y-raw.txt"
            out_file.write_text(transcription, encoding='utf-8')
            
            return str(out_file), title
            
        finally:
            # 6. Cleanup
            if local_file and Path(local_file).exists():
                try:
                    os.remove(local_file)
                except Exception:
                    pass
            if gemini_file_name:
                self.delete_file(gemini_file_name)
