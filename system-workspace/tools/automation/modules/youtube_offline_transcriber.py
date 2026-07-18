import random
import re
import threading
import time
from pathlib import Path

import mishkal.tashkeel
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter


class YouTubeOfflineTranscriber:
    """
    Handles the offline extraction of YouTube transcripts and applying Arabic diacritics using Mishkal.
    Bypasses yt-dlp to avoid 403 Forbidden errors.
    """

    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.output_dir = self.project_root / "system-workspace" / "text-data" / "video-raw"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.formatter = TextFormatter()
        self.local_data = threading.local()

    def get_vocalizer(self):
        if not hasattr(self.local_data, "vocalizer"):
            self.local_data.vocalizer = mishkal.tashkeel.TashkeelClass()
        return self.local_data.vocalizer

    def extract_video_id(self, url):
        """Extracts the video ID from a standard YouTube URL."""
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
        if match:
            return match.group(1)
        return None

    def process_video(self, url, title, seq_num):
        """
        Fetches the transcript, adds Tashkeel, and saves to file.
        Returns (success_bool, message)
        """
        video_id = self.extract_video_id(url)
        if not video_id:
            return False, f"Invalid YouTube URL: {url}"

        # Clean title for filename
        clean_title = re.sub(r'[\\/*?:"<>|]', "", title)
        clean_title = clean_title.replace(" ", "_")
        if len(clean_title) > 50:
            clean_title = clean_title[:50]

        filename = f"{seq_num}-{clean_title}-video-raw.txt"
        output_path = self.output_dir / filename

        # If it already exists, skip
        if output_path.exists():
            return True, f"Skipped (Already exists): {filename}"

        try:
            # 1. Fetch Transcript with Retry Logic
            api = YouTubeTranscriptApi()
            transcript_list = None
            max_retries = 3

            for attempt in range(max_retries):
                try:
                    # Random stagger to avoid concurrent burst
                    time.sleep(random.uniform(1.0, 3.0))
                    transcript_list = api.list(video_id)
                    break
                except Exception as e:
                    if "YouTube is blocking requests" in str(e) and attempt < max_retries - 1:
                        time.sleep(random.uniform(5.0, 10.0))  # Backoff
                        continue
                    raise e

            # Try to get Arabic transcript first
            try:
                transcript = transcript_list.find_transcript(["ar"])
            except Exception:
                # Fallback to auto-translated or any available
                return False, "No Arabic transcript found for this video."

            text = self.formatter.format_transcript(transcript.fetch())

            # 2. Apply Tashkeel using Mishkal
            vocalizer = self.get_vocalizer()

            # Mishkal has a hard limit of 10,000 characters per call, so we chunk the text
            chunk_size = 5000
            text_vocalized = ""
            for i in range(0, len(text), chunk_size):
                chunk = text[i : i + chunk_size]
                text_vocalized += vocalizer.tashkeel(chunk)

            # 3. Save to File
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text_vocalized)

            return True, f"Successfully processed: {filename}"

        except Exception as e:
            return False, f"Error processing {video_id}: {e!s}"
