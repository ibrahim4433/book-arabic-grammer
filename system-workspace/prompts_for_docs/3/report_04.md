### `./system-workspace/tools/automation/modules/youtube_transcriber.py`
- **Status:** Usable
- **Purpose:** Downloads YouTube video audio via `yt-dlp`, uploads the audio file to the Google Gemini File API, and instructs the Gemini AI model to transcribe the audio into Arabic with full diacritics (Tashkeel). It handles polling the API and local file cleanup.
- **Inputs:** `url` (YouTube video URL), `sequence_n` (Optional: Sequence number for naming output file)
- **Outputs:** Saves a `.txt` transcription file in `system-workspace/text-data/video-raw/` (e.g., `1y-raw.txt`)
- **Usage:** `python -c "from modules.youtube_transcriber import YouTubeTranscriber; t = YouTubeTranscriber(api_key='YOUR_KEY', project_root='.'); t.process_url('https://www.youtube.com/watch?v=...')"`
- **Workflow Integration:** Acts as an alternative, more intelligent transcript generator (compared to the offline Mishkal version) when standard YouTube transcripts are poor or unavailable. The high-quality, AI-transcribed output becomes the raw source text that will be processed by either the old workflow or paginated for the new '1-Plan-Per-Page' workflow.
