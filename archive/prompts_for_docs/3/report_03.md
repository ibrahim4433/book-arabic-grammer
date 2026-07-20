### `./system-workspace/tools/automation/modules/youtube_offline_transcriber.py`
- **Status:** Usable
- **Purpose:** Extracts YouTube transcripts directly via the `youtube_transcript_api` (bypassing `yt-dlp` to avoid 403 errors), prioritizing Arabic transcripts. It then applies full Arabic diacritics (Tashkeel) using the local Mishkal library and saves the output to a raw text file.
- **Inputs:** `url` (YouTube video URL), `title` (Video title for naming), `seq_num` (Sequence number for naming)
- **Outputs:** Saves a `.txt` file containing the diacritized transcript in `system-workspace/text-data/video-raw/`
- **Usage:** `python -c "from modules.youtube_offline_transcriber import YouTubeOfflineTranscriber; t = YouTubeOfflineTranscriber('.'); t.process_video('https://www.youtube.com/watch?v=...', 'Title', 1)"`
- **Workflow Integration:** Can be used to gather raw text content. The generated raw text files will later be sliced using `----- PAGE X -----` markers to feed the '1-Plan-Per-Page' engine, ensuring the AI agent receives perfectly diacritized Arabic source material for its page generation tasks.
