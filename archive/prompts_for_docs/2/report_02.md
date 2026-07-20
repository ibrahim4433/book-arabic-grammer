### `system-workspace/tools/automation/modules/youtube_ui.py`
- **Status:** Usable
- **Purpose:** A CLI user interface (using `questionary` and `rich`) for offline batch transcription of YouTube videos, applying Tashkeel to Arabic text.
- **Inputs:** Takes a YouTube URL or reads a CSV file containing URLs and titles from `input/csv-youtube/` or `Pdf-new-resource/`.
- **Outputs:** Calls `YouTubeOfflineTranscriber` to download audio and produce transcriptions (usually text/JSON files, though the actual writing is done by the transcriber module). Outputs progress tables to the terminal.
- **Usage:** ``python3 system-workspace/tools/automation/modules/youtube_ui.py``
- **Workflow Integration:** It operates independently of the '1-Plan-Per-Page' book generation workflow. It is an auxiliary tool used for gathering or processing raw data/audio before it enters the book generation pipeline.
