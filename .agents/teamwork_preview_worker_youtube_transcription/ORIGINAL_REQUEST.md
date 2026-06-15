## 2026-06-15T16:54:33Z

You are teamwork_preview_worker.
Your role: Implementation Worker.
Your working directory: /mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/.agents/teamwork_preview_worker_youtube_transcription/

You are tasked with implementing the YouTube-to-Text video processing and transcription pipeline.

Please review the explorer's reports at:
- Analysis: `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/.agents/teamwork_preview_explorer_explore_env/analysis.md`
- Handoff: `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer/.agents/teamwork_preview_explorer_explore_env/handoff.md`

Requirements:
1. Update `requirements.txt` to include `yt-dlp`. Install `yt-dlp` in the environment so it is available.
2. Implement the downloading and transcription logic. You can create a new module `system-workspace/tools/automation/modules/youtube_transcriber.py` (and/or extend `GeminiClient` in `gemini_client.py`).
   - Use `yt-dlp` to download the audio stream (e.g. in `.m4a` or `.webm` format so it does not strictly depend on `ffmpeg` if not present, but use mp3/m4a/webm as appropriate).
   - Use the Gemini REST Files API to upload the downloaded audio file, poll until the state is 'ACTIVE', transcribe the audio file using `gemini-1.5-flash` or `gemini-1.5-pro` (using `Jules_API.txt` as the API key, matching `GeminiClient`'s fallback logic), and delete the uploaded file from Gemini storage when done.
   - The prompt for Gemini must specify to transcribe the Arabic audio with FULL tashkeel (diacritics).
   - Save the raw transcribed scripts to `system-workspace/text-data/raw/Ny-raw.txt` (where N is the sequence number).
   - If a playlist or multiple links are supplied, they should be processed sequentially and saved as `1y-raw.txt`, `2y-raw.txt`, etc.
   - If a single YouTube URL is supplied, scan `system-workspace/text-data/raw/` for existing `(\d+)y-raw.txt` files to find the next unused number N.
3. Integrate the YouTube-to-Text workflow as a new menu option in `system.py`:
   - Add Option `I) YouTube to Text (Video -> Raw Text)` to the interactive questionary menu.
   - Ask the user for the YouTube URL (single video or playlist).
   - Display a nice UI/progress using `Console`/`Progress` indicating download, upload, transcription status, and output paths.
4. Verify your implementation by running a test script or command. You should write a test script that downloads and transcribes a very short YouTube video (or mocks it if network/sandbox limits prevent external downloads, but try genuine execution first). Ensure that `system.py` compiles and runs.
5. Write a handoff report (`handoff.md`) in your working directory summarizing what was changed, build/test commands run, and verification results.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
