# Project Plan: YouTube to Arabic Text Transcription Tool

## Architecture
- **Input**: YouTube Video or Playlist URL.
- **Processing**:
  - Download audio (or video) from YouTube using a Python library (e.g., `yt-dlp` or similar).
  - Use ffmpeg to convert/compress audio if needed to meet API limits.
  - Transcribe the audio/video file using Gemini API or `gemini` CLI.
  - Generate the Arabic transcript containing voice narration and on-screen text.
- **Output**: Save the transcribed script to `system-workspace/text-data/raw/Ny-raw.txt` (where N is the sequence number).
- **UI Integration**: Add a menu option "I) YouTube to Text (Video -> Raw Text)" inside `system.py`.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| 1 | Exploration & Environment Audit | Check available Python packages, tools (ffmpeg, yt-dlp), secrets/keys, and YouTube video/audio download capabilities. | None | DONE |
| 2 | YouTube Download & Processing Module | Implement a Python module to download YouTube videos/audio as local files. | M1 | DONE |
| 3 | Gemini Transcription Module | Implement transcription using Gemini API or CLI, uploading the audio and asking for an Arabic transcript. | M2 | DONE |
| 4 | Integration & Control Room UI | Integrate the tool into `system.py` with menu option I. | M3 | DONE |
| 5 | E2E Testing & Acceptance | Run test cases on a test video and verify generated raw file format/naming and correct execution. | M4 | DONE |
